---
kernelspec:
  name: python3
  display_name: "Python 3"
---

(chp:the_core)=

# The Core

The Shapley value asks how to divide the value of a coalition _fairly_. It says
nothing about whether the players will accept that division. This chapter studies
the **core**, the set of allocations that are _stable_ in the sense that no group
of players can do better by breaking away. Fairness and stability are different
demands, and as we will see they need not agree.

(motivating_example:will_the_party_stick_together)=

## Motivating Example: Will the party stick together?

Recall the [D&D battle](#motivating_example:dnd_battle) from the previous
chapter, in which Ren, Azel, and Quinn divide 1,000 gold coins. The
[Shapley value](#chp:cooperative_games) divides the hoard fairly, giving

$$
\phi = (\phi_{\text{Ren}}, \phi_{\text{Azel}}, \phi_{\text{Quinn}})
= (350, 450, 200).
$$

This is a fair split: each character receives their average marginal
contribution. But is it stable? Recall that Ren and Azel together can secure
900 coins on their own, since $v(\{\text{Ren}, \text{Azel}\}) = 900$. Under the
Shapley value they receive only $350 + 450 = 800$ between them. The two of them
would do better to walk away from Quinn and split the 900 they can earn alone.

The fair allocation is therefore not stable: a sub-group is being short-changed
relative to what it could guarantee itself. If the party is to stay together,
the division must give every coalition at least what it could secure on its own.
The set of allocations meeting that demand is the subject of this chapter.

## Theory

(sec:definition_of_imputation)=

### Definition: Imputation

---

Given a characteristic function game $G = (N, v)$, a **payoff vector**
$x \in \mathbb{R}^N$ is an **imputation** if it is:

- **efficient**: $\sum_{i \in N} x_i = v(N)$, the whole value of the grand
  coalition is shared out; and
- **individually rational**: $x_i \geq v(\{i\})$ for every player $i$, so that
  no player receives less than they could secure alone.

---

Individual rationality is the weakest possible stability requirement: it asks
only that no _single_ player wishes to leave. The core strengthens this to every
coalition.

#### Example: Imputations of the D&D battle

For the [D&D battle](#motivating_example:dnd_battle) the grand coalition is worth
$v(N) = 1000$ and each player alone is worth $v(\{i\}) = 0$, so a payoff vector
is an imputation precisely when it sums to 1000 and gives every player a
non-negative amount. The Shapley value $(350, 450, 200)$ is an imputation, and so
is the lopsided split $(1000, 0, 0)$ in which Ren takes everything. The vector
$(1100, -100, 0)$ is **not** an imputation: it is efficient, but Azel receives
$-100 < v(\{\text{Azel}\}) = 0$, less than they could secure alone. Individual
rationality alone permits a great many allocations; the core will cut them down.

(sec:definition_of_the_core)=

### Definition: The Core

---

The **core** of a characteristic function game $G = (N, v)$ is the set of
efficient payoff vectors on which no coalition can improve:

$$
\mathcal{C}(G) = \left\{
x \in \mathbb{R}^N \;\middle|\;
\sum_{i \in N} x_i = v(N)
\text{ and }
\sum_{i \in C} x_i \geq v(C)
\text{ for all } C \subseteq N
\right\}.
$$

---

The defining inequalities are the **coalitional rationality** constraints: every
coalition $C$ must receive, in total, at least the value $v(C)$ it could secure
by itself. A coalition for which $\sum_{i \in C} x_i < v(C)$ is said to
**block** the allocation $x$; the core is exactly the set of efficient,
unblocked allocations. Since the singleton constraints $x_i \geq v(\{i\})$ are
among the coalitional ones, every core allocation is an imputation, but the
converse need not hold.

```{note}
The core is a **polytope**: it is the set of points in $\mathbb{R}^N$ satisfying
one linear equality and a finite collection of linear inequalities, one per
coalition. It may be empty, a single point, or a higher-dimensional region.
This is the same polytope structure studied in
[](#chp:best_response_polytopes), and as we will see it makes core membership a
question of linear programming.
```

#### Example: The core of the D&D battle

For the [D&D battle](#motivating_example:dnd_battle), an allocation
$x = (x_{\text{Ren}}, x_{\text{Azel}}, x_{\text{Quinn}})$ is in the core if it is
efficient, $x_{\text{Ren}} + x_{\text{Azel}} + x_{\text{Quinn}} = 1000$, and no
coalition can block it:

$$
\begin{align*}
x_{\text{Ren}} + x_{\text{Azel}} &\geq 900, \\
x_{\text{Ren}} + x_{\text{Quinn}} &\geq 400, \\
x_{\text{Azel}} + x_{\text{Quinn}} &\geq 600, \\
x_{\text{Ren}}, x_{\text{Azel}}, x_{\text{Quinn}} &\geq 0.
\end{align*}
$$

The Shapley value $(350, 450, 200)$ violates the first inequality, since
$350 + 450 = 800 < 900$, confirming that it is not in the core. A stable
allocation must give the strong pair $\{\text{Ren}, \text{Azel}\}$ at least 900
between them. The allocation $(350, 600, 50)$ satisfies every inequality
($950 \geq 900$, $400 \geq 400$, $650 \geq 600$) and so lies in the core: the
party will stay together under it. The core here is not empty, but the fair
allocation lies outside it.

(sec:definition_of_convex_game)=

### Definition: Convex game

---

A characteristic function game $G = (N, v)$ is **convex** (or supermodular) if

$$
v(S \cup T) + v(S \cap T) \geq v(S) + v(T)
\quad \text{for all coalitions } S, T \subseteq N.
$$

---

Equivalently, a game is convex when the marginal contribution of a player to a
coalition never decreases as the coalition grows: players become more valuable
as more of the others join. Convexity is stronger than superadditivity, which is
the special case where $S$ and $T$ are disjoint.

#### Example: The D&D battle is not convex

In the [D&D battle](#motivating_example:dnd_battle), adding Quinn to the coalition
$\{\text{Ren}\}$ raises its value by
$v(\{\text{Ren}, \text{Quinn}\}) - v(\{\text{Ren}\}) = 400$, while adding Quinn to
the larger coalition $\{\text{Ren}, \text{Azel}\}$ raises it by only
$v(N) - v(\{\text{Ren}, \text{Azel}\}) = 100$. Quinn's marginal contribution
_falls_ as the coalition grows, so the game is not convex. This is exactly why,
as the next theorem makes precise, its fair and stable allocations can come
apart.

### Theorem: Convex games have a non-empty core

---

If $G = (N, v)$ is convex, then its core is non-empty and contains the Shapley
value.

---

We state this result without proof; it is due to Shapley [@shapley1971cores].
Convexity is therefore a convenient sufficient condition: for a convex game the
fair allocation and a stable allocation coincide, because the Shapley value is
itself in the core. The D&D battle shows that without convexity the two can come
apart: it is not convex, as the example above shows, and its Shapley value lies
outside its core.

(sec:theorem_bondareva_shapley)=

### Theorem: The Bondareva–Shapley theorem

The core may be empty, and there is an exact condition for when it is not. A
collection of weights $(\lambda_C)_{C \subseteq N,\, C \neq \emptyset}$ with
$\lambda_C \geq 0$ is **balanced** if, for every player $i$,
$\sum_{C \,:\, i \in C} \lambda_C = 1$. The game is **balanced** if for every such
balanced collection $\sum_{C} \lambda_C v(C) \leq v(N)$.

---

The core of $G = (N, v)$ is non-empty if and only if the game is balanced.

---

We state the theorem, due independently to Bondareva and Shapley, without proof.
Its practical content is that core non-emptiness is a **linear programming**
question. The core is non-empty precisely when the linear program

$$
\text{minimise} \sum_{i \in N} x_i
\quad \text{subject to} \quad
\sum_{i \in C} x_i \geq v(C) \text{ for all } C \neq \emptyset
$$

has optimal value equal to $v(N)$; the balancedness condition is exactly the
statement that the dual of this program never exceeds $v(N)$. When the optimum
equals $v(N)$, the optimal $x$ is itself a point of the core.

```{note}
An empty core is a strong statement about a game: it means that _no_ division of
$v(N)$ is stable. Whatever allocation is proposed, some coalition can guarantee
its members strictly more than they are offered and will break away, so the
grand coalition cannot be held together by any binding agreement. The
three-player majority game of [](#core_empty_majority_game) is the classic
example: every split of the surplus is overturned by some two-player majority,
and the bargaining never settles.
```

(sec:definition_of_the_nucleolus)=

### Definition: The nucleolus

When the core is non-empty it is usually not a single point, and we may want to
select one allocation from it. For a payoff vector $x$ and coalition $C$, the
**excess** $e(C, x) = v(C) - \sum_{i \in C} x_i$ measures how dissatisfied $C$
is with $x$: a positive excess means $C$ is blocking. The **nucleolus** is the
imputation that lexicographically minimises the vector of excesses sorted from
largest to smallest, that is, it first makes the most dissatisfied coalition as
satisfied as possible, then the next, and so on.

The nucleolus always exists, is unique, and whenever the core is non-empty it
lies in the core. It can be read as the most stable allocation of all: it pushes
every coalition as far from blocking as the game allows.

#### Example: The nucleolus of the D&D battle

For the [D&D battle](#motivating_example:dnd_battle) the singleton coalitions
have excess $e(\{i\}, x) = -x_i \leq 0$ and so are never the most dissatisfied;
the binding coalitions are the three pairs. Using efficiency
$x_{\text{Ren}} + x_{\text{Azel}} + x_{\text{Quinn}} = 1000$, their excesses are

$$
\begin{align*}
e(\{\text{Ren}, \text{Azel}\}, x) &= 900 - (x_{\text{Ren}} + x_{\text{Azel}})
  = x_{\text{Quinn}} - 100, \\
e(\{\text{Ren}, \text{Quinn}\}, x) &= 400 - (x_{\text{Ren}} + x_{\text{Quinn}})
  = x_{\text{Azel}} - 600, \\
e(\{\text{Azel}, \text{Quinn}\}, x) &= 600 - (x_{\text{Azel}} + x_{\text{Quinn}})
  = x_{\text{Ren}} - 400.
\end{align*}
$$

These three excesses always sum to $1000 - 1100 = -100$, so the largest of them
is at least the average $-100/3$, with equality only when all three are equal.
The nucleolus makes the largest excess as small as possible, and so equalises
them, giving

$$
x = \left(\tfrac{1100}{3},\, \tfrac{1700}{3},\, \tfrac{200}{3}\right)
\approx (366.7,\, 566.7,\, 66.7).
$$

This allocation lies in the core, and it differs from both the Shapley value
$(350, 450, 200)$ and the core allocation $(350, 600, 50)$ met earlier: the
nucleolus is the single division that holds every coalition as far from blocking
as the game permits.

## Exercises

```{exercise}
:label: core_imputation_versus_core

Consider the three-player game with

$$
v(C) = \begin{cases}
0 & \text{if } |C| \leq 1 \\
7 & \text{if } C = \{1, 2\} \\
5 & \text{if } C = \{1, 3\} \\
5 & \text{if } C = \{2, 3\} \\
9 & \text{if } C = \{1, 2, 3\}.
\end{cases}
$$

1. Show that the allocation $(3, 3, 3)$ is an imputation.
2. Determine whether $(3, 3, 3)$ is in the core. If not, identify a blocking
   coalition.
3. Find an allocation that is in the core.
```

```{exercise}
:label: core_empty_majority_game

Consider the three-player majority game, in which any coalition of two or more
players can secure the whole value:

$$
v(C) = \begin{cases}
1 & \text{if } |C| \geq 2 \\
0 & \text{otherwise.}
\end{cases}
$$

Prove that the core is empty.
```

```{exercise}
:label: core_convex_game

Consider the game $v(C) = |C|^2$ on three players.

1. Verify that the game is convex.
2. Compute the Shapley value.
3. Confirm that the Shapley value lies in the core.
```

```{exercise}
:label: core_glove_market

In a glove market, players 1 and 2 each own a left glove and player 3 owns a
right glove. A matched pair of gloves is worth 1, so the value of a coalition is
the number of complete pairs it can form:

$$
v(C) = \min(\ell, r),
$$

where $\ell$ and $r$ are the numbers of left and right gloves held by the
members of $C$.

1. Write down the characteristic function.
2. Find the core, and interpret the result.
```

## Programming

The `coopgt` library can check whether a payoff vector is an imputation or lies
in the core, and whether a game is convex. We continue with the
[D&D battle](#motivating_example:dnd_battle).

```{code-cell} python3
import coopgt.core
import coopgt.shapley_value

characteristic_function = {
    (): 0,
    (1,): 0,
    (2,): 0,
    (3,): 0,
    (1, 2): 900,
    (1, 3): 400,
    (2, 3): 600,
    (1, 2, 3): 1000,
}

shapley = coopgt.shapley_value.calculate(characteristic_function)
print(f"Shapley value: {shapley}")
```

The Shapley value is fair, but it is not in the core, because the coalition
$\{1, 2\}$ can block it:

```{code-cell} python3
print(f"Shapley value in the core? {coopgt.core.is_in_core(characteristic_function, shapley)}")
```

The game is not convex, which is why fairness and stability come apart:

```{code-cell} python3
print(f"Game convex? {coopgt.core.is_convex(characteristic_function)}")
```

By the [Bondareva–Shapley theorem](#sec:theorem_bondareva_shapley) the core is
non-empty exactly when the game is balanced. `coopgt` finds a point of the core
by solving the associated linear program, returning `None` when the core is
empty:

```{code-cell} python3
core_point = coopgt.core.find_core_point(characteristic_function)
print(f"A point in the core: {core_point}")
```

An allocation is returned rather than `None`, so the core is non-empty, and we
can confirm that the allocation it found is indeed a point of the core:

```{code-cell} python3
print(f"Found allocation in the core? {coopgt.core.is_in_core(characteristic_function, core_point)}")
```

```{note}
The core-membership functions used here are part of `coopgt` from version
`0.0.3`. Earlier versions provide only the Shapley value and the characteristic
function property checks.
```

## Notable Research

The core was introduced by Gillies [@gillies1959solutions] as part of his study
of stable allocations in cooperative games, building on the stable-set ideas of
von Neumann and Morgenstern. The exact condition for the core to be non-empty
was established independently by Bondareva [@bondareva1963theory] and Shapley
[@shapley1967balanced] in the balancedness theorem that now bears both their
names, tying core non-emptiness to linear programming duality.

Shapley [@shapley1971cores] showed that convex games always have a non-empty
core whose extreme points are the marginal-contribution vectors, and that the
Shapley value is their barycentre and hence always in the core. The nucleolus
was introduced by Schmeidler [@schmeidler1969nucleolus], who proved that it
always exists, is unique, and lies in the core whenever the core is non-empty.

Cooperative solution concepts of this kind underpin practical cost-sharing and
resource-allocation schemes, from apportioning the cost of shared
infrastructure to allocating gains in collaborative logistics, where stability
is what keeps a coalition of firms or municipalities from walking away.

## Conclusion

In this chapter we studied the **core**, the set of allocations that no
coalition can improve upon. Where the Shapley value answers the question of
_fairness_, the core answers the question of _stability_, and the
[D&D battle](#motivating_example:dnd_battle) shows that the two can disagree:
the fair allocation left the strong pair worse off than they could be alone.

We saw that the core is a polytope, that it can be empty, and that the
**Bondareva–Shapley theorem** characterises non-emptiness through balancedness,
turning the question into a linear program. **Convex games** are a well-behaved
class for which the core is always non-empty and contains the Shapley value, so
that fairness and stability coincide. Finally the **nucleolus** selects a single,
maximally stable allocation from the core whenever one exists.

[](#tbl:the_core_summary) summarises the concepts of this chapter.

```{table} Summary of core concepts
:label: tbl:the_core_summary
:align: center
:class: table-bordered

| Concept | Description |
|---|---|
| Imputation | An efficient, individually rational payoff vector |
| Core | The efficient allocations no coalition can block |
| Blocking coalition | A coalition $C$ with $\sum_{i \in C} x_i < v(C)$ |
| Convex game | A game with $v(S \cup T) + v(S \cap T) \geq v(S) + v(T)$ |
| Bondareva–Shapley theorem | The core is non-empty if and only if the game is balanced |
| Nucleolus | The unique imputation lexicographically minimising excesses |
```

```{important}
The core is the set of efficient allocations that are stable against every
coalition. It can be empty; the Bondareva–Shapley theorem says it is non-empty
exactly when the game is balanced, and convex games are always balanced.
```

---

(solutions:the_core)=

## Solutions

```{solution} core_imputation_versus_core
:label: solution:core_imputation_versus_core

1. The allocation $(3, 3, 3)$ is efficient, since $3 + 3 + 3 = 9 = v(\{1,2,3\})$,
   and individually rational, since each player receives $3 \geq 0 = v(\{i\})$.
   It is therefore an imputation.

2. The coalition $\{1, 2\}$ receives $3 + 3 = 6$, but $v(\{1, 2\}) = 7$. Since
   $6 < 7$, the coalition $\{1, 2\}$ blocks the allocation, so $(3, 3, 3)$ is
   **not** in the core.

3. A core allocation must satisfy $x_1 + x_2 \geq 7$, $x_1 + x_3 \geq 5$,
   $x_2 + x_3 \geq 5$, and $x_1 + x_2 + x_3 = 9$. The first condition forces
   $x_3 \leq 2$, and the other two force $x_1 \geq 3$ and $x_2 \geq 3$. The
   allocation $(3.5, 3.5, 2)$ satisfies all of them: $7 \geq 7$, $5.5 \geq 5$,
   and $5.5 \geq 5$. It is therefore in the core.
```

```{solution} core_empty_majority_game
:label: solution:core_empty_majority_game

Suppose, for contradiction, that $x = (x_1, x_2, x_3)$ is in the core. Then each
two-player coalition is unblocked:

$$
x_1 + x_2 \geq 1, \qquad x_1 + x_3 \geq 1, \qquad x_2 + x_3 \geq 1.
$$

Adding these three inequalities gives $2(x_1 + x_2 + x_3) \geq 3$, that is,
$x_1 + x_2 + x_3 \geq 3/2$. But efficiency requires $x_1 + x_2 + x_3 = v(N) = 1$,
and $1 < 3/2$. This is a contradiction, so no such $x$ exists and the core is
empty. There is therefore no stable way to split the unit of value: whichever
two players agree to share it, the third can always tempt one of them into a new
majority, and the bargaining cycles without end.
```

```{solution} core_convex_game
:label: solution:core_convex_game

1. With $v(C) = |C|^2$, write $a = |S|$, $b = |T|$, $u = |S \cap T|$, so that
   $|S \cup T| = a + b - u$. Convexity requires
   $(a + b - u)^2 + u^2 \geq a^2 + b^2$. Expanding the left-hand side gives
   $a^2 + b^2 + 2u^2 + 2ab - 2au - 2bu = a^2 + b^2 + 2(a - u)(b - u)$. Since
   $u = |S \cap T| \leq \min(|S|, |T|)$, both $a - u \geq 0$ and $b - u \geq 0$,
   so the extra term is non-negative and the inequality holds. The game is
   convex.

2. By symmetry the three players are interchangeable, so the Shapley value
   splits $v(N) = 9$ equally: $\phi = (3, 3, 3)$.

3. Each singleton receives $3 \geq 1 = v(\{i\})$, each pair receives
   $6 \geq 4 = v(\{i, j\})$, and the grand coalition receives $9 = v(N)$. No
   coalition can block, so $(3, 3, 3)$ is in the core, as guaranteed by the
   theorem on convex games.
```

```{solution} core_glove_market
:label: solution:core_glove_market

1. Counting complete pairs in each coalition gives

   $$
   v(C) = \begin{cases}
   0 & \text{if } C \in \{\emptyset, \{1\}, \{2\}, \{3\}, \{1, 2\}\} \\
   1 & \text{if } C \in \{\{1, 3\}, \{2, 3\}, \{1, 2, 3\}\}.
   \end{cases}
   $$

   The coalition $\{1, 2\}$ holds two left gloves and no right glove, so
   $v(\{1, 2\}) = 0$.

2. A core allocation satisfies $x_1 + x_3 \geq 1$, $x_2 + x_3 \geq 1$, and
   $x_1 + x_2 + x_3 = 1$ with $x_i \geq 0$. Substituting
   $x_1 = 1 - x_2 - x_3$ into $x_1 + x_3 \geq 1$ gives $1 - x_2 \geq 1$, so
   $x_2 \leq 0$ and hence $x_2 = 0$; by the same argument with players 1 and 2
   exchanged, $x_1 = 0$. Efficiency then forces $x_3 = 1$. The core is the single
   point $(0, 0, 1)$.

   The scarce right glove captures the entire value. Although players 1 and 2 own
   two thirds of the gloves, their gloves are in surplus, so stability awards
   them nothing. The core makes the value of scarcity precise.
```
