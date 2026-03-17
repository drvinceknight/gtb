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
| **Downtown**     | 1        | 0       | 2      |
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
- UrbanEats opens in **Suburb**: with an expected profit of £4,000

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
u_i(\sigma_i, s_{-i}) \geq u_i(a_i, s_{-i})
\quad \text{for all } s_{-i} \in S_{-i},
$$

and

$$
u_i(\sigma_i, \bar{s}) > u_i(a_i, \bar{s})
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

#### Example: Predicted Behaviour through Iterated Elimination Strategies

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

#### Example: eliminating strategies does not suffice

In many cases, we can simplify a game by eliminating dominated strategies.
However, not all games can be fully resolved using this approach.

Consider the following game.

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

#### Example: Predicted Behaviour through Best Responses in the Action Space

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

#### Example: Predicted Behaviour through Best Responses in the Strategy Space

We can also identify best responses when players use **strategies**.
Let us begin by examining the **Matching Pennies** game.

##### Example: Matching Pennies

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
plt.title("Utility of the row player's actions as a function of the strategy played by the column player")
plt.xlabel("$x$")
plt.legend();
```

From the graph we observe:

1. If $x < \frac{1}{2}$, then $r_2$ is a best response for player 1.
2. If $x > \frac{1}{2}$, then $r_1$ is a best response for player 1.
3. If $x = \frac{1}{2}$, then player 1 is indifferent between $r_1$ and $r_2$.

#### Examples: Coordination Game

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
plt.title("Utility of the column player's actions as a function of the strategy played by the row player")
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

#### Proof

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

#### Example: Rock Paper Scissors Lizard Spock

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

```{exercise} 
:label: iterated_elimination_of_strategies

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

```

```{exercise} 
:label: identifying_best_responses

For each game in [](#iterated_elimination_of_strategies):

1. Identify **all best response** actions.
2. Attempt to predict **rational outcomes** using best response reasoning.
3. Explain any instances where this approach **fails to fully determine the outcome**
   (e.g. games with multiple best responses).
```


```{exercise} 
:label: representing_peace_and_war_in_normal_form

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
```


```{exercise} 
:label: pricing_strategy_in_competing_shops

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
```


```{exercise} 
:label: task_assignment_in_a_shared_workspace

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
```


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

**Iterated elimination** and **best response analysis** reveal plausible behaviours in one-shot games, and both extend naturally to **strategies** where probability plays a role.

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

---

(solutions:rationalisation)=

## Solutions

````{solution} iterated_elimination_of_strategies
:label: solution:iterated_elimination_of_strategies

We apply iterated elimination of dominated strategies to each game.

**Game 1:**

$$
A = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}
\qquad
B = \begin{pmatrix} 1 & 1 \\ 1 & 3 \end{pmatrix}
$$

**Step 1 (Row player):** Compare $r_1 = (2, 1)$ and $r_2 = (1, 1)$. Since $r_1$ gives payoff $2 > 1$ against $c_1$ and payoff $1 = 1$ against $c_2$, row $r_2$ is **weakly dominated** by $r_1$. Eliminate $r_2$.

**Step 2 (Column player):** With only $r_1$ remaining, the column player compares $c_1$ (payoff $1$) and $c_2$ (payoff $1$). Both yield the same payoff, so neither is dominated. We cannot eliminate further.

**Predicted outcome:** $r_1$ is the only rational row choice; the column player is indifferent and may play either column. The prediction is $(r_1, c_1)$ or $(r_1, c_2)$ depending on the column player's tie-breaking.

---

**Game 2:**

$$
A = \begin{pmatrix} 2 & 1 & 3 & 17 \\ 27 & 3 & 1 & 1 \\ 4 & 6 & 7 & 18 \end{pmatrix}
\qquad
B = \begin{pmatrix} 11 & 9 & 10 & 22 \\ 0 & 1 & 1 & 0 \\ 2 & 10 & 12 & 0 \end{pmatrix}
$$

**Step 1 (Row player):** Compare each row:

- $r_1 = (2, 1, 3, 17)$
- $r_2 = (27, 3, 1, 1)$
- $r_3 = (4, 6, 7, 18)$

Comparing $r_1$ and $r_3$: $r_3$ gives $4 > 2$, $6 > 1$, $7 > 3$, $18 > 17$ against all columns. So $r_1$ is **strictly dominated** by $r_3$. Eliminate $r_1$.

**Step 2 (Column player):** With $r_2$ and $r_3$ remaining, the column payoffs are:

$$
B' = \begin{pmatrix} 0 & 1 & 1 & 0 \\ 2 & 10 & 12 & 0 \end{pmatrix}
$$

Compare each column for the column player. Looking at $c_4$: against $r_2$ it gives $0$, against $r_3$ it gives $0$. Column $c_1$: against $r_2$ gives $0$, against $r_3$ gives $2$. So $c_4$ is weakly dominated by $c_1$ (same against $r_2$, worse against $r_3$). Eliminate $c_4$.

**Step 3 (Column player):** With columns $c_1, c_2, c_3$ remaining:

$$
B'' = \begin{pmatrix} 0 & 1 & 1 \\ 2 & 10 & 12 \end{pmatrix}
$$

Compare $c_1$ vs $c_2$: $c_2$ gives $1 > 0$ against $r_2$ and $10 > 2$ against $r_3$. So $c_1$ is **strictly dominated** by $c_2$. Eliminate $c_1$.

**Step 4 (Row player):** With $r_2$, $r_3$ and columns $c_2$, $c_3$:

$$
A'' = \begin{pmatrix} 3 & 1 \\ 6 & 7 \end{pmatrix}
$$

Compare $r_2 = (3, 1)$ and $r_3 = (6, 7)$: $r_3$ strictly dominates $r_2$ on both entries. Eliminate $r_2$.

**Step 5 (Column player):** With only $r_3$ and columns $c_2$, $c_3$:

$$
B''' = \begin{pmatrix} 10 & 12 \end{pmatrix}
$$

$c_3$ gives $12 > 10$, so $c_2$ is strictly dominated by $c_3$. Eliminate $c_2$.

**Predicted outcome:** $(r_3, c_3)$.

---

**Game 3:**

$$
A = \begin{pmatrix} 3 & 3 & 2 \\ 2 & 1 & 3 \end{pmatrix}
\qquad
B = \begin{pmatrix} 2 & 1 & 3 \\ 2 & 3 & 2 \end{pmatrix}
$$

**Step 1 (Column player):** Compare columns for the column player:

- $c_1$ gives $(2, 2)$, $c_2$ gives $(1, 3)$, $c_3$ gives $(3, 2)$.

No column is dominated (each column is best for a different row). Check $c_1$ vs $c_3$: $c_3$ gives $3 > 2$ against $r_1$ but $2 = 2$ against $r_2$. So $c_1$ is **weakly dominated** by $c_3$. Eliminate $c_1$.

**Step 2 (Row player):** With $c_2$ and $c_3$ remaining:

$$
A' = \begin{pmatrix} 3 & 2 \\ 1 & 3 \end{pmatrix}
$$

Compare $r_1 = (3, 2)$ and $r_2 = (1, 3)$: neither dominates the other (row 1 is better against $c_2$, row 2 is better against $c_3$). We cannot eliminate further.

**Result:** Iterated elimination of weakly dominated strategies reduces the game to:

$$
A' = \begin{pmatrix} 3 & 2 \\ 1 & 3 \end{pmatrix}
\qquad
B' = \begin{pmatrix} 1 & 3 \\ 3 & 2 \end{pmatrix}
$$

No unique prediction is obtained. Further analysis (e.g.\ best responses) is required.

---

**Game 4:**

$$
A = \begin{pmatrix} 3 & -1 \\ 2 & 7 \end{pmatrix}
\qquad
B = \begin{pmatrix} -3 & 1 \\ 1 & -6 \end{pmatrix}
$$

**Row player:** Compare $r_1 = (3, -1)$ and $r_2 = (2, 7)$. Neither dominates: $r_1 > r_2$ against $c_1$, but $r_2 > r_1$ against $c_2$.

**Column player:** Compare $c_1 = (-3, 1)$ and $c_2 = (1, -6)$ for column payoffs. Neither dominates: $c_2 > c_1$ against $r_1$, but $c_1 > c_2$ against $r_2$.

**Result:** No strategies can be eliminated. Iterated elimination does not reduce this game.

```{code-cell} python3
import nashpy as nash
import numpy as np

# Game 1
A1 = np.array([[2, 1], [1, 1]])
B1 = np.array([[1, 1], [1, 3]])
print("Game 1 - checking: r2 weakly dominated by r1?",
      all(A1[0, :] >= A1[1, :]) and any(A1[0, :] > A1[1, :]))

# Game 2
A2 = np.array([[2, 1, 3, 17], [27, 3, 1, 1], [4, 6, 7, 18]])
B2 = np.array([[11, 9, 10, 22], [0, 1, 1, 0], [2, 10, 12, 0]])
print("Game 2 - r3 strictly dominates r1?",
      all(A2[2, :] > A2[0, :]))
```

````

---

````{solution} identifying_best_responses
:label: solution:identifying_best_responses

We identify all best response actions for each game in [](#iterated_elimination_of_strategies) and attempt to predict rational outcomes.

**Game 1:**

$$
A = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}
\qquad
B = \begin{pmatrix} 1 & 1 \\ 1 & 3 \end{pmatrix}
$$

Underline best responses (maximum in each column for the row player, maximum in each row for the column player):

$$
A = \begin{pmatrix} \underline{2} & 1 \\ 1 & 1 \end{pmatrix}
\qquad
B = \begin{pmatrix} 1 & \underline{1} \\ 1 & \underline{3} \end{pmatrix}
$$

- Row player: $r_1$ is the unique best response to $c_1$; both $r_1$ and $r_2$ are best responses to $c_2$.
- Column player: Both $c_1$ and $c_2$ are best responses to $r_1$ (payoff tied at $1$); $c_2$ is the unique best response to $r_2$.

Pairs where both are mutual best responses: $(r_1, c_1)$ and $(r_1, c_2)$. However $(r_1, c_1)$ requires column player to choose $c_1$ over $c_2$ even though both are tied — there is no strict incentive. Both $(r_1, c_1)$ and $(r_1, c_2)$ are predicted rational outcomes.

---

**Game 2:**

$$
A = \begin{pmatrix} 2 & 1 & 3 & 17 \\ 27 & 3 & 1 & 1 \\ 4 & 6 & 7 & 18 \end{pmatrix}
\qquad
B = \begin{pmatrix} 11 & 9 & 10 & 22 \\ 0 & 1 & 1 & 0 \\ 2 & 10 & 12 & 0 \end{pmatrix}
$$

Best response underlines:

$$
A = \begin{pmatrix} 2 & 1 & 3 & 17 \\ \underline{27} & 3 & 1 & 1 \\ 4 & \underline{6} & \underline{7} & \underline{18} \end{pmatrix}
\qquad
B = \begin{pmatrix} \underline{11} & \underline{9} & \underline{10} & \underline{22} \\ 0 & 1 & 1 & 0 \\ 2 & 10 & \underline{12} & 0 \end{pmatrix}
$$

- Row player: $r_2$ is best response to $c_1$; $r_3$ is best response to $c_2$, $c_3$, and $c_4$.
- Column player: $c_4$ is best response to $r_1$; $c_1$, $c_2$, $c_3$, $c_4$ are all best responses to $r_2$ (checking: $B$ row 2 is $(0,1,1,0)$ — $c_2$ and $c_3$ tied); $c_3$ is best response to $r_3$.

The unique mutual best response pair is $(r_3, c_3)$, confirming the predicted outcome from iterated elimination.

---

**Game 3:**

$$
A = \begin{pmatrix} 3 & 3 & 2 \\ 2 & 1 & 3 \end{pmatrix}
\qquad
B = \begin{pmatrix} 2 & 1 & 3 \\ 2 & 3 & 2 \end{pmatrix}
$$

Best response underlines:

$$
A = \begin{pmatrix} \underline{3} & \underline{3} & 2 \\ 2 & 1 & \underline{3} \end{pmatrix}
\qquad
B = \begin{pmatrix} \underline{2} & 1 & \underline{3} \\ \underline{2} & \underline{3} & 2 \end{pmatrix}
$$

- Row player: $r_1$ is best response to $c_1$ and $c_2$; $r_2$ is best response to $c_3$; both are tied against $c_1$ for payoff $3$ vs $2$ (no, $3 > 2$ so $r_1$ is unique best response to $c_1$). Actually $r_1$ gives $3$ against both $c_1$ and $c_2$, and $r_2$ gives $3$ against $c_3$.
- Column player: $c_1$ is best response to $r_1$ (payoff $2$) and $r_2$ (payoff $2$); $c_2$ is best response to $r_2$ (payoff $3$); $c_3$ is best response to $r_1$ (payoff $3$).

Pairs where both are mutual best responses:
- $(r_1, c_3)$: $r_1$ gives $2$ against $c_3$ (not a best response since $r_2$ gives $3$ against $c_3$). Not a NE.
- $(r_2, c_2)$: $r_2$ gives $1$ against $c_2$, but $r_1$ gives $3$. Not a NE.
- $(r_1, c_1)$: $r_1$ is best response to $c_1$ (payoff $3 > 2$); $c_1$ gives column payoff $2$, but $c_3$ gives $3 > 2$. So $c_1$ is not a best response to $r_1$. Not a NE.

No pure strategy Nash equilibrium exists. The approach of pure strategy best responses fails to fully determine the outcome; mixed strategies are required, illustrating a case where best response analysis in the action space does not resolve the game.

---

**Game 4:**

$$
A = \begin{pmatrix} 3 & -1 \\ 2 & 7 \end{pmatrix}
\qquad
B = \begin{pmatrix} -3 & 1 \\ 1 & -6 \end{pmatrix}
$$

Best response underlines:

$$
A = \begin{pmatrix} \underline{3} & -1 \\ 2 & \underline{7} \end{pmatrix}
\qquad
B = \begin{pmatrix} -3 & \underline{1} \\ \underline{1} & -6 \end{pmatrix}
$$

- Row player: $r_1$ is best response to $c_1$; $r_2$ is best response to $c_2$.
- Column player: $c_2$ is best response to $r_1$; $c_1$ is best response to $r_2$.

No action profile has both entries underlined simultaneously — there is **no pure strategy Nash equilibrium**. Best response reasoning fails to determine the outcome from the action space alone; a mixed strategy equilibrium must exist (guaranteed by Nash's theorem).

```{code-cell} python3
import nashpy as nash
import numpy as np

# Game 1
A1 = np.array([[2, 1], [1, 1]])
B1 = np.array([[1, 1], [1, 3]])
g1 = nash.Game(A1, B1)
print("Game 1 Nash equilibria:", list(g1.support_enumeration()))

# Game 2
A2 = np.array([[2, 1, 3, 17], [27, 3, 1, 1], [4, 6, 7, 18]])
B2 = np.array([[11, 9, 10, 22], [0, 1, 1, 0], [2, 10, 12, 0]])
g2 = nash.Game(A2, B2)
print("Game 2 Nash equilibria:", list(g2.support_enumeration()))

# Game 3
A3 = np.array([[3, 3, 2], [2, 1, 3]])
B3 = np.array([[2, 1, 3], [2, 3, 2]])
g3 = nash.Game(A3, B3)
print("Game 3 Nash equilibria:", list(g3.support_enumeration()))

# Game 4
A4 = np.array([[3, -1], [2, 7]])
B4 = np.array([[-3, 1], [1, -6]])
g4 = nash.Game(A4, B4)
print("Game 4 Nash equilibria:", list(g4.support_enumeration()))
```

````

---

````{solution} representing_peace_and_war_in_normal_form
:label: solution:representing_peace_and_war_in_normal_form

1. **Players and action sets:**

The players are Country 1 and Country 2 (the row and column players). The action sets are:

$$
\mathcal{A}_1 = \mathcal{A}_2 = \{\text{Peace},\ \text{Attack}\}
$$

2. **Normal form with utilities as negative of casualties:**

$$
M_r = \begin{pmatrix}
0 & -15000 \\
-13000 & -10000
\end{pmatrix}
\qquad
M_c = \begin{pmatrix}
0 & -13000 \\
-15000 & -10000
\end{pmatrix}
$$

Rows and columns correspond to (Peace, Attack). When Country 1 attacks and Country 2 is peaceful, Country 1 suffers $13000$ casualties (from retaliation) and Country 2 suffers $15000$ casualties.

3. **Expected utility plots:**

Let $\sigma_1 = (x, 1-x)$ where $x$ is the probability Country 1 plays Peace.

When Country 2 plays Peace ($\sigma_2 = (1, 0)$):

$$
u_1(x, \text{Peace}) = 0 \cdot x + (-13000)(1-x) = -13000 + 13000x
$$

When Country 2 plays Attack ($\sigma_2 = (0, 1)$):

$$
u_1(x, \text{Attack}) = (-15000) x + (-10000)(1-x) = -10000 - 5000x
$$

```{code-cell} python3
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 100)

u1_peace = -13000 + 13000 * x
u1_attack = -10000 - 5000 * x

plt.figure(figsize=(7, 3))

plt.subplot(1, 2, 1)
plt.plot(x, u1_peace, label="Country 2 plays Peace")
plt.plot(x, u1_attack, label="Country 2 plays Attack")
plt.xlabel("Probability of Peace ($x$)")
plt.ylabel("Expected utility for Country 1")
plt.title("Country 1 expected utility")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x, u1_peace, label="Country 1 plays Peace")
plt.plot(x, u1_attack, label="Country 1 plays Attack")
plt.xlabel("Probability of Peace ($x$)")
plt.ylabel("Expected utility for Country 2")
plt.title("Country 2 expected utility (symmetric)")
plt.legend()

plt.tight_layout()
```

4. **Best responses:**

For Country 1:

- When Country 2 plays Peace: $u_1(\text{Peace}) = 0$ and $u_1(\text{Attack}) = -13000$. So **Peace** is the best response.
- When Country 2 plays Attack: $u_1(\text{Peace}) = -15000$ and $u_1(\text{Attack}) = -10000$. So **Attack** is the best response.

By symmetry the same holds for Country 2.

Thus Attack is not universally dominant here (Peace is best when the opponent is peaceful). The game has two pure Nash equilibria: (Peace, Peace) and (Attack, Attack), as well as a mixed strategy equilibrium. This differs from the pure Prisoners' Dilemma structure where Attack is always dominant. The specific casualty values give a coordination element: both countries prefer mutual peace, but mutual attack is also a self-reinforcing outcome once fear of unilateral peaceful behaviour takes hold.

````

---

````{solution} pricing_strategy_in_competing_shops
:label: solution:pricing_strategy_in_competing_shops

1. **Plausible utility table:**

We define utilities to reflect the trade-off between market share and margin. Let the total market profit be normalised so that equal pricing splits it. A lower price steals customers but earns less per unit; a higher price loses customers but earns more per unit (up to a point).

A plausible assignment (in arbitrary units) for Shop 1 (row) and Shop 2 (column):

$$
M_r = \begin{pmatrix}
3 & 5 & 6 \\
1 & 3 & 5 \\
0 & 1 & 3
\end{pmatrix}
\qquad
M_c = \begin{pmatrix}
3 & 1 & 0 \\
5 & 3 & 1 \\
6 & 5 & 3
\end{pmatrix}
$$

where rows/columns correspond to (Low, Medium, High). When prices are equal, each shop earns $3$. When Shop 1 undercuts Shop 2, Shop 1 earns more and Shop 2 earns less.

2. **Normal form:** The game is represented by the two matrices $M_r$ and $M_c$ above.

3. **Iterated elimination of dominated strategies:**

For the row player, compare High ($0, 1, 3$) to Medium ($1, 3, 5$): Medium gives strictly higher payoff against all column actions. High is **strictly dominated** by Medium. Eliminate High for the row player.

By symmetry (the game is symmetric under reflection), High is also **strictly dominated** for the column player. Eliminate the High column.

After elimination:

$$
M_r' = \begin{pmatrix}
3 & 5 \\
1 & 3
\end{pmatrix}
\qquad
M_c' = \begin{pmatrix}
3 & 1 \\
5 & 3
\end{pmatrix}
$$

Now compare Low ($3, 5$) to Medium ($1, 3$) for the row player: Low strictly dominates Medium (in the reduced game). Eliminate Medium.

By symmetry eliminate Medium for the column player.

After full elimination: both shops play **Low**.

4. **Best response pairs:**

After iterated elimination, the only remaining action for both players is Low. (Low, Low) is a pair of best responses. In the fully reduced $1 \times 1$ game the unique outcome is mutual Low pricing — consistent with a Prisoners' Dilemma-like structure where competitive pressure drives prices down even though both shops would prefer mutual Medium or High pricing.

```{code-cell} python3
import nashpy as nash
import numpy as np

M_r = np.array([[3, 5, 6], [1, 3, 5], [0, 1, 3]])
M_c = np.array([[3, 1, 0], [5, 3, 1], [6, 5, 3]])

g = nash.Game(M_r, M_c)
print("Nash equilibria:", list(g.support_enumeration()))
```

````

---

````{solution} task_assignment_in_a_shared_workspace
:label: solution:task_assignment_in_a_shared_workspace

1. **Utility matrix construction:**

Let Worker 1 be the row player and Worker 2 be the column player. Actions are Documentation (D), Coding (C), Debugging (Db). Utilities reflect:
- If same task: penalty for coordination overhead, base utility reduced.
- If different tasks: bonus for complementary work.
- Each worker has individual skill strengths: Worker 1 is better at Coding, Worker 2 is better at Debugging.

$$
M_r = \begin{pmatrix}
1 & 3 & 4 \\
4 & 2 & 5 \\
3 & 4 & 1
\end{pmatrix}
\qquad
M_c = \begin{pmatrix}
1 & 4 & 3 \\
3 & 2 & 4 \\
5 & 4 & 1
\end{pmatrix}
$$

Rows/columns correspond to (Documentation, Coding, Debugging). Diagonal entries are lower (same task, coordination overhead). Off-diagonal entries are higher (different tasks, complementary productivity).

2. **Normal form:** The game is represented by $M_r$ and $M_c$ above.

3. **Dominated strategies:**

For the row player, compare Documentation ($1, 3, 4$) and Coding ($4, 2, 5$):
- Against Documentation: Coding gives $4 > 1$.
- Against Coding: Documentation gives $3 > 2$.

Neither dominates the other. Compare Documentation and Debugging ($3, 4, 1$):
- Against Documentation: Debugging gives $3 > 1$.
- Against Coding: Debugging gives $4 > 3$.
- Against Debugging: Documentation gives $4 > 1$.

No strategy is strictly dominated by a single other strategy. No actions are strictly dominated; we would need to check domination by mixtures. For this illustrative matrix, no pure strategy is strictly or weakly dominated.

4. **Best responses:**

Underline row player's best responses (column-wise maxima) and column player's best responses (row-wise maxima):

$$
M_r = \begin{pmatrix}
1 & 3 & 4 \\
\underline{4} & 2 & \underline{5} \\
3 & \underline{4} & 1
\end{pmatrix}
\qquad
M_c = \begin{pmatrix}
1 & 4 & 3 \\
3 & 2 & \underline{4} \\
\underline{5} & \underline{4} & 1
\end{pmatrix}
$$

- Row player: $r_2$ (Coding) is best response to $c_1$ (Documentation) and $c_3$ (Debugging); $r_3$ (Debugging) is best response to $c_2$ (Coding).
- Column player: $c_3$ (Debugging) is best response to $r_2$ (Coding); $c_1$ (Documentation) and $c_2$ (Coding) are both best responses to $r_3$ (Debugging).

The unique mutual best response pair: $(r_2, c_3)$ — Worker 1 codes and Worker 2 debugs. This is a Nash equilibrium in pure actions, consistent with the intuition that workers should specialise in complementary tasks.

```{code-cell} python3
import nashpy as nash
import numpy as np

M_r = np.array([[1, 3, 4], [4, 2, 5], [3, 4, 1]])
M_c = np.array([[1, 4, 3], [3, 2, 4], [5, 4, 1]])

g = nash.Game(M_r, M_c)
print("Nash equilibria:", list(g.support_enumeration()))
```

````
