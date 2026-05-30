---
kernelspec:
  name: python3
  display_name: "Python 3"
numbering:
  enumerator: A1.%s
---

(app:absorbing_markov_chain)=

# Appendix: Absorbing Markov Chains

(sec:motivating_example_escaping_a_maze)=

## Motivating Example: Escaping a Maze

A student finds themselves in a strange maze of connected rooms. Some rooms
are marked as **exits**. Once the student reaches one, they leave the maze and
do not return. The other rooms are **ordinary**: the student moves between
them until they reach an exit. Each turn, the student chooses a connected room
uniformly at random.

Suppose the maze consists of six rooms labelled $1$ through $6$, with rooms $5$
and $6$ being exits. The student starts in one of the other rooms and moves
randomly along available corridors. The structure of the maze is shown below:

- Room 1 connects to Rooms 2 and 3
- Room 2 connects to Rooms 1 and 4
- Room 3 connects to Rooms 1, 4, and 5
- Room 4 connects to Rooms 2, 3, and 6
- Rooms 5 and 6 are absorbing exits

Let $P$ be the transition matrix, where rows and columns correspond to the rooms
in order:

$$
P = \begin{pmatrix}
0 & 1/2 & 1/2 & 0 & 0 & 0 \\
1/2 & 0 & 0 & 1/2 & 0 & 0 \\
1/3 & 0 & 0 & 1/3 & 1/3 & 0 \\
0 & 1/3 & 1/3 & 0 & 0 & 1/3 \\
0 & 0 & 0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0 & 0 & 1 \\
\end{pmatrix}
$$

Rooms 5 and 6 are absorbing: the student remains there once entered. The rest
are transient. In the following sections, we will compute:

- The expected number of steps before exiting the maze
- The probability of exiting through Room 5 versus Room 6
- The expected number of visits to each room

This chapter will describe a powerful mathematical tool: Markov Chains and in
particular Absorbing Markov Chains.

## Theory

### Definition of a Markov Chain

---

Let $ S = \{s_1, s_2, \dots, s_n\} $ be a finite set of **states**. A **Markov chain** is defined by:

- A sequence of random variables $ X_0, X_1, X_2, \dots $, where each $ X_t \in S $
- A **transition probability matrix** $ P \in \mathbb{R}\_{\geq 0}^{n \times n} $, where

$$
P_{ij} = \mathbb{P}(X_{t+1} = s_j \mid X_t = s_i)
$$

with $\sum_{j=1}^nP_{ij}=1$ for all $1\leq i \leq n$.

---

A state of the Markov chain can be described by a probability distribution
vector $\pi\in\mathbb{R}_[0, 1]^1$ such that $\sum_{i=1}^n \pi_i=1$.

This gives:

$$\pi^{(t + 1)} = \pi ^{(t)}P$$

and so:

$$\pi^{(t)} = \pi ^{(0)} P ^ t$$

### Example: Escaping the Maze

Let us assume that students are known to start in one of the room with equal
probability. This implies that:

$$\pi ^{(0)}=\begin{pmatrix}1/4&1/4&1/4&1/4&0&0\end{pmatrix}$$

1. Calculate $\pi ^{(1)}$
2. Calculate $\pi ^{(2)}$
3. Given that:

   $$
   P ^ {1000} \approx
   \begin{pmatrix}
   0.& 0.& 0.& 0.& 0.5455& 0.4545\\
   0.& 0.& 0.& 0.& 0.4545& 0.5455\\
   0.& 0.& 0.& 0.& 0.6364& 0.3636\\
   0.& 0.& 0.& 0.& 0.3636& 0.6364\\
   0.& 0.& 0.& 0.& 1.& 0. \\
   0.& 0.& 0.& 0.& 0.& 1.
   \end{pmatrix}
   $$

   What is the likely location of a student after 1000 time steps?

4. We have:

$$
\begin{align*}
\pi ^{(1)} &= \pi ^{(0)} P\\
           &= (1/4\cdot1/2 + 1/4 \cdot 1/3, 1/4\cdot1/2 + 1/4 \cdot 1/3, 1/4\cdot1/2 + 1/4 \cdot 1/3, 1/4\cdot1/2 + 1/4 \cdot 1/3, 1/4\cdot 1/3 + 0\cdot 1, 1/4\cdot 1/3 + 0\cdot 1)\\
           &= (5/24, 5/24, 5/24, 5/24, 1/12, 1/12)
\end{align*}
$$

2. We have:

$$
\begin{align*}
\pi ^{(2)} &= \pi ^{(1)} P\\
           &= (5/24\cdot 1/2 + 5\cdot 1/3, 5/24\cdot 1/2 + 5\cdot 1/3, 5/24\cdot 1/2 + 5\cdot 1/3, 5/24\cdot 1/2 + 5\cdot 1/3, 5/24\cdot1/3+1/2, 5/24\cdot1/3+1/2)
           &= (25/144, 25/144, 25/144, 25/144, 11/72, 11/72)
\end{align*}
$$

3. Finally:

$$
\begin{align*}
\pi ^{(1000)} &= \pi ^{(0)} P ^ 1000\\
              &\approx (0, 0, 0, 0, .5, .5)
\end{align*}
$$

We note that after 1000 time steps all of our probability is in the last two
states. This is due to the nature of the maze but also the nature of the
particular type of Markov chain which is an absorbing Markov chain: the last two
states are absorbing states.

### Definition: Absorbing Markov Chain

---

A Markov chain with transition matrix $P$ is **absorbing** if:

1. It has at least one **absorbing state**, i.e., a state $i$ such that
   $P_{ii} = 1$.

2. From every **non-absorbing** (transient) state $j$, there is a **non-zero**
   probability of reaching **some** absorbing state in a finite number of steps.

In other words, the chain cannot get "stuck" forever in a subset of transient
states.

---

An absorbing Markov chain is a Markov chain whose transition matrix $P$ can be
written (up to an ordering of states) in the following canonical form:

$$
\label{eqn:form_of_absorbing_markov_chain}
P =
\begin{pmatrix}
    Q & R\\
    0 & I
\end{pmatrix}
$$

where:

- $Q$ is the transient submatrix: it contains the probabilities of transitions
  from transient state to transient state.
- $R$ is the transition to absorption submatrix: it contains the probabilities of
  transition from transient state to absorption state.

### Example: The Maze as an absorbing Markov chain

For [](#sec:motivating_example_escaping_a_maze) the Markov chain $P$ can be
written in the form of [](#eqn:form_of_absorbing_markov_chain) with:

$$
Q = \begin{pmatrix}
0 & 1/2 & 1/2 & 0 \\
1/2 & 0 & 0 & 1/2 \\
1/3 & 0 & 0 & 1/3 \\
0 & 1/3 & 1/3 & 0 \\
    \end{pmatrix}
$$

$$
R = \begin{pmatrix}
0 & 0 \\
0 & 0 \\
1/3 & 0 \\
0 & 1/3 \\
\end{pmatrix}
$$

$$
I = \begin{pmatrix}
        1 & 0 \\
        0 & 1
\end{pmatrix}
$$

(sec:definition_of_fundamental_matrix)=

### Definition: Fundamental Matrix

For an absorbing Markov chain in the form [](#eqn:form_of_absorbing_markov_chain) the fundamental matrix $N$ is given by:

$$
N = (I - Q) ^ {-1}
$$

The entry $N_{ij}$ gives the expected number of times the process is in transient
state $j$ before being absorbed having started in state $i$.

(sec:example_fundamental_matrix_of_the_maze)=

### Example: Fundamental matrix of the Maze

For [](#sec:motivating_example_escaping_a_maze) the fundamental matrix is given
by:

$$
\begin{align*}
N &= \left(
    \begin{pmatrix}
        1 & 0 & 0 & 0\\
        0 & 1 & 0 & 0\\
        0 & 0 & 1 & 0\\
        0 & 0 & 0 & 1
    \end{pmatrix}
    -
\begin{pmatrix}
0 & 1/2 & 1/2 & 0 \\
1/2 & 0 & 0 & 1/2 \\
1/3 & 0 & 0 & 1/3 \\
0 & 1/3 & 1/3 & 0 \\
    \end{pmatrix}
\right) ^ {-1}\\
  &= \left(
    \begin{pmatrix}
        1 & -1/2 & -1/2 & 0\\
    -1/2 & 1 & 0 & -1/2\\
        -1/3 & 0 & 1 & -1/3\\
        0 & -1/3 & -1/3 & 1
    \end{pmatrix}
\right) ^ {-1}\\
\end{align*}
$$

This inverse can be computed, a technique for doing this will be reviewed in
[](#sec:gauss_jordan) to give:

$$
N = \begin{pmatrix}26/11 & 18/11 & 18/11 & 15/11\\
18/11 & 26/11 & 15/11 & 18/11\\
12/11 & 10/11 & 21/11 & 12/11\\
10/11 & 12/11 & 12/11 & 21/11
\end{pmatrix}
$$

We can read from this matrix that for example, starting in state $i=2$ the
student will visit state $j=3$ on average $N_{23}=1.36$ times.

This will allow us to identify which absorption state is the most likely.

(sec:definition_of_absorption_probability_matrix)=

### Definition: Absorption Probability Matrix

For an absorbing Markov chain in the form [](#eqn:form_of_absorbing_markov_chain) the absorption probability
matrix $B$ is given by:

$$
B = NR
$$

The probability of being absorbed in to absorbing state $j$ having started at
state $i$ is $B_{ij}$.

### Example: Probability of absorbing state in the Maze

For [](#sec:motivating_example_escaping_a_maze) the absorption probability
matrix is given by:

$$
\begin{align*}
    B & = N R\\
      & = \begin{pmatrix}26/11 & 18/11 & 18/11 & 15/11\\
18/11 & 26/11 & 15/11 & 18/11\\
12/11 & 10/11 & 21/11 & 12/11\\
10/11 & 12/11 & 12/11 & 21/11
\end{pmatrix}
\begin{pmatrix}
0 & 0 \\
0 & 0 \\
1/3 & 0 \\
0 & 1/3 \\
\end{pmatrix}\\
    &=\begin{pmatrix}
        6/11 & 5/11\\
        5/11 & 6/11\\
        7/11 & 4/11\\
        4/11 & 7/11
      \end{pmatrix}
\end{align*}
$$

(sec:gauss_jordan)=

### Definition: Gauss-Jordan Method for inverting a matrix

The Gauss-Jordan Method for inverting a non-singular matrix $A\in\mathbb{R}^{n \times n}$:

1. Set up the augmented matrix $[A \mid I]$, where $I$ is the $n \times n$ identity matrix.
2. Use row operations:
   - Swap rows;
   - Scaling rows;
   - Adding scalar multiples of a row to another row.
3. Once the left hand side of the augmented matrix become $I$ the right hand
   side is $A^{-1}$.

### Example: Compute the inverse of a 4 by 4 matrix

Let us compute the inverse of:

$$
    A =
    \begin{pmatrix}
        1 & -1/2 & -1/2 & 0\\
    -1/2 & 1 & 0 & -1/2\\
        -1/3 & 0 & 1 & -1/3\\
        0 & -1/3 & -1/3 & 1
    \end{pmatrix}
$$

First we create the augmented matrix:

$$
    \begin{pmatrix}
        1 & -1/2 & -1/2 & 0 & 1 & 0 & 0 & 0\\
    -1/2 & 1 & 0 & -1/2     & 0 & 1 & 0 & 0\\
        -1/3 & 0 & 1 & -1/3 & 0 & 0 & 1 & 0\\
        0 & -1/3 & -1/3 & 1 & 0 & 0 & 0 & 1
    \end{pmatrix}
$$

Let us add $1/2$ row 1 to row 2 and $1/3$ row 1 to row 3:

$$
    \begin{pmatrix}
        1 & -1/2 & -1/2 & 0 & 1 & 0 & 0 & 0\\
        0 & 3/4 & -1/4 & -1/2    & 1/2 & 1 & 0 & 0\\
        0 & -1/6 &  5/6 & -1/2 & 1/3 & 0 & 1 & 0\\
        0 & -1/3 & -1/3 & 1 & 0 & 0 & 0 & 1
    \end{pmatrix}
$$

Let us multiple row 2 by $4/3$ (to create a leading 1):

$$
    \begin{pmatrix}
1 & - 1/2 & - 1/2 & 0 & 1 & 0 & 0 & 0\\
0 & 1 & - 1/3 & - 2/3 & 2/3 & 4/3 & 0 & 0\\
0 & - 1/6 & 5/6 & - 1/3 & 1/3 & 0 & 1 & 0\\
0 & - 1/3 & - 1/3 & 1 & 0 & 0 & 0 & 1
    \end{pmatrix}
$$

Let us:

- Add $1/2$ of row 2 to row 1;
- Add $1/6$ of row 2 to row 3.
- Add $1/3$ of row 2 to row 4.

$$
    \begin{pmatrix}
1 & 0 & - 2/3 & - 1/3 & 4/3 & 2/3 & 0 & 0\\
0 & 1 & - 1/3 & - 2/3 & 2/3 & 4/3 & 0 & 0\\
0 & 0 & 7/9 & - 4/9 & 4/9 & 2/9 & 1 & 0\\
0 & 0 & - 4/9 & 7/9 & 2/9 & 4/9 & 0 & 1
    \end{pmatrix}
$$

Let us multiply row 3 by $9/7$:

$$
\begin{pmatrix}
1 & 0 & - 2/3 & - 1/3 & 4/3 & 2/3 & 0 & 0\\
0 & 1 & - 1/3 & - 2/3 & 2/3 & 4/3 & 0 & 0\\
0 & 0 & 1 & - 4/7 & 4/7 & 2/7 & 9/7 & 0\\
0 & 0 & - 4/9 & 7/9 & 2/9 & 4/9 & 0 & 1
\end{pmatrix}
$$

Let us:

- Add $2/3$ of row 3 to row 1;
- Add $1/3$ of row 3 to row 2.
- Add $4/9$ of row 3 to row 4.

$$
\begin{pmatrix}
1 & 0 & 0 & - 5/7 & 12/7 & 6/7 & 6/7 & 0\\
0 & 1 & 0 & - 6/7 & 6/7 & 10/7 & 3/7 & 0\\
0 & 0 & 1 & - 4/7 & 4/7 & 2/7 & 9/7 & 0\\
0 & 0 & 0 & 11/21 & 10/21 & 4/7 & 4/7 & 1
\end{pmatrix}
$$

Let us multiply row 4 by $21/11$:

$$
\begin{pmatrix}
1 & 0 & 0 & - 5/7 & 12/7 & 6/7 & 6/7 & 0\\
0 & 1 & 0 & - 6/7 & 6/7 & 10/7 & 3/7 & 0\\
0 & 0 & 1 & - 4/7 & 4/7 & 2/7 & 9/7 & 0\\
0 & 0 & 0 & 1 & 10/11 & 12/11 & 12/11 & 21/11
\end{pmatrix}
$$

Let us:

- Add $5/7$ of row 4 to row 1;
- Add $6/7$ of row 4 to row 2.
- Add $4/7$ of row 4 to row 3.

$$
\begin{pmatrix}
1 & 0 & 0 & 0 & 26/11 & 18/11 & 18/11 & 15/11\\
0 & 1 & 0 & 0 & 18/11 & 26/11 & 15/11 & 18/11\\
0 & 0 & 1 & 0 & 12/11 & 10/11 & 21/11 & 12/11\\
0 & 0 & 0 & 1 & 10/11 & 12/11 & 12/11 & 21/11
\end{pmatrix}
$$

This has created the identity matrix on the left and results in the following
inverse of $A$ (which was used in [](#sec:example_fundamental_matrix_of_the_maze)):

$$
A^{-1} =
    \begin{pmatrix}
        26/11 & 18/11 & 18/11 & 15/11\\
        18/11 & 26/11 & 15/11 & 18/11\\
        12/11 & 10/11 & 21/11 & 12/11\\
        10/11 & 12/11 & 12/11 & 21/11
    \end{pmatrix}
$$

## Exercises

### Exercise: Transition Classification

Consider the following Markov chain with transition matrix:

$$
P = \begin{pmatrix}
0.5 & 0.5 & 0 & 0 \\
0.25 & 0.5 & 0.25 & 0 \\
0 & 0.25 & 0.5 & 0.25 \\
0 & 0 & 0 & 1
\end{pmatrix}
$$

1. Identify which states are transient and which are absorbing.
2. Write $P$ in canonical form.
3. Compute the fundamental matrix $N$.
4. Use $N$ to compute the expected number of steps until absorption starting from each transient state.

---

### Exercise: Expected Visits

Let $P$ be the maze transition matrix from
[Section @sec:motivating_example_escaping_a_maze]. Suppose the student starts
in Room 1.

1. How many times on average will the student visit Room 4 before reaching an exit?
2. Which ordinary room is visited most often in expectation when starting from Room 3?

---

### Exercise: Symbolic Fundamental Matrix

Let

$$
Q = \begin{pmatrix}
0 & a \\
b & 0
\end{pmatrix}
$$

where $0 < a, b < 1$.

1. Compute the fundamental matrix $N = (I - Q)^{-1}$ symbolically.
2. Express the expected number of total steps before absorption from each starting state in terms of $a$ and $b$.

---

### Exercise: Absorption Probabilities

Suppose a Markov chain has:

$$
Q = \begin{pmatrix}
0.2 & 0.3 \\
0.4 & 0.1
\end{pmatrix},
\qquad
R = \begin{pmatrix}
0.5 & 0 \\
0 & 0.5
\end{pmatrix}
$$

1. Compute the fundamental matrix $N$.
2. Compute the absorption probability matrix $B = NR$.
3. Interpret the meaning of $B_{12}$.

## Programming

The main computational tools required in this chapter are matrix manipulations.
In this section, we demonstrate two Python libraries that support this: one for
**numerical** computation and one for **symbolic** computation. These operate in
different number systems, allowing both approximate and exact linear algebra.

(sec:using_numby_to_carry_out_numeric_matrix_calculations)=

### Using Numpy for Numeric Matrix Calculations

Numpy [@harris2020array] is the standard Python library for numerical
computations. Here are some basic examples:

```{code-cell} python3
import numpy as np

A = np.array(
    [
        [4, 5],
        [7, 8],
    ]
)
B = np.array(
    [
        [1 / 4, 1 / 5],
        [8, 7],
    ]
)

A + 7 * B
```

Matrix multiplication is carried out using the `@` operator:

```{code-cell} python3
A @ B
```

```{warning}
In Numpy, the `*` operator performs elementwise multiplication.
```

To raise a matrix to a power or compute its inverse, we use the `numpy.linalg`
submodule:

```{code-cell} python3
import numpy.linalg

np.linalg.matrix_power(A, 3)
```

```{warning}
In Numpy, the `**` operator performs elementwise exponentiation.
```

```{code-cell} python3
np.linalg.inv(A)
```

### Using Sympy for Symbolic Matrix Computations

Sympy [@10.7717/peerj-cs.103] is the standard Python library for symbolic
mathematics. It allows for exact arithmetic using symbolic expressions:

```{code-cell} python3
import sympy as sym

a = sym.Symbol("a")
b = sym.Symbol("b")
c = sym.Symbol("c")
d = sym.Symbol("d")

A = sym.Matrix(
    [
        [a, b],
        [c, d],
    ]
)
```

Most operations follow the same syntax as in Numpy. For matrix exponentiation
and inversion:

```{code-cell} python3
A ** 3
```

```{code-cell} python3
A.inv()
```

### Using Sympy for Exact Row Operations

Row operations can also be performed using Sympy with exact rational arithmetic.
The `S` operator creates exact symbolic constants:

```{code-cell} python3
A = sym.Matrix(
    [
        [1          , -sym.S(1)/2, -sym.S(1)/2, 0          , 1, 0, 0, 0],
        [-sym.S(1)/2, 1          , 0          , -sym.S(1)/2, 0, 1, 0, 0],
        [-sym.S(1)/3, 0          , 1          , -sym.S(1)/3, 0, 0, 1, 0],
        [0          , -sym.S(1)/3, -sym.S(1)/3, 1          , 0, 0, 0, 1],
    ]
)
A
```

To add $1/2$ of row 1 to row 2, and $1/3$ of row 1 to row 3:

```{code-cell} python3
A[1, :] = A[0, :] / 2 + A[1, :]
A[2, :] = A[0, :] / 3 + A[2, :]
A
```

To scale row 2 by $4/3$:

```{code-cell} python3
A[1, :] = 4 * A[1, :] / 3
A
```

## Notable Research

The first formal description of the canonical form of an absorbing Markov chain
is given in [@snell_finite_1959], which served as a precursor to the influential
book published in 1960 and later reissued in [@kemeny_finite_1976].

Absorbing Markov chains have a wide range of applications. Of particular
relevance to this book is their use in discrete models of evolutionary dynamics,
as discussed in [Chapter @chp:moran_process]. A notable example of this
approach appears in [@nowak2004evolutionary].

Beyond the scope of this book, absorbing Markov chains have been applied to
many other domains, demonstrating their versatility and theoretical interest:

- The original PageRank algorithm developed by Google has been analysed through
  the lens of absorbing Markov chains
  [@bianchini_inside_2005; @langville_deeper_2004].
- In [@palmer_modelling_2018], absorbing chains are used to model deadlock in
  queuing systems, including applications in traffic flow and healthcare.
- The dynamics of battles in the board game _Risk_ are captured using absorbing
  Markov chains in [@tan_markov_1997; @osborne_markov_2003].
- Student retention processes are modelled using absorbing chains in
  [@tedeschi_improving_2023].

## Conclusion

**Absorbing Markov chains** model systems where eventual absorption is guaranteed: escape processes, games, and evolutionary dynamics.

The key concepts covered in this chapter are summarised [](#tbl:absorbing_markov_chains_summary).

```{table} Summary of absorbing Markov chains
:name: tbl:absorbing_markov_chains_summary
:align: center

| Concept                          | Description                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|
| **Markov Chain**                 | A sequence of random states with memoryless transitions                     |
| **Absorbing State**              | A state that, once entered, cannot be left                                 |
| **Transient State**              | A non-absorbing state that leads to absorption with non-zero probability   |
| **Canonical Form**               | Matrix structure separating transient and absorbing states                 |
| **Fundamental Matrix ($N$)**     | $N = (I - Q)^{-1}$ gives expected visits to transient states before absorption |
| **Absorption Probability Matrix**| $B = NR$ gives the probability of ending in each absorbing state           |
| **Gauss-Jordan Elimination**     | A method to compute matrix inverses using row operations                   |
```

```{important}
In an absorbing Markov chain, long-term behaviour is entirely determined by
the structure of the transient-to-absorbing pathways. Once the system’s
dynamics are encoded in matrix form, linear algebra allows exact computation of **expected times**, **absorption probabilities**, and **visit patterns**.
```

---

(solutions:absorbing_markov_chains)=

## Solutions

### Solution to Exercise: Transition Classification

1. **Identifying transient and absorbing states.**

   State 4 is absorbing because $P_{44} = 1$. States 1, 2, and 3 are transient:
   from each of them there is a positive probability path to state 4 (e.g.,
   state 3 reaches state 4 directly with probability 0.25, and states 1 and 2
   reach state 3 which then reaches state 4).

2. **Canonical form.** Reordering the states as transient states $\{1, 2, 3\}$
   first and absorbing state $\{4\}$ last, the matrix is already in canonical
   form:

   $$
   P =
   \begin{pmatrix}
   Q & R \\
   0 & I
   \end{pmatrix}
   $$

   where

   $$
   Q = \begin{pmatrix}
   0.5 & 0.5 & 0 \\
   0.25 & 0.5 & 0.25 \\
   0 & 0.25 & 0.5
   \end{pmatrix},
   \qquad
   R = \begin{pmatrix}
   0 \\ 0 \\ 0.25
   \end{pmatrix},
   \qquad
   I = (1).
   $$

3. **Fundamental matrix $N = (I - Q)^{-1}$.**

   $$
   I - Q = \begin{pmatrix}
   0.5 & -0.5 & 0 \\
   -0.25 & 0.5 & -0.25 \\
   0 & -0.25 & 0.5
   \end{pmatrix}
   $$

   Computing the inverse:

   $$
   N = (I - Q)^{-1} = \begin{pmatrix}
   4 & 4 & 2 \\
   2 & 6 & 3 \\
   1 & 3 & 4
   \end{pmatrix}
   $$

   Here is code to confirm this calculation:

   ```{code-cell} python3
   import numpy as np

   Q = np.array([
       [0.5,  0.5,  0.0 ],
       [0.25, 0.5,  0.25],
       [0.0,  0.25, 0.5 ],
   ])
   R = np.array([[0.0], [0.0], [0.25]])

   N = np.linalg.inv(np.eye(3) - Q)
   print("Fundamental matrix N:")
   print(np.round(N, 6))
   ```

4. **Expected number of steps until absorption.** The expected number of steps
   before absorption starting from transient state $i$ is the $i$-th entry of
   the vector $t = N \mathbf{1}$ where $\mathbf{1}$ is the all-ones vector:

   $$
\begin{align*}
   t &= N \mathbf{1} = \begin{pmatrix} 4+4+2 \\ 2+6+3 \\ 1+3+4 \end{pmatrix} \\
   &= \begin{pmatrix} 10 \\ 11 \\ 8 \end{pmatrix}
\end{align*}
   $$

   So starting from state 1 the expected absorption time is 10 steps, from
   state 2 it is 11 steps, and from state 3 it is 8 steps.

   ```{code-cell} python3
   t = N @ np.ones(3)
   print("Expected steps to absorption:", t)
   ```

---

### Solution to Exercise: Expected Visits

The maze transition matrix from [](#sec:motivating_example_escaping_a_maze) has
fundamental matrix (computed in [](#sec:example_fundamental_matrix_of_the_maze)):

$$
N = \begin{pmatrix}
26/11 & 18/11 & 18/11 & 15/11 \\
18/11 & 26/11 & 15/11 & 18/11 \\
12/11 & 10/11 & 21/11 & 12/11 \\
10/11 & 12/11 & 12/11 & 21/11
\end{pmatrix}
$$

where the transient states are rooms 1 through 4 and the absorbing states are
rooms 5 and 6.

1. **Expected visits to Room 4 starting from Room 1.** By the definition of the
   [fundamental matrix](#sec:definition_of_fundamental_matrix), $N_{ij}$ gives
   the expected number of visits to transient state $j$ before absorption,
   starting from state $i$. Room 4 corresponds to column index 4 (i.e., $j=4$)
   and Room 1 corresponds to row index 1 (i.e., $i=1$), so the answer is:

   $$
   N_{14} = \frac{15}{11} \approx 1.36
   $$

2. **Most visited ordinary room when starting from Room 3.** Looking at row 3
   of $N$:

   $$
   N_{3\cdot} = \left(\frac{12}{11},\ \frac{10}{11},\ \frac{21}{11},\ \frac{12}{11}\right)
   $$

   The largest entry is $N_{33} = 21/11 \approx 1.91$, so Room 3 itself is
   visited most often. This makes intuitive sense since the student starts there
   and must leave before being absorbed.

   ```{code-cell} python3
   import numpy as np

   Q_maze = np.array([
       [0,    1/2,  1/2,  0  ],
       [1/2,  0,    0,    1/2],
       [1/3,  0,    0,    1/3],
       [0,    1/3,  1/3,  0  ],
   ])
   R_maze = np.array([
       [0,   0  ],
       [0,   0  ],
       [1/3, 0  ],
       [0,   1/3],
   ])

   N_maze = np.linalg.inv(np.eye(4) - Q_maze)
   print("Fundamental matrix N (maze):")
   from fractions import Fraction
   import sympy as sym
   N_sym = sym.Matrix(sym.eye(4) - sym.Matrix([
       [0,    sym.Rational(1,2),  sym.Rational(1,2),  0               ],
       [sym.Rational(1,2), 0,     0,                   sym.Rational(1,2)],
       [sym.Rational(1,3), 0,     0,                   sym.Rational(1,3)],
       [0,    sym.Rational(1,3),  sym.Rational(1,3),  0               ],
   ])).inv()
   N_sym
   ```

   ```{code-cell} python3
   print("Expected visits to Room 4 starting from Room 1:", sym.Rational(15, 11))
   print("Row 3 of N:", [N_sym[2, j] for j in range(4)])
   print("Most visited room starting from Room 3: Room", 1 + max(range(4), key=lambda j: N_sym[2, j]))
   ```

---

### Solution to Exercise: Symbolic Fundamental Matrix

Let

$$
Q = \begin{pmatrix} 0 & a \\ b & 0 \end{pmatrix}, \qquad 0 < a, b < 1.
$$

1. **Fundamental matrix $N = (I - Q)^{-1}$.**

   $$
   I - Q = \begin{pmatrix} 1 & -a \\ -b & 1 \end{pmatrix}
   $$

   The determinant of $I - Q$ is $1 - ab$. Since $0 < a, b < 1$ we have
   $0 < ab < 1$ so $1 - ab > 0$ and the matrix is invertible. Therefore:

   $$
   N = (I - Q)^{-1} = \frac{1}{1 - ab}
   \begin{pmatrix} 1 & a \\ b & 1 \end{pmatrix}
   $$

   In component form:

   $$
   N_{11} = N_{22} = \frac{1}{1 - ab}, \qquad N_{12} = \frac{a}{1 - ab}, \qquad N_{21} = \frac{b}{1 - ab}.
   $$

2. **Expected total steps before absorption.** The expected number of total
   steps before absorption from state $i$ is $(N \mathbf{1})_i$:

   $$
   N \mathbf{1} = \frac{1}{1-ab}
   \begin{pmatrix} 1 + a \\ 1 + b \end{pmatrix}
   $$

   So starting from state 1, the expected total steps is $\dfrac{1+a}{1-ab}$,
   and starting from state 2, it is $\dfrac{1+b}{1-ab}$.

   ```{code-cell} python3
   import sympy as sym

   a, b = sym.symbols("a b", positive=True)
   Q_sym = sym.Matrix([[0, a], [b, 0]])
   I_sym = sym.eye(2)
   N_sym2 = (I_sym - Q_sym).inv()
   sym.simplify(N_sym2)
   ```

   ```{code-cell} python3
   t_sym = N_sym2 * sym.Matrix([1, 1])
   sym.simplify(t_sym)
   ```

---

### Solution to Exercise: Absorption Probabilities

Given:

$$
Q = \begin{pmatrix} 0.2 & 0.3 \\ 0.4 & 0.1 \end{pmatrix},
\qquad
R = \begin{pmatrix} 0.5 & 0 \\ 0 & 0.5 \end{pmatrix}.
$$

1. **Fundamental matrix $N$.**

   $$
   I - Q = \begin{pmatrix} 0.8 & -0.3 \\ -0.4 & 0.9 \end{pmatrix}
   $$

   The determinant is $0.8 \times 0.9 - (-0.3)(-0.4) = 0.72 - 0.12 = 0.60$.

   $$
\begin{align*}
   N &= (I - Q)^{-1} = \frac{1}{0.6}\begin{pmatrix} 0.9 & 0.3 \\ 0.4 & 0.8 \end{pmatrix} \\
   &= \begin{pmatrix} 1.5 & 0.5 \\ 2/3 & 4/3 \end{pmatrix}
\end{align*}
   $$

2. **Absorption probability matrix $B = NR$.**

   $$
\begin{align*}
   B &= NR = \begin{pmatrix} 1.5 & 0.5 \\ 2/3 & 4/3 \end{pmatrix}
   \begin{pmatrix} 0.5 & 0 \\ 0 & 0.5 \end{pmatrix} \\
   &= \begin{pmatrix} 0.75 & 0.25 \\ 1/3 & 2/3 \end{pmatrix}
\end{align*}
   $$

3. **Interpretation of $B_{12}$.** The entry $B_{12} = 0.25$ is the probability
   that the process, starting from transient state 1, is eventually absorbed
   into absorbing state 2. In other words, starting from state 1, there is a
   25% chance of being absorbed into state 2 and a 75% chance of being absorbed
   into state 1.

   ```{code-cell} python3
   import numpy as np

   Q_abs = np.array([[0.2, 0.3], [0.4, 0.1]])
   R_abs = np.array([[0.5, 0.0], [0.0, 0.5]])

   N_abs = np.linalg.inv(np.eye(2) - Q_abs)
   print("Fundamental matrix N:")
   print(N_abs)

   B = N_abs @ R_abs
   print("\nAbsorption probability matrix B = NR:")
   print(B)
   print("\nB[0, 1] =", B[0, 1], "(probability of absorption into state 2 from state 1)")
   ```
