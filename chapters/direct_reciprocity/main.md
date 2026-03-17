---
kernelspec:
  name: python3
  display_name: "Python 3"
---

(chp:direct_reciprocity)=

# Direct Reciprocity

(sec:motivating_example_direct_reciprocity)=

## Motivating Example: Research Collaboration

Alice and Bob are researchers who meet regularly to share results before
submitting papers. At each meeting, each can choose to:

- **Cooperate (C)**: share their latest findings openly.
- **Defect (D)**: withhold key results to protect their competitive advantage.

The payoff structure is that of a **Prisoner's Dilemma**: mutual sharing is
best collectively, but each individual has a short-term incentive to withhold.
The [Folk Theorem](#theorem:folk_theorem) tells us that cooperation *can* be
sustained in an infinitely repeated game — but it does not say *how*.

In practice, Alice and Bob remember only the last meeting. Alice might decide:
"I'll share if you shared last time, but withhold if you withheld." This
**memory-one** approach, conditioning solely on the previous round's outcome,
is both cognitively realistic and mathematically tractable.

This chapter asks: which memory-one strategies actually sustain cooperation?
And what are their long-run payoffs?

## Theory

(def:prisoners-dilemma)=

### Definition: Prisoner's Dilemma

---

The **Prisoner's Dilemma** is the two-player symmetric game:

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

with the constraints:

$$
T > R > P > S \qquad 2R > T + S
$$

- The first constraint ensures **Defect** strictly dominates **Cooperate**.
- The second ensures mutual cooperation is socially optimal.

---

#### Example: Simplified Prisoner's Dilemma

Under what conditions is the following game a Prisoner's Dilemma?

$$
A = \begin{pmatrix}
      1       & -\mu \\
      1 + \mu & 0
    \end{pmatrix}\qquad
B = A^T
$$

This requires $1 + \mu > 1$ and $0 > -\mu$, both of which hold for $\mu > 0$.
The constraint $2R > T + S$ gives $2 > 1$, which always holds.
This parametrisation is convenient: $\mu > 0$ is the only condition needed.

(sec:axelrods_tournaments)=

### Axelrod's Tournaments

---

In 1980, Robert Axelrod organised a computer tournament for the iterated
Prisoner's Dilemma [@axelrod1980effective].

- Fourteen strategies were submitted.
- The tournament was a round-robin of 200 iterations, plus a strategy playing
  uniformly at random.
- Some entries were highly sophisticated — one used a $\chi^2$ test to detect
  random opponents.
- The winner was the simplest entry: **Tit For Tat** (TFT), which cooperates
  on the first move then copies the opponent's previous action.

A second tournament with 62 submissions followed [@axelrod1980more]. With
participants now aware of TFT's success, many strategies were designed
specifically to counter it. TFT won again.

---

These results suggested four principles for successful cooperation:

- **Don't be envious**: don't strive for a higher score than your opponent.
- **Be nice**: never defect first.
- **Reciprocate**: match cooperation with cooperation, defection with defection.
- **Don't be too clever**: avoid overly complex exploitation.

```{important}
While influential, these principles have since been challenged by modern
research — see [](#sec:notable_research_direct_reciprocity).
```

### Definition: Reactive Strategy

---

A **reactive strategy** in the Prisoner's Dilemma is a pair
$(p, q) \in [0, 1]^2$ where:

- $p$ is the probability of cooperating given the opponent **cooperated** last round.
- $q$ is the probability of cooperating given the opponent **defected** last round.

---

The first move is typically set separately (often cooperate), since there is no
prior history.

#### Example: Common Reactive Strategies

| Strategy | $(p, q)$ | Description |
|---|---|---|
| Always Cooperate (AllC) | $(1, 1)$ | Cooperates regardless |
| Always Defect (AllD) | $(0, 0)$ | Defects regardless |
| Tit For Tat (TFT) | $(1, 0)$ | Copies opponent's last move |
| Generous TFT (GTFT) | $(1, \epsilon)$ | TFT but occasionally forgives |

```{note}
Reactive strategies are a subclass of **memory-one** strategies, which
condition on the full previous outcome $(a_1, a_2) \in \{C,D\}^2$ rather than
just the opponent's last action. The zero-determinant strategies discussed in
[](#sec:notable_research_direct_reciprocity) are memory-one but not reactive.
```

### Definition: Markov Chain of Two Reactive Strategies

---

When players with reactive strategies $(p, q)$ and $(p', q')$ play an
infinitely repeated Prisoner's Dilemma, the pair of actions at each round
defines a **Markov chain** with state space
$\mathcal{S} = \{CC, CD, DC, DD\}$.

The transition matrix $P \in \mathbb{R}^{4 \times 4}$, with rows and columns
ordered as $(CC, CD, DC, DD)$, is:

$$
P =
\begin{pmatrix}
pp'      & p(1-p')      & (1-p)p'      & (1-p)(1-p')      \\
qp'      & q(1-p')      & (1-q)p'      & (1-q)(1-p')      \\
pq'      & p(1-q')      & (1-p)q'      & (1-p)(1-q')      \\
qq'      & q(1-q')      & (1-q)q'      & (1-q)(1-q')      \\
\end{pmatrix}
$$

where rows correspond to the current state and columns to the next state.

---

The entry $P_{s,s'}$ is the probability of transitioning from state $s$ to
state $s'$. For example, from state $CD$ (player 1 cooperated, player 2
defected): player 1 now cooperates with probability $q$ (their opponent
defected), while player 2 now cooperates with probability $p'$ (their opponent
cooperated).

### Theorem: Long-Run Average Payoffs via Stationary Distribution

---

If the Markov chain defined by $(p, q)$ and $(p', q')$ is **ergodic** (see
[Appendix A2](#app:ergodic_markov_chain)), it has a unique stationary
distribution $\pi = (\pi_{CC}, \pi_{CD}, \pi_{DC}, \pi_{DD})$ satisfying:

$$
\pi P = \pi \qquad \sum_{s \in \mathcal{S}} \pi_s = 1
$$

The long-run average payoffs are then:

$$
\bar{u}_1 = R\,\pi_{CC} + S\,\pi_{CD} + T\,\pi_{DC} + P\,\pi_{DD}
$$

$$
\bar{u}_2 = R\,\pi_{CC} + T\,\pi_{CD} + S\,\pi_{DC} + P\,\pi_{DD}
$$

---

```{note}
The chain is ergodic whenever $0 < p, q, p', q' < 1$ (all probabilities
strictly interior). For boundary cases such as pure TFT $(p=1, q=0)$, the
chain may not be ergodic in general; the stationary distribution must be
verified separately.
```

#### Example: Long-run payoffs for two reactive strategies

Consider the [contractor Prisoner's Dilemma](#example:repeated-contractor-game)
with $R=3, S=0, T=5, P=1$, and two reactive strategies:

- Player 1 (Generous Reciprocator): $(p, q) = (0.9,\; 0.3)$
- Player 2 (Suspicious Reciprocator): $(p', q') = (0.7,\; 0.1)$

From state $CC$: player 1 cooperates with $p=0.9$, player 2 with $p'=0.7$:

$$
CC \to CC: 0.63,\quad CC \to CD: 0.27,\quad CC \to DC: 0.07,\quad CC \to DD: 0.03
$$

From state $CD$: player 1 cooperates with $q=0.3$, player 2 with $p'=0.7$:

$$
CD \to CC: 0.21,\quad CD \to CD: 0.09,\quad CD \to DC: 0.49,\quad CD \to DD: 0.21
$$

From state $DC$: player 1 cooperates with $p=0.9$, player 2 with $q'=0.1$:

$$
DC \to CC: 0.09,\quad DC \to CD: 0.81,\quad DC \to DC: 0.01,\quad DC \to DD: 0.09
$$

From state $DD$: player 1 cooperates with $q=0.3$, player 2 with $q'=0.1$:

$$
DD \to CC: 0.03,\quad DD \to CD: 0.27,\quad DD \to DC: 0.07,\quad DD \to DD: 0.63
$$

So the full transition matrix is:

$$
P =
\begin{pmatrix}
0.63 & 0.27 & 0.07 & 0.03 \\
0.21 & 0.09 & 0.49 & 0.21 \\
0.09 & 0.81 & 0.01 & 0.09 \\
0.03 & 0.27 & 0.07 & 0.63 \\
\end{pmatrix}
$$

The stationary distribution is found by solving $\pi P = \pi$ with
$\sum \pi_i = 1$. This is computed numerically in the Programming section,
giving $\pi \approx (0.246, 0.316, 0.191, 0.246)$ and long-run average payoffs:

$$
\bar{u}_1 \approx 3(0.246) + 0(0.316) + 5(0.191) + 1(0.246) \approx 1.94
$$

$$
\bar{u}_2 \approx 3(0.246) + 5(0.316) + 0(0.191) + 1(0.246) \approx 2.57
$$

The Suspicious Reciprocator earns a higher long-run payoff, reflecting greater
exploitation of the Generous Reciprocator's willingness to forgive.

## Exercises

```{exercise}
:label: identifying_prisoners_dilemmas

Justify whether or not the following games are instances of the Prisoner's
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
```

```{exercise}
:label: reactive_strategy_markov_chain

Consider the Prisoner's Dilemma with $R=3, S=0, T=5, P=1$.

1. Write down the transition matrix $P$ for the Markov chain formed by
   Tit For Tat $(p=1, q=0)$ playing against Always Cooperate $(p'=1, q'=1)$.
2. Write down the transition matrix $P$ for the Markov chain formed by
   Tit For Tat $(p=1, q=0)$ playing against Always Defect $(p'=0, q'=0)$.
3. For each case, identify whether the chain is ergodic and, if so, find
   the stationary distribution and the long-run average payoffs.
```

```{exercise}
:label: repeated_strategies_in_the_prisoners_dilemma

Consider the standard Prisoner's Dilemma:

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

1. **Tit For Tat**: starts by cooperating, then repeats the opponent's previous action.
2. **Alternator**: starts by cooperating, then alternates between cooperation and defection.
3. **75% cooperator**: a random strategy that cooperates 75% of the time.

Obtain the normal form representation of the repeated game for each of the
following scenarios:

- The game is repeated $T = 100$ times.
- The game is repeated $T = 99$ times.
- The game is repeated infinitely with $\delta = \frac{1}{4}$.

For each case, determine the Nash equilibria in action space.
```

## Programming

### Computing the Stationary Distribution of a Reactive Strategy Pair

Given the transition matrix $P$ for two reactive strategies, the stationary
distribution satisfies $\pi P = \pi$. We can find it by solving the linear
system $(P^T - I)\pi^T = 0$ subject to $\sum \pi_i = 1$.

```{code-cell} python3
import numpy as np

def reactive_transition_matrix(p, q, p_prime, q_prime):
    """
    Build the 4x4 transition matrix for reactive strategies (p,q) and (p',q').
    States are ordered: CC, CD, DC, DD.
    """
    P = np.array([
        [p * p_prime,       p * (1 - p_prime),       (1 - p) * p_prime,       (1 - p) * (1 - p_prime)],
        [q * p_prime,       q * (1 - p_prime),       (1 - q) * p_prime,       (1 - q) * (1 - p_prime)],
        [p * q_prime,       p * (1 - q_prime),       (1 - p) * q_prime,       (1 - p) * (1 - q_prime)],
        [q * q_prime,       q * (1 - q_prime),       (1 - q) * q_prime,       (1 - q) * (1 - q_prime)],
    ])
    return P

def stationary_distribution(P):
    """
    Compute the stationary distribution of a transition matrix P.
    """
    n = P.shape[0]
    A = (P.T - np.eye(n))
    A[-1, :] = 1  # replace last equation with normalisation constraint
    b = np.zeros(n)
    b[-1] = 1
    return np.linalg.solve(A, b)

# Generous Reciprocator vs Suspicious Reciprocator
p, q = 0.9, 0.3
p_prime, q_prime = 0.7, 0.1

P = reactive_transition_matrix(p, q, p_prime, q_prime)
print("Transition matrix:")
print(np.round(P, 4))

pi = stationary_distribution(P)
print("\nStationary distribution (CC, CD, DC, DD):")
print(np.round(pi, 4))
```

```{code-cell} python3
# Compute long-run average payoffs
R, S, T, Pval = 3, 0, 5, 1

u1_bar = R * pi[0] + S * pi[1] + T * pi[2] + Pval * pi[3]
u2_bar = R * pi[0] + T * pi[1] + S * pi[2] + Pval * pi[3]

print(f"Long-run average payoff for Player 1: {u1_bar:.4f}")
print(f"Long-run average payoff for Player 2: {u2_bar:.4f}")
```

### Using the Axelrod Library

The `axelrod` Python library [@knight2016open] provides over 240 strategies
and tools to run reproducible tournaments — extending Axelrod's original
experiments to much larger and more diverse strategic populations.

```{code-cell} python3
import axelrod as axl
import numpy as np

players = [axl.TitForTat(), axl.Alternator(), axl.Random(0.75), axl.Grudger()]
delta = 1 / 4
prob_end = 1 - delta
seed = 0
repetitions = 500

tournament = axl.Tournament(
    players=players, prob_end=prob_end, seed=seed, repetitions=repetitions
)
results = tournament.play(progress_bar=False)
M_r = np.array(results.payoff_matrix)
print("Payoff matrix:")
print(np.round(M_r, 3))
```

(sec:notable_research_direct_reciprocity)=

## Notable Research

The seminal empirical work on direct reciprocity is due to Robert Axelrod
[@axelrod1980effective; @axelrod1980more], synthesised in his widely cited book
[@axelrod1984evolution]. As described in [Section 3](#sec:axelrods_tournaments),
Axelrod's tournaments established Tit For Tat as the canonical cooperative
strategy and produced four heuristics for successful play.

Subsequent work has challenged these heuristics. The development of the Axelrod
Python library [@knight2016open] enabled systematic and reproducible analysis
across a far greater population of strategies. In particular,
[@glynatsi2024properties] studied 45,600 tournaments across diverse strategic
populations and parameter regimes, finding that the original heuristics do not
generalise. The revised empirical findings suggest:

- Be a little bit envious.
- Be "nice" in non-noisy environments or when game lengths are longer.
- Reciprocate both cooperation and defection appropriately.
- It is acceptable to be clever.
- Adapt to the environment.

The observation that _being envious_ can be beneficial echoes a landmark
theoretical result. [@press2012iterated] introduced **zero-determinant
strategies** — memory-one strategies that can unilaterally enforce linear payoff
relationships, including extortionate dynamics. This paper was described by
_MIT Technology Review_ as having set "the world of game theory on fire."

However, [@hilbe2013evolution] and [@knight2018evolution] showed that
extortionate strategies do not tend to survive under evolutionary dynamics,
tempering the initial excitement and reinforcing the importance of
adaptability.

## Conclusion

Direct reciprocity offers a tractable lens through which to study how
cooperation can emerge in pairwise repeated interactions. By restricting
attention to memory-one strategies, we obtain a mathematically precise
framework: the interaction of two reactive strategies defines an ergodic Markov
chain, and the stationary distribution determines long-run payoffs.

This chapter defined the Prisoner's Dilemma, presented Axelrod's foundational
tournaments, and developed the theory of reactive strategies and their Markov
chain representation. We saw that Tit For Tat's success in early tournaments
does not fully generalise, and that modern computational work has refined our
understanding of what makes a strategy successful.

[](#tbl:direct_reciprocity_summary) summarises the key concepts.

```{table} Summary of key concepts in direct reciprocity
:label: tbl:direct_reciprocity_summary
:align: center
:class: table-bordered

| Concept | Description |
|---|---|
| Prisoner's Dilemma | A symmetric game where Defect dominates but mutual cooperation is socially optimal |
| Reactive strategy $(p, q)$ | Cooperates with probability $p$ after C, $q$ after D |
| Tit For Tat | Cooperates first, then copies opponent's last move |
| Markov chain of strategies | States are outcome pairs; transitions determined by $(p,q)$ and $(p',q')$ |
| Stationary distribution | Long-run fraction of time spent in each state |
| Long-run average payoff | Payoff weighted by stationary distribution |
| Zero-determinant strategies | Memory-one strategies enforcing linear payoff relationships |
| Axelrod's tournaments | Empirical tournaments establishing TFT's success and four cooperation heuristics |

```

---

```{attention}
Direct reciprocity shows that even the simplest memory-one strategies can
sustain cooperation — or exploit it. The Markov chain framework gives precise
predictions about long-run payoffs, connecting the intuitions from Axelrod's
tournaments to a rigorous mathematical foundation. Modern research continues
to refine our understanding of which strategies thrive across diverse and
evolving populations.
```

---

(solutions:direct_reciprocity)=

## Solutions

````{solution} identifying_prisoners_dilemmas
:label: solution:identifying_prisoners_dilemmas

Recall the [Prisoner's Dilemma](#def:prisoners-dilemma) requires:

$$
T > R > P > S \qquad \text{and} \qquad 2R > T + S
$$

where the row player's matrix is:

$$
A = \begin{pmatrix} R & S \\ T & P \end{pmatrix}
$$

So $R$ is the mutual-cooperation payoff, $T$ the temptation (defect while other
cooperates), $P$ the mutual-defection payoff, and $S$ the sucker payoff.

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

Reading off: $R = 3$, $S = 0$, $T = 5$, $P = 1$.

- $T > R > P > S$: $5 > 3 > 1 > 0$. ✓
- $2R > T + S$: $6 > 5$. ✓

**Game 1 is a Prisoner's Dilemma.**

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

Reading off: $R = 1$, $S = -1$, $T = 2$, $P = 0$.

- $T > R > P > S$: $2 > 1 > 0 > -1$. ✓
- $2R > T + S$: $2 > 2 - 1 = 1$. ✓

**Game 2 is a Prisoner's Dilemma.**

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

The matrices $A$ and $B$ are not transposes of each other ($B \neq A^T$), so
this is **not a symmetric game**. The Prisoner's Dilemma as defined in
[](#def:prisoners-dilemma) is a symmetric game with $B = A^T$.

Since $B \neq A^T$ (e.g., $B_{12} = 5 \neq -1 = A_{21}$), **Game 3 is not a
Prisoner's Dilemma**.

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

Check symmetry: $B = A^T$? $A^T = \begin{pmatrix} 6 & 12 \\ 0 & 1\end{pmatrix}$.
But $B_{22} = 0 \neq 1 = A^T_{22}$. So the game is not symmetric and therefore
**not a Prisoner's Dilemma** as defined.

Even ignoring symmetry, reading $A$: $R=6$, $S=0$, $T=12$, $P=1$. Checking
$2R > T+S$: $12 > 12$. This fails (strict inequality required). **Game 4 is not
a Prisoner's Dilemma**.

```{code-cell} python3
import numpy as np

games = {
    "Game 1": (np.array([[3, 0], [5, 1]]), np.array([[3, 5], [0, 1]])),
    "Game 2": (np.array([[1, -1], [2, 0]]), np.array([[1, 2], [-1, 0]])),
    "Game 3": (np.array([[1, -1], [2, 0]]), np.array([[3, 5], [0, 1]])),
    "Game 4": (np.array([[6, 0], [12, 1]]), np.array([[6, 12], [0, 0]])),
}

for name, (A, B) in games.items():
    R, S = A[0, 0], A[0, 1]
    T, P = A[1, 0], A[1, 1]
    symmetric = np.allclose(B, A.T)
    cond1 = T > R > P > S
    cond2 = 2 * R > T + S
    is_pd = symmetric and cond1 and cond2
    print(f"{name}: R={R}, S={S}, T={T}, P={P}")
    print(f"  symmetric={symmetric}, T>R>P>S={cond1}, 2R>T+S: {2*R}>{T+S} => {cond2}")
    print(f"  Prisoner's Dilemma: {is_pd}\n")
```
````


````{solution} reactive_strategy_markov_chain
:label: solution:reactive_strategy_markov_chain

The Prisoner's Dilemma has $R=3$, $S=0$, $T=5$, $P=1$.

Recall the transition matrix for reactive strategies $(p, q)$ versus $(p', q')$,
with states ordered $(CC, CD, DC, DD)$:

$$
P =
\begin{pmatrix}
pp'      & p(1-p')      & (1-p)p'      & (1-p)(1-p')      \\
qp'      & q(1-p')      & (1-q)p'      & (1-q)(1-p')      \\
pq'      & p(1-q')      & (1-p)q'      & (1-p)(1-q')      \\
qq'      & q(1-q')      & (1-q)q'      & (1-q)(1-q')      \\
\end{pmatrix}
$$

**1. TFT $(p=1, q=0)$ vs AllC $(p'=1, q'=1)$.**

Substituting $p=1, q=0, p'=1, q'=1$:

$$
\begin{align*}
P &=
\begin{pmatrix}
1\cdot1 & 1\cdot0 & 0\cdot1 & 0\cdot0 \\
0\cdot1 & 0\cdot0 & 1\cdot1 & 1\cdot0 \\
1\cdot1 & 1\cdot0 & 0\cdot1 & 0\cdot0 \\
0\cdot1 & 0\cdot0 & 1\cdot1 & 1\cdot0
\end{pmatrix}\\
&=
\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 \\
1 & 0 & 0 & 0 \\
0 & 0 & 1 & 0
\end{pmatrix}
\end{align*}
$$

This chain has two absorbing components. Starting from $CC$: always stays in
$CC$. Starting from $CD$: moves to $DC$, then back to $CC$, then stays. Starting
from $DC$: moves to $CC$. Starting from $DD$: moves to $DC \to CC$.

Since all states eventually reach $CC$ (an absorbing state), the chain is **not
ergodic** (it has an absorbing state rather than a unique stationary
distribution with full support). However, it has a unique stationary distribution:

$$
\pi = (1, 0, 0, 0)
$$

since all paths lead to $CC$ and stay there.

Long-run average payoffs:

$$
\bar{u}_1 = R \cdot 1 + S \cdot 0 + T \cdot 0 + P \cdot 0 = R = 3
$$

$$
\bar{u}_2 = R \cdot 1 + T \cdot 0 + S \cdot 0 + P \cdot 0 = R = 3
$$

Both players cooperate in every round, earning $3$ each.

**2. TFT $(p=1, q=0)$ vs AllD $(p'=0, q'=0)$.**

Substituting $p=1, q=0, p'=0, q'=0$:

$$
\begin{align*}
P &=
\begin{pmatrix}
1\cdot0 & 1\cdot1 & 0\cdot0 & 0\cdot1 \\
0\cdot0 & 0\cdot1 & 1\cdot0 & 1\cdot1 \\
1\cdot0 & 1\cdot1 & 0\cdot0 & 0\cdot1 \\
0\cdot0 & 0\cdot1 & 1\cdot0 & 1\cdot1
\end{pmatrix}\\
&=
\begin{pmatrix}
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
\end{align*}
$$

From any state: $CC \to CD \to DD \to DD \to \cdots$ (DD is absorbing). Starting
from $DC$: $DC \to CD \to DD$.

All paths reach $DD$, so the unique stationary distribution is:

$$
\pi = (0, 0, 0, 1)
$$

The chain is **not ergodic** (absorbing state at $DD$), but it has a unique
stationary distribution with $\pi_{DD} = 1$.

Long-run average payoffs:

$$
\bar{u}_1 = R \cdot 0 + S \cdot 0 + T \cdot 0 + P \cdot 1 = P = 1
$$

$$
\bar{u}_2 = R \cdot 0 + T \cdot 0 + S \cdot 0 + P \cdot 1 = P = 1
$$

Both players end up in perpetual mutual defection, each earning $1$.

**3. Summary.**

Neither chain is ergodic in the strict sense (both have absorbing states).
However, both have a unique limiting distribution:

| Matchup | Stationary $\pi$ | $\bar{u}_1$ | $\bar{u}_2$ | Ergodic? |
|---|---|---|---|---|
| TFT vs AllC | $(1,0,0,0)$ | 3 | 3 | No (absorbing state $CC$) |
| TFT vs AllD | $(0,0,0,1)$ | 1 | 1 | No (absorbing state $DD$) |

```{code-cell} python3
import numpy as np

def reactive_transition_matrix(p, q, p_prime, q_prime):
    P = np.array([
        [p * p_prime, p * (1 - p_prime), (1 - p) * p_prime, (1 - p) * (1 - p_prime)],
        [q * p_prime, q * (1 - p_prime), (1 - q) * p_prime, (1 - q) * (1 - p_prime)],
        [p * q_prime, p * (1 - q_prime), (1 - p) * q_prime, (1 - p) * (1 - q_prime)],
        [q * q_prime, q * (1 - q_prime), (1 - q) * q_prime, (1 - q) * (1 - q_prime)],
    ])
    return P

R, S, T, Pval = 3, 0, 5, 1

# TFT vs AllC
P1 = reactive_transition_matrix(1, 0, 1, 1)
print("TFT vs AllC transition matrix:")
print(P1)

# Stationary distribution by matrix power
pi1 = np.linalg.matrix_power(P1, 100)[0]
print(f"Stationary distribution: {pi1}")
u1_1 = R * pi1[0] + S * pi1[1] + T * pi1[2] + Pval * pi1[3]
u2_1 = R * pi1[0] + T * pi1[1] + S * pi1[2] + Pval * pi1[3]
print(f"Long-run payoffs: u1={u1_1:.4f}, u2={u2_1:.4f}\n")

# TFT vs AllD
P2 = reactive_transition_matrix(1, 0, 0, 0)
print("TFT vs AllD transition matrix:")
print(P2)

pi2 = np.linalg.matrix_power(P2, 100)[0]
print(f"Stationary distribution: {pi2}")
u1_2 = R * pi2[0] + S * pi2[1] + T * pi2[2] + Pval * pi2[3]
u2_2 = R * pi2[0] + T * pi2[1] + S * pi2[2] + Pval * pi2[3]
print(f"Long-run payoffs: u1={u1_2:.4f}, u2={u2_2:.4f}")
```
````


````{solution} repeated_strategies_in_the_prisoners_dilemma
:label: solution:repeated_strategies_in_the_prisoners_dilemma

Consider the Prisoner's Dilemma:

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

with strategies:

1. **TFT**: cooperate first, then copy opponent's previous action.
2. **Alternator**: cooperate first, then alternate $C, D, C, D, \ldots$
3. **75% cooperator**: cooperate with probability $0.75$ each round independently.

The normal form of the repeated game treats each of these strategies as an
action. We build the payoff matrix by computing the total (or average) payoff
for each pair.

**Case: $T = 100$ repetitions.**

We compute the payoff for each strategy pair by simulating the repeated game.

- **TFT vs TFT**: both cooperate every round. Payoff: $(3 \times 100, 3 \times 100) = (300, 300)$.

- **TFT vs Alternator**: TFT starts $C$, Alternator starts $C$. Round 1: $(C,C)$
  payoffs $(3,3)$. Round 2: Alternator defects; TFT copies so plays $C$ in
  round 2. Outcome: $(C,D)$ payoffs $(0,5)$. Round 3: TFT copies $D$ from round 2,
  Alternator cooperates: $(D,C)$ payoffs $(5,0)$. Pattern from round 2 onwards:
  $(C,D), (D,C), (C,D), \ldots$ alternating every round (99 rounds).
  Row payoff: $3 + 49\times(0+5) + 0 = 3 + 245 = 248$. Col payoff: $3 + 49\times(5+0) + 5 = 253$.
  (For $T=100$ there are 99 remaining rounds after round 1, i.e., 49 complete $(CD,DC)$ pairs plus one extra $CD$.)

- **TFT vs 75% cooperator**: varies by the random actions.

- **Alternator vs Alternator**: both alternate $(C, D, C, \ldots)$ in lock-step:
  Rounds 1,3,5,...: both play $C$, payoff $(3,3)$.
  Rounds 2,4,6,...: both play $D$, payoff $(1,1)$.
  50 rounds each: total $= 50 \times 3 + 50 \times 1 = 200$ for each.

- **Alternator vs 75% cooperator** and **75% vs 75%**: expected payoffs depend
  on probabilities.

Rather than computing all entries analytically, we use simulation via the
Axelrod library, which computes the normal form payoff matrix for these three
strategies.

**Normal form representation using average payoffs.**

We use the Axelrod library to obtain payoff matrices for each repetition count
and discount factor. The Nash equilibria are then identified from the payoff
matrices.

```{code-cell} python3
import axelrod as axl
import numpy as np
import nashpy as nash

players = [axl.TitForTat(), axl.Alternator(), axl.Random(0.75)]
player_names = ["TFT", "Alternator", "75%-Coop"]

def run_tournament(players, turns, repetitions=2000, seed=0):
    tournament = axl.Tournament(
        players=players, turns=turns, seed=seed, repetitions=repetitions,
    )
    results = tournament.play(progress_bar=False)
    return np.array(results.payoff_matrix)

# T=100
M_T100 = run_tournament(players, turns=100)
print("Average payoffs per turn, T=100:")
print(np.round(M_T100, 3))
print()
```

```{code-cell} python3
# T=99
M_T99 = run_tournament(players, turns=99)
print("Average payoffs per turn, T=99:")
print(np.round(M_T99, 3))
print()
```

```{code-cell} python3
# Infinite game with delta=1/4: prob_end = 1 - delta = 3/4
players_inf = [axl.TitForTat(), axl.Alternator(), axl.Random(0.75)]
tournament_inf = axl.Tournament(
    players=players_inf, prob_end=3/4, seed=0, repetitions=2000,
)
results_inf = tournament_inf.play(progress_bar=False)
M_inf = np.array(results_inf.payoff_matrix)
print("Average payoffs, infinite game delta=1/4:")
print(np.round(M_inf, 3))
```

**Nash equilibria analysis.**

For a symmetric 3-player (strategy) normal form game, we use nashpy to find
Nash equilibria of the reduced payoff matrix (treating the repeated game as a
one-shot game over the strategy space).

```{code-cell} python3
# For T=100, find Nash equilibria
# The payoff matrix is symmetric (M_c = M_r.T) since the PD is symmetric
for label, M in [("T=100", M_T100), ("T=99", M_T99), ("delta=1/4", M_inf)]:
    M_r_rep = np.array(M)
    M_c_rep = M_r_rep.T
    game_rep = nash.Game(M_r_rep, M_c_rep)
    eqs = list(game_rep.support_enumeration())
    print(f"\n{label} Nash equilibria (strategies: TFT, Alternator, 75%-Coop):")
    for eq in eqs:
        print(" ", [np.round(e, 3) for e in eq])
```

**Key observations:**

- For $T = 100$ (even number of rounds): TFT can be exploited by Alternator in
  the final stages since both know when the game ends. The Nash equilibrium
  analysis reveals whether mutual defection dominates.

- For $T = 99$ (odd): the parity of rounds affects the TFT-vs-Alternator
  interaction, potentially changing Nash equilibria.

- For infinite $\delta = 1/4$: the discount factor is low (players are
  impatient), so future cooperation is worth little. This is close to the
  short-horizon case; the Nash equilibrium tends toward mutual defection/low
  cooperation.

In all three cases, the stage game's dominant strategy (Defect) exerts pressure:
Nash equilibria in the repeated game tend to involve strategies that defect more
frequently when the discount factor is low or the game is finite and short. For
longer horizons and larger $\delta$, cooperative strategies like TFT can be Nash
equilibria.
````
