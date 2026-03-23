---
kernelspec:
  name: python3
  display_name: "Python 3"
---

(chp:evolutionary_biology)=

# The Biological Origins of Evolutionary Game Theory

Evolutionary biology poses questions that look surprisingly like strategic
games: which traits persist in a population, and why? This chapter traces the
biological origins of evolutionary game theory, introducing the evolutionarily
stable strategy and laying the groundwork for the dynamic models that follow.

(sec:motivating_example_stag_antlers)=

## Motivating Example: Why Don't Stags Have Bigger Antlers?

Every autumn on the Scottish hillside, red deer stags compete for access to
females. A stag with larger, heavier antlers is more likely to win a contest
— but growing those antlers over the summer demands enormous energy that
could otherwise go into body condition, immune function, and surviving the
winter.

Here is the puzzle. Suppose in some generation nearly all stags invest
lightly in antler growth. A single stag that invests heavily wins almost
every contest it enters: the other stags, with their modest headgear, back
down quickly. This heavy-investing stag leaves far more offspring than its
rivals. Natural selection, therefore, should favour heavier investment.

Now imagine the next few generations, as heavy investment spreads. Most
stags now carry large antlers. A contest between two of them is no longer
quick: both hold their ground, the fight escalates, and both risk serious
injury. The energy spent growing those antlers no longer buys the advantage
it once did. A stag that invests a little less survives more winters, has
more chances to breed, and may actually do *better* on average than its
heavily-armed neighbours.

So selection favours heavier antlers when they are rare — but the advantage
erodes as they become common. The payoff to an antler-investment strategy
**depends on what strategy the rest of the population is using**. This is
not just differential reproduction; it is differential reproduction that
depends on interaction. It is a game.

The question this example raises — *what is the stable investment level, and
why is it not simply "as large as possible"?* — cannot be answered by
classical genetics alone. It requires the framework developed in this chapter.

## Theory

(sec:bio_natural_selection)=

### Darwin's Three Conditions

In 1859 Darwin proposed that the diversity of life could arise from a
single, simple mechanism — no designer, no foresight, no goal. Three
observable facts about populations are sufficient:

1. **Variation.** Individuals differ from one another in heritable traits:
   body size, beak shape, defensive behaviour, antler investment.

2. **Heritability.** Offspring tend to resemble their parents more than
   they resemble randomly chosen members of the population. Traits are
   passed down.

3. **Differential reproduction.** Some individuals, by virtue of their
   traits, survive longer or leave more offspring than others.

When these three conditions hold, the composition of a population *must*
change over time. Traits that help their bearers reproduce become more
common in the next generation; traits that hinder reproduction fade away.
Darwin called this process **natural selection**.

```{note}
Natural selection is not a force pushing organisms toward some ideal form.
It is a filtering process: variants that reproduce more simply leave more
copies of themselves. There is no planning, no goal, no optimisation — only
differential survival and reproduction, generation after generation.
```

All three conditions hold for stag antlers. Antler size varies across
individuals. It is partly inherited. And it affects how many offspring a
stag leaves (via contest outcomes). Natural selection therefore acts on
antler investment — the only question is in which direction.

(sec:bio_strategy)=

### What Is a "Strategy" in Biology?

In game theory a strategy is a decision rule. In biology a **strategy** is
an inherited behavioural tendency: the tendency to fight or retreat, to
cooperate or defect, to invest heavily in display or conserve resources.

Crucially, biological strategies are not chosen. A stag does not calculate
expected payoffs and decide on an antler investment level. It expresses a
phenotype that is, at least partly, inherited from its parents. Individuals
that happen to inherit effective strategies — effective *against the
opponents they actually encounter* — leave more offspring. Those offspring
inherit the same tendencies. Over generations, effective strategies spread.

The word "strategy" in evolutionary biology is shorthand for an
*inherited behavioural phenotype*. The rational-agent interpretation is a
useful fiction that lets us apply game-theoretic mathematics to a process
that is entirely mechanical.

(sec:bio_fitness)=

### Fitness: Reproductive Success as Payoff

The central quantity in evolutionary biology is **fitness** — the expected
number of surviving offspring an individual leaves. Variants with higher
fitness increase in frequency; variants with lower fitness decline.

In classical population genetics, fitness is treated as a fixed property
of a type. If type $A$ produces on average $W_A$ offspring and type $B$
produces $W_B$, and their current frequencies are $x_A$ and $x_B = 1 - x_A$,
then after one generation of selection:

$$
x_A' = \frac{W_A \, x_A}{W_A \, x_A + W_B \, x_B} = \frac{W_A}{\bar W} \, x_A
$$

where $\bar W = W_A x_A + W_B x_B$ is the mean fitness of the population.
Type $A$ increases in frequency whenever $W_A > \bar W$ — whenever its
fitness exceeds the population average.

This is correct when fitnesses are constant. But in the stag example,
fitnesses are not constant: the payoff to heavy antler investment is high
when it is rare and low when it is common. Fitness depends on the current
composition of the population.

(sec:bio_frequency_dependence)=

### Frequency-Dependent Selection

Selection is **frequency-dependent** when the fitness of a type depends on
the current composition of the population, not just on its own properties
in isolation.

Frequency dependence arises whenever individuals interact — which is
essentially always in real populations. The stag antler example is a
canonical instance, but the phenomenon is ubiquitous:

- A bacterium that secretes a costly public-good molecule benefits the
  group but is exploited by non-secretors. Its fitness advantage depends
  on how many non-secretors are present.
- A fish that mimics a toxic species is protected by predators — but only
  while the toxic species remains common enough for predators to have
  learned the association.
- A worker bee that reproduces rather than works gains personally in the
  short run — but a colony of non-workers produces nothing and dies.

In all these cases, what makes a strategy "good" depends on what strategies
your neighbours are using. This is the defining feature of an evolutionary
game.

(sec:bio_hawk_dove)=

### The Hawk–Dove Game

The stag example is formalised by the **Hawk–Dove game**, introduced by
Maynard Smith and Price [@smith1973logic] to explain why animal contests
so rarely escalate to serious injury.

Two strategies:

- **Hawk** (H): always escalate; fight until injured or opponent retreats.
- **Dove** (D): display first; retreat immediately if opponent escalates.

Each contest is over a resource worth $V > 0$ to the winner. A fight
between two Hawks injures one of them at cost $C$, where $C > V$. The
expected payoffs for each encounter type are:

$$
\begin{array}{c|cc}
       & \text{meets H} & \text{meets D} \\
\text{H plays} & \frac{V-C}{2} & V \\
\text{D plays} & 0             & \frac{V}{2}
\end{array}
$$

In a population where Hawks make up fraction $x$, the expected fitness of
each strategy is:

$$
\pi_H(x) = \frac{V-C}{2} \cdot x + V \cdot (1-x) = V - x\frac{V+C}{2}
$$

$$
\pi_D(x) = 0 \cdot x + \frac{V}{2}(1-x) = \frac{V(1-x)}{2}
$$

Setting $\pi_H = \pi_D$ gives the frequency at which neither strategy has
an advantage:

$$
x^* = \frac{V}{C}
$$

Since $C > V$, we have $x^* \in (0,1)$: the stable outcome is a
**mixed population**, not fixation of either pure strategy. For $x < x^*$,
Hawks do better than Doves and increase; for $x > x^*$, Doves do better
and Hawks decrease. The equilibrium is stable and corresponds to a Nash
equilibrium of the underlying game.

```{note}
In the stag example, "Hawk" corresponds to heavy antler investment
and "Dove" to light investment. The stable antler investment level in the
population is $x^* = V/C$ — determined entirely by the ratio of the
resource value to the cost of escalation. Real stag populations show
exactly this kind of stable polymorphism in investment strategies.
```

(sec:bio_bridge)=

### The Bridge: Fitness Is Payoff

The conceptual step from population genetics to evolutionary game theory
requires a single substitution:

> **Replace the fixed fitness constants of classical genetics with payoffs
> that depend on what strategies you encounter.**

In a pairwise interaction model, where each individual is paired at random
with another drawn from the population, the expected fitness of an individual
using strategy $i$ in a population where strategy $j$ has frequency $x_j$ is:

$$
\pi_i(x) = \sum_j x_j \cdot M_{ij}
$$

where $M_{ij}$ is the payoff to strategy $i$ when meeting strategy $j$.
The payoff matrix $M$ *is* the fitness matrix. Strategies with above-average
fitness increase in frequency; strategies with below-average fitness decline.

```{table} The correspondence between population genetics and evolutionary game theory
:label: tbl:genetics_egt_correspondence
:align: center
:class: table-bordered

| Population genetics | Evolutionary game theory |
|---|---|
| Genotype / allele | Strategy |
| Absolute fitness $W_i$ | Expected payoff $\pi_i$ |
| Fitness advantage over mean | $\pi_i - \bar\pi$ drives frequency change |
| Frequency-dependent fitness | Payoff matrix $M_{ij}$ |
| Mutation rate $\mu$ | Strategy exploration / trembling hand |
| Population size $N$ | Governs how much chance matters vs selection |
| Genetic drift | Stochastic fluctuations in finite-population models |
| Evolutionarily stable strategy | Nash equilibrium that selection cannot destabilise |

```

(sec:bio_roadmap)=

### What the Following Chapters Formalise

**[Replicator Dynamics](#chp:replicator_dynamics)** takes the limit of a
very large, well-mixed population and asks: how do strategy frequencies
change continuously over time? The answer is the replicator equation
$\dot x_i = x_i(\pi_i - \bar\pi)$. This is the continuous-time mathematical
form of natural selection under frequency-dependent fitness.

**[The Moran Process](#chp:moran_process)** takes a small, finite population
seriously. In a small population, chance matters: even a fitter strategy can
be lost by bad luck before it spreads. The Moran process models one individual
being copied at each time step, and the key question is the *fixation
probability* — the chance that a single mutant takes over rather than dying
out.

**[Learning and Evolutionary Dynamics](#chp:further_learning_dynamics)**
asks what happens when individuals update strategies by imitation, rational
introspection, or best-response. These social-learning mechanisms produce
the same large-population limit as biological evolution, but differ in
important ways in small populations.

Together these chapters show that the replicator equation is the
**universal large-population limit** of all plausible evolutionary and
social-learning update rules — and that the Nash equilibria of the stage
game are its rest points.

## Exercises

```{exercise}
:label: bio_selection_recurrence

A population of beetles has two colour morphs: cryptic (C, blends with
bark) and conspicuous (K, visible to predators). In a forest environment,
$W_C = 1.08$ and $W_K = 1.0$. Starting from $x_C = 0.2$:

1. Compute $x_C'$ after one generation of selection.
2. Compute $x_C''$ after a second generation.
3. In which direction is selection pushing the population, and why?
4. If the environment changes so that $W_C = 0.9$ and $W_K = 1.0$,
   repeat parts 1–3. What does this illustrate about the role of
   environment in determining which traits are favoured?
```

```{exercise}
:label: bio_frequency_dependence_classify

For each of the following scenarios, state whether fitness is
frequency-dependent and briefly justify your answer:

1. A plant that photosynthesises more efficiently than its neighbours has
   higher fitness regardless of the plant community around it.
2. A fish that mimics the appearance of a toxic species is protected from
   predators, but only while the toxic species remains common enough for
   predators to have learned the association.
3. In a public goods game, a cooperator's benefit depends on how many
   others also cooperate.
4. A faster cheetah always catches more prey, independently of what other
   cheetahs are doing.
```

```{exercise}
:label: bio_hawk_dove_equilibrium

For the Hawk–Dove game with $V = 4$ and $C = 10$:

1. Write out the payoff matrix.
2. Compute the equilibrium frequency $x^* = V/C$.
3. Verify that $x^*$ is a Nash equilibrium of the stage game: show
   that at $x = x^*$, a Hawk and a Dove receive the same expected payoff.
4. Starting from $x_H = 0.1$, is the Hawk frequency increasing or
   decreasing? What about from $x_H = 0.6$? Use the payoff expressions
   $\pi_H(x)$ and $\pi_D(x)$ to justify your answers.
```

```{exercise}
:label: bio_ess_check

A strategy $\sigma^*$ is an **evolutionarily stable strategy (ESS)** if a
population playing $\sigma^*$ cannot be invaded by any rare mutant strategy
$\sigma'$. Formally, $\sigma^*$ is an ESS if for all $\sigma' \neq \sigma^*$:

$$
u(\sigma^*, \sigma^*) > u(\sigma', \sigma^*)
$$

or $u(\sigma^*, \sigma^*) = u(\sigma', \sigma^*)$ and
$u(\sigma^*, \sigma') > u(\sigma', \sigma')$.

For the Hawk–Dove game with $V = 4, C = 10$:

1. Is the pure Hawk strategy ($x = 1$) an ESS? Check whether a Dove
   mutant invades a Hawk population.
2. Is the pure Dove strategy ($x = 0$) an ESS? Check whether a Hawk
   mutant invades a Dove population.
3. Is the mixed strategy $\sigma^* = (x^*, 1 - x^*)$ an ESS?
```

## Programming

### Selection and Frequency Dependence

The following code illustrates the core idea of this chapter: how selection
changes population frequencies over time, and how the strength of selection
determines the speed of change.

```{code-cell} python3
import numpy as np
import matplotlib.pyplot as plt

def selection_trajectory(x0, W_A, W_B, generations):
    """Discrete-generation selection with constant fitnesses."""
    x = x0
    traj = [x]
    for _ in range(generations):
        W_bar = W_A * x + W_B * (1 - x)
        x = W_A * x / W_bar
        traj.append(x)
    return np.array(traj)

fig, axes = plt.subplots(1, 2, figsize=(7, 3))

# Left: multiple starting points, same selection pressure
ax = axes[0]
for x0 in [0.02, 0.1, 0.3, 0.5, 0.7, 0.9]:
    traj = selection_trajectory(x0, W_A=1.08, W_B=1.0, generations=80)
    ax.plot(traj, color="steelblue", alpha=0.65)
ax.set_xlabel("Generation")
ax.set_ylabel("Frequency of type A")
ax.set_title("Selection ($W_A = 1.08 > W_B = 1.0$):\ndifferent starting frequencies")
ax.set_ylim(0, 1)

# Right: same starting point, different selection strengths
ax = axes[1]
for s, label in [(0.01, "$s=0.01$"), (0.05, "$s=0.05$"),
                 (0.15, "$s=0.15$"), (0.4,  "$s=0.40$")]:
    traj = selection_trajectory(0.05, W_A=1 + s, W_B=1.0, generations=150)
    ax.plot(traj, label=label)
ax.set_xlabel("Generation")
ax.set_ylabel("Frequency of type A")
ax.set_title("Effect of selection strength\n(starting from $x_A = 0.05$)")
ax.set_ylim(0, 1)
ax.legend()

plt.tight_layout();
```

Both panels show constant-fitness selection: there is a single stable
outcome (fixation of $A$) regardless of the starting frequency. Stronger
selection reaches fixation faster but the destination is the same.

### Hawk–Dove: Frequency-Dependent Selection

Now consider frequency-dependent fitness. The Hawk–Dove replicator dynamics
show that the stable outcome is an *interior equilibrium*, not fixation.

```{code-cell} python3
from scipy.integrate import solve_ivp

V, C = 4, 10  # resource value, injury cost
x_star = V / C

def hawk_dove(t, y):
    x = y[0]
    pi_H = (V - C) / 2 * x + V * (1 - x)
    pi_D = V / 2 * (1 - x)
    pi_bar = x * pi_H + (1 - x) * pi_D
    return [x * (pi_H - pi_bar)]

t_span = (0, 30)
t_eval = np.linspace(0, 30, 400)

plt.figure(figsize=(7, 4))
for x0 in [0.04, 0.15, 0.35, 0.55, 0.75, 0.94]:
    sol = solve_ivp(hawk_dove, t_span, [x0], t_eval=t_eval)
    plt.plot(sol.t, sol.y[0], color="steelblue", alpha=0.7)

plt.axhline(x_star, color="crimson", linestyle="--",
            label=f"Stable equilibrium $x^* = V/C = {x_star:.2f}$")
plt.xlabel("Time")
plt.ylabel("Frequency of Hawk")
plt.title(f"Hawk–Dove ($V={V}$, $C={C}$): selection converges to $x^*$ from any starting point")
plt.ylim(0, 1)
plt.legend();
```

Compare this to the constant-fitness case above. Here, trajectories from
both sides converge to the same interior point — neither strategy takes
over. This is frequency-dependent selection at work: the advantage of being
a Hawk disappears as Hawks become common, and the advantage of being a Dove
disappears as Doves become common.

## Notable Research

The founding paper of evolutionary game theory is [@smith1973logic], which
introduced the Hawk–Dove game and the concept of an evolutionarily stable
strategy. It was simultaneously a contribution to theoretical biology and a
demonstration that Nash equilibrium analysis could be applied to
non-rational agents. Maynard Smith later developed the theory in full in his
book [@smith1982evolution].

The mathematical link between ESS and the dynamic stability of the replicator
equation was established by [@taylor1978evolutionary]. This paper showed that
evolutionary stability (a static, game-theoretic concept) and asymptotic
stability under selection dynamics (a dynamical systems concept) are, under
broad conditions, equivalent — justifying the use of Nash equilibrium as a
prediction for biological populations.

The broader programme connecting population genetics to game theory, and
showing that many different biological update rules share the same
large-population limit, is surveyed in [@nowak2006evolutionary], which
provides extensive biological examples alongside the mathematical theory.

## Conclusion

Natural selection is not rational deliberation, but it produces outcomes that
look as though it is. The reason is that evolution is a kind of optimisation
— but what it optimises is *reproductive success against the current
population*, not a fixed objective. Whenever reproductive success depends on
what strategies your neighbours use, you have a game. The payoff matrix of
that game is the fitness matrix of the biological population.

The three conditions for natural selection — variation, heritability,
differential reproduction — translate directly into the components of the
mathematical models in the chapters that follow:

- **Variation**: multiple strategies $i = 1, \ldots, m$ coexist.
- **Heritability**: offspring adopt the parent strategy.
- **Differential reproduction**: strategies with $\pi_i > \bar\pi$ increase
  in frequency.

Every result in the evolutionary chapters of this book is a consequence of
applying these three conditions to populations playing games.

[](#tbl:bio_summary) summarises the key concepts introduced in this chapter.

```{table} Summary of biological foundations
:label: tbl:bio_summary
:align: center
:class: table-bordered

| Concept | Description | Connects to |
|---|---|---|
| Natural selection | Differential reproduction of heritable variants | All evolutionary chapters |
| Fitness $W_i$ | Expected reproductive output of type $i$ | Payoff $\pi_i$ in evolutionary game theory |
| Frequency-dependent selection | Fitness depends on population composition | Payoff matrix $M_{ij}$ |
| Hawk–Dove game | Canonical model of animal conflict | Replicator dynamics, ESS |
| Evolutionarily stable strategy | Nash equilibrium robust to rare invasion | Stable fixed points of replicator dynamics |

```

---

```{attention}
The key conceptual move in evolutionary game theory is replacing fixed
fitness constants with frequency-dependent payoffs. Once fitness is a
payoff that depends on interactions, every result from classical game
theory — Nash equilibrium, mixed strategies, evolutionary stability —
becomes a statement about which strategies natural selection will sustain.
```

---

(solutions:evolutionary_biology)=

## Solutions

````{solution} bio_selection_recurrence
:label: solution:bio_selection_recurrence

1. With $W_C = 1.08$, $W_K = 1.0$, and $x_C = 0.2$:

$$
\bar W = W_C x_C + W_K x_K = 1.08 \times 0.2 + 1.0 \times 0.8 = 0.216 + 0.8 = 1.016
$$

$$
x_C' = \frac{W_C \, x_C}{\bar W} = \frac{1.08 \times 0.2}{1.016} = \frac{0.216}{1.016} \approx 0.2126
$$

2. Apply the same recurrence with $x_C = 0.2126$:

$$
\bar W = 1.08 \times 0.2126 + 1.0 \times 0.7874 = 0.2296 + 0.7874 = 1.0170
$$

$$
x_C'' = \frac{1.08 \times 0.2126}{1.0170} \approx \frac{0.2296}{1.0170} \approx 0.2258
$$

3. Selection is pushing the population toward higher frequencies of the cryptic
morph ($x_C$ increasing). Since $W_C > W_K$, the cryptic morph always has
above-average fitness ($W_C > \bar W$ for all $x_C \in (0,1)$), so it increases
every generation. In the forest environment, blending with bark is advantageous —
conspicuous beetles are more likely to be eaten.

4. With $W_C = 0.9$ and $W_K = 1.0$, starting from $x_C = 0.2$:

$$
\bar W = 0.9 \times 0.2 + 1.0 \times 0.8 = 0.18 + 0.8 = 0.98
$$

$$
x_C' = \frac{0.9 \times 0.2}{0.98} = \frac{0.18}{0.98} \approx 0.1837
$$

Now selection pushes *against* the cryptic morph. In this changed environment
(e.g. a cleared forest where the bark background is gone), the conspicuous
morph does better. This illustrates that **the direction of selection depends
entirely on the environment**: the same trait can be advantageous in one
environment and deleterious in another. There is no universally "fitter" type.

```{code-cell} python3
import numpy as np

def selection_step(x, W_A, W_B):
    W_bar = W_A * x + W_B * (1 - x)
    return W_A * x / W_bar

# Forest environment
x = 0.2
print("Forest environment (W_C=1.08, W_K=1.0):")
for gen in range(1, 4):
    x = selection_step(x, 1.08, 1.0)
    print(f"  Generation {gen}: x_C = {x:.4f}")

# Changed environment
x = 0.2
print("\nChanged environment (W_C=0.9, W_K=1.0):")
for gen in range(1, 4):
    x = selection_step(x, 0.9, 1.0)
    print(f"  Generation {gen}: x_C = {x:.4f}")
```
````

````{solution} bio_frequency_dependence_classify
:label: solution:bio_frequency_dependence_classify

1. **Not frequency-dependent.** The plant's improved photosynthesis gives a
   fixed advantage regardless of what other plants are doing. Fitness here is a
   constant property of the genotype, not a function of the population
   composition.

2. **Frequency-dependent.** The protection conferred by mimicry depends on
   how common the toxic model species is in the population. When the model is
   rare, predators have not learned the association, and the mimic gains little
   benefit. The fitness of the mimicry strategy depends on the frequency of
   the toxic model in the broader community — a textbook case of positive
   frequency-dependent selection.

3. **Frequency-dependent.** The payoff to a cooperator in a public goods game
   depends directly on how many others cooperate: more contributors means a
   larger shared benefit. This is the defining structure of a public goods game
   and is a core example of frequency-dependent selection in biology (e.g.
   bacteria secreting shared enzymes).

4. **Not frequency-dependent** (under the stated assumption). If faster
   cheetahs always catch more prey independently of what other cheetahs do,
   fitness is a constant function of speed and does not depend on the
   population composition. In practice, cheetah speed might interact with prey
   evolution (an arms race), but the scenario as stated implies constant fitness.
````

````{solution} bio_hawk_dove_equilibrium
:label: solution:bio_hawk_dove_equilibrium

With $V = 4$ and $C = 10$:

1. The payoff matrix is:

$$
\begin{align*}
M &= \begin{pmatrix}
(V-C)/2 & V \\
0       & V/2
\end{pmatrix} \\
&=
\begin{pmatrix}
-3 & 4 \\
0  & 2
\end{pmatrix}
\end{align*}
$$

where rows/columns are Hawk (H) and Dove (D).

2. The equilibrium frequency is:

$$
x^* = \frac{V}{C} = \frac{4}{10} = 0.4
$$

3. The expected payoff to each strategy in a population with Hawk frequency $x$:

$$
\pi_H(x) = \frac{V-C}{2} \cdot x + V(1-x) = -3x + 4(1-x) = 4 - 7x
$$

$$
\pi_D(x) = 0 \cdot x + \frac{V}{2}(1-x) = 2(1-x)
$$

At $x = x^* = 0.4$:

$$
\pi_H(0.4) = 4 - 7(0.4) = 4 - 2.8 = 1.2
$$

$$
\pi_D(0.4) = 2(1 - 0.4) = 2(0.6) = 1.2
$$

Since $\pi_H(x^*) = \pi_D(x^*) = 1.2$, neither strategy does better than the
other, confirming $x^*$ is a Nash equilibrium: no individual has an incentive
to switch strategy unilaterally.

4. The Hawk frequency is **increasing** from $x_H = 0.1$, because:

$$
\pi_H(0.1) = 4 - 7(0.1) = 3.3 > \pi_D(0.1) = 2(0.9) = 1.8
$$

Hawks do better than Doves, so the Hawk frequency rises toward $x^*$.

The Hawk frequency is **decreasing** from $x_H = 0.6$, because:

$$
\pi_H(0.6) = 4 - 7(0.6) = -0.2 < \pi_D(0.6) = 2(0.4) = 0.8
$$

Doves do better than Hawks, so the Hawk frequency falls back toward $x^*$.
This confirms that $x^* = 0.4$ is a **stable** equilibrium.

```{code-cell} python3
V, C = 4, 10

def pi_H(x): return (V - C) / 2 * x + V * (1 - x)
def pi_D(x): return V / 2 * (1 - x)

x_star = V / C
print(f"Equilibrium frequency x* = V/C = {x_star}")
print(f"pi_H(x*) = {pi_H(x_star):.4f}")
print(f"pi_D(x*) = {pi_D(x_star):.4f}")
print()
print(f"At x=0.1: pi_H = {pi_H(0.1):.2f}, pi_D = {pi_D(0.1):.2f}  -> Hawks increase")
print(f"At x=0.6: pi_H = {pi_H(0.6):.2f}, pi_D = {pi_D(0.6):.2f}  -> Hawks decrease")
```
````

````{solution} bio_ess_check
:label: solution:bio_ess_check

Recall the ESS conditions with $V=4$, $C=10$, and payoff matrix
$M = \begin{pmatrix}-3 & 4 \\ 0 & 2\end{pmatrix}$.

1. **Is pure Hawk ($x=1$) an ESS?**

   Check whether a rare Dove mutant invades: we need $u(H,H) > u(D,H)$.

   $$u(H,H) = M_{HH} = \frac{V-C}{2} = -3$$

   $$u(D,H) = M_{DH} = 0$$

   Since $u(H,H) = -3 < 0 = u(D,H)$, a Dove mutant does **strictly better**
   than a Hawk in an all-Hawk population. The all-Hawk population is therefore
   **not an ESS**: Doves invade successfully. This makes biological sense —
   when everyone is aggressive, avoiding fights is very profitable.

2. **Is pure Dove ($x=0$) an ESS?**

   Check whether a rare Hawk mutant invades: we need $u(D,D) > u(H,D)$.

   $$u(D,D) = M_{DD} = \frac{V}{2} = 2$$

   $$u(H,D) = M_{HD} = V = 4$$

   Since $u(D,D) = 2 < 4 = u(H,D)$, a Hawk mutant does **strictly better**
   than a Dove in an all-Dove population. The all-Dove population is **not an
   ESS**: Hawks invade successfully. When everyone is passive, aggression pays.

3. **Is the mixed strategy $\sigma^* = (0.4, 0.6)$ an ESS?**

   Since $\sigma^*$ is an interior Nash equilibrium, we need to check the
   secondary ESS condition. At $x = x^*$, every strategy (including all
   mutants) gets the same payoff against $\sigma^*$. So the first ESS
   condition holds with equality for all $\sigma'$, and we must check the
   secondary condition:

   $$u(\sigma^*, \sigma') > u(\sigma', \sigma') \quad \text{for all } \sigma' \neq \sigma^*$$

   For a mutant playing Hawk with probability $y$ (so $\sigma' = (y, 1-y)$):

   $$
   u(\sigma^*, \sigma') = x^* \cdot u(H,\sigma') + (1-x^*) \cdot u(D,\sigma')
   $$

   Since $u(H,\sigma') = u(D,\sigma')$ at $x^*$ (both equal $V/2 \cdot (1-y) + ...$,
   actually let us compute directly):

   $$u(H,\sigma') = -3y + 4(1-y) = 4 - 7y$$
   $$u(D,\sigma') = 0 \cdot y + 2(1-y) = 2 - 2y$$

   $$u(\sigma^*, \sigma') = 0.4(4-7y) + 0.6(2-2y) = 1.6 - 2.8y + 1.2 - 1.2y = 2.8 - 4y$$

   $$u(\sigma', \sigma') = y(4-7y) + (1-y)(2-2y) = 4y - 7y^2 + 2 - 4y + 2y^2 = 2 - 5y^2$$

   The secondary condition requires $u(\sigma^*, \sigma') > u(\sigma', \sigma')$:

   $$2.8 - 4y > 2 - 5y^2$$
   $$5y^2 - 4y + 0.8 > 0$$
   $$5(y - 0.4)^2 > 0$$

   This holds for all $y \neq 0.4 = x^*$. Therefore $\sigma^* = (0.4, 0.6)$
   **is an ESS**. The mixed-strategy equilibrium is the unique evolutionarily
   stable outcome of the Hawk-Dove game.

```{code-cell} python3
import sympy as sym

y = sym.Symbol("y")
V, C = 4, 10
x_star = sym.Rational(V, C)

u_H_sigma_prime = (V - C) / 2 * y + V * (1 - y)
u_D_sigma_prime = sym.Rational(V, 2) * (1 - y)

u_star_sigma_prime = x_star * u_H_sigma_prime + (1 - x_star) * u_D_sigma_prime
u_prime_sigma_prime = y * u_H_sigma_prime + (1 - y) * u_D_sigma_prime

diff = sym.expand(u_star_sigma_prime - u_prime_sigma_prime)
print("u(σ*, σ') - u(σ', σ') =", diff)
print("Factored:", sym.factor(diff))
```
````
