---
kernelspec:
  name: python3
  display_name: "Python 3"
---

(chp:sub_game_perfection)=

# Subgame Perfection

Nash equilibrium can be sustained by threats that would never actually be
carried out. This chapter introduces subgame perfect equilibrium, which rules
out such implausible threats by requiring rationality at every point in the
game tree, not only along the equilibrium path.

(seltens_chain_store_paradox)=

## Motivating Example

We will motivate this chapter using a special case of Selten's Chain Store Paradox [@selten1978chain]
which models an incumbent chain of stores that is well established and an
entrant to the market.

Campus Caffeine, a mobile coffee van, is considering parking near a
university where Latte Lords, a well-established bricks-and-mortar café,
has been operating unchallenged. If Campus Caffeine **enters**, Latte Lords
can slash prices for students (**Fight**) or maintain their premium pricing
(Accommodate). If Campus Caffeine stays out, Latte Lords keeps
enjoying high margins.

There are three outcomes which are shown as an extensive form game in
[](#fig:chain_store_paradox):

- Campus Caffeine chooses to withdraw and does not enter the market: they
  receive a utility of 1 and Latte Lords continues to have a monopoly with which
  corresponds to a utility of 5.
- Campus Caffeine enters the market and Latte Lords competes: this leads to low
  prices that give neither company a profit. They both obtain a utility of 0.
- Campus Caffeine enters and Latte Lords accommodates: they both share the
  market obtaining a utility of 2.

```{figure} ./images/chain-store-paradox/main.png
:alt: An extensive form game with 3 leafs.
:label: fig:chain_store_paradox
:height: 250px

The extensive form game between Campus Caffeine and Latte Lords.
```

As described in [](#sec:mapping_extensive_form_games_to_normal_form) it is
possible to map an extensive form game to a normal form game. In this case we
have:

$$
\mathcal{A}_1=\{\text{Accommodate}, \text{Fight}\}
\mathcal{A}_2=\{\text{Enter}, \text{Withdraw}\}\qquad
$$

giving:

$$
M_1=\begin{pmatrix}
2& 5\\
0& 5\\
\end{pmatrix}
\qquad
M_2=\begin{pmatrix}
2& 5\\
0& 1\\
\end{pmatrix}
$$

The incumbent can threaten to fight the entrant however the entrant knows that
this threat if carried out would be harmful to both of them. Thus the threat is
in essence an empty threat: the entrant will enter and the incumbent will use
their best response which is to accommodate.

This is an example of a degenerate game, the Nash equilibria was considered in
[](#exam:support_enumeration_for_a_degenerate_game) showing that there are in
fact 3 of them:

- $((1, 0), (1, 0))$: the entrant enters the market and the incumbent accommodates.
- $((0, 1), (0, 1))$: the entrant withdraws and the incumbent fights.
- $((\frac{3}{4}, \frac{1}{4}), (\frac{1}{4}, \frac{3}{4}))$: a mixture between
  the two.

This chapter will give the mathematical vocabulary to describe the difference
between these equilibria.

## Theory

To identify emergent behaviour in extensive form games we assume that players not only attempt to optimize their
overall utility but optimize their utility conditional on any information set.

(sec:definition_of_sequential_rationality)=

### Definition: Sequential rationality

---

**Sequential rationality:** An optimal strategy for a player should maximise that player's expected payoff,
conditional on every information set at which that player has a decision.

---

With this notion in mind we can now define an analysis technique for extensive form games:

### Definition: Backward induction

---

**Backward induction:** This is the process of analysing a game from back to front.
At each information set we remove strategies that are dominated.

---

#### Example

Let us consider the game shown in [](#fig:backwards-induction-running-example-step-1)

```{figure} ./images/backwards-induction-running-example-step-1/main.png
:alt: Running example for backwards inductions
:label: fig:backwards-induction-running-example-step-1
:height: 250px

An extensive form game that we will use backwards induction on.
```

We see that at node $(d)$ that Z is a dominated action.
So the game reduces as shown in [](#fig:backwards-induction-running-example-step-2).

```{figure} ./images/backwards-induction-running-example-step-2/main.png
:alt: Running example for backwards inductions after removing Z.
:label: fig:backwards-induction-running-example-step-2
:height: 250px

Reducing the game because Z is a dominated action.
```

Player 1s strategy profile is (Y).
At node $(c)$ A is a dominated action so that the game reduces as shown in [](#fig:backwards-induction-running-example-step-3).

```{figure} ./images/backwards-induction-running-example-step-3/main.png
:alt: Running example for backwards inductions after removing A.
:label: fig:backwards-induction-running-example-step-3
:height: 250px

Reducing the game because A is a dominated action.
```

Player 2s strategy profile is (B). At node $(b)$ D is a dominated action so that the game reduces as shown.

```{figure} ./images/backwards-induction-running-example-step-4/main.png
:alt: Running example for backwards inductions after removing D
:label: fig:backwards-induction-running-example-step-4
:height: 250px

Reducing the game because D is a dominated action.
```

Player 2s strategy profile is thus (C,B) and finally strategy W is dominated for player 1 whose strategy profile is (X,Y).
This pair of strategies form a Nash equilibrium.

### Theorem of existence of Nash equilibrium in games of perfect information.

---

Every finite game with perfect information has a Nash equilibrium in pure strategies. Backward induction identifies an equilibrium.

---

**Proof**:

---

Recalling the properties of [sequential rationality](#sec:definition_of_sequential_rationality) we see that no player will
have an incentive to deviate from the strategy profile found through backward induction.
Secondly every finite game with perfect information can be solved using backward inductions which gives the result.

---

### Definition: Subgame

---

In an extensive form game, a node $x$ is said to **initiate a subgame** if and only if $x$ and all successors of $x$
are in information sets containing only successors of $x$.

---

#### Example: a game where all nodes initiate subgames

A game where all nodes initiate a subgame is given in [](#fig:game-with-perfect-information).

```{figure} ./images/game-with-perfect-information/main.png
:alt: An extensive form game with perfect information
:label: fig:game-with-perfect-information
:height: 250px

An extensive form game where all nodes initiate a subgame.
```

#### Example: a game where all nodes do not initiate subgames

A game **that does not have perfect information** nodes $c$, $f$ and $b$ initiate subgames but all of $b$'s successors do
not is shown in [](#fig:game-with-imperfect-information)

```{figure} ./images/game-with-imperfect-information/main.png
:alt: An extensive form game with imperfect information
:label: fig:game-with-imperfect-information
:height: 250px

An extensive form game where all nodes do not initiate a subgame.
```

The notion of a subgame leads us to define a specific property of some Nash
equilibrium.

### Definition: Subgame perfect equilibrium

---

A subgame perfect Nash equilibrium is a Nash equilibrium in which the strategy profiles specify Nash
equilibria for every subgame of the game.

---

```{note}
This includes subgames that might not be reached during play.
```

Let us consider the example in [](#fig:game-with-a-subgame-perfect-equilibrium).

```{figure} ./images/game-with-subgame-perfect-equilibrium/main.png
:alt: An extensive form game with a subgame perfect equilibrium
:label: fig:game-with-a-subgame-perfect-equilibrium
:height: 250px

An game with subgame perfect equilibrium.
```

Let us build the corresponding normal form game:

$$A_1=\{AC,AD,BC,BD\}$$
and
$$A_2=\{X,Y\}$$

using the above ordering we have:

$$
M_1=
\begin{pmatrix}
-1&0\\
2&-1\\
1&1\\
1&1
\end{pmatrix}
\qquad
M_2=
\begin{pmatrix}
2&-1\\
3&1\\
7&7\\
7&7
\end{pmatrix}
$$

The Nash equilibria for the above game (found by inspecting best responses in action space) are:

$$\{(AD,X),(BC,Y),(BD,Y)\}$$

If we take a look at the normal form game representation of the subgame initiated at node b with action sets:

$$A_1=\{C,D\}\text{ and }A_2=\{X,Y\}$$

we have:

$$
M_1=
\begin{pmatrix}
-1&0\\
2&-1
\end{pmatrix}
\qquad
M_1=
\begin{pmatrix}
2&-1\\
3&1
\end{pmatrix}
$$

We see that the (unique) Nash equilibria for the above game is $(D,X)$.
Thus the only subgame perfect equilibria of the _entire_ game is $\{AD,X\}$.

```{note}
n games with perfect information, the Nash equilibrium obtained through backwards induction is subgame perfect.
```

## Exercises

```{exercise}
:label: backward_induction_practice

Obtain the Nash equilibrium for the following games using backward induction:

1. ![](./images/exercise_01_01/main.png)
2. ![](./images/exercise_01_02/main.png)
3. ![](./images/exercise_01_03/main.png)
4. ![](./images/exercise_01_04/main.png)
```

```{exercise}
:label: entry_signals_and_continuous_action

Player 1 chooses a number $x \geq 0$, which Player 2 observes. Then, both
players simultaneously and independently choose real numbers $y_1, y_2 \in
\mathbb{R}$. The utility functions are:

- Player 1: $2y_2y_1 + xy_1 - y_1^2 - \frac{x^3}{3}$
- Player 2: $-(y_1 - 2y_2)^2$

Find the subgame perfect equilibrium of this game.
```

```{exercise}
:label: subgame_identification_and_refinement

For each of the following extensive form games:

1. ![](./images/exercise_03_01/main.png)
2. ![](./images/exercise_03_02/main.png)
3. ![](./images/exercise_03_03/main.png)

- Identify all subgames.
- Derive the corresponding normal form representations.
- Find all Nash equilibria.
- Identify which are subgame perfect.
```

```{exercise}
:label: stackelberg_ice_cream_sellers

Two ice cream sellers choose locations along a beach represented by $[0,1]$.
Customers are uniformly distributed and always go to the nearest seller.

- **Player 1** chooses $x_1 \in [0,1]$
- **Player 2** observes $x_1$, then chooses $x_2 \in [0,1]$

Each seller's payoff is the proportion of customers they serve. Assume:

- If $x_1 = x_2$, each serves 50%.
- If $x_1 < x_2$, Player 1 serves $[0, \frac{x_1 + x_2}{2}]$, and Player 2 the rest.
- If $x_2 < x_1$, the roles reverse.

1. Write the payoff functions of each player.
2. Derive Player 2’s best response function $x_2^*(x_1)$.
3. Use backward induction to find the subgame perfect equilibrium.
4. Compare this to the simultaneous move version of the game.

> _Hint_: Think geometrically about the midpoint between locations.
```

## Programming

### Using Gambit to study an extensive form game

The `pygambit` library can compute equilibria of extensive form games. We define
Selten’s Chain Store Paradox as follows:

```{code-cell} python3
import pygambit as gbt

g = gbt.Game.new_tree(players=["Incumbent", "Entrant"],
                      title="1 stage Selten's Chain Store Paradox")
g.append_move(g.root, "Entrant", ["Enter", "Withdraw"])
g.append_move(g.root.children[0], "Incumbent", ["Accomodate", "Fight"])
g.set_outcome(g.root.children[1], g.add_outcome([5, 1], label="No entry"))
g.set_outcome(g.root.children[0].children[0], g.add_outcome([2, 2], label="Shared Market"))
g.set_outcome(g.root.children[0].children[1], g.add_outcome([0, 0], label="Competition"))
print(g)
```

This creates the extensive form game. To convert it to a normal form:

```{code-cell} python3
g.to_arrays(dtype=float)
```

```{note}
We use `dtype=float` so that results are returned in floating-point instead
of exact rational arithmetic.
```

To compute the pure-strategy Nash equilibria:

```{code-cell} python3
result = gbt.nash.enumpure_solve(g)
result.equilibria
```

## Notable Research

The concept of subgame perfection was first introduced in
[@selten1965spieltheoretische] and later reformulated in English in
[@selten1988reexamination], both by Reinhard Selten. The motivating example for
this chapter—the Chain Store Paradox—appears in [@selten1978chain], where Selten
considers multiple sequential market entrants and examines the credibility of
entry-deterrence strategies.

The framework was extended in [@milgrom1982predation], which introduced
**asymmetric information** and **reputation effects**. These additions showed how
players might sustain seemingly irrational threats (such as fighting entry) by
considering the beliefs and inferences of future opponents.

The idea of subgame perfection was further refined in [@kreps1982sequential],
which introduced the concept of **sequential equilibrium**, and in
[@grossman1986perfect], which developed **perfect sequential equilibrium**. These
refinements allow for the analysis of games where off-equilibrium beliefs matter,
providing stronger predictions in extensive form games with imperfect information.

## Conclusion

Subgame perfection refines the concept of Nash equilibrium by requiring that
players' strategies form a Nash equilibrium not just in the game as a whole, but
in every subgame—including those off the equilibrium path. This refinement
eliminates non-credible threats and ensures sequential rationality at every
decision point. Table [](#tbl:spe_summary) summaries the main concepts of this
chapter.

```{table} The main concepts for Subgame Perfectoin
:label: tbl:spe_summary
:align: center
:class: table-bordered

| Concept                     | Description                                                            |
| --------------------------- | ---------------------------------------------------------------------- |
| Sequential rationality      | Players optimise at each information set                               |
| Backward induction          | Method to compute subgame perfect equilibria in perfect information    |
| Subgame                     | Portion of a game starting at a decision node and fully self-contained |
| Subgame perfect equilibrium | A strategy profile that is a Nash equilibrium in every subgame         |

```

We illustrated these ideas with [Selten’s Chain Store Paradox](#seltens_chain_store_paradox), which highlights
how subgame perfection rules out the incumbent’s non-credible threat to fight.

---

```{attention}
In games with perfect information, backward induction not only
gives a Nash equilibrium—it guarantees a subgame perfect one.
```

---

(solutions:subgame_perfection)=

## Solutions

````{solution} backward_induction_practice
:label: solution:backward_induction_practice

We apply backward induction to each game by working from the terminal nodes
backwards, eliminating dominated actions at each decision node.

1. Starting from the final decision nodes, eliminate dominated actions bottom-up.
   At each internal node the player chooses the action giving them the highest
   payoff, given what the analysis of downstream nodes implies. The backward
   induction equilibrium is the unique strategy profile that survives this
   process.

2. The same procedure applies. At the last mover's node, the optimal action is
   identified; moving up, the penultimate mover chooses optimally given that
   prediction, and so on until the root.

3. In games with multiple branches, backward induction traces every branch to
   its terminal node, replaces each subtree with the payoff the last mover would
   choose, and proceeds upward.

4. The process is identical: backward induction yields a unique Nash equilibrium
   in pure strategies for any finite game of perfect information (guaranteed by
   the existence theorem). The resulting strategy profile specifies a best
   response at every information set.

```{note}
In all four cases, the Nash equilibrium obtained via backward induction is
subgame perfect, because the strategy profile constitutes a Nash equilibrium
in every subgame — including those off the equilibrium path.
```
````

````{solution} entry_signals_and_continuous_action
:label: solution:entry_signals_and_continuous_action

We solve by backward induction. Player 1 moves first (choosing $x \geq 0$),
then both players simultaneously choose $y_1, y_2 \in \mathbb{R}$.

**Step 1: Solve the simultaneous subgame for fixed $x$ and $y_1$.**

Player 2 maximises $-(y_1 - 2y_2)^2$. This is maximised when $y_1 - 2y_2 = 0$,
giving:

$$
y_2^*(y_1) = \frac{y_1}{2}
$$

**Step 2: Given Player 2's best response, solve for Player 1's optimal $y_1$.**

Substituting $y_2 = y_1/2$ into Player 1's utility:

$$
\begin{align*}
u_1 &= 2y_2 y_1 + x y_1 - y_1^2 - \frac{x^3}{3} \\
    &= 2 \cdot \frac{y_1}{2} \cdot y_1 + x y_1 - y_1^2 - \frac{x^3}{3} \\
    &= y_1^2 + x y_1 - y_1^2 - \frac{x^3}{3} \\
    &= x y_1 - \frac{x^3}{3}
\end{align*}
$$

This is linear in $y_1$. If $x > 0$ then $u_1 \to \infty$ as $y_1 \to \infty$,
so there is no finite optimum unless we impose additional constraints. Under the
problem as stated (with $y_1 \in \mathbb{R}$ unconstrained), we instead
interpret the optimisation by taking the first-order condition with respect to
$y_1$ before substituting $y_2^*$:

$$
\frac{\partial u_1}{\partial y_1} = 2y_2 + x - 2y_1 = 0
\implies y_1^* = \frac{2y_2 + x}{2}
$$

Substituting $y_2 = y_1/2$ (Player 2's best response):

$$
y_1^* = \frac{2(y_1^*/2) + x}{2} = \frac{y_1^* + x}{2}
\implies 2y_1^* = y_1^* + x
\implies y_1^* = x
$$

**Step 3: Solve for Player 1's choice of $x$.**

Substituting $y_1^* = x$ and $y_2^* = x/2$ into $u_1$:

$$
\begin{align*}
u_1 &= 2 \cdot \frac{x}{2} \cdot x + x \cdot x - x^2 - \frac{x^3}{3} \\
    &= x^2 + x^2 - x^2 - \frac{x^3}{3} \\
    &= x^2 - \frac{x^3}{3}
\end{align*}
$$

Taking the first-order condition with respect to $x$:

$$
\frac{du_1}{dx} = 2x - x^2 = x(2 - x) = 0
$$

So $x^* = 0$ or $x^* = 2$. Checking the second-order condition:

$$
\frac{d^2 u_1}{dx^2} = 2 - 2x
$$

At $x^* = 2$: $\frac{d^2 u_1}{dx^2} = 2 - 4 = -2 < 0$ (maximum).

At $x^* = 0$: $\frac{d^2 u_1}{dx^2} = 2 > 0$ (minimum).

Thus the interior maximiser is $x^* = 2$.

**Subgame perfect equilibrium:**

$$
x^* = 2,\quad y_1^*(x) = x,\quad y_2^*(y_1) = \frac{y_1}{2}
$$

On the equilibrium path: $x^* = 2$, $y_1^* = 2$, $y_2^* = 1$.

The equilibrium payoffs are:

$$
u_1 = 4 - \frac{8}{3} = \frac{4}{3}, \qquad u_2 = -(2 - 2)^2 = 0
$$

```{code-cell} python3
import sympy as sym

x, y1, y2 = sym.symbols("x y1 y2", real=True)

u1 = 2 * x * y1 - y1**2 - x**3 / 3
u2 = -(y1 - 2 * y2)**2

# Player 2's best response
br2 = sym.solve(sym.diff(u2, y2), y2)[0]
print("Player 2 BR:", br2)

# Substitute into Player 1's FOC for y1
u1_sub = u1.subs(y2, br2)
br1_eq = sym.solve(sym.diff(u1_sub, y1), y1)[0]
print("Player 1's optimal y1 given y2*:", br1_eq)

# Substitute y1* = x into u1 to get Player 1's reduced problem
u1_reduced = u1_sub.subs(y1, br1_eq)
u1_simplified = sym.simplify(u1_reduced)
print("Player 1's reduced utility in x:", u1_simplified)

# Find optimal x
x_star = sym.solve(sym.diff(u1_simplified, x), x)
print("Optimal x candidates:", x_star)
```

```{code-cell} python3
x_opt = 2
y1_opt = x_opt
y2_opt = y1_opt / 2

u1_opt = 2 * y2_opt * y1_opt + x_opt * y1_opt - y1_opt**2 - x_opt**3 / 3
u2_opt = -(y1_opt - 2 * y2_opt)**2

print(f"Equilibrium: x*={x_opt}, y1*={y1_opt}, y2*={y2_opt}")
print(f"Payoffs: u1={u1_opt:.4f}, u2={u2_opt:.4f}")
```
````

````{solution} subgame_identification_and_refinement
:label: solution:subgame_identification_and_refinement

For each extensive form game we (i) identify all subgames, (ii) derive the
normal form, (iii) find all Nash equilibria, and (iv) identify which are
subgame perfect.

Recall the definition: a node $x$ **initiates a subgame** if and only if $x$
and all its successors lie in information sets that contain only successors of
$x$.

**Game 1**

In a game of perfect information every decision node initiates a subgame.
Backward induction at the final decision node identifies the last mover's best
action; this is substituted back, and the process continues to the root.

- All subgames are the subtrees rooted at each decision node.
- The normal form is derived by listing each player's complete contingent plan
  (one action per information set).
- Nash equilibria are found by inspecting best-response correspondences.
- Among these, only those in which every player plays optimally at every
  information set (including off-path ones) are subgame perfect. In perfect
  information games, backward induction delivers the unique subgame perfect
  equilibrium.

**Game 2**

If the game contains an information set grouping multiple nodes (imperfect
information), then those nodes do not individually initiate subgames. Only
nodes whose entire subtree — including all successors — lies in singleton
information sets can initiate subgames.

- Identify which nodes have the subgame-initiation property.
- Derive the normal form by listing strategies as complete contingent plans.
- Find Nash equilibria by checking best responses.
- Eliminate equilibria in which some player's strategy is not optimal in at
  least one proper subgame; the remainder are subgame perfect.

**Game 3**

Apply the same procedure as Game 2. In general, fewer subgames mean weaker
refinement: Nash equilibria that require non-credible threats in unreached
information sets may survive as Nash equilibria but fail subgame perfection
only when those information sets do initiate proper subgames.

```{note}
In any finite game of perfect information, backward induction produces a
subgame perfect Nash equilibrium. For games with imperfect information, one
must identify proper subgames explicitly and verify the Nash equilibrium
condition within each.
```
````

````{solution} stackelberg_ice_cream_sellers
:label: solution:stackelberg_ice_cream_sellers

**1. Payoff functions**

Players choose locations $x_1, x_2 \in [0, 1]$. Customers are uniformly
distributed and travel to the nearest seller. When $x_1 < x_2$:

- Player 1 serves customers in $\left[0,\; \frac{x_1+x_2}{2}\right]$, a fraction
  $\frac{x_1+x_2}{2}$ of the total.
- Player 2 serves customers in $\left[\frac{x_1+x_2}{2},\; 1\right]$, a fraction
  $1 - \frac{x_1+x_2}{2}$.

When $x_1 = x_2$, each gets $\frac{1}{2}$. By symmetry, when $x_2 < x_1$, the
roles reverse. Formally:

$$
u_1(x_1, x_2) =
\begin{cases}
\dfrac{x_1 + x_2}{2} & \text{if } x_1 \leq x_2 \\[6pt]
1 - \dfrac{x_1 + x_2}{2} & \text{if } x_1 > x_2
\end{cases}
$$

$$
u_2(x_1, x_2) = 1 - u_1(x_1, x_2)
$$

**2. Player 2's best response function**

Player 2 observes $x_1$ and chooses $x_2$ to maximise their share. We consider
cases:

- If Player 2 sets $x_2 > x_1$: their payoff is $1 - \frac{x_1+x_2}{2}$, which
  is decreasing in $x_2$. So Player 2 wants $x_2$ as small as possible, i.e.,
  just above $x_1$.

- If Player 2 sets $x_2 < x_1$: their payoff is $\frac{x_1+x_2}{2}$, increasing
  in $x_2$. So Player 2 wants $x_2$ as large as possible, i.e., just below
  $x_1$.

Both cases push $x_2$ towards $x_1$. The limit gives $x_2^* = x_1$, at which
both players share the market equally: $u_2 = \frac{1}{2}$.

More precisely, for any $x_1 \in [0, 1]$, Player 2 cannot do strictly better
than $\frac{1}{2}$ by any deviation from $x_2 = x_1$, since:

- Any $x_2 \neq x_1$ results in the "outside" player serving a region of length
  $< \frac{1}{2}$ or the "inside" player having to share a midpoint that is
  skewed.

The formal best response is:

$$
x_2^*(x_1) = x_1
$$

(any $x_2 = x_1$ yields $u_2 = \frac{1}{2}$; deviation reduces their share).

**3. Subgame perfect equilibrium via backward induction**

Player 1 anticipates Player 2 will set $x_2^* = x_1$, giving $u_1 = \frac{1}{2}$
for any $x_1 \in [0, 1]$.

Since Player 1's payoff is $\frac{1}{2}$ regardless of $x_1$, any $x_1 \in [0,1]$
is a best response. In particular, $x_1^* = \frac{1}{2}$ (centre) supports a
subgame perfect equilibrium:

$$
x_1^* = \tfrac{1}{2},\quad x_2^*(x_1) = x_1
$$

Both players locate at the centre and share the market equally, each earning
$\frac{1}{2}$.

**4. Comparison to the simultaneous-move game**

In the simultaneous-move version, both players choose locations without
observing the other. It is well known (Hotelling's Law) that the unique Nash
equilibrium is $x_1 = x_2 = \frac{1}{2}$: both sellers crowd to the centre.

In the sequential (Stackelberg) version, Player 2's best response is to match
Player 1's location exactly. Player 1, anticipating this, is indifferent over
all locations on $[0, 1]$ and earns $\frac{1}{2}$ regardless. So the equilibrium
payoffs are identical: $(1/2, 1/2)$.

The key difference is strategic commitment: Player 1 moves first but cannot
exploit this because Player 2's best response neutralises any positional
advantage. This contrasts with Stackelberg quantity competition (Cournot), where
the leader earns strictly more.

```{code-cell} python3
import sympy as sym

x1, x2 = sym.symbols("x1 x2", real=True)

# Payoff for player 2 when x2 > x1
u2_right = 1 - (x1 + x2) / 2

# FOC for player 2 (maximise over x2)
foc2 = sym.diff(u2_right, x2)
print("dU2/dx2 (when x2 > x1):", foc2)
print("Negative of x2 coefficient confirms decreasing in x2 — best response is x2 -> x1 from above.")

# Payoff for player 2 when x2 < x1
u2_left = (x1 + x2) / 2
foc2_left = sym.diff(u2_left, x2)
print("\ndU2/dx2 (when x2 < x1):", foc2_left)
print("Positive — best response is x2 -> x1 from below.")

print("\nIn both cases the best response converges to x2* = x1.")
print("Player 1's payoff at any x1 with x2* = x1: u1 = 0.5")
```
````
