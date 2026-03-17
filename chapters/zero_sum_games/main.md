---
kernelspec:
  name: python3
  display_name: "Python 3"
---

(chp:zero_sum_games)=

# Zero-Sum Games

(sec:motivating_example_zero_sum_games)=

## Motivating Example

Consider the standard **Rock-Paper-Scissors** game
The payoff matrix for the row player is:

$$
M = \begin{pmatrix}
  0  & -1 & 1 \\
  1  & 0  & -1\\
  -1 & 1  & 0
\end{pmatrix}
$$

We are going to modify the game to reflect the fact that some row player in
question enjoys winning and hates losing with Paper more than any other action:

$$
M = \begin{pmatrix}
  0  & -1 & 1 \\
  2  & 0  & -2\\
  -1 & 1  & 0
\end{pmatrix}
$$

Is there a way for the **row player** to choose a strategy that guarantees a
certain minimum expected payoff, regardless of how the column player responds?

## Theory

This chapter will consider a specific subset of [](#sec:normal_form_games).

(sec:definition_zero_sum_game)=

### Definition: Zero Sum Game

---

A two player normal form game with payoff matrices $(M_r, M_c) \in {\mathbb{R}^{m\times n}}^2$
is called zero sum if and only if:

$$M_r + M_c = 0$$

---

In the case of a zero sum game we will use the convention of defining it with:

$$M=M_r$$

and implying $M_c=-M$.

### Definition: the min-max and max-min strategies

Given a zero-sum game defined by a payoff matrix $M \in \mathbb{R}^{m \times n}$
and a strategy $y \in \mathbb{R}^n$ for the **column player**, the **row player**
seeks a [best response strategy](#sec:best_responses)
$x \in \mathbb{R}^m$ that maximises their expected payoff:

$$
\max_{x \in \mathcal{A}_1} x M y^T
$$

This corresponds to choosing the rows of $M$ that yields the highest expected
value under the strategy $y$, i.e.,

$$
\max_{i \leq m} (M y^T)_i
$$

The column player, by selecting $y$, can influence the upper bound $v$ of this
maximum. Since the game is zero-sum, the column player will aim to choose $y$
to make this upper bound $v$ as small as possible.

Hence,

$$
\max_{x \in \mathcal{A}_1} x M y^T = \max_{i \leq m} (M y^T)_i =
\min \left\{ v \in \mathbb{R} \;\middle|\; M y^T \leq \mathbb{1} v \right\}
$$

The **min-max strategy** $y$ for the column player is the solution to the
following optimisation problem (referred to as a **linear program**):

$$
\begin{aligned}
\min_{y, v} \quad & v \\
\text{subject to} \quad & M y^T \leq \mathbb{1} v \\
& y \in \mathcal{A}_2
\end{aligned}
$$

In this formulation, $v$ is the **min-max value** of the game.

The corresponding **max-min strategy** $x$ for the row player solves the
following linear program:

$$
\begin{aligned}
\max_{x, u} \quad & u \\
\text{subject to} \quad & x M \geq \mathbb{1} u \\
& x \in \mathcal{A}_1
\end{aligned}
$$

In this case, $u$ is the **max-min value** of the game.

#### Example: Max-min strategy for modified Rock-Paper-Scissors

For the [modified Rock-Paper-Scissors game](#sec:motivating_example_zero_sum_games),
the **max-min strategy** $x$ for the row player satisfies the following linear
program:

$$
\begin{aligned}
\max_{x, u} \quad & u \\
\text{subject to} \quad
& 2x_2 - x_3 \geq u \\
& -x_1 + x_3 \geq u \\
& x_1 - 2x_2 \geq u \\
& x_1 + x_2 + x_3  = 1 \\
& x_i \geq 0 \quad \text{for all } i \in \{1, 2, 3\}
\end{aligned}
$$

(exam:max_min_strategy_for_matching_pennies)=

#### Example: Max-min strategy for Matching Pennies

For [](#matching_pennies) with payoff matrix:

$$
M = \begin{pmatrix}
        1 & -1 \\
        -1& 1
    \end{pmatrix}
$$

the **max-min strategy** $x$ for the row player satisfies the following linear
program:

$$
\begin{aligned}
\max_{x, u} \quad & u \\
\text{subject to} \quad
& x_1 - x_2 \geq u \\
& -x_1 + x_2 \geq u \\
& x_1 + x_2 = 1 \\
& x_i \geq 0 \quad \text{for all } i \in \{1, 2\}
\end{aligned}
$$

Given that $x_1 + x_2 = 1$, this linear program corresponds to:

$$
\begin{aligned}
\max_{x_1, u} \quad & u \\
\text{subject to} \quad
& 2x_1 - 1 \geq u \\
& -2x_1 + 1 \geq u \\
& 0 \leq x_1 \leq 1
\end{aligned}
$$

These constraints can be rewritten as:

$$
\begin{aligned}
x_1 &\geq \frac{1 + u}{2} \\
x_1 &\leq \frac{1 - u}{2} \\
0 &\leq x_1 \leq 1
\end{aligned}
$$

This implies:

$$
\frac{1 + u}{2} \leq x_1 \leq \frac{1 - u}{2}
$$

which leads to:

$$
\frac{1 + u}{2} \leq \frac{1 - u}{2} \quad \Rightarrow \quad u \leq -u
$$

This inequality holds only when $u = 0$. When $u = 0$, the constraints reduce to:

$$
\frac{1}{2} \leq x_1 \leq \frac{1}{2}
$$

yielding the unique solution $x_1 = \frac{1}{2}$.

Thus, the **max-min strategy** is:

$$
x = \left( \frac{1}{2}, \frac{1}{2} \right)
$$

### Theorem: The minimax theorem

The minimax theorem [@vonNeumann1928] states that if there exists
optimal values of the:

1.  _max-min_ value $u$ and the _max-min_ strategy $x$.
2.  _min-max_ value $v$ and the _min-max_ strategy $y$.

then $u=v$.

The proof which uses the
**linear program duality theorem** is omitted from
this book but can be found in [@Vanderbei1998].

Note that this answers the question posed at the end of
[](#sec:motivating_example_zero_sum_games)
through a choice of strategy the row player can ensure they obtain the
value of the game which is equal to the max-min value and the
min-max value.

In the next section we will start to introduce practical tools with which to do
that.

(sec:zero_sum_game_standard_form_linear_program)=

### Definition: Standard Form Linear program

A standard form of the linear program can be written which more readily
will allow us to use [Integer Pivoting](#app:integer_pivoting).

---

In a [zero-sum game](#sec:definition_zero_sum_game), given a row player payoff
matrix $M$ with $m$ rows and $n$ columns, the following linear program yields
the **max-min strategy** and the **value** of the game:

$$
\min_{x \in \mathbb{R}^{(m + 1) \times 1}} \; c x
$$

subject to:

$$
\begin{aligned}
M_{\text{ub}} x &\leq b_{\text{ub}} \\
M_{\text{eq}} x &= b_{\text{eq}} \\
x_i &\geq 0 \quad \text{for } i \leq m
\end{aligned}
$$

The coefficients in this linear program are defined as:

$$
\label{eqn:standard_form_linear_program}
\begin{aligned}
c &= (\underbrace{0, \dots, 0}_{m}, -1)
&& \text{where } c \in \{0, 1\}^{1 \times (m + 1)} \\[0.5em]
M_{\text{ub}} &=
\begin{pmatrix}
(-M^T)_{11} & \dots & (-M^T)_{1m} & 1 \\
\vdots & \ddots & \vdots & 1 \\
(-M^T)_{n1} & \dots & (-M^T)_{nm} & 1
\end{pmatrix}
&& M_{\text{ub}} \in \mathbb{R}^{n \times (m + 1)} \\[0.5em]
b_{\text{ub}} &= (0, \dots, 0)^T
&& b_{\text{ub}} \in \mathbb{R}^{n \times 1} \\[0.5em]
M_{\text{eq}} &= (\underbrace{1, \dots, 1}_{m}, 0)
&& M_{\text{eq}} \in \{0, 1\}^{1 \times (m + 1)} \\[0.5em]
b_{\text{eq}} &= 1
\end{aligned}
$$

#### Example: Standard form for the Modified Rock Paper Scissors Game

For the [modified Rock-Paper-Scissors game](#sec:motivating_example_zero_sum_games),
the corresponding coefficients are:

$$
\begin{aligned}
c &= (0, 0, 0, -1) \\[0.5em]
M_{\text{ub}} &=
\begin{pmatrix}
0  & -2 & 1  & 1 \\
1  &  0 & -1 & 1 \\
-1 & 2  & 0  & 1
\end{pmatrix} \\[0.5em]
b_{\text{ub}} &=
\begin{pmatrix}
0 \\
0 \\
0
\end{pmatrix} \\[0.5em]
M_{\text{eq}} &= (1, 1, 1, 0) \\[0.5em]
b_{\text{eq}} &= 1
\end{aligned}
$$

### Definition: Tableau for Zero-Sum Game

---

Given a zero-sum game with payoff matrix $M\in \mathbb{R}{m\times n}$
the [standard form linear program](#sec:zero_sum_game_standard_form_linear_program):
can be represented by the following **initial tableau**:

$$
T =
\left(
\begin{array}{ccccccc|c}
        x_1 & \dots  & x_m          & v  & s_1 & \dots & s_n & b\\
(-M^T)^{11} & \dots  & (-M^T)_{1m}  & 1  & 1 & \dots   & 1   & 0\\
     \vdots & \ddots & \vdots       & 1  & 0 & \ddots  & 0   & 0\\
(-M^T)_{n1} & \dots  & (-M^T)\_{nm} & 1  & 0 & \dots   & 1   & 0\\
          1 & \dots  & 1            & 0  & 0 & \dots   & 1   & 1\\
          0 & \dots  & 0            & -1 & 0 & \dots   & 0   & 0
\end{array}
\right)
$$

Here, slack variables have been introduced to convert inequalities into
equalities. The tableau is arranged with columns for the decision variables
$x_1, \dots, x_m$, the game value variable $v$, slack variables $s_1, \dots,
s_n$, and the right-hand side.

```{important}
The final row of the tableau has been somewhat artifically added: it does not
correspond to any specific part of [](#eqn:standard_form_linear_program).
However this is an important addition to the tableau as it will indicate two
things:

- Which column to choose to pivot in other words which variable to make
non-basic.
- When to stop integer pivoting.

Given a Tableau, we choose to pivot the column with the lowest negative value in
the final row: this corresponds to the variable that will reduce the objective
function the most. When all values in the final row are non-negative we stop
integer pivoting.
```

We proceed by performing **integer pivoting** to move from one basic feasible
solution to another, reducing the objective function at each step until
optimality is reached.

(exam:integer_pivoting_for_modified_rock_paper_scissors)=

#### Example: Integer Pivoting for Modified Rock-Paper-Scissors

We now solve the [modified Rock-Paper-Scissors game](#sec:motivating_example_zero_sum_games)
using the tableau method. Recall that the standard form coefficients are:

$$
\begin{aligned}
c &= (0, 0, 0, -1) \\
M_{\text{ub}} &=
\begin{pmatrix}
0 & -2 & 1 & 1 \\
1 & 0 & -1 & 1  \\
-1 & 2 & 0 & 1
\end{pmatrix} \\
b_{\text{ub}} &=
\begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} \\
M_{\text{eq}} &= (1, 1, 1, 1, 0) \\
b_{\text{eq}} &= 1
\end{aligned}
$$

To construct the tableau, we introduce slack variables $s_1, s_2, s_3$ for the
inequality constraints, and denote the game value variable by $v = x_5$.

#### Initial Tableau

The initial tableau is:

$$
\begin{array}{ccccccc|c}
 x_1 & x_2 & x_3 & v & s_1 & s_2 & s_3 & b \\
        0& -2& 1& 1&  1& 0& 0& 0&\\
        1& 0& -1&1& 0& 1& 0& 0&\\
        -1& 2& 0& 1&  0& 0& 1& 0&\\
        1& 1& 1& 0& 0& 0& 0& 1&\\
        0& 0& 0& -1& 0& 0& 0& 0&\\
\end{array}
$$

The last row is the objective function: minimising $v$. We begin by identifying
the entering variable with the most negative coefficient in the objective row,
which is $v$.

#### Pivot 1: Entering variable $v$

To pivot on $v$, we look at the positive entries in the $v$ column (rows 1–3).
All are $1$, so we apply the **ratio test**:

- Row 1: $0 / 1 = 0$
- Row 2: $0 / 1 = 0$
- Row 3: $0 / 1 = 0$

Ties are broken arbitrarily. Suppose we choose row 1:
we subtract appropriate multiples of this row from all others to eliminate
$v$ from those rows:

- Row 2 $\gets$ Row 2 - Row 1
- Row 3 $\gets$ Row 3 - Row 1
- Objective row = Objective + Row 1

After row operations:

$$
\begin{array}{ccccccc|c}
 x_1 & x_2 & x_3 & v & s_1 & s_2 & s_3 & b \\
         0& -2&  1&  1&  1&  0&  0&  0\\
         1&  2& -2&  0& -1&  1&  0&  0\\
        -1&  4& -1&  0& -1&  0&  1&  0\\
         1&  1&  1&  0&  0&  0&  0&  1\\
         0& -2&  1&  0&  1&  0&  0&  0
\end{array}
$$

#### Pivot 2: Entering variable $x_2$

Next, inspect the objective row. The most negative coefficient is $-2$ for $x_2$.

Apply ratio test on rows with positive $x_2$ entries:

- Row 2: $0 / 2 = 0$
- Row 3: $0 / 4 = 0$
- Row 4: $1 / 1 = 1$

Choose Row 2 (arbitrary tie-break).

Pivot on entry in row 2, column $x_2$ and eliminate
$x_2$ from other rows. After computations, we get:

$$
\begin{array}{ccccccc|c}
 x_1 & x_2 & x_3  & v & s_1 & s_2 & s_3 & b \\
         2&  0& -2&  2&  0&  2&  0&  0\\
         1&  2& -2&  0& -1&  1&  0&  0\\
        -6&  0&  6&  0&  2& -4&  2&  0\\
         1&  0&  4&  0&  1& -1&  0&  2\\
         2&  0& -2&  0&  0&  2&  0&  0
\end{array}
$$

#### Pivot 3: Entering variable $x_3$

Continue inspecting the objective row. The most negative is now $-2$ for $x_3$,
so it enters. Apply ratio test among positive entries in column $x_3$.

- Row 3: $0 / 6 = 0$

There is a single candidate: pivot on row 3. Eliminate $x_3$ from other rows.
After computations we get:

$$
\begin{array}{ccccccc|c}
 x_1 & x_2 & x_3  & v & s_1 & s_2 & s_3 & b \\
          0&  0&  0& 12&  4&  4&  4&  0\\
         -6& 12&  0&  0& -2& -2&  4&  0\\
         -6&  0&  6&  0&  2& -4&  2&  0\\
         30&  0&  0&  0& -2& 10& -8& 12\\
          0&  0&  0&  0&  4&  4&  4&  0
\end{array}
$$

We now set the basic variables to 0 and read the equations for the non-basic
variables:

$$
\begin{align*}
s_1 &=0\\
s_2 &=0 \\
s_3 &=0 \\
12 v &= 0\\
-6x_1 + 12x_2&=0\\
-6x_1 + 6 x_3&=0\\
30x_1 &= 12
\end{align*}
$$

This gives:

$$
x = (12/30, 6/30, 12/30)\qquad v=0
$$

Thus, the **max-min strategy** is:

$$
x = \left( \frac{2}{5}, \frac{1}{5}, \frac{2}{5} \right)
$$

## Exercises

```{exercise}
:label: coefficients_for_standard_form_lp

Obtain the coefficients of the [standard form](#sec:zero_sum_game_standard_form_linear_program)
linear system for the zero-sum games with the following payoff matrices:

1. $M = \begin{pmatrix} 3 & -1\ -1 & 2 \end{pmatrix}$
2. $M = \begin{pmatrix} -1 & -1\ -1 & 3 \end{pmatrix}$
3. $M = \begin{pmatrix} 2 & 1 & -3\ -3 & -1 & 3 \end{pmatrix}$
4. $M = \begin{pmatrix} 3 & -2 & 0\ -3 & 0 & 3 \ 0 & 2 & -5 \end{pmatrix}$
```

```{exercise}
:label: max-min_strategy_for_matching_pennies

For [Example: Max-min strategy for Matching Pennies](#exam:max_min_strategy_for_matching_pennies):

1. Use integer pivoting to confirm that the max-min strategy is $x = (1/2, 1/2)$.
2. By letting $M = -M^T$, or otherwise, obtain the min-max strategy for the
   column player.
3. Use the [Best Response Condition](#thrm:best_response_condition) to confirm
   your calculations.
```

```{exercise}
:label: max-min_strategy_for_rock_paper_scissors

Obtain the max-min strategy for the standard game of Rock Paper Scissors
defined by:

$$
M = \begin{pmatrix}
  0  & -1 & 1 \\
  1  & 0  & -1\\
  -1 & 1  & 0
\end{pmatrix}
$$
```

```{exercise}
:label: modified_rock_paper_scissors

For [Example: Integer pivoting for modified Rock Paper Scissors](#exam:integer_pivoting_for_modified_rock_paper_scissors):

1. By letting $M = -M^T$, or otherwise, obtain the min-max strategy for the
   column player.
2. Use the [Best Response Condition](#thrm:best_response_condition) to confirm
   your calculations.
```

## Programming

### Solve linear programs using Scipy

The `scipy` library provides functionality to solve a linear program in
[standard form](#sec:zero_sum_game_standard_form_linear_program).

We begin by creating the various matrices and vectors: $M_{ub}$, $M_{eq}$,
$b_{ub}$, $b_{eq}$, and $c$:

```{code-cell} python3
import numpy as np

M = np.array(
    [
        [0, -1, 1],
        [2, 0, -2],
        [-1, 1, 0],
    ]
)
M_ub = np.hstack((-M.T, [[1], [1], [1]]))
M_eq = np.array(([[1, 1, 1, 0]]))
b_ub = np.array(
    [
        [0],
        [0],
        [0],
    ]
)
b_eq = 1
c = np.array([0, 0, 0, -1])
```

Now we can pass these to `scipy.optimize.linprog`:

```{code-cell} python3
import scipy.optimize

res = scipy.optimize.linprog(
    c=c,
    A_ub=M_ub,
    b_ub=b_ub,
    A_eq=M_eq,
    b_eq=b_eq,
)
res
```

This returns the full output of the optimisation. The min-max strategy is
contained in all but the last entry of `res.x`:

```{code-cell} python3
res.x[:-1]
```

The last entry of `res.x` gives the value of the game:

```{code-cell} python3
res.x[-1]
```

### Obtain min-max and max-min strategies using Nashpy

`nashpy` can be used to directly obtain the min-max and max-min strategies:

```{code-cell} python3
import nashpy as nash

game = nash.Game(M, -M)
game.linear_program()
```

### Obtain min-max and max-min strategies using Gambit

`Gambit` can be used to directly obtain the min-max and max-min strategies. We
start by creating a pygambit game from arrays:

```{code-cell} python3
import pygambit as gbt

game = gbt.Game.from_arrays(M, -M)
print(game)
```

Now we can solve the underlying linear program:

```{code-cell} python3
gbt.nash.lp_solve(game)
```

## Notable Research

The foundations of zero-sum game theory and its connection to linear
programming emerged from a convergence of ideas in mathematics, economics, and
operations research during the mid-20th century.

The **minimax theorem** was first proven by John von Neumann in 1928
[@vonneumann1928theorie]. This landmark result, stating that every finite,
two-player zero-sum game has a value and optimal strategies, was later
generalised in 1944 [@vonneumann1944theory].

The **minimax theorem** does not necessarily only apply to zero-sum games but in
fact applies to any constant sum game where $M_r + M_c = K$ for some constant
$K$. An example of this is shown in [@chiappori2002testing] where penalty kicks
are modelled and the payoff matrices correspond to the probability of
scoring (or for the column player saving) a penalty.

Until the work of [@nash1950equilibrium] the minimax theorem was the main solution concept in game theory.
For his foundational work on equilibrium in non-cooperative games,
John Nash was awarded the Nobel Prize in Economic Sciences in 1994,
shared with John Harsanyi and Reinhard Selten.
His contributions form the cornerstone of non-cooperative game theory.

## Conclusion

This chapter introduced zero-sum games, where one player’s gain is precisely
balanced by the other’s loss. We explored the foundational minimax theorem, the
max-min and min-max strategies, and showed how linear programming provides a
practical and elegant way to compute optimal strategies.

The central insight of this chapter is the equivalence between solving a
zero-sum game and solving a pair of dual linear programs. This connection
allows us to apply tools from optimisation—such as tableau methods and integer
pivoting—to find equilibrium strategies.

[](#tbl:zero_sum_summary) summarises the two central linear programs seen in this chapter.

```{table} The main linear programs for Zero Sum Game
:label: tbl:zero_sum_summary
:align: center
:class: table-bordered


| Problem    | Player        | Objective    | Constraints                                      |
| ---------- | ------------- | ------------ | ------------------------------------------------ |
| Max-min LP | Row player    | Maximise $u$ | $x M \geq \mathbb{1} u$, $x \in \mathcal{A}_1$   |
| Min-max LP | Column player | Minimise $v$ | $M y^T \leq \mathbb{1} v$, $y \in \mathcal{A}_2$ |

```

---

```{attention}
The **value of a zero-sum game** is the unique number that both players can
guarantee for themselves through optimal play, and it can be computed by
solving either the max-min or min-max linear program.
```

---

(solutions:zero_sum_games)=

## Solutions

````{solution} coefficients_for_standard_form_lp
:label: solution:coefficients_for_standard_form_lp

We obtain the [standard form linear program](#sec:zero_sum_game_standard_form_linear_program) coefficients for each game. Recall the standard form uses:

$$
c = (0, \dots, 0, -1), \quad
M_{\text{ub}} = \begin{pmatrix} -M^T & \mathbb{1} \end{pmatrix}, \quad
b_{\text{ub}} = \mathbb{0}, \quad
M_{\text{eq}} = (1, \dots, 1, 0), \quad
b_{\text{eq}} = 1
$$

**1.** $M = \begin{pmatrix} 3 & -1 \\ -1 & 2 \end{pmatrix}$

This is a $2 \times 2$ game so the decision vector is $(x_1, x_2, v)$.

$$
-M^T = -\begin{pmatrix} 3 & -1 \\ -1 & 2 \end{pmatrix}^T = -\begin{pmatrix} 3 & -1 \\ -1 & 2 \end{pmatrix} = \begin{pmatrix} -3 & 1 \\ 1 & -2 \end{pmatrix}
$$

$$
c = (0, 0, -1)
$$

$$
M_{\text{ub}} = \begin{pmatrix} -3 & 1 & 1 \\ 1 & -2 & 1 \end{pmatrix}
\qquad
b_{\text{ub}} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}
$$

$$
M_{\text{eq}} = (1, 1, 0)
\qquad
b_{\text{eq}} = 1
$$

---

**2.** $M = \begin{pmatrix} -1 & -1 \\ -1 & 3 \end{pmatrix}$

$$
-M^T = \begin{pmatrix} 1 & 1 \\ 1 & -3 \end{pmatrix}
$$

$$
c = (0, 0, -1)
$$

$$
M_{\text{ub}} = \begin{pmatrix} 1 & 1 & 1 \\ 1 & -3 & 1 \end{pmatrix}
\qquad
b_{\text{ub}} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}
$$

$$
M_{\text{eq}} = (1, 1, 0)
\qquad
b_{\text{eq}} = 1
$$

---

**3.** $M = \begin{pmatrix} 2 & 1 & -3 \\ -3 & -1 & 3 \end{pmatrix}$

This is a $2 \times 3$ game. The row player has 2 actions, so the decision vector is $(x_1, x_2, v)$.

$$
-M^T = -\begin{pmatrix} 2 & -3 \\ 1 & -1 \\ -3 & 3 \end{pmatrix} = \begin{pmatrix} -2 & 3 \\ -1 & 1 \\ 3 & -3 \end{pmatrix}
$$

$$
c = (0, 0, -1)
$$

$$
M_{\text{ub}} = \begin{pmatrix} -2 & 3 & 1 \\ -1 & 1 & 1 \\ 3 & -3 & 1 \end{pmatrix}
\qquad
b_{\text{ub}} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}
$$

$$
M_{\text{eq}} = (1, 1, 0)
\qquad
b_{\text{eq}} = 1
$$

---

**4.** $M = \begin{pmatrix} 3 & -2 & 0 \\ -3 & 0 & 3 \\ 0 & 2 & -5 \end{pmatrix}$

This is a $3 \times 3$ game. The decision vector is $(x_1, x_2, x_3, v)$.

$$
-M^T = -\begin{pmatrix} 3 & -3 & 0 \\ -2 & 0 & 2 \\ 0 & 3 & -5 \end{pmatrix} = \begin{pmatrix} -3 & 3 & 0 \\ 2 & 0 & -2 \\ 0 & -3 & 5 \end{pmatrix}
$$

$$
c = (0, 0, 0, -1)
$$

$$
M_{\text{ub}} = \begin{pmatrix} -3 & 3 & 0 & 1 \\ 2 & 0 & -2 & 1 \\ 0 & -3 & 5 & 1 \end{pmatrix}
\qquad
b_{\text{ub}} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}
$$

$$
M_{\text{eq}} = (1, 1, 1, 0)
\qquad
b_{\text{eq}} = 1
$$

```{code-cell} python3
import numpy as np

# Verify game 1
M1 = np.array([[3, -1], [-1, 2]])
M_ub1 = np.hstack((-M1.T, np.ones((2, 1))))
print("Game 1 M_ub:\n", M_ub1)
print("Game 1 c:", np.array([0, 0, -1]))

# Verify game 4
M4 = np.array([[3, -2, 0], [-3, 0, 3], [0, 2, -5]])
M_ub4 = np.hstack((-M4.T, np.ones((3, 1))))
print("\nGame 4 M_ub:\n", M_ub4)
print("Game 4 c:", np.array([0, 0, 0, -1]))
```

````

---

````{solution} max-min_strategy_for_matching_pennies
:label: solution:max-min_strategy_for_matching_pennies

Recall the Matching Pennies payoff matrix:

$$
M = \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix}
$$

**1. Integer pivoting to confirm max-min strategy $x = (1/2, 1/2)$:**

The standard form coefficients are:

$$
c = (0, 0, -1), \quad
M_{\text{ub}} = \begin{pmatrix} -1 & 1 & 1 \\ 1 & -1 & 1 \end{pmatrix}, \quad
b_{\text{ub}} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}, \quad
M_{\text{eq}} = (1, 1, 0), \quad
b_{\text{eq}} = 1
$$

The initial tableau (introducing slack variables $s_1, s_2$) is:

$$
\begin{array}{ccccc|c}
x_1 & x_2 & v & s_1 & s_2 & b \\
-1 & 1 & 1 & 1 & 0 & 0 \\
1 & -1 & 1 & 0 & 1 & 0 \\
1 & 1 & 0 & 0 & 0 & 1 \\
0 & 0 & -1 & 0 & 0 & 0
\end{array}
$$

**Pivot 1: Entering variable $v$ (most negative objective coefficient $= -1$).**

All entries in the $v$ column among constraint rows are $1$. Ratio test: all rows give $0/1 = 0$. Choose Row 1 as the pivot row.

- Row 2 $\gets$ Row 2 $-$ Row 1
- Row 3 stays (Row 3 has no $v$ entry)
- Objective row $\gets$ Objective $+$ Row 1

$$
\begin{array}{ccccc|c}
x_1 & x_2 & v & s_1 & s_2 & b \\
-1 & 1 & 1 & 1 & 0 & 0 \\
2 & -2 & 0 & -1 & 1 & 0 \\
1 & 1 & 0 & 0 & 0 & 1 \\
-1 & 1 & 0 & 1 & 0 & 0
\end{array}
$$

**Pivot 2: Entering variable $x_1$ (most negative objective coefficient $= -1$).**

Positive entries in $x_1$ column: Row 2 ($2$) and Row 3 ($1$). Ratio test: Row 2 gives $0/2 = 0$, Row 3 gives $1/1 = 1$. Choose Row 2.

- Row 1 $\gets$ Row 1 $\cdot 2 +$ Row 2: $(-2+2, 2-2, 2+0, 2-1, 0+1, 0) = (0, 0, 2, 1, 1, 0)$
- Row 3 $\gets$ Row 3 $\cdot 2 -$ Row 2: $(2-2, 2+2, 0, 0+1, 0-1, 2) = (0, 4, 0, 1, -1, 2)$
- Objective $\gets$ Objective $\cdot 2 +$ Row 2: $(-2+2, 2-2, 0, 2-1, 0+1, 0) = (0, 0, 0, 1, 1, 0)$

$$
\begin{array}{ccccc|c}
x_1 & x_2 & v & s_1 & s_2 & b \\
0 & 0 & 2 & 1 & 1 & 0 \\
2 & -2 & 0 & -1 & 1 & 0 \\
0 & 4 & 0 & 1 & -1 & 2 \\
0 & 0 & 0 & 1 & 1 & 0
\end{array}
$$

All objective row entries are non-negative: we stop. Setting non-basic variables ($s_1 = s_2 = 0$) and reading the system:

$$
2v = 0 \implies v = 0
$$
$$
2x_1 - 2x_2 = 0 \implies x_1 = x_2
$$
$$
4x_2 = 2 \implies x_2 = \frac{1}{2}
$$

Thus $x_1 = x_2 = 1/2$, confirming:

$$
x = \left(\frac{1}{2},\ \frac{1}{2}\right), \qquad v = 0
$$

**2. Min-max strategy for the column player:**

The column player's game is given by $-M^T$. Since $M$ is antisymmetric ($M = -M^T$ for this game), the min-max LP for the column player is identical in structure. Setting $M' = -M^T$:

$$
M' = -M^T = -\begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix}
$$

By the identical symmetry of the problem, the min-max strategy for the column player is:

$$
y = \left(\frac{1}{2},\ \frac{1}{2}\right)
$$

with min-max value $v = 0$. By the [minimax theorem](#chp:zero_sum_games), $u = v = 0$.

**3. Best Response Condition check:**

With $x = (1/2, 1/2)$ and $y = (1/2, 1/2)$:

$$
M y^T = \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix} \begin{pmatrix} 1/2 \\ 1/2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}
$$

Both entries equal $0 = \max_k (My^T)_k$, and the support of $x$ is $\{1, 2\}$, so the [best response condition](#thrm:best_response_condition) is satisfied: $x$ is a best response to $y$.

By symmetry:

$$
x M = \begin{pmatrix} 1/2 & 1/2 \end{pmatrix} \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} 0 & 0 \end{pmatrix}
$$

Both entries of $xM$ are equal, confirming $y$ is a best response to $x$.

```{code-cell} python3
import numpy as np
import scipy.optimize
import nashpy as nash

M = np.array([[1, -1], [-1, 1]])
M_ub = np.hstack((-M.T, np.ones((2, 1))))
b_ub = np.zeros((2, 1))
M_eq = np.array([[1, 1, 0]])
b_eq = 1
c = np.array([0, 0, -1])

res = scipy.optimize.linprog(c=c, A_ub=M_ub, b_ub=b_ub, A_eq=M_eq, b_eq=b_eq)
print("Max-min strategy:", res.x[:-1])
print("Value of game:", res.x[-1])

# Verify best response condition
x = np.array([0.5, 0.5])
y = np.array([0.5, 0.5])
print("M y^T =", M @ y)
print("x M =", x @ M)
```

````

---

````{solution} max-min_strategy_for_rock_paper_scissors
:label: solution:max-min_strategy_for_rock_paper_scissors

The standard Rock-Paper-Scissors payoff matrix is:

$$
M = \begin{pmatrix}
0 & -1 & 1 \\
1 & 0 & -1 \\
-1 & 1 & 0
\end{pmatrix}
$$

The standard form coefficients are:

$$
c = (0, 0, 0, -1)
$$

$$
M_{\text{ub}} = \begin{pmatrix}
0 & -1 & 1 & 1 \\
1 & 0 & -1 & 1 \\
-1 & 1 & 0 & 1
\end{pmatrix}
\qquad
b_{\text{ub}} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}
$$

$$
M_{\text{eq}} = (1, 1, 1, 0), \qquad b_{\text{eq}} = 1
$$

**Integer pivoting:**

Initial tableau:

$$
\begin{array}{ccccccc|c}
x_1 & x_2 & x_3 & v & s_1 & s_2 & s_3 & b \\
0 & -1 & 1 & 1 & 1 & 0 & 0 & 0 \\
1 & 0 & -1 & 1 & 0 & 1 & 0 & 0 \\
-1 & 1 & 0 & 1 & 0 & 0 & 1 & 0 \\
1 & 1 & 1 & 0 & 0 & 0 & 0 & 1 \\
0 & 0 & 0 & -1 & 0 & 0 & 0 & 0
\end{array}
$$

**Pivot 1:** $v$ enters (coefficient $-1$). Choose Row 1 (ratio $0/1 = 0$).

- Row 2 $\gets$ Row 2 $-$ Row 1: $(1, 1, -2, 0, -1, 1, 0, 0)$
- Row 3 $\gets$ Row 3 $-$ Row 1: $(-1, 2, -1, 0, -1, 0, 1, 0)$
- Objective $\gets$ Objective $+$ Row 1: $(0, -1, 1, 0, 1, 0, 0, 0)$

$$
\begin{array}{ccccccc|c}
0 & -1 & 1 & 1 & 1 & 0 & 0 & 0 \\
1 & 1 & -2 & 0 & -1 & 1 & 0 & 0 \\
-1 & 2 & -1 & 0 & -1 & 0 & 1 & 0 \\
1 & 1 & 1 & 0 & 0 & 0 & 0 & 1 \\
0 & -1 & 1 & 0 & 1 & 0 & 0 & 0
\end{array}
$$

**Pivot 2:** $x_2$ enters (coefficient $-1$). Positive entries in $x_2$ column: Row 2 ($1$, ratio $0$), Row 3 ($2$, ratio $0$), Row 4 ($1$, ratio $1$). Choose Row 2 (tie-break).

Pivot on $(2, x_2)$, entry = 1. Eliminate $x_2$ from other rows:
- Row 1 $\gets$ Row 1 $+$ Row 2: $(1, 0, -1, 1, 0, 1, 0, 0)$
- Row 3 $\gets$ Row 3 $-$ $2 \cdot$ Row 2: $(-3, 0, 3, 0, 1, -2, 1, 0)$
- Row 4 $\gets$ Row 4 $-$ Row 2: $(0, 0, 3, 0, 1, -1, 0, 1)$
- Objective $\gets$ Objective $+$ Row 2: $(1, 0, -1, 0, 0, 1, 0, 0)$

$$
\begin{array}{ccccccc|c}
1 & 0 & -1 & 1 & 0 & 1 & 0 & 0 \\
1 & 1 & -2 & 0 & -1 & 1 & 0 & 0 \\
-3 & 0 & 3 & 0 & 1 & -2 & 1 & 0 \\
0 & 0 & 3 & 0 & 1 & -1 & 0 & 1 \\
1 & 0 & -1 & 0 & 0 & 1 & 0 & 0
\end{array}
$$

**Pivot 3:** $x_3$ enters (coefficient $-1$). Positive entries in $x_3$ column: Row 3 ($3$, ratio $0$), Row 4 ($3$, ratio $1/3$). Choose Row 3.

Pivot on $(3, x_3)$, entry = 3. Eliminate $x_3$:
- Row 1 $\gets$ 3 $\cdot$ Row 1 $+$ Row 3: $(0, 0, 0, 3, 1, 1, 1, 0)$
- Row 2 $\gets$ 3 $\cdot$ Row 2 $+$ 2 $\cdot$ Row 3: $(-3, 3, 0, 0, -1, -1, 2, 0)$
- Row 4 $\gets$ 3 $\cdot$ Row 4 $-$ Row 3: $(3, 0, 6, 0, 2, -1, -1, 3)$...

Let me compute more carefully. Actually, since this game is perfectly symmetric (Rock-Paper-Scissors is a symmetric zero-sum game), we can exploit the symmetry: the max-min strategy must assign equal probability to all three actions.

**Claim:** $x = (1/3, 1/3, 1/3)$ with value $v = 0$.

**Verification:** For any column strategy $y$:

$$
xM = \frac{1}{3}(0+1-1,\ -1+0+1,\ 1-1+0) = \frac{1}{3}(0, 0, 0) = (0, 0, 0)
$$

So $(xM)_j = 0$ for all $j$, meaning the row player guarantees expected payoff $0$ regardless of $y$. The uniform strategy $(1/3, 1/3, 1/3)$ achieves the maximum of the minimum payoff.

By symmetry of the game under any permutation of the actions, any deviation from the uniform mixture would allow the column player to exploit the imbalance.

Thus:

$$
x = \left(\frac{1}{3},\ \frac{1}{3},\ \frac{1}{3}\right), \qquad v = 0
$$

```{code-cell} python3
import numpy as np
import scipy.optimize
import nashpy as nash

M = np.array([[0, -1, 1], [1, 0, -1], [-1, 1, 0]])

M_ub = np.hstack((-M.T, np.ones((3, 1))))
b_ub = np.zeros((3, 1))
M_eq = np.array([[1, 1, 1, 0]])
b_eq = 1
c = np.array([0, 0, 0, -1])

res = scipy.optimize.linprog(c=c, A_ub=M_ub, b_ub=b_ub, A_eq=M_eq, b_eq=b_eq)
print("Max-min strategy:", res.x[:-1])
print("Value of game:", res.x[-1])

# Verify
x = np.array([1/3, 1/3, 1/3])
print("x M =", x @ M, "(should be all zeros)")

# Using nashpy
game = nash.Game(M, -M)
print("Nashpy result:", game.linear_program())
```

````

---

````{solution} modified_rock_paper_scissors
:label: solution:modified_rock_paper_scissors

The modified Rock-Paper-Scissors payoff matrix is:

$$
M = \begin{pmatrix}
0 & -1 & 1 \\
2 & 0 & -2 \\
-1 & 1 & 0
\end{pmatrix}
$$

From [](#exam:integer_pivoting_for_modified_rock_paper_scissors) the max-min strategy is $x = (2/5, 1/5, 2/5)$ with value $v = 0$.

**1. Min-max strategy for the column player:**

The column player's game is given by replacing $M$ with $-M^T$:

$$
-M^T = -\begin{pmatrix} 0 & 2 & -1 \\ -1 & 0 & 1 \\ 1 & -2 & 0 \end{pmatrix} = \begin{pmatrix} 0 & -2 & 1 \\ 1 & 0 & -1 \\ -1 & 2 & 0 \end{pmatrix}
$$

The column player's max-min LP (equivalently the min-max LP for the original game) uses $-M^T$ as the row player matrix. We solve:

$$
\begin{aligned}
\max_{y, u} \quad & u \\
\text{subject to} \quad & y (-M^T) \geq \mathbb{1} u \\
& y \in \mathcal{A}_2
\end{aligned}
$$

The standard form for this LP:

$$
c = (0, 0, 0, -1), \quad
M_{\text{ub}}' = \begin{pmatrix} 0 & -1 & 1 & 1 \\ 2 & 0 & -2 & 1 \\ -1 & 1 & 0 & 1 \end{pmatrix}, \quad
M_{\text{eq}} = (1,1,1,0), \quad b_{\text{eq}} = 1
$$

By the [minimax theorem](#chp:zero_sum_games), $u = v = 0$ and we need to find $y = (y_1, y_2, y_3)$ such that:

$$
M y^T \leq \mathbb{1} \cdot 0 = \mathbb{0}
$$

That is:

$$
\begin{aligned}
-y_2 + y_3 &\leq 0 \\
2y_1 - 2y_3 &\leq 0 \\
-y_1 + y_2 &\leq 0
\end{aligned}
$$

Combined with the constraints that the row player is indifferent (since $v = 0$, the column player must make the row player indifferent across the support of the max-min strategy). The support of $x = (2/5, 1/5, 2/5)$ is $\{r_1, r_2, r_3\}$ (all three actions). So we need:

$$
(My^T)_1 = (My^T)_2 = (My^T)_3 = 0
$$

$$
\begin{aligned}
-y_2 + y_3 &= 0 \\
2y_1 - 2y_3 &= 0 \\
-y_1 + y_2 &= 0
\end{aligned}
$$

From the first equation: $y_3 = y_2$.
From the second: $y_1 = y_3 = y_2$.
So $y_1 = y_2 = y_3$. With $y_1 + y_2 + y_3 = 1$:

$$
y = \left(\frac{1}{3},\ \frac{1}{3},\ \frac{1}{3}\right)
$$

**2. Best Response Condition check:**

We verify that $x = (2/5, 1/5, 2/5)$ is a best response to $y = (1/3, 1/3, 1/3)$:

$$
\begin{align*}
My^T &= \begin{pmatrix}
0 & -1 & 1 \\
2 & 0 & -2 \\
-1 & 1 & 0
\end{pmatrix}
\begin{pmatrix} 1/3 \\ 1/3 \\ 1/3 \end{pmatrix} \\
&= \begin{pmatrix}
(0 - 1 + 1)/3 \\
(2 + 0 - 2)/3 \\
(-1 + 1 + 0)/3
\end{pmatrix} \\
&= \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}
\end{align*}
$$

All entries are equal to $0 = \max_k(My^T)_k$. Since the support of $x = \{1, 2, 3\}$ (all three actions have positive weight), the [best response condition](#thrm:best_response_condition) is satisfied. $x$ is a best response to $y$.

We verify $y = (1/3, 1/3, 1/3)$ is a best response to $x = (2/5, 1/5, 2/5)$:

$$
xM = \begin{pmatrix} 2/5 & 1/5 & 2/5 \end{pmatrix}
\begin{pmatrix}
0 & -1 & 1 \\
2 & 0 & -2 \\
-1 & 1 & 0
\end{pmatrix}
$$

$$
\begin{align*}
&= \left(\frac{0 \cdot 2 + 2 \cdot 1 - 1 \cdot 2}{5},\ \frac{-2 + 0 + 2}{5},\ \frac{2 - 2 + 0}{5}\right)\\
&= \left(\frac{0}{5},\ \frac{0}{5},\ \frac{0}{5}\right) = (0, 0, 0)
\end{align*}
$$

All entries of $xM$ are equal and equal to $0$. The support of $y = \{1, 2, 3\}$, so the best response condition is satisfied for $y$ as well.

```{code-cell} python3
import numpy as np
import scipy.optimize
import nashpy as nash

M = np.array([[0, -1, 1], [2, 0, -2], [-1, 1, 0]])

# Max-min for row player
M_ub_row = np.hstack((-M.T, np.ones((3, 1))))
b_ub = np.zeros((3, 1))
M_eq = np.array([[1, 1, 1, 0]])
b_eq = 1
c = np.array([0, 0, 0, -1])
res_row = scipy.optimize.linprog(c=c, A_ub=M_ub_row, b_ub=b_ub, A_eq=M_eq, b_eq=b_eq)
print("Max-min (row) strategy:", res_row.x[:-1])
print("Max-min value:", res_row.x[-1])

# Min-max for column player using -M^T
M_neg_T = -M.T
M_ub_col = np.hstack((-M_neg_T.T, np.ones((3, 1))))
res_col = scipy.optimize.linprog(c=c, A_ub=M_ub_col, b_ub=b_ub, A_eq=M_eq, b_eq=b_eq)
print("Min-max (column) strategy:", res_col.x[:-1])
print("Min-max value:", res_col.x[-1])

# Best response condition check
x = np.array([2/5, 1/5, 2/5])
y = np.array([1/3, 1/3, 1/3])
print("\nM y^T =", M @ y, "(should be [0, 0, 0])")
print("x M =", x @ M, "(should be [0, 0, 0])")

# Using nashpy
game = nash.Game(M, -M)
print("\nNashpy linear_program:", game.linear_program())
```

````
