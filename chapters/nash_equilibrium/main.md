---
kernelspec:
  name: python3
  display_name: "Python 3"
---

(chp:nash_equilibrium)=

# Nash Equilibrium

(sec:motivating_example_nash_equilibrium)=

### Motivating Example

In the [Coordination Game](#sec:motivating-example-zero-sum-games), in how many  
situations do neither player have an incentive to **independently** change  
their strategy?

Neither player having a reason to change their strategy implies that both  
strategies are [best responses](#sec:best_responses) to each other.

Recall that for the **Coordination game** is defined by:

$$
M_r = \begin{pmatrix}
3 & 1 \\
0 & 2
\end{pmatrix}
\qquad
M_c = \begin{pmatrix}
2 & 1 \\
0 & 3
\end{pmatrix}
$$

If we consider strategies that only play a single action, there are two options
for each strategy:

$$
\sigma_1 \in \{(1, 0), (0, 1)\}
$$

and:

$$
\sigma_2 \in \{(1, 0), (0, 1)\}
$$

We will inspect all four combinations:

- $\sigma_1 = (1, 0)$ and $\sigma_2 = (1, 0)$ corresponds to both players
  playing their first action, which gives:
  $u_r(\sigma_1, \sigma_2) = 3$ and $u_c(\sigma_1, \sigma_2) = 2$.  
  If the row player were to modify their strategy (while the column player
  stayed unchanged) to play the second action, their utility would decrease.
  Likewise, if the column player were to modify their strategy, their utility
  would also decrease.

- $\sigma_1 = (1, 0)$ and $\sigma_2 = (0, 1)$ corresponds to the row player
  playing their first action and the column player playing their second action,
  which gives: $u_r(\sigma_1, \sigma_2) = 1$ and $u_c(\sigma_1, \sigma_2) = 1$.  
  In this case, if either player were to move, their utility would increase.

- $\sigma_1 = (0, 1)$ and $\sigma_2 = (1, 0)$ corresponds to the row player
  playing their second action and the column player playing their first action,
  which gives: $u_r(\sigma_1, \sigma_2) = 0$ and $u_c(\sigma_1, \sigma_2) = 0$.  
  In this case, if either player were to move, their utility would increase.

- $\sigma_1 = (0, 1)$ and $\sigma_2 = (0, 1)$ corresponds to both players
  playing their second action, which gives:
  $u_r(\sigma_1, \sigma_2) = 2$ and $u_c(\sigma_1, \sigma_2) = 3$.  
  If the row player were to modify their strategy (while the column player
  stayed unchanged), their utility would decrease. Likewise, if the column
  player were to modify their strategy, their utility would also decrease.

Is there another pair of strategies that are best responses to each other and
will such a pair always exist for any game?

## Theory

A pair of strategies that are best responses to each other is a Nash
equilibrium.

### Definition: Nash Equilibria

---

In an $N$-player normal form game, a **Nash equilibrium** is a strategy profile  
$\tilde{s} = (\tilde{s}_1, \tilde{s}_2, \dots, \tilde{s}_N)$ such that:

$$
u_i(\tilde{s}) = \max_{\bar{s}_i \in \Delta(\mathcal{A}_i)} u_i(\bar{s}_i, \tilde{s}_{-i}) \quad \text{for all } i
$$

---

```{warning}
In many game theory texts, Nash equilibria in normal form games are referred to as
either pure strategy Nash equilibria, where each player chooses a single
action with certainty, or mixed strategy Nash equilibria, where players
randomise over multiple actions with positive probability.
```

The following algorithm gives an approach to use the [best response condition](#thrm:best_response_condition)
to systematically find all Nash equilibrium.

(def:support_enumeration_algorithm)=

### Definition: Support Enumeration Algorithm

The algorithm proceeds as follows:

For a two-player game  
$(M_r, M_c) \in \left(\mathbb{R}^{m \times n}\right)^2$, the following algorithm  
returns all pairs of best responses:

1. For all pairs of supports (subsets of the action space)
   $(I, J)$:
2. Solve the following equations (to ensure best responses):

   $$
   \sum_{i \in I} {\sigma_{r}}_i {M_{c}}_{ij} = v \quad \text{for all } j \in J
   $$

   $$
   \sum_{j \in J} {M_r}_{ij} {\sigma_{c}}_j = u \quad \text{for all } i \in I
   $$

3. Solve the normalisation and non-negativity constraints:

   - $\sum_{i=1}^m {\sigma_{r}}_i = 1$ and ${\sigma_1}_i \geq 0$ for all $i$
   - $\sum_{j=1}^n {\sigma_{c}}_j = 1$ and ${\sigma_2}_j \geq 0$ for all $j$

4. Check the best response condition.

Repeat steps 2–4 for all potential pairs of actions.

```{note}
The algorithm is described in the context of $N=2$ players here.

It is a direct application of the [best response condition](#thrm:best_response_condition)
and can be generalised to larger $N$.
```

### Example: Support enumeration algorithm for the coordination game

Let us apply the support enumeration algorithm to
[the coordination game](#sec:motivating_example_nash_equilibrium).

The following supports (subsets of the action space) need to be considered:

$$
I \in \{\{r_1\}, \{r_2\}, \{r_1, r_2\}\}
$$

and

$$
J \in \{\{c_1\}, \{c_2\}, \{c_1, c_2\}\}
$$

For the cases where $|I|=|J|=1$ steps 2, 3 and 4 of the [support enumeration
algorithm](#def:support_enumeration_algorithm) correspond to finding best
responses in the action space. This can be done by [highlighting best
responses](#exam:predicted_behaviour_through_best_responses_in_the_action_space):

$$
M_r = \begin{pmatrix}
\underline{3} & 1 \\
0 & \underline{2}
\end{pmatrix}
\qquad
M_c = \begin{pmatrix}
\underline{2} & 1 \\
0 & \underline{3}
\end{pmatrix}
$$

The support enumeration algorithm for $|I|=|J|=1$ gives the two following Nash
equilibria:

$$
((1, 0), (1, 0)) \qquad ((0, 1), (0, 1))
$$

```{note}
For $|I|\neq |J|$ we can omit steps 2, 3 and 4 as there is a single given best response to an
action in each action space. For example, we do not need to consider
specifically if there is a Nash equilibrium when the row player plays the first
row and the column player plays both the first and the second column (since the
utility for those two columns is not the same. This will be tackled formaly in
[](#def:degenerate_games).
```

The final pair of actions to consider is when $I=(r_1, r_2)$ and $J=(c_1, c_2$.
In this case let:

$$\sigma_1=(x, 1 - x)\qquad \sigma_2=(y,1-y)$$

for $0 < x < 1$ and $0 < y < 1$.

Step 2 corresponds to setting:

$$
\begin{align*}
\sum_{i \in I} {\sigma_{r}}_i {M_{c}}_{i1} = 2 x + 0 (1-x) &= v\\
\sum_{i \in I} {\sigma_{r}}_i {M_{c}}_{i2} = 1 x + 3 (1 -x) &= v
\end{align*}
$$

and

$$
\begin{align*}
\sum_{j \in J} {M_r}_{1j} {\sigma_{c}}_j = 3y + 1(1-y) &= u \\
\sum_{j \in J} {M_r}_{2j} {\sigma_{c}}_j = 0y + 2(1-y) &= u \\
\end{align*}
$$

The particular values of $u$ or $v$ are not required so we can equate these
pairs of
expressions:

$$
\begin{align*}
2x = x + 3-3x &\implies x =\frac{3}{4}\\
3y + 1-y = 2 - 2y &\implies y =\frac{1}{4}\\
\end{align*}
$$

Giving: $\sigma_1 = (3/4, 1/4)$ and $\sigma_2=(1/4, 3/4)$.

Step 3 already holds as we enforced $\sigma_1 = (x, 1 - x)$ and $\sigma_2 = (y,
1 - y)$ at the start of our calculations. This is not necessarily the case for
larger games.

The final step, step 4, requires us to check the [best response
condition](#thrm:best_response_condition). This is to check that there exists no
better choice of action outside of the chosen set of $I$ and $J$. This is more
relevant for games with larger action spaces but let us nonetheless carry out
the calculations:

$$M_r \sigma_2^\mathsf{T}= \begin{pmatrix}3/2 \\ 3/2\end{pmatrix}$$

and

$$
\sigma_1 M_c = \begin{pmatrix}3/2 & 3/2\end{pmatrix}
$$

as required by the best response condition. The support enumeration algorithm
has given 3 Nash equilibria:

$$
\left\{
    ((1, 0), (1, 0)),
    ((0, 1), (0, 1)),
    ((\frac{3}{4}, \frac{1}{4}), (\frac{1}{4}, \frac{3}{4})),
\right\}
$$

The support enumeration algorithm is one of many algorithms that can be used to
compute Nash equilibrium. Like most of the algorithms it works well for "most"
games. When games are "degenerate" it may need more calculations and fail to
give all equilibria.

(def:degenerate_games)=

### Definition: Degenerate Games

---

A two player game is called non degenerate if no strategy of support size $k$ has more than $k$ best response actions.

---

(exam:support_enumeration_for_a_degenerate_game)=

### Example: Support Enumeration for a degenerate game

Let us use support enumeration for the following game.

$$
    M_r =
      \begin{pmatrix}
           2 & 5 \\
           0 & 5\\
      \end{pmatrix}
\qquad
    M_c =
      \begin{pmatrix}
           2 & 1 \\
           0 & 1\\
      \end{pmatrix}
$$

First, we note that this game is degenerate, there are two best responses in
action space to the first column:

$$
    M_r =
      \begin{pmatrix}
           \underline{2} & \underline{5} \\
           0 & \underline{5}\\
      \end{pmatrix}
\qquad
    M_c =
      \begin{pmatrix}
           \underline{2} & 1 \\
           0 & \underline{1}\\
      \end{pmatrix}
$$

Evaluating best responses in action space gives Nash equilibria:

$$
((1, 0), (1, 0)) \qquad ((0, 1), (0, 1))
$$

We need to consider new pairs of supports:

- $\sigma_1=(x, 1-x)$ and $\sigma_2 = (1, 0)$: there is single best response to
  the first column so nothing else to consider here.
- $\sigma_1=(x, 1-x)$ and $\sigma_2 = (0, 1)$: step 2 holds for all $x$, step 3
  is already satisfied (the vectors are both probability distributions) thus we
  are left to check the best response condition:
  $$_sigma_1M_c=(2x, 1)$$
  the only value of $x$ that gives a pair of best response is when the column
  player has no incentive to move from the support thus $2x=1 \implies x=1/2$.

## Exercises

### Exercise: Support Enumeration

Use support enumeration to find Nash equilibria for the following games:

1.

$$
A =
\begin{pmatrix}
3  & 3 & 2 \\
2  & 1 & 3
\end{pmatrix}
\qquad
B =
\begin{pmatrix}
2  & 1 & 3 \\
2  & 3 & 2
\end{pmatrix}
$$

2.

$$
A =
\begin{pmatrix}
3 & -1 \\
2 & 7
\end{pmatrix}
\qquad
B =
\begin{pmatrix}
-3 & 1 \\
1 & -6
\end{pmatrix}
$$

### Exercise: Penalty kick strategies and Nash equilibrium

A soccer player (Player 1) is taking a penalty kick and can shoot either left or  
right: $S_1 = \{\text{SL}, \text{SR}\}$. The goalie (Player 2) can dive left or  
right: $S_2 = \{\text{DL}, \text{DR}\}$. The probabilities of scoring a goal  
(depending on the chosen strategies) are shown in the matrix below:

$$
\begin{pmatrix}
0.8 & 0.15 \\
0.2 & 0.95
\end{pmatrix}
$$

Assume the utility to Player 1 is the probability of scoring, and the utility  
to Player 2 is the probability of preventing a goal. What is the Nash  
equilibrium of this game?

Now suppose Player 1 has a third strategy: shooting in the middle. The new  
action set becomes $S_1 = \{\text{SL}, \text{SM}, \text{SR}\}$. The updated  
probability matrix is:

$$
\begin{pmatrix}
0.8 & 0.15 \\
0.5 & 0.5 \\
0.2 & 0.95
\end{pmatrix}
$$

Determine the new Nash equilibrium for the extended game.

## Programming

The Nashpy library has an implementation of the support enumeration algorithm.
First let us create the payoff matrices and the game:

```{code-cell} python3
import numpy as np
import nashpy as nash

A = np.array(
    (
        (3, 1),
        (0, 2),
    )
)
B = np.array(
    (
        (2, 1),
        (0, 3),
    )
)

coordination_game = nash.Game(A, B)
coordination_game
```

Now to use the support enumeration algorithm:

```{code-cell} python3
list(coordination_game.support_enumeration())
```

```{note}
The Nashpy library uses a concept called a generator which allows us to
efficiently create the steps of an algorithm without using resources. The call
to transform the generator in to a `list` empties the generator to actually go
through the steps of the algorithm.
```

## Notable Research

Support enumeration is as close to a "from first principles" algorithm for
computing Nash equilibria. Thus there is no specific paper to point to as per
its formulation. Or indeed there is no specific set of papers that use it for
their findings although a lot of papers that consider small games are in essence
using support enumeration.

For example in [@chiappori2002testing] theoretical results are given regarding
penalty kicks that rely
on the indifference ensured by the best response condition which is in turn
essentially an application of the support enumeration algorithm.

A similar paper applied to another animal conservation is [@lee2016devaluing] in
which the authors build a theoretical model of the effectiveness of Rhino horn
devaluation. Once again the calculation presented are essentially an application
of the support enumeration algorithm.

In [@knight2017measuring] whilst a different algorithm is used to identify Nash
equilibrium for strategic hospital interactions it is somewhat similar to the
support enumeration algorithm except that it takes advantage of the specific
structure of the game considered.

## Conclusion

This chapter introduced the concept of Nash equilibrium and demonstrated a  
systematic method for identifying all equilibria in a two-player game using the  
**support enumeration algorithm**. This method is rooted directly in the best  
response condition and provides a computational approach that works well for  
many games, particularly when the number of actions is small.

It is important to recognise that the support enumeration algorithm is  
conceptually simple but can become computationally expensive as the action  
spaces grow. Nevertheless, it serves as a useful tool both in theory and in  
practice, particularly for small-scale empirical models.

[](#tbl:ne_summary) summarises the core concepts introduced in this chapter.

```{table} The main concepts of Nash equilibrium
:label: tbl:ne_summary
:align: center
:class: table-bordered


| Concept                       | Description                                                                        |
| ----------------------------- | ---------------------------------------------------------------------------------- |
| Nash equilibrium              | A strategy profile where each player's strategy is a best response to the others'  |
| Support of a strategy         | The set of actions played with positive probability                                |
| Support enumeration algorithm | Enumerates possible supports and checks conditions for equilibrium                 |
| Degenerate game               | A game in which some strategy of support size $k$ has more than $k$ best responses |

```

---

```{attention}
Support enumeration embodies the best response condition and provides an
accessible, transparent algorithm for computing all equilibria in two-player
games.
```
