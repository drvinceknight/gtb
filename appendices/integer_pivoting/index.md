---
kernelspec:
  name: python3
  display_name: "Python 3"
numbering:
  enumerator: A5.%s
---

(app:integer_pivoting)=

# Appendix: Integer Pivoting

(sec:motivating_example_two_views_of_a_polytope)=

## Motivating Example: Two Views of a Polytope

Consider the following set of points:

$$
\label{eqn:polytope_as_convex_hull}
\mathcal{P} = \left\{ \sum_{i=1}^{4} \lambda_i v_i\;\middle|\;
\begin{array}{l}
  \sum_{i=1}^4 \lambda_i = 1 \\
  \lambda_i \geq 0 \quad \text{for all } i \\
  v_i \in \{(0, 0), (1/3, 0), (1/4, 1/4), (0, 1/3)\}
\end{array}
\right\}
$$

This set $\mathcal{P}$ is a **polytope**, defined as the **convex hull** of a
finite
set of vertices:

$$
V = \{(0, 0),\ (1/3, 0),\ (1/4, 1/4),\ (0, 1/3)\}.
$$

A visualization is provided in [](#fig:polytope_as_convex_hull).

```{figure} ./images/polytope_as_convex_hull/main.png
:alt: A 2D polytope shown as a convex hull
:label: fig:polytope_as_convex_hull
:height: 250px

The two-dimensional polytope defined by [](#eqn:polytope_as_convex_hull),
shown as the convex hull of four points.
```

Polytopes can also be equivalently defined as the **intersection of half-
spaces**, that is, bounded regions formed by linear inequalities. This alternate view is
illustrated in [](#fig:polytope_as_intersection_of_halfspaces).

```{figure} ./images/polytope_as_intersection_of_halfspaces/main.png
:alt: A 2D polytope as an intersection of half-spaces
:label: fig:polytope_as_intersection_of_halfspaces
:height: 250px

The same polytope shown in [](#fig:polytope_as_convex_hull), represented as
the intersection of linear inequalities.
```

This second definition corresponds to:

$$
\label{eqn:polytope_as_intersection_of_halfspaces}
\mathcal{P} = \left\{ x \in \mathbb{R}^2\;\middle|\;
\begin{array}{l}
  x_1 \geq 0 \\
  x_2 \geq 0 \\
  x_1 + 3x_2 \leq 1 \\
  3x_1 + x_2 \leq 1 \\
\end{array}
\right\}
$$

The inequalities in [](#eqn:polytope_as_intersection_of_halfspaces) define
supporting half-spaces that together enclose the polytope.

Polytopes appear throughout mathematics, particularly in **optimisation**, where
they form the feasible regions of linear programs. These connections are central
to game theory, especially in the study of [zero-sum games](#chp:zero_sum_games)
and [general games](#chp:best_response_polytopes).

While this example lives in $\mathbb{R}^2$, the techniques extend to
**higher-dimensional polytopes**. The goal of this chapter is to develop tools
for moving from **vertex to vertex** in such polytopes, an essential idea in
both mathematical optimisation and algorithmic game theory.

## Theory

### Definition: Polytope as a Convex Hull

Let $V \subseteq \mathbb{R}^K$ be a finite set of points. A **polytope**
$\mathcal{P}$ is the set of all **convex combinations** of points in $V$:

$$
\mathcal{P} =
\left\{
\sum_{i=1}^{|V|} \lambda_i v_i \in \mathbb{R}^K \;\middle|\;
\sum_{i=1}^{|V|} \lambda_i = 1,\;
\lambda_i \geq 0,\;
v_i \in V
\right\}
$$

### Definition: Polytope as an Intersection of Half-Spaces

Let $M \in \mathbb{R}^{m \times n}$ and $b \in \mathbb{R}^m$. A **polytope**
$\mathcal{P}$ can also be defined as the set of points satisfying a system of
linear inequalities:

$$
\mathcal{P} = \left\{ x \in \mathbb{R}^n \;\middle|\; Mx \leq b \right\}
$$

```{important}
All polytopes can be represented either as a convex hull or as an
intersection of half-spaces.
```

The representation of a polytope as the intersection of half-spaces via
$Mx \leq b$ will allow us to work efficiently with large systems.

(sec:slack_variables)=

### Definition: Slack Variable

Given a system of linear inequalities of the form $Mx \leq b$, a **slack
variable** transforms each inequality into an equality by accounting for the
difference between the left- and right-hand sides.

Formally, for each row $i$, the inequality

$$
(Mx)_i \leq b_i
$$

can be rewritten as

$$
(Mx)_i + s_i = b_i \quad \text{with} \quad s_i \geq 0,
$$

where $s_i\geq 0$ is the **slack variable** corresponding to the $i$-th
inequality.

(sec:definition_tableau_representation_of_vertices)=

### Definition: Tableau Representation of Vertices

For $M \in \mathbb{R}^{m \times n}$ and $b \in \mathbb{R}^m$,
given a system of linear inequalities:

$$
Mx \leq b
$$

This system of linear inequalities can be written as a system of equalities by
adding [slack variables](#sec:slack_variables) to give a modified linear system
of equalities:

$$
\bar M \bar x = b
$$

Where $\bar M \in\mathbb{R}^{m \times m + n} $ and $\bar x \in \mathbb{R} ^{m +
1}$ includes coefficients for the added slack variables:

$$
\bar M = \begin{pmatrix} M & I_{m} \end{pmatrix}
\qquad
\bar x = \begin{pmatrix}x_1\\ \vdots \\ x_n \\ s_1 \\ \vdots \\ s_m\end{pmatrix}
$$

---

Given the system $\bar M \bar x = b$ a tableau is an extended matrix of the
form:

$$\begin{pmatrix}\bar M & I_m & b\end{pmatrix}$$

---

This augmented matrix of the underlying linear system is used to represent
points in Polytopes. Through elementary row operations which will be called
pivots we can move from one vertex to another.

(exmpl:tableaux_for_the_example)=

### Example: Tableaux for the [Motivating Example](#sec:motivating_example_two_views_of_a_polytope)

The linear system for the [Motivating
Example](#sec:motivating_example_two_views_of_a_polytope) is:

$$
\begin{align*}
  x_1 + 3x_2&\leq 1 \\
  3x_1 + x_2 &\leq 1
\end{align*}
$$

```{note}
We omit the non negativity inequality.
```

This corresponds to:

$$
M = \begin{pmatrix}
        1 & 3\\
        3 & 1\\
\end{pmatrix}
\qquad
b = \begin{pmatrix}
        1\\
        1\\
\end{pmatrix}
$$

We can write a Tableau that represents the equivalent system of equations $\bar
M \bar x = b$:

$$
\label{eqn:tableau_one}
T^{(1)} = \begin{pmatrix}
           1 & 3 & 1 & 0 & 1\\
           3 & 1 & 0 & 1 & 1
    \end{pmatrix}
$$

Tableaux are augmented matrices for linear systems, it is possible to do
elementary row operations on them that do not modify the underlying system.
We can also derive alternative tableaux from this example:

Multiplying $T^{(1)}$'s row 1 by 3 and subtracting row 2 gives:

$$
\label{eqn:tableau_two}
T^{(2)} = \begin{pmatrix}
           0 & 8 & 3 & -1 & 2\\
           3 & 1 & 0 & 1 & 1
    \end{pmatrix}
$$

Multiplying $T^{(2)}$'s row 2 by 8 and subtracting row 1 gives:

$$
\label{eqn:tableau_three}
T^{(3)} = \begin{pmatrix}
           0 & 8 & 3 & -1 & 2\\
           24 & 0 & -3 & 9 & 6
    \end{pmatrix}
$$

Multiplying $T^{(3)}$'s row 1 by 9 and adding row 2 gives:

$$
\label{eqn:tableau_four}
T^{(4)} = \begin{pmatrix}
           24 & 72 & 24 & 0 & 24\\
           24 & 0 & -3 & 9 & 6
    \end{pmatrix}
$$

There are other tableaux that correspond to the same systems of equations but
we next explore how tableaux correspond to vertices of polytopes. To do
this we need a new definition:

### Definition: Basic variables

---

A basic variable of a tableau corresponds to a column that
is linearly independent from the others.

---

### Example: Basic variables for the different Tableaux of the [Motivating Example](#sec:motivating_example_two_views_of_a_polytope)

The basic variables for:

- The tableau [](#eqn:tableau_one) are the two slack variables $s_1$ and $s_2$.
- The tableau [](#eqn:tableau_two) are $x_1$ and $s_1$.
- The tableau [](#eqn:tableau_three) are $x_1$ and $x_2$.
- The tableau [](#eqn:tableau_four) are $x_2$ and $s_2$.

Thus, the non-basic variables for:

- The tableau [](#eqn:tableau_one) are $x_1$ and $x_2$.
- The tableau [](#eqn:tableau_two) are $x_2$ and $s_2$.
- The tableau [](#eqn:tableau_three) are $s_1$ and $s_2$.
- The tableau [](#eqn:tableau_four) are $x_1$ and $s_1$.

(sec:equivalence_between_a_tableau_and_a_vertex)=

### Equivalence between a tableau and a vertex

A tableau represents the constraints and feasible region of a polytope. A given
tableau represents a vertex of the polytope.

To obtain a vertex from the tableau:

- Set the non basic variables to be 0;
- Solve the remaining system of equations.

### Example: equivalence between tableaux and vertices

1. For [](#eqn:tableau_one): we set the non-basic variables to 0:

   $$x_1=0\qquad x_2=0$$

   The remaining linear system from the tableau is:

   $$
        \begin{align*}
            s_1=1\\
            s_2=1
        \end{align*}
   $$

   Note that we do not need to solve this remaining linear system as setting the
   non-basic variables to 0 immediately gives us the vertex: $(x_1, x_2)=(0, 0)$
   (the
   origin of [](#fig:polytope_as_convex_hull)).

2. For [](#eqn:tableau_two): we set the non-basic variables to 0:

   $$x_2=0\qquad s_2=0$$

   The remaining linear system from the tableau is:

   $$
        \begin{align*}
            3x_1=1\\
            3s_1=2
        \end{align*}
   $$

   Solving this gives: $(x_1, x_2)=(1/3, 0)$ (the
   bottom right vertex of [](#fig:polytope_as_convex_hull)).

3. For [](#eqn:tableau_three): we set the non-basic variables to 0:

   $$s_1=0\qquad s_2=0$$

   The remaining linear system from the tableau is:

   $$
        \begin{align*}
            24x_1=6\\
            8x_2=2
        \end{align*}
   $$

   Solving this gives: $(x_1, x_2)=(1/4, 1/4)$ (the
   top right vertex of [](#fig:polytope_as_convex_hull)).

4. For [](#eqn:tableau_four): we set the non-basic variables to 0:

   $$x_1=0\qquad s_1=0$$

   The remaining linear system from the tableau is:

   $$
        \begin{align*}
            72x_2=24\\
            9s_2=6
        \end{align*}
   $$

   Solving this gives: $(x_1, x_2)=(0, 1/3)$ (the
   top left vertex of [](#fig:polytope_as_convex_hull)).

We have recovered all four vertices from the 4 tableaux of
[](#exmpl:tableaux_for_the_example). Note that in that example
through the process of applying elementary row operations to the tableaux we
moved across the edges of the polytope as shown in
[](#fig:moving_across_edges_in_a_polytope).

```{figure} ./images/moving_across_edges_in_a_polytope/main.png
:alt: The same 2D polytope with arrows showing movement across edges.
:label: fig:moving_across_edges_in_a_polytope
:height: 250px

The two-dimensional polytope defined by [](#eqn:polytope_as_convex_hull),
with arrows showing the process of moving along the edges. The various row
operations are written as short hand.
```

This process corresponds to making a non-basic variable basic and carefully
choosing which basic variable to make non-basic.

(sec:definition_integer_pivoting)=

### Definition: Integer Pivoting

**Pivoting** is the process of updating a tableau by selecting one basic
variable to leave the basis and one non-basic variable to enter it. This
corresponds to performing row operations to rewrite the system so that the
new basic variable appears with coefficient 1 in its row and 0 in all others.

In **integer pivoting**, we perform this process using only integer-preserving
row operations, such as adding or subtracting integer multiples of rows. This
is useful for maintaining exact arithmetic and geometric intuition in discrete
settings.

Suppose you are given a tableau representing a system of equations
and you choose a non-basic variable $x_j$ to enter the basis.

```{note}
**How** a particular variable $x_j$ is chosen is important and depends on the
context. Two different approaches will be considered in chapters
[](#chp:zero_sum_games) and
[](#chp:best_response_polytopes).
```

The goal is to
perform a **pivot** so that $x_j$ becomes basic and one of the current basic
variables is removed from the basis.

The pivot is carried out using the following steps:

1. **Identify the pivot column**
   Select the column of the tableau corresponding to $x_j$.

2. **Select the pivot row minimum ratio test**
   For each row $i$ where the coefficient $T_{ij} > 0$, compute the ratio:

   $$
   \frac{b_i}{T_{ij}}
   $$

   (where $b_i$ corresponds to the final column of $T$.)

   Choose the row $r$ with the **smallest non-negative ratio**. The basic
   variable in this row will leave the basis.

3. **Eliminate the pivot column in all other rows**
   For each row $i \neq r$, if necessary multiply it by a suitable **integer
   multiplier** and then
   subtract suitable **integer multiples** of row $r$
   so that the entry in column $j$ becomes zero.

After these steps, the tableau reflects a new basic solution where $x_j$ is
basic, and one previous basic variable has become non-basic.

````{attention}
The mimimum ratio test corresponds to finding which of the inequalities will
become "tight" first.

For example for [](#eqn:tableau_two) recall:

$$
T^{(1)} = \begin{pmatrix}
           1 & 3 & 1 & 0 & 1\\
           3 & 1 & 0 & 1 & 1
    \end{pmatrix}
$$

which has non basic variables $x_1$ and $x_2$. We have a choice of letting
either of those two variables becoming basic. Let us choose $x_2$ to become
basic. This requires us to choose which row will gain a 0 in the second column.

This choice corresponds to choosing which of the following two constraints
becomes a tight equality first:

$$
\begin{align*}
x_1 + 3x_2 &\leq 1\\
3x_1 + x_2 &\leq 1\\
\end{align*}
$$

or equivalently:

$$
\begin{align*}
x_1 + 3x_2 + s_1&= 1\\
3x_1 + x_2 + s_2&= 1\\
\end{align*}
$$

as we want $x_2$ to enter while $x_1$ remains 0 this yields:

$$
\begin{align*}
3x_2 + s_1&= 1\\
x_2 + s_2&= 1\\
\end{align*}
$$

Either $s_1$ or $s_2$ must become 0 as shown in
[](#fig:graphical_representation_of_the_minimum_ratio_test). So either:

$$
\begin{align*}
x_2&= 1/3\\
x_2&= 1\\
\end{align*}
$$

Note that if $x_2=1$ then the first constraint is not valid which is what the
minimum ratio test is checking. The minimum ratio test would ensure we pivot
on the first row.

```{figure} ./images/graphical_representation_of_the_minimum_ratio_test/main.png
:alt: Graphical representation of the minimum ratio test.
:label: fig:graphical_representation_of_the_minimum_ratio_test
:height: 450px

Choosing which variable to make 0 which corresponds to it become basic. Given a
choice of making $x_2$ non-basic, we move along the corresponding edge until we
arrive at the first inequality constraint. This is equivalent to the minimum
ratio test.
```
````

### Example: Moving from $T^{(1)}$ to $T^{(2)}$

Let us start at:

$$
T^{(1)} = \begin{pmatrix}
           1 & 3 & 1 & 0 & 1\\
           3 & 1 & 0 & 1 & 1
    \end{pmatrix}
$$

The non-basic variables are $x_1$ and $x_2$. Let us choose to let $x_2$ become
basic. This corresponds to the second column of the tableau.

Next we use the minimum ratio test:

1. The ratio for the first row: $\frac{1}{3}$
2. The ratio for the second row: $\frac{1}{1}$

Both of these are non-negative and the minimum value is obtained in the first
row. Thus we pivot on the first row making the value in the second column and
"all other rows" (in this case just the second row) 0.

Multiplying $T^{(1)}$'s row 2 by 3 and subtracting row 1 gives:

$$
T^{(2)} = \begin{pmatrix}
           1 & 3 & 1 & 0 & 1\\
           8 & 0 & -1 & 3 & 2
    \end{pmatrix}
$$

Using [](#sec:equivalence_between_a_tableau_and_a_vertex) we set the basic
variables to 0:

$$x_1=0\qquad s_1=0$$

The remaining linear system from the tableau is:

$$
    \begin{align*}
        3x_2=1\\
        3s_2=2
    \end{align*}
$$

Solving this gives: $(x_1, x_2)=(0, 1/3)$.

## Exercises

### Exercise: Polytope Representation

For each of the following sets of vertices:

- Draw the corresponding polytope.
- Write the polytope as the intersection of a set of halfspaces (i.e.
  inequalities).

1. $ V = \{(0, 0), (0, 1), (1, 0), (1, 1)\} $
2. $ V = \{(0, 0), (0, \tfrac{1}{4}), (1, \tfrac{2}{3}), (2, \tfrac{1}{5})\} $
3. $ V = \{(0, 0), (0, \tfrac{1}{4}), (1, \tfrac{2}{3}), (2, \tfrac{1}{5}), (1,
   0)\} $

---

(exer:basic_and_non_basic_variables)=

### Exercise: Basic and Non-Basic Variables

For each of the following tableaux, identify the **basic** and **non-basic**
variables:

1.  $$
    T^{(a)} =
    \begin{pmatrix}
    1 & 0 & 5 & 1 & 1\\
    0 & 1 & 4 & 9 & 1
    \end{pmatrix}
    $$

2.  $$
    T^{(b)} =
    \begin{pmatrix}
    4 & 8 & 1 & 0 & 1\\
    8 & 1 & 0 & 1 & 1
    \end{pmatrix}
    $$

### Exercise: Integer Pivoting

For the tableaux in [](#exer:basic_and_non_basic_variables):

For each **non-basic variable**, perform one step of integer pivoting:

1. Identify the pivot column;
2. Perform the **minimum ratio test** to determine the pivot row;
3. Execute the required **row operations** to complete the pivot.

## Programming

### Using SciPy to obtain the convex hull

The SciPy library has functionality to obtain the convex hull of a set of
vertices.

```{code-cell} python3
import scipy.spatial
import numpy as np

V = [np.array([0, 0]), np.array([1 / 3, 0]), np.array([1 / 4, 1 / 4]),
np.array([0, 1 / 3])]
P = scipy.spatial.ConvexHull(V)
scipy.spatial.convex_hull_plot_2d(P);
```

The obtained convex hull can be used to get the system of linear inequalities:

```{code-cell} python3
P.equations
```

```{note}
The last two rows can be rescaled to give the original inequalities of
[](#eqn:polytope_as_intersection_of_halfspaces).
```

### Using SciPy to obtain the half space

The Scipy library has functionality to obtain the vertices from a given
intersection of half spaces.

First we create the system of linear inequalities $Mx \leq b$, this is done
passing: $(M, -b)$ as single matrix

```{code-cell} python3
halfspace = np.array(
    (
        (-1, 0, 0),
        (0, -1, 0),
        (3, 1, -1),
        (1, 3, -1),
    )
)
```

We need to pass a point known to be in the interior of the Polytope.
Now we can obtain the vertices the original vertices from
[](#eqn:polytope_as_convex_hull).

```{code-cell} python3
P = scipy.spatial.HalfspaceIntersection(halfspace, interior_point=np.array((1/5,
1/5)))
P.intersections
```

### Carrying out row operations using NumPy

NumPy's array operations allow for straightforward row operations.

```{code-cell} python3
T_1 = np.array(
    (
        (1, 3, 1, 0, 1),
        (3, 1, 0, 1, 1),
    )
)
T_2 = T_1
T_2[0] = 3 * T_2[0] - T_2[1]
T_2
```

### Pivoting tableaux with Nashpy

NashPy has some internal functionality for integer pivoting, which at present is
not designed to be
user facing but is nonetheless useable:

```{code-cell} python3
import nashpy as nash

T = nash.linalg.Tableau(T_2)
```

Having created this tableau we can get the indices of the basic and non-basic
variables:

```{code-cell} python3
T.basic_variables
```

```{code-cell} python3
T.non_basic_variables
```

```{note}
Recall that Python uses 0 based indexing: the first variable/column corresponds
to index 0.
```

We can pivot the tableau on a given column and given row:

```{code-cell} python3
T._pivot(column_index=1, pivot_row_index=1)
```

This pivoted on the second column (index 1) returning which non-basic variable
becomes basic as a result.

We can look at the tableau:

```{code-cell} python3
T._tableau
```

## Notable Research

The concept of pivoting and tableaux was first introduced by the mathematician
George Dantzig in a 1947 report during his tenure at the Pentagon [@dantzig1947maximization].

The initial publication of this idea is found in [@dantzig1951maximization].
Although Dantzig did not explicitly mention tableaux, they naturally emerged as
an efficient method for traversing the edges of a polytope.

In [@dantzig2020impact] (originally published in 1990), Dantzig shares the
following anecdote:

> "The first idea that would occur to anyone as a technique for solving a linear
> program, aside from the obvious one of moving through the interior of the
> convex set, is that of moving from one vertex to the next along the edges of
> the polyhedral set. I discarded this idea immediately as impractical in higher
> dimensional spaces. It seemed intuitively obvious that there would be far too
> many vertices and edges to wander over in the general case for such a method
> to be efficient.
>
> When Hurwicz came to visit me at the Pentagon in the summer of 1947, I told
> him how I had discarded this vertex-edge approach as intuitively inefficient
> for solving LP. I suggested instead that we study the problem in the geometry
> of columns rather than the usual one of the rows -- column geometry incidentally
> was the one I had used in my Ph.D. thesis on the Neyman-Pearson Lemma. We
> dubbed the new method 'climbing the bean pole.'"

A comprehensive historical overview is provided in [@todd2002many], which
includes
several other notable publications.

Two significant works connect integer pivoting to game theory:

- In a 1951 book chapter, Dantzig established a connection for
  [zero-sum games](#chp:zero_sum_games), as described in
  [@adler2013equivalence].

- [@lemke1964equilibrium] introduces the [Lemke-Howson
  algorithm](#chp:best_response_polytopes),
  which employs integer pivoting to find Nash equilibria in general games.

## Conclusion

Integer pivoting offers a powerful lens through which to understand movement
across the vertices of polytopes, providing a concrete foundation for key
algorithms in linear programming and game theory. Through the tableau
representation, we are able to:

- Translate systems of inequalities into algebraic form;
- Perform exact row operations that correspond to movement along polytope edges;
- Interpret basic and non-basic variables as defining vertices and directions of movement.

These tools underpin the algorithms used for zero-sum games and Nash equilibrium computation.

[](#tbl:integer_pivoting) summarises the key concepts introduced in this
appendix.

```{table} Summary of integer pivoting
:name: tbl:integer_pivoting
:align: center

| Concept                | Description                                                            |
| ---------------------- | ---------------------------------------------------------------------- |
| Polytope (convex hull) | Set of convex combinations of finite points                            |
| Polytope (half-spaces) | Set of solutions to a system of linear inequalities                    |
| Slack variable         | Converts an inequality into an equality with a non-negative remainder  |
| Tableau                | Augmented matrix form of a linear system with slack variables          |
| Basic variable         | Variable corresponding to a pivot column; used to determine a vertex   |
| Non-basic variable     | Set to 0 when solving for vertex from tableau                          |
| Pivoting               | Row operations used to exchange basic and non-basic variables          |
| Minimum ratio test     | Selects the pivot row to preserve feasibility during a pivot           |
| Integer pivoting       | Pivoting using only integer row operations to maintain exact structure |
```

```{important}
Each tableau corresponds to a vertex of a polytope, and integer pivoting
lets us move precisely from one vertex to a neighbouring one, forming the
algorithmic core of many key results in game theory.
```

---

(solutions:integer_pivoting)=

## Solutions

### Solution to Exercise: Polytope Representation

**1.** $V = \{(0,0), (0,1), (1,0), (1,1)\}$

This is the unit square. As the intersection of half-spaces:

$$
\mathcal{P} = \{x \in \mathbb{R}^2 \mid x_1 \geq 0,\ x_2 \geq 0,\ x_1 \leq 1,\ x_2 \leq 1\}
$$

In standard form $Mx \leq b$:

$$
M = \begin{pmatrix}-1 & 0 \\ 0 & -1 \\ 1 & 0 \\ 0 & 1\end{pmatrix},
\qquad b = \begin{pmatrix}0 \\ 0 \\ 1 \\ 1\end{pmatrix}.
$$

**2.** $V = \{(0,0), (0, 1/4), (1, 2/3), (2, 1/5)\}$

We must find the convex hull of these four points. Computing the supporting
half-spaces (using the convex hull):

The edges of the convex hull connect:
- $(0,0)$ to $(0,1/4)$: left edge, $x_1 \geq 0$.
- $(0,0)$ to $(2,1/5)$: bottom edge. The line through these points has slope
  $1/10$, giving $x_2 \geq x_1/10$, i.e., $x_1 - 10 x_2 \leq 0$.
- $(0,1/4)$ to $(1,2/3)$: upper-left edge. Slope = $(2/3 - 1/4)/1 = 5/12$.
  Line: $x_2 - 1/4 = (5/12)(x_1 - 0)$, i.e., $x_2 = 5x_1/12 + 1/4$, giving
  $-5x_1 + 12x_2 \leq 3$.
- $(1,2/3)$ to $(2,1/5)$: upper-right edge. Slope = $(1/5 - 2/3)/1 = -7/15$.
  Line: $x_2 - 2/3 = (-7/15)(x_1 - 1)$, i.e., $7x_1 + 15x_2 \leq 17$.
- $(2,1/5)$ to $(0,0)$: see bottom edge above (they share the same bounding
  line $x_1 - 10x_2 \leq 0$ together with $x_1 \leq 2$).

A complete half-space representation is:

$$
x_1 \geq 0, \quad x_1 - 10 x_2 \leq 0, \quad -5x_1 + 12x_2 \leq 3, \quad 7x_1 + 15x_2 \leq 17, \quad x_1 \leq 2.
$$

```{code-cell} python3
import scipy.spatial
import numpy as np
import matplotlib.pyplot as plt

V1 = np.array([[0,0],[0,1],[1,0],[1,1]], dtype=float)
hull1 = scipy.spatial.ConvexHull(V1)
fig, axes = plt.subplots(1, 3, figsize=(9, 3))

for ax, V, title in zip(
    axes,
    [
        np.array([[0,0],[0,1],[1,0],[1,1]], dtype=float),
        np.array([[0,0],[0,1/4],[1,2/3],[2,1/5]], dtype=float),
        np.array([[0,0],[0,1/4],[1,2/3],[2,1/5],[1,0]], dtype=float),
    ],
    ["V1: unit square", "V2: 4 points", "V3: 5 points"]
):
    hull = scipy.spatial.ConvexHull(V)
    scipy.spatial.convex_hull_plot_2d(hull, ax=ax)
    ax.scatter(V[:, 0], V[:, 1], color="red", zorder=5)
    ax.set_title(title)

plt.tight_layout()
```

```{code-cell} python3
# Show the half-space inequalities for V2
V2 = np.array([[0,0],[0,1/4],[1,2/3],[2,1/5]], dtype=float)
hull2 = scipy.spatial.ConvexHull(V2)
print("Half-space equations for V2 (each row: [a, b, c] means a*x1 + b*x2 + c <= 0):")
print(hull2.equations)
```

**3.** $V = \{(0,0), (0,1/4), (1,2/3), (2,1/5), (1,0)\}$

The point $(1,0)$ lies inside or on the boundary of the convex hull of $V$ from
part 2 (it is below the bottom edge $x_1 - 10x_2 \leq 0$ at $x_1=1$:
$1 - 0 = 1 > 0$, so $(1,0)$ is actually outside that edge). Adding $(1,0)$
changes the convex hull.

```{code-cell} python3
V3 = np.array([[0,0],[0,1/4],[1,2/3],[2,1/5],[1,0]], dtype=float)
hull3 = scipy.spatial.ConvexHull(V3)
print("Half-space equations for V3:")
print(hull3.equations)
print("\nVertices of hull3:", V3[hull3.vertices])
```

---

(solutions:integer_pivoting:basic_nonbasic)=

### Solution to Exercise: Basic and Non-Basic Variables

**1.** For

$$
T^{(a)} = \begin{pmatrix}
1 & 0 & 5 & 1 & 1 \\
0 & 1 & 4 & 9 & 1
\end{pmatrix}
$$

The columns (from left to right) correspond to variables $x_1, x_2, x_3, x_4$
(or $s_1, s_2$ if these are slack variables). A basic variable corresponds to a
column that has exactly one nonzero entry (a unit vector). Inspecting the
columns:

- Column 1 ($x_1$): $(1, 0)^T$, a unit vector. **Basic.**
- Column 2 ($x_2$): $(0, 1)^T$, a unit vector. **Basic.**
- Column 3 ($x_3$): $(5, 4)^T$, not a unit vector. **Non-basic.**
- Column 4 ($x_4$): $(1, 9)^T$, not a unit vector. **Non-basic.**

**Basic variables:** $x_1, x_2$.
**Non-basic variables:** $x_3, x_4$.

Setting non-basic variables to zero: $x_3 = x_4 = 0$, the system gives
$x_1 = 1$ and $x_2 = 1$, so the corresponding vertex is $(x_1, x_2) = (1, 1)$
(if $x_3, x_4$ are the original variables, otherwise the vertex is in the
$x_1, x_2$ coordinates).

**2.** For

$$
T^{(b)} = \begin{pmatrix}
4 & 8 & 1 & 0 & 1 \\
8 & 1 & 0 & 1 & 1
\end{pmatrix}
$$

- Column 1 ($x_1$): $(4, 8)^T$, not a unit vector. **Non-basic.**
- Column 2 ($x_2$): $(8, 1)^T$, not a unit vector. **Non-basic.**
- Column 3 ($s_1$): $(1, 0)^T$, a unit vector. **Basic.**
- Column 4 ($s_2$): $(0, 1)^T$, a unit vector. **Basic.**

**Basic variables:** $s_1, s_2$.
**Non-basic variables:** $x_1, x_2$.

Setting non-basic variables to zero: $x_1 = x_2 = 0$, and from the last
column, $s_1 = 1$, $s_2 = 1$. This corresponds to the origin vertex.

---

### Solution to Exercise: Integer Pivoting

We perform integer pivoting on each non-basic variable for the two tableaux
from the exercise above.

**Pivoting on $T^{(a)}$:** The non-basic variables are $x_3$ and $x_4$.

**Pivot on $x_3$ (column 3):**

The pivot column entries are $(5, 4)$. Both are positive, so we apply the
minimum ratio test:

- Row 1: $b_1 / T_{13} = 1/5$
- Row 2: $b_2 / T_{23} = 1/4$

The minimum ratio is $1/5$ in row 1, so we pivot on row 1.

To eliminate $x_3$ from row 2 by integer pivoting (as defined in
[](#sec:definition_integer_pivoting)), multiply row 2 by 5 and subtract 4 times
row 1, zeroing out column 3 in row 2:

$$
\begin{align*}
\text{new row 2} &= 5 \times (0,1,4,9,1) - 4 \times (1,0,5,1,1) \\
&= (0,5,20,45,5) - (4,0,20,4,4) = (-4, 5, 0, 41, 1).
\end{align*}
$$

The updated tableau is:

$$
T^{(a')} = \begin{pmatrix}
1 & 0 & 5 & 1 & 1 \\
-4 & 5 & 0 & 41 & 1
\end{pmatrix}
$$

The basic variables are now $x_3$ (from row 1) and $x_2$ (from row 2). Setting
non-basic variables $x_1 = x_4 = 0$: from row 1, $5x_3 = 1 \Rightarrow x_3 = 1/5$;
from row 2, $5x_2 = 1 \Rightarrow x_2 = 1/5$.

**Pivot on $x_4$ (column 4) of $T^{(a)}$:**

The pivot column entries are $(1, 9)$. Both positive. Minimum ratio test:

- Row 1: $1/1 = 1$
- Row 2: $1/9$

Minimum is $1/9$ in row 2. Pivot on row 2. Eliminate $x_4$ from row 1:
multiply row 1 by 9 and subtract row 2 (integer pivoting):

$$
\begin{align*}
\text{new row 1} &= 9 \times (1,0,5,1,1) - 1 \times (0,1,4,9,1) \\
&= (9,0,45,9,9) - (0,1,4,9,1) = (9, -1, 41, 0, 8).
\end{align*}
$$

The updated tableau is:

$$
T^{(a'')} = \begin{pmatrix}
9 & -1 & 41 & 0 & 8 \\
0 & 1 & 4 & 9 & 1
\end{pmatrix}
$$

**Pivoting on $T^{(b)}$:** The non-basic variables are $x_1$ and $x_2$.

**Pivot on $x_1$ (column 1):**

The pivot column entries are $(4, 8)$. Both positive. Minimum ratio test:

- Row 1: $1/4$
- Row 2: $1/8$

Minimum is $1/8$ in row 2. Pivot on row 2. Eliminate $x_1$ from row 1:

$$
\begin{align*}
\text{new row 1} &= 8 \times (4,8,1,0,1) - 4 \times (8,1,0,1,1) \\
&= (32,64,8,0,8) - (32,4,0,4,4) = (0, 60, 8, -4, 4).
\end{align*}
$$

The updated tableau is:

$$
T^{(b')} = \begin{pmatrix}
0 & 60 & 8 & -4 & 4 \\
8 & 1 & 0 & 1 & 1
\end{pmatrix}
$$

Basic variables are now $x_1$ (row 2) and $s_1$ (row 1). Setting $x_2 = s_2 = 0$:
from row 2, $8x_1 = 1 \Rightarrow x_1 = 1/8$.

**Pivot on $x_2$ (column 2):**

Starting from $T^{(b)}$, the pivot column entries are $(8, 1)$. Both positive.
Minimum ratio test:

- Row 1: $1/8$
- Row 2: $1/1 = 1$

Minimum is $1/8$ in row 1. Pivot on row 1. Eliminate $x_2$ from row 2:

$$
\begin{align*}
\text{new row 2} &= 8 \times (8,1,0,1,1) - 1 \times (4,8,1,0,1) \\
&= (64,8,0,8,8) - (4,8,1,0,1) = (60, 0, -1, 8, 7).
\end{align*}
$$

The updated tableau is:

$$
T^{(b'')} = \begin{pmatrix}
4 & 8 & 1 & 0 & 1 \\
60 & 0 & -1 & 8 & 7
\end{pmatrix}
$$

Basic variables are now $s_1$ (row 1) and $x_2$ (row 2). Setting $x_1 = s_2 = 0$:
from row 1, $8x_2 + s_1 = 1$; from row 2, $8s_2 = 7$... Actually with $x_1 = s_2 = 0$:
row 1 gives $8x_2 = 1 \Rightarrow x_2 = 1/8$.

```{code-cell} python3
import numpy as np

# Tableau T^(a)
T_a = np.array([[1, 0, 5, 1, 1],
                [0, 1, 4, 9, 1]], dtype=float)

# Pivot on column 3 (index 2), pivot row 1 (index 0): minimum ratio 1/5
T_a_pivot_x3 = T_a.copy()
pivot_col, pivot_row = 2, 0
# new_row2 = 5*row2 - 4*row1 (to zero column 3 in row 2)
T_a_pivot_x3[1] = T_a[1] * T_a[0, pivot_col] - T_a[0] * T_a[1, pivot_col]
print("T^(a) after pivot on x3 (col 3, row 1):")
print(T_a_pivot_x3)

# Pivot on column 4 (index 3) of T^(a), pivot row 2 (index 1): minimum ratio 1/9
T_a_pivot_x4 = T_a.copy()
pivot_col, pivot_row = 3, 1
# new_row1 = 9*row1 - row2 (to zero column 4 in row 1)
T_a_pivot_x4[0] = T_a[0] * T_a[1, pivot_col] - T_a[1] * T_a[0, pivot_col]
print("\nT^(a) after pivot on x4 (col 4, row 2):")
print(T_a_pivot_x4)
```

```{code-cell} python3
# Tableau T^(b)
T_b = np.array([[4, 8, 1, 0, 1],
                [8, 1, 0, 1, 1]], dtype=float)

# Pivot on x1 (col 1, index 0), pivot row 2 (index 1): minimum ratio 1/8
T_b_pivot_x1 = T_b.copy()
pivot_col, pivot_row = 0, 1
T_b_pivot_x1[0] = T_b[0] * T_b[1, pivot_col] - T_b[1] * T_b[0, pivot_col]
print("T^(b) after pivot on x1 (col 1, row 2):")
print(T_b_pivot_x1)

# Pivot on x2 (col 2, index 1), pivot row 1 (index 0): minimum ratio 1/8
T_b_pivot_x2 = T_b.copy()
pivot_col, pivot_row = 1, 0
T_b_pivot_x2[1] = T_b[1] * T_b[0, pivot_col] - T_b[0] * T_b[1, pivot_col]
print("\nT^(b) after pivot on x2 (col 2, row 1):")
print(T_b_pivot_x2)
```
