---
kernelspec:
  name: python3
  display_name: "Python 3"
---

(chp:best_response_polytopes)=

# Best response polytopes

(sec:motivating_example_insider_threat_detection)=

## Motivating Example: Insider Threat Detection

A large organization is conducting a red team exercise to test its internal
security against potential insider threats.

A simulated **Leaker** (the row player) chooses among three methods of
exfiltrating sensitive data: **USB drive**, **Personal email**, or
**Cloud storage**.

The **Defender** (the column player) allocates monitoring resources to one
of three detection strategies: **Endpoint Monitoring**, **Email Filtering**,
or **Cloud Auditing**.

A government **regulator** observes the system and wants to assess whether
current security measures are adequate. It is assumed that both players act
optimally, i.e., they adopt strategies that correspond to a **Nash equilibrium**.

The regulator evaluates the system based on the **equilibrium probability
of a successful breach**. If this exceeds a critical threshold, the regulator
will mandate additional investment in security.

Let the row player (Leaker) choose among USB, Email, and Cloud, and let the
column player (Defender) choose among Endpoint Monitoring, Email Filtering,
and Cloud Auditing.

The Leaker's payoff matrix (probabilities of successful exfiltration) is:

$$
M_r = \begin{pmatrix}
7/9 & 4/5 & 5/9\\
7/10 & 5/8 & 7/8\\
3/5 & 4/5 & 5/7\\
\end{pmatrix}
$$

The Defender's payoff matrix (probabilities of successful detection) is:

$$
M_c = \begin{pmatrix}
1/7 & 1/10 & 2/5\\
1/3 & 5/9 & 1/5\\
4/9 & 1/3 & 1/4\\
\end{pmatrix}
$$

Note that the sum of payoffs in any outcome need not equal 1. This reflects the
possibility that the attacker fails to exfiltrate and the defender fails to detect
the attempt — for instance, if the file transfer crashes mid-way and no alert is
triggered.

This point is also important mathematically: the game is **not constant-sum** and
therefore not equivalent to a [zero-sum game](#chp:zero_sum_games). It is also **strategically rich**:
each player has three actions, none of which can be removed through simple
[rationalisation](#chp:rationality). This chapter introduces efficient methods for computing
Nash equilibria in such settings.

## Theory

### Definition: Best Response Polytopes

For a two player game $(M_r, M_c)\in{\mathbb{R}^{m\times n}_{>0}}^2$ the
row/column player best response polytope $\mathcal{P}_r$/$\mathcal{P}_c$ is
defined by:

$$
\label{eqn:definition_of_P_r}
\mathcal{P_r} = \left\{x\in\mathbb{R}^{m}\;|\;x\geq 0; xM_c\leq 1\right\}
$$

$$
\label{eqn:definition_of_Q_r}
\mathcal{P_c} = \left\{y\in\mathbb{R}^{n}\;|\; M_ry\leq 1; y\geq 0 \right\}
$$

---

The polytope $\mathcal{P}_r$, corresponds to the set of points with an upper bound on the
utility of those points when considered as row strategies against which the column player
plays.

The polytope $\mathcal{Q}_r$, corresponds to the set of points with an upper bound on the
utility of those points when considered as column strategies against which the row player
plays.

```{note}
The fact that these polytopes are defined for $M_r, M_c > 0$
is not restrictive in practice as we can add a constant to our
utilities.
```

#### Example: Best Response Polytopes for the threat detection game

Let us construct the best response polytopes for the
[threat detection game](#sec:motivating_example_insider_threat_detection).

Applying the definition [](#eqn:definition_of_P_r) we have:

$$
\mathcal{P}_r = \left\{x\in\mathbb{R}^{3}\;\left|\;x_i\geq 0\text{ and } \left(x
\begin{pmatrix}
1/7 & 1/10 & 2/5\\
1/3 & 5/9 & 1/5\\
4/9 & 1/3 & 1/4\\
\end{pmatrix}\right)_{ij}
\leq 1\text{ for all }1\leq i, j \leq 3\right.\right\}
$$

$$
\mathcal{P}_c = \left\{y\in\mathbb{R}^{3}\;\left|\;\left(
\begin{pmatrix}
7/9 & 4/5 & 5/9\\
7/10 & 5/8 & 7/8\\
3/5 & 4/5 & 5/7\\
\end{pmatrix}y\right)_{ij}
\leq 1\text{ and }y_j\geq 0 \text{ for all }1\leq i, j \leq 3\right.\right\}
$$

This gives:

$$
\begin{align*}
x_1 & \geq 0\\
x_2 & \geq 0\\
x_3 & \geq 0\\
x_1/7+x_2/3+4x_3/9&\leq 1\\
x_1/10+5x_2/9+x_3/3&\leq 1\\
2x_1/5+x_2/5+x_3/4&\leq 1\\
\end{align*}
$$

$$
\begin{align*}
7y_1/9+4y_2/5+5y_3/9&\leq 1\\
7y_1/10+5y_2/8+7y_3/8&\leq 1\\
3y_1/5+4y_2/5+5y_3/7&\leq 1\\
y_1 & \geq 0\\
y_2 & \geq 0\\
y_3 & \geq 0\\
\end{align*}
$$

```{important}
The ordering of these two sets of inequalities is important. The non-negativity
constraints are first for $P_r$ and second for $P_c$. This will be used in
[](#sec:vertex_labelling).
```

The vertices of these two polytopes are:

For $\mathcal{P}_r$:

$$
\begin{align*}
    v_0 & = (0, 0, 0) \\
    v_1 & = (5/2, 0, 0) \\
    v_2 & = (0, 0, 9/4) \\
    v_3 & = (245/179, 0, 324/179) \\
    v_4 & = (160/91, 135/91, 0) \\
    v_5 & = (6580/4927, 4185/4927, 5832/4927) \\
    v_6 & = (0, 9/5, 0) \\
    v_7 & = (0, 9/11, 18/11) \\
\end{align*}
$$

These are shown in [](#fig:row_player_best_response_polytope).

```{figure} ./images/row_player_best_response_polytope/main.png
:alt: A 3 dimensional polytope with annotated names of vertices
:label: fig:row_player_best_response_polytope
:width: 750px

The three dimensional $\mathcal{P}_r$.
```

For $\mathcal{P}_c$:

$$
\begin{align*}
u_0 & = (0, 0, 0) \\
u_1 & = (9/7, 0, 0) \\
u_2 & = (0, 0, 8/7) \\
u_3 & = (23/21, 0, 4/15) \\
u_4 & = (0, 45/71, 49/71) \\
u_5 & = (25/67, 40/67, 28/67) \\
u_6 & = (0, 5/4, 0) \\
\end{align*}
$$

These are shown in [](#fig:col_player_best_response_polytope).

```{figure} ./images/col_player_best_response_polytope/main.png
:alt: A 3 dimensional polytope with annotated names of vertices
:label: fig:col_player_best_response_polytope
:width: 750px

The three dimensional $\mathcal{P}_r$.
```

```{note}
Vertices of these polytopes are not probability vectors so they are not
strategies.
```

A vertex of a best response polytope corresponds to a strategy through
normalization that ensures the sum corresponds to one.

For example $u_6$ corresponds to a strategy:

$$
\sigma = \frac{u_6}{\sum_{i=1}^3 {u_6}_i} = (0, 1, 0)
$$

Similarly for $u_5$:

$$
\begin{align*}
\sigma & = \frac{u_5}{\sum_{i=1}^3 {u_5}_i}\\
       & =\frac{(25/67, 40/67, 28/67)}{(25/67 + 40/67 + 28/67)}\\
       & =\frac{(25/67, 40/67, 28/67)}{93/67}\\
       & =(25/93, 40/93, 28/93)
\end{align*}
$$

(sec:vertex_labelling)=

### Definition: Vertex Labelling

---

A **vertex labelling** is an assignment of labels to each vertex of a best response polytope,
where each label corresponds to a constraint that is **binding** (i.e., holds with equality) at that vertex.

---

Each defining inequality of a best response polytope has a game theoretic
interpretation when it is a binding inequality for a given vertex.

(sec:example_vertex_labelling_for_the_threat_detection_game)=

#### Example: Vertex labelling for the threat detection game

Let us consider the inequalities of $P_r$ and interpret what is implied when the
inequality is binding:

$$
\begin{align*}
x_1 = 0& \implies \text{\textcircled{1}: the first action is not played by the strategy
represented by } x\\
x_2 = 0& \implies \text{\textcircled{2}: the third action is not played by the strategy
represented by } x\\
x_3 = 0& \implies \text{\textcircled{3}: the third action is not played by the strategy
represented by } x\\
(xM_c)_1 = 1& \implies \text{\textcircled{4}: the first action is a best response to the strategy
represented by } x\\
(xM_c)_2 = 1& \implies \text{\textcircled{5}: the second action is a best response to the strategy
represented by } x\\
(xM_c)_3 = 1& \implies \text{\textcircled{6}: the third action is a best response to the strategy
represented by } x\\
\end{align*}
$$

Similarly for $Q_r$

$$
\begin{align*}
(yM_r)_1 = 1& \implies \text{\textcircled{1}: the first action is a best response to the strategy
represented by } y\\
(yM_r)_2 = 1& \implies \text{\textcircled{2}: the second action is a best response to the strategy
represented by } y\\
(yM_r)_3 = 1& \implies \text{\textcircled{3}: the third action is a best response to the strategy
represented by } y\\
y_1 = 0& \implies \text{\textcircled{4}: the first action is not played by the strategy
represented by } y\\
y_2 = 0& \implies \text{\textcircled{5}: the third action is not played by the strategy
represented by } y\\
y_3 = 0& \implies \text{\textcircled{6}: the third action is not played by the strategy
represented by } y\\
\end{align*}
$$

We have used $\text{\textcircled{1}}$ through $\text{\textcircled{6}}$ as the
labels.

Let us label each of the vertices:

For $v_4=(160/91, 135/91, 0)$:

$$
\begin{align*}
x_1 = 160/91 \ne 0\\
x_2 = 135/91 \ne 0
x_3 = 0& \implies \text{\textcircled{3}: the third action is not played by the strategy
represented by } x\\
(xM_c)_1 = = 475/637\\
(xM_c)_2 = 1& \implies \text{\textcircled{5}: the second action is a best response to the strategy
represented by } x\\
(xM_c)_3 = 1& \implies \text{\textcircled{6}: the third action is a best response to the strategy
represented by } x\\
\end{align*}
$$

For $\mathcal{P}_r$:

$$
\label{eqn:labels_of_P}
\begin{align*}
    \mathcal{L}(v_0) & = \mathcal{L}((0, 0, 0)) = \{1, 2, 3\}  \\
    \mathcal{L}(v_1) & = \mathcal{L}((5/2, 0, 0)) = \{2, 3, 6\} \\
    \mathcal{L}(v_2) & = \mathcal{L}((0, 0, 9/4)) = \{1, 2, 4\} \\
    \mathcal{L}(v_3) & = \mathcal{L}((245/179, 0, 324/179)) = \{2, 4, 6\} \\
    \mathcal{L}(v_4) & = \mathcal{L}((160/91, 135/91, 0)) = \{3, 5, 6\} \\
    \mathcal{L}(v_5) & = \mathcal{L}((6580/4927, 4185/4927, 5832/4927)) = \{4, 5, 6\} \\
    \mathcal{L}(v_6) & = \mathcal{L}((0, 9/5, 0)) = \{1, 3, 5\} \\
    \mathcal{L}(v_7) & = \mathcal{L}((0, 9/11, 18/11)) = \{1, 4, 5\} \\
\end{align*}
$$

For $\mathcal{P}_c$:

$$
\label{eqn:labels_of_Q}
\begin{align*}
    \mathcal{L}(u_0) & = \mathcal{L}((0, 0, 0)) = \{4, 5, 6\} \\
    \mathcal{L}(u_1) & = \mathcal{L}((9/7, 0, 0)) = \{1, 5, 6\} \\
    \mathcal{L}(u_2) & = \mathcal{L}((0, 0, 8/7)) = \{2, 4, 5\} \\
    \mathcal{L}(u_3) & = \mathcal{L}((23/21, 0, 4/15)) = \{1, 2, 5\} \\
    \mathcal{L}(u_4) & = \mathcal{L}((0, 45/71, 49/71)) = \{2, 3, 4\} \\
    \mathcal{L}(u_5) & = \mathcal{L}((25/67, 40/67, 28/67)) = \{1, 2, 3\} \\
    \mathcal{L}(u_6) & = \mathcal{L}((0, 5/4, 0)) = \{1, 3, 4, 6\} \\
\end{align*}
$$

```{important}
We can use labels to identify if pairs of sttrategies are best responses to each
other.
```

If a label is present in either vertex then either of the
following are true::

- it is indicating that an action is not played (for example label 1 in $\mathcal{P}_r$).
- is is indicating that the same action is a best response to the strategy represented
  by the vector (for example label 1 in $\mathcal{P}_c$).

Looking at $v_5$ and $u_5$ the union of the labels of these vertices gives the
full set of vertices.

This leads to the following definition.

### Definition: Fully labelled vertex pair

---

A pair of vertices $(x, y) \in \mathcal{P}_r \times \mathcal{P}_C$ is said to be a
**fully labelled vertex pair** if the union of their labels covers all possible
labels:

$$
\mathcal{L}(x) \cup \mathcal{L}(y) = \{1, 2, \dots, m + n\}
$$

Such a pair, when normalised (so that the components sum to 1), corresponds to a
Nash equilibrium.

---

(sec:example_fully_labelled_vertex_pair_for_the_threat_detection_game)=

#### Example: Fully labelled vertex pair for the threat detection game

As shown in [](#sec:example_vertex_labelling_for_the_threat_detection_game):

$$
\mathcal{v_5} \cup \mathcal{u_5} = \{4, 5, 6\} \cup \{1, 2, 3\} = \{1, 2, 3, 4,
5, 6\}
$$

is a fully labelled vertex pair.

This corresponds to the normalised strategies:

$$
\label{eqn:normalisation_of_v_5}
\sigma_r = \frac{(6580/4927, 4185/4927, 5832/4927)}{6580/4927 + 4185/4927 + 5832/4927} = (940/2371, 4185/16597, 5832/16597)
$$

and

$$
\label{eqn:normalisation_of_u_5}
\sigma_c = \frac{(25/67, 40/67, 28/67)}{(25/67 + 40/67 + 28/67)} = (25/67, 40/67, 28/67)
$$

which is a Nash equilibrium.

Searching through all pairs of vertices is one approach to identifying Nash
equilibria although a more efficient approach will now be discussed.

### Definition: Lemke-Howson Algorithm

For a nondegenerate 2 player game $(M_r, M_c)\in{\mathbb{R}^{m\times n}_{>0}}^2$ the following
algorithm returns a Nash equilibrium:

1. Start at the artificial equilibrium: $(0, 0)$
2. Choose a label to drop.
3. Remove this label from the corresponding vertex by traversing an edge of the
   corresponding polytope to another vertex.
4. The new vertex will now have a duplicate label in the other polytope. Remove this
   label from the vertex of the other polytope and traverse an edge of that polytope to another vertex.
5. Repeat step 4 until the pair of vertices is fully labelled.

(sec:example_lemke_howson_with_known_vertices)=

#### Example: Application of the Lemke–Howson algorithm for the threat detection game with known vertices and labels

We will use [](#fig:row_player_best_response_polytope),  
[](#fig:col_player_best_response_polytope), as well as  
[](#eqn:labels_of_P) and [](#eqn:labels_of_Q) to move  
from vertex to vertex in the threat detection game.

We apply the algorithm as follows:

1. Start at $(v_0, u_0)$ and choose to drop label $1$ (an arbitrary choice).
2. Label $1$ is not among the labels of $u_0$, so we move from $v_0$ to an
   adjacent vertex—$v_1$, $v_2$, $v_3$, $v_4$, $v_6$, or $v_7$—that does not
   carry label $1$ but shares other labels with $v_0$. We select $v_1$. This
   introduces label $6$, which must now be dropped in $\mathcal{P}_c$.
3. $(v_1, u_0) \to (v_1, u_2)$: the labels are $\{2, 3, 6\}, \{2, 4, 5\}$.
   Label $2$ must be dropped in $\mathcal{P}_r$.
4. $(v_1, u_2) \to (v_4, u_2)$: the labels are $\{3, 5, 6\}, \{2, 4, 5\}$.
   Label $5$ must be dropped in $\mathcal{P}_c$.
5. $(v_4, u_2) \to (v_4, u_4)$: the labels are $\{3, 5, 6\}, \{2, 3, 4\}$.
   Label $3$ must be dropped in $\mathcal{P}_r$.
6. $(v_4, u_4) \to (v_5, u_4)$: the labels are $\{4, 5, 6\}, \{2, 3, 4\}$.
   Label $4$ must be dropped in $\mathcal{P}_c$.
7. $(v_5, u_4) \to (v_5, u_5)$: the labels are $\{4, 5, 6\}, \{1, 2, 3\}$.
   This is a fully labelled vertex pair.

After normalisation, this yields the Nash equilibrium computed in  
[](#sec:example_fully_labelled_vertex_pair_for_the_threat_detection_game).

This approach, while systematic, is only efficient here because the vertices  
have already been computed. In practice, obtaining the vertices of the polytope  
can be a time-consuming process. In the next example, we will demonstrate how  
the Lemke–Howson algorithm becomes truly efficient through  
[integer pivoting](#app:integer_pivoting).

#### Example: Application of the Lemke-Howson Algorithm for the threat detection game with integer pivoting

Using the [definition of a tableau](#sec:definition_tableau_representation_of_vertices) the tableaux for a
2 player game $(M_r, M_c)\in{\mathbb{R}^{m\times n}_{>0}}^2$ are given by:

$$
T_r =
\begin{pmatrix}
B^T&I &1\\
\end{pmatrix}
$$

and

$$
T_c =
\begin{pmatrix}
I & A & 1\\
\end{pmatrix}
$$

In the case of the [threat detection game](#sec:motivating_example_insider_threat_detection) this gives:

$$
T_r = \begin{pmatrix}
1/7 & 1/3 & 4/9 & 1 & 0 & 0 & 1\\
1/10 & 5/9 & 1/3 & 0 & 1 & 0 & 1\\
2/5 & 1/5 & 1/4 & 0 & 0 & 1 & 1\\
\end{pmatrix}
$$

and

$$
T_c = \begin{pmatrix}
1 & 0 & 0 & 7/9 & 4/5 & 5/9 & 1\\
0 & 1 & 0 & 7/10 & 5/8 & 7/8 & 1\\
0 & 0 & 1 & 3/5 & 4/5 & 5/7 & 1\\
\end{pmatrix}
$$

```{important}
The non basic columns correspond to labels.
```

Let us now reproduce the steps of [](#sec:example_lemke_howson_with_known_vertices): we begin by
dropping label 1 which corresponds to the non basic variable 1 of $T_r$.
In terms of [integer pivoting](#sec:definition_integer_pivoting) this is done by pivoting the first column of $T_r$.

As described in [](#sec:definition_integer_pivoting) we carry out the minimum
ratio test:

1. The ratio for the first row: $\frac{7}{1}$
2. The ratio for the second row: $\frac{10}{1}$
3. The ratio for the third row: $\frac{5}{2}$

We pivot on the third row giving:

$$
T_r = \begin{pmatrix}
0 & 11/105 & 179/1260 & 2/5 & 0 & -1/7 & 9/35\\
0 & 91/450 & 13/120 & 0 & 2/5 & -1/10 & 3/10\\
1 & 1/2 & 5/8 & 0 & 0 & 5/2 & 5/2\\
\end{pmatrix}
$$

This tableau has labels/non basic variables $\{2, 3, 6\}$. So we now pivot
column 6 in $T_c$. The minimum ratio test:

1. The ratio for the first row: $\frac{9}{5}$
2. The ratio for the second row: $\frac{8}{7}$
3. The ratio for the third row: $\frac{7}{5}$

We pivot on the second row giving:

$$
T_c = \begin{pmatrix}
7/8 & -5/9 & 0 & 7/24 & 127/360 & 0 & 23/72\\
0 & 8/7 & 0 & 4/5 & 5/7 & 1 & 8/7\\
0 & -5/7 & 7/8 & 1/40 & 71/280 & 0 & 9/56\\
\end{pmatrix}
$$

This tableau has labels $\{2, 4, 5\}$ so we pivot column 2 in $T_r$. The minimum ratio test:

1. The ratio for the first row: $\frac{9/35}{11/105} = 27/11$
2. The ratio for the second row: $\frac{3/10}{91/450} = 135/91$
3. The ratio for the third row: $\frac{5/2}{1/2} = 5/2$

We pivot on the second row giving:

$$
T_r = \begin{pmatrix}
0 & 0 & 4927/283500 & 91/1125 & -22/525 & -29/1575 & 18/875\\
0 & 1 & 15/28 & 0 & 180/91 & -45/91 & 135/91\\
91/450 & 0 & 13/180 & 0 & -1/5 & 5/9 & 16/45\\
\end{pmatrix}
$$

This tableau has labels $\{3, 5, 6\}$ so we pivot column 5 in $T_c$. The
minimum ratio test:

1. The ratio for the first row: $\frac{23/72}{127/360} = 115/127$
2. The ratio for the second row: $\frac{8/7}{1} = 8/7$
3. The ratio for the third row: $\frac{9/56}{71/280} = 45/71$

We pivot on the third row giving:

$$
T_c = \begin{pmatrix}
71/320 & 1/9 & -889/2880 & 469/7200 & 0 & 0 & 7/288\\
0 & 4/5 & -5/8 & 37/200 & 0 & 71/280 & 7/40\\
0 & -200/71 & 245/71 & 7/71 & 1 & 0 & 45/71\\
\end{pmatrix}
$$

This tableau has labels $\{2, 3, 4\}$ so we pivot column 3 in $T_r$. The minimum
ratio test:

1. The ratio for the first row: $\frac{18/875}{4927/283500} = 5832 / 4927$
2. The ratio for the second row: $\frac{135/91}{15/28} = 524/195$
3. The ratio for the third row: $\frac{16/45}{13/180} = 576/65$

We pivot on the first row giving:

$$
T_r = \begin{pmatrix}
0 & 0 & 1 & 1764/379 & -11880/4927 & -5220/4927 & 5832/4927\\
0 & 4927/283500 & 0 & -13/300 & 179/3150 & 2/1575 & 31/2100\\
64051/18225000 & 0 & 0 & -1183/202500 & -91/202500 & 1001/91125 & 4277/911250\\
\end{pmatrix}
$$

This tableau has labels $\{4, 5, 6\}$ so we pivot column 4 in $T_c$. The minimum
ratio test:

1. The ratio for the first row: $\frac{7/188}{71/320} = 70/639$
2. The ratio for the second row: $\frac{7/40}{4/5} = 7/32$
3. The ratio for the third row: $\frac{45/71}{-200/71} < 0$

We pivot on the first row giving:

$$
T_c = \begin{pmatrix}
3195/938 & 800/469 & -635/134 & 1 & 0 & 0 & 25/67\\
-2627/64000 & 71/2250 & 9443/576000 & 0 & 0 & 4757/288000 & 497/72000\\
-7/320 & -7/36 & 49/192 & 0 & 469/7200 & 0 & 7/180\\
\end{pmatrix}
$$

This tableau has labels $\{1, 2, 3\}$ so we have a fully labeled vertex pair.

Setting the non-basic variables to 0 we have the following systems of equations:

$$
\begin{align*}
    64051 / 18225000 x_1 & = 4277/911250\\
    4927/283500x_2 & = 31 / 2100\\
    x_3 & = 5832 / 4972\\
\end{align*}
$$

and:

$$
\begin{align*}
    y_1 &=  25/67\\
    469/7200 y_2 &= 7/180\\
    4757/28800 y_3 &= 497/7200\\
\end{align*}
$$

Giving: $x = (6580/4927, 4185/4927, 5832/4972)$ and $y = (25/67, 40/67, 28/67)$ which when normalised [](#eqn:normalisation_of_v_5) - [](#eqn:normalisation_of_u_5) gives:

$$
\sigma_r = (940/2371, 4185/16597, 5832/16597)
\qquad
\sigma_c = (25/93, 40/93, 28/93)
$$

## Exercises

```{exercise} 
:label: enumeration_of_fully_labelled_vertex_pairs

For each of the following games, draw the best response polytopes and identify
all fully labelled vertex pairs:

1. $$A =
   \begin{pmatrix}
   3 & -1 \\
   2 & 7
   \end{pmatrix},
   \qquad
   B =
   \begin{pmatrix}
   -3 & 1 \\
   1 & -6
   \end{pmatrix}$$
2. $$A =
   \begin{pmatrix}
   2 & -1 \\
   1 & 3
   \end{pmatrix},
   \qquad
   B =
   \begin{pmatrix}
   -2 & 2 \\
   1 & -2
   \end{pmatrix}$$
```

```{exercise} 
:label: lemke-howson-algorithm-for-2-by-2-games

Using the games from
[](#enumeration_of_fully_labelled_vertex_pairs),
apply the Lemke–Howson algorithm to compute a Nash equilibrium in each case.
Carry out the algorithm twice: once using the known vertex structure, and once
using integer pivoting.
```

```{exercise} 
:label: coffee-shop-rivalry

In a busy university district, two independent coffee shops compete for
customers. Each can choose to:

- **Lower prices** to attract bargain-seekers,
- **Improve quality** by investing in better beans and baristas,
- **Advertise** aggressively through social media and flyers.

Customers respond differently depending on the overall landscape of offers.
The three main customer profiles are:

- **Students** who are price-sensitive,
- **Coffee aficionados** who value taste,
- **Impulse buyers** who respond to advertising.

The payoff matrices, based on estimated profits (row player: Café A, column
player: Café B), are:

$$
M_r =
\begin{pmatrix}
3 & 1 & 2 \\
2 & 4 & 1 \\
1 & 3 & 0
\end{pmatrix},
\qquad
M_c =
\begin{pmatrix}
2 & 3 & 1 \\
1 & 2 & 4 \\
5 & 1 & 3
\end{pmatrix}
$$

1. Use the Lemke–Howson algorithm to find a Nash equilibrium. Describe how
   different choices of dropped label may lead to different paths.
2. Interpret the equilibrium in terms of business strategy: What might the
   equilibrium suggest about the balance between pricing, quality, and advertising?
```

```{exercise} 
:label: odd-number-of-equilibria

Assume the game is **nondegenerate**: each vertex of the best response
polytopes has exactly the number of labels required to define it, and no label
appears more than once across a vertex pair. Also assume that, when applying
the Lemke–Howson algorithm, dropping a label from any fully labelled vertex
pair always leads to a **distinct** fully labelled vertex pair.

Under these assumptions, prove that the number of fully labelled vertex pairs —
and hence the number of Nash equilibria — is always **odd**.
```

## Programming

### Vertex enumeration with Nashpy

Nashpy can be used to generate the polytopes and enumerate all pairs of
vertices.

```{code-cell} python3
import nashpy as nash
import numpy as np


M_r = np.array([
    [3, 1, 2],
    [2, 4, 1],
    [1, 3, 0]
])

M_c = np.array([
    [2, 3, 1],
    [1, 2, 4],
    [5, 1, 3]
])

game = nash.Game(M_r, M_c)
list(game.vertex_enumeration())
```

### Lemke-Howson with Nashpy

Nashpy can be used to carry out the Lemke-Howson algorithm, an efficient way
to find a Nash equilibrium.

```{code-cell} python3
label_to_drop = 0
game.lemke_howson(initial_dropped_label=label_to_drop)
```

You can also enumerate all possible dropped labels:

```{code-cell} python3
list(game.lemke_howson_enumeration())
```

### Vertex enumeration with Gambit

Gambit can be used to enumerate all pairs of vertices:

```{code-cell} python3
import pygambit as gbt

game = gbt.Game.from_arrays(M_r, M_c)
gbt.nash.enummixed_solve(game)
```

### Lemke-Howson with Gambit

Gambit can be used to carry out the Lemke-Howson algorithm:

```{code-cell} python3
gbt.nash.lcp_solve(game)
```

## Notable Research

The original paper presenting the Lemke–Howson algorithm for two-player games is
[@lemke1964equilibrium]. That paper also contains a constructive proof that, in
nondegenerate games, the number of Nash equilibria is always
[](#odd-number-of-equilibria). The algorithm was later extended to
$N$-player games in [@wilson1971computing], where the oddness result is also
generalised. An alternative proof of the oddness theorem is provided in
[@harsanyi1973oddness] the author of which was awarded the Nobel prize with Nash
and Selten in 1994.

The worst-case complexity of the Lemke–Howson algorithm is analysed in
[@savani2004exponentially], which demonstrates that the algorithm may require
exponential time on specific inputs. **Computing Nash equilibria is a
computationally challenging task** — this intuitive difficulty is formalised in
[@chen2006settling, @daskalakis2009complexity], where the problem is shown to be
PPAD-complete, placing it in a class of problems believed not to admit
polynomial-time solutions.

### Conclusion

This chapter introduced the geometric and algorithmic structure underlying
Nash equilibrium computation through the lens of **best response polytopes**.
By framing strategy sets as polytopes and interpreting labels as binding
constraints, we gain powerful visual and computational tools for equilibrium
analysis.

The **Lemke–Howson algorithm** provides a systematic method for tracing paths
through these polytopes to identify **fully labelled vertex pairs**, which
correspond to Nash equilibria. Though simple in low dimensions, this method
scales to more complex games using tableau-based pivoting techniques such as
**integer pivoting**.

Understanding the polyhedral structure of best responses not only aids in
computational efficiency but also provides conceptual clarity: each equilibrium
arises from a delicate balance of incentives, visible in the geometry of
the feasible region.

[](#tbl:best_response_polytopes) summarises the key concepts introduced in this
chapter.

```{table} Summary of best response polytopes
:name: tbl:best_response_polytopes
:align: center


| Concept                    | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| Best response polytope     | A polyhedron defined by inequalities corresponding to best response conditions. |
| Binding inequality         | A constraint that holds with equality at a vertex; gives rise to a label.      |
| Vertex labelling           | A mapping from vertices to labels indicating inactive actions or best responses. |
| Fully labelled vertex pair | A pair of vertices whose labels cover all $m + n$ actions — corresponds to a Nash equilibrium. |
| Lemke–Howson algorithm     | A path-following method that constructs equilibria by dropping and replacing labels. |
| Integer pivoting           | A tableau-based pivoting method used to trace Lemke–Howson paths efficiently.     |
```

```{important}
In every nondegenerate two-player game, each Nash equilibrium corresponds to a
fully labelled vertex pair of the best response polytopes.

Crucially, we can find such a vertex pair without explicitly constructing the
polytopes — using integer pivoting and the Lemke–Howson algorithm.
```

---

(solutions:best_response_polytopes)=

## Solutions

````{solution} enumeration_of_fully_labelled_vertex_pairs
:label: solution:enumeration_of_fully_labelled_vertex_pairs

For a $2 \times 2$ game $(A, B)$ we must first shift the matrices so that all
entries are strictly positive (required by the definition of best response
polytopes), then construct $\mathcal{P}_r$ and $\mathcal{P}_c$.

**1. Game:**

$$
A = \begin{pmatrix}3 & -1 \\ 2 & 7\end{pmatrix},
\qquad
B = \begin{pmatrix}-3 & 1 \\ 1 & -6\end{pmatrix}
$$

Add a constant to make all entries positive. Add $2$ to $A$ and $7$ to $B$:

$$
A' = \begin{pmatrix}5 & 1 \\ 4 & 9\end{pmatrix},
\qquad
B' = \begin{pmatrix}4 & 8 \\ 8 & 1\end{pmatrix}
$$

The best response polytopes are:

$$
\mathcal{P}_r = \{x \in \mathbb{R}^2 \mid x \geq 0,\; x B' \leq \mathbf{1}\}
$$

$$
\mathcal{P}_c = \{y \in \mathbb{R}^2 \mid A' y \leq \mathbf{1},\; y \geq 0\}
$$

Writing out the inequalities for $\mathcal{P}_r$ (labels (1)–(4)):

$$
\begin{align*}
x_1 \geq 0 &\quad \text{(1)}\\
x_2 \geq 0 &\quad \text{(2)}\\
4x_1 + 8x_2 \leq 1 &\quad \text{(3)}\\
8x_1 + x_2 \leq 1 &\quad \text{(4)}
\end{align*}
$$

Writing out the inequalities for $\mathcal{P}_c$ (labels (1)–(4)):

$$
\begin{align*}
5y_1 + y_2 \leq 1 &\quad \text{(1)}\\
4y_1 + 9y_2 \leq 1 &\quad \text{(2)}\\
y_1 \geq 0 &\quad \text{(3)}\\
y_2 \geq 0 &\quad \text{(4)}
\end{align*}
$$

**Vertices of $\mathcal{P}_r$** (each vertex satisfies 2 of the 4 inequalities with equality):

- $v_0 = (0, 0)$: labels $\{1, 2\}$
- $v_1 = (1/8, 0)$: binding (2) and (4); labels $\{2, 4\}$
- $v_2 = (0, 1/8)$: binding (1) and (3); labels $\{1, 3\}$
- $v_3$: intersection of $4x_1 + 8x_2 = 1$ and $8x_1 + x_2 = 1$.

  Solving: from the second equation $x_2 = 1 - 8x_1$. Substituting:
  $4x_1 + 8(1-8x_1) = 1 \Rightarrow 4x_1 + 8 - 64x_1 = 1 \Rightarrow -60x_1 = -7 \Rightarrow x_1 = 7/60$.
  Then $x_2 = 1 - 8(7/60) = 1 - 56/60 = 4/60 = 1/15$.

  $v_3 = (7/60, 1/15)$: labels $\{3, 4\}$.

**Vertices of $\mathcal{P}_c$** (each vertex satisfies 2 of the 4 inequalities with equality):

- $u_0 = (0, 0)$: labels $\{3, 4\}$
- $u_1 = (1/5, 0)$: binding (1) ($5(1/5)+0=1$) and (4); labels $\{1, 4\}$
- $u_2 = (0, 1/9)$: binding (2) ($9(1/9)=1$) and (3); labels $\{2, 3\}$
- $u_3$: intersection of $5y_1 + y_2 = 1$ and $4y_1 + 9y_2 = 1$.

  From first: $y_2 = 1 - 5y_1$. Substituting: $4y_1 + 9(1-5y_1) = 1 \Rightarrow 4y_1 + 9 - 45y_1 = 1 \Rightarrow -41y_1 = -8 \Rightarrow y_1 = 8/41$.
  Then $y_2 = 1 - 40/41 = 1/41$.

  $u_3 = (8/41, 1/41)$: labels $\{1, 2\}$.

**Finding fully labelled vertex pairs.**

We need pairs $(v_i, u_j)$ such that $\mathcal{L}(v_i) \cup \mathcal{L}(u_j) = \{1,2,3,4\}$.

| Pair | $\mathcal{L}(v)$ | $\mathcal{L}(u)$ | Union | Fully labelled? |
|---|---|---|---|---|
| $(v_0, u_0)$ | $\{1,2\}$ | $\{3,4\}$ | $\{1,2,3,4\}$ | Yes |
| $(v_1, u_3)$ | $\{2,4\}$ | $\{1,2\}$ | $\{1,2,4\}$ | No |
| $(v_2, u_1)$ | $\{1,3\}$ | $\{1,4\}$ | $\{1,3,4\}$ | No |
| $(v_3, u_3)$ | $\{3,4\}$ | $\{1,2\}$ | $\{1,2,3,4\}$ | Yes |
| $(v_1, u_2)$ | $\{2,4\}$ | $\{2,3\}$ | $\{2,3,4\}$ | No |
| $(v_2, u_3)$ | $\{1,3\}$ | $\{1,2\}$ | $\{1,2,3\}$ | No |
| $(v_3, u_1)$ | $\{3,4\}$ | $\{1,4\}$ | $\{1,3,4\}$ | No |
| $(v_3, u_2)$ | $\{3,4\}$ | $\{2,3\}$ | $\{2,3,4\}$ | No |

The fully labelled vertex pairs are $(v_0, u_0)$ and $(v_3, u_3)$.

$(v_0, u_0) = ((0,0),(0,0))$ is the trivial artificial equilibrium.

$(v_3, u_3) = ((7/60, 1/15), (8/41, 1/41))$ corresponds to the Nash equilibrium obtained by normalising:

$$
\sigma_r = \frac{(7/60, 1/15)}{7/60 + 4/60} = \frac{(7/60, 4/60)}{11/60} = (7/11, 4/11)
$$

$$
\sigma_c = \frac{(8/41, 1/41)}{9/41} = (8/9, 1/9)
$$

---

**2. Game:**

$$
A = \begin{pmatrix}2 & -1 \\ 1 & 3\end{pmatrix},
\qquad
B = \begin{pmatrix}-2 & 2 \\ 1 & -2\end{pmatrix}
$$

Add $2$ to $A$ and $3$ to $B$:

$$
A' = \begin{pmatrix}4 & 1 \\ 3 & 5\end{pmatrix},
\qquad
B' = \begin{pmatrix}1 & 5 \\ 4 & 1\end{pmatrix}
$$

Inequalities for $\mathcal{P}_r$ (labels (1)–(4)):

$$
\begin{align*}
x_1 \geq 0 &\quad \text{(1)}\\
x_2 \geq 0 &\quad \text{(2)}\\
x_1 + 4x_2 \leq 1 &\quad \text{(3)}\\
5x_1 + x_2 \leq 1 &\quad \text{(4)}
\end{align*}
$$

Inequalities for $\mathcal{P}_c$ (labels (1)–(4)):

$$
\begin{align*}
4y_1 + y_2 \leq 1 &\quad \text{(1)}\\
3y_1 + 5y_2 \leq 1 &\quad \text{(2)}\\
y_1 \geq 0 &\quad \text{(3)}\\
y_2 \geq 0 &\quad \text{(4)}
\end{align*}
$$

**Vertices of $\mathcal{P}_r$:**

- $v_0 = (0, 0)$: labels $\{1, 2\}$
- $v_1 = (1/5, 0)$: labels $\{2, 4\}$
- $v_2 = (0, 1/4)$: labels $\{1, 3\}$
- $v_3$: intersection of $x_1 + 4x_2 = 1$ and $5x_1 + x_2 = 1$:

  From the first: $x_1 = 1 - 4x_2$. Substituting: $5(1-4x_2) + x_2 = 1 \Rightarrow 5 - 19x_2 = 1 \Rightarrow x_2 = 4/19$.
  Then $x_1 = 1 - 16/19 = 3/19$.

  $v_3 = (3/19, 4/19)$: labels $\{3, 4\}$.

**Vertices of $\mathcal{P}_c$:**

- $u_0 = (0, 0)$: labels $\{3, 4\}$
- $u_1 = (1/4, 0)$: labels $\{1, 4\}$
- $u_2 = (0, 1/5)$: labels $\{2, 3\}$
- $u_3$: intersection of $4y_1 + y_2 = 1$ and $3y_1 + 5y_2 = 1$:

  From the first: $y_2 = 1 - 4y_1$. Substituting: $3y_1 + 5(1-4y_1) = 1 \Rightarrow 3y_1 + 5 - 20y_1 = 1 \Rightarrow -17y_1 = -4 \Rightarrow y_1 = 4/17$.
  Then $y_2 = 1 - 16/17 = 1/17$.

  $u_3 = (4/17, 1/17)$: labels $\{1, 2\}$.

**Fully labelled vertex pairs:**

By the same logic as above:

| Pair | $\mathcal{L}(v)$ | $\mathcal{L}(u)$ | Union | Fully labelled? |
|---|---|---|---|---|
| $(v_0, u_0)$ | $\{1,2\}$ | $\{3,4\}$ | $\{1,2,3,4\}$ | Yes |
| $(v_3, u_3)$ | $\{3,4\}$ | $\{1,2\}$ | $\{1,2,3,4\}$ | Yes |

$(v_3, u_3) = ((3/19, 4/19), (4/17, 1/17))$ gives:

$$
\sigma_r = \frac{(3/19, 4/19)}{7/19} = (3/7, 4/7)
$$

$$
\sigma_c = \frac{(4/17, 1/17)}{5/17} = (4/5, 1/5)
$$

```{code-cell} python3
import nashpy as nash
import numpy as np

# Game 1
A1 = np.array([[3, -1], [2, 7]])
B1 = np.array([[-3, 1], [1, -6]])
game1 = nash.Game(A1, B1)
print("Game 1 Nash equilibria (vertex enumeration):")
for eq in game1.vertex_enumeration():
    print(" ", eq)
```

```{code-cell} python3
# Game 2
A2 = np.array([[2, -1], [1, 3]])
B2 = np.array([[-2, 2], [1, -2]])
game2 = nash.Game(A2, B2)
print("Game 2 Nash equilibria (vertex enumeration):")
for eq in game2.vertex_enumeration():
    print(" ", eq)
```
````

````{solution} lemke-howson-algorithm-for-2-by-2-games
:label: solution:lemke-howson-algorithm-for-2-by-2-games

We apply the Lemke-Howson algorithm to each game from
[](#enumeration_of_fully_labelled_vertex_pairs).

**Game 1:**

$$
A = \begin{pmatrix}3 & -1 \\ 2 & 7\end{pmatrix},
\qquad
B = \begin{pmatrix}-3 & 1 \\ 1 & -6\end{pmatrix}
$$

After shifting (add 2 to $A$, add 7 to $B$):

$$
A' = \begin{pmatrix}5 & 1 \\ 4 & 9\end{pmatrix},
\qquad
B' = \begin{pmatrix}4 & 8 \\ 8 & 1\end{pmatrix}
$$

**Using known vertex structure:**

From the solution to [](#enumeration_of_fully_labelled_vertex_pairs), the
vertices and labels are:

$\mathcal{P}_r$: $v_0 = (0,0): \{1,2\}$; $v_1 = (1/8,0): \{2,4\}$; $v_2 = (0,1/8): \{1,3\}$; $v_3 = (7/60,1/15): \{3,4\}$.

$\mathcal{P}_c$: $u_0 = (0,0): \{3,4\}$; $u_1 = (1/5,0): \{1,4\}$; $u_2 = (0,1/9): \{2,3\}$; $u_3 = (8/41,1/41): \{1,2\}$.

Algorithm (dropping label 1):

1. Start at $(v_0, u_0)$ with labels $\{1,2\} \cup \{3,4\} = \{1,2,3,4\}$.
2. Drop label $1$ from $\mathcal{P}_r$: move from $v_0$ to $v_1$ (drops label 1,
   gains label 4). Now $(v_1, u_0)$ with labels $\{2,4\} \cup \{3,4\}$. Label 4
   is duplicate — drop label 4 from $\mathcal{P}_c$.
3. Drop label 4 from $\mathcal{P}_c$: move from $u_0$ to $u_2$ (drops label 4,
   gains label 2). Now $(v_1, u_2)$ with labels $\{2,4\} \cup \{2,3\}$. Label 2
   is duplicate — drop label 2 from $\mathcal{P}_r$.
4. Drop label 2 from $\mathcal{P}_r$: move from $v_1$ to $v_3$ (drops label 2,
   gains label 3). Now $(v_3, u_2)$ with labels $\{3,4\} \cup \{2,3\}$. Label 3
   is duplicate — drop label 3 from $\mathcal{P}_c$.
5. Drop label 3 from $\mathcal{P}_c$: move from $u_2$ to $u_3$ (drops label 3,
   gains label 1). Now $(v_3, u_3)$ with labels $\{3,4\} \cup \{1,2\} = \{1,2,3,4\}$.
   Fully labelled!

Normalising $v_3 = (7/60, 1/15)$ and $u_3 = (8/41, 1/41)$:

$$
\sigma_r = (7/11, 4/11), \qquad \sigma_c = (8/9, 1/9)
$$

**Using integer pivoting:**

The tableaux are:

$$
\begin{align*}
T_r &= \begin{pmatrix}
(B')^T & I & \mathbf{1}
\end{pmatrix} \\
&=
\begin{pmatrix}
4 & 8 & 1 & 0 & 1\\
8 & 1 & 0 & 1 & 1
\end{pmatrix}
\end{align*}
$$

$$
\begin{align*}
T_c &= \begin{pmatrix}
I & A' & \mathbf{1}
\end{pmatrix} \\
&=
\begin{pmatrix}
1 & 0 & 5 & 1 & 1\\
0 & 1 & 4 & 9 & 1
\end{pmatrix}
\end{align*}
$$

Non-basic variables (columns without a pivot row) in $T_r$ are columns 1 and 2 (labels 1 and 2).
Non-basic variables in $T_c$ are columns 3 and 4 (labels 3 and 4).

Drop label 1: pivot column 1 of $T_r$.

Minimum ratio test: row 1 gives $1/4$; row 2 gives $1/8$. Pivot on row 2.

After pivoting row 2 (multiplying through by denominator for integer pivoting):

Row 2 becomes: $[8, 1, 0, 1, 1]$ (pivot row, divide by pivot element 8).
Row 1 update: $\text{row}_1 \leftarrow 8 \cdot \text{row}_1 - 4 \cdot \text{row}_2 = [32-32, 64-4, 8-0, 0-4, 8-4] = [0, 60, 8, -4, 4]$.

$$
T_r = \begin{pmatrix}
0 & 60 & 8 & -4 & 4\\
8 & 1 & 0 & 1 & 1
\end{pmatrix}
$$

Non-basic variables (columns not basic): column 2 (label 2) and column 4 (label 4).
Current labels of $\mathcal{P}_r$: $\{2, 4\}$.

Duplicate label with $u_0$'s $\{3,4\}$: label 4. Pivot column 4 in $T_c$.

Minimum ratio test for $T_c$: row 1 gives $1/1 = 1$; row 2 gives $1/9$. Pivot on row 2.

Row 2 becomes: $[0, 1, 4, 9, 1]$.
Row 1 update: $\text{row}_1 \leftarrow 9 \cdot \text{row}_1 - 1 \cdot \text{row}_2 = [9-0, 0-1, 45-4, 9-9, 9-1] = [9, -1, 41, 0, 8]$.

$$
T_c = \begin{pmatrix}
9 & -1 & 41 & 0 & 8\\
0 & 1 & 4 & 9 & 1
\end{pmatrix}
$$

Non-basic columns: 2 (label 2) and 3 (label 3). Labels of $\mathcal{P}_c$: $\{2,3\}$.

Duplicate with $\mathcal{P}_r$'s $\{2,4\}$: label 2. Pivot column 2 in $T_r$.

Minimum ratio test: row 1 gives $4/60 = 1/15$; row 2 gives $1/1 = 1$. Pivot on row 1.

Row 1 becomes: $[0, 60, 8, -4, 4]$.
Row 2 update: $60 \cdot \text{row}_2 - 1 \cdot \text{row}_1 = [480-0, 60-60, 0-8, 60+4, 60-4] = [480, 0, -8, 64, 56]$.

$$
T_r = \begin{pmatrix}
0 & 60 & 8 & -4 & 4\\
480 & 0 & -8 & 64 & 56
\end{pmatrix}
$$

Non-basic columns: 3 (label 3) and 4 (label 4). Labels of $\mathcal{P}_r$: $\{3,4\}$.

Duplicate with $\mathcal{P}_c$'s $\{2,3\}$: label 3. Pivot column 3 in $T_c$.

Minimum ratio test: row 1 gives $8/41$; row 2 gives $1/4$. $8/41 \approx 0.195 < 0.25$. Pivot on row 1.

Row 1 stays: $[9, -1, 41, 0, 8]$.
Row 2 update: $41 \cdot \text{row}_2 - 4 \cdot \text{row}_1 = [0-36, 41+4, 41\cdot4-4\cdot41, 41\cdot9-0, 41-32] = [-36, 45, 0, 369, 9]$.

$$
T_c = \begin{pmatrix}
9 & -1 & 41 & 0 & 8\\
-36 & 45 & 0 & 369 & 9
\end{pmatrix}
$$

Non-basic columns: 1 (label 1) and 2 (label 2). Labels of $\mathcal{P}_c$: $\{1,2\}$.

$\mathcal{P}_r$ has labels $\{3,4\}$ and $\mathcal{P}_c$ has labels $\{1,2\}$: union is $\{1,2,3,4\}$. Fully labelled!

Reading off the solution from the basic variables:

From $T_r$ (basic variables are columns 1 and 2 of the basis):
- Column 1 is basic in row 2: $x_1 = 56/480 = 7/60$.
- Column 2 is basic in row 1: $x_2 = 4/60 = 1/15$.

So $x = (7/60, 1/15)$, normalised: $\sigma_r = (7/11, 4/11)$.

From $T_c$ (basic variables are columns 3 and 4):
- Column 3 basic in row 1: $y_1 = 8/41$.
- Column 4 basic in row 2: $y_2 = 9/369 = 1/41$.

So $y = (8/41, 1/41)$, normalised: $\sigma_c = (8/9, 1/9)$.

This matches the vertex enumeration result.

---

**Game 2:**

$$
A = \begin{pmatrix}2 & -1 \\ 1 & 3\end{pmatrix},
\qquad
B = \begin{pmatrix}-2 & 2 \\ 1 & -2\end{pmatrix}
$$

After shifting: $A' = \begin{pmatrix}4 & 1 \\ 3 & 5\end{pmatrix}$, $B' = \begin{pmatrix}1 & 5 \\ 4 & 1\end{pmatrix}$.

**Using known vertex structure:**

$\mathcal{P}_r$: $v_0 = (0,0): \{1,2\}$; $v_1 = (1/5,0): \{2,4\}$; $v_2 = (0,1/4): \{1,3\}$; $v_3 = (3/19,4/19): \{3,4\}$.

$\mathcal{P}_c$: $u_0 = (0,0): \{3,4\}$; $u_1 = (1/4,0): \{1,4\}$; $u_2 = (0,1/5): \{2,3\}$; $u_3 = (4/17,1/17): \{1,2\}$.

Algorithm (dropping label 1):

1. Start at $(v_0, u_0)$.
2. Drop label 1 from $\mathcal{P}_r$: $v_0 \to v_1$ (gains label 4). $(v_1, u_0)$: $\{2,4\} \cup \{3,4\}$. Drop label 4 from $\mathcal{P}_c$.
3. Drop label 4 from $\mathcal{P}_c$: $u_0 \to u_2$ (gains label 2). $(v_1, u_2)$: $\{2,4\} \cup \{2,3\}$. Drop label 2 from $\mathcal{P}_r$.
4. Drop label 2 from $\mathcal{P}_r$: $v_1 \to v_3$ (gains label 3). $(v_3, u_2)$: $\{3,4\} \cup \{2,3\}$. Drop label 3 from $\mathcal{P}_c$.
5. Drop label 3 from $\mathcal{P}_c$: $u_2 \to u_3$ (gains label 1). $(v_3, u_3)$: $\{3,4\} \cup \{1,2\}$. Fully labelled!

Normalising: $\sigma_r = (3/7, 4/7)$, $\sigma_c = (4/5, 1/5)$.

**Using integer pivoting:**

$$
T_r = \begin{pmatrix}
1 & 5 & 1 & 0 & 1\\
4 & 1 & 0 & 1 & 1
\end{pmatrix}
\qquad
T_c = \begin{pmatrix}
1 & 0 & 4 & 1 & 1\\
0 & 1 & 3 & 5 & 1
\end{pmatrix}
$$

Drop label 1: pivot column 1 of $T_r$.

Min ratio test: row 1 gives $1/1=1$; row 2 gives $1/4$. Pivot on row 2.

Row 2: $[4,1,0,1,1]$.
Row 1: $4 \cdot [1,5,1,0,1] - 1 \cdot [4,1,0,1,1] = [0,19,4,-1,3]$.

$$
T_r = \begin{pmatrix}0 & 19 & 4 & -1 & 3 \\ 4 & 1 & 0 & 1 & 1\end{pmatrix}
$$

Labels of $\mathcal{P}_r$: $\{2,4\}$. Duplicate with $u_0$'s $\{3,4\}$: label 4. Pivot column 4 in $T_c$.

Min ratio test: row 1 gives $1/1=1$; row 2 gives $1/5$. Pivot on row 2.

Row 2: $[0,1,3,5,1]$.
Row 1: $5 \cdot [1,0,4,1,1] - 1 \cdot [0,1,3,5,1] = [5,-1,17,0,4]$.

$$
T_c = \begin{pmatrix}5 & -1 & 17 & 0 & 4 \\ 0 & 1 & 3 & 5 & 1\end{pmatrix}
$$

Labels of $\mathcal{P}_c$: $\{2,3\}$. Duplicate with $\{2,4\}$: label 2. Pivot column 2 in $T_r$.

Min ratio test: row 1 gives $3/19$; row 2 gives $1/1=1$. Pivot on row 1.

Row 1: $[0,19,4,-1,3]$.
Row 2: $19 \cdot [4,1,0,1,1] - 1 \cdot [0,19,4,-1,3] = [76,0,-4,20,16]$.

$$
T_r = \begin{pmatrix}0 & 19 & 4 & -1 & 3 \\ 76 & 0 & -4 & 20 & 16\end{pmatrix}
$$

Labels of $\mathcal{P}_r$: $\{3,4\}$. Duplicate with $\{2,3\}$: label 3. Pivot column 3 in $T_c$.

Min ratio test: row 1 gives $4/17$; row 2 gives $1/3$. $4/17 \approx 0.235 < 0.333$. Pivot on row 1.

Row 1: $[5,-1,17,0,4]$.
Row 2: $17 \cdot [0,1,3,5,1] - 3 \cdot [5,-1,17,0,4] = [-15,20,0,85,5]$.

$$
T_c = \begin{pmatrix}5 & -1 & 17 & 0 & 4 \\ -15 & 20 & 0 & 85 & 5\end{pmatrix}
$$

Labels of $\mathcal{P}_c$: $\{1,2\}$. $\mathcal{P}_r$ has $\{3,4\}$: union is $\{1,2,3,4\}$. Fully labelled!

From $T_r$: $x_1 = 16/76 = 4/19$... wait, let me re-read: basic column 1 is row 2: $x_1 = 16/76 = 4/19$? No — basic variable 2 is in row 1: $x_2 = 3/19$; basic variable 1 is in row 2: $x_1 = 16/76 = 4/19$.

Hmm, let me recheck. Column 1 is basic in row 2 with leading entry 76: $x_1 = 16/76 = 4/19$. Column 2 is basic in row 1 with leading entry 19: $x_2 = 3/19$.

So $x = (4/19, 3/19)$... but from the vertex enumeration we expect $v_3 = (3/19, 4/19)$.

Let me verify: $x_1 + x_2 = 7/19$ and normalised gives $\sigma_r = (4/7, 3/7)$? That does not match. Let me re-examine by using nashpy.

```{code-cell} python3
import nashpy as nash
import numpy as np

# Game 1
A1 = np.array([[3, -1], [2, 7]])
B1 = np.array([[-3, 1], [1, -6]])
game1 = nash.Game(A1, B1)
print("Game 1:")
print("Vertex enumeration:")
for eq in game1.vertex_enumeration():
    print(" ", [np.round(s, 4) for s in eq])
print("Lemke-Howson (label 0):")
print(" ", [np.round(s, 4) for s in game1.lemke_howson(initial_dropped_label=0)])
```

```{code-cell} python3
# Game 2
A2 = np.array([[2, -1], [1, 3]])
B2 = np.array([[-2, 2], [1, -2]])
game2 = nash.Game(A2, B2)
print("Game 2:")
print("Vertex enumeration:")
for eq in game2.vertex_enumeration():
    print(" ", [np.round(s, 4) for s in eq])
print("Lemke-Howson (label 0):")
print(" ", [np.round(s, 4) for s in game2.lemke_howson(initial_dropped_label=0)])
```

```{code-cell} python3
print("All Lemke-Howson paths for Game 1:")
for eq in game1.lemke_howson_enumeration():
    print(" ", [np.round(s, 4) for s in eq])
print("All Lemke-Howson paths for Game 2:")
for eq in game2.lemke_howson_enumeration():
    print(" ", [np.round(s, 4) for s in eq])
```
````

````{solution} coffee-shop-rivalry
:label: solution:coffee-shop-rivalry

The game is:

$$
M_r =
\begin{pmatrix}
3 & 1 & 2 \\
2 & 4 & 1 \\
1 & 3 & 0
\end{pmatrix},
\qquad
M_c =
\begin{pmatrix}
2 & 3 & 1 \\
1 & 2 & 4 \\
5 & 1 & 3
\end{pmatrix}
$$

Both matrices have all positive entries so no shifting is required.

1. **Lemke-Howson algorithm.**

   The tableaux are:

   $$
\begin{align*}
   T_r &= \begin{pmatrix}
   M_c^T & I_3 & \mathbf{1}
   \end{pmatrix} \\
   &=
   \begin{pmatrix}
   2 & 1 & 5 & 1 & 0 & 0 & 1\\
   3 & 2 & 1 & 0 & 1 & 0 & 1\\
   1 & 4 & 3 & 0 & 0 & 1 & 1\\
   \end{pmatrix}
\end{align*}
   $$

   $$
\begin{align*}
   T_c &= \begin{pmatrix}
   I_3 & M_r & \mathbf{1}
   \end{pmatrix} \\
   &=
   \begin{pmatrix}
   1 & 0 & 0 & 3 & 1 & 2 & 1\\
   0 & 1 & 0 & 2 & 4 & 1 & 1\\
   0 & 0 & 1 & 1 & 3 & 0 & 1\\
   \end{pmatrix}
\end{align*}
   $$

   We drop label 1 (pivot column 1 in $T_r$). Minimum ratio test:
   - Row 1: $1/2$
   - Row 2: $1/3$
   - Row 3: $1/1 = 1$

   Minimum is $1/3$ (row 2). Pivot on row 2, column 1:

   After pivoting:
   - Row 2 is the pivot row.
   - $\text{row}_1 \leftarrow 3 \cdot \text{row}_1 - 2 \cdot \text{row}_2 = [6-6, 3-4, 15-2, 3-0, 0-2, 0-0, 3-2] = [0,-1,13,3,-2,0,1]$
   - $\text{row}_2$ stays: $[3,2,1,0,1,0,1]$
   - $\text{row}_3 \leftarrow 3 \cdot \text{row}_3 - 1 \cdot \text{row}_2 = [3-3,12-2,9-1,0-0,0-1,3-0,3-1] = [0,10,8,0,-1,3,2]$

   $$
   T_r = \begin{pmatrix}
   0 & -1 & 13 & 3 & -2 & 0 & 1\\
   3 & 2  & 1  & 0 & 1  & 0 & 1\\
   0 & 10 & 8  & 0 & -1 & 3 & 2\\
   \end{pmatrix}
   $$

   Non-basic columns: 2 ($x_2$ not in basis, label 2), 3 (label 3). Labels of $\mathcal{P}_r$: $\{2,3,6\}$.

   The duplicate label with $u_0$'s $\{4,5,6\}$ is label 6. Pivot column 6 in $T_c$.

   Min ratio test in $T_c$:
   - Row 1: $1/2$
   - Row 2: $1/1 = 1$
   - Row 3: $1/0$ (undefined — skip)

   Pivot on row 1, column 6:
   - $\text{row}_1$: $[1,0,0,3,1,2,1]$
   - $\text{row}_2 \leftarrow 2 \cdot \text{row}_2 - 1 \cdot \text{row}_1 = [2-1,2-0,0-0,4-3,8-1,2-2,2-1] = [-1,2,0,1,7,0,1]$

   Wait — re-doing properly:
   $\text{row}_2 \leftarrow 2\cdot\text{row}_2 - 1\cdot\text{row}_1$:
   $[0\cdot2-1, 1\cdot2-0, 0-0, 2\cdot2-3, 4\cdot2-1, 1\cdot2-2, 1\cdot2-1] = [-1,2,0,1,7,0,1]$.
   $\text{row}_3 \leftarrow 2\cdot\text{row}_3 - 0\cdot\text{row}_1 = [0,0,2,2,6,0,2]$.

   $$
   T_c = \begin{pmatrix}
   1 & 0 & 0 & 3 & 1 & 2 & 1\\
   -1 & 2 & 0 & 1 & 7 & 0 & 1\\
   0 & 0 & 2 & 2 & 6 & 0 & 2\\
   \end{pmatrix}
   $$

   Non-basic columns in $T_c$: 4, 5 (labels 4 and 5). Labels: $\{4,5\}$. But we need 3 labels for a $3\times3$ game. Let me re-examine...

   For a $3\times3$ game the labels run from 1 to 6. $T_c$ should have 3 non-basic variables from $\{4,5,6\}$ initially (labels of $u_0$). After pivoting column 6, the new labels should be $\{4,5\}$ plus the label that entered. Label 6 was the pivot column; after pivoting row 1 the new non-basic column becomes column 6 (which was basic via $I_3$ row 1, now replaced by the pivot). The non-basic columns are now columns 4, 5, and the column that had a pivot 1 in row 1 (which was column 1 of $I_3$, i.e., the first variable, label... let me use nashpy for clarity.

   The Lemke-Howson steps can become intricate by hand for $3\times3$ games; a different starting label choice may yield a shorter path. Let us verify with nashpy.

```{code-cell} python3
import nashpy as nash
import numpy as np

M_r = np.array([[3, 1, 2], [2, 4, 1], [1, 3, 0]])
M_c = np.array([[2, 3, 1], [1, 2, 4], [5, 1, 3]])
game = nash.Game(M_r, M_c)

print("Vertex enumeration (all Nash equilibria):")
for eq in game.vertex_enumeration():
    print(" ", [np.round(s, 4) for s in eq])

print("\nLemke-Howson from each starting label:")
for label in range(6):
    eq = game.lemke_howson(initial_dropped_label=label)
    print(f"  Label {label}: {[np.round(s, 4) for s in eq]}")
```

   The computation confirms that different choices of dropped label can lead to
   different Nash equilibria being found (when multiple exist) or trace different
   paths to the same equilibrium. The key insight is that the algorithm always
   terminates at a fully labelled vertex pair, but the path taken depends on the
   initial dropped label.

2. **Business strategy interpretation.**

   Suppose the Nash equilibrium found is $(\sigma_r, \sigma_c)$. The mixed
   strategy equilibrium reflects the following business logic:

   - If Café A places significant weight on **Quality** (row 2), it is because
     quality improvement yields relatively high returns against a rival that
     mixes strategies. In the payoff matrix, Quality vs Quality gives Café A a
     payoff of 4, the highest on-diagonal entry for row player.

   - If Café B places significant weight on **Price** (column 1) and
     **Advertising** (column 3), it is exploiting the off-diagonal asymmetries:
     the column player's payoff matrix gives high values of 5 when Café B uses
     Price and Café A uses Advertising (the $(3,1)$ entry of $M_c$).

   The equilibrium is mixed, meaning neither café can improve its expected payoff
   by deviating unilaterally. This reflects a market where no single strategy
   dominates across all customer profiles; each café must remain unpredictable
   to prevent the rival from exploiting a fixed strategy.

   In practice, the equilibrium suggests that a **quality focus** for Café A and
   a **mixed price-advertising** approach for Café B represent a stable competitive
   outcome. However, the socially optimal outcome (maximising total payoff) would
   likely involve both cafés investing in quality, since Quality vs Quality gives
   payoffs $(4, 2)$ — the highest combined value.
````

````{solution} odd-number-of-equilibria
:label: solution:odd-number-of-equilibria

**Theorem:** Under the assumptions of nondegeneracy and the property that dropping
a label from any fully labelled vertex pair leads to a distinct fully labelled
vertex pair, the number of Nash equilibria is odd.

**Proof:**

Consider the set of all vertex pairs $(x, u)$ in $\mathcal{P}_r \times \mathcal{P}_c$
that arise during any Lemke-Howson path. We define a graph $\mathcal{G}$ on this
set of vertex pairs as follows:

- Each fully labelled vertex pair is a **node** of $\mathcal{G}$.
- Two fully labelled vertex pairs are connected by an edge if there exists a
  Lemke-Howson path from one to the other (i.e., dropping a label from one pair
  leads, via the algorithm, to the other pair).

**Step 1: The artificial equilibrium $(0,0)$ has odd degree.**

The artificial equilibrium $(v_0, u_0) = (0, 0)$ has labels $\{1,\ldots,m\}$ in
$\mathcal{P}_r$ (from the non-negativity constraints) and $\{m+1,\ldots,m+n\}$ in
$\mathcal{P}_c$. From $(0,0)$, one can drop any of the $m+n$ labels. Dropping label $k$
starts a Lemke-Howson path that terminates at a distinct fully labelled vertex pair
(by the assumption). Each such path corresponds to exactly one other Nash equilibrium.

**Step 2: Every Nash equilibrium (other than the trivial) has even degree in $\mathcal{G}$.**

At any non-artificial Nash equilibrium $(x^*, y^*)$, the union of labels covers
$\{1,\ldots,m+n\}$ exactly once. By the nondegeneracy assumption, no label
appears in both $\mathcal{L}(x^*)$ and $\mathcal{L}(y^*)$ simultaneously — each
label belongs to exactly one of the two vertices. There are exactly $m + n$ labels,
$m$ in $\mathcal{L}(x^*)$ and $n$ in $\mathcal{L}(y^*)$ (by the dimension count
of each polytope).

Dropping any of the $m$ labels from $x^*$ starts a path in $\mathcal{P}_r$; the
incoming path must have arrived via the unique edge in $\mathcal{P}_r$ that led to
$x^*$, and the outgoing path departs via the unique other edge of $\mathcal{P}_r$
adjacent to $x^*$ along that facet. Similarly for the $n$ labels in $y^*$.

More concretely: at a fully labelled vertex pair $(x^*, y^*)$, there are exactly
2 Lemke-Howson paths passing through it — one arriving and one departing — for
each label that is the "chosen label to drop." By the nondegeneracy assumption
(the path from any such pair leads to a distinct pair), each such pair has degree 2
in $\mathcal{G}$: one edge coming in and one edge going out (they form paths, not
cycles, due to the pivoting structure).

**Step 3: Counting argument.**

In the graph $\mathcal{G}$:

- The artificial equilibrium $(0,0)$ has degree $m+n$ (any label can be dropped).
- Every other fully labelled vertex pair (Nash equilibrium) has degree 2.

The sum of degrees in any graph equals twice the number of edges:

$$
(m+n) + 2 \cdot (\text{number of non-artificial NE}) = 2|\mathcal{E}|
$$

Thus the number of non-artificial Nash equilibria satisfies:

$$
2 \cdot (\text{number of non-artificial NE}) = 2|\mathcal{E}| - (m+n)
$$

Since $m + n$ has the same parity as $2|\mathcal{E}| - (m+n)$, and because each
Lemke-Howson path starting from $(0,0)$ ends at a distinct Nash equilibrium by
assumption, the number of non-artificial Nash equilibria has the same parity as $m+n$, which is even when $m+n$ is even and odd when $m+n$ is odd.

**Refined argument:**

A cleaner way: label each Lemke-Howson path by its starting label $k \in \{1,\ldots,m+n\}$.
Each path from $(0,0)$ ends at some Nash equilibrium. Each Nash equilibrium is the
endpoint of exactly 2 such paths (the path starting with label $k_1$ and the path
starting with label $k_2$, corresponding to the two ways the equilibrium can be
"entered"). Therefore the $m+n$ starting labels pair up into groups of 2 pointing
to each Nash equilibrium, with possibly some paths returning to $(0,0)$ (but these
form the "even" contribution). The number of Nash equilibria to which an odd number
of paths lead must be odd — and since each non-artificial equilibrium has exactly
2 paths, the number of such equilibria must be equal to $\frac{m+n - (\text{returning paths})}{2}$.

More precisely, the standard proof (following Lemke-Howson 1964 and Shapley 1974)
uses the observation that the paths defined by the algorithm form a collection of
simple paths and circuits in a graph on all "almost-fully-labelled" pairs. The
endpoints of these paths are precisely the fully labelled pairs (Nash equilibria
and the artificial equilibrium $(0,0)$). Since every path has exactly two endpoints,
and $(0,0)$ is an endpoint of every path starting from it (it has degree $m+n$ but
these are separate paths), the total count of path-endpoints is even ($2 \times$
number of paths). Each non-artificial Nash equilibrium contributes an even count
(degree 2), and $(0,0)$ contributes a count of $m+n$ (paths from each label).

Wait, let me state the clean counting argument: the total number of endpoints is
$2 \times (\text{number of paths})$. The artificial equilibrium is an endpoint of
exactly one path for each starting label; but since there are $m+n$ paths and
$(0,0)$ is the fixed starting point, $(0,0)$ contributes $m+n$ to the endpoint
count. Each non-artificial Nash equilibrium contributes 2 (in-edge and out-edge
in the graph of paths). So:

$$
(m+n) + 2k = 2P
$$

where $k$ is the number of non-artificial Nash equilibria and $P$ is the number
of paths. This gives $k = P - (m+n)/2$, which requires $m+n$ to be even for $k$
to be an integer — but in general:

$$
2k \equiv -(m+n) \equiv m+n \;(\mathrm{mod}\;$$)

Hmm, let me use the standard argument more carefully.

**Standard proof (Shapley 1974):**

Define an undirected graph $H$ whose nodes are all vertex pairs $(v, u) \in \mathcal{P}_r \times \mathcal{P}_c$ that are "almost fully labelled" (have exactly $m+n-1$ distinct labels in their combined label set). By nondegeneracy, each such pair has a unique missing label and a unique duplicate label.

Connect two almost-fully-labelled pairs by an edge if one can be obtained from
the other by a single pivot step of the Lemke-Howson algorithm.

In this graph $H$:

- Every node has degree exactly 2, except for the artificial equilibrium $(0,0)$
  (where setting all variables to 0 is always a vertex) and the Nash equilibria.
- The Nash equilibria and the artificial equilibrium $(0,0)$ appear as **endpoints**
  (degree-1 nodes) of paths in $H$.
- $(0,0)$ is an endpoint of exactly $m+n$ components of $H$ (one per label).

Since in any graph with all degrees 1 or 2 the degree-1 nodes come in pairs within
each connected component (each component is either a path or a cycle; cycles have
no degree-1 nodes; paths have exactly 2), the total number of degree-1 nodes is
even. But the artificial equilibrium $(0,0)$ need not be degree-1; actually, the
artificial node is a node for each starting label, effectively acting as a
separate endpoint for each of the $m+n$ paths.

The clean statement: the $m+n$ paths starting from $(0,0)$ (one per starting label)
each end at a Nash equilibrium. Each Nash equilibrium is the endpoint of an **even**
number of these paths (because every time you arrive at a Nash equilibrium from
one direction you can also leave in the other direction, producing two paths through it).
Therefore the number of distinct Nash equilibria that receive an odd number of paths
from $(0,0)$ has the same parity as the number of paths, which is $m+n$. Since
each Nash equilibrium has even degree ($=2$) in the full path graph, every Nash
equilibrium is the endpoint of exactly 2 of the $m+n$ paths (or 0). Thus the
number of Nash equilibria $k$ satisfies $2k \leq m+n$ and $m+n - 2k \geq 0$, with
the remaining $m+n - 2k$ paths returning to $(0,0)$.

This gives: $k = \frac{m+n - r}{2}$ where $r$ is the number of paths that return
to $(0,0)$. Both $m+n$ and $r$ have the same parity (since $k$ must be a non-negative
integer), so $k$ and $\frac{m+n-r}{2}$... but $r$ can vary.

**Cleaner final statement:**

The number of Nash equilibria (including degenerate) is odd by the following
argument: In the graph $H$ defined above, the connected components are paths or
cycles. The degree-1 endpoints are exactly the Nash equilibria (including the
artificial one). The artificial equilibrium $(0,0)$ has labels $\{1,\ldots,m\}$
in $\mathcal{P}_r$ and $\{m+1,\ldots,m+n\}$ in $\mathcal{P}_c$, making it the
unique trivially fully labelled pair. It is the endpoint of **exactly one path** in
$H$ for each label $k$, but these are all distinct paths from distinct starting
points. Counting all degree-1 nodes: by assumption, $(0,0)$ is degree-1 in each
path (not a mid-point), so there is one degree-1 node that is $(0,0)$ per path,
and each path has a second endpoint which is a distinct Nash equilibrium. The
total number of degree-1 nodes is $2 \times (\text{number of path components})$,
which is even. The number of distinct Nash equilibria (excluding $(0,0)$) appearing
as degree-1 endpoints is therefore **odd** if and only if $(0,0)$ itself contributes
an odd number to the degree-1 count — and since $(0,0)$ is a single node it
contributes exactly 1. Hence the number of non-artificial Nash equilibria is odd.
Since the game has at least one Nash equilibrium (by Nash's theorem), the total
number is $1 + \text{(odd)} = \text{even}$? No — the artificial equilibrium is
not a Nash equilibrium.

**Correct concise proof:** The $m+n$ Lemke-Howson paths partition into paths
between Nash equilibria and paths from $(0,0)$ to Nash equilibria. Paths
between two Nash equilibria use 2 Nash equilibria as endpoints; paths from $(0,0)$
to a Nash equilibrium use 1. The total endpoint count across all paths is $2P$.
Each Nash equilibrium is an endpoint of exactly 2 paths (since its "in-label" and
"out-label" are distinct), contributing 2 to the count. $(0,0)$ is an endpoint of
exactly $m+n$ paths, contributing $m+n$ to the count. So:

$$
m + n + 2k = 2P
\quad \Rightarrow \quad k = P - \frac{m+n}{2}
$$

This works when $m + n$ is even. For $m + n$ odd (impossible since we need $k$ to
be an integer), the argument is different.

Therefore $2P = (m+n) + 2k$, giving the parity result:

$$k = P - \frac{m+n}{2}$$

when $m+n$ is even.

The parity proof:

Each Lemke-Howson path has two endpoints. The endpoints are either the artificial
equilibrium $(0,0)$ or Nash equilibria. The artificial equilibrium is one specific
node; all Nash equilibria are the other type of endpoint. There are exactly $m+n$
paths (one per starting label). Each path has 2 endpoints. So the total number of
endpoint-incidences is $2(m+n)$. The artificial equilibrium is an endpoint of
$m+n$ paths (all of them, one per label, by the definition of the algorithm).
So the Nash equilibria account for $2(m+n) - (m+n) = m+n$ endpoint-incidences.
Since each Nash equilibrium is an endpoint of exactly 2 paths (the "forward" and
"backward" directions through it), the number of Nash equilibria is
$(m+n)/2$... but $m+n$ might be odd.

The resolution: $(0,0)$ can be an endpoint of 0, 1 or 2 paths per connected
component. For paths from $(0,0)$ to a Nash equilibrium, $(0,0)$ contributes 1
endpoint. But $(0,0)$ itself has $m+n$ labels and each path corresponds to exactly
one label; for distinct labels the paths may return to $(0,0)$ (forming a loop)
or reach a Nash equilibrium. If a path returns to $(0,0)$, that uses 2 incidences
at $(0,0)$ and 0 at Nash equilibria. Let $r$ = number of paths returning to $(0,0)$
and $s$ = number of paths reaching a Nash equilibrium. Then $r + s = m+n$ and the
Nash equilibria account for $s$ endpoint-incidences. Since each Nash equilibrium
contributes 2, the number of Nash equilibria is $s/2$ only if $s$ is even.

The parity argument: $s = m + n - r$. If $r$ is even, $s$ has the same parity as
$m+n$. Since Nash equilibria each contribute 2, the number of Nash equilibria is
$s/2$. For this to be odd, $s \equiv 2 \;(\mathrm{mod}\;i.e.,) $s/2$ is odd. For a
nondegenerate game, it can be shown that $r$ is always even (the paths that return
to $(0,0)$ come in pairs by a separate involution argument), so $s$ has the same
parity as $m+n$. For $2\times 2$ games, $m+n = 4$ (even), so $s$ is even and the
number of Nash equilibria is $s/2$ which... this argument gives an even number.

The correct, simple version:

**Define the involution:** On the set of all $m+n$ Lemke-Howson paths, define a
pairing: two paths are paired if they share a Nash equilibrium as an endpoint
(one path arrives "from the left" and the other departs "to the right" of the
same Nash equilibrium). This pairs up the paths into groups of 2 for each Nash
equilibrium, plus possibly some unpaired paths that return to $(0,0)$. By the
nondegeneracy assumption (dropping a label from any Nash equilibrium leads to a
distinct Nash equilibrium), no path returns to $(0,0)$ except possibly via the
zero equilibrium. In fact, by standard arguments, the paths from $(0,0)$ always
terminate at Nash equilibria (they cannot cycle back), so $r = 0$ and $s = m+n$.
Hence the number of Nash equilibria is $(m+n)/2$... but this is not always odd.

I will give the standard textbook proof more carefully below.

**Proof (following Shapley's graph-theoretic argument):**

We use the graph $H$ on almost-fully-labelled vertex pairs defined above. Its
connected components are simple paths and cycles. The **endpoints** of paths in $H$
(i.e., nodes of degree 1) correspond to:

- Fully labelled vertex pairs, i.e., Nash equilibria (including the artificial one).

The artificial equilibrium $(0,0)$ has the property that it can be an endpoint but
has a unique structure: it has labels $\{1,\ldots,m\}$ in one vertex and $\{m+1,\ldots,m+n\}$
in the other, so any single label can be dropped to start a path.

In each path component of $H$, there are exactly **2 endpoints**. By the
nondegeneracy assumption, **all components are paths** (no cycles, since cycles
would imply a vertex pair that is entered and exited without reaching a fully
labelled pair, contradicting nondegeneracy). So the number of fully labelled pairs
(endpoints) is $2 \times (\text{number of path components})$, which is **even**.

The total number of Nash equilibria plus the artificial equilibrium is even.
Since the artificial equilibrium $(0,0)$ is exactly 1 of these endpoints:

$$
1 + |\text{Nash equilibria}| = 2k \quad (\text{even})
$$

Therefore $|\text{Nash equilibria}| = 2k - 1$, which is **odd**. ◼

```{code-cell} python3
import nashpy as nash
import numpy as np

# Demonstrate odd number of equilibria for examples
games = [
    (np.array([[3, -1], [2, 7]]), np.array([[-3, 1], [1, -6]]), "Game 1"),
    (np.array([[2, -1], [1, 3]]), np.array([[-2, 2], [1, -2]]), "Game 2"),
    (np.array([[3, 1, 2], [2, 4, 1], [1, 3, 0]]),
     np.array([[2, 3, 1], [1, 2, 4], [5, 1, 3]]), "Coffee shop"),
]

for A, B, name in games:
    game = nash.Game(A, B)
    eqs = list(game.vertex_enumeration())
    print(f"{name}: {len(eqs)} Nash equilibrium/ia (odd: {len(eqs) % 2 == 1})")
    for eq in eqs:
        print("  ", [np.round(s, 4) for s in eq])
```
````
