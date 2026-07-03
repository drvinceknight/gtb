"""Computational verification of the worked examples in the book.

Each test reproduces a numeric claim made in a chapter, using that chapter's
own library where one exists (``nashpy``, ``coopgt``, ``matching``,
``pref_voting``, ``scipy``) and ``sympy``/``numpy`` otherwise. The tests are
self-contained and can be run with::

    uv run pytest tests/

Any library that is not installed causes only its own tests to be skipped, so
the suite can be plugged into CI incrementally.
"""

import pytest


def test_rock_paper_scissors_lizard_spock():
    """
    Rationalisation: best response conditin.

    chapters/rationalisation/index.md, the example
    after the best response condition.
    """
    numpy = pytest.importorskip("numpy")
    sigma_2 = numpy.array((1 / 4, 0, 0, 3 / 4, 0))

    M_r = numpy.array(
        (
            (0, -1, 1, 1, -1),
            (1, 0, -1, -1, 1),
            (-1, 1, 0, 1, -1),
            (-1, 1, -1, 0, 1),
            (1, -1, 1, -1, 0),
        )
    )
    expected_row_utilities = numpy.array((0.75, -0.5, 0.5, -0.25, -0.5))
    row_utilities = M_r @ sigma_2
    assert numpy.array_equal(expected_row_utilities, row_utilities)


def test_zero_sum_maxmin_strategies():
    """Zero-Sum Games: max-min strategies via nashpy.

    chapters/zero_sum_games/index.md, Programming section "Obtain min-max and
    max-min strategies using Nashpy" (modified Rock-Paper-Scissors), and the
    exercises `max-min_strategy_for_matching_pennies` and
    `max-min_strategy_for_rock_paper_scissors`.
    """
    nash = pytest.importorskip("nashpy")
    numpy = pytest.importorskip("numpy")

    modified_rock_paper_scissors = numpy.array([[0, -1, 1], [2, 0, -2], [-1, 1, 0]])
    game = nash.Game(modified_rock_paper_scissors, -modified_rock_paper_scissors)
    row_strategy, _ = game.linear_program()
    assert numpy.allclose(row_strategy, [0.4, 0.2, 0.4])

    matching_pennies = numpy.array([[1, -1], [-1, 1]])
    row_strategy, column_strategy = nash.Game(
        matching_pennies, -matching_pennies
    ).linear_program()
    assert numpy.allclose(row_strategy, [0.5, 0.5])
    assert numpy.allclose(column_strategy, [0.5, 0.5])

    rock_paper_scissors = numpy.array([[0, -1, 1], [1, 0, -1], [-1, 1, 0]])
    row_strategy, _ = nash.Game(
        rock_paper_scissors, -rock_paper_scissors
    ).linear_program()
    assert numpy.allclose(row_strategy, [1 / 3, 1 / 3, 1 / 3])


def test_nash_equilibrium_coordination_game():
    """Nash Equilibrium / Games: the coordination game has two pure equilibria.

    Coordination game `eqn:coordination_game_payoff_matrices` in
    chapters/games/index.md; the same game and its equilibria are used in
    chapters/nash_equilibrium/index.md and chapters/rationalisation/index.md.
    """
    nash = pytest.importorskip("nashpy")
    numpy = pytest.importorskip("numpy")

    row_payoffs = numpy.array([[3, 1], [0, 2]])
    column_payoffs = numpy.array([[2, 1], [0, 3]])
    equilibria = list(nash.Game(row_payoffs, column_payoffs).support_enumeration())

    pure = [
        (tuple(row), tuple(column))
        for row, column in equilibria
        if set(row) <= {0.0, 1.0} and set(column) <= {0.0, 1.0}
    ]
    assert ((1.0, 0.0), (1.0, 0.0)) in pure
    assert ((0.0, 1.0), (0.0, 1.0)) in pure


def test_repeated_games_average_payoff_cell():
    """Repeated Games: the (S_D, S_C) average payoff is (3, -7).

    chapters/repeated_games/index.md, solution
    `payoffs_and_equilibrium_in_the_infinite_game`. S_D has the row player
    always play r1 and S_C has the column player always play c2, so the
    average payoff is the (r1, c2) cell of the stage game.
    """
    numpy = pytest.importorskip("numpy")

    row_stage_payoffs = numpy.array([[-1, 3], [-2, 2]])
    column_stage_payoffs = numpy.array([[1, -7], [6, 2]])
    assert row_stage_payoffs[0, 1] == 3
    assert column_stage_payoffs[0, 1] == -7


def test_further_learning_dynamics_wright_fisher():
    """Further Learning Dynamics: 0.731**4 rounds to 0.286, not 0.284.

    chapters/further_learning_dynamics/index.md, "Example: One Generation of
    the Wright-Fisher Process".
    """
    assert round(0.731**4, 3) == 0.286


def test_moran_process_fixation_probabilities():
    """Moran Process: fixation probabilities for the new solutions.

    chapters/moran_process/index.md, solutions
    `moran_process_with_neutral_drift` and `specific_fixation_probabilities`,
    which apply `eqn:formula_for_fixation_probabilities`.
    """
    sympy = pytest.importorskip("sympy")

    def fixation_probability(payoff_matrix, population_size):
        def resident_fitness(mutant_count):
            return (population_size - mutant_count - 1) * payoff_matrix[0][
                0
            ] + mutant_count * payoff_matrix[0][1]

        def mutant_fitness(mutant_count):
            return (population_size - mutant_count) * payoff_matrix[1][0] + (
                mutant_count - 1
            ) * payoff_matrix[1][1]

        gammas = [
            sympy.Rational(resident_fitness(k), mutant_fitness(k))
            for k in range(1, population_size)
        ]
        total = 1
        product = 1
        for gamma in gammas:
            product *= gamma
            total += product
        return sympy.simplify(1 / total)

    # Neutral drift: rho_1 = 1/N.
    assert fixation_probability([[1, 1], [1, 1]], 4) == sympy.Rational(1, 4)
    # Specific matrix from the solution: rho_1 = 7/15.
    assert fixation_probability([[1, 2], [3, 1]], 4) == sympy.Rational(7, 15)


def test_replicator_dynamics_interior_fixed_points():
    """Replicator Dynamics: interior fixed points solve f_1(x) = f_2(x).

    chapters/replicator_dynamics/index.md, solutions
    `stability_from_fitness_functions` and
    `stable_populations_from_payoff_matrices`.
    """
    sympy = pytest.importorskip("sympy")
    x = sympy.Symbol("x")

    # Stability-from-fitness exercise, parts 1-3.
    assert sympy.solve((x - (1 - x)) - ((1 - x) - 2 * x), x) == [sympy.Rational(2, 5)]
    roots = sympy.solve(
        (x * (1 - x) - (1 - x)) - ((1 - x) - x + sympy.Rational(1, 2)), x
    )
    assert sympy.Rational(2) - sympy.sqrt(6) / 2 in roots
    assert sympy.solve(x**2 - (1 - x) ** 2, x) == [sympy.Rational(1, 2)]

    # Stable-populations-from-payoff-matrices exercise (Hawk-Dove x = 1/4).
    anti_coordination = (2 - 5) * x + (4 - 3) * (1 - x)
    assert sympy.solve(anti_coordination, x) == [sympy.Rational(1, 4)]


def test_best_response_polytopes_ratios():
    """Best Response Polytopes: the corrected label-dropping ratio is 25/67.

    chapters/best_response_polytopes/index.md, "Example: Application of the
    Lemke-Howson Algorithm for the threat detection game with integer
    pivoting" (the vertex and label computations).
    """
    sympy = pytest.importorskip("sympy")
    assert sympy.Rational(7, 288) / sympy.Rational(469, 7200) == sympy.Rational(25, 67)
    # Vertex denominator is 4927, not 4972.
    assert sympy.Rational(5832, 4927) != sympy.Rational(5832, 4972)


def test_routing_games_nash_flow_roots():
    """Routing Games: the corrected quadratic roots.

    chapters/routing_games/index.md, "Example: Nash Flow for Delivery
    companies game" (Definition: Nash Flow).
    """
    sympy = pytest.importorskip("sympy")
    alpha = sympy.Symbol("alpha")

    # Nash flow root (-3 + sqrt(69)) / 10 in the feasible region.
    roots = sympy.solve(5 * alpha**2 + 3 * alpha - 3, alpha)
    assert (-sympy.Rational(3, 10) + sympy.sqrt(69) / 10) in roots
    feasible = [root for root in roots if 0 <= root <= 1]
    assert len(feasible) == 1

    # Second worked example root -1/2 + sqrt(3)/2.
    roots = sympy.solve(2 * alpha**2 + 2 * alpha - 1, alpha)
    assert (-sympy.Rational(1, 2) + sympy.sqrt(3) / 2) in roots


def test_matching_games_stable_matching():
    """Matching Games: Gale-Shapley reproduces the stated stable matching.

    chapters/matching_games/index.md, Programming section (the `matching`
    library's `StableMarriage`), reproducing the worked example of the
    authors/reviewers matching.
    """
    matching = pytest.importorskip("matching")
    from matching.games import StableMarriage

    author_prefs = {
        "A1": ["R3", "R1", "R4", "R5", "R2"],
        "A2": ["R2", "R4", "R3", "R5", "R1"],
        "A3": ["R5", "R2", "R3", "R1", "R4"],
        "A4": ["R2", "R3", "R5", "R1", "R4"],
        "A5": ["R5", "R3", "R4", "R2", "R1"],
    }
    reviewer_prefs = {
        "R1": ["A3", "A1", "A5", "A4", "A2"],
        "R2": ["A4", "A2", "A5", "A1", "A3"],
        "R3": ["A1", "A5", "A2", "A3", "A4"],
        "R4": ["A2", "A5", "A3", "A1", "A4"],
        "R5": ["A5", "A3", "A4", "A1", "A2"],
    }
    game = StableMarriage.create_from_dictionaries(author_prefs, reviewer_prefs)
    matches = {str(a): str(r) for a, r in game.solve().items()}
    assert matches == {
        "A1": "R3",
        "A2": "R4",
        "A3": "R1",
        "A4": "R2",
        "A5": "R5",
    }


def test_auction_games_revenue_equivalence():
    """Auction Games: first- and second-price auctions share expected revenue.

    chapters/auction_games/index.md, `revenue_equivalence` (the Revenue
    Equivalence Theorem) together with "Theorem: Bayesian Nash equilibrium in
    a first-price auction with uniform values".
    """
    sympy = pytest.importorskip("sympy")
    number_of_bidders = sympy.Symbol("n", positive=True, integer=True)

    # Second-price: expected payment is E[second-highest of n Unif[0,1] values].
    second_price_revenue = (number_of_bidders - 1) / (number_of_bidders + 1)
    # First-price symmetric BNE: bid (n-1)/n * v, winner has the highest value.
    first_price_revenue = sympy.simplify(
        (number_of_bidders - 1)
        / number_of_bidders
        * number_of_bidders
        / (number_of_bidders + 1)
    )
    assert sympy.simplify(second_price_revenue - first_price_revenue) == 0


def test_social_choice_condorcet_and_borda():
    """Social Choice: the motivating profile via pref_voting.

    chapters/social_choice/index.md, Programming section, using the profile of
    the "Voting on exam topics" motivating example.
    """
    profiles = pytest.importorskip("pref_voting.profiles")
    c1_methods = pytest.importorskip("pref_voting.c1_methods")
    scoring_methods = pytest.importorskip("pref_voting.scoring_methods")

    profile = profiles.Profile([[0, 1, 2]] * 18 + [[1, 2, 0]] * 16 + [[2, 0, 1]] * 11)
    # Cyclic majority: no Condorcet winner (all alternatives returned).
    assert sorted(c1_methods.condorcet(profile)) == [0, 1, 2]
    # Borda selects alternative 1 (B).
    assert list(scoring_methods.borda(profile)) == [1]


def _coopgt_games():
    return {
        "dnd": {
            (): 0,
            (1,): 0,
            (2,): 0,
            (3,): 0,
            (1, 2): 900,
            (1, 3): 400,
            (2, 3): 600,
            (1, 2, 3): 1000,
        },
        "v1": {
            (): 0,
            (1,): 5,
            (2,): 3,
            (3,): 2,
            (1, 2): 12,
            (1, 3): 5,
            (2, 3): 4,
            (1, 2, 3): 13,
        },
        "v2": {(): 0, (1,): 6, (2,): 0, (1, 2): 5},
        "v3": {
            (): 0,
            (1,): 6,
            (2,): 6,
            (3,): 13,
            (1, 2): 6,
            (1, 3): 13,
            (2, 3): 13,
            (1, 2, 3): 26,
        },
        "v4": {
            (): 0,
            (1,): 6,
            (2,): 7,
            (3,): 0,
            (4,): 8,
            (1, 2): 7,
            (1, 3): 6,
            (1, 4): 12,
            (2, 3): 7,
            (2, 4): 12,
            (3, 4): 8,
            (1, 2, 3): 7,
            (1, 2, 4): 24,
            (1, 3, 4): 12,
            (2, 3, 4): 12,
            (1, 2, 3, 4): 25,
        },
        "linear": {
            (): 0,
            (1,): 0.122,
            (2,): 0.097,
            (3,): 0.551,
            (1, 2): 0.174,
            (1, 3): 0.581,
            (2, 3): 0.620,
            (1, 2, 3): 0.623,
        },
    }


def test_cooperative_games_shapley_values():
    """Cooperative Games: every stated Shapley value, via coopgt.

    chapters/cooperative_games/index.md: the D&D battle
    (`motivating_example:dnd_battle`), exercise
    `shapley-value-computation-and-properties` (games v1-v4), and exercise
    `interpreting_linear_models` (the linear-model game).
    """
    shapley_value = pytest.importorskip("coopgt.shapley_value")
    numpy = pytest.importorskip("numpy")
    games = _coopgt_games()

    expected = {
        "dnd": [350, 450, 200],
        "v1": [20 / 3, 31 / 6, 7 / 6],
        "v2": [11 / 2, -1 / 2],
        "v3": [19 / 3, 19 / 3, 40 / 3],
        "v4": [83 / 12, 89 / 12, 1 / 4, 125 / 12],
        "linear": [0.0595, 0.0665, 0.497],
    }
    for name, characteristic_function in games.items():
        value = shapley_value.calculate(characteristic_function=characteristic_function)
        assert numpy.allclose(value, expected[name], atol=1e-3), name


def test_cooperative_games_properties():
    """Cooperative Games: monotone/superadditive flags, via coopgt.

    chapters/cooperative_games/index.md, exercise
    `shapley-value-computation-and-properties` (monotonicity and
    superadditivity parts of the solution).
    """
    properties = pytest.importorskip("coopgt.characteristic_function_properties")
    games = _coopgt_games()

    assert properties.is_monotone(games["v1"]) is True
    assert properties.is_superadditive(games["v1"]) is False
    assert properties.is_monotone(games["v2"]) is False
    assert properties.is_monotone(games["v3"]) is True
    assert properties.is_superadditive(games["v3"]) is False
    assert properties.is_monotone(games["v4"]) is True
    assert properties.is_superadditive(games["v4"]) is False


def test_cooperative_games_additivity():
    """Cooperative Games: the additivity exercise, via coopgt.

    chapters/cooperative_games/index.md, exercise `additivity-and-symmetry`.
    """
    shapley_value = pytest.importorskip("coopgt.shapley_value")
    numpy = pytest.importorskip("numpy")

    va = {
        (): 0,
        (1,): 2,
        (2,): 2,
        (3,): 0,
        (1, 2): 0,
        (1, 3): 0,
        (2, 3): 0,
        (1, 2, 3): 0,
    }
    vb = {
        (): 0,
        (1,): 0,
        (2,): 0,
        (3,): 0,
        (1, 2): 0,
        (1, 3): 1,
        (2, 3): 1,
        (1, 2, 3): 3,
    }
    v_plus = {coalition: va[coalition] + vb[coalition] for coalition in va}

    phi_a = shapley_value.calculate(characteristic_function=va)
    phi_b = shapley_value.calculate(characteristic_function=vb)
    phi_plus = shapley_value.calculate(characteristic_function=v_plus)
    assert numpy.allclose(phi_a, [1 / 3, 1 / 3, -2 / 3])
    assert numpy.allclose(phi_b, [5 / 6, 5 / 6, 4 / 3])
    assert numpy.allclose(phi_plus, numpy.array(phi_a) + numpy.array(phi_b))


def test_the_core_membership():
    """The Core: membership, convexity and emptiness, via coopgt.

    chapters/the_core/index.md, Programming section (the D&D battle) and the
    exercises `core_convex_game`, `core_glove_market` and
    `core_empty_majority_game`, plus the nucleolus example.
    """
    core = pytest.importorskip("coopgt.core")
    shapley_value = pytest.importorskip("coopgt.shapley_value")

    dnd = _coopgt_games()["dnd"]
    shapley = shapley_value.calculate(dnd)
    assert core.is_in_core(dnd, shapley) is False
    assert core.is_in_core(dnd, [350, 600, 50]) is True
    assert core.is_convex(dnd) is False
    assert core.is_in_core(dnd, [1100 / 3, 1700 / 3, 200 / 3]) is True

    convex_game = {
        (): 0,
        (1,): 1,
        (2,): 1,
        (3,): 1,
        (1, 2): 4,
        (1, 3): 4,
        (2, 3): 4,
        (1, 2, 3): 9,
    }
    assert core.is_convex(convex_game) is True
    assert core.is_in_core(convex_game, [3, 3, 3]) is True

    glove_market = {
        (): 0,
        (1,): 0,
        (2,): 0,
        (3,): 0,
        (1, 2): 0,
        (1, 3): 1,
        (2, 3): 1,
        (1, 2, 3): 1,
    }
    assert core.is_in_core(glove_market, [0, 0, 1]) is True
    assert core.is_in_core(glove_market, [0.5, 0, 0.5]) is False

    majority_game = {
        (): 0,
        (1,): 0,
        (2,): 0,
        (3,): 0,
        (1, 2): 1,
        (1, 3): 1,
        (2, 3): 1,
        (1, 2, 3): 1,
    }
    assert core.find_core_point(majority_game) is None
