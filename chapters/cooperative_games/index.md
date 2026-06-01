---
kernelspec:
  name: python3
  display_name: "Python 3"
---

(chp:cooperative_games)=

# Cooperative Games

When players can form coalitions and make binding agreements, the key question
shifts from what strategy to play to how to share the resulting surplus fairly.
This chapter studies cooperative games through the characteristic function and
develops the Shapley value as a principled allocation scheme.

(motivating_example:dnd_battle)=

## Motivating Example: Dividing the loot after a D&D battle

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

#### Example: The characteristic function game of the D&D battle

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

#### Example: The D&D battle is a monotone characteristic function game

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

#### Example: The D&D battle is not a superadditive characteristic function game

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

#### Example: A possible payoff vector:

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

#### Example: An efficient Payoff Vector for the D&D Battle

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

#### Example: The Null Player Property in the D&D Battle

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

#### Example: The Symmetry Property in the D&D Battle

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

#### Example: The Additive Property in the D&D Battle

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

#### Example: The predecessors for the D&D Battle

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

#### Example: Marginal Contributions in the D&D Battle

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

#### Example: The Shapley Value for the D&D Battle

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

```{exercise} 
:label: shapley-value-computation-and-properties

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
```

```{exercise} 
:label: interpreting_linear_models

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
the features. These were generated using synthetic data.

| Model                                         | $R^2$ |
| --------------------------------------------- | ----- |
| $y = c_1 x_1$                                 | 0.122 |
| $y = c_2 x_2$           | 0.097 |
| $y = c_3 x_3$ | 0.551 |
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
```

```{exercise} 
:label: additivity-and-symmetry

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
```

```{exercise} 
:label: null-player-and-marginal-contributions

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
```

```{exercise} 
:label: properties-of-the-shapley-value

Prove that the Shapley value satisfies the following properties:

- Efficiency
- Null player property
- Symmetry
- Additivity

Note that this does not prove uniqueness; that is, other vectors might satisfy these properties
(though in fact, the Shapley value is uniquely defined by them).
```

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
is_valid = coopgt.characteristic_function_properties.is_valid(
    characteristic_function=characteristic_function
)
print(f"Characteristic function valid? {is_valid}")
```

Here we can check if it is [monotone](#sec:definition_of_monotone_characteristic_function):

```{code-cell} python3
is_monotone = coopgt.characteristic_function_properties.is_monotone(
    characteristic_function=characteristic_function
)
print(f"Characteristic function monotone? {is_monotone}")
```

Here we can check if it is
[supperadditive](#sec:definition_of_superadditive_characteristic_function):

```{code-cell} python3
is_superadditive = coopgt.characteristic_function_properties.is_superadditive(
    characteristic_function=characteristic_function
)
print(f"Characteristic function superadditive? {is_superadditive}")
```

Let us compute the Shapley value:

```{code-cell} python3
import coopgt.shapley_value

shapley_value = coopgt.shapley_value.calculate(
    characteristic_function=characteristic_function
)
print(f"Shapley value: {shapley_value}")
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
[](#interpreting_linear_models),
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

The four axioms (efficiency, null player, symmetry, and additivity) uniquely determine the Shapley value. We also saw applications to machine learning interpretability.

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
player**, **symmetry**, and **additivity**, making it a principled way to fairly
divide rewards in cooperative settings.
```

---

(solutions:cooperative_games)=

## Solutions

````{solution} shapley-value-computation-and-properties
:label: solution:shapley-value-computation-and-properties

**Game $v_1$**

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

1. **Monotonicity of $v_1$**: We must check $v(C_1)\leq v(C_2)$ for all $C_1\subseteq C_2$. All singleton-to-pair comparisons:

   - $v_1(\{1\})=5\leq 12=v_1(\{1,2\})$ ✓
   - $v_1(\{1\})=5\leq 5=v_1(\{1,3\})$ ✓
   - $v_1(\{2\})=3\leq 12=v_1(\{1,2\})$ ✓
   - $v_1(\{2\})=3\leq 4=v_1(\{2,3\})$ ✓
   - $v_1(\{3\})=2\leq 5=v_1(\{1,3\})$ ✓
   - $v_1(\{3\})=2\leq 4=v_1(\{2,3\})$ ✓

   All pair-to-grand-coalition comparisons:

   - $v_1(\{1,2\})=12\leq 13=v_1(\{1,2,3\})$ ✓
   - $v_1(\{1,3\})=5\leq 13=v_1(\{1,2,3\})$ ✓
   - $v_1(\{2,3\})=4\leq 13=v_1(\{1,2,3\})$ ✓

   **$v_1$ is monotone.**

2. **Superadditivity of $v_1$**: We check $v(C_1\cup C_2)\geq v(C_1)+v(C_2)$ for all disjoint $C_1,C_2$.

   - $v_1(\{1,2\})\geq v_1(\{1\})+v_1(\{2\})$: $12\geq 5+3=8$ ✓
   - $v_1(\{1,3\})\geq v_1(\{1\})+v_1(\{3\})$: $5\geq 5+2=7$? No: $5 < 7$.

   **$v_1$ is not superadditive** (coalition $\{1,3\}$ is worth less than the sum of the individual values of players 1 and 3).

3. **Shapley value of $v_1$**: We enumerate all $3!=6$ permutations and compute marginal contributions.

   | $\pi$ | $\Delta^{v_1}_\pi(1)$ | $\Delta^{v_1}_\pi(2)$ | $\Delta^{v_1}_\pi(3)$ |
   |---|---|---|---|
   | $(1,2,3)$ | $v_1(\{1\})-v_1(\emptyset)=5$ | $v_1(\{1,2\})-v_1(\{1\})=7$ | $v_1(\{1,2,3\})-v_1(\{1,2\})=1$ |
   | $(1,3,2)$ | $5$ | $v_1(\{1,2,3\})-v_1(\{1,3\})=8$ | $v_1(\{1,3\})-v_1(\{1\})=0$ |
   | $(2,1,3)$ | $v_1(\{1,2\})-v_1(\{2\})=9$ | $3$ | $v_1(\{1,2,3\})-v_1(\{1,2\})=1$ |
   | $(2,3,1)$ | $v_1(\{1,2,3\})-v_1(\{2,3\})=9$ | $3$ | $v_1(\{2,3\})-v_1(\{2\})=1$ |
   | $(3,1,2)$ | $v_1(\{1,3\})-v_1(\{3\})=3$ | $v_1(\{1,2,3\})-v_1(\{1,3\})=8$ | $2$ |
   | $(3,2,1)$ | $v_1(\{1,2,3\})-v_1(\{2,3\})=9$ | $v_1(\{2,3\})-v_1(\{3\})=2$ | $2$ |

   $$
   \phi_1(v_1)=\frac{5+5+9+9+3+9}{6}=\frac{40}{6}=\frac{20}{3}\approx 6.67
   $$

   $$
   \phi_2(v_1)=\frac{7+8+3+3+8+2}{6}=\frac{31}{6}\approx 5.17
   $$

   $$
   \phi_3(v_1)=\frac{1+0+1+1+2+2}{6}=\frac{7}{6}\approx 1.17
   $$

   **Check**: $\phi_1+\phi_2+\phi_3=20/3+31/6+7/6=40/6+31/6+7/6=78/6=13=v_1(\{1,2,3\})$ ✓

---

**Game $v_2$**

$$
v_2(C)=\begin{cases}
6,&\text{if }C=\{1\}\\
0,&\text{if }C=\{2\}\\
5,&\text{if }C=\{1,2\}
\end{cases}
$$

This is a two-player game with $N=2$.

1. **Monotonicity of $v_2$**:

   - $v_2(\{1\})=6\leq 5=v_2(\{1,2\})$? No: $6>5$.

   **$v_2$ is not monotone.**

2. **Superadditivity of $v_2$**:

   - $v_2(\{1,2\})\geq v_2(\{1\})+v_2(\{2\})$: $5\geq 6+0=6$? No: $5<6$.

   **$v_2$ is not superadditive.**

3. **Shapley value of $v_2$**: With $N=2$ there are $2!=2$ permutations.

   | $\pi$ | $\Delta^{v_2}_\pi(1)$ | $\Delta^{v_2}_\pi(2)$ |
   |---|---|---|
   | $(1,2)$ | $v_2(\{1\})-v_2(\emptyset)=6$ | $v_2(\{1,2\})-v_2(\{1\})=-1$ |
   | $(2,1)$ | $v_2(\{1,2\})-v_2(\{2\})=5$ | $v_2(\{2\})-v_2(\emptyset)=0$ |

   $$
   \phi_1(v_2)=\frac{6+5}{2}=\frac{11}{2}=5.5
   $$

   $$
   \phi_2(v_2)=\frac{-1+0}{2}=-\frac{1}{2}=-0.5
   $$

   **Check**: $5.5+(-0.5)=5=v_2(\{1,2\})$ ✓

---

**Game $v_3$**

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

1. **Monotonicity of $v_3$**:

   - $v_3(\{1\})=6\leq 6=v_3(\{1,2\})$ ✓
   - $v_3(\{2\})=6\leq 6=v_3(\{1,2\})$ ✓
   - $v_3(\{1\})=6\leq 13=v_3(\{1,3\})$ ✓
   - $v_3(\{3\})=13\leq 13=v_3(\{1,3\})$ ✓
   - $v_3(\{2\})=6\leq 13=v_3(\{2,3\})$ ✓
   - $v_3(\{3\})=13\leq 13=v_3(\{2,3\})$ ✓
   - $v_3(\{1,2\})=6\leq 26=v_3(\{1,2,3\})$ ✓
   - $v_3(\{1,3\})=13\leq 26=v_3(\{1,2,3\})$ ✓
   - $v_3(\{2,3\})=13\leq 26=v_3(\{1,2,3\})$ ✓

   **$v_3$ is monotone.**

2. **Superadditivity of $v_3$**:

   - $v_3(\{1,2\})\geq v_3(\{1\})+v_3(\{2\})$: $6\geq 6+6=12$? No: $6<12$.

   **$v_3$ is not superadditive.**

3. **Shapley value of $v_3$**:

   | $\pi$ | $\Delta^{v_3}_\pi(1)$ | $\Delta^{v_3}_\pi(2)$ | $\Delta^{v_3}_\pi(3)$ |
   |---|---|---|---|
   | $(1,2,3)$ | $6$ | $v_3(\{1,2\})-v_3(\{1\})=0$ | $v_3(\{1,2,3\})-v_3(\{1,2\})=20$ |
   | $(1,3,2)$ | $6$ | $v_3(\{1,2,3\})-v_3(\{1,3\})=13$ | $v_3(\{1,3\})-v_3(\{1\})=7$ |
   | $(2,1,3)$ | $v_3(\{1,2\})-v_3(\{2\})=0$ | $6$ | $v_3(\{1,2,3\})-v_3(\{1,2\})=20$ |
   | $(2,3,1)$ | $v_3(\{1,2,3\})-v_3(\{2,3\})=13$ | $6$ | $v_3(\{2,3\})-v_3(\{2\})=7$ |
   | $(3,1,2)$ | $v_3(\{1,3\})-v_3(\{3\})=0$ | $v_3(\{1,2,3\})-v_3(\{1,3\})=13$ | $13$ |
   | $(3,2,1)$ | $v_3(\{1,2,3\})-v_3(\{2,3\})=13$ | $v_3(\{2,3\})-v_3(\{3\})=0$ | $13$ |

   $$
   \phi_1(v_3)=\frac{6+6+0+13+0+13}{6}=\frac{38}{6}=\frac{19}{3}\approx 6.33
   $$

   $$
   \phi_2(v_3)=\frac{0+13+6+6+13+0}{6}=\frac{38}{6}=\frac{19}{3}\approx 6.33
   $$

   $$
   \phi_3(v_3)=\frac{20+7+20+7+13+13}{6}=\frac{80}{6}=\frac{40}{3}\approx 13.33
   $$

   **Check**: $19/3+19/3+40/3=78/3=26=v_3(\{1,2,3\})$ ✓

   Note that $\phi_1=\phi_2$, which is consistent with the symmetry of $v_3$ (players 1 and 2 contribute identically to every coalition).

---

**Game $v_4$**

$$
v_4(C)=\begin{cases}
6,&C=\{1\}\\7,&C=\{2\}\\0,&C=\{3\}\\8,&C=\{4\}\\
7,&C=\{1,2\}\\6,&C=\{1,3\}\\12,&C=\{1,4\}\\
7,&C=\{2,3\}\\12,&C=\{2,4\}\\8,&C=\{3,4\}\\
7,&C=\{1,2,3\}\\24,&C=\{1,2,4\}\\12,&C=\{1,3,4\}\\12,&C=\{2,3,4\}\\
25,&C=\{1,2,3,4\}
\end{cases}
$$

1. **Monotonicity of $v_4$**: We check a few key comparisons.

   - $v_4(\{1\})=6\leq 7=v_4(\{1,2\})$ ✓
   - $v_4(\{2\})=7\leq 7=v_4(\{1,2\})$ ✓
   - $v_4(\{1,2\})=7\leq 7=v_4(\{1,2,3\})$ ✓
   - $v_4(\{1,2,3\})=7\leq 25=v_4(\{1,2,3,4\})$ ✓
   - $v_4(\{3\})=0\leq 6=v_4(\{1,3\})$ ✓
   - $v_4(\{1,2,4\})=24\leq 25=v_4(\{1,2,3,4\})$ ✓

   All subset relationships hold. **$v_4$ is monotone.**

2. **Superadditivity of $v_4$**: Check a few disjoint pairs.

   - $v_4(\{1,2\})\geq v_4(\{1\})+v_4(\{2\})$: $7\geq 6+7=13$? No: $7<13$.

   **$v_4$ is not superadditive.**

3. **Shapley value of $v_4$**: With $N=4$ there are $4!=24$ permutations. We use the formula:

   $$
   \phi_i(v_4)=\sum_{S\subseteq N\setminus\{i\}}\frac{|S|!(|N|-|S|-1)!}{|N|!}\bigl[v_4(S\cup\{i\})-v_4(S)\bigr]
   $$

   For player 1, the relevant subsets $S\subseteq\{2,3,4\}$ are:

   | $S$ | $|S|$ | weight $=\frac{|S|!\,(3-|S|)!}{24}$ | $v_4(S\cup\{1\})-v_4(S)$ |
   |---|---|---|---|
   | $\emptyset$ | 0 | $\frac{0!\cdot 3!}{24}=\frac{6}{24}$ | $v_4(\{1\})-0=6$ |
   | $\{2\}$ | 1 | $\frac{1!\cdot 2!}{24}=\frac{2}{24}$ | $v_4(\{1,2\})-v_4(\{2\})=7-7=0$ |
   | $\{3\}$ | 1 | $\frac{2}{24}$ | $v_4(\{1,3\})-v_4(\{3\})=6-0=6$ |
   | $\{4\}$ | 1 | $\frac{2}{24}$ | $v_4(\{1,4\})-v_4(\{4\})=12-8=4$ |
   | $\{2,3\}$ | 2 | $\frac{2!\cdot 1!}{24}=\frac{2}{24}$ | $v_4(\{1,2,3\})-v_4(\{2,3\})=7-7=0$ |
   | $\{2,4\}$ | 2 | $\frac{2}{24}$ | $v_4(\{1,2,4\})-v_4(\{2,4\})=24-12=12$ |
   | $\{3,4\}$ | 2 | $\frac{2}{24}$ | $v_4(\{1,3,4\})-v_4(\{3,4\})=12-8=4$ |
   | $\{2,3,4\}$ | 3 | $\frac{3!\cdot 0!}{24}=\frac{6}{24}$ | $v_4(\{1,2,3,4\})-v_4(\{2,3,4\})=25-12=13$ |

   $$
\begin{align*}
   \phi_1&=\frac{1}{24}\bigl[6\cdot 6+2\cdot 0+2\cdot 6+2\cdot 4+2\cdot 0+2\cdot 12+2\cdot 4+6\cdot 13\bigr] \\
          &=\frac{36+0+12+8+0+24+8+78}{24}=\frac{166}{24}=\frac{83}{12}\approx 6.92
\end{align*}
   $$

   For player 2, subsets $S\subseteq\{1,3,4\}$:

   | $S$ | $v_4(S\cup\{2\})-v_4(S)$ |
   |---|---|
   | $\emptyset$ | $7$ |
   | $\{1\}$ | $7-6=1$ |
   | $\{3\}$ | $7-0=7$ |
   | $\{4\}$ | $12-8=4$ |
   | $\{1,3\}$ | $7-6=1$ |
   | $\{1,4\}$ | $24-12=12$ |
   | $\{3,4\}$ | $12-8=4$ |
   | $\{1,3,4\}$ | $25-12=13$ |

   $$
\begin{align*}
   \phi_2&=\frac{6\cdot 7+2\cdot 1+2\cdot 7+2\cdot 4+2\cdot 1+2\cdot 12+2\cdot 4+6\cdot 13}{24} \\
          &=\frac{42+2+14+8+2+24+8+78}{24}=\frac{178}{24}=\frac{89}{12}\approx 7.42
\end{align*}
   $$

   For player 3, subsets $S\subseteq\{1,2,4\}$:

   | $S$ | $v_4(S\cup\{3\})-v_4(S)$ |
   |---|---|
   | $\emptyset$ | $0$ |
   | $\{1\}$ | $6-6=0$ |
   | $\{2\}$ | $7-7=0$ |
   | $\{4\}$ | $8-8=0$ |
   | $\{1,2\}$ | $7-7=0$ |
   | $\{1,4\}$ | $12-12=0$ |
   | $\{2,4\}$ | $12-12=0$ |
   | $\{1,2,4\}$ | $25-24=1$ |

   $$
\begin{align*}
   \phi_3&=\frac{6\cdot 0+2\cdot 0+2\cdot 0+2\cdot 0+2\cdot 0+2\cdot 0+2\cdot 0+6\cdot 1}{24} \\
          &=\frac{6}{24}=\frac{1}{4}=0.25
\end{align*}
   $$

   For player 4, subsets $S\subseteq\{1,2,3\}$:

   | $S$ | $v_4(S\cup\{4\})-v_4(S)$ |
   |---|---|
   | $\emptyset$ | $8$ |
   | $\{1\}$ | $12-6=6$ |
   | $\{2\}$ | $12-7=5$ |
   | $\{3\}$ | $8-0=8$ |
   | $\{1,2\}$ | $24-7=17$ |
   | $\{1,3\}$ | $12-6=6$ |
   | $\{2,3\}$ | $12-7=5$ |
   | $\{1,2,3\}$ | $25-7=18$ |

   $$
\begin{align*}
   \phi_4&=\frac{6\cdot 8+2\cdot 6+2\cdot 5+2\cdot 8+2\cdot 17+2\cdot 6+2\cdot 5+6\cdot 18}{24} \\
          &=\frac{48+12+10+16+34+12+10+108}{24}=\frac{250}{24}=\frac{125}{12}\approx 10.42
\end{align*}
   $$

   **Check**: $83/12+89/12+3/12+125/12=300/12=25=v_4(\{1,2,3,4\})$ ✓

```{code-cell} python3
import coopgt.characteristic_function_properties
import coopgt.shapley_value

# Game v1
v1 = {
    (): 0,
    (1,): 5, (2,): 3, (3,): 2,
    (1, 2): 12, (1, 3): 5, (2, 3): 4,
    (1, 2, 3): 13,
}
print("v1 monotone:", coopgt.characteristic_function_properties.is_monotone(v1))
print("v1 superadditive:", coopgt.characteristic_function_properties.is_superadditive(v1))
print("v1 Shapley:", coopgt.shapley_value.calculate(v1))
```

```{code-cell} python3
# Game v2
v2 = {(): 0, (1,): 6, (2,): 0, (1, 2): 5}
print("v2 monotone:", coopgt.characteristic_function_properties.is_monotone(v2))
print("v2 superadditive:", coopgt.characteristic_function_properties.is_superadditive(v2))
print("v2 Shapley:", coopgt.shapley_value.calculate(v2))
```

```{code-cell} python3
# Game v3
v3 = {
    (): 0,
    (1,): 6, (2,): 6, (3,): 13,
    (1, 2): 6, (1, 3): 13, (2, 3): 13,
    (1, 2, 3): 26,
}
print("v3 monotone:", coopgt.characteristic_function_properties.is_monotone(v3))
print("v3 superadditive:", coopgt.characteristic_function_properties.is_superadditive(v3))
print("v3 Shapley:", coopgt.shapley_value.calculate(v3))
```

```{code-cell} python3
# Game v4
v4 = {
    (): 0,
    (1,): 6, (2,): 7, (3,): 0, (4,): 8,
    (1, 2): 7, (1, 3): 6, (1, 4): 12,
    (2, 3): 7, (2, 4): 12, (3, 4): 8,
    (1, 2, 3): 7, (1, 2, 4): 24, (1, 3, 4): 12, (2, 3, 4): 12,
    (1, 2, 3, 4): 25,
}
print("v4 monotone:", coopgt.characteristic_function_properties.is_monotone(v4))
print("v4 superadditive:", coopgt.characteristic_function_properties.is_superadditive(v4))
print("v4 Shapley:", coopgt.shapley_value.calculate(v4))
```
````

````{solution} interpreting_linear_models
:label: solution:interpreting_linear_models

1. **Characteristic function $v(S)$**

   Using the $R^2$ values from the table, with players $\{x_1, x_2, x_3\}$:

   $$
   v(\emptyset)=0,\quad v(\{x_1\})=0.122,\quad v(\{x_2\})=0.097,\quad v(\{x_3\})=0.551
   $$

   $$
   v(\{x_1,x_2\})=0.174,\quad v(\{x_1,x_3\})=0.581,\quad v(\{x_2,x_3\})=0.620
   $$

   $$
   v(\{x_1,x_2,x_3\})=0.623
   $$

2. **Shapley value computation**

   We apply the formula with $N=3$:

   $$
   \phi_i(v)=\sum_{S\subseteq N\setminus\{i\}}\frac{|S|!(2-|S|)!}{6}\bigl[v(S\cup\{i\})-v(S)\bigr]
   $$

   **For $x_1$** (subsets $S\subseteq\{x_2,x_3\}$):

   | $S$ | weight | $v(S\cup\{x_1\})-v(S)$ |
   |---|---|---|
   | $\emptyset$ | $1/6$ | $0.122-0=0.122$ |
   | $\{x_2\}$ | $1/6$ | $0.174-0.097=0.077$ |
   | $\{x_3\}$ | $1/6$ | $0.581-0.551=0.030$ |
   | $\{x_2,x_3\}$ | $1/6$ | $0.623-0.620=0.003$ |

   $$
\begin{align*}
   \phi_{x_1}&=\frac{1}{6}(2\cdot 0.122+1\cdot 0.077+1\cdot 0.030+2\cdot 0.003) \\
             &=\frac{0.244+0.077+0.030+0.006}{6}=\frac{0.357}{6}\approx 0.0572
\end{align*}
   $$

   (Using weights: $|S|=0$ gets weight $\frac{0!\cdot 2!}{6}=2/6$, $|S|=1$ gets $\frac{1!\cdot 1!}{6}=1/6$, $|S|=2$ gets $\frac{2!\cdot 0!}{6}=2/6$.)

   $$
   \phi_{x_1}=\frac{2\cdot 0.122+1\cdot 0.077+1\cdot 0.030+2\cdot 0.003}{6}=\frac{0.357}{6}\approx 0.0595
   $$

   **For $x_2$** (subsets $S\subseteq\{x_1,x_3\}$):

   | $S$ | weight | $v(S\cup\{x_2\})-v(S)$ |
   |---|---|---|
   | $\emptyset$ | $2/6$ | $0.097$ |
   | $\{x_1\}$ | $1/6$ | $0.174-0.122=0.052$ |
   | $\{x_3\}$ | $1/6$ | $0.620-0.551=0.069$ |
   | $\{x_1,x_3\}$ | $2/6$ | $0.623-0.581=0.042$ |

   $$
   \phi_{x_2}=\frac{2\cdot 0.097+1\cdot 0.052+1\cdot 0.069+2\cdot 0.042}{6}=\frac{0.194+0.052+0.069+0.084}{6}=\frac{0.399}{6}\approx 0.0665
   $$

   **For $x_3$** (subsets $S\subseteq\{x_1,x_2\}$):

   | $S$ | weight | $v(S\cup\{x_3\})-v(S)$ |
   |---|---|---|
   | $\emptyset$ | $2/6$ | $0.551$ |
   | $\{x_1\}$ | $1/6$ | $0.581-0.122=0.459$ |
   | $\{x_2\}$ | $1/6$ | $0.620-0.097=0.523$ |
   | $\{x_1,x_2\}$ | $2/6$ | $0.623-0.174=0.449$ |

   $$
   \phi_{x_3}=\frac{2\cdot 0.551+1\cdot 0.459+1\cdot 0.523+2\cdot 0.449}{6}=\frac{1.102+0.459+0.523+0.898}{6}=\frac{2.982}{6}\approx 0.4970
   $$

   **Check**: $0.0595+0.0665+0.4970\approx 0.623=v(\{x_1,x_2,x_3\})$ ✓

3. **Interpretation**

   The Shapley values are approximately:

   $$
   \phi_{x_1}\approx 0.060,\quad\phi_{x_2}\approx 0.067,\quad\phi_{x_3}\approx 0.497
   $$

   Feature $x_3$ contributes by far the most explanatory power, accounting for roughly $0.497/0.623\approx 80\%$ of the total $R^2$. Features $x_1$ and $x_2$ contribute very little, with $x_1$ contributing slightly less than $x_2$. The Shapley value allocates the credit for the combined model performance fairly across the features, accounting for all possible orderings in which they are added.

```{code-cell} python3
import coopgt.shapley_value

v_linear = {
    (): 0,
    (1,): 0.122,
    (2,): 0.097,
    (3,): 0.551,
    (1, 2): 0.174,
    (1, 3): 0.581,
    (2, 3): 0.620,
    (1, 2, 3): 0.623,
}

shapley = coopgt.shapley_value.calculate(characteristic_function=v_linear)
print("Shapley values (x1, x2, x3):", shapley)
print(f"Sum: {sum(shapley):.3f} (should equal {v_linear[(1, 2, 3)]})")
```
````

````{solution} additivity-and-symmetry
:label: solution:additivity-and-symmetry

**Game $v_a$** on $N=\{1,2,3\}$:

$$
v_a(C)=\begin{cases}2, &C=\{1\}\\2, &C=\{2\}\\0, &\text{otherwise}\end{cases}
$$

**Game $v_b$** on $N=\{1,2,3\}$:

$$
v_b(C)=\begin{cases}1, &C=\{1,3\}\\1, &C=\{2,3\}\\3, &C=\{1,2,3\}\\0, &\text{otherwise}\end{cases}
$$

1. **Symmetry property**

   Recall the symmetry property: if $v(C\cup\{i\})=v(C\cup\{j\})$ for all $C\subseteq\Omega\setminus\{i,j\}$, then $\phi_i=\phi_j$.

   **For $v_a$**: Players 1 and 2 are symmetric. For every $C\subseteq\{3\}$:

   - $v_a(C\cup\{1\})$: if $C=\emptyset$, $v_a(\{1\})=2$; if $C=\{3\}$, $v_a(\{1,3\})=0$.
   - $v_a(C\cup\{2\})$: if $C=\emptyset$, $v_a(\{2\})=2$; if $C=\{3\}$, $v_a(\{2,3\})=0$.

   Since $v_a(C\cup\{1\})=v_a(C\cup\{2\})$ for all $C\subseteq\{3\}$, players 1 and 2 are symmetric under $v_a$. No other pair is symmetric, so players 1 and 2 are the only pair the property constrains.

   **$v_a$ satisfies the symmetry property.**

   **For $v_b$**: Players 1 and 2 are symmetric. For every $C\subseteq\{3\}$:

   - $C=\emptyset$: $v_b(\{1\})=0=v_b(\{2\})$ ✓
   - $C=\{3\}$: $v_b(\{1,3\})=1=v_b(\{2,3\})$ ✓

   **$v_b$ satisfies the symmetry property.**

2. **Shapley values of $v_a$ and $v_b$**

   **Shapley value of $v_a$**:

   Because $v_a$ is not monotone (the singletons $\{1\}$ and $\{2\}$ are worth
   $2$, but every larger coalition is worth $0$), the marginal contributions must
   be computed carefully, term by term:

   | $\pi$ | $\Delta^{v_a}_\pi(1)$ | $\Delta^{v_a}_\pi(2)$ | $\Delta^{v_a}_\pi(3)$ |
   |---|---|---|---|
   | $(1,2,3)$ | $v_a(\{1\})=2$ | $v_a(\{1,2\})-v_a(\{1\})=-2$ | $v_a(\{1,2,3\})-v_a(\{1,2\})=0$ |
   | $(1,3,2)$ | $2$ | $v_a(\{1,2,3\})-v_a(\{1,3\})=0$ | $v_a(\{1,3\})-v_a(\{1\})=-2$ |
   | $(2,1,3)$ | $v_a(\{1,2\})-v_a(\{2\})=-2$ | $v_a(\{2\})=2$ | $0$ |
   | $(2,3,1)$ | $v_a(\{1,2,3\})-v_a(\{2,3\})=0$ | $2$ | $v_a(\{2,3\})-v_a(\{2\})=-2$ |
   | $(3,1,2)$ | $v_a(\{1,3\})-v_a(\{3\})=0$ | $v_a(\{1,2,3\})-v_a(\{1,3\})=0$ | $v_a(\{3\})=0$ |
   | $(3,2,1)$ | $v_a(\{1,2,3\})-v_a(\{2,3\})=0$ | $v_a(\{2,3\})-v_a(\{3\})=0$ | $0$ |

   $$
   \phi_1(v_a)=\frac{2+2-2+0+0+0}{6}=\frac{2}{6}=\frac{1}{3}
   $$

   $$
   \phi_2(v_a)=\frac{-2+0+2+2+0+0}{6}=\frac{2}{6}=\frac{1}{3}
   $$

   $$
   \phi_3(v_a)=\frac{0-2+0-2+0+0}{6}=\frac{-4}{6}=-\frac{2}{3}
   $$

   **Check**: $1/3+1/3-2/3=0=v_a(\{1,2,3\})$ ✓

   **Shapley value of $v_b$**:

   | $\pi$ | $\Delta^{v_b}_\pi(1)$ | $\Delta^{v_b}_\pi(2)$ | $\Delta^{v_b}_\pi(3)$ |
   |---|---|---|---|
   | $(1,2,3)$ | $0$ | $0$ | $v_b(\{1,2,3\})-v_b(\{1,2\})=3$ |
   | $(1,3,2)$ | $0$ | $v_b(\{1,2,3\})-v_b(\{1,3\})=2$ | $v_b(\{1,3\})-v_b(\{1\})=1$ |
   | $(2,1,3)$ | $0$ | $0$ | $3$ |
   | $(2,3,1)$ | $v_b(\{1,2,3\})-v_b(\{2,3\})=2$ | $0$ | $v_b(\{2,3\})-v_b(\{2\})=1$ |
   | $(3,1,2)$ | $v_b(\{1,3\})-v_b(\{3\})=1$ | $v_b(\{1,2,3\})-v_b(\{1,3\})=2$ | $0$ |
   | $(3,2,1)$ | $v_b(\{1,2,3\})-v_b(\{2,3\})=2$ | $v_b(\{2,3\})-v_b(\{3\})=1$ | $0$ |

   $$
   \phi_1(v_b)=\frac{0+0+0+2+1+2}{6}=\frac{5}{6}
   $$

   $$
   \phi_2(v_b)=\frac{0+2+0+0+2+1}{6}=\frac{5}{6}
   $$

   $$
   \phi_3(v_b)=\frac{3+1+3+1+0+0}{6}=\frac{8}{6}=\frac{4}{3}
   $$

   **Check**: $5/6+5/6+4/3=5/6+5/6+8/6=18/6=3=v_b(\{1,2,3\})$ ✓

3. **The game $v^+ = v_a + v_b$**

   $$
   v^+(C)=v_a(C)+v_b(C)
   $$

   | $C$ | $v_a(C)$ | $v_b(C)$ | $v^+(C)$ |
   |---|---|---|---|
   | $\emptyset$ | $0$ | $0$ | $0$ |
   | $\{1\}$ | $2$ | $0$ | $2$ |
   | $\{2\}$ | $2$ | $0$ | $2$ |
   | $\{3\}$ | $0$ | $0$ | $0$ |
   | $\{1,2\}$ | $0$ | $0$ | $0$ |
   | $\{1,3\}$ | $0$ | $1$ | $1$ |
   | $\{2,3\}$ | $0$ | $1$ | $1$ |
   | $\{1,2,3\}$ | $0$ | $3$ | $3$ |

   Using the Shapley formula for $v^+$:

   $$
   \phi_1(v^+)=\phi_1(v_a)+\phi_1(v_b)=\frac{1}{3}+\frac{5}{6}=\frac{2}{6}+\frac{5}{6}=\frac{7}{6}
   $$

   $$
   \phi_2(v^+)=\frac{1}{3}+\frac{5}{6}=\frac{7}{6}
   $$

   $$
   \phi_3(v^+)=-\frac{2}{3}+\frac{4}{3}=\frac{2}{3}
   $$

4. **Verification of the additivity property**

   We verify by computing the Shapley value of $v^+$ directly.

   | $\pi$ | $\Delta^{v^+}_\pi(1)$ | $\Delta^{v^+}_\pi(2)$ | $\Delta^{v^+}_\pi(3)$ |
   |---|---|---|---|
   | $(1,2,3)$ | $2$ | $-2$ | $3$ |
   | $(1,3,2)$ | $2$ | $2$ | $-1$ |
   | $(2,1,3)$ | $-2$ | $2$ | $3$ |
   | $(2,3,1)$ | $2$ | $2$ | $-1$ |
   | $(3,1,2)$ | $1$ | $2$ | $0$ |
   | $(3,2,1)$ | $2$ | $1$ | $0$ |

   $$
   \phi_1(v^+)=\frac{2+2-2+2+1+2}{6}=\frac{7}{6}\checkmark
   $$

   $$
   \phi_2(v^+)=\frac{-2+2+2+2+2+1}{6}=\frac{7}{6}\checkmark
   $$

   $$
   \phi_3(v^+)=\frac{3-1+3-1+0+0}{6}=\frac{4}{6}=\frac{2}{3}\checkmark
   $$

   The Shapley value of $v^+$ equals $\phi(v_a)+\phi(v_b)$, confirming the **additivity property**.

```{code-cell} python3
import coopgt.shapley_value

va = {
    (): 0,
    (1,): 2, (2,): 2, (3,): 0,
    (1, 2): 0, (1, 3): 0, (2, 3): 0,
    (1, 2, 3): 0,
}

vb = {
    (): 0,
    (1,): 0, (2,): 0, (3,): 0,
    (1, 2): 0, (1, 3): 1, (2, 3): 1,
    (1, 2, 3): 3,
}

v_plus = {k: va[k] + vb[k] for k in va}

phi_a = coopgt.shapley_value.calculate(characteristic_function=va)
phi_b = coopgt.shapley_value.calculate(characteristic_function=vb)
phi_plus = coopgt.shapley_value.calculate(characteristic_function=v_plus)

print("Shapley value of v_a:", phi_a)
print("Shapley value of v_b:", phi_b)
print("Shapley value of v_a + v_b (direct):", phi_plus)
print("Sum of Shapley values:", [a + b for a, b in zip(phi_a, phi_b)])
print("Additivity holds:", all(abs(p - (a + b)) < 1e-10 for p, a, b in zip(phi_plus, phi_a, phi_b)))
```
````

````{solution} null-player-and-marginal-contributions
:label: solution:null-player-and-marginal-contributions

The game $v$ on $N=\{1,2,3\}$ is:

$$
v(C)=\begin{cases}
4, &C=\{1\}\\
7, &C=\{1,2\}\\
7, &C=\{1,2,3\}\\
0, &\text{otherwise}
\end{cases}
$$

1. **Identifying null players**

   A player $i$ is a null player if $v(C\cup\{i\})=v(C)$ for all coalitions $C\subseteq\Omega$.

   **Player 2**: Check whether $v(C\cup\{2\})=v(C)$ for all $C$:

   - $C=\emptyset$: $v(\{2\})=0=v(\emptyset)=0$ ✓
   - $C=\{1\}$: $v(\{1,2\})=7\neq 4=v(\{1\})$ ✗

   Player 2 is **not** a null player.

   **Player 3**: Check whether $v(C\cup\{3\})=v(C)$ for all $C$:

   - $C=\emptyset$: $v(\{3\})=0=v(\emptyset)=0$ ✓
   - $C=\{1\}$: $v(\{1,3\})=0\neq 4=v(\{1\})$ ✗ (the coalition $\{1,3\}$ is not listed, so its value is $0$).

   Player 3 is **not** a null player.

2. **Marginal contributions**

   | $\pi$ | $\Delta^v_\pi(1)$ | $\Delta^v_\pi(2)$ | $\Delta^v_\pi(3)$ |
   |---|---|---|---|
   | $(1,2,3)$ | $v(\{1\})-0=4$ | $v(\{1,2\})-v(\{1\})=3$ | $v(\{1,2,3\})-v(\{1,2\})=0$ |
   | $(1,3,2)$ | $v(\{1\})-0=4$ | $v(\{1,2,3\})-v(\{1,3\})=7$ | $v(\{1,3\})-v(\{1\})=-4$ |
   | $(2,1,3)$ | $v(\{1,2\})-v(\{2\})=7$ | $v(\{2\})-0=0$ | $v(\{1,2,3\})-v(\{1,2\})=0$ |
   | $(2,3,1)$ | $v(\{1,2,3\})-v(\{2,3\})=7$ | $v(\{2\})-0=0$ | $v(\{2,3\})-v(\{2\})=0$ |
   | $(3,1,2)$ | $v(\{1,3\})-v(\{3\})=0$ | $v(\{1,2,3\})-v(\{1,3\})=7$ | $v(\{3\})-0=0$ |
   | $(3,2,1)$ | $v(\{1,2,3\})-v(\{2,3\})=7$ | $v(\{2,3\})-v(\{3\})=0$ | $v(\{3\})-0=0$ |

3. **Shapley value**

   $$
   \phi_1(v)=\frac{4+4+7+7+0+7}{6}=\frac{29}{6}\approx 4.83
   $$

   $$
   \phi_2(v)=\frac{3+7+0+0+7+0}{6}=\frac{17}{6}\approx 2.83
   $$

   $$
   \phi_3(v)=\frac{0-4+0+0+0+0}{6}=-\frac{4}{6}=-\frac{2}{3}\approx -0.67
   $$

   **Check**: $29/6+17/6-4/6=42/6=7=v(\{1,2,3\})$ ✓

   **Null player property**: Player 3 is not a null player (since $v(\{1,3\})\neq v(\{1\})$), so the null player property does not require $\phi_3=0$. Indeed $\phi_3=-2/3\neq 0$. The Shapley value correctly penalises player 3 for actually reducing the value of coalition $\{1\}$ when they join.

   To see this concretely: adding player 3 to coalition $\{1\}$ reduces the value from $4$ to $0$. This negative marginal contribution is reflected in the Shapley value.

```{code-cell} python3
import coopgt.shapley_value

v = {
    (): 0,
    (1,): 4, (2,): 0, (3,): 0,
    (1, 2): 7, (1, 3): 0, (2, 3): 0,
    (1, 2, 3): 7,
}

shapley = coopgt.shapley_value.calculate(characteristic_function=v)
print("Shapley value:", shapley)
print(f"phi_1 = {shapley[0]:.4f} (expected 29/6 = {29/6:.4f})")
print(f"phi_2 = {shapley[1]:.4f} (expected 17/6 = {17/6:.4f})")
print(f"phi_3 = {shapley[2]:.4f} (expected -2/3 = {-2/3:.4f})")
```
````

````{solution} properties-of-the-shapley-value
:label: solution:properties-of-the-shapley-value

Recall the Shapley value:

$$
\phi_i(G)=\frac{1}{N!}\sum_{\pi\in\Pi_N}\Delta_\pi^G(i)=\frac{1}{N!}\sum_{\pi\in\Pi_N}\bigl[v(S_\pi(i)\cup\{i\})-v(S_\pi(i))\bigr]
$$

**Proof of Efficiency**

We must show $\sum_{i=1}^N\phi_i(G)=v(\Omega)$.

$$
\sum_{i=1}^N\phi_i(G)=\frac{1}{N!}\sum_{i=1}^N\sum_{\pi\in\Pi_N}\Delta_\pi^G(i)=\frac{1}{N!}\sum_{\pi\in\Pi_N}\sum_{i=1}^N\Delta_\pi^G(i)
$$

For a fixed permutation $\pi=(\pi_1,\pi_2,\ldots,\pi_N)$, the marginal contributions telescope:

$$
\sum_{i=1}^N\Delta_\pi^G(i)=\sum_{k=1}^N\bigl[v(\{\pi_1,\ldots,\pi_k\})-v(\{\pi_1,\ldots,\pi_{k-1}\})\bigr]=v(\Omega)-v(\emptyset)=v(\Omega)
$$

since $v(\emptyset)=0$. Therefore:

$$
\sum_{i=1}^N\phi_i(G)=\frac{1}{N!}\sum_{\pi\in\Pi_N}v(\Omega)=\frac{N!\cdot v(\Omega)}{N!}=v(\Omega)
\qquad\square
$$

---

**Proof of the Null Player Property**

Suppose $v(C\cup\{i\})=v(C)$ for all $C\subseteq\Omega$. Then for every permutation $\pi$:

$$
\Delta_\pi^G(i)=v(S_\pi(i)\cup\{i\})-v(S_\pi(i))=0
$$

Therefore:

$$
\phi_i(G)=\frac{1}{N!}\sum_{\pi\in\Pi_N}0=0\qquad\square
$$

---

**Proof of the Symmetry Property**

Suppose $v(C\cup\{i\})=v(C\cup\{j\})$ for all $C\subseteq\Omega\setminus\{i,j\}$. We wish to show $\phi_i=\phi_j$.

For any permutation $\pi$, define the permutation $\pi'$ by swapping the positions of $i$ and $j$ in $\pi$. This defines a bijection on $\Pi_N$ (swapping $i$ and $j$ in every permutation), and every permutation is paired with a unique partner.

Consider any permutation $\pi$. Let $S=S_\pi(i)\setminus\{j\}$, i.e. the predecessors of $i$ not counting $j$.

**Case 1**: $j$ is not a predecessor of $i$ in $\pi$ (i.e. $i$ comes before $j$). Then $S_\pi(i)\subseteq\Omega\setminus\{i,j\}$, so:

$$
\Delta_\pi^G(i)=v(S_\pi(i)\cup\{i\})-v(S_\pi(i))
$$

In $\pi'$ (where $i$ and $j$ are swapped), $j$ now appears where $i$ was, so $S_{\pi'}(j)=S_\pi(i)$:

$$
\Delta_{\pi'}^G(j)=v(S_{\pi'}(j)\cup\{j\})-v(S_{\pi'}(j))=v(S_\pi(i)\cup\{j\})-v(S_\pi(i))
$$

Since $S_\pi(i)\subseteq\Omega\setminus\{i,j\}$, the symmetry assumption gives $v(S_\pi(i)\cup\{i\})=v(S_\pi(i)\cup\{j\})$, so:

$$
\Delta_\pi^G(i)=\Delta_{\pi'}^G(j)
$$

**Case 2**: $j$ is a predecessor of $i$ in $\pi$. Then $S_\pi(i)$ contains $j$. Let $S=S_\pi(i)\setminus\{j\}\subseteq\Omega\setminus\{i,j\}$. Then:

$$
\Delta_\pi^G(i)=v(S\cup\{i,j\})-v(S\cup\{j\})
$$

In $\pi'$, $i$ has been moved to where $j$ was, so the predecessors of $j$ in $\pi'$ are the predecessors of $i$ in $\pi$ with $j$ relabelled as $i$, namely $S\cup\{i\}$. Thus:

$$
\Delta_{\pi'}^G(j)=v(S\cup\{i,j\})-v(S\cup\{i\})
$$

Since $S\subseteq\Omega\setminus\{i,j\}$, the symmetry assumption gives $v(S\cup\{i\})=v(S\cup\{j\})$, so $\Delta_\pi^G(i)=\Delta_{\pi'}^G(j)$ in this case as well.

In both cases $\Delta_\pi^G(i)=\Delta_{\pi'}^G(j)$. Since $\pi\mapsto\pi'$ is a bijection on $\Pi_N$, summing over all permutations gives:

$$
\phi_i(G)=\frac{1}{N!}\sum_{\pi\in\Pi_N}\Delta_\pi^G(i)=\frac{1}{N!}\sum_{\pi\in\Pi_N}\Delta_{\pi'}^G(j)=\frac{1}{N!}\sum_{\pi'\in\Pi_N}\Delta_{\pi'}^G(j)=\phi_j(G)\qquad\square
$$

---

**Proof of the Additivity Property**

Let $G_1=(N,v_1)$, $G_2=(N,v_2)$, and $G^+=(N,v^+)$ with $v^+=v_1+v_2$.

$$
\phi_i(G^+)=\frac{1}{N!}\sum_{\pi\in\Pi_N}\bigl[v^+(S_\pi(i)\cup\{i\})-v^+(S_\pi(i))\bigr]
$$

$$
=\frac{1}{N!}\sum_{\pi\in\Pi_N}\bigl[(v_1+v_2)(S_\pi(i)\cup\{i\})-(v_1+v_2)(S_\pi(i))\bigr]
$$

$$
=\frac{1}{N!}\sum_{\pi\in\Pi_N}\bigl[v_1(S_\pi(i)\cup\{i\})-v_1(S_\pi(i))\bigr]+\frac{1}{N!}\sum_{\pi\in\Pi_N}\bigl[v_2(S_\pi(i)\cup\{i\})-v_2(S_\pi(i))\bigr]
$$

$$
=\phi_i(G_1)+\phi_i(G_2)\qquad\square
$$
````
