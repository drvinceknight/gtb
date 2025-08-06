---
kernelspec:
  name: python3
  display_name: "Python 3"
---

# Cooperative Games

(motivating_example:dnd_battle)=

## Example: Dividing the loot after a D&D battle

After a climactic boss fight, a party of adventurers must divide a hoard of  
1,000 gold coins recovered after fighting a dragon.

> The party includes:
>
> - **Ren** the fighter, who absorbed the dragon’s attacks.
> - **Azel** the wizard, who cast a decisive spell at the turning point.
> - **Quinn** the bard, who provided support and distracted the dragon  
>   with an improvised limerick.

Each character played a crucial role, but in very different ways. How can they  
divide the treasure fairly?

Based on past encounters, the party has a sense of how much gold they might  
have secured without the full team:

- $\{\text{Ren}\} = 0$ (they can’t get past the dragon alone)
- $\{\text{Azel}\} = 0$ (powerful spells, but too vulnerable on their own)
- $\{\text{Quinn}\} = 0$ (charming, but not a serious threat)
- $\{\text{Ren}, \text{Azel}\} = 900$ (they can defeat the dragon, but with great effort)
- $\{\text{Ren}, \text{Quinn}\} = 400$ (they can stall the dragon,  
  but not defeat it)
- $\{\text{Azel}, \text{Quinn}\} = 600$ (Azel can burn the dragon while  
  Quinn keeps it distracted)
- $\{\text{Ren}, \text{Azel}, \text{Quinn}\} = 1000$ (the full party defeats  
  the dragon smoothly and decisively)

This is a classic example of a **cooperative game**, and understanding how to  
allocate resources fairly in such settings is the focus of this chapter.

## Theory

### Definition: characteristic function game

A **characteristic function game** $G$ is given by a pair  
$(N, v)$ where $N$ is the number of players and  
$v: 2^{[N]} \to \mathbb{R}$ is a **characteristic function** which  
maps every coalition of players to a payoff.

### Example: The characteristic function game of the D&D battle

For [the D&D battle](#motivating_example:dnd_battle), we have $N = 3$ and the  
characteristic function $v$ is given by:

$$
\label{eqn:dnd_characteristic_function}
v(c) =
\begin{cases}
0 & \text{if } c = \emptyset \\
0 & \text{if } c = \{\text{Ren}\} \\
0 & \text{if } c = \{\text{Azel}\} \\
0 & \text{if } c = \{\text{Quinn}\} \\
900 & \text{if } c = \{\text{Ren}, \text{Azel}\} \\
400 & \text{if } c = \{\text{Ren}, \text{Quinn}\} \\
600 & \text{if } c = \{\text{Azel}, \text{Quinn}\} \\
1000 & \text{if } c = \{\text{Ren}, \text{Azel}, \text{Quinn}\}
\end{cases}
$$

(sec:definition_of_monotone_characteristic_function)=

### Definition: Monotone characteristic function game

---

A characteristic function game $G = (N, v)$ is called **monotone** if it satisfies  
$v(C_2) \geq v(C_1)$ for all $C_1 \subseteq C_2$.

---

### Example: The D&D battle is a monotone characteristic function game

The function defined in [](#eqn:dnd_characteristic_function) is monotone.  
However, the following game is not:

$$
\label{eqn:none_monotone_characteristic_function_game}
v(c) =
\begin{cases}
0 & \text{if } c = \emptyset \\
0 & \text{if } c = \{\text{Ren}\} \\
0 & \text{if } c = \{\text{Azel}\} \\
0 & \text{if } c = \{\text{Quinn}\} \\
1100 & \text{if } c = \{\text{Ren}, \text{Azel}\} \\
400 & \text{if } c = \{\text{Ren}, \text{Quinn}\} \\
600 & \text{if } c = \{\text{Azel}, \text{Quinn}\} \\
1000 & \text{if } c = \{\text{Ren}, \text{Azel}, \text{Quinn}\}
\end{cases}
$$

Indeed, Ren and Azel receive more **without** Quinn than with them, violating monotonicity.

(sec:definition_of_superadditive_characteristic_function)=

### Definition: superadditive characteristic function game

A characteristic function game $G = (N, v)$ is called **superadditive** if it satisfies  
$v(C_1 \cup C_2) \geq v(C_1) + v(C_2)$ for all disjoint coalitions  
$C_1 \cap C_2 = \emptyset$.

---

### Example: The D&D battle is not a superadditive characteristic function game

The function defined in [](#eqn:dnd_characteristic_function) is superadditive.  
However, the following game is not:

$$
\label{eqn:none_superadditive_characteristic_function_game}
v(c) =
\begin{cases}
0 & \text{if } c = \emptyset \\
0 & \text{if } c = \{\text{Ren}\} \\
700 & \text{if } c = \{\text{Azel}\} \\
0 & \text{if } c = \{\text{Quinn}\} \\
900 & \text{if } c = \{\text{Ren}, \text{Azel}\} \\
400 & \text{if } c = \{\text{Ren}, \text{Quinn}\} \\
600 & \text{if } c = \{\text{Azel}, \text{Quinn}\} \\
1000 & \text{if } c = \{\text{Ren}, \text{Azel}, \text{Quinn}\}
\end{cases}
$$

Indeed:

$$v(\{\text{Ren}, \text{Quinn}\}) + v(\{\text{Azel}\}) = 400 + 700 = 1100 > 1000 = v(\{\text{Ren}, \text{Azel}, \text{Quinn}\})$$

so the game violates superadditivity.

### Definition: Payoff vector

When we talk about a solution to a characteristic function game, we mean a  
payoff vector $\lambda \in \mathbb{R}_{\geq 0}^N$ that allocates the value of  
the grand coalition among the players. In particular, $\lambda$ must satisfy:

$$
\sum_{i=1}^N \lambda_i = v(\Omega)
$$

### Example: A possible payoff vector:

One possible payoff vector for [](#eqn:dnd_characteristic_function) is:

$$
\label{eqn:efficient_payoff_vector}
\lambda = (200, 350, 450)
$$

This would seem unfair as Quinn gets 450 of the gold.
To find a "fair" distribution of the grand coalition we must
define what is meant by "fair". We require four desirable properties:

- Efficiency;
- Null player;
- Symmetry;
- Additivity.

### Definition: Efficiency

---

Given a game $G = (N, v)$, a payoff vector $\lambda$ is **efficient** if:

$$
\sum_{i=1}^N \lambda_i = v(\Omega)
$$

### Example: An efficient Payoff Vector for the D&D Battle

An efficient payoff vector is one that shares all 1,000 gold coins like the one
in [](#eqn:efficient_payoff_vector).

---

### Definition: Null Player Property

---

Given a game $G = (N, v)$, a payoff vector $\lambda$ satisfies the **null player property** if, for a player $i$:

If $v(C \cup i) = v(C)$ for all coalitions $C \subseteq \Omega$, then:

$$
\lambda_i = 0
$$

### Example: The Null Player Property in the D&D Battle

In [](#motivating_example:dnd_battle), Quinn contributes very little, yet still
adds value to each coalition he joins. For instance, without Quinn, the grand
coalition would only obtain 900 coins. If, however, a member of the party made
no difference to the value of any coalition, the null player property dictates
that this player should receive a payoff of 0.

---

### Definition: Symmetry Property

---

Given a game $G = (N, v)$, a payoff vector $\lambda$ satisfies the **symmetry property** if, for any pair of players $i, j$:

If $v(C \cup i) = v(C \cup j)$ for all coalitions $C \subseteq \Omega \setminus \{i, j\}$, then:

$$
\lambda_i = \lambda_j
$$

---

### Example: The Symmetry Property in the D&D Battle

In [](#motivating_example:dnd_battle), no two players contribute equally to
every coalition they join. If there were such players, the symmetry property
would guarantee that they each receive an equal share of the gold

### Definition: Additivity Property

---

Given two games $G_1 = (N, v_1)$ and $G_2 = (N, v_2)$, define their sum $G^+ = (N, v^+)$ by:

$$
v^+(C) = v_1(C) + v_2(C) \quad \text{for all } C \subseteq \Omega
$$

A payoff vector $\lambda$ satisfies the **additivity property** if:

$$
\lambda_i^{(G^+)} = \lambda_i^{(G_1)} + \lambda_i^{(G_2)}
$$

---

### Example: The Additive Property in the D&D Battle

In [](#motivating_example:dnd_battle), if there were in fact two separate battles,
the method for distributing the gold should  
yield the same result as treating both battles as a single event with the  
combined total reward.

### Definition: Predecessors

---

Given a permutation $\pi$ of $[N]$, the set of **predecessors** of player $i$ in $\pi$
is denoted by $S_pi(i)$ and defined as:

$$
S_\pi(i)=\{j \in [N] \mid \pi(j)<\pi(i)\}
$$

---

### Example: The predecessors for the D&D Battle

For [](#motivating_example:dnd_battle) we have $N=3$ if we assume the ordering:
$(\text{Ren}, \text{Azel}, \text{Quinn})$
[](#tbl:predecessors_for_dnd_game) gives the predecessors of each individual for
each of the $3!=6$ permutations of $[N]$.

```{table} The predecessors of each individual for each permutation
:label: tbl:predecessors_for_dnd_game
:align: center
:class: table-bordered

| $\pi$       | $S_{\pi}(1)$ (Predecessors of Ren) | $S_{\pi}(2)$ (Predecessors of Azel) | $S_{\pi}(3)$ (Predecessors of Quinn) |
|-------------|------------------------------------|-------------------------------------|-------------------------------------|
| $(1, 2, 3)$ | $\emptyset$                        | $\{1\}$                             | $\{1, 2\}$                          |
| $(1, 3, 2)$ | $\emptyset$                        | $\{1, 3\}$                          | $\{1\}$                             |
| $(2, 1, 3)$ | $\{2\}$                            | $\emptyset$                         | $\{1, 2\}$                          |
| $(2, 3, 1)$ | $\{2, 3\}$                         | $\emptyset$                         | $\{2\}$                             |
| $(3, 1, 2)$ | $\{3\}$                            | $\{1, 3\}$                          | $\emptyset$                         |
| $(3, 2, 1)$ | $\{2, 3\}$                         | $\{3\}$                             | $\emptyset$                         |

```

```{note}
Here we are using the indices of the players for ease of notation where $1$
corresponds to the first individual (Ren), $2$ corresponds to the second
individual (Azel) and $3$ corresponds to the third individual $Quinn$.
```

### Definition: Marginal Contribution

---

Given a permutation $\pi$ of $[N]$, the **marginal contribution** of player
$i$ with respect to $\pi$ is defined as:

$$
\Delta_\pi^G(i)=v(S_{\pi}(i)\cup \{i\})-v(S_{\pi}(i))
$$

---

### Example: Marginal Contributions in the D&D Battle

For [](#motivating_example:dnd_battle) $(\text{Ren}, \text{Azel}, \text{Quinn})$, with $N = 3$.
[](#tbl:marginal_contributions_dnd) shows the marginal contribution $\Delta_\pi^G(i)$ for each player
$i$ in each permutation $\pi$ using [](#eqn:dnd_characteristic_function).

```{table} Marginal contributions of each individual for each permutation
:label: tbl:marginal_contributions_dnd
:align: center
:class: table-bordered

| $\pi$       | $\Delta_\pi^G(1)$ (Ren) | $\Delta_\pi^G(2)$ (Azel) | $\Delta_\pi^G(3)$ (Quinn) |
|-------------|-------------------------|--------------------------|---------------------------|
| $(1, 2, 3)$ | $0$                     | $900$                     | $100$                     |
| $(1, 3, 2)$ | $0$                     | $600$                    | $400$                     |
| $(2, 1, 3)$ | $900$                   | $0$                      | $100$                     |
| $(2, 3, 1)$ | $400$                   | $0$                      | $600$                     |
| $(3, 1, 2)$ | $400$                   | $600$                    | $0$                     |
| $(3, 2, 1)$ | $400$                   | $600$                    | $0$                     |

```

We are now ready to define the **Shapley value** for any cooperative game $G=(N,v)$.

### Definition: Shapley Value

---

Given a cooperative game $G=(N,v)$, the **Shapley value** of player $i$
is denoted by $\phi_i(G)$ and defined as:

$$
\phi_i(G)=\frac{1}{N!}\sum_{\pi\in\Pi_n}\Delta_\pi^G(i)
$$

---

### Example: The Shapley Value for the D&D Battle

For [](#motivating_example:dnd_battle) the Shapley value is the vector with
entries corresponding to the average of each of the columnts of
[](#tbl:marginal_contributions_dnd).

$$
\begin{align*}
\phi_1 &= \frac{0 + 0 + 900 + 400 + 400 + 400}{6} = 350\\
\phi_2 &= \frac{900 + 600 + 0 + 0 + 400 + 600}{6} = 450\\
\phi_3 &= \frac{100 + 400 + 100 + 600 + 0 + 0}{6} = 200\\
\end{align*}
$$

Giving: $\phi=(350, 450, 200)$

## Exercises

### Exercise: Shapley Value Computation and Properties

For the following cooperative games:

1. Verify whether the game is monotonic.
2. Verify whether the game is superadditive.
3. Obtain the Shapley value.

$$
v_1(C)=\begin{cases}
5,&\text{if }C=\{1\}\\
3,&\text{if }C=\{2\}\\
2,&\text{if }C=\{3\}\\
12,&\text{if }C=\{1,2\}\\
5,&\text{if }C=\{1,3\}\\
4,&\text{if }C=\{2,3\}\\
13,&\text{if }C=\{1,2,3\}
\end{cases}
$$

$$
v_2(C)=\begin{cases}
6,&\text{if }C=\{1\}\\
0,&\text{if }C=\{2\}\\
5,&\text{if }C=\{1,2\}
\end{cases}
$$

$$
v_3(C)=\begin{cases}
6,&\text{if }C=\{1\}\\
6,&\text{if }C=\{2\}\\
13,&\text{if }C=\{3\}\\
6,&\text{if }C=\{1,2\}\\
13,&\text{if }C=\{1,3\}\\
13,&\text{if }C=\{2,3\}\\
26,&\text{if }C=\{1,2,3\}
\end{cases}
$$

$$
v_4(C)=\begin{cases}
6,&\text{if }C=\{1\}\\
7,&\text{if }C=\{2\}\\
0,&\text{if }C=\{3\}\\
8,&\text{if }C=\{4\}\\
7,&\text{if }C=\{1,2\}\\
6,&\text{if }C=\{1,3\}\\
12,&\text{if }C=\{1,4\}\\
7,&\text{if }C=\{2,3\}\\
12,&\text{if }C=\{2,4\}\\
8,&\text{if }C=\{3,4\}\\
7,&\text{if }C=\{1,2,3\}\\
24,&\text{if }C=\{1,2,4\}\\
12,&\text{if }C=\{1,3,4\}\\
12,&\text{if }C=\{2,3,4\}\\
25,&\text{if }C=\{1,2,3,4\}
\end{cases}
$$

(exercise:interpreting_linear_models)=

### Exercise: Interpreting linear model performance with the Shapley value

In statistics and machine learning, a **linear model** predicts a target
variable $y$ as a weighted sum of input features $x_1, x_2, \dots, x_n$.
The **coefficient of determination**, denoted $R^2$, measures how well the model
explains the variance in the data. It takes values between 0 and 1, with higher
values indicating better explanatory power.

In cooperative game theory, a **characteristic function** maps every coalition
(subset of players) to a value. In this exercise, we will interpret each feature
as a player, and define the value of a coalition to be the $R^2$ of the model
trained on those features.

Suppose we are predicting a target variable $y$ using a linear model:

$$
y = c_1 x_1 + c_2 x_2 + c_3 x_3
$$

Below are the $R^2$ values obtained from fitting models to different subsets of
the features. These were generated using synthetic data (you can refer to
:download:`main.py </_static/data-for-shapley-regression-tutorial/main.py>` for the code).

| Model                                         | $R^2$ |
| --------------------------------------------- | ----- |
| $y = c_1 x_1$                                 | 0.122 |
| $y = \phantom{c_1 x_1 +{}} c_2 x_2$           | 0.097 |
| $y = \phantom{c_1 x_1 + c_2 x_2 +{}} c_3 x_3$ | 0.551 |
| $y = c_1 x_1 + c_2 x_2$                       | 0.174 |
| $y = c_1 x_1 + c_3 x_3$                       | 0.581 |
| $y = c_2 x_2 + c_3 x_3$                       | 0.620 |
| $y = c_1 x_1 + c_2 x_2 + c_3 x_3$             | 0.623 |

1. Define the characteristic function $v(S)$ for each subset of
   $\{x_1, x_2, x_3\}$ using the table above.

2. Compute the Shapley value for each feature with respect to the
   characteristic function $v$.

3. Interpret the result: Which feature contributes the most explanatory power?
   Which contributes the least?

### Exercise: Additivity and Symmetry

Consider the following two cooperative games defined on $N=\{1,2,3\}$:

**Game $v_a$:**

$$
v_a(C)=\begin{cases}
2, &\text{if }C=\{1\}\\
2, &\text{if }C=\{2\}\\
0, &\text{otherwise}
\end{cases}
$$

**Game $v_b$:**

$$
v_b(C)=\begin{cases}
1, &\text{if }C=\{1,3\}\\
1, &\text{if }C=\{2,3\}\\
3, &\text{if }C=\{1,2,3\}\\
0, &\text{otherwise}
\end{cases}
$$

1. Verify that both games satisfy the symmetry property.
2. Obtain the Shapley value for $v_a$ and $v_b$ individually.
3. Construct the game $(v_a + v_b)$ and calculate the Shapley value.
4. Verify that the Shapley value of $(v_a + v_b)$ equals the sum of the Shapley values of $v_a$ and $v_b$.

### Exercise: Null Player and Marginal Contributions

Consider the cooperative game $v$ defined on $N=\{1,2,3\}$:

$$
v(C)=\begin{cases}
4, &\text{if }C=\{1\}\\
7, &\text{if }C=\{1,2\}\\
7, &\text{if }C=\{1,2,3\}\\
0, &\text{otherwise}
\end{cases}
$$

1. Identify any null players in this game.
2. Compute the marginal contributions of each player.
3. Calculate the Shapley value and confirm it respects the null player property.

### Exercise: Properties of the Shapley Value

Prove that the Shapley value satisfies the following properties:

- Efficiency
- Null player property
- Symmetry
- Additivity

Note that this does not prove uniqueness; that is, other vectors might satisfy these properties
(though in fact, the Shapley value is uniquely defined by them).

## Programming

The CoopGT library has functionality to verify properties of a characteristic
function game and also compute the Shapley value.

Here let us define a characteristic function and check if it is valid:

```{code-cell} python3
import coopgt.characteristic_function_properties


characteristic_function = {
    (): 0,
    (1,): 0,
    (2,): 0,
    (3,): 0,
    (1, 2): 900,
    (1,3): 400,
    (2, 3): 600,
    (1, 2, 3): 1000,
}
coopgt.characteristic_function_properties.is_valid(characteristic_function=characteristic_function)
```

Here we can check if it is [monotone](#sec:definition_of_monotone_characteristic_function):

```{code-cell} python3
coopgt.characteristic_function_properties.is_monotone(
    characteristic_function=characteristic_function
)
```

Here we can check if it is
[supperadditive](#sec:definition_of_superadditive_characteristic_function):

```{code-cell} python3
coopgt.characteristic_function_properties.is_superadditive(
    characteristic_function=characteristic_function
)
```

Let us compute the Shapley value:

```{code-cell} python3
import coopgt.shapley_value

coopgt.shapley_value.calculate(characteristic_function=characteristic_function)
```

## Notable Research

The Shapley value was first introduced by Shapley in [@shapley1953value], a
foundational paper in cooperative game theory. Although Shapley is best known
for this concept, he was awarded the Nobel Prize in Economics for his later
work on [matching games](#chp:matching_games).

In large games, the computational cost of calculating the Shapley value can be
prohibitive. While not necessarily intractable in the formal sense, as shown in
[@deng1994complexity], the number of permutations makes exact computation
impractical. One of the earliest practical approaches to this challenge is
[@castro2009polynomial], which proposes Monte Carlo sampling of permutations as
an efficient approximation method.

One of the most impactful application areas of the Shapley value in recent years
has been in **model explainability**. As explored in
[#exercise:interpreting_linear_models](#exercise:interpreting_linear_models),
the Shapley value provides a principled way to attribute a model’s output to its
input features. One of the first papers to formalize this idea was
[@strumbelj2010efficient]. This approach has since seen wide application,
particularly in healthcare, where a comprehensive overview is provided in
[@jin2022explainable].

## Conclusion

In this chapter, we introduced the theory of **cooperative games**, where groups
of players can form coalitions and share the resulting value. We focused on
**characteristic function games**, where the value of each coalition is known,
and explored how to fairly distribute this value using the **Shapley value**.

We discussed the key axioms that characterize fairness—efficiency, null player,
symmetry, and additivity and saw how they uniquely determine the Shapley value.
We also explored computational aspects, applications to machine learning, and
interactive programming tools to calculate Shapley values.

[](#tbl:cooperative_games_summary) gives a summary of the concepts of this
chapter.

```{table} Summary of cooperative game concepts
:label: tbl:cooperative_games_summary
:align: center
:class: table-bordered

| Concept                      | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| Characteristic function      | Maps each subset (coalition) of players to a real-valued payoff             |
| Monotonicity                 | Adding players to a coalition cannot decrease its value                     |
| Superadditivity              | The value of two disjoint coalitions is at most the value of their union    |
| Payoff vector                | A distribution of the total value among all players                         |
| Marginal contribution        | The added value a player brings to a coalition                              |
| Predecessors in permutation | Players who appear before a given player in a permutation                   |
| Shapley value                | The average marginal contribution: a unique, fair payoff satisfying four axioms                                |
```

```{important}
The Shapley value is the only payoff rule that satisfies **efficiency**, **null
player**, **symmetry**, and **additivity**—making it a principled way to fairly
divide rewards in cooperative settings.
```
