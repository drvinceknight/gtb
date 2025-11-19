---
kernelspec:
  name: python3
  display_name: "Python 3"
---

(chp:repeated_games)=

# Repeated Games

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
- The concept of direct reciprocity.

## Theory

### Definition: repeated game

Given a two player game $(A,B)\in\mathbb{R}^{{m\times n}^2}$, referred to as a
stage game, a $T$-stage repeated game is a game in which players play that
stage game for $T>0$ repetitions. Players make decisions based on the full
history of play over all the repetitions.

### Example: Counting leaves in repeated games

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

3.

$$
M_r = \begin{pmatrix}0 & 1 \\ -1 & 3\end{pmatrix}
\qquad
M_c = - M_r
\qquad
T = 3
$$

Three stages of 2 actions each: $4 \times 4 \times 4 = 64$ leaves.

4.

$$
M_r = \begin{pmatrix}0 & 1 & 4\\1 &-1 & 3\end{pmatrix}
\qquad
M_c = - M_r
\qquad
T = 2
$$

First stage: $2 \times 3 = 6$ outcomes. Each of those leads to 6 in the
second stage. Total: $6 \times 6 = 36$ leaves.

(sec:definition-of-strategies-in-repeated-games)=

### Definition: Strategies in a repeated game

A strategy for a player in a repeated game is a mapping from all possible
histories of play to a probability distribution over the action set of the
stage game.

### Example: Validity of repeated game strategies

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

### Proof

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

### Example

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

### Example: Reputation in a repeated game

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

### Example:

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

### Example:

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

### Proof

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

(def:prisoners-dilemma)=

### Definition: Prisoner's Dilemma

The general form is:

$$
A =
\begin{pmatrix}
    R & S\\
    T & P
\end{pmatrix}\qquad
B =
\begin{pmatrix}
    R & T\\
    S & P
\end{pmatrix}
$$

with the following constraints:

$$
T > R > P > S \qquad 2R > T + S
$$

- The first constraint ensures that the second action "Defect" dominates the
  first action "Cooperate".
- The second constraint ensures that a social dilemma arises: the sum of the
  utilities to both players is best when they both cooperate.

This game is a good model of agent (human, etc) interaction: a player can choose
to take a slight loss of utility for the benefit of the other player **and**
themselves.

### Example: Simplifed form of the Prisoner's Dilemma:

Under what conditions is the following game a Prisoner's Dilemma:

$$
A = \begin{pmatrix}
      1       & -\mu \\
      1 + \mu & 0
    \end{pmatrix}\qquad
B = A^T
$$

This is a Prisoner's Dilemma when:

$$
1 + \mu > 1 \text{ and } 0 > -\mu
$$

and:

$$
2\times 1 = 2 > 1 = 1 + \mu -\mu
$$

Both of these equations hold for $\mu>0$, in fact the second equation holds for
all $\mu$. This is a convenient form for
the Prisoner's Dilemma as it corresponds to a 1-dimensional parametrization.

As a single one-shot game there is not much more to say about the Prisoner's
Dilemma. It becomes fascinating when studied as a repeated game.

(sec:axelrods_tournaments)=

### Axelrod's tournaments

---

In 1980, political scientist Robert Axelrod organized a computer tournament for
an iterated Prisoner's Dilemma, as described in [@axelrod1980effective].

- Fourteen strategies were submitted.
- The tournament was a round-robin of 200 iterations, including a fifteenth
  player who played uniformly at random.
- Some submissions were highly sophisticated—for example, one strategy used a
  $\chi^2$ test to detect opponents behaving randomly. Further details can be
  found [here](http://axelrod.readthedocs.io/en/stable/reference/overview_of_strategies.html#axelrod-s-first-tournament).
- The winner (by average score) was a surprisingly simple strategy: **Tit For Tat**,
  which begins by cooperating and then mimics the opponent's previous move.

Following this, Axelrod hosted a second tournament with 62 strategy submissions
[@axelrod1980more], again including a random strategy. Participants in this
second round were aware of the original results, and many strategies were
designed specifically to counter or improve upon **Tit For Tat**. Nonetheless,
**Tit For Tat** prevailed once again.

These tournaments led to the wide acceptance of four principles for effective
cooperation:

- Do not be envious: avoid striving for a higher payoff than your opponent.
- Be _nice_: never be the first to defect.
- Reciprocate: respond to cooperation with cooperation, and to defection with defection.
- Avoid overcomplication: do not attempt to outwit or exploit the opponent with excessive cunning.

```{important}
While these four rules were long held as canonical, modern research has shown
they do not always hold. A discussion of these findings appears in
[Section 6](#sec:notable_research).
```

These early experiments with the repeated Prisoner's Dilemma were not only
influential in political science but also laid a foundation for the study of
emergent cooperation in multi-agent systems.

## Exercises

### Exercise: Constructing non-stage-equilibrium repeated outcomes

---

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

---

### Exercise: Size of action space

For a general stage game with $(M_r, M_c) \in \mathbb{R}^{(m\times n)^2}$
identify the size of the action space for the repeated game for each player when:

- $m=2, n=2$ and $T=2$.
- General $m, n$ and $T=3$.
- General $m, n, T$.

### Exercise: Identifying Prisoners Dilemmas

---

Justify whether or not the following games are instances of the Prisoners
Dilemma.

**Game 1**

$$
A =
\begin{pmatrix}
3 & 0\\
5 & 1
\end{pmatrix}
\qquad
B =
\begin{pmatrix}
3 & 5\\
0 & 1
\end{pmatrix}
$$

**Game 2**

$$
A =
\begin{pmatrix}
1 & -1\\
2 & 0
\end{pmatrix}
\qquad
B =
\begin{pmatrix}
1 & 2\\
-1 & 0
\end{pmatrix}
$$

**Game 3**

$$
A =
\begin{pmatrix}
1 & -1\\
2 & 0
\end{pmatrix}
\qquad
B =
\begin{pmatrix}
3 & 5\\
0 & 1
\end{pmatrix}
$$

**Game 4**

$$
A =
\begin{pmatrix}
6 & 0\\
12 & 1
\end{pmatrix}
\qquad
B =
\begin{pmatrix}
6 & 12\\
0 & 0
\end{pmatrix}
$$

---

### Exercise: Repeated strategies in the Prisoners Dilemma

---

Consider the standard Prisoners Dilemma:

$$
M_r =
\begin{pmatrix}
3 & 0\\
5 & 1
\end{pmatrix}
\qquad
M_c =
\begin{pmatrix}
3 & 5\\
0 & 1
\end{pmatrix}
$$

Suppose players repeatedly play this game using one of the following strategies:

1. **Tit For Tat**: starts by cooperating, then repeats the opponent’s previous action.
2. **Alternator**: starts by cooperating, then alternates between cooperation and defection.
3. **75% cooperator**: a random strategy that cooperates 75% of the time.

Obtain the normal form representation of the repeated game for each of the
following scenarios:

- The game is repeated $T = 100$ times.
- The game is repeated $T = 99$ times.
- The game is repeated infinitely with $\delta = \frac{1}{4}$.

For each case, determine the Nash equilibria in action space.

---

### Exercise: Payoffs and equilibrium in the infinite game

---

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

---

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

### Using the Axelrod library to study the repeated Prisoners Dilemma

There is a python library called `axelrod` which has functionality to run
tournaments akin to [Robert Axelrod's original tournaments](#sec:axelrods_tournaments) but also includes
more than 240 total strategies as well as further functionality.

To generate a tournament with 4 strategies with $\delta=1/4$

1. **Tit For Tat**: starts by cooperating, then repeats the opponent’s previous action.
2. **Alternator**: starts by cooperating, then alternates between cooperation and defection.
3. **75% cooperator**: a random strategy that cooperates 75% of the time.
4. **Grudger**: starts by cooperating, then defects forever if the opponent ever
   defects against it.

First let us set up some parameters such as the players as well as the seed to
ensure reproducibility of the random results.

```{code-cell} python3
import axelrod as axl

players = [axl.TitForTat(), axl.Alternator(), axl.Random(.75), axl.Grudger()]
delta = 1 / 4
seed = 0
repetitions = 500
prob_end = 1 - delta
```

Now we create and run the tournament obtaining the payoff matrix from the
results:

```{code-cell} python
tournament = axl.Tournament(players=players, prob_end=prob_end, seed=seed, repetitions=repetitions)
results = tournament.play(progress_bar=False)
M_r = np.array(results.payoff_matrix)
M_r
```

(sec:notable_research)=

## Notable research

The most influential early research on repeated games comes from the two
seminal papers by Robert Axelrod [@axelrod1980effective; @axelrod1980more],
which culminated in his widely cited book [@axelrod1984evolution]. As discussed
in [Section 6](#sec:axelrods_tournaments), Axelrod's findings included a set of
heuristics for successful behavior in the repeated Prisoner's Dilemma.

Subsequent work has challenged these principles. The development of the Axelrod
Python library [@knight2016open] enabled systematic and reproducible analysis
across a far greater population of strategies. In particular,
[@glynatsi2024properties] studied 45,600 tournaments across diverse strategic
populations and parameter regimes, finding that the original heuristics do not
generalize. The revised empirical findings suggest the following properties are
associated with successful play:

- Be a little bit envious.
- Be "nice" in non-noisy environments or when game lengths are longer.
- Reciprocate both cooperation and defection appropriately; be provocable in
  tournaments with short matches and generous in noisy environments.
- It is acceptable to be clever.
- Adapt to the environment; adjust to the mean population cooperation rate.

The observation that _being envious_ can be beneficial echoes a more recent
development that was famously described by _MIT Technology Review_ as having
set "the world of game theory on fire". In their landmark paper,
[@press2012iterated] introduced a novel class of memory-one strategies called
**zero-determinant strategies**, which can unilaterally enforce linear payoff
relationships, including extortionate dynamics.

However, the excitement around these strategies has been tempered by further
theoretical and computational research. Studies such as
[@hilbe2013evolution; @knight2018evolution] demonstrate
that extortionate strategies, while elegant, do not tend to survive under
evolutionary dynamics. These results reinforce the importance of adaptability
and contextual behavior in long-run strategic success.

The [Folk Theorem presented in this chapter](#theorem:folk_theorem) can be
traced to foundational work by [@friedman1971non] (with a correction in
[@friedman1973non]) and the general formulation in [@fudenberg1986folk]. These
theoretical insights laid the groundwork for subsequent developments such as
[@young1993evolution], which shows how social conventions and norms can emerge
from adaptive play in repeated settings.

## Conclusion

Repeated games introduce a rich strategic landscape where history matters and
reputation can sustain cooperation. Unlike one-shot interactions, repeated
games allow for long-term incentives to shape behavior, often leading to
outcomes that dominate those of stage game equilibria.

This chapter explored key ideas including the formal definitions of repeated
and infinitely repeated games, strategy spaces based on full histories,
subgame perfection through sequences of Nash profiles, and the pivotal role of
discounting. Through examples and the Folk Theorem, we saw how cooperation can
emerge—even in environments like the Prisoner's Dilemma—when players value the
future sufficiently.

In addition to theoretical foundations, we examined computational tools such as
the Nashpy and Axelrod libraries, which allow for large-scale simulations and
reproducible research into emergent cooperative behavior. We also revisited
classical findings, including Axelrod's tournaments, and contrasted them with
modern insights that challenge early heuristics. A summary of key concepts is
given in [](#tbl:repeated_games_summary).

```{table} The main linear programs for Zero Sum Game
:label: tbl:repeated_games_summary
:align: center
:class: table-bordered


| Concept                                 | Description                                                                 |
|-----------------------------------------|-----------------------------------------------------------------------------|
| Repeated game                           | A game consisting of multiple repetitions of a fixed stage game            |
| Strategy in repeated game               | A mapping from history of play to actions                                  |
| Subgame perfect equilibrium             | An equilibrium where players play a Nash profile in every subgame          |
| Reputation                              | Players may cooperate to sustain credibility and trust over time           |
| Discount factor ($\delta$)             | Models time preference or probability of continuation                      |
| Average utility                         | Weighted utility that accounts for $\delta$ as average continuation length |
| Folk Theorem                            | Any individually rational payoff can be sustained given $\delta$ is high enough |
| Prisoner’s Dilemma                      | A canonical stage game often used to model cooperation and defection       |
| Zero-determinant strategies             | Memory-one strategies capable of extorting opponents (not evolutionarily stable) |
| Axelrod’s tournaments                   | Early empirical work showing Tit for Tat’s success in repeated dilemmas    |

```

---

```{attention}
Repeated games illustrate how cooperation can be rational—even when short-term
incentives push toward defection. Through strategies that condition on history
and the presence of credible threats, players can build trust and sustain
mutually beneficial outcomes.

The Folk Theorem formalizes this by showing that *any* payoff better than the
stage game Nash equilibrium can be supported, provided the players are
sufficiently patient.
```
