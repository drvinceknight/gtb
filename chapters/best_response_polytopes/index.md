---
kernelspec:
  name: python3
  display_name: "Python 3"
---

(chp:best_response_polytopes)=

# Best response polytopes

The set of mixed strategies that best respond to some opponent strategy forms
a polytope, and Nash equilibria correspond to complementary vertices of a pair
of such polytopes. This chapter develops this geometric perspective and
introduces the Lemke–Howson algorithm for finding Nash equilibria in two-player
games.

```{figure} assets/illustrations/tetris.png
:alt: Interlocking geometric blocks, reminiscent of fitting polytope pieces together.
:label: fig:tetris
:class: illustration
:width: 60%

Geometric pieces fitting together. The best responses of each player form a
polytope, and the Nash equilibria of a game sit at carefully matched vertices
of a pair of such shapes.
```

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
the attempt, for instance, if the file transfer crashes mid-way and no alert is
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

The polytope $\mathcal{P}_c$, corresponds to the set of points with an upper bound on the
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

The three dimensional $\mathcal{P}_c$.
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
x_2 = 0& \implies \text{\textcircled{2}: the second action is not played by the strategy
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

Similarly for $\mathcal{P}_c$

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
y_2 = 0& \implies \text{\textcircled{5}: the second action is not played by the strategy
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
x_2 = 135/91 \ne 0\\
x_3 = 0& \implies \text{\textcircled{3}: the third action is not played by the strategy
represented by } x\\
(xM_c)_1 = 475/637\\
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
We can use labels to identify if pairs of strategies are best responses to each
other.
```

If a label is present in either vertex then either of the
following are true:

- it is indicating that an action is not played (for example label 1 in $\mathcal{P}_r$).
- it is indicating that the same action is a best response to the strategy represented
  by the vector (for example label 1 in $\mathcal{P}_c$).

Looking at $v_5$ and $u_5$ the union of the labels of these vertices gives the
full set of vertices.

This leads to the following definition.

### Definition: Fully labelled vertex pair

---

A pair of vertices $(x, y) \in \mathcal{P}_r \times \mathcal{P}_c$ is said to be a
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
   adjacent vertex ($v_1$, $v_2$, $v_3$, $v_4$, $v_6$, or $v_7$) that does not
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

1. The ratio for the first row: $\frac{7/288}{469/7200} = 25/67$
2. The ratio for the second row: $\frac{7/40}{37/200} = 35/37$
3. The ratio for the third row: $\frac{45/71}{7/71} = 45/7$

We pivot on the first row giving:

$$
T_c = \begin{pmatrix}
3195/938 & 800/469 & -635/134 & 1 & 0 & 0 & 25/67\\
-2627/64000 & 71/2250 & 9443/576000 & 0 & 0 & 4757/288000 & 497/72000\\
-7/320 & -7/36 & 49/192 & 0 & 469/7200 & 0 & 7/180\\
\end{pmatrix}
$$

This tableau has labels $\{1, 2, 3\}$ so we have a fully labelled vertex pair.

Setting the non-basic variables to 0 we have the following systems of equations:

$$
\begin{align*}
    64051 / 18225000 x_1 & = 4277/911250\\
    4927/283500x_2 & = 31 / 2100\\
    x_3 & = 5832 / 4927\\
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

Giving: $x = (6580/4927, 4185/4927, 5832/4927)$ and $y = (25/67, 40/67, 28/67)$ which when normalised [](#eqn:normalisation_of_v_5) - [](#eqn:normalisation_of_u_5) gives:

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

Under these assumptions, prove that the number of fully labelled vertex pairs,
and hence the number of Nash equilibria, is always **odd**.
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
print(list(game.vertex_enumeration()))
```

### Lemke-Howson with Nashpy

Nashpy can be used to carry out the Lemke-Howson algorithm, an efficient way
to find a Nash equilibrium.

```{code-cell} python3
label_to_drop = 0
print(f"Nash equilibrium: {game.lemke_howson(initial_dropped_label=label_to_drop)}")
```

You can also enumerate all possible dropped labels:

```{code-cell} python3
print(list(game.lemke_howson_enumeration()))
```

### Vertex enumeration with Gambit

Gambit can be used to enumerate all pairs of vertices:

```{code-cell} python3
import pygambit as gbt

game = gbt.Game.from_arrays(M_r, M_c)
print(gbt.nash.enummixed_solve(game))
```

### Lemke-Howson with Gambit

Gambit can be used to carry out the Lemke-Howson algorithm:

```{code-cell} python3
print(gbt.nash.lcp_solve(game))
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
computationally challenging task**; this intuitive difficulty is formalised in
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
| Fully labelled vertex pair | A pair of vertices whose labels cover all $m + n$ actions, corresponds to a Nash equilibrium. |
| Lemke–Howson algorithm     | A path-following method that constructs equilibria by dropping and replacing labels. |
| Integer pivoting           | A tableau-based pivoting method used to trace Lemke–Howson paths efficiently.     |
```

```{important}
In every nondegenerate two-player game, each Nash equilibrium corresponds to a
fully labelled vertex pair of the best response polytopes.

Crucially, we can find such a vertex pair without explicitly constructing the
polytopes, using integer pivoting and the Lemke–Howson algorithm.
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
   is duplicate, so drop label 4 from $\mathcal{P}_c$.
3. Drop label 4 from $\mathcal{P}_c$: move from $u_0$ to $u_2$ (drops label 4,
   gains label 2). Now $(v_1, u_2)$ with labels $\{2,4\} \cup \{2,3\}$. Label 2
   is duplicate, so drop label 2 from $\mathcal{P}_r$.
4. Drop label 2 from $\mathcal{P}_r$: move from $v_1$ to $v_3$ (drops label 2,
   gains label 3). Now $(v_3, u_2)$ with labels $\{3,4\} \cup \{2,3\}$. Label 3
   is duplicate, so drop label 3 from $\mathcal{P}_c$.
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
1 & 4 & 1 & 0 & 1\\
5 & 1 & 0 & 1 & 1
\end{pmatrix}
\qquad
T_c = \begin{pmatrix}
1 & 0 & 4 & 1 & 1\\
0 & 1 & 3 & 5 & 1
\end{pmatrix}
$$

Drop label 1: pivot column 1 of $T_r$.

Min ratio test: row 1 gives $1/1 = 1$; row 2 gives $1/5$. Pivot on row 2.

Row 2 (the pivot row) is unchanged: $[5,1,0,1,1]$.
Row 1: $5 \cdot [1,4,1,0,1] - 1 \cdot [5,1,0,1,1] = [0,19,5,-1,4]$.

$$
T_r = \begin{pmatrix}0 & 19 & 5 & -1 & 4 \\ 5 & 1 & 0 & 1 & 1\end{pmatrix}
$$

Labels of $\mathcal{P}_r$: $\{2,4\}$. Duplicate with $u_0$'s $\{3,4\}$: label 4. Pivot column 4 in $T_c$.

Min ratio test: row 1 gives $1/1 = 1$; row 2 gives $1/5$. Pivot on row 2.

Row 2 (the pivot row) is unchanged: $[0,1,3,5,1]$.
Row 1: $5 \cdot [1,0,4,1,1] - 1 \cdot [0,1,3,5,1] = [5,-1,17,0,4]$.

$$
T_c = \begin{pmatrix}5 & -1 & 17 & 0 & 4 \\ 0 & 1 & 3 & 5 & 1\end{pmatrix}
$$

Labels of $\mathcal{P}_c$: $\{2,3\}$. Duplicate with $\{2,4\}$: label 2. Pivot column 2 in $T_r$.

Min ratio test: row 1 gives $4/19$; row 2 gives $1/1 = 1$. Pivot on row 1.

Row 1 (the pivot row) is unchanged: $[0,19,5,-1,4]$.
Row 2: $19 \cdot [5,1,0,1,1] - 1 \cdot [0,19,5,-1,4] = [95,0,-5,20,15]$.

$$
T_r = \begin{pmatrix}0 & 19 & 5 & -1 & 4 \\ 95 & 0 & -5 & 20 & 15\end{pmatrix}
$$

Labels of $\mathcal{P}_r$: $\{3,4\}$. Duplicate with $\{2,3\}$: label 3. Pivot column 3 in $T_c$.

Min ratio test: row 1 gives $4/17$; row 2 gives $1/3$. $4/17 \approx 0.235 < 0.333$. Pivot on row 1.

Row 1 (the pivot row) is unchanged: $[5,-1,17,0,4]$.
Row 2: $17 \cdot [0,1,3,5,1] - 3 \cdot [5,-1,17,0,4] = [-15,20,0,85,5]$.

$$
T_c = \begin{pmatrix}5 & -1 & 17 & 0 & 4 \\ -15 & 20 & 0 & 85 & 5\end{pmatrix}
$$

Labels of $\mathcal{P}_c$: $\{1,2\}$. $\mathcal{P}_r$ has $\{3,4\}$: union is $\{1,2,3,4\}$. Fully labelled!

Reading off the solution from the basic variables. In $T_r$, column 1 is basic in
row 2 and column 2 is basic in row 1:

$$
x_1 = \frac{15}{95} = \frac{3}{19}, \qquad x_2 = \frac{4}{19},
$$

so $x = (3/19, 4/19)$, normalised: $\sigma_r = (3/7, 4/7)$. In $T_c$, column 3 is
basic in row 1 and column 4 is basic in row 2:

$$
y_1 = \frac{4}{17}, \qquad y_2 = \frac{5}{85} = \frac{1}{17},
$$

so $y = (4/17, 1/17)$, normalised: $\sigma_c = (4/5, 1/5)$. This matches the vertex
enumeration result.

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

   The minimum is $1/3$ (row 2). Pivoting on row 2:
   - Row 2 (the pivot row) is unchanged: $[3,2,1,0,1,0,1]$.
   - $\text{row}_1 \leftarrow 3 \cdot \text{row}_1 - 2 \cdot \text{row}_2 = [0,-1,13,3,-2,0,1]$.
   - $\text{row}_3 \leftarrow 3 \cdot \text{row}_3 - 1 \cdot \text{row}_2 = [0,10,8,0,-1,3,2]$.

   $$
   T_r = \begin{pmatrix}
   0 & -1 & 13 & 3 & -2 & 0 & 1\\
   3 & 2  & 1  & 0 & 1  & 0 & 1\\
   0 & 10 & 8  & 0 & -1 & 3 & 2\\
   \end{pmatrix}
   $$

   The non-basic columns are 2, 3, and 5, so the labels of $\mathcal{P}_r$ are
   $\{2,3,5\}$. The duplicate with $u_0$'s $\{4,5,6\}$ is label 5. Pivot column 5
   in $T_c$.

   Minimum ratio test in $T_c$:
   - Row 1: $1/1 = 1$
   - Row 2: $1/4$
   - Row 3: $1/3$

   The minimum is $1/4$ (row 2). Pivoting on row 2:
   - Row 2 (the pivot row) is unchanged: $[0,1,0,2,4,1,1]$.
   - $\text{row}_1 \leftarrow 4 \cdot \text{row}_1 - 1 \cdot \text{row}_2 = [4,-1,0,10,0,7,3]$.
   - $\text{row}_3 \leftarrow 4 \cdot \text{row}_3 - 3 \cdot \text{row}_2 = [0,-3,4,-2,0,-3,1]$.

   $$
   T_c = \begin{pmatrix}
   4 & -1 & 0 & 10 & 0 & 7 & 3\\
   0 & 1  & 0 & 2  & 4 & 1 & 1\\
   0 & -3 & 4 & -2 & 0 & -3& 1\\
   \end{pmatrix}
   $$

   The labels of $\mathcal{P}_c$ are $\{2,4,6\}$. The duplicate with $\{2,3,5\}$
   is label 2. Pivot column 2 in $T_r$.

   Minimum ratio test (skipping non-positive entries):
   - Row 2: $1/2$
   - Row 3: $2/10 = 1/5$

   The minimum is $1/5$ (row 3). Pivoting on row 3:
   - Row 3 (the pivot row) is unchanged: $[0,10,8,0,-1,3,2]$.
   - $\text{row}_1 \leftarrow 10 \cdot \text{row}_1 + 1 \cdot \text{row}_3 = [0,0,138,30,-21,3,12]$.
   - $\text{row}_2 \leftarrow 10 \cdot \text{row}_2 - 2 \cdot \text{row}_3 = [30,0,-6,0,12,-6,6]$.

   $$
   T_r = \begin{pmatrix}
   0  & 0  & 138 & 30 & -21 & 3  & 12\\
   30 & 0  & -6  & 0  & 12  & -6 & 6\\
   0  & 10 & 8   & 0  & -1  & 3  & 2\\
   \end{pmatrix}
   $$

   The labels of $\mathcal{P}_r$ are $\{3,5,6\}$. The duplicate with $\{2,4,6\}$
   is label 6. Pivot column 6 in $T_c$.

   Minimum ratio test (skipping non-positive entries):
   - Row 1: $3/7$
   - Row 2: $1/1 = 1$

   The minimum is $3/7$ (row 1). Pivoting on row 1:
   - Row 1 (the pivot row) is unchanged: $[4,-1,0,10,0,7,3]$.
   - $\text{row}_2 \leftarrow 7 \cdot \text{row}_2 - 1 \cdot \text{row}_1 = [-4,8,0,4,28,0,4]$.
   - $\text{row}_3 \leftarrow 7 \cdot \text{row}_3 + 3 \cdot \text{row}_1 = [12,-24,28,16,0,0,16]$.

   $$
   T_c = \begin{pmatrix}
   4   & -1  & 0  & 10 & 0  & 7 & 3\\
   -4  & 8   & 0  & 4  & 28 & 0 & 4\\
   12  & -24 & 28 & 16 & 0  & 0 & 16\\
   \end{pmatrix}
   $$

   The labels of $\mathcal{P}_c$ are $\{1,2,4\}$. Together with $\mathcal{P}_r$'s
   $\{3,5,6\}$ the union is $\{1,2,3,4,5,6\}$: fully labelled.

   Reading off the basic variables. From $T_r$, column 1 is basic in row 2 and
   column 2 in row 3:

   $$
   x_1 = \frac{6}{30} = \frac{1}{5}, \qquad x_2 = \frac{2}{10} = \frac{1}{5},
   \qquad x_3 = 0,
   $$

   so $\sigma_r = (1/2, 1/2, 0)$. From $T_c$, column 5 is basic in row 2 and
   column 6 in row 1:

   $$
   y_1 = 0, \qquad y_2 = \frac{4}{28} = \frac{1}{7}, \qquad y_3 = \frac{3}{7},
   $$

   so $\sigma_c = (0, 1/4, 3/4)$. We can confirm this with nashpy.

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

   The algorithm returns $\sigma_r = (1/2, 1/2, 0)$ and $\sigma_c = (0, 1/4, 3/4)$.
   Café A splits evenly between **Price** and **Quality** and never **Advertises**;
   Café B never competes on **Price**, playing **Quality** a quarter of the time
   and **Advertising** the rest.

   - Café A is indifferent between Price and Quality against $\sigma_c$: both earn
     an expected payoff of $7/4$, while Advertising earns only $3/4$ and is dropped.
     Mixing equally between its two best responses is what keeps Café B indifferent
     in turn.

   - Café B avoids Price because, against an opponent who never advertises, Price
     is the weaker option: both Quality and Advertising earn $5/2$ against
     $\sigma_r$, whereas Price earns only $3/2$.

   The equilibrium is mixed, meaning neither café can improve its expected payoff
   by deviating unilaterally. This reflects a market where no single strategy
   dominates across all customer profiles; each café must remain unpredictable
   across the strategies it does use to prevent the rival from exploiting a fixed
   choice.
````

````{solution} odd-number-of-equilibria
:label: solution:odd-number-of-equilibria

**Theorem:** Under the assumptions of nondegeneracy and the property that dropping
a label from any fully labelled vertex pair leads to a distinct fully labelled
vertex pair, the number of Nash equilibria is odd.

**Proof:**

Each vertex of $\mathcal{P}_r$ carries exactly $m$ labels and each vertex of
$\mathcal{P}_c$ exactly $n$, so a vertex pair $(x, y)$ carries $m + n$ labels
counted with multiplicity. Call the pair **completely labelled** when these labels
are all distinct, so that every label in $\{1, \ldots, m + n\}$ appears exactly
once; this is the fully labelled condition. By nondegeneracy the completely
labelled pairs are exactly the Nash equilibria together with the artificial pair
$(0, 0)$, whose labels are $\{1, \ldots, m\}$ (from $x = 0$) and
$\{m + 1, \ldots, m + n\}$ (from $y = 0$).

Fix a label $k \in \{1, \ldots, m + n\}$ and call a pair **$k$-almost completely
labelled** if every label except possibly $k$ appears. Under nondegeneracy such a
pair is either completely labelled, or carries every label except $k$ with exactly
one other label duplicated.

Form the graph $H_k$ whose nodes are the $k$-almost completely labelled pairs, with
an edge joining two pairs that differ by a single Lemke-Howson pivot: dropping the
duplicated label from one of the two vertices that carry it. The degree of a node
is then determined by two cases:

- A node that is not completely labelled has exactly one duplicated label, carried
  by a vertex of $\mathcal{P}_r$ and a vertex of $\mathcal{P}_c$. Dropping it on
  either side gives a pivot, so the node has **degree 2**.
- A completely labelled node has no duplicated label, so the only available move is
  to drop label $k$ itself. It has **degree 1**.

Every connected component of $H_k$ is therefore a path or a cycle, and the degree-1
nodes are precisely the completely labelled pairs. In a disjoint union of paths and
cycles the degree-1 nodes come in pairs, one at each end of every path, so their
total number is **even**.

The completely labelled pairs are the Nash equilibria together with the artificial
pair $(0, 0)$. Hence

$$
\bigl|\text{Nash equilibria}\bigr| + 1 \text{ is even},
$$

so the number of Nash equilibria is **odd**. $\square$

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
