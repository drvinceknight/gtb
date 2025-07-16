---
kernelspec:
  name: python3
  display_name: "Python 3"
---

(chp:rationality)=

# Rationality

## Motivating Example: Competing Restaurant Locations

Two restaurant chains, **FreshBite** and **UrbanEats**, are expanding into a new
city. Each must choose one of three neighbourhoods for a flagship store:
**Downtown**, **Midtown**, or **Suburb**.

- **FreshBite** (row player) prioritises foot traffic and brand visibility.
- **UrbanEats** (column player) prefers low rental costs and long-term margins.

The projected profits (in £1000s) for each company depend on both their own
choice and their competitor’s. Since they are competing in the same market,
outcomes reflect strategic interaction.

[](#tbl:freshbite_profits) and [](#tbl:urbaneats_profits) show the expected
profits for each company based on their own decision (row) and their
competitor’s choice (column).

```{table} Projected profits for __FreshBite__ (in thousands of pounds)
:label: tbl:freshbite_profits
:align: center
:class: table-bordered

|                  | Downtown | Midtown | Suburb |
|------------------|----------|---------|--------|
| **Downtown**     | 4        | 3       | 2      |
| **Midtown**      | 3        | 2       | 3      |
| **Suburb**       | 2        | 1       | 1      |

```

```{table} Projected profits for __UrbanEats__ (in thousands of pounds)
:label: tbl:urbaneats_profits
:align: center
:class: table-bordered

|                  | Downtown | Midtown | Suburb |
|------------------|----------|---------|--------|
| **Downtown**     | 1        | 0       | 3      |
| **Midtown**      | 0        | 2       | 6      |
| **Suburb**       | 2        | 4       | 5      |

```

These tables are assumed to be publicly available from a consultation
commissioned by the city council.

```{important}
[](#tbl:freshbite_profits) and [](#tbl:urbaneats_profits) are not the payoff
matrices $M_r$ and $M_c$ of [](#eqn:payoff_matrices_definition).
They represent the raw projected profit data used to define the game.
```

The payoff matrices for the equivalent Normal Form Game are:

$$
M_r=\begin{pmatrix}
4 & 3 & 2\\
3 & 2 & 3\\
2 & 1 & 1
\end{pmatrix}
\qquad
M_c=\begin{pmatrix}
1 & 0 & 2\\
0 & 2 & 4\\
2 & 6 & 5
\end{pmatrix}
$$

```{note}
$M_c$ is obtained by transposing the rows and columns of
[](#tbl:urbaneats_profits).
```

Let us begin from FreshBite’s perspective:
Suburb results in lower profits than Midtown or Downtown, regardless
of UrbanEats’ action. A rational FreshBite would therefore never choose
Suburb, as illustrated in [](#fig:rationalisation_of_restaurants_step_1)
although it might still choose
**Midtown** or **Downtown**.

```{figure} ./images/rationalisation_of_restaurants_step_1/main.png
:alt: Two payoff matrices with a line crossing out Suburb in the row player matrix
:label: fig:rationalisation_of_restaurants_step_1
:height: 250px

Crossing out Suburb as an action that will never be played by the row player.
```

With Suburb eliminated for FreshBite, UrbanEats can update their view.
Against the remaining options (Downtown and Midtown), UrbanEats
consistently receives higher profits by choosing Suburb rather than either
alternative. Hence, Downtown and Midtown can be removed from
consideration, as shown in [](#fig:rationalisation_of_restaurants_step_2).

```{figure} ./images/rationalisation_of_restaurants_step_2/main.png
:alt: Two payoff matrices with a line crossing out Midtown in the column player matrix
:label: fig:rationalisation_of_restaurants_step_2
:height: 250px

Crossing out Midtown and Downtown as actions that will never be played by the column
player.
```

FreshBite, now comparing Downtown and Midtown against only
Suburb from UrbanEats, finds that Midtown yields a better outcome.
They therefore eliminate Downtown, leaving Midtown as their
only rational option, as shown in [](#fig:rationalisation_of_restaurants_step_3).

```{figure} ./images/rationalisation_of_restaurants_step_3/main.png
:alt: Two payoff matrices with a line crossing out Midtown in the column player matrix
:label: fig:rationalisation_of_restaurants_step_3
:height: 250px

Crossing out Downtown as an action that will never be played by the row
player.
```

The step-by-step logic of **iterated elimination of strategies**,
combined with the assumption of full information and mutual rationality, leads to
the predicted outcome:

- FreshBite opens in **Midtown**: with an expected profit of £3,000.
- UrbanEats opens in **Surbuban**: with an expected profit of £4,000

```{note}
This outcome is not necessarily optimal for both players, but it is rational
given the available information and the structure of the interaction.
```

In the next section, we introduce the **theory of dominance and best responses**.
These concepts provide the formal tools for identifying outcomes like this one,
and for understanding how strategic agents simplify complex decisions.

## Theory

In certain games it is evident that certain strategies should never be used by a rational player.
To formalise this we need a couple of definitions.

### Definition: Incomplete Strategy Profile

---

In an $N$-player normal form game, when focusing on player $i$, we denote by
$s_{(-i)}$ an **incomplete strategy profile** representing the strategies chosen
by all players _except_ player $i$.

---

For example, in a 3-player game where $\mathcal{A}_i = \{A, B\}$ for all $i$,
a valid strategy profile might be
$s = ((1, 0),\ (1, 0),\ (0, 1))$,
indicating that players 1 and 2 choose $A$, and player 3 chooses $B$.

The corresponding incomplete strategy profile for player 2 is:
$s_{(-2)} = ((1, 0),\ (0, 1))$
— capturing only the choices of players 1 and 3.

We write $S_{(-i)}$ to denote the set of all such incomplete strategy profiles
from the perspective of player $i$.

This notation allows us to define a key concept in strategic reasoning.

---

### Definition: Strictly Dominated Strategy

---

In an $N$-player normal form game, an action $a_i \in \mathcal{A}_i$ is said to
be **strictly dominated** if there exists a strategy
$\sigma_i \in \Delta(\mathcal{A}_i)$ such that:

$$
u_i(\sigma_i, s_{(-i)}) > u_i(a_i, s_{(-i)}) \quad \text{for all } s_{(-i)} \in S_{(-i)}.
$$

---

That is, no matter what the other players do, player $i$ always receives a
strictly higher payoff by playing $\sigma_i$ instead of the action $a_i$.

When modelling rational behaviour, such actions can be systematically
excluded from consideration.

### Definition: Weakly Dominated Strategy

---

In an $N$-player normal form game, an action $a_i \in \mathcal{A}_i$
is said to be **weakly dominated** if there exists a
strategy $\sigma_i \in \Delta(\mathcal{A}_i)$ such that:

$$
u_i(\sigma_i, s_{-i}) \geq u_i(s_i, s_{-i})
\quad \text{for all } s_{-i} \in S_{-i},
$$

and

$$
u_i(\sigma_i, \bar{s}) > u_i(s_i, \bar{s})
\quad \text{for some } \bar{s} \in S_{-i}.
$$

---

That is, $\sigma_i$ does at least as well as $s_i$ against all possible
strategies of the other players, and strictly better against at least one.

As with strictly dominated strategies, we can use weak dominance to
guide predictions of rational behaviour by eliminating weakly dominated strategies.
Doing so, however, relies on a deeper assumption about what players know
about one another.

### Common Knowledge of Rationality

So far, we have assumed that players behave rationally.
But to justify iterative elimination procedures, we must go further.
The key idea is that not only are players rational, but they also know that
others are rational—and that this knowledge is shared recursively.

This leads to the concept of **Common Knowledge of Rationality (CKR)**:

- Each player is rational.
- Each player knows that all other players are rational.
- Each player knows that all others know that they are rational.
- Each player knows that all others know that they all know that they are rational.
- And so on, indefinitely.

This infinite chain of mutual knowledge is what constitutes **common knowledge**.

By assuming CKR, we justify the use of techniques like the iterated elimination
of dominated strategies as a model of rational prediction.

### Example: Predicted Behaviour through Iterated Elimination Strategies

Consider the following normal form game, with separate payoff matrices for
the row and column players:

$$
M_r = \begin{pmatrix}
1 & 1 & 0 \\
0 & 0 & 2
\end{pmatrix}
\qquad
M_c = \begin{pmatrix}
0 & 2 & 1 \\
3 & 1 & 1
\end{pmatrix}
$$

We proceed by examining whether any strategies can be removed based on
weak dominance.

**Step 1:** From the column player’s perspective, column $c_3$ is weakly
dominated by column $c_2$. That is, for every row, $c_2$ performs at least
as well as $c_3$, and strictly better for at least one row.
We remove $c_3$ from consideration.

**Step 2:** With $c_3$ removed, the row player now compares $r_1$ and $r_2$.
Row $r_2$ is weakly dominated by $r_1$, since $r_1$ yields outcomes that are
always at least as good and sometimes strictly better.
We eliminate $r_2$.

**Step 3:** Finally, the column player is left with $c_1$ and $c_2$.
Column $c_1$ is now weakly dominated by $c_2$, and can be eliminated.

After these steps, we are left with a single strategy profile:

$$
s = (r_1, c_2)
$$

This strategy profile is a **predicted outcome** based on
iterated elimination of weakly dominated strategies,
assuming mutual rationality and full knowledge of the payoffs.

```{note}
Unlike strictly dominated strategies, weakly dominated strategies
can sometimes be part of a predicted outcome. This process provides
a reasonable prediction but not a definitive one.
```

### Example: eliminating strategies does not suffice

In many cases, we can simplify a game by eliminating dominated strategies.
However, not all games can be fully resolved using this approach.

Consider the following two games.

$$
M_r = \begin{pmatrix}
1 & 4 & 2 \\
4 & 0 & 4 \\
2 & 3 & 5
\end{pmatrix}
\qquad
M_c = \begin{pmatrix}
3 & 2 & 2 \\
0 & 3 & 1 \\
5 & 4 & 6
\end{pmatrix}
$$

Although some weakly dominated strategies may be eliminated here,
we still end up with multiple strategy combinations remaining.
No single obvious solution emerges from dominance alone.
Here is another example:

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

In this game, no strategy is strictly or weakly dominated for either player.
Elimination techniques do not reduce the strategy space,
and further analysis is required to predict behaviour.

These examples show that **dominance is a helpful tool**,
but not always sufficient. We need further concepts—such as
[**best responses**](#sec:best_responses) to analyse such games.
Payoff matrices for the row and column players:

(sec:best_responses)=

### Definition: Best Response

---

In an $N$-player normal form game, a strategy $s^*$ for player $i$ is a
**best response** to some incomplete strategy profile $s_{-i}$ if and only if:

$$
u_i(s^*,\ s_{-i}) \geq u_i(s,\ s_{-i}) \quad \text{for all } s \in \Delta(\mathcal{A}_i).
$$

---

That is, $s^*$ gives player $i$ the highest possible payoff,
given the strategies chosen by the other players.

We can now begin to predict rational behaviour by identifying the best responses
to actions of the other players.

(exam:predicted_behaviour_through_best_responses_in_the_action_space)=

### Example: Predicted Behaviour through Best Responses in the Action Space

Consider the following game with payoff matrices for the row and column players:

$$
M_r = \begin{pmatrix}
1 & 4 & 2 \\
4 & 0 & 4 \\
2 & 3 & 5
\end{pmatrix}
\qquad
M_c = \begin{pmatrix}
3 & 2 & 2 \\
0 & 3 & 1 \\
5 & 4 & 6
\end{pmatrix}
$$

We highlight best responses by underlining the maximum value(s) in each
row (for the column player) and in each column (for the row player):

$$
M_r =
\begin{pmatrix}
1 & \underline{4} & 2 \\
\underline{4} & 0 & 4 \\
2 & 3 & \underline{5}
\end{pmatrix}
\qquad
M_c =
\begin{pmatrix}
\underline{3} & 2 & 2 \\
0 & \underline{3} & 1 \\
5 & 4 & \underline{6}
\end{pmatrix}
$$

Here, $((0, 0, 1), (0, 0, 1))$ is a pair of best responses:

- $r_3$ is a best response to $c_3$,
- and $c_3$ is a best response to $r_3$.

This mutual best response suggests a potential **stable outcome**.

In the next example we will consider finding best responses in the entire
strategy space and not just the action space.

### Example: Predicted Behaviour through Best Responses in the Strategy Space

We can also identify best responses when players use **strategies**.
Let us begin by examining the **Matching Pennies** game.

#### Example: Matching Pennies

Recalling the [Payoff matrices for the row and column players](#matching_pennies):

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

Assume that player 2 plays a strategy
$\sigma_2 = (x,\ 1 - x)$. Then player 1’s expected utilities are:

$$
u_1(r_1,\ \sigma_2) = 2x - 1
\qquad \text{and} \qquad
u_1(r_2,\ \sigma_2) = 1 - 2x
$$

We will use some code to plot these two payoff values:

```{code-cell} python3
import matplotlib.pyplot as plt
import numpy as np

x = np.array((0, 1))

plt.figure()
plt.plot(2 * x - 1, label=r"$u_1(r_1, \sigma_2) = 2x - 1$")
plt.plot(1 -  2 * x, label=r"$ u_1(r_2, \sigma_2) = 1 - 2x $")
plt.title("Utility of the row player's actions as a function of the stratey played by the column player")
plt.xlabel("$x$")
plt.legend();
```

From the graph we observe:

1. If $x < \frac{1}{2}$, then $r_2$ is a best response for player 1.
2. If $x > \frac{1}{2}$, then $r_1$ is a best response for player 1.
3. If $x = \frac{1}{2}$, then player 1 is indifferent between $r_1$ and $r_2$.

### Examples: Coordination Game

Recalling the [Payoff matrices for the row and column players](#sec:coordination_game):

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

Assume that player 1 plays a strategy
$\sigma_1 = (x,\ 1 - x)$. Then player 2’s expected utilities are:

$$
u_1(r_1,\ \sigma_2) = 2x + (1 - x) = x + 1
\qquad \text{and} \qquad
u_1(r_2,\ \sigma_2) = 3(1 - x) = 3 - 3 x
$$

We will use some code to plot these two payoff values:

```{code-cell} python3
import matplotlib.pyplot as plt
import numpy as np

x = np.array((0, 1))

plt.figure()
plt.plot(x + 1, label=r"$u_2(\sigma_1, c_1) = x + 1$")
plt.plot(3 - 3 * x, label=r"$ u_2(\sigma_2, c_2) = 3 - 3 x $")
plt.title("Utility of the column player's actions as a function of the stratey played by the row player")
plt.xlabel("$x$")
plt.legend();
```

We can now determine the best response for player 1 based on the value of $x$:

1. If $x < \frac{1}{2}$, then $c_1$ is a best response.
2. If $x > \frac{1}{2}$, then $c_2$ is a best response.
3. If $x = \frac{1}{2}$, then player 1 is **indifferent** between $c_1$ and $c_2$.

This example shows how best responses depend continuously on
the opponent’s strategy, and that indifference can arise at precise
thresholds in strategies.

(thrm:best_response_condition)=

### Theorem: Best Response Condition

---

In a two-player game $(A,\ B) \in \left(\mathbb{R}^{m \times n}\right)^2$,
a strategy $\sigma_r^*$ of the row player is a **best response** to a strategy
$\sigma_c$ of the column player if and only if:

$$
\sigma_{r^*}(i) > 0 \quad \Rightarrow \quad (A \sigma_c^\mathsf{T})_i =
\max_{k \in \mathcal{A}_1}(A \sigma_c^\mathsf{T})_k
\quad \text{for all } i \in \mathcal{A}_1
$$

---

### Proof

The term $(A \sigma_c^\mathsf{T})_i$ represents the utility for the row player
when playing their $i^{\text{th}}$ action. Thus:

$$
\sigma_r A \sigma_c^\mathsf{T} = \sum_{i=1}^{m} \sigma_{r}(i) \cdot (A \sigma_c^\mathsf{T})_i
$$

Let $u = \max_k (A \sigma_c^\mathsf{T})_k$. Then:

$$
\begin{align}
\sigma_r A \sigma_c^\mathsf{T}
&= \sum_{i=1}^{m} \sigma_r(i) \left[u - u + (A \sigma_c^\mathsf{T})_i\right] \\
&= \sum_{i=1}^{m} \sigma_r(i) u - \sum_{i=1}^{m} \sigma_r(i) (u - (A \sigma_c^\mathsf{T})_i) \\
&= u - \sum_{i=1}^{m} \sigma_r(i) (u - (A \sigma_c^\mathsf{T})_i)
\end{align}
$$

Since $u - (A \sigma_c^\mathsf{T})_i \geq 0$ for all $i$,
the maximum expected utility for the row player is $u$, and this occurs **if and only if**:

$$
\sigma_r(i) > 0 \quad \Rightarrow \quad (A \sigma_c^\mathsf{T})_i = u
$$

as required.

---

(sec:rock_paper_scissors_lizard_spock)=

### Example: Rock Paper Scissors Lizard Spock

The classic Rock Paper Scissors game can be extended to
**Rock Paper Scissors Lizard Spock**, where:

- Scissors cuts Paper
- Paper covers Rock
- Rock crushes Lizard
- Lizard poisons Spock
- Spock smashes Scissors
- Scissors decapitates Lizard
- Lizard eats Paper
- Paper disproves Spock
- Spock vaporizes Rock
- Rock crushes Scissors

This results in the following payoff matrices:

$$
M_r =
\begin{pmatrix}
 0 & -1 &  1 &  1 & -1 \\
 1 &  0 & -1 & -1 &  1 \\
-1 &  1 &  0 &  1 & -1 \\
-1 &  1 & -1 &  0 &  1 \\
 1 & -1 &  1 & -1 &  0 \\
\end{pmatrix}
\qquad
M_c = -M_r
$$

```{note}
This is the first example of a [Zero-Sum Game](#chp:zero_sum_games),
where one player’s gain is exactly the other’s loss.
```

We can now use the [Best Response Condition Theorem](#thrm:best_response_condition)
to check whether the strategy
$\sigma_1 = \left(\frac{1}{3},\ 0,\ \frac{1}{3},\ \frac{1}{3},\ 0\right)$
is a best response to
$\sigma_2 = \left(0,\ \frac{1}{4},\ 0,\ 0,\ \frac{3}{4}\right)$.

We begin by computing the expected utilities for each of player 1’s actions:

$$
M_r \sigma_2^\mathsf{T} =
\begin{pmatrix}
0.75 \\
-0.5 \\
0.5 \\
-0.25 \\
-0.5
\end{pmatrix}
$$

From this vector, we observe that:

$$
\max_{k \in \mathcal{A}_1} (A \sigma_2^\mathsf{T})_k = 0.75
$$

```{note}
The set of actions that a strategy $\sigma$ plays with non zero probability is
referred to as the support of $\sigma$.
```

The support of $\sigma_1$ is $\mathcal{S}(\sigma_1) = \{1,\ 3,\ 4\}$.
Among these, only $(A \sigma_2^\mathsf{T})_1 = 0.75$ equals the maximum.

Since $(A \sigma_2^\mathsf{T})_3 = 0.5$ and $(A \sigma_2^\mathsf{T})_4 = -0.25$,
the condition for a best response is not satisfied.

Therefore, $\sigma_1$ is not a best response to $\sigma_2$.
Indeed, the row player should revise their strategy to place positive weight
only on the action that yields the maximum payoff.

## Exercises

(exer:iterated_elimination_of_dominated_strategies)=

### Exercise: Iterated Elimination of Strategies

Use **iterated elimination of dominated strategies** to attempt to predict
rational behaviour in each of the following games. Represent all steps clearly.

1.  $$
    A =
    \begin{pmatrix}
    2 & 1 \\
    1 & 1
    \end{pmatrix}
    \qquad
    B =
    \begin{pmatrix}
    1 & 1 \\
    1 & 3
    \end{pmatrix}
    $$

2.  $$
    A =
    \begin{pmatrix}
    2  & 1 & 3 & 17 \\
    27 & 3 & 1 & 1 \\
    4  & 6 & 7 & 18
    \end{pmatrix}
    \qquad
    B =
    \begin{pmatrix}
    11 & 9  & 10 & 22 \\
    0  & 1  & 1  & 0  \\
    2  & 10 & 12 & 0
    \end{pmatrix}
    $$

3.  $$
    A =
    \begin{pmatrix}
    3 & 3 & 2 \\
    2 & 1 & 3
    \end{pmatrix}
    \qquad
    B =
    \begin{pmatrix}
    2 & 1 & 3 \\
    2 & 3 & 2
    \end{pmatrix}
    $$

4.  $$
    A =
    \begin{pmatrix}
    3 & -1 \\
    2 & 7
    \end{pmatrix}
    \qquad
    B =
    \begin{pmatrix}
    -3 & 1 \\
    1 & -6
    \end{pmatrix}
    $$

---

### Exercise: Identifying Best Responses

For each game in [](#exer:iterated_elimination_of_dominated_strategies):

1. Identify **all best response** actions.
2. Attempt to predict **rational outcomes** using best response reasoning.
3. Explain any instances where this approach **fails to fully determine the outcome**
   (e.g. games with multiple best responses).

---

### Exercise: Representing Peace and War in Normal Form

Model the following real-world conflict scenario as a **normal form game**.

> Two neighbouring countries possess powerful military forces.
>
> - If both attack, each suffers 10,000 civilian casualties.
> - If one attacks while the other remains peaceful, the peaceful country suffers
>   15,000 casualties and retaliates, causing the attacker 13,000 casualties.
> - If both remain peaceful, there are no casualties.

Answer the following:

1. Clearly state the **players** and their **action sets**.
2. Represent the game in **normal form**, assuming utilities are the negative of casualties.
3. Plot the **expected utilities** for each country assuming it plays a generic strategy
   while the other plays:
   - Peaceful
   - Aggressive
4. Identify the **best responses** of each country.

---

### Exercise: Pricing Strategy in Competing Shops

> Two shops on the same street are deciding how to price their product.
> Each can set the price as **Low**, **Medium**, or **High**.
>
> - If both choose the same price, they split the market.
> - If one sets a lower price, they attract more customers but earn less per item.
> - If one sets a higher price, they retain fewer customers but may benefit from higher margins.

1. Define a plausible utility table for both players.
2. Represent the game in normal form using two matrices.
3. Identify and eliminate any actions that are never chosen under rational behaviour.
4. Discuss whether this game has any pairs of actions that are best responses to
   each other.

---

### Exercise: Task Assignment in a Shared Workspace

> Two workers must each choose a task to complete in a shared workspace:
> **Documentation**, **Coding**, or **Debugging**.
>
> - If they choose the same task, productivity drops due to coordination overhead.
> - If they choose different tasks, overall productivity improves.
> - Each task has a different utility value depending on the player's preference and skill.

1. Construct a utility matrix for both players that reflects this scenario.
2. Represent the game in normal form.
3. Are any actions strictly or weakly dominated?
4. Determine best responses for both players.

---

## Programming

### Computing utilities of all actions

[](#thrm:best_response_condition) relies on computing the utilities of all
actions when the other player is playing a specific strategy. This corresponds
to the matrix multiplication:

$$
M_r \sigma_c^\mathsf{T}
$$

Similarly to [](#sec:linear_algebraic_formulation_of_expected_utility) this
enables **efficient numerical computation** in programming
languages that support vectorized matrix operations.

### Computing utilities of all actions with Numpy

Python's numerical library **NumPy** [@harris2020array] provides vectorized operations through
its `array` class. Below, we define the elements from the
[earlier Rock Paper Scissors Lizard Spock example](#sec:rock_paper_scissors_lizard_spock):

```{code-cell} python3
M_r = np.array(
    (
        (0, -1, 1, 1, -1),
        (1, 0, -1, -1, 1),
        (-1, 1, 0, 1, -1),
        (-1, 1, -1, 0, 1),
        (1, -1, 1, -1, 0),
    )
)

sigma_2 = np.array((1 / 4, 0, 0, 3 / 4, 0))
```

We can now compute the expected utility for each of the row player's actions:

```{code-cell} python3
M_r @ sigma_2
```

### Finding non zero entries of an array with Numpy

NumPy gives functionality for finding non zero entries of an array:

```{code-cell} python3
sigma_1 = np.array((1 / 3, 0, 1 / 3, 1 / 3, 0))
sigma_1.nonzero()
```

### Checking the best response condition with Numpy

To check the best response condition with NumPy we can efficiently compare the
location of the non zero values of a strategy with the maximum utility of the
action set.

```{code-cell} python3
(M_r @ sigma_2)[sigma_1.nonzero()] == (M_r @ sigma_2).max()
```

Just as in [](#sec:rock_paper_scissors_lizard_spock) we see that $\sigma_1$ is not
a best response as all the non zero values do not give maximum utility.
If we modify the row player's behaviour to only play the first action then we do
get a best response:

```{code-cell} python3
sigma_1 = np.array((1, 0, 0, 0, 0))
(M_r @ sigma_2)[sigma_1.nonzero()] == (M_r @ sigma_2).max()
```

### Checking best response condition with Nashpy

The Python library **Nashpy** [@knight2018nashpy] can be used to directly check
the best response condition for two strategies. It checks if either strategy is
a best response to each other.

```{code-cell} python3
import nashpy as nash

rpsls = nash.Game(M_r, - M_r)
rpsls.is_best_response(sigma_r=sigma_1, sigma_c=sigma_2)
```

This confirms that $\sigma_1=(1, 0, 0, 0, )$ is a best response to $\sigma_2=(1
/ 4, 0, 0, 3 / 4, 0)$ but not vice versa.

## Notable Research

In [@nash1950equilibrium], John Nash introduced the foundational concept of
**Nash equilibrium**: a strategy profile (i.e., a combination of strategies,
one per player) where each strategy is a best response to the others. In such a
setting, no player has an incentive to unilaterally deviate from their choice.
Nash's landmark result showed that at least one such equilibrium exists in any
finite game — a result that earned him the Nobel Prize in Economics.

More recent research explores how often certain types of equilibria occur. For
instance, [@wiese2022frequency] investigates how frequently **best response
dynamics** (where players iteratively switch to their best response) lead to
convergence at a Nash equilibrium. This builds on earlier work such as
[@dresher1970probability], which studied the likelihood that a game possesses a
Nash equilibrium in actions.

Another line of research explores how the structure of a game influences the
convergence to equilibrium. For example, in congestion games or routing games,
players choose paths through a network, and each player’s cost depends on the
congestion caused by others. These games often admit Nash
equilibria in actions and allow best response dynamics to converge under mild conditions.
This property has led to applications in traffic flow, internet routing, and
load balancing. The work of [@rosenthal1973class] formally introduced this
class of games and remains a cornerstone of algorithmic game theory.

In an applied context, [@knight2017measuring] models interactions between
hospitals under performance-based targets. The authors prove the existence of
an equilibrium in **actions** (as opposed to more general strategies).
This finding provides insight into how policy incentives might be structured to
align hospital decision-making with public health outcomes.

## Conclusion

In this chapter, we introduced fundamental tools for predicting strategic
behaviour: **dominated strategies**, **best responses**, and the assumption of
**common knowledge of rationality**. These ideas allowed us to identify
outcomes that rational players would be unlikely to avoid—such as the
elimination of actions that never perform best and the selection of strategies
that respond optimally to others.

Using both motivating examples and formal definitions, we saw how
**iterated elimination** and **best response analysis** can reveal
plausible behaviours in one-shot games. We also explored how reasoning about
rationality can be extended beyond pure actions to **strategies**,
where probability plays a role in decision-making.

These concepts (summarised in [](#tbl:rationality_summary)) lay the foundation for understanding **equilibrium**—the central
concept where players’ strategies mutually reinforce each other. In the next
chapter, we formalise this idea, introducing **Nash equilibrium** and
exploring its existence, interpretation, and implications across different
types of games.

```{table} Summary of core concepts introduced in this chapter.
:align: center
:class: table-bordered
:label: tbl:rationality_summary

| Concept                         | Description                                                                 |
|---------------------------------|-----------------------------------------------------------------------------|
| Dominated Strategy              | An action that is always worse than another; never rational to play        |
| Iterated Elimination            | Sequentially removing dominated strategies to simplify the game            |
| Best Response                   | The strategy that maximises a player's utility given others' choices       |
| Strategy Profile                | A complete specification of strategies for all players                     |
| Incomplete Strategy Profile     | Strategies for all players except one                                      |
| Common Knowledge of Rationality | All players are rational, and know that others are, recursively            |
| Best Response Condition         | A formal test for optimality in response to a strategy               |

```

```{attention}
If a strategy is never a best response to any opponent strategy, it can
be safely ignored in predicting rational behaviour.
```
