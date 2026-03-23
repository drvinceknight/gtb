---
kernelspec:
  name: python3
  display_name: "Python 3"
numbering:
  enumerator: A1.%s
---

(app:evolutionary_biology)=

# Appendix: Biological Foundations of Evolutionary Dynamics

(sec:motivating_example_foraging)=

## Motivating Example: Foraging Strategies

Consider a large population of birds feeding in a meadow. Each bird uses
one of two foraging strategies:

- **Aggressive (H)**: compete directly for the richest food patches, risking
  injury in confrontations with other aggressive birds.
- **Passive (D)**: avoid conflict, feed on less contested patches, and
  retreat when challenged.

Each spring, chicks inherit their parents' strategy (with occasional
errors — mutations). By autumn, the number of surviving offspring a bird
raises depends on how well it fed — and feeding success depends not only on
a bird's own strategy but on **how many other birds around it are
aggressive or passive**.

Three observations stand out:

1. **Variation exists**: some birds are aggressive, others passive.
2. **Traits are heritable**: strategy tends to pass from parent to offspring.
3. **Reproduction is differential**: aggressive birds thrive when rare
   (uncontested patches everywhere) but fare poorly when common (constant
   costly fights). Passive birds do steadily regardless.

These three conditions — variation, heritability, differential reproduction
— are precisely **Darwin's conditions for evolution by natural selection**.
The frequency-dependent aspect, where a strategy's success depends on what
others are doing, is what makes this a problem for **evolutionary game
theory**.

This appendix provides the biological foundation for the evolutionary
dynamics studied in [Replicator Dynamics](#chp:replicator_dynamics),
[Moran Process](#chp:moran_process), and
[Learning and Evolutionary Dynamics](#chp:further_learning_dynamics).

## Theory

### Definition: Natural Selection

---

A population evolves by **natural selection** when the following three
conditions hold:

1. **Variation**: individuals in the population differ in some heritable
   trait.
2. **Heritability**: offspring resemble their parents more than they
   resemble random members of the population.
3. **Differential reproduction**: individuals with different trait values
   leave different numbers of offspring on average.

---

When these conditions hold, the composition of the population changes over
time: traits associated with higher reproductive success become more common.
This is not a directed process — there is no goal or foresight — it is a
consequence of arithmetic applied to heritable variation.

#### Example: Selection on a Binary Trait

Suppose a population consists of two types, $A$ and $B$, with population
counts $n_A$ and $n_B$ and total size $N = n_A + n_B$. In each generation,
type $A$ individuals produce on average $W_A$ offspring and type $B$
individuals produce $W_B$ offspring (both $> 0$). After one generation of
selection (no mutation, no drift):

$$
n_A' = W_A\, n_A \qquad n_B' = W_B\, n_B
$$

The frequency of $A$ in the next generation is:

$$
\begin{align*}
x_A' &= \frac{W_A\, n_A}{W_A\, n_A + W_B\, n_B} \\
&= \frac{W_A\, x_A}{W_A\, x_A + W_B\, x_B} \\
&= \frac{W_A}{\bar W}\, x_A
\end{align*}
$$

where $\bar W = W_A x_A + W_B x_B$ is the **mean fitness** of the
population. Type $A$ increases in frequency whenever $W_A > \bar W$, i.e.,
whenever its fitness exceeds the population average.

### Definition: Fitness

---

The **absolute fitness** $W_i$ of type $i$ is the expected number of
offspring an individual of type $i$ produces in one generation.

The **relative fitness** $w_i$ is defined as:

$$
w_i = \frac{W_i}{\bar{W}}, \qquad \bar{W} = \sum_j x_j W_j
$$

In continuous time, the **Malthusian fitness** (or intrinsic growth rate)
$r_i$ satisfies $n_i(t) = n_i(0)\,e^{r_i t}$ in the absence of
competition.

---

```{note}
In evolutionary game theory, the fitness of type $i$ is typically defined
as a function of the population composition:
$W_i = W_i(x_1, x_2, \ldots)$.
When fitness is constant (independent of frequencies), selection simply
drives the highest-fitness type to fixation. When fitness depends on
frequencies, the outcome can be a stable polymorphism — this is
**frequency-dependent selection**, covered below.
```

#### Example: Relative Fitness and the Selection Coefficient

Suppose type $A$ has absolute fitness $W_A = 1 + s$ and type $B$ has
$W_B = 1$, where $s > 0$ is the **selection coefficient**. Then:

$$
\bar{W} = (1+s)x_A + x_B = 1 + s x_A
$$

$$
x_A' = \frac{(1+s)\,x_A}{1 + s x_A}
$$

For small $s$ and small $x_A$, the change per generation is approximately:

$$
\Delta x_A \approx s\,x_A(1 - x_A)
$$

This is the discrete-generation analogue of the replicator equation
$\dot x_A = x_A(\pi_A - \bar\pi)$, with $s$ playing the role of the fitness
advantage $\pi_A - \bar\pi$.

### Theorem: Fisher's Fundamental Theorem of Natural Selection

---

The rate of increase in mean fitness of a population equals the
**additive genetic variance** in fitness:

$$
\frac{d\bar{W}}{dt} = \mathrm{Var}(W)
$$

---

#### Proof sketch

In the discrete one-generation model with two types:

$$
\begin{align*}
\bar{W}' - \bar{W} \\
&= \sum_i x_i' W_i - \bar{W} \\
&= \sum_i \frac{W_i x_i}{\bar{W}} W_i - \bar{W} \\
&= \frac{\sum_i W_i^2 x_i}{\bar{W}} - \bar{W} \\
&= \frac{\mathbb{E}[W^2] - \bar{W}^2}{\bar{W}} \\
&= \frac{\mathrm{Var}(W)}{\bar{W}}
\end{align*}
$$

For $\bar W \approx 1$ (weak selection), this is approximately
$\mathrm{Var}(W) \geq 0$.

```{important}
Fisher's theorem implies that mean fitness never decreases under selection
alone — selection always exploits existing variation. However, mutation
and frequency-dependent selection can both reduce mean fitness, so the
theorem applies strictly only to selection acting on fixed fitness values.
```

### Definition: Mutation

---

A **mutation** is a heritable change in strategy or genotype that occurs
with probability $\mu$ per replication event, independently of selection.

In a two-type model, type $A$ mutates to type $B$ at rate $\mu_{AB}$ and
type $B$ mutates to type $A$ at rate $\mu_{BA}$ per generation. The
expected frequency of $A$ after one generation of selection and mutation
is:

$$
x_A' = (1 - \mu_{AB})\,\frac{W_A}{\bar W}\,x_A
+ \mu_{BA}\,\frac{W_B}{\bar W}\,x_B
$$

---

#### Example: Mutation–Selection Balance

At equilibrium ($x_A' = x_A = \hat x_A$), selection favouring $A$ is
balanced by mutation away from $A$. For small mutation rates and strong
selection ($W_A = 1+s$, $W_B = 1$, $\mu_{AB} = \mu$, $\mu_{BA} \approx 0$):

$$
\hat x_B \approx \frac{\mu}{s}
$$

This is the classical **mutation–selection balance**: even a strongly
deleterious type is maintained in the population at a low frequency
determined by the ratio of mutation rate to selection coefficient. This
result has direct applications in modelling the persistence of
suboptimal strategies under evolutionary dynamics.

### Definition: Genetic Drift

---

**Genetic drift** refers to random fluctuations in allele or strategy
frequencies that arise from the finite size of a population. Even when
a type has higher fitness, it may be lost by chance in a small population.

In a population of size $N$, the **variance** introduced by random
sampling in one generation is:

$$
\mathrm{Var}(\Delta x) = \frac{x(1-x)}{N}
$$

Drift is negligible when $N$ is large but dominates selection when
$Ns \ll 1$, i.e., when the selection coefficient $s$ is smaller than
$1/N$.

---

The competition between drift and selection is captured by the condition:

- $Ns \gg 1$: selection dominates; the fitter type nearly always fixes.
- $Ns \ll 1$: drift dominates; fixation is essentially random.
- $Ns \approx 1$: the transition regime where both matter.

```{note}
The **Moran process** (Chapter @chp:moran_process) and the
**Wright–Fisher process**
(Chapter @chp:further_learning_dynamics) are the two standard finite-population
models that formalise genetic drift. The fixation probability formula
$\rho_1$ in the Moran process quantifies precisely how selection and drift
trade off in a population of size $N$.
```

#### Example: Fixation Probability under Drift and Selection

Under the Moran process with two types and selection coefficient $s$
(so $W_A = 1+s$, $W_B = 1$), the fixation probability of a single $A$
mutant in a population of $N$ is:

$$
\rho_1 = \frac{1 - (1+s)^{-1}}{1 - (1+s)^{-N}}
$$

For neutral drift ($s = 0$) this gives $\rho_1 = 1/N$ — fixation is
purely a matter of chance. For strong positive selection ($s \gg 1/N$),
$\rho_1 \approx s$, recovering the deterministic prediction. For weak
selection ($s \ll 1$, $sN$ moderate), $\rho_1 \approx s / (1 - e^{-sN})$,
showing the interplay between both forces.

### Definition: Frequency-Dependent Selection

---

Selection is **frequency-dependent** when the fitness of a type depends on
the current composition of the population, not just on its own properties
in isolation.

Formally, $W_i = W_i(x_1, x_2, \ldots, x_m)$ where $x_j$ is the frequency
of type $j$.

---

Frequency dependence arises whenever individuals interact — which is
essentially always in real populations. The foraging example from the
motivating example is a canonical instance:

| Population composition | $W_H$ | $W_D$ |
|---|---|---|
| All passive ($x_H = 0$) | Very high (no competition) | Moderate |
| Mixed ($x_H = 0.5$) | Moderate | Moderate |
| All aggressive ($x_H = 1$) | Low (constant fighting) | — |

When $W_H > W_D$ at low $x_H$ but $W_H < W_D$ at high $x_H$, there is a
stable interior equilibrium — a **polymorphism** — where both strategies
persist. This is the defining feature of **negative frequency-dependent
selection** and underlies much of the biological diversity we observe.

#### Example: The Hawk–Dove Game

The foraging scenario above is formalised by the **Hawk–Dove game**
[@smith1973logic], with payoff matrix:

$$
M = \begin{pmatrix}
(V - C)/2 & V \\
0          & V/2
\end{pmatrix}
$$

where $V > 0$ is the value of the resource and $C > V$ is the cost of
injury ($H$ = Hawk/Aggressive, $D$ = Dove/Passive). The fitness of a
Hawk in a population with Hawk frequency $x$ is:

$$
\begin{align*}
\pi_H(x) &= \frac{V-C}{2}\cdot x + V\cdot(1-x) \\
&= V - x\cdot\frac{V+C}{2}
\end{align*}
$$

and the fitness of a Dove is:

$$
\pi_D(x) = 0 \cdot x + \frac{V}{2}(1-x) = \frac{V(1-x)}{2}
$$

Setting $\pi_H = \pi_D$ gives the interior equilibrium:

$$
x^* = \frac{V}{C}
$$

For $C > V$ this is a valid frequency, and it is the unique stable
equilibrium of the replicator dynamics — both strategies coexist at this
ratio.

### Definition: Evolutionary Stable Strategy

---

A strategy $\sigma^*$ is an **evolutionarily stable strategy (ESS)** if
a population playing $\sigma^*$ cannot be invaded by any small group of
mutants playing a different strategy $\sigma'$ [@smith1973logic].

Formally, $\sigma^*$ is an ESS if for all $\sigma' \neq \sigma^*$:

$$
u(\sigma^*, \sigma^*) > u(\sigma', \sigma^*)
$$

or

$$
u(\sigma^*, \sigma^*) = u(\sigma', \sigma^*)
\;\text{ and }\;
u(\sigma^*, \sigma') > u(\sigma', \sigma')
$$

---

The ESS concept connects directly to Nash equilibrium: every ESS is a Nash
equilibrium of the underlying stage game, but not every Nash equilibrium
is an ESS. The additional stability condition rules out neutral equilibria
that would be destabilised by drift.

### From Natural Selection to Evolutionary Game Theory

The key conceptual step from classical population genetics to evolutionary
game theory is recognising that **fitness is a payoff**.

In classical genetics, fitness is a fixed property of a genotype — a
constant $W_i$. In evolutionary game theory, fitness arises from
**interactions between individuals**: if two individuals are paired and
play a game, the payoff they receive is their fitness contribution for
that encounter.

When individuals interact pairwise and are drawn uniformly from the
population, the expected fitness of type $i$ in a population with frequency
vector $x = (x_1, \ldots, x_m)$ is:

$$
\pi_i(x) = \sum_j x_j M_{ij}
$$

where $M_{ij}$ is the payoff to type $i$ when facing type $j$. This is
precisely the fitness function used in the
[Replicator Dynamics chapter](#chp:replicator_dynamics). The payoff
matrix $M$ **is** the fitness matrix; evolutionary game theory is
population genetics with frequency-dependent fitness defined by strategic
interaction.

```{table} Correspondence between genetics and evolutionary game theory
:label: tbl:genetics_egt_correspondence
:align: center
:class: table-bordered

| Genetics concept | Game theory concept |
|---|---|
| Genotype / allele | Strategy |
| Absolute fitness $W_i$ | Expected payoff $\pi_i$ |
| Selection coefficient $s$ | Fitness advantage $\pi_i - \bar\pi$ |
| Frequency-dependent fitness | Payoff matrix entry $M_{ij}$ |
| Mutation rate $\mu$ | Exploration / trembling hand |
| Population size $N$ | Determines drift vs selection balance |
| Genetic drift | Stochastic fluctuations in finite-population models |
| ESS | Strict Nash equilibrium that is also uninvadable |

```

## Exercises

```{exercise}
:label: selection_on_two_types

A population of bacteria has two resistance genotypes: sensitive ($S$) and
resistant ($R$). In the absence of antibiotics, $W_S = 1.05$ and $W_R = 1.0$
(resistance carries a fitness cost). In the presence of antibiotics,
$W_S = 0.3$ and $W_R = 1.0$.

1. Compute the frequency of $R$ after one generation, starting from
   $x_R = 0.01$, under each environment.
2. How many generations does it take for $x_R$ to exceed $0.5$ in the
   antibiotic environment? (Set up the recurrence and solve numerically.)
3. Compute the mutation–selection balance frequency $\hat x_S$ in the
   antibiotic environment, assuming $\mu_{RS} = 10^{-5}$ (resistance
   occasionally reverts to sensitivity).
```

```{exercise}
:label: drift_vs_selection

Consider a Moran process with two types, $A$ (fitness $1+s$) and $B$
(fitness $1$), in a population of size $N$.

1. For $N = 10$, plot the fixation probability $\rho_1$ of a single $A$
   mutant as a function of $s \in [-0.5, 0.5]$.
2. At what value of $s$ is $\rho_1 = 1/N$ (the neutral drift value)?
3. For what population sizes $N$ does a $1\%$ fitness advantage ($s=0.01$)
   give a fixation probability greater than $0.5$?
```

```{exercise}
:label: hawk_dove_equilibrium

For the Hawk–Dove game with $V = 2$ and $C = 6$:

1. Compute the equilibrium frequency $x^*$.
2. Verify that $x^*$ is a Nash equilibrium of the stage game.
3. Verify that the mixed strategy $\sigma^* = (x^*, 1-x^*)$ is an ESS.
4. Starting from $x_H = 0.1$, trace the replicator dynamics trajectory
   toward equilibrium (numerically or by solving the ODE).
```

```{exercise}
:label: frequency_dependence_check

For each of the following scenarios, state whether fitness is
frequency-dependent and briefly justify:

1. A plant that photosynthesize more efficiently has higher fitness
   regardless of the plant community around it.
2. A fish that mimics the appearance of a toxic species is protected by
   predators, but only while the toxic species remains common enough for
   predators to have learned the association.
3. In a public goods game, a contributor's benefit depends on how many
   others also contribute.
4. A faster cheetah always catches more prey, independent of what other
   cheetahs are doing.
```

## Programming

### Simulating Selection and Drift

The following simulates the Wright–Fisher model with selection, tracking
how frequencies change over many generations for different population
sizes.

```{code-cell} python3
import numpy as np
import matplotlib.pyplot as plt

def wright_fisher(x0, s, N, generations, rng):
    """
    Wright-Fisher model with selection coefficient s, population N.
    x0: initial frequency of type A.
    Returns array of frequencies over time.
    """
    x = x0
    trajectory = [x]
    for _ in range(generations):
        if x == 0 or x == 1:
            trajectory.append(x)
            continue
        W_bar = (1 + s) * x + 1 * (1 - x)
        p = (1 + s) * x / W_bar          # probability of sampling A
        count = rng.binomial(N, p)
        x = count / N
        trajectory.append(x)
    return np.array(trajectory)

rng = np.random.default_rng(seed=0)
generations = 200
x0 = 0.1
s = 0.05

fig, axes = plt.subplots(1, 3, figsize=(12, 4), sharey=True)
for ax, N in zip(axes, [10, 100, 1000]):
    for _ in range(20):
        traj = wright_fisher(x0, s, N, generations, rng)
        ax.plot(traj, alpha=0.4, linewidth=0.8)
    ax.set_title(f"N = {N}")
    ax.set_xlabel("Generation")
    ax.set_ylim(0, 1)

axes[0].set_ylabel("Frequency of A")
fig.suptitle(f"Wright–Fisher: selection s={s}, drift decreases as N grows")
plt.tight_layout();
```

### Mutation–Selection Dynamics

```{code-cell} python3
def mutation_selection(x0, W_A, W_B, mu_AB, mu_BA, generations):
    """One-locus mutation-selection model (deterministic)."""
    x = x0
    trajectory = [x]
    for _ in range(generations):
        W_bar = W_A * x + W_B * (1 - x)
        x_sel = W_A * x / W_bar           # after selection
        x_new = (1 - mu_AB) * x_sel + mu_BA * (1 - x_sel)  # after mutation
        x = x_new
        trajectory.append(x)
    return np.array(trajectory)

gens = 300
traj_no_mut  = mutation_selection(0.01, 1.05, 1.0, 0,      0,      gens)
traj_with_mut = mutation_selection(0.01, 1.05, 1.0, 0.002,  0.0001, gens)

plt.figure()
plt.plot(traj_no_mut,   label="No mutation")
plt.plot(traj_with_mut, label="With mutation ($\\mu=0.002$)")
plt.xlabel("Generation")
plt.ylabel("Frequency of A")
plt.title("Mutation–selection dynamics")
plt.legend()
plt.ylim(0, 1);
```

### Hawk–Dove Replicator Dynamics

```{code-cell} python3
from scipy.integrate import solve_ivp

V, C = 2, 6

def hawk_dove_replicator(t, y):
    x = y[0]
    pi_H = (V - C) / 2 * x + V * (1 - x)
    pi_D = V / 2 * (1 - x)
    pi_bar = x * pi_H + (1 - x) * pi_D
    return [x * (pi_H - pi_bar)]

x_star = V / C
t_span = (0, 30)
t_eval = np.linspace(*t_span, 300)

plt.figure()
for x0 in [0.05, 0.2, 0.5, 0.8, 0.95]:
    sol = solve_ivp(hawk_dove_replicator, t_span, [x0], t_eval=t_eval)
    plt.plot(sol.t, sol.y[0], label=f"$x_0={x0}$")

plt.axhline(x_star, color="black", linestyle="--", label=f"$x^*={x_star:.2f}$")
plt.xlabel("Time")
plt.ylabel("Frequency of Hawk")
plt.title("Hawk–Dove replicator dynamics")
plt.legend(loc="right")
plt.ylim(0, 1);
```

## Notable Research

The mathematical study of natural selection began with the foundational
work of Fisher [@Fisher1930], Haldane [@Haldane1927; @Haldane1932], and
Wright [@Wright1931], who together established the Modern Synthesis —
reconciling Darwinian selection with Mendelian genetics. Fisher's
fundamental theorem and Wright's adaptive landscape concept remain central
organising ideas.

The application of game theory to biology was initiated by
[@smith1973logic], who introduced the concept of an evolutionarily stable
strategy (ESS) to explain why animal conflict so rarely escalates to
serious injury. This paper is widely regarded as the birth of evolutionary
game theory.

The connection between ESS and the replicator dynamics was established by
[@taylor1978evolutionary], who showed that ESS corresponds to asymptotically
stable fixed points of the replicator equation. This link between static
stability (ESS) and dynamic stability (replicator) is the foundation of
the evolutionary dynamics chapters in this book.

The modern synthesis of evolutionary game theory in finite populations —
incorporating drift, mutation, and frequency-dependent selection in a
unified framework — is surveyed in [@nowak2004evolutionary] and treated in
depth in [@nowak2006evolutionary].

## Conclusion

This appendix introduced the biological mechanisms — selection, mutation,
and drift — that underlie the mathematical models developed in the
evolutionary dynamics chapters of this book. The key conceptual bridge is
that **fitness is a payoff**: in a population of interacting individuals,
the reproductive success of a strategy depends on what strategies it
encounters, and the payoff matrix captures this dependency precisely.

The replicator equation, the Moran process, and the imitation, introspection,
and Wright–Fisher dynamics are all formal models of the three-condition
Darwinian process: variation (multiple strategies exist), heritability
(offspring adopt the parent strategy), and differential reproduction (fitness
drives frequency change). Understanding which biological assumptions justify
which mathematical model — and when finite-population effects, mutation, or
frequency dependence matter — equips the reader to apply evolutionary game
theory to real biological, social, and economic systems.

[](#tbl:biology_summary) summarises the key concepts.

```{table} Summary of biological foundations
:label: tbl:biology_summary
:align: center
:class: table-bordered

| Concept | Definition | Game-theoretic role |
|---|---|---|
| Natural selection | Differential reproduction of heritable variants | Drives frequency change toward higher-fitness strategies |
| Absolute fitness $W_i$ | Expected number of offspring | Payoff $\pi_i$ in evolutionary game theory |
| Relative fitness $w_i$ | Fitness relative to population mean | Determines direction of selection |
| Selection coefficient $s$ | Fitness advantage of a type | $\pi_i - \bar\pi$ in the replicator equation |
| Fisher's Fundamental Theorem | Mean fitness increases at rate $\mathrm{Var}(W)$ | Selection always exploits existing variation |
| Mutation | Heritable change at rate $\mu$ | Maintains variation; prevents fixation |
| Mutation–selection balance | Equilibrium $\hat x \approx \mu/s$ | Source of persistent suboptimal strategies |
| Genetic drift | Random frequency change in finite populations | Modelled by Moran and Wright–Fisher processes |
| Frequency-dependent selection | Fitness depends on population composition | Payoff matrix $M_{ij}$ defines fitness |
| Evolutionarily stable strategy | Nash equilibrium robust to invasion | Connects static game theory to dynamic stability |

```

---

```{attention}
The three mechanisms of evolution — selection, mutation, and drift — are
not alternatives but complementary forces that act simultaneously.
Selection exploits variation, mutation replenishes it, and drift
introduces randomness that can fix even suboptimal strategies in small
populations. The interplay of all three is what makes evolutionary
dynamics rich — and what makes game theory essential for understanding it.
```
