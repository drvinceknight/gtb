---
kernelspec:
  name: python3
  display_name: "Python 3"
---

(chp:direct_reciprocity)=

# Direct Reciprocity

Sustained cooperation over time depends on players remembering past interactions
and responding to them appropriately. This chapter begins with Axelrod's
computer tournaments, which identified strategies that succeed in the iterated
Prisoner's Dilemma, before focusing on reactive strategies: a tractable class
that conditions only on the opponent's last move.

```{figure} assets/illustrations/cooperation_buttons.png
:alt: A choice between a cooperate button and a defect button.
:label: fig:cooperation_buttons
:class: illustration
:width: 70%

Cooperate or defect: in a repeated encounter each player presses one button at
a time, with an eye on how the other has played before. Direct reciprocity
studies how such conditional responses sustain cooperation.
```

(sec:motivating_example_direct_reciprocity)=

## Motivating Example: Research Collaboration

Alice and Bob are researchers who meet regularly to share results before
submitting papers. At each meeting, each can choose to:

- **Cooperate (C)**: share their latest findings openly.
- **Defect (D)**: withhold key results to protect their competitive advantage.

The payoff structure is that of a **Prisoner's Dilemma**: mutual sharing is
best collectively, but each individual has a short-term incentive to withhold.
The [Folk Theorem](#theorem:folk_theorem) tells us that cooperation _can_ be
sustained in an infinitely repeated game: but it does not say _how_.

In practice, Alice and Bob remember only the last meeting. Alice might decide:
"I'll share if you shared last time, but withhold if you withheld." This
**memory-one** approach, conditioning solely on the previous round's outcome,
is both cognitively realistic and mathematically tractable.

This chapter asks: which reactive strategies actually sustain cooperation,
and what are their long-run payoffs?

## Theory

We start by giving a more general definition of [](#exam:prisoners_dilemma).
This game captures the fundamental structure of direct reciprocity in a repeated
game setting.

(def:prisoners-dilemma)=

### Definition: Prisoner's Dilemma

---

The **Prisoner's Dilemma** is the two-player symmetric game:

$$
A =
\begin{pmatrix}
    R & S\\
    T & P
\end{pmatrix}\qquad
B =
\begin{pmatrix}
    R & T\\
    S & P
\end{pmatrix}
$$

with the constraints:

$$
T > R > P > S \qquad 2R > T + S
$$

- The first constraint ensures **Defect** strictly dominates **Cooperate**.
- The second ensures mutual cooperation is socially optimal.

---

#### Example: Simplified Prisoner's Dilemma

Under what conditions is the following game a Prisoner's Dilemma?

$$
A = \begin{pmatrix}
      1       & -\mu \\
      1 + \mu & 0
    \end{pmatrix}\qquad
B = A^T
$$

This requires $1 + \mu > 1$ and $0 > -\mu$, both of which hold for $\mu > 0$.
The constraint $2R > T + S$ gives $2 > 1$, which always holds.
This parametrisation is convenient: $\mu > 0$ is the only condition needed.

(sec:axelrods_tournaments)=

### Axelrod's Tournaments

---

In 1980, Robert Axelrod organised a computer tournament for the iterated
Prisoner's Dilemma [@axelrod1980effective].

- Fourteen strategies were submitted.
- The tournament was a round-robin of 200 iterations, plus a strategy playing
  uniformly at random.
- Some entries were highly sophisticated; one used a $\chi^2$ test to detect
  random opponents.
- The winner was the simplest entry: **Tit For Tat** (TFT), which cooperates
  on the first move then copies the opponent's previous action.

A second tournament with 62 submissions followed [@axelrod1980more]. With
participants now aware of TFT's success, many strategies were designed
specifically to counter it. TFT won again.

---

These results suggested four principles for successful cooperation:

- **Don't be envious**: don't strive for a higher score than your opponent.
- **Be nice**: never defect first.
- **Reciprocate**: match cooperation with cooperation, defection with defection.
- **Don't be too clever**: avoid overly complex exploitation.

```{important}
While influential, these principles have since been challenged by modern
research (see [](#sec:notable_research_direct_reciprocity)).
```

### Definition: Reactive Strategy

---

A **reactive strategy** in the Prisoner's Dilemma is a pair
$(p, q) \in [0, 1]^2$ where:

- $p$ is the probability of cooperating given the opponent **cooperated** last round.
- $q$ is the probability of cooperating given the opponent **defected** last round.

---

The first move is typically set separately (often cooperate), since there is no
prior history.

#### Example: Common Reactive Strategies

| Strategy                | $(p, q)$        | Description                                             |
| ----------------------- | --------------- | ------------------------------------------------------- |
| Always Cooperate (AllC) | $(1, 1)$        | Cooperates regardless of opponent's action              |
| Always Defect (AllD)    | $(0, 0)$        | Defects regardless of opponent's action                 |
| Tit For Tat (TFT)       | $(1, 0)$        | Copies opponent's last move exactly                     |
| Generous TFT (GTFT)     | $(1, \epsilon)$ | TFT but occasionally forgives a defection               |
| Random                  | $(1/2, 1/2)$    | Cooperates with probability $1/2$ regardless of context |
| Generous Reciprocator   | $(0.9, 0.3)$    | Strongly reciprocates cooperation; sometimes forgives   |
| Suspicious Reciprocator | $(0.7, 0.1)$    | Cautiously cooperative; rarely forgives defection       |

```{note}
Reactive strategies are a subclass of **memory-one** strategies, which
condition on the full previous outcome $(a_1, a_2) \in \{C,D\}^2$ rather than
just the opponent's last action. The zero-determinant strategies discussed in
[](#sec:notable_research_direct_reciprocity) are memory-one but not reactive.
```

(def:markov_chain_of_reactive_strategies)=

### Definition: Markov Chain of Two Reactive Strategies

---

When players with reactive strategies $(p, q)$ and $(p', q')$ play an
infinitely repeated Prisoner's Dilemma, the pair of actions at each round
defines a **Markov chain** with state space
$\mathcal{S} = \{CC, CD, DC, DD\}$.

The transition matrix $P \in \mathbb{R}^{4 \times 4}$, with rows and columns
ordered as $(CC, CD, DC, DD)$, is:

$$
M =
\begin{pmatrix}
pp'      & p(1-p')      & (1-p)p'      & (1-p)(1-p')      \\
qp'      & q(1-p')      & (1-q)p'      & (1-q)(1-p')      \\
pq'      & p(1-q')      & (1-p)q'      & (1-p)(1-q')      \\
qq'      & q(1-q')      & (1-q)q'      & (1-q)(1-q')      \\
\end{pmatrix}
$$

where rows correspond to the current state and columns to the next state.

---

The entry $M_{ss'}$ is the probability of transitioning from state $s$ to
state $s'$. For example, from state $CD$ (player 1 cooperated, player 2
defected): player 1 now cooperates with probability $q$ (their opponent
defected), while player 2 now cooperates with probability $p'$ (their opponent
cooperated).

(theorem:long_run_average_payoff_via_stationary_distribution)=

### Theorem: Long-Run Average Payoffs via Stationary Distribution

---

If the Markov chain defined by $(p, q)$ and $(p', q')$ is **ergodic** (see
[Appendix A3](#app:ergodic_markov_chain)), it has a unique stationary
distribution $\pi = (\pi_{CC}, \pi_{CD}, \pi_{DC}, \pi_{DD})$ satisfying:

$$
\pi M = \pi \qquad \sum_{s \in \mathcal{S}} \pi_s = 1
$$

The long-run average payoffs are then:

$$
\bar{u}_1 = R\,\pi_{CC} + S\,\pi_{CD} + T\,\pi_{DC} + P\,\pi_{DD}
$$

$$
\bar{u}_2 = R\,\pi_{CC} + T\,\pi_{CD} + S\,\pi_{DC} + P\,\pi_{DD}
$$

---

```{note}
The chain is ergodic whenever $0 < p, q, p', q' < 1$ (all probabilities
strictly interior). For boundary cases such as pure TFT $(p=1, q=0)$, the
chain may not be ergodic in general; the stationary distribution must be
verified separately.
```

(theorem:steady_state_distribution_for_two_reactive_strategies)=

### Theorem: Steady-State Distribution for Two Reactive Strategies

---

When both players use strictly non-deterministic reactive strategies
($0 < p, q, p', q' < 1$), the stationary distribution has a closed form.
Define:

$$
r_1 = p - q \qquad r_2 = p' - q'
$$

and:

$$
s_1 = \frac{q' r_1 + q}{1 - r_1 r_2} \qquad s_2 = \frac{q r_2 + q'}{1 - r_1 r_2}
$$

Then the unique stationary distribution is:

$$
\pi = \bigl(s_1 s_2,\; s_1(1-s_2),\; (1-s_1)s_2,\; (1-s_1)(1-s_2)\bigr)
$$

and the long-run average payoffs are:

$$
\bar{u}_1 = R\,s_1 s_2 + S\,s_1(1-s_2) + T\,(1-s_1)s_2 + P\,(1-s_1)(1-s_2)
$$

$$
\bar{u}_2 = R\,s_1 s_2 + T\,s_1(1-s_2) + S\,(1-s_1)s_2 + P\,(1-s_1)(1-s_2)
$$

---

The values $s_1$ and $s_2$ are the long-run cooperation probabilities of each
player. The stationary distribution factorises as a product of marginals, so
the players' long-run actions are independent despite their strategies being
correlated round-to-round.

#### Proof

Verify by direct substitution: set
$\pi = (s_1 s_2,\, s_1(1-s_2),\, (1-s_1)s_2,\, (1-s_1)(1-s_2))$ and confirm
$\pi M = \pi$ holds with the transition matrix from the definition above:

$$
\pi M =
(s_1 s_2,\, s_1(1-s_2),\, (1-s_1)s_2,\, (1-s_1)(1-s_2)) P
$$

After carrying out the multiplication, each component of $\pi M$ reduces to the
corresponding component of $\pi$ when $s_1$ and $s_2$ satisfy the given
expressions. The algebra is routine but lengthy.

(example:long-run-payoffs-for-two-reactive-strategies)=

#### Example: Long-run payoffs for two reactive strategies

Consider the [contractor Prisoner's Dilemma](#example:repeated-contractor-game)
with $R=3, S=0, T=5, P=1$, and two reactive strategies:

- Player 1 (Generous Reciprocator): $(p, q) = (0.9,\; 0.3)$
- Player 2 (Suspicious Reciprocator): $(p', q') = (0.7,\; 0.1)$

From state $CC$: player 1 cooperates with $p=0.9$, player 2 with $p'=0.7$:

$$
CC \to CC: 0.63,\quad CC \to CD: 0.27,\quad CC \to DC: 0.07,\quad CC \to DD: 0.03
$$

From state $CD$: player 1 cooperates with $q=0.3$, player 2 with $p'=0.7$:

$$
CD \to CC: 0.21,\quad CD \to CD: 0.09,\quad CD \to DC: 0.49,\quad CD \to DD: 0.21
$$

From state $DC$: player 1 cooperates with $p=0.9$, player 2 with $q'=0.1$:

$$
DC \to CC: 0.09,\quad DC \to CD: 0.81,\quad DC \to DC: 0.01,\quad DC \to DD: 0.09
$$

From state $DD$: player 1 cooperates with $q=0.3$, player 2 with $q'=0.1$:

$$
DD \to CC: 0.03,\quad DD \to CD: 0.27,\quad DD \to DC: 0.07,\quad DD \to DD: 0.63
$$

So the full transition matrix is:

$$
M =
\begin{pmatrix}
0.63 & 0.27 & 0.07 & 0.03 \\
0.21 & 0.09 & 0.49 & 0.21 \\
0.09 & 0.81 & 0.01 & 0.09 \\
0.03 & 0.27 & 0.07 & 0.63 \\
\end{pmatrix}
$$

Since all four parameters are strictly interior, we apply the closed-form
theorem. With $r_1 = 0.9 - 0.3 = 0.6$ and $r_2 = 0.7 - 0.1 = 0.6$:

$$
s_1 = \frac{0.1 \times 0.6 + 0.3}{1 - 0.6 \times 0.6} = \frac{0.36}{0.64} = \frac{9}{16}
\qquad
s_2 = \frac{0.3 \times 0.6 + 0.1}{0.64} = \frac{0.28}{0.64} = \frac{7}{16}
$$

The stationary distribution is:

$$
\pi = \left(\frac{9}{16} \cdot \frac{7}{16},\; \frac{9}{16} \cdot \frac{9}{16},\; \frac{7}{16} \cdot \frac{7}{16},\; \frac{7}{16} \cdot \frac{9}{16}\right)
= \left(\frac{63}{256},\; \frac{81}{256},\; \frac{49}{256},\; \frac{63}{256}\right)
$$

Long-run average payoffs:

$$
\bar{u}_1 = \frac{3 \cdot 63 + 0 \cdot 81 + 5 \cdot 49 + 1 \cdot 63}{256} = \frac{497}{256} \approx 1.94
$$

$$
\bar{u}_2 = \frac{3 \cdot 63 + 5 \cdot 81 + 0 \cdot 49 + 1 \cdot 63}{256} = \frac{657}{256} \approx 2.57
$$

The Suspicious Reciprocator earns a higher long-run payoff. Despite cooperating
less, their lower generosity extracts value from the Generous Reciprocator's
willingness to forgive defections.

## Exercises

```{exercise}
:label: identifying_prisoners_dilemmas

Justify whether or not the following games are instances of the Prisoner's
Dilemma.

**Game 1**

$$
A =
\begin{pmatrix}
3 & 0\\
5 & 1
\end{pmatrix}
\qquad
B =
\begin{pmatrix}
3 & 5\\
0 & 1
\end{pmatrix}
$$

**Game 2**

$$
A =
\begin{pmatrix}
1 & -1\\
2 & 0
\end{pmatrix}
\qquad
B =
\begin{pmatrix}
1 & 2\\
-1 & 0
\end{pmatrix}
$$

**Game 3**

$$
A =
\begin{pmatrix}
1 & -1\\
2 & 0
\end{pmatrix}
\qquad
B =
\begin{pmatrix}
3 & 5\\
0 & 1
\end{pmatrix}
$$

**Game 4**

$$
A =
\begin{pmatrix}
6 & 0\\
12 & 1
\end{pmatrix}
\qquad
B =
\begin{pmatrix}
6 & 12\\
0 & 0
\end{pmatrix}
$$
```

```{exercise}
:label: reactive_strategy_markov_chain

Consider the Prisoner's Dilemma with $R=3, S=0, T=5, P=1$.

1. Write down the transition matrix $P$ for the Markov chain formed by
   Tit For Tat $(p=1, q=0)$ playing against Always Cooperate $(p'=1, q'=1)$.
2. Write down the transition matrix $P$ for the Markov chain formed by
   Tit For Tat $(p=1, q=0)$ playing against Always Defect $(p'=0, q'=0)$.
3. For each case, identify whether the chain is ergodic and, if so, find
   the stationary distribution and the long-run average payoffs.
```

```{exercise}
:label: general_reactive_strategy_markov_chains

For each of the following pairs of reactive strategies:

1. $p=(1/2, 1/2)\qquad p'=(1/2, 1/2)$
2. $p=(1/4, 1/2)\qquad p'=(1/2, 1/4)$
3. $p=(1/3, 1/3)\qquad p'=(2/3, 1/4)$

Obtain the Markov chain representation for a match and the utilities for both players as
a function of $R, S, T, P$.
```

```{exercise}
:label: best_response_to_reactive_strategies

Assuming $p=(x, 1/2)$ and using $R=3, S=0, T=5, P=1$, find the optimal $x$ against the
following players:

   1. $p'=(1, 0)$
   2. $p'=(1/2, 1/2)$

Interpret these results.
```

```{exercise}
:label: three_reactive_strategies

Consider the Prisoner's Dilemma with $R = 3$, $S = 0$, $T = 5$, $P = 1$ and
the four reactive strategies:

- **AllC**: $(p, q) = (1, 1)$, always cooperate.
- **TFT**: $(p, q) = (1, 0)$, cooperate first, then copy the opponent's last move.
- **AllD**: $(p, q) = (0, 0)$, always defect.
- **SR** (Suspicious Reciprocator): $(p, q) = (7/10, 1/10)$.

Assume both players cooperate on the first move.

1. For each of the ten distinct pairings (every strategy against each of the
   four, including itself, using symmetry to halve the work), identify the
   long-run stationary distribution and the average payoffs $(\bar{u}_1,
   \bar{u}_2)$.
2. Write the $4 \times 4$ payoff matrix $M_r$ for the repeated game in which
   AllC, TFT, AllD, and SR are the available actions.
3. Find all pure Nash equilibria of this game and compare the payoffs they deliver.
```

## Programming

(sec:computing_the_stationary_distribution_of_a_reactive_strategy_pair)=

### Computing the Stationary Distribution of a Reactive Strategy Pair

Given the transition matrix $P$ for two reactive strategies, the stationary
distribution satisfies $\pi P = \pi$. We can find it by solving the linear
system $(P^T - I)\pi^T = 0$ subject to $\sum \pi_i = 1$.

```{code-cell} python3
import numpy as np

def reactive_transition_matrix(p, q, p_prime, q_prime):
    """
    Build the 4x4 transition matrix for reactive strategies (p,q) and (p',q').
    States are ordered: CC, CD, DC, DD.
    """
    M = np.array([
        [p * p_prime,       p * (1 - p_prime),       (1 - p) * p_prime,       (1 - p) * (1 - p_prime)],
        [q * p_prime,       q * (1 - p_prime),       (1 - q) * p_prime,       (1 - q) * (1 - p_prime)],
        [p * q_prime,       p * (1 - q_prime),       (1 - p) * q_prime,       (1 - p) * (1 - q_prime)],
        [q * q_prime,       q * (1 - q_prime),       (1 - q) * q_prime,       (1 - q) * (1 - q_prime)],
    ])
    return M

def stationary_distribution(M):
    """
    Compute the stationary distribution of a transition matrix M.
    """
    n = M.shape[0]
    A = (M.T - np.eye(n))
    A[-1, :] = 1
    b = np.zeros(n)
    b[-1] = 1
    return np.linalg.solve(A, b)

# Generous Reciprocator vs Suspicious Reciprocator
p, q = 0.9, 0.3
p_prime, q_prime = 0.7, 0.1

M = reactive_transition_matrix(p, q, p_prime, q_prime)
print("Transition matrix:")
print(np.round(M, 4))

pi = stationary_distribution(M)
print("\nStationary distribution (CC, CD, DC, DD):")
print(np.round(pi, 4))
```

```{code-cell} python3
# Compute long-run average payoffs
R, S, T, P = 3, 0, 5, 1

u1_bar = R * pi[0] + S * pi[1] + T * pi[2] + P * pi[3]
u2_bar = R * pi[0] + T * pi[1] + S * pi[2] + P * pi[3]

print(f"Long-run average payoff for Player 1: {u1_bar:.4f}")
print(f"Long-run average payoff for Player 2: {u2_bar:.4f}")
```

### Using the Axelrod Library

The `axelrod` Python library [@knight2016open] provides over 240 strategies
and tools to run reproducible tournaments, extending Axelrod's original
experiments to much larger and more diverse strategic populations.

#### Studying Reactive Strategies

The Axelrod library provides `axl.ReactivePlayer`, which takes the reactive
strategy parameters $(p, q)$ directly, matching the notation used throughout
this chapter.

The following code runs a long match between the Generous Reciprocator
$(p, q) = (0.9, 0.3)$ and the Suspicious Reciprocator $(p', q') = (0.7, 0.1)$
from the [example above](#example:long-run-payoffs-for-two-reactive-strategies)
and compares the result to the closed-form payoffs.

```{code-cell} python3
import axelrod as axl
import numpy as np

generous = axl.ReactivePlayer(probabilities=(0.9, 0.3))
suspicious = axl.ReactivePlayer(probabilities=(0.7, 0.1))

match = axl.Match([generous, suspicious], turns=50000, seed=0)
match.play()
u1, u2 = match.final_score_per_turn()
print(f"Simulated:   Generous={u1:.4f}, Suspicious={u2:.4f}")
print(f"Theoretical: Generous={497/256:.4f}, Suspicious={657/256:.4f}")
```

#### Exploring Wider Populations

Reactive strategies are a subclass of **memory-one strategies**, which
condition on the full previous outcome $(a_1, a_2) \in \{C, D\}^2$ rather than
just the opponent's last action. The Axelrod library includes many built-in
memory-one strategies.

```{code-cell} python3
import axelrod as axl
import numpy as np

# Some notable memory-one strategies included in the library
players = [
    axl.TitForTat(),       # reactive: (p, q) = (1, 0)
    axl.ZDGTFT2(),         # generous zero-determinant strategy
    axl.ZDExtortion(),     # extortionate zero-determinant strategy
    axl.Cooperator(),      # reactive: (p, q) = (1, 1)
    axl.Defector(),        # reactive: (p, q) = (0, 0)
]

tournament = axl.Tournament(
    players=players, turns=200, repetitions=200, seed=0
)
results = tournament.play(progress_bar=False)
print("Ranking:")
for rank, name in enumerate(results.ranked_names):
    print(f"  {rank + 1}. {name}")
```

The Axelrod library documentation includes a tutorial showing how to replicate
Axelrod's original 1980 tournament, providing a reproducible starting point for
exploring how strategy performance depends on the composition of the population.

(sec:notable_research_direct_reciprocity)=

## Notable Research

The seminal empirical work on direct reciprocity is due to Robert Axelrod
[@axelrod1980effective; @axelrod1980more], synthesised in his widely cited book
[@axelrod1984evolution]. As described in [Section 3](#sec:axelrods_tournaments),
Axelrod's tournaments established Tit For Tat as the canonical cooperative
strategy and produced four heuristics for successful play.

Subsequent work has challenged these heuristics. The development of the Axelrod
Python library [@knight2016open] enabled systematic and reproducible analysis
across a far greater population of strategies. In particular,
[@glynatsi2024properties] studied 45,600 tournaments across diverse strategic
populations and parameter regimes, finding that the original heuristics do not
generalise. The revised empirical findings suggest:

- Be a little bit envious.
- Be "nice" in non-noisy environments or when game lengths are longer.
- Reciprocate both cooperation and defection appropriately.
- It is acceptable to be clever.
- Adapt to the environment.

The observation that _being envious_ can be beneficial echoes a landmark
theoretical result. [@press2012iterated] introduced **zero-determinant
strategies**, memory-one strategies that can unilaterally enforce linear payoff
relationships, including extortionate dynamics. This paper was described by
_MIT Technology Review_ as having set "the world of game theory on fire."

However, [@hilbe2013evolution] and [@knight2018evolution] showed that
extortionate strategies do not tend to survive under evolutionary dynamics,
tempering the initial excitement and reinforcing the importance of
adaptability.

## Conclusion

This chapter examined how cooperation can emerge in pairwise repeated
interactions. Axelrod's tournaments identified Tit For Tat as the canonical
cooperative strategy and produced four heuristics for successful play. These
heuristics have since been challenged: modern computational work, enabled by
large-scale reproducible tournaments, finds that what succeeds depends heavily
on the strategic population and game parameters.

The theoretical core of the chapter is the reactive strategy framework.
When two players use reactive strategies, their interaction defines a Markov
chain over outcome pairs, and the stationary distribution gives long-run
average payoffs. This connects the intuitions from Axelrod's tournaments to a
rigorous mathematical foundation.

[](#tbl:direct_reciprocity_summary) summarises the key concepts.

```{table} Summary of key concepts in direct reciprocity
:label: tbl:direct_reciprocity_summary
:align: center
:class: table-bordered

| Concept | Description |
|---|---|
| Prisoner's Dilemma | A symmetric game where Defect dominates but mutual cooperation is socially optimal |
| Reactive strategy $(p, q)$ | Cooperates with probability $p$ after C, $q$ after D |
| Tit For Tat | Cooperates first, then copies opponent's last move |
| Markov chain of strategies | States are outcome pairs; transitions determined by $(p,q)$ and $(p',q')$ |
| Stationary distribution | Long-run fraction of time spent in each state |
| Long-run average payoff | Payoff weighted by stationary distribution |
| Zero-determinant strategies | Memory-one strategies enforcing linear payoff relationships |
| Axelrod's tournaments | Empirical tournaments establishing TFT's success and four cooperation heuristics |

```

---

```{attention}
Even the simplest reactive strategies can sustain cooperation or undermine it.
The Markov chain framework gives precise predictions about long-run payoffs, and
modern research continues to refine our understanding of which strategies thrive
across diverse and evolving populations.
```

---

(solutions:direct_reciprocity)=

## Solutions

```{solution} identifying_prisoners_dilemmas
:label: solution:identifying_prisoners_dilemmas

Game 1:

This is a Prisoners Dilemma: $(R, S, T, P) = (3, 0, 5, 1)$.

Game 2:

This is a Prisoners Dilemma: $(R, S, T, P) = (1, -1, 2, 0)$: $2>1>0>-1$ and $2\times 1 > 2 - 1$.

Game 3:

This is not a Prisoner's Dilemma $A \ne B ^ T$

Game 4:

This is not a Prisoner's Dilemma $A \ne B ^ T$
```

````{solution} reactive_strategy_markov_chain
:label: solution:reactive_strategy_markov_chain

This is a substitution exercise using
the [](#def:markov_chain_of_reactive_strategies):

**1. TFT $(p=1, q=0)$ vs AllC $(p'=1, q'=1)$.**

Substituting $p=1, q=0, p'=1, q'=1$:

$$
\begin{align*}
M &=
\begin{pmatrix}
1\cdot1 & 1\cdot0 & 0\cdot1 & 0\cdot0 \\
0\cdot1 & 0\cdot0 & 1\cdot1 & 1\cdot0 \\
1\cdot1 & 1\cdot0 & 0\cdot1 & 0\cdot0 \\
0\cdot1 & 0\cdot0 & 1\cdot1 & 1\cdot0
\end{pmatrix}\\
&=
\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 \\
1 & 0 & 0 & 0 \\
0 & 0 & 1 & 0
\end{pmatrix}
\end{align*}
$$

This chain has two absorbing components. Starting from $CC$: always stays in
$CC$. Starting from $CD$: moves to $DC$, then back to $CC$, then stays. Starting
from $DC$: moves to $CC$. Starting from $DD$: moves to $DC \to CC$.

Since all states eventually reach $CC$ (an absorbing state), the chain is **not
ergodic** (it has an absorbing state rather than a unique stationary
distribution with full support). However, it has a unique stationary distribution:

$$
\pi = (1, 0, 0, 0)
$$

since all paths lead to $CC$ and stay there.

The long-run average payoffs is given by the [](#theorem:long_run_average_payoff_via_stationary_distribution)

$$
\bar{u}_1 = R \cdot 1 + S \cdot 0 + T \cdot 0 + P \cdot 0 = R = 3
$$

$$
\bar{u}_2 = R \cdot 1 + T \cdot 0 + S \cdot 0 + P \cdot 0 = R = 3
$$

Both players cooperate in every round, earning $3$ each.

Here is some code to confirm the above calculations using functions written in
[](#sec:computing_the_stationary_distribution_of_a_reactive_strategy_pair)

```{code-cell} python3
M = reactive_transition_matrix(p=1, q=0, p_prime=1, q_prime=1)
print(M)
```

```{code-cell} python3
stationary_distribution(M)
```

**2. TFT $(p=1, q=0)$ vs AllD $(p'=0, q'=0)$.**

Substituting $p=1, q=0, p'=0, q'=0$:

$$
\begin{align*}
M &=
\begin{pmatrix}
1\cdot0 & 1\cdot1 & 0\cdot0 & 0\cdot1 \\
0\cdot0 & 0\cdot1 & 1\cdot0 & 1\cdot1 \\
1\cdot0 & 1\cdot1 & 0\cdot0 & 0\cdot1 \\
0\cdot0 & 0\cdot1 & 1\cdot0 & 1\cdot1
\end{pmatrix}\\
&=
\begin{pmatrix}
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
\end{align*}
$$

From any state: $CC \to CD \to DD \to DD \to \cdots$ (DD is absorbing). Starting
from $DC$: $DC \to CD \to DD$.

All paths reach $DD$, so the unique stationary distribution is:

$$
\pi = (0, 0, 0, 1)
$$

The chain is **not ergodic** (absorbing state at $DD$), but it has a unique
stationary distribution with $\pi_{DD} = 1$.

The long-run average payoffs is given by the [](#theorem:long_run_average_payoff_via_stationary_distribution)

$$
\bar{u}_1 = R \cdot 0 + S \cdot 0 + T \cdot 0 + P \cdot 1 = P = 1
$$

$$
\bar{u}_2 = R \cdot 0 + T \cdot 0 + S \cdot 0 + P \cdot 1 = P = 1
$$

Both players end up in perpetual mutual defection, each earning $1$.



```{code-cell} python3
M = reactive_transition_matrix(p=1, q=0, p_prime=0, q_prime=0)
print(M)
```

```{code-cell} python3
stationary_distribution(M)
```
````

````{solution} general_reactive_strategy_markov_chains
:label: solution:general_reactive_strategy_markov_chains

This is a substitution exercise using
the [](#def:markov_chain_of_reactive_strategies) and
the [](#theorem:steady_state_distribution_for_two_reactive_strategies):

1. $p=(1/2, 1/2)\qquad p'=(1/2, 1/2)$

  $$M = \begin{pmatrix}
  1/4&1/4&1/4&1/4\\
  1/4&1/4&1/4&1/4\\
  1/4&1/4&1/4&1/4\\
  1/4&1/4&1/4&1/4
  \end{pmatrix}$$

Long-run average payoffs:

$$
\bar{u}_1 = \frac{P + R + S + T}{4}
$$

$$
\bar{u}_2 = \frac{P + R + S + T}{4}
$$

2. $p=(1/4, 1/2)\qquad p'=(1/2, 1/4)$

$$
    M =
        \begin{pmatrix}
            1/8&1/8&3/8&3/8\\
            1/4&1/4&1/4&1/4\\
            1/16&3/16&3/16&9/16\\
            1/8&3/8&1/8&3/8
        \end{pmatrix}
$$

Long-run average payoffs:

$$
\bar{u}_1 = \frac{110 P + 42 R + 77 S + 60 T}{289}
$$

$$
\bar{u}_2 = \frac{110 P + 42 R + 60 S + 77 T}{289}
$$

3. $p=(1/3, 1/3)\qquad p'=(2/3, 1/4)$

$$M = \begin{pmatrix}
2/9 & 1/9 & 4/9 & 2/9\\
2/9 & 1/9 & 4/9 & 2/9\\
1/12 & 1/4 & 1/6 & 1/2\\
1/12 & 1/4 & 1/6 & 1/2
\end{pmatrix}$$

$$
\bar{u}_1 = \frac{22 P + 7 R + 11 S + 14 T}{54}
$$

$$
\bar{u}_2 = \frac{22 P + 7 R + 14 S + 11 T}{54}
$$

Here is some code to verify the above calculations:

```{code-cell} python3
import sympy as sym

R = sym.Symbol("R")
S = sym.Symbol("S")
T = sym.Symbol("T")
P = sym.Symbol("P")

for (p, q), (p_prime, q_prime) in [
    ([1 / 2, 1 / 2], [1 / 2, 1 / 2]),
    ([1 / 4, 1 / 2], [1 / 2, 1 / 4]),
    ([1 / 3, 1 / 3], [2 / 3, 1 / 4]),
]:
    M = reactive_transition_matrix(p, q, p_prime, q_prime)
    pi = stationary_distribution(M).round(3)
    u1_bar = R * pi[0] + S * pi[1] + T * pi[2] + P * pi[3]
    u2_bar = R * pi[0] + T * pi[1] + S * pi[2] + P * pi[3]
    print("=====")
    print(f"(p, q)={(p, q)}, (p', q')={(p_prime, q_prime)}")
    print("gives:")
    print(M)
    print(
        "With utility:",
        u1_bar,
        u2_bar,
    )
```

````

````{solution} best_response_to_reactive_strategies
:label: solution:best_response_to_reactive_strategies


This is a substitution exercise using
the [](#theorem:steady_state_distribution_for_two_reactive_strategies):

1. $p'=(1, 0)$

  $$u(x)=\frac{(-10x + 4(x - 1)^2 + 13)}{(2x - 3)^2}$$

The derivative of this function is given by:

$$
\frac{2(6x - 7)}{(2x - 3)^3}
$$

This derivative has zero for $x=7/6$ which is $>1$. Thus the utility is monotonic over the
interval $[0, 1]$. We have (by substitution):

$$u(0)=17/9\qquad u(1)=3$$

Thus $u(x)$ is an increasing function so the optimal value of $x$ is $1$.

Against a player that is unforgiving (reacts to defection with defection), given that our
player will play randomly against a defection it is better to always cooperate.

2. $p'=(1/2, 1/2)$

  $$u(x)=-3x/4+21/8$$

This is a decreasing function so the optimal value of $x$ is $0$.

Against a random player (who takes no notice of what we do) it is better to defect.

Here is some code to verify our calculations (using a function that implements
[](#theorem:steady_state_distribution_for_two_reactive_strategies)):

```{code-cell} python3
def theoretic_steady_state(p, q, p_prime, q_prime):

    r_1 = p - q
    r_2 = p_prime - q_prime
    s_1 = (q_prime * r_1 + q) / (1 - r_1 * r_2)
    s_2 = (q * r_2 + q_prime) / (1 - r_1 * r_2)
    return np.array([s_1 * s_2, s_1 * (1 - s_2), (1 - s_1) * s_2, (1 - s_1) * (1 - s_2)])

R, S, T, P = sym.Symbol("R"), sym.Symbol("S"), sym.Symbol("T"), sym.Symbol("P"),

def theoretic_utility(p, q, p_prime, q_prime, rstp=np.array([R, S, T, P])):
    pi = theoretic_steady_state(p, q, p_prime, q_prime)
    return np.dot(pi, rstp)

x = sym.Symbol("x")
for (p_prime, q_prime) in [(sym.S(1), sym.S(0)), (sym.S(1) / 2, sym.S(1) / 2)]:
    print(f"(p', q')={(p_prime, q_prime)}")
    utility = sym.factor(theoretic_utility(x, sym.S(1) / 2, p_prime, q_prime, rstp=np.array((3, 0, 5, 1))))
    print(f"    u(x)={utility}")
    print(f"    u(0)={utility.subs({x:0})}")
    print(f"    u(1)={utility.subs({x:1})}")
    print(f"    du(x)/dx={utility.diff(x).simplify()}")
    print(f"    solution of du(x)/dx=0: {sym.solveset(utility.diff(x), x)}")
```
````

````{solution} three_reactive_strategies
:label: solution:three_reactive_strategies

**Part 1.**

AllC, TFT, and AllD are at the boundary of the parameter space, so we trace
those chains directly. SR has strictly interior parameters, so the
[closed-form theorem](#theorem:steady_state_distribution_for_two_reactive_strategies)
applies whenever SR is one of the players. Since the PD is symmetric,
$(\bar{u}_1, \bar{u}_2)$ for $A$ vs $B$ equals $(\bar{u}_2, \bar{u}_1)$
for $B$ vs $A$, halving the number of computations.

**Pairings among AllC, TFT, AllD** (traced directly, starting from $CC$):

- **AllC vs AllC.** Chain stays in $CC$. $\pi = (1,0,0,0)$. Payoffs $(3,3)$.
- **AllC vs TFT.** AllC cooperates always; TFT sees cooperation and reciprocates. Chain stays in $CC$. $\pi = (1,0,0,0)$. Payoffs $(3,3)$.
- **AllC vs AllD.** AllC cooperates, AllD defects unconditionally. State $CD$ is absorbing. $\pi = (0,1,0,0)$. Payoffs $(0,5)$.
- **TFT vs TFT.** Starting from $CC$: both cooperate each round. $\pi = (1,0,0,0)$. Payoffs $(3,3)$.
- **TFT vs AllD.** $CC \to CD \to DD$; $DD$ absorbing. $\pi = (0,0,0,1)$. Payoffs $(1,1)$.
- **AllD vs AllD.** $CC \to DD$; $DD$ absorbing. $\pi = (0,0,0,1)$. Payoffs $(1,1)$.

**Pairings involving SR** (closed-form theorem, $r_1 = p - q$, $r_2 = p' - q'$):

Write $\text{SR} = (7/10,\, 1/10)$ so $r_{\text{SR}} = 7/10 - 1/10 = 3/5$.

**SR vs AllC.** $r_1 = 3/5$, $r_2 = 1-1 = 0$. Denominator $= 1$.

$$s_1 = \tfrac{3}{5} \cdot 1 + \tfrac{1}{10} = \tfrac{7}{10}, \qquad s_2 = \tfrac{1}{10} \cdot 0 + 1 = 1$$

$\pi = (7/10,\, 0,\, 3/10,\, 0)$.

$$\bar{u}_1 = 3 \cdot \tfrac{7}{10} + 5 \cdot \tfrac{3}{10} = \tfrac{36}{10} = \tfrac{18}{5}, \qquad \bar{u}_2 = 3 \cdot \tfrac{7}{10} = \tfrac{21}{10}$$

**SR vs TFT.** $r_1 = 3/5$, $r_2 = 1-0 = 1$. Denominator $= 1 - 3/5 = 2/5$.

$$s_1 = \frac{0 \cdot \tfrac{3}{5} + \tfrac{1}{10}}{\tfrac{2}{5}} = \frac{\tfrac{1}{10}}{\tfrac{2}{5}} = \frac{1}{4}, \qquad s_2 = \frac{\tfrac{1}{10} \cdot 1 + 0}{\tfrac{2}{5}} = \frac{1}{4}$$

$\pi = (1/16,\, 3/16,\, 3/16,\, 9/16)$.

$$\bar{u}_1 = \frac{3 + 0 + 15 + 9}{16} = \frac{27}{16}, \qquad \bar{u}_2 = \frac{3 + 15 + 0 + 9}{16} = \frac{27}{16}$$

**SR vs AllD.** $r_1 = 3/5$, $r_2 = 0-0 = 0$. Denominator $= 1$.

$$s_1 = 0 \cdot \tfrac{3}{5} + \tfrac{1}{10} = \tfrac{1}{10}, \qquad s_2 = \tfrac{1}{10} \cdot 0 + 0 = 0$$

$\pi = (0,\, 1/10,\, 0,\, 9/10)$.

$$\bar{u}_1 = 0 \cdot \tfrac{1}{10} + 1 \cdot \tfrac{9}{10} = \tfrac{9}{10}, \qquad \bar{u}_2 = 5 \cdot \tfrac{1}{10} + 1 \cdot \tfrac{9}{10} = \tfrac{7}{5}$$

**SR vs SR.** $r_1 = r_2 = 3/5$. Denominator $= 1 - 9/25 = 16/25$.

$$s_1 = \frac{\tfrac{1}{10} \cdot \tfrac{3}{5} + \tfrac{1}{10}}{\tfrac{16}{25}} = \frac{\tfrac{8}{50}}{\tfrac{16}{25}} = \frac{1}{4}, \qquad s_2 = \frac{1}{4}$$

$\pi = (1/16,\, 3/16,\, 3/16,\, 9/16)$.

$$\bar{u}_1 = \bar{u}_2 = \frac{27}{16}$$

**Part 2.** Reading off the row player's payoff, with rows and columns ordered
(AllC, TFT, AllD, SR) and symmetric pairs filled in by the PD symmetry:

$$
M_r =
\begin{pmatrix}
3 & 3 & 0 & \tfrac{21}{10} \\[4pt]
3 & 3 & 1 & \tfrac{27}{16} \\[4pt]
5 & 1 & 1 & \tfrac{7}{5}   \\[4pt]
\tfrac{18}{5} & \tfrac{27}{16} & \tfrac{9}{10} & \tfrac{27}{16}
\end{pmatrix}
$$

Since the PD is symmetric, $M_c = M_r^T$.

**Part 3.** We test each pure strategy pair.

**(AllC, AllC):** Row deviates to AllD: $5 > 3$. **Not a NE.**

**(TFT, TFT):** Deviating to AllC earns $3 = 3$ (no gain); to AllD earns $1 < 3$;
to SR earns $27/16 < 3$. **Is a NE.**

**(AllD, AllD):** Deviating to AllC earns $0 < 1$; to TFT earns $1 = 1$ (no
gain); to SR earns $9/10 < 1$. **Is a NE.**

**(SR, SR):** SR earns $27/16 \approx 1.69$. Deviating to AllC earns
$21/10 = 2.1 > 27/16$ (equivalently $336/160 > 270/160$), so the deviation is
profitable; to TFT earns $27/16$ (a tie); to AllD earns $7/5 = 1.4 < 27/16$.
Since deviating to AllC pays, this is **not a NE.**

The two pure Nash equilibria are **(TFT, TFT)** and **(AllD, AllD)**. The
(TFT, TFT) equilibrium payoff-dominates (AllD, AllD), with both players earning
$3$ rather than $1$.

We can confirm the payoff matrix, and the resulting equilibria, with the
`axelrod` library by simulating a long match between each pair of strategies.

```{code-cell} python3
import axelrod as axl
import numpy as np

# Reactive parameters (p, q); reactive players cooperate on the first move.
strategies = {"AllC": (1, 1), "TFT": (1, 0), "AllD": (0, 0), "SR": (0.7, 0.1)}
order = ["AllC", "TFT", "AllD", "SR"]


def long_run_payoff(row, col, turns=200000, seed=1):
    players = [
        axl.ReactivePlayer(probabilities=strategies[row]),
        axl.ReactivePlayer(probabilities=strategies[col]),
    ]
    match = axl.Match(players, turns=turns, seed=seed)
    match.play()
    return match.final_score_per_turn()[0]


payoff_matrix = np.array(
    [[long_run_payoff(row, col) for col in order] for row in order]
)
print("Row-player payoff matrix (AllC, TFT, AllD, SR):")
print(np.round(payoff_matrix, 3))
```

```{code-cell} python3
# A profile (s, s) is a pure Nash equilibrium when no row deviation beats it.
for index, strategy in enumerate(order):
    own = payoff_matrix[index, index]
    best_deviation = payoff_matrix[:, index].max()
    print(
        f"({strategy}, {strategy}): payoff {own:.3f}, "
        f"best response {best_deviation:.3f}, "
        f"Nash equilibrium: {own >= best_deviation - 1e-6}"
    )
```
````
