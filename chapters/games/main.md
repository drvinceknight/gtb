---
kernelspec:
  name: python3
  display_name: "Python 3"
---

# Games

```{figure} ./logo/main.png
:alt: Logo of chapter
:height: 50px
```

## Motivating Example

Consider the following scenario: you would like to meet your **friends** for
coffee. You know the following about their behavior:

- With probability 20%, they choose coffee house A.
- With probability 80%, they choose coffee house B.

If your goal is to maximise the probability of meeting them, what should you
do?

```{figure} ./images/probabilistic_decision_tree/main.png
:alt: A probabilistic decision tree
:label: fig:probabilistic_decision_tree
:height: 250px

A probabilistic decision tree. A square node is used to indicate a decision and
a circlular node is used to indicate a probailistic event.
```

As illustrated in [Figure 1](#fig:probabilistic_decision_tree), if you must
choose your location without communication, the optimal choice is coffee house
B, offering an 80% chance of meeting your friends.

However, in many situations, decisions are not made in isolation. Often, one
party moves first, and others respond after observing that choice. If you were
able to announce your decision before your friends chose where to go, the
interaction would become a sequential decision problem — an instance of a
**game**. [](#fig:consecutive_decision_tree) shows this game.

```{figure} ./images/consecutive_decision_tree/main.png
:alt: An extensive form game
:label: fig:consecutive_decision_tree
:height: 250px

Visual representation of the consecutive decisions.
```

In such games, outcomes depend not only on chance but critically on the
sequence of actions taken by all players.

## Theory

We now return to the tree diagrams introduced previously. In game theory,
such trees are used to represent a particular type of game known as an
**extensive form game**.

(definition_extensive_form_game)=

### Definition: Extensive Form Game

---

An $N$-player extensive form game **with complete information** consists of:

- A finite set of players $\mathcal{N}$ with $|\mathcal{N}| = N$.
- A tree $G = (V, E, x^0)$ where:
  - $V$ is the set of vertices,
  - $E$ is the set of edges, and
  - $x^0 \in V$ is the root of the tree.
- A partition $(V_i)_{i \in \mathcal{N}}$ of the non-terminal vertices,
  assigning each decision node to a player.
- A set $O$ of possible outcomes.
- A function $u$ mapping each terminal node (leaf) of $G$ to an element of
  $O$.

---

(battle_of_the_sexes)=

### Example: Sequential Coordination Game

Consider the following game, often referred to as the **Battle of the Sexes**.

> Two friends must decide which movie to watch at the cinema.  
> Bob prefers a comedy, while Celine prefers a sports movie.  
> However, both would rather attend the cinema together than go separately.

The structure of the game and the utilities for Bob and Celine are shown in
[](#fig:battle_of_the_sexes_perfect_information_bob_first).

```{figure} ./images/battle_of_the_sexes_perfect_information_bob_first/main.png
:alt: An extensive form game
:label: fig:battle_of_the_sexes_perfect_information_bob_first
:height: 250px

The coordination game with Bob choosing first.
```

If Bob chooses first, the outcome can be predicted as follows:

1. Bob observes that whatever choice he makes, Celine will prefer to follow
   and select the same type of movie.
2. Bob, anticipating this, chooses a comedy to secure the slightly higher
   utility he prefers.

(This reasoning uses a method known as **backward induction**, which we will
formalize later.)

Alternatively, we can model the game with Celine moving first, as shown in
[](#fig:battle_of_the_sexes_perfect_information_celine_first).

```{figure} ./images/battle_of_the_sexes_perfect_information_celine_first/main.png
:alt: An extensive form game
:label: fig:battle_of_the_sexes_perfect_information_celine_first
:height: 250px

The coordination game with Celine choosing first.
```

In this version:

1. Celine observes that whatever choice she makes, Bob will prefer to follow
   and select the same type of movie.
2. Celine, anticipating this, chooses the sports movie to secure her preferred
   outcome.

In both representations, we assume that players have complete information
about previous actions when making their decisions. Specifically, we assume
that the information available at nodes **b** and **c** differs: players know
precisely where they are in the game. This assumption will later be relaxed
when we study games with **imperfect information**.

### Definition: Information Set

---

Given a game in extensive form  
$(\mathcal{N}, G, (V_i)_{i \in \mathcal{N}}, O, u)$,  
the set of information sets $v_i$ for player $i \in \mathcal{N}$ is a partition
of $V_i$.

Each element of $v_i$ denotes a set of nodes at which the player cannot
distinguish their exact location when choosing an action.

---

Two nodes of a game tree are said to belong to the same **information set** if
the player making a decision at that point cannot distinguish between them.

This implies that:

- Every information set contains vertices for a single player.
- All vertices in an information set must have the same number of successors
  (with the same action labels).

We represent nodes that are part of the same information set diagrammatically
by connecting them with a dashed line, as shown in
[](#fig:battle_of_the_sexes_imperfect_information).

In our example involving Celine and Bob, if both players must choose a movie
without knowing the other's choice, nodes **b** and **c** belong to the same
information set.

```{figure} ./images/battle_of_the_sexes_imperfect_information/main.png
:alt: An extensive form game with imperfect information.
:label: fig:battle_of_the_sexes_imperfect_information
:height: 250px

The coordination game with imperfect information.
```

In this case, it becomes significantly more difficult to predict the outcome
of the game.

Another way to represent a game is in **normal form**.

(sec:normal_form_games)=

### Definition: Normal Form Game

---

An $N$-player normal form game consists of:

- A finite set of $N$ players.
- An action set for the players:  
  $\{\mathcal{A}_1, \mathcal{A}_2, \dots, \mathcal{A}_N\}$.
- A set of payoff functions for the players:  
  $u_i : \mathcal{A}_1 \times \mathcal{A}_2 \times \dots \times \mathcal{A}_N 
  \to \mathbb{R}$.

---

Unless otherwise stated, we assume throughout this text that all players act
to maximise their individual payoffs.

#### Bi-Matrix Representation

One common way to represent a two-player normal form game is using a
**bi-matrix**. Suppose that $N = 2$ and the action sets are:  
$\mathcal{A}_1 = \{r_i \mid 1 \leq i \leq m \}$ and  
$\mathcal{A}_2 = \{c_j \mid 1 \leq j \leq n \}$.

A general bi-matrix mapping rows (actions of the first player) and columns
(actions of the second player) to pairs of payoff values:

$$
\Gamma=\begin{pmatrix}
(u_1(r_1,c_1),u_2(r_1,c_1))&(u_1(r_1,c_2),u_2(r_1,c_2))&\dots&(u_1(r_1,c_n),u_2(r_1,c_n))\\
(u_1(r_2,c_1),u_2(r_2,c_1))&(u_1(r_2,c_2),u_2(r_2,c_2))&\dots&(u_1(r_2,c_n),u_2(r_2,c_n))\\
\vdots&\dots&\dots&\vdots\\
(u_1(r_m,c_1),u_2(r_m,c_1))&(u_1(r_m,c_2),u_2(r_m,c_2))&\dots&(u_1(r_m,c_n),u_2(r_m,c_n))\\
\end{pmatrix}
$$

An alternative approach is to use two separate matrices: $M_r$ for the row
player and $M_c$ for the column player, defined as follows:

$$
\label{eqn:payoff_matrices_definition}
(M_r)_{ij} = u_1(r_i, c_j) \qquad (M_c)_{ij} = u_2(r_i, c_j)
$$

This is the preferred representation used in this text.

(sec:coordination_game)=

### Example: Coordination game

See [](#battle_of_the_sexes) for a sequential form
representation. The normal form of this game is defined by the following payoff
matrices for the row and column players:

$$
M_r = \begin{pmatrix}
3 & 0 \\
1 & 2
\end{pmatrix}
\qquad
M_c = \begin{pmatrix}
2 & 0 \\
1 & 3
\end{pmatrix}
$$

---

### Example: Prisoners’ Dilemma

> Two thieves have been caught by the police and separated for questioning.  
> If both cooperate (remain silent), they each receive a short sentence.  
> If one defects (betrays the other), they are offered a deal while the other
> receives a long sentence.  
> If both defect, they both receive a medium-length sentence.

The normal form of this game is represented by:

$$
M_r = \begin{pmatrix}
3 & 0 \\
5 & 1
\end{pmatrix}
\qquad
M_c = \begin{pmatrix}
3 & 5 \\
0 & 1
\end{pmatrix}
$$

---

### Example: Hawk–Dove

> Suppose two birds of prey must share a limited resource.  
> Hawks always fight over the resource — potentially to the death or at great
> cost — and dominate doves.  
> Doves, on the other hand, avoid conflict and share the resource if paired
> with another dove.

This interaction is modelled as:

$$
M_r = \begin{pmatrix}
0 & 3 \\
1 & 2
\end{pmatrix}
\qquad
M_c = \begin{pmatrix}
0 & 1 \\
3 & 2
\end{pmatrix}
$$

---

### Example: Pigs

> Two pigs — one dominant and one subservient — share a pen containing a
> lever that dispenses food.  
> Pressing the lever takes time, giving the other pig an opportunity to eat.  
> If the dominant pig presses the lever, the subservient pig eats most of the
> food before being pushed away.  
> If the subservient pig presses the lever, the dominant pig eats all the food.  
> If both pigs press the lever, the subservient pig manages to eat a third of
> the food.

The game is represented by:

$$
M_r = \begin{pmatrix}
4 & 2 \\
6 & 0
\end{pmatrix}
\qquad
M_c = \begin{pmatrix}
2 & 3 \\
-1 & 0
\end{pmatrix}
$$

(matching_pennies)=

### Example: Matching Pennies

> Two players simultaneously choose to display a coin as either Heads or Tails.  
> If both players show the same face, player 1 wins.  
> If the faces differ, player 2 wins.

This zero-sum game is represented as:

$$
M_r = \begin{pmatrix}
1 & -1 \\
-1 & 1
\end{pmatrix}
\qquad
M_c = \begin{pmatrix}
-1 & 1 \\
1 & -1
\end{pmatrix}
$$

We now discuss how players choose their actions in both normal and extensive
form games.

### Definition: Strategy in Normal Form Games

---

A strategy for a player with action set $\mathcal{A}$ is a probability
distribution over the elements of $\mathcal{A}$.

---

Typically, a strategy is denoted by $\sigma \in [0, 1]^{|\mathcal{A}|}_{\mathbb{R}}$, subject to the condition:

$$
\sum_{i=1}^{|\mathcal{A}|} \sigma_i = 1
$$

Given an action set $\mathcal{A}$ the set of valid strategies is denoted as $\Delta \mathcal{S}$ so that:

$$\left\{\sigma \in [0, 1]^{|\mathcal{A}|}_{\mathbb{R}} \left|\sum_{i=1}^{|\mathcal{A}|} \sigma_i = 1 \right.\right\}$$

In the [Matching Pennies game](#matching_pennies), a strategy profile such as  
$\sigma_1 = (0.2, 0.8)$ and $\sigma_2 = (0.6, 0.4)$ implies that player 1 plays
Heads with probability 0.2, and player 2 plays Heads with probability 0.6.

We can extend the utility function, which maps from action profiles to
$\mathbb{R}$, using **expected utility**. For a two-player game, we write:

$$
\label{eqn:expected_utility}
u_i(\sigma_1, \sigma_2) =
\sum_{a_1 \in \mathcal{A}_1} \sum_{a_2 \in \mathcal{A}_2}
\sigma_1(a_1) \sigma_2(a_2) u_i(a_1, a_2)
$$

Here, we treat $\sigma_i$ as a function $\sigma_i: \mathcal{A}_i \to [0, 1]$
so that $\sigma_i(a_i)$ is the probability of choosing action $a_i \in 
\mathcal{A}_i$.

(sec:example_expected_utility_in_matching_pennies)=

### Example: Expected Utility in Matching Pennies

Using the [Matching Pennies game](#matching_pennies) and the strategy profile  
$\sigma_1 = (0.2, 0.8)$ and $\sigma_2 = (0.6, 0.4)$, the expected utilities are:

$$
u_1(\sigma_1, \sigma_2) =
0.2 \cdot 0.6 \cdot 1 +
0.2 \cdot 0.4 \cdot (-1) +
0.8 \cdot 0.6 \cdot (-1) +
0.8 \cdot 0.4 \cdot 1 = -0.12
$$

$$
u_2(\sigma_1, \sigma_2) =
0.2 \cdot 0.6 \cdot (-1) +
0.2 \cdot 0.4 \cdot 1 +
0.8 \cdot 0.6 \cdot 1 +
0.8 \cdot 0.4 \cdot (-1) = 0.12
$$

Now, suppose player 2 always plays Tails. Then  
$\sigma_2 = (0, 1)$, and if $\sigma_1 = (x, 1 - x)$, we have:

$$
u_1(\sigma_1, \sigma_2) =
x \cdot 0 + (1 - x) \cdot 1 = 1 - 2x
$$

Similarly, if player 1 always plays Tails, and  
$\sigma_2 = (y, 1 - y)$, the expected utility for player 2 is:

$$
u_2(\sigma_1, \sigma_2) =
x \cdot y \cdot (-1) + x \cdot (1 - y) \cdot 1 +
(1 - x) \cdot y \cdot 1 + (1 - x) \cdot (1 - y) \cdot (-1)
$$

If we simplify and assume player 1 always plays Tails, then $x = 0$ and we get:

$$
u_2(\sigma_1, \sigma_2) = y \cdot 1 + (1 - y) \cdot (-1) = 2y - 1
$$

We can visualise both of these expected utility functions below:

```{code-cell} python3
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 100)

plt.figure()
plt.plot(x, 1 - 2 * x, label="$u_1$ (column plays tails)")
plt.plot(x, 2 * x - 1, label="$u_2$ (row plays tails)")
plt.xlabel("Probability of playing Heads")
plt.ylabel("Expected Utility")
plt.legend()
plt.title("Expected Utility vs Strategy");
```

---

### Definition: Strategy in Extensive Form Games

---

A strategy for a player in an
[Extensive Form Game](#definition_extensive_form_game) is a mapping from each
information set to a probability distribution over the available actions at
that set.

---

### Example: Strategies in the Sequential Coordination Game

In the [Sequential Coordination Game](#fig:battle_of_the_sexes_perfect_information_bob_first),
Bob has a single decision node. His strategy can be represented as:

$$
\begin{cases}
a \to (x, 1 - x)
\end{cases}
$$

where $x$ is the probability of choosing "sports".

Celine has two decision nodes, which depend on Bob's choice. Her strategy is:

$$
\begin{cases}
b \to (x_b, 1 - x_b) \\
c \to (x_c, 1 - x_c)
\end{cases}
$$

Here, $x_b$ is the probability of choosing "sports" if Bob chose sports, and
$x_c$ is the probability of choosing sports if Bob chose comedy.

If Celine is unaware of Bob’s decision, as in the  
[coordination game with imperfect information](#fig:battle_of_the_sexes_imperfect_information),
then nodes **b** and **c** form a single information set. Her strategy becomes:

$$
\begin{cases}
\{b, c\} \to (x, 1 - x)
\end{cases}
$$

This leads us to a fundamental idea: **every extensive form game corresponds to
a normal form game**, where strategies describe complete plans of action across
all information sets.

(sec:mapping_extensive_form_games_to_normal_form)=

### Mapping Extensive Form Games to Normal Form

An extensive form game can be mapped to a normal form game by enumerating all
possible strategies that specify a single action at each information set. This
collection of strategies defines the action sets in the corresponding normal
form game.

These strategies can be thought of as vectors in the Cartesian product of the
action sets available at each information set. For a player
$i \in \mathcal{N}$ with information sets
$v_i = ((v_i)_1, (v_i)_2, \dots, (v_i)_n)$, a strategy  
$s = (s_1, s_2, \dots, s_n)$ prescribes one action at each information set.  
For example, $s_2$ specifies the action to take at every vertex contained
within $(v_i)_2$.

### Example: Strategy Enumeration in the Sequential Coordination Game

Consider the  
[Sequential Coordination Game](#fig:battle_of_the_sexes_perfect_information_bob_first).
We enumerate all strategies for each player by listing single actions
taken at each information set.

For Bob, who has a single information set, the list of all strategies in the extensive form game that prescribe a
single action is:

$$
\left\{
\begin{cases}
a \to (1, 0)
\end{cases}
,
\begin{cases}
a \to (0, 1)
\end{cases}
\right\}
$$

These correspond to always choosing **Sports** or always choosing **Comedy**.
The action set in the Normal Form Game is:

$$
\mathcal{A}_1 = \{\text{Sports},\ \text{Comedy}\}
$$

For Celine, who has two information sets (after Bob's move), the pure
strategies in the extensive form are:

$$
\left\{
\begin{cases}
b \to (1, 0) \\
c \to (1, 0)
\end{cases}
,
\begin{cases}
b \to (1, 0) \\
c \to (0, 1)
\end{cases}
,
\begin{cases}
b \to (0, 1) \\
c \to (1, 0)
\end{cases}
,
\begin{cases}
b \to (0, 1) \\
c \to (0, 1)
\end{cases}
\right\}
$$

These strategies describe how Celine responds to each of Bob’s possible
choices. Thinking of these as vectors in the Cartesian product of available
actions at each information set, we can define Celine’s action set in the
Normal Form Game as:

$$
\mathcal{A}_2 = \{
(\text{Sports}, \text{Sports}),\
(\text{Sports}, \text{Comedy}),\
(\text{Comedy}, \text{Sports}),\
(\text{Comedy}, \text{Comedy})
\}
$$

Using these enumerated strategies, the payoff matrices for Bob (the row
player) and Celine (the column player) are:

$$
M_r = \begin{pmatrix}
3 & 3 & 1 & 1 \\
0 & 2 & 0 & 2 \\
\end{pmatrix}
\qquad
M_c = \begin{pmatrix}
2 & 2 & 1 & 1 \\
0 & 3 & 0 & 3 \\
\end{pmatrix}
$$

## Exercises

### Exercise: Structure of a Perfect Information Game

Using the [Sequential Coordination Game](#fig:battle_of_the_sexes_perfect_information_bob_first) and the
[definition of an Extensive Form Game](#definition_extensive_form_game):

1. What is the finite set of players $\mathcal{N}$?
2. What are the elements of the game tree $G = (V, E, x^0)$?
3. What is the partition $(V_i)_{i \in \mathcal{N}}$?
4. What is the set of possible game outcomes $O$?
5. What is the mapping $u$ from every leaf of $G$ to an element of $O$?

---

### Exercise: Structure of an Imperfect Information Game

Using the [Coordination Game with imperfect information](#fig:battle_of_the_sexes_imperfect_information) and the
[definition of an Extensive Form Game](#definition_extensive_form_game):

1. What is the finite set of players $\mathcal{N}$?
2. What are the elements of the game tree $G = (V, E, x^0)$?
3. What is the partition $(V_i)_{i \in \mathcal{N}}$?
4. What is the set of possible game outcomes $O$?
5. What is the mapping $u$ from every leaf of $G$ to an element of $O$?

---

### Exercise: Identifying Information Sets from Game Trees

For each of the following games with $\mathcal{N} = \{\text{Alice},\ \text{Bob}\}$,  
assume that decision nodes $A_i$ belong to Alice and $B_i$ belong to Bob.  
Determine all **information sets**.

1.

```{image} ./images/extensive-form-games/main.png
:alt: Extensive form game
:width: 500px
```

2.

```{image} ./images/extensive-form-games-with-imperfect-information/main.png
:alt: Extensive form game with imperfect information
:width: 500px
```

3.

```{image} ./images/extensive-form-game-example-with-perfect-information/main.png
:alt: Extensive form game example with perfect information
:width: 500px
```

4.

```{image} ./images/extensive-form-game-example-with-imperfect-information/main.png
:alt: Extensive form game example with imperfect information
:width: 500px
```

5.

```{image} ./images/extensive-form-game-incoherent-example-with-imperfect-information/main.png
:alt: Incoherent extensive form game with imperfect information
:width: 500px
```

---

### Exercise: Messaging Platform Coordination

> Alice, Bob, and Celine are childhood friends who want to stay in touch
> online. Each has a choice between three messaging platforms:
> **WhatsApp**, **Instagram**, and **Snapchat**.

- Clearly identify the players and their strategy sets.
- Propose a reasonable interpretation of utility values.
- Write the normal form representation of the game.

---

### Exercise: Peace or War — A Strategic Dilemma

> Two neighbouring countries possess highly destructive military forces.
>
> - If both attack, each suffers **10,000** civilian casualties.
> - If one attacks while the other remains peaceful, the peaceful country suffers
>   **15,000** casualties while the attacker suffers **13,000** in retaliation.
> - If both remain peaceful, there are **no** casualties.

- Clearly state the players and their strategy sets.
- Plot the expected utility to each country assuming it plays a mixed strategy
  while the other remains peaceful.
- Plot the expected utility to each country assuming it plays a mixed strategy
  while the other attacks.

## Programming

(sec:linear_algebraic_formulation_of_expected_utility)=

### Linear Algebraic Form of Expected Utility

The expected utility calculation defined in [](#eqn:expected_utility)
corresponds to a matrix formulation using
linear algebra:

$$
\label{eqn:linear_algebraic_formulation_of_expected_utility}
u_i(\sigma_1, \sigma_2) = \sigma_1 M \sigma_2^T
$$

Here, $M$ is the payoff matrix for player $i$, and $\sigma_1$, $\sigma_2$ are
row and column player strategies, treated as row vectors.

This linear algebraic form will be important in later chapters,
and it also enables **efficient numerical computation** in programming
languages that support vectorized matrix operations.

(sec:using_numpy_for_utility_calculations)=

### Using NumPy to Compute Expected Utilities

Python's numerical library **NumPy** [@harris2020array] provides vectorized operations through
its `array` class. Below, we define the elements from the
[earlier Matching Pennies example](#sec:example_expected_utility_in_matching_pennies):

```{code-cell} python3
import numpy as np

M_r = np.array(
    (
        (1, -1),
        (-1, 1),
    )
)
M_c = -M_r

sigma_r = np.array((0.2, 0.8))
sigma_c = np.array((0.6, 0.4))
```

:::{note}
We use the fact that $M_r = -M_c$ here, which holds because the Matching
Pennies game happens to be a **zero-sum game** — a topic discussed in a later chapter.
% Add reference to zero sum chapter
:::

We can now compute the expected utility for the row player using
[](#eqn:linear_algebraic_formulation_of_expected_utility):

```{code-cell} python3
sigma_r @ M_r @ sigma_c
```

The equivalent calculation for the column player is:

```{code-cell} python3
sigma_r @ M_c @ sigma_c
```

:::{important}
Use `@` for matrix multiplication, not `*`, which performs element-wise
multiplication.
:::

### Using Nashpy to Create Games and Compute Utilities

The Python library **Nashpy** [@knight2018nashpy] is specifically designed for two-player normal form games.
We can use it to create the [Matching Pennies game](#matching_pennies):

```{code-cell} python3
import nashpy as nash

matching_pennies = nash.Game(M_r, M_c)
matching_pennies
```

:::{note}
We reuse `M_r` and `M_c` from [](#sec:using_numpy_for_utility_calculations) and so do not need
to redefine them.
:::

To compute the expected utilities of both players:

```{code-cell} python3
matching_pennies[sigma_r, sigma_c]
```

:::{note}
**Nashpy** is the main Python library used in this text for studying games.
:::

## Notable Research

This chapter has introduced the mathematical foundations needed to define games
and strategic behaviour in interactive decision-making. In later
chapters, we will analyse **emergent behaviour**, a central focus of much
contemporary game theory research.

This section presents a brief overview of selected studies that demonstrate how
game theory is applied across a range of real-world scenarios. We highlight the
types of situations being modelled rather than focusing on technical details.

In [@lee2016devaluing], the authors develop a game-theoretic model of **rhino
horn devaluation**—a conservation strategy in which a rhinoceros's horn is
partially removed to reduce its value to poachers. This work, along with
follow-up research such as [@glynatsi2018evolutionary], explores the conditions
under which poachers are deterred from targeting these endangered animals.

Game theory has also been applied to **healthcare systems**. In
[@knight2017measuring], hospitals are modelled as agents who may strategically
limit bed availability to meet performance targets. A related study,
[@panayides2023game], examines the interaction between hospitals and ambulance
services. Both models use game theory to identify conditions under which
rational decision-making may benefit patients overall.

In a different health-related setting, [@basanta2008studying] presents a
game-theoretic model of **cancer progression**, interpreting the dynamics
between different cell types through the lens of evolutionary games.

In [@jordan2009optimizing], the authors model **play calling in American
Football**. Their framework incorporates factors such as game stage and risk
aversion to identify advantageous strategic decisions in a Normal Form setting.

The study [@kwak2020modeling] constructs a game-theoretic version of the
**Volunteer’s Dilemma**, in which individuals can choose to help or remain
bystanders. The authors formalise this as a general $N$-player Normal Form Game
and investigate how helping behaviour varies with the cost of intervention.

A related dilemma is explored in [@weitz2016oscillating], where the focus shifts
from individual help to shared environmental resources. This model examines how
agent behaviour affects the environment, which in turn feeds back to influence
future strategic choices.

While the above studies are primarily based on **Normal Form Games**,
[@boyd2023generalized] presents a model in **Extensive Form**. The authors
consider a water resource management problem where three firms are located
sequentially along a river basin. The model captures the asymmetric benefits
faced by upstream versus downstream players. The proposed mechanism—a
non-cooperative water-release market—enables upstream agents to release water,
creating a more equitable outcome for all parties.

## Conclusion

In this chapter, we introduced the formal structure of games, focusing on both
**normal form** and **extensive form** representations. [](#tbl:game_summary) shows a comparison of these two forms.
We saw how strategies,
utilities, and information sets define the behaviour of rational agents in
interactive decision-making scenarios.

```{table} The main concepts for Normal Form and Extensive Form Games.
:label: tbl:game_summary
:align: center
:class: table-bordered

| Concept                  | Normal Form Game                              | Extensive Form Game                             |
|--------------------------|-----------------------------------------------|--------------------------------------------------|
| Representation           | Payoff Matrices                               | Game tree                                       |
| Sequence of Moves        | Simultaneous                                  | Sequential (possibly with information sets)     |
| Players                  | $\mathcal{N}$                                 | $\mathcal{N}$                                   |
| Actions                  | $\mathcal{A}_i$ per player                    | Specified at each decision node                             |
| Strategies               | Probability distributions over actions        | Mappings from information sets to probability distributions over actions       |
| Utilities                | $u_i(\vec{a})$ for action profiles            | $u(x)$ for each terminal node                   |
| Information              | Perfect (assumes all actions known at once)   | Can be perfect or imperfect (via information sets) |

```

Through motivating examples, formal definitions, and real-world applications,
we began to see how even simple games can model complex dynamics. From
coordinating with friends to navigating competitive environments, these tools
lay the groundwork for deeper analysis in the chapters to come.

Next, we turn to the study of **emergent behaviour**, where individual
strategies interact in surprising ways across repeated play, populations, or
networks of agents. Understanding these patterns is essential for analysing
systems that evolve over time — and for designing mechanisms that shape them.

---

```{attention}
Every extensive form game has an equivalent representation in normal form,
where strategies specify complete plans of action across all information sets.
```

```

```
