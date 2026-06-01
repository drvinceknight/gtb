---
kernelspec:
  name: python3
  display_name: "Python 3"
---

(chp:further_learning_dynamics)=

# Learning and Evolutionary Dynamics

The replicator dynamics and Moran process are just two of many ways a
population might update its strategies over time. This chapter examines a
broader family of learning and evolutionary dynamics, exploring how the choice
of update rule shapes long-run behaviour.

(sec:motivating_example_learning_dynamics)=

## Motivating Example: Does the Update Rule Matter?

Return to the graduate student reading group from
[](#sec:motivating_example_preprint). The same coordination game governs
citations, textbook ($T$) versus preprint ($P$), but now consider three
plausible ways students might update their habits:

1. **Imitation**: a student notices a peer doing well and copies them.
2. **Best-response**: a student calculates which citation would be optimal
   given current group behaviour and switches if warranted.
3. **Generational turnover**: new students join each cohort and tend to adopt
   whichever citation style is more prevalent.

The payoff matrix is the same in all three cases. Yet these mechanisms can
produce different trajectories, different fixation probabilities, and different
long-run distributions. This raises a fundamental question: **does the update
rule matter?**

The answer is yes, particularly in small populations, at high selection
intensity, or when the game has multiple equilibria. This chapter introduces
three families of update rules (imitation, introspection, and best-response)
alongside the Wright–Fisher process, and shows how they relate to each
other and to the [replicator dynamics](#chp:replicator_dynamics) and
[Moran process](#chp:moran_process) studied in previous chapters.

## Theory

### Definition: Imitation Dynamics

---

In **imitation dynamics** a population of $N$ individuals updates
strategy by pairwise comparison. At each step:

1. Two individuals $i$ and $j$ are selected uniformly at random.
2. Individual $i$ switches to $j$'s strategy with the **Fermi probability**:

$$
P(i \to j) = \frac{1}{1 + e^{-\beta(\pi_j - \pi_i)}}
$$

where $\pi_i$ and $\pi_j$ are their current payoffs and $\beta \geq 0$ is
the **selection intensity**.

---

The parameter $\beta$ controls how strongly payoff differences drive
imitation:

- $\beta = 0$: strategies are copied uniformly at random (neutral drift).
- $\beta \to \infty$: copying is deterministic; the higher-payoff strategy
  is always adopted.

```{note}
The Fermi function $1/(1+e^{-x})$ is borrowed from statistical physics,
where it describes the probability of a particle occupying a higher-energy
state. Here it models the "temperature" of decision-making: high $\beta$
means cold (rational), low $\beta$ means hot (noisy).
```

#### Example: Imitation in the Citation Game

For the [citation coordination game](#sec:motivating_example_preprint) with
$\beta = 1$, suppose the group has $N=4$ students with 2 citing the textbook
and 2 citing the preprint. Each student's fitness is:

$$
\pi_T = \frac{1 \cdot 3 + 2 \cdot 0}{3} = 1
\qquad
\pi_P = \frac{2 \cdot 1 + 1 \cdot 2}{3} = \frac{4}{3}
$$

If student $i$ cites $T$ and is paired with student $j$ citing $P$, the
probability that $i$ switches to $P$ is:

$$
\begin{align*}
P(i \to j) &= \frac{1}{1 + e^{-1 \cdot (4/3 - 1)}}\\
&= \frac{1}{1 + e^{-1/3}} \approx 0.582
\end{align*}
$$

Compare this to the Moran process, where the probability of the preprint
spreading would instead depend on relative fitness proportions. Both models
favour $P$ in this state, but at different rates and with different
stochastic properties.

### Definition: Introspection Dynamics

---

In **introspection dynamics** individuals update by counterfactual
reasoning rather than by observing others. At each step:

1. One individual $i$ is selected uniformly at random.
2. Individual $i$ computes the payoff $\pi_j$ they *would* receive if they
   switched to each alternative strategy $j$, holding all other individuals'
   strategies fixed.
3. They switch to strategy $j$ with the Fermi probability:

$$
P(i \to j) = \frac{1}{1 + e^{-\beta(\pi_j - \pi_i)}}
$$

---

The key distinction from imitation is the information used: imitation
requires observing another individual's payoff; introspection requires only
computing a hypothetical payoff from the current population composition.

#### Example: Introspection vs Imitation

In the citation game at state $(v_T, v_P) = (2, 2)$, a textbook-citing
student using introspection computes:

- Current payoff: $\pi_T = 1$ (playing $T$ against 1 $T$-player and 2
  $P$-players among the remaining 3 partners).
- Hypothetical payoff if switching: $\pi_P = (2 \cdot 1 + 1 \cdot 2)/3 =
  4/3$ (playing $P$ against the 2 $P$-players and 1 $T$-player).

The switching probability is the same as in the imitation example above,
$\approx 0.582$. In symmetric games with homogeneous populations the two
dynamics coincide; differences emerge in asymmetric games or structured
populations where who you observe versus who you *are* matters.

### Definition: Best-Response Dynamics

---

**Best-response dynamics** is the deterministic limit of introspection
dynamics as $\beta \to \infty$. At each step an individual switches to
whichever strategy has the highest expected payoff against the current
population:

$$
P(i \to j) =
\begin{cases}
1   & \text{if } \pi_j > \pi_i,\\
0   & \text{if } \pi_j < \pi_i,\\
1/2 & \text{if } \pi_j = \pi_i.
\end{cases}
$$

In the infinite-population continuous-time limit, the population share
$x_i$ of strategy $i$ evolves as [@gilboa1991social]:

$$
\dot{x}_i = \mathbf{1}[\pi_i = \max_k \pi_k] - x_i
$$

---

Best-response dynamics is used in economic models where agents are fully
rational and have perfect information about population composition. It
always converges to a Nash equilibrium or cycles around one, but unlike
replicator dynamics it can reach strict equilibria from any initial
condition.

### Definition: Wright–Fisher Process

---

The **Wright–Fisher process** models evolution in a population with
non-overlapping generations of fixed size $N$. Each generation is formed
by sampling $N$ offspring independently from the previous generation, where
strategy $i$ is chosen with probability proportional to its fitness:

$$
p_i = \frac{f_i}{\sum_k f_k}
$$

Optionally, each offspring mutates to a uniformly chosen strategy with
probability $\mu$.

---

Unlike the Moran process, which replaces one individual at a time, the
Wright–Fisher process replaces the entire population simultaneously. This
makes it the natural model for organisms with discrete, synchronised
generations (annual plants, insects, some microbes). The biological
origins of this process, and of the Moran process, are discussed in
[Chapter @chp:evolutionary_biology].

#### Example: One Generation of the Wright–Fisher Process

For the citation game at state $(v_T, v_P) = (3, 1)$ with $N=4$ and
$\beta = 1$ (using exponential fitness $f_i = e^{\beta \pi_i}$):

$$
f_T = e^{6/3} = e^2 \approx 7.39
\qquad
f_P = e^{3/3} = e^1 \approx 2.72
$$

The probability that a randomly sampled offspring cites $T$ is:

$$
p_T = \frac{7.39}{7.39 + 2.72} \approx 0.731
$$

The next generation $(v_T', v_P')$ follows a Binomial$(4,\ 0.731)$
distribution, so for example $P(v_T'=4) \approx 0.731^4 \approx 0.284$.

### Theorem: Mean-Field Limit

---

For all four dynamics (imitation, introspection, best-response, and
Wright–Fisher) in the limit of large population size $N \to \infty$ and
weak selection $\beta \to 0$ (with $\beta N$ held fixed), the expected
change in strategy frequencies converges to the **replicator equation**
[@traulsen2005coevolutionary; @hofbauer1998evolutionary]:

$$
\dot{x}_i = x_i(\pi_i - \bar{\pi}), \qquad \bar{\pi} = \sum_k x_k \pi_k
$$

---

This result explains why replicator dynamics occupies a central place in
evolutionary game theory: it is the universal mean-field limit shared by
all these distinct microscopic update rules. Differences between dynamics
matter most in small populations or at high selection intensity.

## Exercises

```{exercise}
:label: fermi_transition_probabilities

Consider the Prisoner's Dilemma with $R=3, S=0, T=5, P=1$ and a population
of $N=4$ with 2 cooperators and 2 defectors. Each individual interacts with
all $N-1$ others.

1. Compute the average payoff $\pi_C$ and $\pi_D$ at this state.
2. Using $\beta = 1$, compute the Fermi probability that a cooperator imitates
   a defector, and vice versa.
3. What happens to these probabilities as $\beta \to 0$ and $\beta \to \infty$?
```

```{exercise}
:label: comparing_dynamics

Consider the coordination game
$M = \begin{pmatrix}2 & 0 \\ 0 & 1\end{pmatrix}$
with $N=4$ individuals, starting from state $(v_1, v_2) = (2, 2)$.

1. Under imitation dynamics with $\beta = 2$, compute the probability that
   the number of type-1 individuals increases by 1.
2. Under the Moran process, compute the same probability.
3. Under the Wright–Fisher process (one generation, using $f_i = e^{\beta\pi_i}$
   with $\beta=2$), what is the probability of the next state being $(3,1)$?
4. Which dynamic most strongly favours strategy 1 in this state?
```

```{exercise}
:label: best_response_dynamics_coordination

Consider the coordination game with payoff matrix

$$
M = \begin{pmatrix}3 & 0 \\ 0 & 2\end{pmatrix}
$$

in the continuous best-response dynamics with population shares
$x_1, x_2 = 1 - x_1$.

1. Find all rest points of the dynamics.
2. Determine the stability of each rest point.
3. Compare to the Nash equilibria of the game.
```

```{exercise}
:label: update_rules_and_equilibrium_selection

Consider the Stag Hunt game:

$$
M = \begin{pmatrix}4 & 0 \\ 1 & 2\end{pmatrix}
$$

Both $(1,0)$ and $(0,1)$ are strict Nash equilibria (risk-dominant: $(0,1)$;
payoff-dominant: $(1,0)$).

1. Under replicator dynamics, which equilibrium does the system converge to
   from the initial condition $x_1 = 0.4$?
2. Under best-response dynamics, what is the basin of attraction of each
   equilibrium?
3. Briefly explain why best-response dynamics and replicator dynamics can
   select different equilibria in games with multiple strict Nash equilibria.
```

## Programming

The `ludics` library represents an
evolutionary game as a finite-population Markov chain and computes fixation
probabilities and stationary distributions exactly. It implements the Moran
process, Fermi imitation, and introspection dynamics directly, and its
transition-matrix builder accepts a custom update rule, which lets us add the
Wright–Fisher process as well.

### Setting up the citation game

We work with the citation coordination game on a population of $N = 4$ students.
A state records each individual's strategy ($0$ for textbook, $1$ for preprint),
and the fitness of an individual is its average payoff against the rest of the
population.

```{code-cell} python3
import numpy as np
import ludics

payoff_matrix = np.array([[3, 0], [1, 2]])  # citation game: T = 0, P = 1


def citation_fitness(state, payoff_matrix, **kwargs):
    """Average payoff of each individual against all others."""
    number_of_individuals = len(state)
    return np.array([
        np.mean([
            payoff_matrix[state[individual], state[other]]
            for other in range(number_of_individuals)
            if other != individual
        ])
        for individual in range(number_of_individuals)
    ])


state_space = ludics.get_state_space(N=4, k=2)
```

### Building each dynamic as a Markov chain

Moran, Fermi imitation, and introspection are built in. Wright–Fisher is not,
but because each of the $N$ offspring of a generation is drawn independently in
proportion to parental fitness, its transition probability factorises as a
product over offspring, and `generate_transition_matrix` accepts it as a custom
rule.

```{code-cell} python3
def wright_fisher_transition_probability(
    source, target, fitness_function, selection_intensity, **kwargs
):
    """Wright–Fisher: each offspring is sampled independently, in proportion
    to parental fitness (non-overlapping generations)."""
    fitness = 1 + selection_intensity * fitness_function(source, **kwargs)
    total_fitness = fitness.sum()
    probability = 1.0
    for offspring_type in target:
        probability *= fitness[source == offspring_type].sum() / total_fitness
    return probability


moran = ludics.generate_transition_matrix(
    state_space, citation_fitness, ludics.compute_moran_transition_probability,
    selection_intensity=1.0, payoff_matrix=payoff_matrix,
)
fermi = ludics.generate_transition_matrix(
    state_space, citation_fitness, ludics.compute_fermi_transition_probability,
    choice_intensity=1.0, payoff_matrix=payoff_matrix,
)
wright_fisher = ludics.generate_transition_matrix(
    state_space, citation_fitness, wright_fisher_transition_probability,
    selection_intensity=1.0, payoff_matrix=payoff_matrix,
)
introspection = ludics.generate_transition_matrix(
    state_space, citation_fitness,
    ludics.compute_introspection_transition_probability,
    choice_intensity=1.0, number_of_strategies=2, payoff_matrix=payoff_matrix,
)
```

### Does the update rule matter?

The three absorbing dynamics, Moran, Fermi imitation, and Wright–Fisher, each
end in fixation: every individual ends up citing either the textbook or the
preprint. We read off the probability that a single preprint adopter eventually
takes over, and it differs from one rule to the next, which is the central
message of this chapter.

```{code-cell} python3
single_adopter = next(i for i, s in enumerate(state_space) if s.sum() == 1)
all_preprint = next(i for i, s in enumerate(state_space) if s.sum() == 4)

for name, matrix in [("Moran", moran), ("Fermi imitation", fermi),
                     ("Wright-Fisher", wright_fisher)]:
    absorption = ludics.get_absorption_probabilities(matrix, state_space)
    pairs = np.array(absorption[single_adopter]).reshape(-1, 2)
    fixation = next(p for index, p in pairs if int(index) == all_preprint)
    print(f"{name}: fixation probability of one preprint adopter = {fixation:.4f}")
```

Introspection dynamics, by contrast, is ergodic: it never fixes but visits every
state indefinitely, so the natural summary is its stationary distribution.

```{code-cell} python3
stationary = ludics.compute_steady_state(introspection)
print(
    "Introspection: stationary probability of all-preprint =",
    round(float(stationary[all_preprint]), 4),
)
```

```{note}
The `ludics` cells above build the entire Markov chain and extract exact fixation
probabilities and stationary distributions, whereas the exercises and their
solutions work directly with the per-step transition probabilities by hand. The
two approaches describe the same dynamics but adopt different conventions, so
their numbers need not coincide exactly. In particular, `ludics` parametrises the
Fermi and introspection rules by a `choice_intensity` (an inverse temperature,
roughly $1/\beta$) and the Moran process by a fitness of the form
$1 + \delta\,\pi$, while the worked examples use $\beta$ directly, proportional
fitness $f = \pi$ for the Moran process, and exponential fitness
$f = e^{\beta \pi}$ for the Wright–Fisher process. Each is a standard choice, and
the qualitative comparison between update rules is unaffected.
```

(sec:notable_research_learning_dynamics)=

## Notable Research

The Fermi imitation rule used in this chapter was proposed and analysed by
[@traulsen2006pairwise], who showed that pairwise comparison dynamics reduces
to the replicator equation in the large-population, weak-selection limit. This
paper is foundational to the study of evolutionary dynamics in finite
populations under social learning.

Introspection dynamics is a more recent addition to this family, introduced by
[@couto2022introspection]. Unlike imitation, introspection does not require
observing a specific partner's outcome, only reasoning about what *would*
happen under an alternative strategy. This distinction becomes particularly
important in asymmetric games and has applications to human behavioural
experiments where direct comparison is not always possible.

Best-response dynamics has roots in the economic learning literature, tracing
back to [@gilboa1991social]. Its relationship to replicator dynamics and
its convergence properties in potential games are thoroughly analysed in
[@hofbauer1998evolutionary].

The Wright–Fisher process predates the Moran process in the biological
literature, originating in the foundational work of Fisher [@Fisher1930]
and Wright [@Wright1931] on genetic drift. The key result that both
processes converge to replicator dynamics in the large-population limit
was established in [@traulsen2005coevolutionary].

## Conclusion

This chapter surveyed four update rules (imitation, introspection,
best-response, and Wright–Fisher) as alternatives to the Moran process and
replicator dynamics covered in preceding chapters. Together they form a
landscape of evolutionary and learning models that share a common mean-field
limit (the replicator equation) but differ in their finite-population and
high-selection behaviour.

The choice of update rule is not merely a mathematical convention. It
reflects an assumption about how real agents (biological organisms, humans,
firms) actually change their behaviour: by copying successful peers, by
rational introspection, by best-responding to the current environment, or
through generational turnover. Understanding when these assumptions differ in
their predictions is essential for applying evolutionary game theory to
empirical settings.

[](#tbl:learning_dynamics_summary) summarises the key concepts.

```{table} Summary of learning and evolutionary dynamics
:label: tbl:learning_dynamics_summary
:align: center
:class: table-bordered

| Dynamic | Update mechanism | Finite population? | Mean-field limit |
|---|---|---|---|
| Replicator | Continuous frequency change proportional to relative payoff | No (infinite) | n/a (is the limit) |
| Moran | Birth proportional to fitness; death uniform | Yes | Replicator |
| Imitation | Fermi pairwise copying with selection intensity $\beta$ | Yes | Replicator |
| Introspection | Counterfactual switching via Fermi rule | Yes | Replicator |
| Best-response | Deterministic switch to highest-payoff strategy | No (or $\beta\to\infty$) | Replicator |
| Wright–Fisher | Multinomial sampling proportional to fitness per generation | Yes | Replicator |

```

---

```{attention}
All of the dynamics in this chapter, and in the two preceding chapters,
converge to the replicator equation as the population becomes large and
selection becomes weak. The replicator equation is therefore not just one
model among many: it is the universal mean-field description of evolutionary
and social learning. The distinctive predictions of finite-population models
emerge precisely where this approximation breaks down.
```

---

(solutions:further_learning_dynamics)=

## Solutions

````{solution} fermi_transition_probabilities
:label: solution:fermi_transition_probabilities

1. With $N=4$, 2 cooperators (C) and 2 defectors (D), each individual interacts
   with all $N-1 = 3$ others.

   For a cooperator, the opponents are 1 cooperator and 2 defectors:

   $$
   \pi_C = \frac{1 \cdot R + 2 \cdot S}{3} = \frac{1 \cdot 3 + 2 \cdot 0}{3} = 1
   $$

   For a defector, the opponents are 2 cooperators and 1 defector:

   $$
   \pi_D = \frac{2 \cdot T + 1 \cdot P}{3} = \frac{2 \cdot 5 + 1 \cdot 1}{3} = \frac{11}{3}
   $$

2. Using the [Fermi probability](#chp:further_learning_dynamics) with $\beta = 1$:

   The probability that a cooperator imitates a defector (switching from C to D):

   $$
\begin{align*}
   P(C \to D) &= \frac{1}{1 + e^{-\beta(\pi_D - \pi_C)}} \\
   &= \frac{1}{1 + e^{-(11/3 - 1)}} \\
   &= \frac{1}{1 + e^{-8/3}}
   \approx \frac{1}{1 + 0.0695}
   \approx 0.935
\end{align*}
   $$

   The probability that a defector imitates a cooperator (switching from D to C):

   $$
\begin{align*}
   P(D \to C) &= \frac{1}{1 + e^{-\beta(\pi_C - \pi_D)}} \\
   &= \frac{1}{1 + e^{-(1 - 11/3)}} \\
   &= \frac{1}{1 + e^{8/3}}
   \approx \frac{1}{1 + 14.39}
   \approx 0.065
\end{align*}
   $$

   Note that $P(C \to D) + P(D \to C) = 1$, as expected from the symmetry
   $P(i \to j) = 1 - P(j \to i)$.

3. As $\beta \to 0$: Both Fermi probabilities converge to $1/2$. The exponential
   term $e^{-\beta \Delta\pi} \to 1$ regardless of the payoff difference $\Delta\pi$,
   so $P(i \to j) \to 1/(1+1) = 1/2$. Imitation becomes purely random, neutral
   drift.

   As $\beta \to \infty$: The higher-payoff individual is always imitated. Since
   $\pi_D > \pi_C$, we get $P(C \to D) \to 1$ and $P(D \to C) \to 0$. Defectors
   are always imitated and cooperators never are; the dynamics are deterministic
   and defection takes over.

```{code-cell} python3
import numpy as np

R, S, T, P_pd = 3, 0, 5, 1
N = 4
n_C, n_D = 2, 2

pi_C = (n_C - 1) * R + n_D * S
pi_C /= (N - 1)
pi_D = n_C * T + (n_D - 1) * P_pd
pi_D /= (N - 1)

print(f"pi_C = {pi_C}")
print(f"pi_D = {pi_D:.4f}")

beta = 1
P_C_to_D = 1 / (1 + np.exp(-beta * (pi_D - pi_C)))
P_D_to_C = 1 / (1 + np.exp(-beta * (pi_C - pi_D)))
print(f"P(C->D) = {P_C_to_D:.4f}")
print(f"P(D->C) = {P_D_to_C:.4f}")
```

```{code-cell} python3
import matplotlib.pyplot as plt

beta_values = np.linspace(0.01, 5, 300)
P_C_to_D_vals = 1 / (1 + np.exp(-beta_values * (pi_D - pi_C)))
P_D_to_C_vals = 1 / (1 + np.exp(-beta_values * (pi_C - pi_D)))

plt.figure()
plt.plot(beta_values, P_C_to_D_vals, label=r"$P(C \to D)$")
plt.plot(beta_values, P_D_to_C_vals, label=r"$P(D \to C)$")
plt.axhline(0.5, color="gray", linestyle="--", linewidth=0.8)
plt.xlabel(r"$\beta$")
plt.ylabel("Fermi probability")
plt.title("Fermi transition probabilities vs selection intensity")
plt.legend()
plt.ylim(0, 1);
```
````

````{solution} comparing_dynamics
:label: solution:comparing_dynamics

The game is
$M = \begin{pmatrix}2 & 0 \\ 0 & 1\end{pmatrix}$
with $N = 4$ and state $(v_1, v_2) = (2, 2)$.

Each individual interacts with all $N-1 = 3$ others.

**Payoffs at state $(2,2)$:**

For a type-1 individual (1 ally among 3 opponents):

$$
\pi_1 = \frac{1 \cdot 2 + 2 \cdot 0}{3} = \frac{2}{3}
$$

For a type-2 individual (2 opponents of type 1, 1 ally):

$$
\pi_2 = \frac{2 \cdot 0 + 1 \cdot 1}{3} = \frac{1}{3}
$$

1. **Imitation dynamics with $\beta = 2$.**

   For the number of type-1 individuals to increase by 1, a type-2 individual
   must be selected as $i$, a type-1 individual must be selected as $j$, and $i$
   must adopt $j$'s strategy.

   Probability of selecting a type-2 individual as $i$ and a type-1 individual as
   $j$:

   $$
   \frac{v_2}{N} \cdot \frac{v_1}{N-1} = \frac{2}{4} \cdot \frac{2}{3} = \frac{1}{3}
   $$

   Fermi probability that the type-2 individual imitates the type-1 individual:

   $$
\begin{align*}
   P(2 \to 1) &= \frac{1}{1 + e^{-\beta(\pi_1 - \pi_2)}} \\
   &= \frac{1}{1 + e^{-2(2/3 - 1/3)}} \\
   &= \frac{1}{1 + e^{-2/3}}
   \approx 0.661
\end{align*}
   $$

   Therefore the probability of increasing type-1 count by 1:

   $$
   P(\text{increase}) = \frac{1}{3} \times \frac{1}{1 + e^{-2/3}} \approx 0.220
   $$

2. **Moran process.**

   In the Moran process, fitness is proportional to payoff (using linear fitness
   $f_i = 1 + \delta \pi_i$ or simply $f_i = \pi_i$ with normalisation). Using
   proportional fitness $f_i = \pi_i$:

   $$
   p_{2 \to 1} = \frac{v_1 \cdot \pi_1}{v_1 \pi_1 + v_2 \pi_2} \cdot \frac{v_2}{N-1}
   $$

   The probability that a type-1 is selected for reproduction and a type-2 for
   removal:

   $$
\begin{align*}
   P(\text{increase}) &= \frac{v_1 \pi_1}{v_1 \pi_1 + v_2 \pi_2} \cdot \frac{v_2}{N} \\
   &= \frac{2 \cdot (2/3)}{2 \cdot (2/3) + 2 \cdot (1/3)} \cdot \frac{2}{4} \\
   &= \frac{4/3}{4/3 + 2/3} \cdot \frac{1}{2} \\
   &= \frac{2}{3} \cdot \frac{1}{2} = \frac{1}{3}
\end{align*}
   $$

3. **Wright-Fisher process (one generation, $f_i = e^{\beta \pi_i}$ with $\beta=2$).**

   Exponential fitnesses:

   $$
   f_1 = e^{2 \cdot 2/3} = e^{4/3} \approx 3.794
   \qquad
   f_2 = e^{2 \cdot 1/3} = e^{2/3} \approx 1.948
   $$

   Sampling probability for type-1:

   $$
\begin{align*}
   p_1 &= \frac{v_1 f_1}{v_1 f_1 + v_2 f_2} \\
   &= \frac{2 e^{4/3}}{2 e^{4/3} + 2 e^{2/3}} \\
   &= \frac{e^{4/3}}{e^{4/3} + e^{2/3}} \\
   &= \frac{1}{1 + e^{-2/3}}
   \approx 0.661
\end{align*}
   $$

   The next generation $(v_1', v_2')$ follows Binomial$(4, p_1)$. The probability
   of the next state being $(3, 1)$ is:

   $$
\begin{align*}
   P(v_1' &= 3) = \binom{4}{3} p_1^3 (1-p_1)^1 \\
   &= 4 \times (0.661)^3 \times (0.339)
   \approx 4 \times 0.289 \times 0.339
   \approx 0.392
\end{align*}
   $$

4. **Comparison.**

   - Imitation dynamics: $P(\text{increase}) \approx 0.220$
   - Moran process: $P(\text{increase}) = 1/3 \approx 0.333$
   - Wright-Fisher (probability of state $(3,1)$): $\approx 0.392$

   The Wright-Fisher process most strongly favours strategy 1 in this state,
   followed by the Moran process, then imitation dynamics. The difference arises
   because the Wright-Fisher process uses exponential fitness (amplifying payoff
   differences) and replaces the whole population at once, whereas imitation uses
   the Fermi rule with a moderate $\beta$, and the Moran process uses linear
   (proportional) fitness.

```{code-cell} python3
import numpy as np
from math import comb

M = np.array([[2, 0], [0, 1]])
N = 4
v1, v2 = 2, 2
beta = 2

# Payoffs
pi1 = ((v1 - 1) * M[0, 0] + v2 * M[0, 1]) / (N - 1)
pi2 = (v1 * M[1, 0] + (v2 - 1) * M[1, 1]) / (N - 1)
print(f"pi_1 = {pi1:.4f}, pi_2 = {pi2:.4f}")

# 1. Imitation
P_2to1 = 1 / (1 + np.exp(-beta * (pi1 - pi2)))
P_imitation_increase = (v2 / N) * (v1 / (N - 1)) * P_2to1
print(f"Imitation P(increase) = {P_imitation_increase:.4f}")

# 2. Moran
total_fitness = v1 * pi1 + v2 * pi2
P_moran_increase = (v1 * pi1 / total_fitness) * (v2 / N)
print(f"Moran P(increase) = {P_moran_increase:.4f}")

# 3. Wright-Fisher
f1 = np.exp(beta * pi1)
f2 = np.exp(beta * pi2)
p1 = (v1 * f1) / (v1 * f1 + v2 * f2)
P_WF_3 = comb(N, 3) * p1**3 * (1 - p1)**1
print(f"Wright-Fisher p_1 = {p1:.4f}")
print(f"Wright-Fisher P(next state = (3,1)) = {P_WF_3:.4f}")
```
````

````{solution} best_response_dynamics_coordination
:label: solution:best_response_dynamics_coordination

The game is
$M = \begin{pmatrix}3 & 0 \\ 0 & 2\end{pmatrix}$
with population shares $x_1$ and $x_2 = 1 - x_1$.

The expected payoffs against the current population are:

$$
\pi_1(x_1) = 3x_1 + 0 \cdot (1-x_1) = 3x_1
$$

$$
\pi_2(x_1) = 0 \cdot x_1 + 2(1-x_1) = 2(1-x_1)
$$

1. **Rest points of best-response dynamics.**

   From the [definition of best-response dynamics](#chp:further_learning_dynamics):

   $$
   \dot{x}_1 = \mathbf{1}[\pi_1 = \max(\pi_1, \pi_2)] - x_1
   $$

   At a rest point $\dot{x}_1 = 0$. Three cases arise:

   - If $\pi_1 > \pi_2$ (i.e., $3x_1 > 2(1-x_1)$, i.e., $x_1 > 2/5$):
     $\dot{x}_1 = 1 - x_1 = 0 \Rightarrow x_1 = 1$.
   - If $\pi_1 < \pi_2$ (i.e., $x_1 < 2/5$):
     $\dot{x}_1 = 0 - x_1 = 0 \Rightarrow x_1 = 0$.
   - If $\pi_1 = \pi_2$ (i.e., $x_1 = 2/5$): both strategies are best responses,
     so by the convention $\mathbf{1}[\pi_1 = \max] = 1/2$ the target share is
     $1/2$, giving $\dot{x}_1 = 1/2 - 2/5 = 1/10 \neq 0$.

   So $x_1 = 2/5$ is **not** a rest point of the best-response dynamics (in
   continuous time with this convention).

   The rest points are $x_1 \in \{0, 1\}$.

2. **Stability of each rest point.**

   - For $x_1 \in (0, 2/5)$: $\pi_2 > \pi_1$, so $\dot{x}_1 = 0 - x_1 = -x_1 < 0$.
     The trajectory moves toward $x_1 = 0$. Thus $x_1 = 0$ is **stable**.
   - For $x_1 \in (2/5, 1)$: $\pi_1 > \pi_2$, so $\dot{x}_1 = 1 - x_1 > 0$.
     The trajectory moves toward $x_1 = 1$. Thus $x_1 = 1$ is **stable**.
   - The threshold $x_1 = 2/5$ is an unstable boundary: perturbations away from
     $2/5$ are amplified, not corrected.

   Both pure states are stable rest points. The basin of attraction of $x_1 = 0$
   is $[0, 2/5)$ and of $x_1 = 1$ is $(2/5, 1]$.

3. **Comparison to Nash equilibria.**

   The Nash equilibria of $M = \begin{pmatrix}3 & 0 \\ 0 & 2\end{pmatrix}$ are:

   - Pure Nash: $(1,0)$ and $(0,1)$ (both strict, as they are the best response
     to themselves in a coordination game).
   - Mixed Nash: $(x_1^*, 1-x_1^*)$ with $x_1^* = 2/5$, found by making the
     opponent indifferent: $3x_1 = 2(1-x_1) \Rightarrow x_1 = 2/5$.

   The two stable rest points $x_1 \in \{0, 1\}$ correspond exactly to the two
   strict Nash equilibria. The mixed Nash equilibrium at $x_1 = 2/5$ is **not** a
   rest point of the best-response dynamics in the continuous formulation (and is
   unstable under nearby perturbations). This is consistent with the general
   result that rest points of best-response dynamics are Nash equilibria, and
   strict Nash equilibria are always stable rest points.

```{code-cell} python3
import numpy as np
import matplotlib.pyplot as plt

M = np.array([[3, 0], [0, 2]])
x1_values = np.linspace(0, 1, 500)

pi1 = M[0, 0] * x1_values + M[0, 1] * (1 - x1_values)
pi2 = M[1, 0] * x1_values + M[1, 1] * (1 - x1_values)

# Best-response dynamics: dx1/dt = BR(x) - x1
# BR = 1 if pi1 > pi2, 0 if pi1 < pi2, 1/2 if equal
BR = np.where(pi1 > pi2, 1.0, np.where(pi1 < pi2, 0.0, 0.5))
dx1_dt = BR - x1_values

plt.figure()
plt.plot(x1_values, dx1_dt, label=r"$\dot{x}_1$")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(2/5, color="red", linestyle="--", label=r"$x_1=2/5$ (mixed NE)")
plt.xlabel("$x_1$")
plt.ylabel(r"$\dot{x}_1$")
plt.title("Best-response dynamics for coordination game")
plt.legend()
plt.ylim(-1.1, 1.1);
```
````

````{solution} update_rules_and_equilibrium_selection
:label: solution:update_rules_and_equilibrium_selection

The Stag Hunt game is
$M = \begin{pmatrix}4 & 0 \\ 1 & 2\end{pmatrix}$
with $x_1$ denoting the share of the population playing strategy 1 (Stag).

The expected payoffs are:

$$
\pi_1(x_1) = 4x_1 + 0 \cdot (1-x_1) = 4x_1
$$

$$
\pi_2(x_1) = 1 \cdot x_1 + 2(1-x_1) = 2 - x_1
$$

1. **Replicator dynamics from $x_1 = 0.4$.**

   The average fitness is:

   $$
\begin{align*}
   \bar{\pi} &= x_1 \pi_1 + (1-x_1)\pi_2 = x_1 \cdot 4x_1 + (1-x_1)(2-x_1) \\
   &= 4x_1^2 + 2 - 3x_1 + x_1^2 = 5x_1^2 - 3x_1 + 2
\end{align*}
   $$

   The replicator equation:

   $$
\begin{align*}
   \dot{x}_1 &= x_1(\pi_1 - \bar{\pi}) = x_1(4x_1 - (5x_1^2 - 3x_1 + 2)) \\
   &= x_1(-5x_1^2 + 7x_1 - 2) \\
   &= -x_1(5x_1 - 2)(x_1 - 1)
\end{align*}
   $$

   The interior fixed point where $\pi_1 = \pi_2$:

   $$
   4x_1 = 2 - x_1 \Rightarrow x_1^* = \frac{2}{5} = 0.4
   $$

   At $x_1 = 0.4$ exactly, we are at the interior fixed point $x_1^* = 2/5$.
   The stability at $x_1^*$ determines where nearby trajectories go.

   Evaluate the derivative of $\dot{x}_1$ at $x_1^*$: for $x_1$ slightly above
   $2/5$ (say $x_1 = 0.41$):

   $$
   \pi_1(0.41) = 4(0.41) = 1.64 > \pi_2(0.41) = 2 - 0.41 = 1.59
   $$

   So $\dot{x}_1 > 0$ for $x_1 > 2/5$: the trajectory moves toward $x_1 = 1$.

   For $x_1$ slightly below $2/5$ (say $x_1 = 0.39$):

   $$
   \pi_1(0.39) = 1.56 < \pi_2(0.39) = 1.61
   $$

   So $\dot{x}_1 < 0$ for $x_1 < 2/5$: the trajectory moves toward $x_1 = 0$.

   Since the initial condition $x_1 = 0.4 = x_1^*$ is exactly the unstable fixed
   point, the system is in a degenerate case. Any infinitesimal perturbation above
   $2/5$ leads to convergence to $x_1 = 1$ (payoff-dominant, Stag equilibrium),
   and any perturbation below $2/5$ leads to $x_1 = 0$ (risk-dominant, Hare
   equilibrium).

   Starting from $x_1 = 0.4$ exactly, the system remains at this unstable
   equilibrium in exact arithmetic. In practice, numerical integration will send
   it to one of the two pure states depending on rounding. The dynamics are
   exquisitely sensitive at this threshold; this is the defining feature of
   the mixed Nash equilibrium being unstable under replicator dynamics.

2. **Best-response dynamics: basins of attraction.**

   Under best-response dynamics, the best response switches at $\pi_1 = \pi_2$,
   i.e., at $x_1^* = 2/5$.

   - For $x_1 > 2/5$: $\pi_1 > \pi_2$, so the best response is strategy 1.
     $\dot{x}_1 = 1 - x_1 > 0$. Basin of attraction of $(1, 0)$: $(2/5, 1]$.
   - For $x_1 < 2/5$: $\pi_2 > \pi_1$, so best response is strategy 2.
     $\dot{x}_1 = 0 - x_1 = -x_1 < 0$. Basin of attraction of $(0, 1)$: $[0, 2/5)$.

   The basin of the payoff-dominant equilibrium $(1,0)$ is $(2/5, 1]$.
   The basin of the risk-dominant equilibrium $(0,1)$ is $[0, 2/5)$.

   Note: the risk-dominant equilibrium $(0,1)$ has the larger basin under
   best-response dynamics (since $2/5 < 1/2$). This is in fact a general result:
   best-response dynamics (and many learning dynamics) favour the risk-dominant
   equilibrium when the mixed Nash equilibrium lies below $1/2$.

3. **Why the two dynamics can select different equilibria.**

   Best-response dynamics and replicator dynamics both have the same rest points
   (Nash equilibria) and the same stability classification at the pure states.
   However, they can differ in their transient behaviour and selected equilibrium
   in two key ways:

   - **Speed of convergence**: Replicator dynamics amplifies payoff differences
     gradually (proportional to current frequency $x_i$ and excess payoff), while
     best-response dynamics switches immediately and completely to the best strategy.
     Near the interior fixed point, the two dynamics can therefore traverse different
     paths in state space.
   - **Selection at the boundary**: In games where the interior equilibrium coincides
     with a risk-dominant threshold ($x^* \neq 1/2$), the basin of attraction under
     replicator dynamics depends on the cubic form of the replicator equation, while
     under best-response dynamics the basin is determined purely by $x^*$ as a
     linear threshold. For this game both agree (the unstable fixed point is at
     $x^* = 2/5$ for both), but in more complex multi-strategy games the basins
     can genuinely differ.
   - **Stochastic finite-population versions**: Moran-process-like stochastic
     analogues of these dynamics can select different equilibria because the
     transition probabilities depend on the microscopic update rule, not just the
     mean-field dynamics.

```{code-cell} python3
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

x_1 = sym.Symbol("x_1")
M_sym = sym.Matrix([[4, 0], [1, 2]])

pi1 = 4 * x_1
pi2 = 2 - x_1
phi = x_1 * pi1 + (1 - x_1) * pi2
x1_dot = x_1 * (pi1 - phi)
x1_dot_simplified = sym.simplify(x1_dot)
print("Replicator equation:", x1_dot_simplified)
fixed_points = sym.solveset(x1_dot_simplified, x_1)
print("Fixed points:", fixed_points)
```

```{code-cell} python3
x1_values = np.linspace(0, 1, 500)
pi1_num = 4 * x1_values
pi2_num = 2 - x1_values
phi_num = x1_values * pi1_num + (1 - x1_values) * pi2_num
x1_dot_num = x1_values * (pi1_num - phi_num)

# Best-response dynamics
BR = np.where(pi1_num > pi2_num, 1.0, np.where(pi1_num < pi2_num, 0.0, 0.5))
br_dot = BR - x1_values

plt.figure(figsize=(8, 5))
plt.plot(x1_values, x1_dot_num, label="Replicator $\\dot{x}_1$")
plt.plot(x1_values, br_dot, label="Best-response $\\dot{x}_1$", linestyle="--")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(2/5, color="red", linestyle=":", label=r"$x_1^*=2/5$")
plt.xlabel("$x_1$")
plt.ylabel(r"$\dot{x}_1$")
plt.title("Replicator vs best-response dynamics: Stag Hunt")
plt.legend()
plt.ylim(-0.5, 0.5);
```
````
