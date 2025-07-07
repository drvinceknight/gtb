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

### Example: Best Response Polytopes for the threat detection game

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

### Example: Vertex labelling for the threat detection game

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

### Example: Fully labelled vertex pair for the threat detection game

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

### Example: Application of the Lemke–Howson algorithm for the threat detection game with known vertices and labels

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

### Example: Application of the Lemke-Howson Algorithm for the threat detection game with integer pivoting

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

(exercise:enumeration_of_fully_labelled_vertex_pairs)=

### Exercise: Enumeration of fully labelled vertex pairs

For each of the following games, draw the best response polytopes and identify
all fully labelled vertex pairs:

1. $
   A =
   \begin{pmatrix}
   3 & -1 \\
   2 & 7
   \end{pmatrix},
   \qquad
   B =
   \begin{pmatrix}
   -3 & 1 \\
   1 & -6
   \end{pmatrix}
   $
2. $
   A =
   \begin{pmatrix}
   2 & -1 \\
   1 & 3
   \end{pmatrix},
   \qquad
   B =
   \begin{pmatrix}
   -2 & 2 \\
   1 & -2
   \end{pmatrix}
   $

### Exercise: Lemke-Howson algorithm for 2-by-2 games

Using the games from
[Exercise: Enumeration of fully labelled vertex pairs](#exercise:enumeration_of_fully_labelled_vertex_pairs),
apply the Lemke–Howson algorithm to compute a Nash equilibrium in each case.
Carry out the algorithm twice: once using the known vertex structure, and once
using integer pivoting.

### Exercise: Coffee shop rivalry

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

$
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
$

1. Use the Lemke–Howson algorithm to find a Nash equilibrium. Describe how
   different choices of dropped label may lead to different paths.
2. Interpret the equilibrium in terms of business strategy: What might the
   equilibrium suggest about the balance between pricing, quality, and advertising?

(exercise_odd_number_of_equilibria)=

### Exercise: Odd number of equilibria

Assume the game is **nondegenerate**: each vertex of the best response
polytopes has exactly the number of labels required to define it, and no label
appears more than once across a vertex pair. Also assume that, when applying
the Lemke–Howson algorithm, dropping a label from any fully labelled vertex
pair always leads to a **distinct** fully labelled vertex pair.

Under these assumptions, prove that the number of fully labelled vertex pairs —
and hence the number of Nash equilibria — is always **odd**.

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
[odd](#exercise_odd_number_of_equilibria). The algorithm was later extended to
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
