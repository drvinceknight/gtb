---
kernelspec:
  name: python3
  display_name: "Python 3"
---

(chp:repeated_games)=

# Repeated Games

When the same game is played repeatedly, players can condition future behaviour
on past actions, opening the door to cooperation that would be impossible in a
one-shot interaction. This chapter shows how indefinite repetition can sustain
cooperative outcomes, culminating in the Folk Theorem.

(example:repeated-contractor-game)=

## Motivating Example: Construction Contractors

Consider two local construction firms, **Firm A** and **Firm B**, who
regularly bid on municipal infrastructure projects.

Each quarter, the city may announce a new contract for firms to bid on — a school,
a road, or a public facility. These firms can choose to:

- **Bid High (H)**: maintain high prices and sustain mutual profitability, or
- **Bid Low (L)**: undercut the other firm to win the project outright.

If both firms bid high, they enjoy good margins and may take turns winning contracts.
If one undercuts while the other bids high, the undercutter wins the project and earns
a higher profit, at the cost of undermining trust. If both bid low, a price war ensues,
shrinking profits for both.

However, the number of projects is not fixed in advance. After each bidding round,
there is a probability $\delta \in (0, 1)$ that **another project becomes available**.
Thus, the game is repeated probabilistically, with continuation probability $\delta$.
The expected number of repetitions is $\frac{1}{1 - \delta}$.

Each firm chooses an action in each round:

- $H$: Bid High
- $L$: Bid Low

The one-shot payoff matrix is given by:

```{math}
M_r = \begin{pmatrix}
3 & 0\\
5 & 1
\end{pmatrix}
\qquad
M_c = \begin{pmatrix}
3 & 5\\
0 & 1
\end{pmatrix}
```

This is a classic example of a [Prisoner’s Dilemma](#exam:prisoners_dilemma):
short-term incentives tempt each player to defect
(bid low), but long-term cooperation (bid high) could yield better payoffs.

The remainder of this chapter will explore:

- How cooperation can be sustained using history-dependent strategies.
- What conditions on $\delta$ allow for equilibrium cooperation.
- The formal statement and implications of the **Folk Theorem**.

## Theory

### Definition: repeated game

Given a two player game $(A,B)\in\mathbb{R}^{{m\times n}^2}$, referred to as a
stage game, a $T$-stage repeated game is a game in which players play that
stage game for $T>0$ repetitions. Players make decisions based on the full
history of play over all the repetitions.

#### Example: Counting leaves in repeated games

Consider the following stage games and values of $T$. How many leaves would the
extensive form representation of the repeated game have?

1.

$$
M_r = \begin{pmatrix}1 & 2 \\ 2 & 3\end{pmatrix}
\qquad
M_c = \begin{pmatrix}2 & 3 \\ 1 & -1\end{pmatrix}
\qquad
T = 2
$$

The initial play of the game has 4 outcomes (2 actions each). Each of these
leads to 4 more in the second stage. Total: $4 \times 4 = 16$ leaves.

2.

$$
M_r = \begin{pmatrix}0 & 1 \\ -1 & 3\end{pmatrix}
\qquad
M_c = - M_r
\qquad
T = 2
$$

Same as (1): $4 \times 4 = 16$ leaves.

(sec:definition_of_strategies_in_repeated_games)=

### Definition: Strategies in a repeated game

A strategy for a player in a repeated game is a mapping from all possible
histories of play to a probability distribution over the action set of the
stage game.

#### Example: Validity of repeated game strategies

For the [Coordination Game](#sec:coordination_game) with $T=2$
determine whether the following strategy pairs are valid, and if so, what
outcome they lead to.

1. Row player:

$$
\begin{align*}
    (\emptyset, \emptyset) &\to C\\
    (S, S) &\to C\\
    (S, C) &\to C\\
    (C, S) &\to S\\
    (C, C) &\to S\\
\end{align*}
$$

Column player:

$$
\begin{align*}
    (\emptyset, \emptyset) &\to S\\
    (S, S) &\to C\\
    (S, C) &\to C\\
    (C, S) &\to S\\
    (C, C) &\to S\\
\end{align*}
$$

Valid strategy pair. Outcome: $(3,2)$ (corresponds to $O_9$ in the extensive form).

2. Row player:

$$
\begin{align*}
    (\emptyset, \emptyset) &\to C\\
    (S, S) &\to C\\
    (C, S) &\to S\\
    (C, C) &\to S\\
\end{align*}
$$

Column player:

$$
\begin{align*}
    (\emptyset, \emptyset) &\to S\\
    (S, S) &\to C\\
    (S, C) &\to C\\
    (C, S) &\to S\\
    (C, C) &\to S\\
\end{align*}
$$

Invalid: the row player does not define an action for history $(S, C)$.

3. Row player:

$$
\begin{align*}
    (\emptyset, \emptyset) &\to C\\
    (S, S) &\to C\\
    (C, S) &\to S\\
    (S, C) &\to S\\
    (C, C) &\to S\\
\end{align*}
$$

Column player:

$$
\begin{align*}
    (\emptyset, \emptyset) &\to S\\
    (S, S) &\to C\\
    (S, C) &\to C\\
    (C, S) &\to \alpha\\
    (C, C) &\to S\\
\end{align*}
$$

Invalid: column player uses an invalid action $\alpha$.

4. Row player:

$$
\begin{align*}
    (\emptyset, \emptyset) &\to S\\
    (S, S) &\to C\\
    (C, S) &\to S\\
    (S, C) &\to C\\
    (C, C) &\to S\\
\end{align*}
$$

Column player:

$$
\begin{align*}
    (\emptyset, \emptyset) &\to S\\
    (S, S) &\to C\\
    (S, C) &\to C\\
    (C, S) &\to S\\
    (C, C) &\to S\\
\end{align*}
$$

Valid strategy pair. Outcome: $(5,5)$ (corresponds to $O_4$ in the extensive form).

### Theorem: Subgame perfection of sequence of stage Nash profiles

---

For any repeated game, any sequence of stage Nash profiles gives the outcome of a
subgame perfect Nash equilibrium.

---

Where by stage Nash profile we refer to a strategy profile that is a Nash Equilibrium in the stage game.

#### Proof

---

If we consider the strategy given by:

> "Player $i$ should play strategy $\tilde s^{(k)}_i$ regardless of the play of any previous strategy profiles."

where $\tilde s^{(k)}_i$ is the strategy played by player $i$ in any stage Nash profile.
The $k$ is used to indicate that all players play strategies from the same stage Nash profile.

Using backwards induction we see that this strategy is a Nash equilibrium.
Furthermore it is a stage Nash profile so it is a Nash equilibria for the
last stage game which is the last subgame.
If we consider (in an inductive way) each subsequent subgame the result holds.

---

#### Example

Consider the following stage game:

$$
M_r=\begin{pmatrix}
2&0&1\\
0&1&0\\
\end{pmatrix}
\qquad
M_c=\begin{pmatrix}
3&2&4\\
1&2&0\\
\end{pmatrix}
$$

There are two Nash equilibria in action space for this stage game:

$$
(r_1, c_3)\qquad(r_2, c_2)
$$

For $T=2$ we have 4 possible outcomes that correspond to the outcome of a subgame perfect Nash equilibria:

$$(r_1r_1,c_3c_3)\text{ giving utility vector: }(2,8)$$

$$(r_1r_2,c_3c_2)\text{ giving utility vector: }(2,6)$$

$$(r_2r_1,c_2c_3)\text{ giving utility vector: }(2,6)$$

$$(r_2r_2,c_2c_2)\text{ giving utility vector: }(2,4)$$

Importantly, not all subgame Nash equilibria outcomes are of the above form.

### Reputation

In a repeated game it is possible for players to encode reputation and trust in
their strategies.

#### Example: Reputation in a repeated game

Consider the following stage game with $T=2$:

$$
A =
    \begin{pmatrix}
        0 & 6 & 1\\
        1 & 7 & 5
    \end{pmatrix}
\qquad
B =
    \begin{pmatrix}
        0 & 3 & 1\\
        1 & 0 & 1
    \end{pmatrix}
$$

Through inspection it is possible to verify that the following strategy pair is
a Nash equilibrium.

For the row player:

$$
\begin{align*}
    (\emptyset, \emptyset) &\to r_1\\
    (r_1, c_1) &\to r_2\\
    (r_1, c_2) &\to r_2\\
    (r_1, c_3) &\to r_2\\
    (r_2, c_1) &\to r_2\\
    (r_2, c_2) &\to r_2\\
    (r_2, c_3) &\to r_2\\
\end{align*}
$$

For the column player:

$$
\begin{align*}
    (\emptyset, \emptyset) &\to c_2\\
    (r_1, c_1) &\to c_3\\
    (r_2, c_1) &\to c_1\\
    (r_1, c_2) &\to c_3\\
    (r_2, c_2) &\to c_1\\
    (r_1, c_3) &\to c_3\\
    (r_2, c_3) &\to c_1\\
\end{align*}
$$

This pair of strategies corresponds to the following scenario:

The row player plays $r_1$ and the column player plays $c_2$ in the first
stage. The row player plays $r_2$ and the column player plays $c_3$ in the
second stage.

Note that if the row player deviates and plays $r_2$ in the first stage, then
the column player will play $c_1$ in the second stage.

If both players play these strategies, their utilities are: $(11, 4)$, which is
better **for both players** than the utilities at any sequence of stage
Nash equilibria in action space.

**But is this a Nash equilibrium?** To find out, we investigate whether either
player has an incentive to deviate.

1. If the row player deviates, they would only be rational to do so in the
   first stage. If they did, they would gain 1 in that stage but lose 4 in the
   second stage. Thus they have no incentive to deviate.
2. If the column player deviates, they would only do so in the first stage and
   gain no utility.

Thus, this strategy pair **is a Nash equilibrium** and evidences how reputation
can be built and cooperation can emerge from complex dynamics.

### Definition: Infinitely Repeated Game with Discounting

---

Given a two player game $(A,B)\in\mathbb{R}^{{m\times n}^2}$, referred to as a
stage game, an infinitely repeated game with discounting factor $\delta$ is a
game in which players play that stage game an infinite amount of times and gain
the following utility:

$$
U(s_r, s_c) = \sum_{i=0}^{\infty}\delta ^ i u(s_r(i), s_c(i))
$$

where $u(s_r(i), s_c(i))$ denotes the utility obtained in the stage game for
actions $s_r(i)$ and $s_c(i)$ which are the actions given by strategies $s_r$
and $s_c$ at stage $i$.

---

```{note}
The interpretation of $\delta$ can be twofold. Firsly it can be thought of as a
common economic tool to reduce value of future gains. Secondly it can be thought
of as a probability of the game ending.
```

(exam:utility_with_discounting)=

#### Example:

Consider [](#example:repeated-contractor-game) and assume Firm A plans to undercut at
all contracts: bidding low. Firm B plans to start by
cooperating (bidding high) but if Firm A ever undercuts then Firm B will undercut for all
subsequent contracts.

$$
\begin{align*}
U_A(s_r, s_c) &= \sum_{i=0}^{\infty}\delta ^ i u_A(s_r(i), s_c(i)) \\
              &= u_A(L, H) + \sum_{i=1}^{\infty} \delta ^{i} u_A(L, L) \\
              &=  u_A(L, H) +  u_A(L, L)\sum_{i=1}^{\infty} \delta ^{i}\\
              &= u_A(L, H) + u_A(L, L) \frac{\delta}{1-\delta}
\end{align*}
$$

and

$$
\begin{align*}
U_B(s_r, s_c) &= \sum_{i=0}^{\infty}\delta ^ i u_B(s_r(i), s_c(i)) \\
              &= u_B(L, H) + \sum_{i=1}^{\infty} \delta ^{i} u_B(L, L) \\
              &=  u_B(L, H) +  u_B(L, L)\sum_{i=1}^{\infty} \delta ^{i}\\
              &= u_B(L, H) + u_B(L, L) \frac{\delta}{1-\delta}
\end{align*}
$$

Replacing the values from the stage game this gives:

$$
U_A(s_r, s_c)= 5 + \frac{\delta}{1-\delta}
\qquad
U_B(s_r, s_c)= 0 + \frac{\delta}{1-\delta}
$$

### Definition: Average utility

If we interpret $\delta$ as the probability of the repeated game not ending then the _average_ length of the game is:

$$\bar T=\frac{1}{1-\delta}$$

We can use this to define the **average payoff** per stage:

$$\bar U_i(r,c)=(1-\delta)U_i(r,c)$$

#### Example:

Consider 3 strategies for [](#example:repeated-contractor-game):

- $S_c$ Always cooperate: bid high on all contracts.
- $S_d$ Always defect: bid low on all contracts.
- $S_g$ Grudger: bid high until facing a low bid and then bid low for ever.

For $\delta \in (1/4, 3/4)$:

1. Obtain the 3 by 3 Normal form game using average utility.
2. Check if mutual cooperation is a Nash equilibrium for both games.

We construct the Normal Form game representation with the 3 strategies becoming
the action space (as described in [](#sec:mapping_extensive_form_games_to_normal_form)).

We see that if $S_c$ is played against $S_g$ then both players cooperate at each
stage giving:

$$\bar U_r(S_c, S_c)=\bar U_r(S_g, S_g)=\bar U_r(S_g, S_c)=\bar U_r(S_c, S_g)=(1-\delta)\frac{3}{1-\delta}=3$$

For $S_d$ and $S_c$ we have:

$$
\bar U_r(S_d, S_c)=5
$$

$$
\bar U_r(S_d, S_d)=1
$$

$$
\bar U_r(S_c, S_d)=0
$$

For $S_g$ and $S_d$ we
repeat the calculations of [](#exam:utility_with_discounting) to obtain:

$$
\bar U_r(S_g, S_d) = (1 - \delta)\left(0 + \sum_{i=1}^{\infty}\delta
^i\right)=(1-\delta)\frac{\delta}{1-\delta}=\delta
$$

and

$$
\bar U_r(S_d, S_g) = (1 - \delta)\left(5 + \sum_{i=1}^{\infty}\delta
^i\right)=(1-\delta)5 + (1-\delta)\frac{\delta}{1-\delta}=5-4\delta
$$

Using the action space ordered as: $\{S_c, S_d, S_g\}$ this gives:

$$
M_r = \begin{pmatrix}
        3 & 0 & 3\\
        5 & 1 & 5 - 4\delta\\
        3 & \delta & 3\\
      \end{pmatrix}
$$

The game is symmetric so:

$$
M_c=M_r^T
$$

For $\delta=1/4$ this gives:

$$
M_r = \begin{pmatrix}
        3 & 0 & 3\\
        \underline{5} & \underline{1} & \underline{4}\\
        3 & \frac{1}{4} & 3\\
      \end{pmatrix}
$$

The game is symmetric so:

$$
M_c = \begin{pmatrix}
        3 & \underline{5} & 3\\
        0 & \underline{1} & \frac{1}{4}\\
        3 & \underline{4} & 3\\
      \end{pmatrix}
$$

We see that $s_c$ and $s_g$ are both dominated by $s_d$ thus mutual cooperation
is not a Nash equilibrium.

For $\delta=3/4$ this gives:

$$
M_r = \begin{pmatrix}
        3 & 0 & \underline{3}\\
        \underline{5} & \underline{1} & 2\\
        3 & \frac{3}{4} & \underline{3}\\
      \end{pmatrix}
$$

The game is symmetric so:

$$
M_c = \begin{pmatrix}
        3 & \underline{5} & 3\\
        0 & \underline{1} & \frac{3}{4}\\
        \underline{3} & 2 & \underline{3}\\
      \end{pmatrix}
$$

We see that mutual cooperation now is a Nash equilibrium because $s_g$ is now a
best response to $s_g$.

The fact that cooperation can be stable for a higher value of $\delta$ is in
fact a theorem that holds in the general case.

We need one final definition to describe what we imply:

### Definition of individually rational payoffs

---

**Individually rational payoffs** are average payoffs that exceed the stage game Nash equilibrium payoffs for both players.

---

As an example consider the plot corresponding to a repeated Prisoner's Dilemma
shown in [](#fig:convex_hull_of_payoffs_for_prisoners_dilemma).

```{figure} ./images/convex_hull_of_payoffs_for_prisoners_dilemma/main.png
:alt: A 2 dimension polygon
:label: fig:convex_hull_of_payoffs_for_prisoners_dilemma
:height: 250px

The convex hull of payoffs for the Prisoner's Dilemma.
```

The feasible average payoffs correspond to the feasible payoffs in the stage game.
The individually rational payoffs show the payoffs that are **better for both players** than the stage Nash equilibrium.

The following theorem states that we can choose a particular discount rate that for which
there exists a subgame perfect Nash equilibrium that would give any individually rational payoff pair!

(theorem:folk_theorem)=

### Theorem: Folk Theorem

---

Let $(u_1^*,u_2^*)$ be a pair of Nash equilibrium payoffs for a stage game. For every individually rational pair $(v_1,v_2)$ there exists $\bar \delta$ such that for all $1>\delta>\bar \delta>0$ there is a subgame perfect Nash equilibrium with payoffs $(v_1,v_2)$.

---

#### Proof

---

Let $(\sigma_1^*,\sigma_2^*)$ be the stage Nash profile that yields $(u_1^*,u_2^*)$.
Now assume that playing $\bar\sigma_1\in\Delta \mathcal{A}_1$ and $\bar\sigma_2\in\Delta \mathcal{A}_2$ in
every stage gives $(v_1,v_2)$ (an individual rational payoff pair).

Consider the following strategy:

> "Begin by using $\bar \sigma_i$ and continue to use $\bar \sigma_i$ as long as both players use the
> agreed strategies. If any player deviates: use $\sigma_i^*$ for all future stages."

We begin by proving that the above is a Nash equilibrium.

Without loss of generality if player 1 deviates to $\sigma_1'\in\Delta S_1$ such that
$u_1(\sigma_1',\bar \sigma_2)>v_1$ in stage $k$ then:

$$U_1^{(k)}=\sum_{t=1}^{k-1}\delta^{t-1}v_1+\delta^{k-1}u_1(\sigma_1',\bar \sigma_2)+u_1^*\left(\frac{1}{1-\delta}-\sum_{t=1}^{k}\delta^{t-1}\right)$$

Recalling that player 1 would receive $v_1$ in every stage with no
deviation, the biggest gain to be made from deviating is if player 1 deviates
in the first stage (all future gains are more heavily discounted). Thus if we
can find $\bar\delta$ such that $\delta>\bar\delta$ implies that
$U_1^{(1)}\leq \frac{v_1}{1-\delta}$ then player 1 has no incentive to deviate.

$$
\begin{aligned}
U_1^{(1)}=u_1(\sigma_1',\bar\sigma_2)+u_1^*\frac{\delta}{1-\delta}&\leq\frac{v_1}{1-\delta}\\
(1-\delta)u_1(\sigma_1',\bar\sigma_2)+u_1^*\delta&\leq v_1\\
u_1(\sigma_1',\bar\sigma_2)-v_1&\leq \delta(u_1(\sigma_1',\bar\sigma_2)-u_1^*)\\
\end{aligned}
$$

as $u_1(\sigma_1',\bar \sigma_2)>v_1>u_1^*$, taking
$\bar\delta=\frac{u_1(\sigma_1',\bar\sigma_2)-v_1}{u_1(\sigma_1',\bar\sigma_2)-u_1^*}$ gives the
required required result for player 1 and repeating the argument for player 2 completes the
proof of the fact that the prescribed strategy is a Nash equilibrium.

By construction this strategy is also a subgame perfect Nash equilibrium. Given
any history **both** players will act in the same way and no player will have an incentive to deviate:

- If we consider a subgame just after any player has deviated from
  $\bar\sigma_i$ then both players use $\sigma_i^*$.
- If we consider a subgame just after no player has deviated from
  $\bar\sigma_i$ then both players continue to use $\bar\sigma_i$.

## Exercises

```{exercise} 
:label: constructing_non-stage-equilibrium_repeated_outcomes


Recalling that a subgame perfect equilibrium for a finitely repeated game must
involve a stage Nash equilibrium in the final stage, attempt to identify a
subgame perfect equilibrium for the repeated game that is not a simple
repetition of stage Nash profiles for each of the following games.

**Game 1**

Let

$$
M_r =
\begin{pmatrix}
4 & 7\\
1 & 4
\end{pmatrix},\qquad
M_c =
\begin{pmatrix}
3 & 6\\
1 & 3
\end{pmatrix}
$$

**Game 2**

Let

$$
M_r =
\begin{pmatrix}
5 & 0\\
0 & 1\\
3 & 0
\end{pmatrix},\qquad
M_c =
\begin{pmatrix}
4 & 3\\
3 & 4\\
6 & 3
\end{pmatrix}
$$

**Game 3**

Let

$$
M_r =
\begin{pmatrix}
1 & 0 & -1\\
-1 & -1 & 0
\end{pmatrix},\qquad
M_c =
\begin{pmatrix}
2 & 3 & 1\\
0 & -1 & 1
\end{pmatrix}
$$
```


```{exercise} 
:label: size_of_action_space

For a general stage game with $(M_r, M_c) \in \mathbb{R}^{(m\times n)^2}$
identify the size of the action space for the repeated game for each player when:

- $m=2, n=2$ and $T=2$.
- General $m, n$ and $T=3$.
- General $m, n, T$.
```



```{exercise} 
:label: payoffs_and_equilibrium_in_the_infinite_game


Consider the following stage game:

$$
M_r =
\begin{pmatrix}
-1 & 3\\
-2 & 2
\end{pmatrix}
\qquad
M_c =
\begin{pmatrix}
1 & -7\\
6 & 2
\end{pmatrix}
$$

1. For $\delta = \frac{1}{3}$, compute the average payoffs for the strategies
   $S_D$: "always play the first row" and $S_C$: "always play the second row".

2. Plot the feasible average payoff space and the individually rational payoff space.

3. Using the Folk Theorem, determine whether there exists a value of $\delta$
   that supports a subgame perfect equilibrium with average payoffs:

   - $(3/2, 3/2)$
   - $(0, 3)$
   - $(2, 6)$
   - $(2, 0)$
```


## Programming

### Using Nashpy to generate repeated games

The Nashpy library has support for generating repeated games. Let us generate
the repeated game obtained from the Prisoners Dilemma with $T=2$:

```{code-cell} python3
import nashpy.repeated_games

import nashpy as nash
import numpy as np

M_r = np.array([[3, 0], [5, 1]])
M_c = M_r.T
prisoners_dilemma = nash.Game(M_r, M_c)
repeated_pd = nash.repeated_games.obtain_repeated_game(game=prisoners_dilemma, repetitions=2)
repeated_pd
```

```{warning}
The action space for repeated games can become incredibly large even for low
values of repetitions. This might result in games that cannot be generated
computationaly.
```

We can directly obtain the action space of the row player for a given repeated
game as a python generator:

```{code-cell} python3
strategies = nash.repeated_games.obtain_strategy_space(A=M_r, repetitions=2)
len(list(strategies))
```

To obtain the action space for the columbn player use `A=M_c.T`:

```{code-cell} python3
strategies = nash.repeated_games.obtain_strategy_space(A=M_c.T, repetitions=2)
len(list(strategies))
```

(sec:notable_research)=

## Notable research

The Folk Theorem presented in this chapter has a rich theoretical lineage.
The foundational result is due to [@friedman1971non] (with a correction in
[@friedman1973non]), with the general formulation appearing in
[@fudenberg1986folk]. These results established the theoretical basis for
understanding how cooperation can be sustained in long-run interactions.

[@young1993evolution] showed how social conventions and norms can emerge from
adaptive play in repeated settings, providing an evolutionary foundation for
Folk Theorem-type outcomes.

## Conclusion

Repeated games introduce a rich strategic landscape where history matters and
reputation can sustain cooperation. Unlike one-shot interactions, repeated
games allow for long-term incentives to shape behaviour, often leading to
outcomes that dominate those of stage game equilibria.

This chapter covered the formal definitions of repeated and infinitely repeated
games, strategy spaces based on full histories, subgame perfection through
sequences of Nash profiles, and the pivotal role of discounting. Through
examples and the Folk Theorem, we saw how cooperation can emerge — even in
environments like the Prisoner’s Dilemma — when players value the future
sufficiently.

[](#tbl:repeated_games_summary) summarises the key concepts.

```{table} Summary of key concepts in repeated games
:label: tbl:repeated_games_summary
:align: center
:class: table-bordered

| Concept | Description |
|---|---|
| Repeated game | A game consisting of multiple repetitions of a fixed stage game |
| Strategy in repeated game | A mapping from history of play to actions |
| Subgame perfect equilibrium | An equilibrium where players play a Nash profile in every subgame |
| Reputation | Players may cooperate to sustain credibility and trust over time |
| Discount factor ($\delta$) | Models time preference or probability of continuation |
| Average utility | $(1-\delta)$ times the discounted sum of stage payoffs |
| Individually rational payoffs | Average payoffs that exceed stage game Nash equilibrium payoffs |
| Folk Theorem | Any individually rational payoff can be sustained given $\delta$ is high enough |

```

---

```{attention}
Repeated games illustrate how cooperation can be rational — even when short-term
incentives push toward defection. Through strategies that condition on history
and the presence of credible threats, players can build trust and sustain
mutually beneficial outcomes. The Folk Theorem formalises this by showing that
*any* payoff better than the stage game Nash equilibrium can be supported,
provided the players are sufficiently patient.
```

---

(solutions:repeated_games)=

## Solutions

````{solution} constructing_non-stage-equilibrium_repeated_outcomes
:label: solution:constructing_non-stage-equilibrium_repeated_outcomes

Recall that in a finitely repeated game the final stage must be played as a
stage Nash equilibrium. To sustain a non-Nash outcome in the first stage we
need **multiple** stage Nash equilibria: one can be used as a reward and another
as a punishment.

**Game 1**

$$
M_r =
\begin{pmatrix}
4 & 7\\
1 & 4
\end{pmatrix},\qquad
M_c =
\begin{pmatrix}
3 & 6\\
1 & 3
\end{pmatrix}
$$

First find the stage Nash equilibria. Checking best responses:

- $(r_1, c_1)$: Row gets 4 vs 1 (prefers $r_1$); Column gets 3 vs 6 (prefers $c_2$). Not NE.
- $(r_1, c_2)$: Row gets 7 vs 4 (prefers $r_1$); Column gets 6 vs 3 (prefers $c_2$). NE.
- $(r_2, c_1)$: Row gets 1 vs 4 (prefers $r_1$). Not NE.
- $(r_2, c_2)$: Row gets 4 vs 7 (prefers $r_1$). Not NE.

There is only **one** pure strategy Nash equilibrium: $(r_1, c_2)$. With a
unique stage Nash equilibrium, there is no second equilibrium to use as a
punishment. Thus it is **not possible** to sustain a non-stage-Nash outcome as
a subgame perfect equilibrium for any finite repetition.

```{code-cell} python3
import nashpy as nash
import numpy as np

M_r1 = np.array([[4, 7], [1, 4]])
M_c1 = np.array([[3, 6], [1, 3]])
game1 = nash.Game(M_r1, M_c1)
print("Game 1 Nash equilibria:")
for eq in game1.support_enumeration():
    print(eq)
```

**Game 2**

$$
M_r =
\begin{pmatrix}
5 & 0\\
0 & 1\\
3 & 0
\end{pmatrix},\qquad
M_c =
\begin{pmatrix}
4 & 3\\
3 & 4\\
6 & 3
\end{pmatrix}
$$

Find stage Nash equilibria by checking best responses in action space:

- $(r_1, c_1)$: Row: $5\geq 0\geq 3$? Row prefers $r_1$. Column: $4$ vs $3$ — prefers $c_1$. Is $(r_1, c_1)$ a NE? Row BR to $c_1$: $r_1$ (5>0>3). Column BR to $r_1$: $c_1$ (4>3). **NE**.
- $(r_2, c_2)$: Row BR to $c_2$: $r_2$ (1>0>0). Column BR to $r_2$: $c_2$ (4>3). **NE**.
- $(r_3, c_1)$: Row BR to $c_1$: $r_1$ (5>0>3). Not NE.

So there are (at least) two pure Nash equilibria: $(r_1, c_1)$ with payoffs $(5, 4)$
and $(r_2, c_2)$ with payoffs $(1, 4)$.

With two Nash equilibria we can construct a subgame perfect equilibrium using
the better equilibrium $(r_1, c_1)$ as a reward and $(r_2, c_2)$ as a punishment.

Consider the outcome $(r_3, c_1)$ in stage 1, yielding $(3, 6)$, followed by
$(r_1, c_1)$ in stage 2 if no deviation occurred, and $(r_2, c_2)$ otherwise.

**Is $(r_3, c_1)$ achievable in stage 1 under this strategy?**

- Row's payoff under cooperation: $3 + 5 = 8$.
- Row's best deviation in stage 1 (given column plays $c_1$): play $r_1$ for
  payoff $5 + 1 = 6$ (punishment in stage 2 is $(r_2, c_2)$ giving row $1$).
  Since $8 > 6$, row has no incentive to deviate.

- Column's payoff under cooperation: $6 + 4 = 10$.
- Column's best deviation in stage 1 (given row plays $r_3$): play $c_2$ for
  payoff $3 + 4 = 7$ (punishment in stage 2). Since $10 > 7$, column has no
  incentive to deviate.

Thus the strategy profile:

> Stage 1: $(r_3, c_1)$. Stage 2: play $(r_1, c_1)$ if stage 1 was $(r_3, c_1)$,
> otherwise play $(r_2, c_2)$.

is a subgame perfect equilibrium yielding utility vector $(3+5, 6+4) = (8, 10)$,
which is **not** a repetition of stage Nash profiles.

```{code-cell} python3
M_r2 = np.array([[5, 0], [0, 1], [3, 0]])
M_c2 = np.array([[4, 3], [3, 4], [6, 3]])
game2 = nash.Game(M_r2, M_c2)
print("Game 2 Nash equilibria:")
for eq in game2.support_enumeration():
    print(eq)
```

**Game 3**

$$
M_r =
\begin{pmatrix}
1 & 0 & -1\\
-1 & -1 & 0
\end{pmatrix},\qquad
M_c =
\begin{pmatrix}
2 & 3 & 1\\
0 & -1 & 1
\end{pmatrix}
$$

Find stage Nash equilibria:

- $(r_1, c_1)$: Row BR to $c_1$: $r_1$ (1>-1). Column BR to $r_1$: $c_2$ (3>2>1). Not NE.
- $(r_1, c_2)$: Row BR to $c_2$: $r_1$ (0>-1). Column BR to $r_1$: $c_2$ (3>2>1). NE? Column: 3 vs 2 vs 1 — prefers $c_2$. **NE**.
- $(r_2, c_3)$: Row BR to $c_3$: $r_2$ (0>-1). Column BR to $r_2$: $c_1$ or $c_3$ (both give 1, vs -1 for $c_2$). So $(r_2, c_1)$ and $(r_2, c_3)$ are potential NE. For $(r_2,c_3)$: Column: 1 vs -1 vs 1 — ties between $c_1$ and $c_3$. Row: $c_3$ gives 0, $c_1$ gives -1 — prefers $r_2$ to $c_3$. **NE** (and so is $(r_2, c_1)$).

We check with code:

```{code-cell} python3
M_r3 = np.array([[1, 0, -1], [-1, -1, 0]])
M_c3 = np.array([[2, 3, 1], [0, -1, 1]])
game3 = nash.Game(M_r3, M_c3)
print("Game 3 Nash equilibria:")
for eq in game3.support_enumeration():
    print(eq)
```

With multiple stage Nash equilibria, one can construct a subgame perfect
equilibrium sustaining a non-stage-Nash outcome in stage 1, using the
best-for-both equilibrium as a reward and the worst as a punishment, provided
the incentive constraint is satisfied.
````


````{solution} size_of_action_space
:label: solution:size_of_action_space

A strategy in a repeated game maps every possible history of play to an action.
We count the number of distinct strategies for the row player.

**Setup.** In each stage the row player has $m$ actions and the column player
has $n$ actions, so there are $mn$ possible outcomes per stage.

At stage $t$ the history consists of the $t-1$ outcomes already played, so
there are $(mn)^{t-1}$ possible histories entering stage $t$.

A strategy specifies one of $m$ actions for each such history, so the number of
pure strategies for a single stage $t$ (conditional on history) is
$m^{(mn)^{t-1}}$.

Since each stage is independent and the strategy must specify actions for all
$T$ stages and all possible histories, the total number of pure strategies for
the row player is:

$$
\begin{align*}
\prod_{t=1}^{T} m^{(mn)^{t-1}} \\
&= m^{\sum_{t=1}^{T}(mn)^{t-1}} \\
&= m^{\frac{(mn)^T - 1}{mn - 1}}
\end{align*}
$$

**Case 1: $m = 2,\; n = 2,\; T = 2$.**

$$
\text{Number of strategies} = 2^{\frac{(4)^2 - 1}{4 - 1}} = 2^{\frac{15}{3}} = 2^5 = 32
$$

We verify: at $T=1$ there are $1$ history (empty) so $2^1=2$ action choices.
At $T=2$ there are $(2\cdot2)^1=4$ possible stage-1 histories, giving $2^4=16$
action choices. Total: $2 \times 16 = 32$.

**Case 2: General $m, n,\; T = 3$.**

$$
\text{Number of strategies} = m^{1 + mn + (mn)^2} = m^{\frac{(mn)^3-1}{mn-1}}
$$

At $t=1$: 1 history, $m$ choices. At $t=2$: $mn$ histories, $m^{mn}$ choices.
At $t=3$: $(mn)^2$ histories, $m^{(mn)^2}$ choices. Product:

$$
m \cdot m^{mn} \cdot m^{(mn)^2} = m^{1 + mn + (mn)^2}
$$

**Case 3: General $m, n, T$.**

$$
\text{Number of strategies for row player} = m^{\sum_{t=0}^{T-1}(mn)^t} = m^{\frac{(mn)^T-1}{mn-1}}
$$

By symmetry, the column player's action space has size $n^{\frac{(mn)^T-1}{mn-1}}$.

```{code-cell} python3
import sympy as sym

m, n, T_sym = sym.symbols("m n T", positive=True, integer=True)

# General formula
exponent = sym.Sum((m * n)**sym.Symbol("t"), (sym.Symbol("t"), 0, T_sym - 1)).doit()
row_strategies = m**exponent
print("Row player strategies (general):", row_strategies)

# Specific case m=2, n=2, T=2
result_22 = int(2 ** ((4**2 - 1) // (4 - 1)))
print(f"\nm=2, n=2, T=2: row player has {result_22} pure strategies")

# m=2, n=2, T=3
exponent_T3 = 1 + 4 + 16
result_223 = 2**exponent_T3
print(f"m=2, n=2, T=3: row player has {result_223} pure strategies")
```
````


````{solution} payoffs_and_equilibrium_in_the_infinite_game
:label: solution:payoffs_and_equilibrium_in_the_infinite_game

Consider the stage game:

$$
M_r =
\begin{pmatrix}
-1 & 3\\
-2 & 2
\end{pmatrix}
\qquad
M_c =
\begin{pmatrix}
1 & -7\\
6 & 2
\end{pmatrix}
$$

**1. Average payoffs for $S_D$ (always row 1) and $S_C$ (always row 2), $\delta = 1/3$.**

If both players use $S_D$ (always $r_1$/$c_1$), the stage payoff is $(-1, 1)$ every round:

$$
\bar U_r(S_D, S_D) = (1 - \delta)(-1)\sum_{i=0}^{\infty}\delta^i = (1-\delta)\frac{-1}{1-\delta} = -1
$$

$$
\bar U_c(S_D, S_D) = 1
$$

If both use $S_C$ (always $r_2$/$c_2$), stage payoff is $(2, 2)$:

$$
\bar U_r(S_C, S_C) = (1-\delta)\frac{2}{1-\delta} = 2, \qquad \bar U_c(S_C, S_C) = 2
$$

If row plays $S_D$ and column plays $S_C$ (column always plays $c_1$, row always plays $r_1$):
Stage payoff is $(-1, 1)$:

$$
\bar U_r(S_D, S_C) = -1, \qquad \bar U_c(S_D, S_C) = 1
$$

If row plays $S_C$ and column plays $S_D$:
Row always plays $r_2$, column always plays $c_1$: stage payoff is $(-2, 6)$:

$$
\bar U_r(S_C, S_D) = -2, \qquad \bar U_c(S_C, S_D) = 6
$$

The Nash equilibria of the stage game must be identified to proceed. We check:

- $(r_1, c_1)$: Row BR to $c_1$: $-1 > -2$ so $r_1$. Column BR to $r_1$: $1 > -7$ so $c_1$. **NE** with payoff $(-1, 1)$.
- $(r_2, c_2)$: Row BR to $c_2$: $2 > 3$? No, $r_1$ gives 3. Not NE.

So the unique pure Nash equilibrium of the stage game is $(r_1, c_1)$ with payoffs
$(-1, 1)$.

```{code-cell} python3
import nashpy as nash
import numpy as np

M_r = np.array([[-1, 3], [-2, 2]])
M_c = np.array([[1, -7], [6, 2]])
game = nash.Game(M_r, M_c)
print("Stage Nash equilibria:")
for eq in game.support_enumeration():
    print(eq)
print()

delta = 1 / 3
print(f"delta = {delta}")
print(f"Average payoff (S_D, S_D): row={-1}, col={1}")
print(f"Average payoff (S_C, S_C): row={2}, col={2}")
print(f"Average payoff (S_D, S_C): row={-1}, col={1}")
print(f"Average payoff (S_C, S_D): row={-2}, col={6}")
```

**2. Feasible and individually rational payoff space.**

The feasible average payoffs are convex combinations of the four corner payoffs
$(−1, 1)$, $(3, -7)$, $(-2, 6)$, $(2, 2)$ (the stage outcomes $(r_1c_1)$,
$(r_1c_2)$, $(r_2c_1)$, $(r_2c_2)$).

The individually rational payoffs are those feasible payoffs $(v_1, v_2)$ with:

$$
v_1 > u_1^* = -1 \qquad \text{and} \qquad v_2 > u_2^* = 1
$$

i.e., payoffs that strictly exceed the stage Nash equilibrium payoffs for both players.

```{code-cell} python3
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import ConvexHull

# Stage game outcomes: (row payoff, col payoff) for each action pair
outcomes = np.array([[-1, 1], [3, -7], [-2, 6], [2, 2]])

hull = ConvexHull(outcomes)
hull_pts = np.append(hull.vertices, hull.vertices[0])

fig, ax = plt.subplots()
ax.fill(outcomes[hull.vertices, 0], outcomes[hull.vertices, 1],
        alpha=0.3, label="Feasible payoffs")

# Individually rational region: v1 > -1, v2 > 1
# Intersection with feasible region
ax.axvline(-1, color="red", linestyle="--", label="$u_1^* = -1$")
ax.axhline(1, color="blue", linestyle="--", label="$u_2^* = 1$")

ax.scatter(outcomes[:, 0], outcomes[:, 1], color="black", zorder=5)
for i, (x, y) in enumerate(outcomes):
    ax.annotate(f"({x},{y})", (x, y), textcoords="offset points", xytext=(5, 5))

ax.set_xlabel("$v_1$ (row payoff)")
ax.set_ylabel("$v_2$ (column payoff)")
ax.set_title("Feasible and individually rational payoff space")
ax.legend()
plt.tight_layout()
plt.show()
```

**3. Folk Theorem analysis.**

By the [Folk Theorem](#theorem:folk_theorem), a payoff pair $(v_1, v_2)$ can be
sustained as a subgame perfect equilibrium for sufficiently large $\delta$ if
and only if $(v_1, v_2)$ is:

(a) **Feasible**: a convex combination of the stage game payoff vectors.
(b) **Individually rational**: $v_1 > u_1^* = -1$ and $v_2 > u_2^* = 1$.

We check each candidate:

- $(3/2,\; 3/2)$: Is $3/2 > -1$? Yes. Is $3/2 > 1$? Yes. Is $(3/2, 3/2)$ feasible?
  It lies between $(−1,1)$, $(2,2)$, and $(−2,6)$; it is a convex combination
  of the corners. **Yes — supportable by the Folk Theorem.**

- $(0,\; 3)$: Is $0 > -1$? Yes. Is $3 > 1$? Yes. Feasibility: $(0,3)$ lies in the
  convex hull of the four stage payoffs. **Yes — supportable.**

- $(2,\; 6)$: Is $2 > -1$? Yes. Is $6 > 1$? Yes. Feasibility: $(2,6)$ is not
  one of the corner payoffs. It would require column getting 6 (from $r_2,c_1$
  giving $(-2,6)$) and row getting 2 simultaneously, which is not a single
  stage outcome. Check if $(2,6)$ is in the convex hull:
  The maximum row payoff when column gets 6 is $-2$ (from $(r_2,c_1)$). To get
  row payoff 2 we need stages $(r_2,c_2)$ giving $(2,2)$, but then column gets 2
  not 6. $(2,6)$ is **not in the convex hull** of feasible payoffs — it requires
  both players to receive their maximum simultaneously, which is impossible.
  **Not supportable.**

- $(2,\; 0)$: Is $0 > 1$? **No.** This fails individual rationality for the
  column player. **Not supportable.**

```{code-cell} python3
from scipy.spatial import ConvexHull
import numpy as np

outcomes = np.array([[-1, 1], [3, -7], [-2, 6], [2, 2]])
hull = ConvexHull(outcomes)

def in_convex_hull(point, hull):
    """Test if a point lies within a convex hull."""
    from scipy.spatial import Delaunay
    deln = Delaunay(outcomes[hull.vertices])
    return deln.find_simplex(point) >= 0

candidates = [(1.5, 1.5), (0, 3), (2, 6), (2, 0)]
nash_payoffs = (-1, 1)

for v1, v2 in candidates:
    feasible = in_convex_hull(np.array([v1, v2]), hull)
    ind_rational = (v1 > nash_payoffs[0]) and (v2 > nash_payoffs[1])
    supportable = feasible and ind_rational
    print(f"({v1}, {v2}): feasible={feasible}, ind_rational={ind_rational}, "
          f"folk_theorem_supportable={supportable}")
```
````
