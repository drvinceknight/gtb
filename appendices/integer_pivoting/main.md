---
kernelspec:
  name: python3
  display_name: "Python 3"
numbering:
  enumerator: A1.%s
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
spaces**—
that is, bounded regions formed by linear inequalities. This alternate view is
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
  3x_1 + 3x \leq 1 \\
\end{array}
\right\}
$$

The inequalities in [](#eqn:polytope_as_intersection_of_halfspaces) define
supporting half-spaces that together enclose the polytope.

Polytopes appear throughout mathematics, particularly in **optimisation**, where
they form the feasible regions of linear programs. These connections are central
to game theory, especially in the study of [zero-sum games](#chp:zero_sum_games)
and [general games](#chp:lemke_howson_algorithm).

While this example lives in $\mathbb{R}^2$, the techniques extend to
**higher-dimensional polytopes**. The goal of this chapter is to develop tools
for moving from **vertex to vertex** in such polytopes—an essential idea in
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
           24 & 0 & -1 & 9 & 6
    \end{pmatrix}
$$

Multiplying $T^{(3)}$'s row 1 by 9 and adding row 2 gives:

$$
\label{eqn:tableau_four}
T^{(4)} = \begin{pmatrix}
           24 & 72 & 26 & 0 & 24\\
           24 & 0 & -1 & 9 & 6
    \end{pmatrix}
$$

There are other tableaux that correspond to the same systems of equations but
we next explore how tableaux correspond to vertices of polytopes. To do
this we need a new definition:

### Definition: Basic variables

---

A basic variable of a tableau corresponds a column that
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
- The tableau [](#eqn:tableau_four) are $s_2$ and $x_2$.

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
            8s_1=2
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
            9s_1=6
        \end{align*}
   $$

   Solving this gives: $(x_1, x_2)=(1/3, 0)$ (the
   top right vertex of [](#fig:polytope_as_convex_hull)).

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
[](#chp:lemke_howson_algorithm).
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

### Example: Moving from $T^{(1)}$ to $T^{(3)}$

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

For the tableaux in [](#exer:basic_and_non_basic_variables) (insert reference):

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

NumPy's linear array gives allows for straightforward row operations.

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

This pivoted on the first column returning which non-variable becomes basic as a
result.

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
  algorithm](#chp:lemke_howson_algorithm),
  which employs integer pivoting to find Nash equilibria in general games.

## Conclusion

Integer pivoting offers a powerful lens through which to understand movement
across the vertices of polytopes, providing a concrete foundation for key
algorithms in linear programming and game theory. Through the tableau
representation, we are able to:

- Translate systems of inequalities into algebraic form;
- Perform exact row operations that correspond to movement along polytope edges;
- Interpret basic and non-basic variables as defining vertices and directions of movement.

This chapter has introduced the core tools required to navigate these geometric
structures, setting the stage for applications in zero-sum games and Nash
equilibrium computation.

The following table summarises the key concepts introduced:

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

```{important}
Each tableau corresponds to a vertex of a polytope, and integer pivoting
lets us move precisely from one vertex to a neighboring one—forming the
algorithmic core of many key results in game theory.
```
