---
kernelspec:
  name: python3
  display_name: "Python 3"
---

(chp:moran_process)=

# Moran Process

In finite populations, random drift can overturn selection: a rare mutant
strategy may take hold by chance even if it offers no advantage. This chapter
introduces the Moran process to study such fixation events, analysing the
probability that a single mutant takes over or disappears.

(sec:motivating_example_preprint)=

## Motivating Example: Everyone’s citing the preprint

In a graduate student reading group, everyone cites a well-established
textbook in their essays. One student, though, starts citing a
**recent preprint** they found on arXiv.

> "It’s got a better proof of the key result, and it’s open access."

Each week:

- A student is admired for their choice of citation (fitness ∝ novelty,
  clarity, or style).
- Another student, chosen at random, updates their references to match.

Over time, the group begins to shift its citation culture. The **preprint
might become canonical**, or the students might return to citing the
traditional text.

The more students who cite the preprint, the more attractive it becomes to
others: shared references lead to easier discussion, common assumptions, and
social reinforcement. In this way, the **fitness** of citing the preprint is
not fixed; it **depends on the current citation habits** of the group. This
makes the process **frequency-dependent**, just as in evolutionary game
dynamics where payoffs arise from interaction with others.

To model this interaction explicitly, consider the following symmetric game.
Each player chooses whether to cite the **textbook** ($T$) or the
**preprint** ($P$). The row and column player payoffs are given by:

$$
M_r = \begin{pmatrix}
3 & 0 \\
1 & 2
\end{pmatrix}
\qquad
M_c = \begin{pmatrix}
3 & 1 \\
0 & 2
\end{pmatrix}
$$

If both students cite the textbook, they align well and receive the highest
payoff of 3. If both cite the preprint, they still coordinate and get a
payoff of 2, slightly lower, but still beneficial.

If one cites the textbook while the other cites the preprint, there is a
mismatch: the **preprint-citer** still gets some benefit (payoff 1) from its
clarity and openness, but the textbook-citer gains nothing (payoff 0) from
the mismatch.

Note here that the group is small and so the infinite population assumption of
[](#chp:replicator_dynamics) does not apply: the topic of this chapter is the
Moran Process a model suited for exactly this purpose.

```{note}
The Moran process was originally developed in population genetics to model
**genetic drift**, the random fluctuation of gene frequencies in small
biological populations. For the biological context and the relationship
between drift and selection, see [Chapter @chp:evolutionary_biology].
```

## Theory

### Definition: Moran Process

First defined in [@moran1958random], the Moran process assumes a constant population of
$N$ individuals which can be of $m$ different types. There exists a fitness
function $f: \{1, \dots, m\} \times \{1, \dots, m\}^N \to \mathbb{R}$ that maps
each individual to a numeric fitness value which is dependent on the types of
the individuals in the population.

The process is defined as follows. At each step:

1. Every individual $k$ has their fitness $f_k$ calculated.
2. An individual is randomly selected for copying. This selection is done
   proportional to their fitness $f_k(v)$. Thus, the probability of selecting
   individual $k$ for copying is given by:

   $$
   \frac{f_k(v)}{\sum_{h=1}^N f_h(v)}
   $$

3. An individual is selected for removal. This selection is done uniformly
   at random. Thus, the probability of selecting individual $i$ for removal
   is:

   $$
   \frac{1}{N}
   $$

4. An individual of the same type as the individual selected for copying is
   introduced to the population.
5. The individual selected for removal is removed.

The process is repeated until there is only one type of individual left in the
population.

---

A common representation of the fitness function $f$ is to use a game.
In this setting, the fitness of an individual of type $i$ is:

$$f_i(v) = (v_{i} - 1)A_{ii} + \sum_{j\ne i, j=1}^{N}v_jA_{ij}$$

#### Example: Selection Probabilities for citation behaviour.

For the [](#sec:motivating_example_preprint) let us consider the situation with
$N$ individuals in the reading group: 3 cite the text book ($T$) and 1 cites the
preprint ($P$). This gives a total number of 5 different populations.
[](#tbl:selection_probabilities) gives the different selection probabilities for
each population.

```{table} Selection probabilities for citation behaviour
:name: tbl:selection_probabilities
:align: center

| $(v_T, v_P)$ | $f_T$                       | $f_P$                       | Prob copy $T$                                           | Prob copy $P$        | Prob remove $T$  | Prob remove $P$  |
|--------------|-----------------------------|-----------------------------|---------------------------------------------------------|----------------------|------------------|------------------|
| $(4, 0)$     | $3 \cdot 3 = 9$             | –                           | $1$                                                     | $0$                  | $1$              | $0$              |
| $(3, 1)$     | $2 \cdot 3 + 1 \cdot 0 = 6$ | $3 \cdot 1 + 0 \cdot 2 = 3$ | $\frac{3 \cdot 6}{3 \cdot 6 + 1 \cdot 3} = \frac{6}{7}$ | $\frac{1}{7}$        | $\frac{3}{4}$    | $\frac{1}{4}$    |
| $(2, 2)$     | $1 \cdot 3 + 2 \cdot 0 = 3$ | $2 \cdot 1 + 1 \cdot 2 = 4$ | $\frac{2 \cdot 3}{2 \cdot 3 + 2 \cdot 4} = \frac{3}{7}$ | $\frac{4}{7}$        | $\frac{1}{2}$    | $\frac{1}{2}$    |
| $(1, 3)$     | $0 \cdot 3 + 3 \cdot 0 = 0$ | $1 \cdot 1 + 2 \cdot 2 = 5$ | $\frac{1 \cdot 0}{1 \cdot 0 + 3 \cdot 5} = 0$           | $1$                  | $\frac{1}{4}$    | $\frac{3}{4}$    |
| $(0, 4)$     | –                           | $0 \cdot 1 + 3 \cdot 2 = 6$ | $0$                                                     | $1$                  | $0$              | $1$              |
```

(sec:definition_of_fixation_probability)=

### Definition: The Fixation Probability

---

The fixation probability of a given type in a Moran process is the probability
that the population eventually becomes composed entirely of individuals of that type.

---

In the case of a finite population of size $N$ with **two** types: a resident type and a mutant type.
Suppose the process begins with $i$ individuals of the mutant type and $N - i$ residents.

Let $\rho_i$ denote the fixation probability of the mutant type starting from $i$ individuals. Then:

- $\rho_0 = 0$, since no mutants exist.
- $\rho_N = 1$, since all individuals are mutants.
- For $0 < i < N$, $\rho_i$ gives the probability that the mutant type eventually fixates
  (i.e., reaches frequency $N$), assuming the dynamics follow the Moran process.

In practice fixation probabilities correspond to absorption probabilities
of an underlying [absorbing Markov chain](#app:absorbing_markov_chain).

Then, the transition probabilities for the underling Markov chain are:

$$
P_{i \to i+1} = (\text{Prob copy mutant})\cdot (\text{Prob remove resident})
$$

and

$$
P_{i \to i-1} = (\text{Prob copy resident})\cdot (\text{Prob remove mutant})
$$

Finally:

$$
\label{eqn:probabilities_of_no_change_in_moran_process}
P_{i \to i} = 1 - P_{i \to i+1} - P_{i \to i-1}
$$

(sec:example_fixation_of_citation_behaviour_as_an_absorbing_markov_chain)=

#### Example: Fixation of citation behaviour as an absorbing Markov chain

For given $N$ the [](#sec:motivating_example_preprint) the underlying absorbing Markov
chain has a state space that can be indexed by $i$ the number of individuals
that cite the preprint.

For $N=4$, we can write down the probability of going from state $i$ to state $j$: $p_{ij}$
using [](#tbl:selection_probabilities):

$$
\begin{align*}
P &= \begin{pmatrix}
1     &  0   &  0  &   0  &   0  \\
(6/7)\cdot(1/4)     &  P_{11}   &  (1/7)\cdot(3/4)  &   0  &   0  \\
0     &  (3/7)\cdot(1/2)   &  P_{22}  &   (4/7)\cdot(1/2)  &   0  \\
0     &  0   &   0\cdot(3/4) &   P_{33}  &   (1)\cdot(1/4)  \\
0     &  0   &  0  &   0  &   1  \\
\end{pmatrix}&&\text{ using the selection probabilities}\\
&= \begin{pmatrix}
1     &  0   &  0  &   0  &   0  \\
3/14     &  19/28   &  3/28  &   0  &   0  \\
0     &  3/14   & 1/2  &   2/7  &   0  \\
0     &  0   &  0  &   3/4  &   1/4  \\
0     &  0   &  0  &   0  &   1  \\
\end{pmatrix}&&
\text{ using } P_{i \to i} = 1 - P_{i \to i+1} - P_{i \to i-1}
\end{align*}
$$

This is an [absorbing Markov chain](#app:absorbing_markov_chain) which, by reordering of states, we can write in the canonical form:

$$
P =
\begin{pmatrix}
    Q & R\\
    0 & I
\end{pmatrix}
$$

with:

$$
Q = \begin{pmatrix}
   19/28   &  3/28  &   0 \\
 3/14   & 1/2  &   2/7  \\
 0   &  0  &   3/4  \\
    \end{pmatrix}
$$

and

$$
R = \begin{pmatrix}
3/14 & 0\\
0 & 0\\
0 & 1/4
\end{pmatrix}
$$

thus we can calculate the [fundamental matrix](#sec:definition_of_fundamental_matrix):

$$
\begin{align*}
N &= \begin{pmatrix}
   9/28   &  -3/28  &   0 \\
 -3/14   & 1/2  &   -2/7  \\
 0   &  0  &   1/4  \\
    \end{pmatrix} ^ {-1}\\
& = \begin{pmatrix}
98/27 & 7/9 & 8/9\\14/9 & 7/3 & 8/3\\0 & 0 & 4
\end{pmatrix}
\end{align*}
$$

We omit the calculation of the inverse which can be obtained using [Gauss-Jordan
elimination](#sec:gauss_jordan) or any other approach.

We can now compute the [absorption probability matrix](#sec:definition_of_absorption_probability_matrix):

$$
B = N R =
\begin{pmatrix}
7/9 & 2/9\\ 1/3 & 2/3\\0 & 1
\end{pmatrix}
$$

Thus if a single mutant, or in our case a single individual starts citing the pre
print: there is $2/9$ chance that the entire reading group starts citing the
pre print over time.

$$
\rho_1 = \frac{2}{9}
$$

### Theorem: The fixation probabilities in populations of two types

---

Given a Moran process in a population with two types as defined in [](#sec:definition_of_fixation_probability),
the fixation probability $\rho_i$ is given by:

$$
\label{eqn:formula_for_fixation_probabilities}
\rho_i=\frac{1+\sum_{j=1}^{i-1}\prod_{k=1}^j\gamma_k}{1+\sum_{j=1}^{N-1}\prod_{k=1}^j\gamma_k}
$$

where:

$$
\gamma_k = \frac{f_R(k)}{f_M(k)}
$$

---

**Proof**:

---

For the underlying absorbing Markov chain we have:

$$
\begin{align*}
    p_{i,i+1}\rho_{i+1} & = -p_{i,i-1}\rho_{i-1} + \rho_i(1 - p_{ii}) \\
    p_{i,i+1}\rho_{i+1} & = p_{i,i-1}(\rho_{i} - \rho_{i-1}) + \rho_ip_{i,i+1} \\
    \rho_{i+1} - \rho_i    & = \frac{p_{i, i-1}}{p_{i, i+1}}(\rho_i-\rho_{i-1})=\gamma_i(\rho_i-\rho_{i-1})
\end{align*}
$$

with:

$$
\begin{align*}
    \gamma_i &= \frac{p_{i, i - 1}}{p_{i, i + 1}}\\
             &= \frac{\frac{(N - i)f_R(i)}{if_M(i) + (N - i)f_R(i)}\frac{i}{N}}{\frac{if_M(i)}{if_M(i) + (N - i)f_R(i)}\frac{N-i}{N}}\\
             &= \frac{(N - i)f_R(i)}{if_M(i) + (N - i)f_R(i)}\frac{i}{N}{\frac{if_M(i) + (N - i)f_R(i)}{if_M(i)}\frac{N}{N-i}}\\
             &= \frac{(N - i)f_R(i)i}{if_M(i)(N-i)}\\
             &= \frac{f_R(i)}{f_M(i)}\\
\end{align*}
$$

We observe that:

$$
\begin{align}
    \rho_2 - \rho_1 &= \gamma_1(\rho_1-\rho_{0})=\gamma_1\rho_1\\
    \rho_3 - \rho_2 &= \gamma_2(\rho_2-\rho_1)=\gamma_2\gamma_1\rho_1\\
    \rho_4 - \rho_3 &= \gamma_3(\rho_3-\rho_2)=\gamma_3\gamma_2\gamma_1\rho_1\\
              &\; \vdots & \\
    \rho_{i+1} - \rho_i &= \gamma_i(\rho_i-\rho_{i-1})=\prod_{k=1}^i\gamma_k\rho_1\\
               &\; \vdots & \\
    \rho_{N} - \rho_{N-1} &= \gamma_{N-1}(\rho_{N-1}-\rho_{N-2})=\prod_{k=1}^{N-1}\gamma_k\rho_1\\
\end{align}
$$

thus we have:

$$\rho_i=\sum_{j=0}^{i-1}\rho_{j+1}-\rho_j=\left(1+\sum_{j=1}^{i-1}\prod_{k=1}^j\gamma_k\right)\rho_1$$

solving the following equation to obtain $\rho_1$ gives the required result.

$$\rho_N=1=\left(1+\sum_{j=1}^{N-1}\prod_{k=1}^j\gamma_k\right)\rho_1$$

---

#### Example: Direct calculation of fixation of citation behaviour

For given $N$ the fixation probabilities of [](#sec:motivating_example_preprint) can be found
directly using [](#eqn:formula_for_fixation_probabilities).

For $N=4$, recalling that $R=T$ and $M=P$, we can write down the values of $\gamma_i$ using [](#tbl:selection_probabilities):

$$
\begin{align*}
    \gamma_1 & = \frac{f_{T}(1)}{f_{P}(1)} = \frac{6}{3}=2\\
    \gamma_2 & = \frac{f_{T}(2)}{f_{P}(2)} = \frac{3}{4}\\
    \gamma_3 & = \frac{f_{T}(3)}{f_{P}(3)} = \frac{0}{5}
\end{align*}
$$

This gives:

$$
\begin{align*}
\rho_1 &= \frac{1}{1 + \sum_{j=1}^3\prod_{k=1}^{j}\gamma_k} \\
       &= \frac{1}{1 + \prod_{k=1}^{1}\gamma_k + \prod_{k=1}^{2}\gamma_k + \prod_{k=1}^{3}\gamma_k} \\
       &= \frac{1}{1 + \gamma_1 + \gamma_1\gamma_2 + \gamma_1\gamma_2\gamma_3} \\
       &= \frac{1}{1 + 2 + \frac{2\cdot 3}{4} + \frac{2\cdot 3 \cdot 0}{4\cdot5}} \\
       &= \frac{1}{1 + 2 + \frac{6}{4}}=\frac{2}{9}\\
\end{align*}
$$

as calculated [](#sec:example_fixation_of_citation_behaviour_as_an_absorbing_markov_chain).

(sec:moran_selection_strength)=

### Selection Strength

The fitness function in the Moran process need not equal the raw game payoff
directly. A parameter $w \in [0, 1]$, the **intensity of selection** (or
**selection strength**), controls how strongly payoffs influence reproductive
success. The fitness of type $i$ under selection intensity $w$ is:

$$f_i = 1 - w + w\,\pi_i$$

where $\pi_i$ is the expected payoff of type $i$ against the current population.

(sec:definition_relative_fitness)=

### Definition: Relative fitness and the constant-fitness Moran process

---

A **constant-fitness Moran process** is one in which each type has a fitness
that does not depend on the composition of the population. With two types, a
resident of fitness $f_R$ and a mutant of fitness $f_M$, the **relative
fitness** of the mutant is the ratio:

$$r = \frac{f_M}{f_R}$$

It is conventional to normalise the resident fitness to $f_R = 1$, so that the
mutant has fitness $f_M = r$ and $r$ measures how much fitter the mutant is than
the resident. Thus $r > 1$ corresponds to an advantageous mutant, $r < 1$ to a
disadvantageous one, and $r = 1$ to a neutral mutant.

For a constant-fitness process every ratio
$\gamma_k = f_R(k) / f_M(k) = r^{-1}$ is the same, so the products in
[](#eqn:formula_for_fixation_probabilities) become powers of $r^{-1}$ and the
fixation probability starting from $i$ mutants has the closed form:

$$\rho_i = \frac{1 - r^{-i}}{1 - r^{-N}}, \qquad r \neq 1$$

In particular, a single mutant fixates with probability:

$$\rho_1 = \frac{1 - r^{-1}}{1 - r^{-N}}$$

---

The neutral case $r = 1$ is recovered as a limit below, and gives
$\rho_1 = 1/N$.

(sec:definition_neutral_drift)=

### Definition: Neutral Drift

---

A Moran process exhibits **neutral drift** when $w = 0$, so that every
individual has fitness 1 regardless of strategy. The fixation probability of a
single mutant is:

$$\rho_1^{\text{neutral}} = \frac{1}{N}$$

---

This follows directly from [](#eqn:formula_for_fixation_probabilities): with
all fitnesses equal, $\gamma_k = 1$ for all $k$, and the formula reduces to
$1/N$. A mutant fixates with exactly the same probability as any randomly
chosen individual would be expected to, so chance alone determines the outcome.

(sec:definition_strong_selection)=

### Definition: Strong Selection

---

A Moran process exhibits **strong selection** when $w = 1$, so that the fitness
of each type equals its raw payoff:

$$f_i = \pi_i$$

---

The outcome depends entirely on which strategy earns higher payoffs against
the current population composition. Payoff differences are felt at full
strength at every step of the process.

(sec:definition_weak_selection)=

### Definition: Weak Selection

---

A Moran process operates under **weak selection** when $0 < w \ll 1$, so that
payoff differences introduce only a small perturbation to the neutral baseline.
The fixation probability admits a first-order expansion in $w$:

$$\rho_1 = \frac{1}{N} + w \cdot c + O(w^2)$$

for a constant $c$ that depends on the payoff matrix and population size $N$.
A mutant is **favoured by selection** if $\rho_1 > 1/N$.

---

The weak-selection regime is widely used because it permits analytical results
for arbitrary games: whether a mutant is favoured reduces to a linear condition
on the payoff matrix entries alone [@nowak2006evolutionary].

```{note}
The parameterisation $f_i = 1 - w + w\pi_i$ ensures fitness remains positive
for small $w$ even when $\pi_i$ can be negative, and reduces continuously to
neutral drift as $w \to 0$. It is equivalent to the constant-fitness
formulation $W_A = 1 + w(\pi_A - 1)$, $W_B = 1$, used in the fitness
recurrence of [](#sec:bio_fitness).
```

## Exercises

```{exercise}
:label: moran_process_with_neutral_drift

A Moran process with neutral drift is when: $f_k{v}=C$ for all $k$ for all $v$
for some constant $C$. In other words: a Moran process with neutral drift is a
Moran process where the fitness of all types for all populations is the same.

For a population with 2 types:

1. Describe the transition probabilities for the Moran process with neutral drift.
2. Obtain the transition probability matrix for the Moran process with neutral drift with $N=4$ individuals.
3. Obtain the general formula for $\rho_1$ for a Moran process with neutral
   drift for general $N$.
```

```{exercise}
:label: specific_fixation_probabilities

For the following games, assuming the mutant is of the second type, obtain the fixation probability $\rho_1$ for $N=4$:

1. $M=\begin{pmatrix}1 & 1 \\ 1 & 1\end{pmatrix}$
2. $M=\begin{pmatrix}1 & 2 \\ 3 & 1\end{pmatrix}$
```

```{exercise}
:label: the_effect_of_fitness

Consider the game $M=\begin{pmatrix}r & 1 \\ 1 & 1\end{pmatrix}$ for $r>1$ and $N$, assuming the mutant is of the second type,
obtain $\rho_1$ as a function of $r$. How does $r$ effect the chance of fixation?
```

```{exercise}
:label: moran_weak_strong_selection

Consider the constant-fitness Moran process in which a mutant type has fitness
$f_M = 1 - w + w r$ and the resident has fitness $f_R = 1 - w + w \cdot 1 = 1$,
where $r > 0$ and $w \in [0, 1]$ is the selection intensity. There are $N$
individuals in total.

1. Show that $\gamma_k = f_R / f_M$ is independent of $k$, and write down its
   value as a function of $w$ and $r$.

2. Using [](#eqn:formula_for_fixation_probabilities), derive a closed-form
   expression for $\rho_1$ in terms of $\gamma$.

3. Show that as $w \to 0$ (neutral drift), $\rho_1 \to 1/N$.

4. For $r > 1$ (the mutant has a higher raw payoff than the resident), show that
   $\rho_1 > 1/N$ for all $w > 0$: the mutant is favoured by selection at every
   positive selection intensity.

5. Interpret the two limits $w \to 0$ (weak selection) and $w \to 1$ (strong
   selection) biologically. In which regime does random drift dominate, and in
   which does payoff advantage dominate?
```

```{exercise}
:label: moran_process:exam_style_1

Consider the following matrix:

$$
M =
\begin{pmatrix}
3a & a \\
2a & 2
\end{pmatrix},
\qquad a>0.
$$


1. Show that for all $a>0$ the game defined by $M, M^T$ is **not** a Prisoners' Dilemma.

2. Find all **Nash equilibria** of the game as a function of $a$.  

3. Now consider a **two-type Moran process** with a population of size $N$.  
Type $1$ individuals play row $1$; type $2$ individuals play row $2$.

The fitness of each type is given by:

$$
f_1(i) = \left(\frac{(i-1) M_{11} + (N-i) M_{12}}{N-1}\right),
$$

$$
f_2(i) = \left(\frac{i\, M_{21} + (N-i-1) M_{22}}{N-1}\right),
$$

where $i$ is the number of type-1 individuals.

Using the standard formula:

$$
\begin{align*}
\rho_i \\
&=
\frac{
1 + \sum_{j=1}^{i-1} \prod_{k=1}^{j} \gamma_k
}{
1 + \sum_{j=1}^{N-1} \prod_{k=1}^{j} \gamma_k
},
\qquad
\gamma_k = \frac{f_2(k)}{f_1(k)},
\end{align*}
$$

4. Compute explicitly the fixation probability of a **single mutant** ($\rho_1$) for  
$N \in \{2, 3, 4\}$.  

5. For $N\in\{2, 3, 4\}$, analyse the fixation probability $\rho_1$ in the two limits:

1. $a \to 0$,  
2. $a \to \infty$.

Explain the evolutionary intuition behind these two limiting behaviours and relate 
them to the role of **fitness amplification** in frequency-dependent selection. 
```

## Programming

### Using Nashpy to simulate a Moran process

Nashpy has functionality to simulate a single Moran process. Let us create a 3
by 3 game (for a population with 3 types) and an initial population.

```{code-cell} python3
import nashpy as nash
import numpy as np

M = np.array(
    (
        (2, 3, 1),
        (4, 1, 2),
        (1, 2, 5),
    )
)
game = nash.Game(M)
initial_population = np.array((0, 0, 0, 1, 1, 1, 2))
```

```{note}
The population above corresponds to 3 individuals of the first type, 3 of the
second type and one of the third type. This is the format expected by Nashpy.
```

Now to run a Moran process, note that we seed the numpy pseudo-random number generator which is used by Nashpy:

```{code-cell} python3
np.random.seed(0)
populations = game.moran_process(initial_population=initial_population)
print(list(populations))
```

### Using Nashpy to approximate fixation probabilities

Nashpy can be directly used to approximate the fixation probabilities by
repeated a large number of Moran processes:

```{code-cell} python3
M = np.array(
    (
        (3, 0),
        (1, 2),
    )
)
game = nash.Game(M)
initial_population = np.array((0, 0, 0, 1))
fixation_probabilities = game.fixation_probabilities(
    initial_population=initial_population, repetitions=10_000
)
print(f"Fixation probabilities: {fixation_probabilities}")
```

This shows that the final population with only `1`s in it occurs $2/7\approx .22$ of the time.

## Notable Research

### Notable Research in the Moran Process and Population Genetics

The Moran process was first introduced in [@moran1958random], but it was not the
first major model in population genetics. Foundational theoretical work by
Ronald Fisher [@Fisher1930], J.B.S. Haldane [@Haldane1927; @Haldane1932], and
Sewall Wright [@Wright1931] laid the mathematical groundwork for understanding
evolution, focusing on selection and genetic drift in both infinite and finite
populations. These early models often used diffusion approximations or the
discrete-generation Wright-Fisher model. In contrast, the Moran process provided
a continuous-time, discrete-space alternative that allows exact calculation of
fixation probabilities and times. For example, Antal and Scheuring
[@AntalScheuring2006] derived precise analytical results within this framework.

The Moran process has become indispensable in evolutionary game theory, where
individual fitness depends on strategic interactions. This is central to the
theory of evolutionarily stable strategies [@taylor1978evolutionary]. It has been
especially influential in studying social dilemmas, such as the evolution of
cooperation. Traulsen and Nowak [@TraulsenNowak2006] showed how cooperation can
be favoured in finite populations, while Knight [@knight2018evolution] explored
how self-recognition algorithms can emerge through such dilemmas under the Moran
process.

The process is also crucial for analysing the role of population structure. A
notable extension is the Moran process on graphs, where individuals interact only
with their neighbors. This framework was first proposed by Lieberman, Hauert, and
Nowak [@LiebermanHauertNowak2005] and further refined by Ohtsuki, Pacheco, and
Nowak [@OhtsukiPachecoNowak2007]. The `Nashpy` library [@knight2018nashpy] can be
used to simulate Moran processes on such networks. 

A final, and remarkable, result is the one proved by Traulsen, Claussen, and
Hauert [@traulsen2005coevolutionary]: in the limit of large population size, the
Moran process converges to the replicator dynamics equation.

## Conclusion

The Moran process offers a foundational framework for understanding how
strategies evolve in finite populations. Like the [replicator dynamics
equation](#chp:replicator_dynamics), it links fitness to the growth or decline
of types over time, but with a critical distinction: it captures the inherent
stochasticity of small populations.

The central result is the fixation probability formula: by mapping the process to an [absorbing Markov chain](#app:absorbing_markov_chain), exact analysis becomes tractable for two-type populations.

The key concepts covered in this chapter are summarized in
[](#tbl:moran_process_summary).

```{table} Summary of key concepts in the Moran process
:name: tbl:moran_process_summary
:align: center

| Concept                        | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| **Moran process**             | A stochastic model of evolution in finite populations                       |
| **Copy selection probability**| Probability of choosing an individual for reproduction, proportional to fitness |
| **Removal selection probability**| Probability of choosing an individual for removal, uniform across the population |
| **Absorbing state**           | A population state in which all individuals are of a single type            |
| **Fixation probability**      | Probability that a given type eventually takes over the population          |
```

```{important}
In a finite population the Moran Process will terminate with non zero
probability in a state with all individuals being of the same type.

The fixation probability quantifies the likelihood that a particular type
ultimately dominates the population.
```

---

(solutions:moran_process)=

## Solutions

````{solution} moran_process_with_neutral_drift
:label: solution:moran_process_with_neutral_drift

1. Under neutral drift every individual has the same fitness $C$, so selection
   for copying is uniform. In a state with $i$ mutants and $N - i$ residents a
   mutant is copied with probability $i/N$ and a resident with probability
   $(N - i)/N$; removal is uniform, so a resident is removed with probability
   $(N - i)/N$ and a mutant with probability $i/N$. Hence

   $$
   P_{i \to i+1} = \frac{i}{N}\cdot\frac{N - i}{N} = \frac{i(N - i)}{N^2},
   \qquad
   P_{i \to i-1} = \frac{N - i}{N}\cdot\frac{i}{N} = \frac{i(N - i)}{N^2},
   $$

   with $P_{i \to i} = 1 - 2i(N - i)/N^2$. The up and down probabilities are
   equal, so the process is a symmetric random walk on $\{0, 1, \dots, N\}$
   with the two endpoints absorbing.

2. For $N = 4$ we have $i(N - i)/16$ equal to $3/16$, $4/16 = 1/4$ and $3/16$
   for $i = 1, 2, 3$. Indexing the states by the number of mutants
   $i \in \{0, 1, 2, 3, 4\}$,

   $$
   P = \begin{pmatrix}
   1 & 0 & 0 & 0 & 0\\
   3/16 & 5/8 & 3/16 & 0 & 0\\
   0 & 1/4 & 1/2 & 1/4 & 0\\
   0 & 0 & 3/16 & 5/8 & 3/16\\
   0 & 0 & 0 & 0 & 1
   \end{pmatrix}.
   $$

3. Since every $\gamma_k = f_R(k)/f_M(k) = C/C = 1$, the products in
   [](#eqn:formula_for_fixation_probabilities) are all $1$ and

   $$
   \rho_i = \frac{1 + \sum_{j=1}^{i-1} 1}{1 + \sum_{j=1}^{N-1} 1} = \frac{i}{N},
   \qquad\text{so}\qquad \rho_1 = \frac{1}{N}.
   $$

   A single neutral mutant fixates with probability $1/N$, exactly its initial
   share of the population.
````

````{solution} specific_fixation_probabilities
:label: solution:specific_fixation_probabilities

The mutant is the second type, so residents are of the first type. In a state
with $k$ mutants the fitnesses are
$f_R(k) = (N - k - 1)M_{11} + k M_{12}$ and
$f_M(k) = (N - k)M_{21} + (k - 1)M_{22}$, and $\gamma_k = f_R(k)/f_M(k)$. With
$N = 4$,

$$
\rho_1 = \frac{1}{1 + \gamma_1 + \gamma_1\gamma_2 + \gamma_1\gamma_2\gamma_3}.
$$

1. For $M = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ every payoff equals
   $1$, so $f_R(k) = (N - k - 1) + k = N - 1$ and
   $f_M(k) = (N - k) + (k - 1) = N - 1$. Thus $\gamma_k = 1$ for all $k$: this
   is neutral drift and $\rho_1 = 1/N = 1/4$.

2. For $M = \begin{pmatrix} 1 & 2 \\ 3 & 1 \end{pmatrix}$ we obtain
   $f_R(k) = (3 - k) + 2k = 3 + k$ and $f_M(k) = 3(4 - k) + (k - 1) = 11 - 2k$,
   so $\gamma_k = (3 + k)/(11 - 2k)$. Hence $\gamma_1 = 4/9$, $\gamma_2 = 5/7$
   and $\gamma_3 = 6/5$, giving

   $$
   \rho_1 = \frac{1}{1 + \frac{4}{9} + \frac{4}{9}\cdot\frac{5}{7}
   + \frac{4}{9}\cdot\frac{5}{7}\cdot\frac{6}{5}}
   = \frac{1}{15/7} = \frac{7}{15}.
   $$

```{code-cell} python3
import sympy as sym

def fixation_probability(M, N):
    resident_fitness = lambda k: (N - k - 1) * M[0][0] + k * M[0][1]
    mutant_fitness = lambda k: (N - k) * M[1][0] + (k - 1) * M[1][1]
    gammas = [
        sym.Rational(resident_fitness(k), mutant_fitness(k)) for k in range(1, N)
    ]
    total = 1
    product = 1
    for gamma in gammas:
        product *= gamma
        total += product
    return sym.simplify(1 / total)

print(fixation_probability([[1, 1], [1, 1]], 4))
print(fixation_probability([[1, 2], [3, 1]], 4))
```
````

````{solution} the_effect_of_fitness
:label: solution:the_effect_of_fitness

The mutant is the second type. Since the second row of
$M = \begin{pmatrix} r & 1 \\ 1 & 1 \end{pmatrix}$ is constant, a mutant always
earns $1$ against any opponent, while residents earn $r$ against each other and
$1$ against a mutant. In a state with $k$ mutants,

$$
f_R(k) = (N - k - 1)r + k, \qquad f_M(k) = (N - k) + (k - 1) = N - 1,
$$

so

$$
\gamma_k = \frac{f_R(k)}{f_M(k)} = \frac{r(N - 1 - k) + k}{N - 1}.
$$

For $r > 1$ and $k < N - 1$ we have $\gamma_k > 1$, while $\gamma_{N-1} = 1$;
the residents are the fitter type and the products grow with $r$. The fixation
probability is therefore

$$
\rho_1 = \frac{1}{1 + \sum_{j=1}^{N-1}\prod_{k=1}^{j}\gamma_k},
$$

a decreasing function of $r$. Evaluating for small $N$:

- $N = 2$: $\gamma_1 = 1$ and $\rho_1 = 1/2$ for every $r$. With a single
  resident and a single mutant neither type has yet met its own kind, so the
  contest is neutral.
- $N = 3$: $\gamma_1 = (r + 1)/2$ and $\gamma_2 = 1$, giving
  $\rho_1 = 1/(r + 2)$.
- $N = 4$: $\gamma_1 = (2r + 1)/3$, $\gamma_2 = (r + 2)/3$ and $\gamma_3 = 1$,
  giving $\rho_1 = 9 / \bigl(4(r + 2)^2\bigr)$.

As $r \to 1$ each expression returns the neutral value $1/N$, and as
$r \to \infty$ the fixation probability tends to $0$ for $N \geq 3$: the fitter
the residents, the less likely a mutant is to take over. Because the mutant's
fitness is fixed at $N - 1$, the parameter $r$ acts entirely through the
residents.

```{code-cell} python3
import sympy as sym

r = sym.Symbol("r", positive=True)

def fixation_probability(M, N):
    resident_fitness = lambda k: (N - k - 1) * M[0][0] + k * M[0][1]
    mutant_fitness = lambda k: (N - k) * M[1][0] + (k - 1) * M[1][1]
    gammas = [resident_fitness(k) / mutant_fitness(k) for k in range(1, N)]
    total = 1
    product = 1
    for gamma in gammas:
        product *= gamma
        total += product
    return sym.simplify(1 / total)

for N in (2, 3, 4):
    rho_1 = fixation_probability([[r, 1], [1, 1]], N)
    print(N, rho_1, sym.limit(rho_1, r, sym.oo))
```
````

````{solution} moran_weak_strong_selection
:label: solution:moran_weak_strong_selection

1. With $f_M = 1 - w + wr$ and $f_R = 1$, the ratio is:

$$\gamma_k = \frac{f_R}{f_M} = \frac{1}{1 - w + wr} = \frac{1}{1 + w(r-1)}$$

which is independent of $k$ (constant-fitness Moran process).

2. Since $\gamma_k = \gamma$ for all $k$, the products simplify:
$\prod_{k=1}^{j}\gamma_k = \gamma^j$. Thus:

$$\rho_1 = \frac{1}{1 + \sum_{j=1}^{N-1}\gamma^j} = \frac{1}{\sum_{j=0}^{N-1}\gamma^j}$$

For $\gamma \neq 1$ this is a geometric sum:

$$\rho_1 = \frac{1 - \gamma}{1 - \gamma^N}$$

3. As $w \to 0$, $\gamma \to 1$. Applying L'Hôpital's rule (or noting both
numerator and denominator tend to 0):

$$\lim_{\gamma \to 1}\frac{1 - \gamma}{1 - \gamma^N} = \lim_{\gamma \to 1}\frac{-1}{-N\gamma^{N-1}} = \frac{1}{N}$$

So $\rho_1 \to 1/N$ as $w \to 0$, confirming the neutral drift result.

4. For $r > 1$ and $w > 0$, we have $\gamma = 1/(1 + w(r-1)) < 1$. With
$\gamma < 1$ the fixation probability is:

$$\rho_1 = \frac{1 - \gamma}{1 - \gamma^N}$$

We need to show $\rho_1 > 1/N$, i.e. $N(1 - \gamma) > 1 - \gamma^N$.
Define $g(\gamma) = 1 - \gamma^N - N(1 - \gamma)$ for $\gamma \in (0,1)$.
Then $g(1) = 0$ and $g'(\gamma) = -N\gamma^{N-1} + N = N(1 - \gamma^{N-1}) > 0$
for $\gamma \in (0,1)$. So $g$ is increasing on $(0,1)$ and $g(\gamma) < g(1) = 0$,
meaning $1 - \gamma^N < N(1-\gamma)$, i.e. $\rho_1 > 1/N$. $\square$

5. Under **weak selection** ($w \approx 0$) the fitnesses of all individuals
are nearly equal (all close to 1), so which individual is copied is nearly
random. Random drift dominates: the mutant may fix or go extinct regardless of
whether $r > 1$ or $r < 1$, and the fixation probability is close to $1/N$.
Under **strong selection** ($w = 1$) fitness differences are maximal. If
$r > 1$, the mutant is substantially fitter than the resident at every
population state, and the fixation probability is maximised. In the extreme,
as $r \to \infty$, $\gamma \to 0$ and $\rho_1 \to 1$: the mutant is almost
certain to take over. Strong selection amplifies the effect of fitness
differences; weak selection washes them out.

```{code-cell} python3
import numpy as np
import matplotlib.pyplot as plt

def rho_1(w, r, N):
    gamma = 1 / (1 + w * (r - 1))
    if abs(gamma - 1) < 1e-12:
        return 1 / N
    return (1 - gamma) / (1 - gamma ** N)

N = 10
r_values = [1.5, 2.0, 3.0]
w_range = np.linspace(0, 1, 200)

plt.figure(figsize=(6, 4))
for r in r_values:
    plt.plot(w_range, [rho_1(w, r, N) for w in w_range], label=f"$r = {r}$")
plt.axhline(1 / N, color="gray", linestyle="--", label=f"Neutral drift $1/N = 1/{N}$")
plt.xlabel("Selection intensity $w$")
plt.ylabel(r"Fixation probability $\rho_1$")
plt.title(f"Fixation probability vs selection intensity ($N={N}$)")
plt.legend()
plt.tight_layout()
```
````

````{solution} moran_process:exam_style_1
:label: solution:moran_process:exam_style_1

1. The standard definition of the [Prisoners Dilemma](#def:prisoners-dilemma) is:

$$
M_r = 
\begin{pmatrix}
    R & S\\
    T & P
\end{pmatrix}
$$

with $T > R > P > S$ and $2R > T + S$. In this case we have:

$$R=3a\qquad T=2a \qquad S=a \qquad P=2$$

This implies that for $a>0$ we have $T<R$ thus this is not Prisoner's Dilemma.

2. There are 5 potential Nash equilibria for

$$
M_r = 
\begin{pmatrix}
    3a & a\\
    2a & 2
\end{pmatrix}
\qquad
M_c = 
\begin{pmatrix}
    3a & 2a\\
    a & 2
\end{pmatrix}
$$

$(r_1, c_1)$ is a Nash Equilibrium if and only if:

$$
3a \geq 2a \Leftrightarrow a\geq 0
$$


$(r_1, c_2)$ is a Nash Equilibrium if and only if:

$$
a \geq 2 \text{ and } 2a \geq 3a \Rightarrow a \geq 0
$$

This is not possible.

$(r_2, c_1)$ is a Nash equilibrium if and only if:


$$
2a \geq 3a \text{ and } a \geq 2a 
$$

Which is again, not possible.


$(r_2, c_2)$ is a Nash equilibrium if and only if:

$$
a \leq 2
$$

Let $\sigma_1=(x, 1 - x)$ and $\sigma_2=(y, 1-y)$.

$(\sigma_1, \sigma_2)$ with $0<x<1$ and $0<y<1$ is a Nash equilibrium if and
only if:

$$
\begin{align}
3ay+a(1-y)&=2ay+2(1-y)\\
     2ay+a&=2ay+2-2y\\
     y(2a-2a+2)&=2-a\\
              y&=\frac{2 - a}{2}
\end{align}
$$

$0<y<1$ holds if and only if:

$$
0<a<2
$$

The above answers the question. Here is some code to count and display the final
situation:

```{code-cell} python3
import nashpy as nash
import matplotlib.pyplot as plt
import numpy as np

a_values = np.linspace(-10, 10, 500)
number_of_equilibrium = []
for a in a_values:
    M_r = np.array(
        (
            (3 * a, a),
            (2 * a, 2),
        )
    )
    M_c = M_r.T
    game = nash.Game(M_r, M_c)
    number_of_equilibrium.append(
        len(
            list(game.support_enumeration())
        )
    )

plt.figure()
plt.scatter(a_values, number_of_equilibrium)
plt.xlabel("$a$")
plt.title("number of equilibrium")
plt.axvline(2)
plt.axvline(0)
plt.text(-7.5, 2, r"$\{(r_2, c_2)\}$")
plt.text(5, 2, r"$\{(r_1, c_1)\}$")
plt.text(0.75, 1.5, r"$\{(r_1, c_1), (\sigma_1, \sigma_2),(r_2, c_2) \}$", rotation=90);
```

4. For $N=2$:

$$
\begin{align}
f_1(a) &= \frac{(i - 1)3a+(2 - i)a}{1}\\
f_2(a) &= \frac{2ai+2(1 - i)}{1}\\
\end{align}
$$

This gives:

$$
\gamma_i = \frac{i(2a - 2) + 2}{2ai - a} = \frac{2ai-2i + 2}{2ai - a}
$$

This gives:

$$
\rho_1 = \frac{1}{1 + \gamma_1} = \frac{1}{1 + \frac{2a}{a}}=\frac{1}{1 + 2}=\frac{1}{3}
$$

Let us use some code to confirm these calculations:

```{code-cell} python3
import sympy as sym

i = sym.Symbol("i")
a = sym.Symbol("a")
f_1 = ((3 * a * (i - 1) + (2 - i) * a) / 2)
f_2 = ((2 * a * i + 2 * (1 - i)) / 2)
gamma = sym.simplify(f_2 / f_1)
gamma
```

```{code-cell} python3
rho_1_N_2 = 1 / (1 + gamma.subs({i: 1}))
rho_1_N_2
```

For $N=3$:

$$
\begin{align}
f_1(a) &= \frac{(i - 1)3a+(3 - i)a}{2}\\
f_2(a) &= \frac{2ai+2(2 - i)}{2}\\
\end{align}
$$

$$
\gamma_i = \frac{2ai +4 - 2i}{3ai-3a+3a-ai}=\frac{2ai+4-2i}{2ai}=\frac{i(a-1) + 2}{ai}
$$



This gives:

$$
\begin{align}
\rho_1 &= \frac{1}{1 + \gamma_1 + \gamma_1\gamma_2} = \frac{1}{1 + \frac{a + 1}{a} + \frac{a+1}{a}\frac{2a}{2a}}
       &= \frac{1}{\frac{a + 2a + 2}{a}}\\
       &=\frac{a}{3a + 2}
\end{align}
$$

Let us use some code to confirm these calculations:

```{code-cell} python3
f_1 = ((3 * a * (i - 1) + (3 - i) * a) / 2)
f_2 = ((2 * a * i + 2 * (2 - i)) / 2)
gamma = sym.simplify(f_2 / f_1)
gamma
```


```{code-cell} python3
rho_1_N_3 = 1 / (1 + gamma.subs({i: 1})+ gamma.subs({i: 1}) * gamma.subs({i: 2}))
sym.simplify(rho_1_N_3)
```

For $N=4$:

$$
\begin{align}
f_1(a) &= \frac{(i - 1)3a+(4 - i)a}{3}\\
f_2(a) &= \frac{2ai+2(3 - i)}{3}\\
\end{align}
$$

$$
\gamma_i = \frac{i(2a - 2) + 6}{2ai + a}=\frac{2(ai-i+3)}{a(2i+1)}
$$

This gives:

$$
\begin{align}
\rho_1 &= \frac{1}{1 + \gamma_1 + \gamma_1\gamma_2 + \gamma_1\gamma_2\gamma_3}\\
       & = \frac{1}{1 + \frac{2(a + 2)}{3a} + \frac{2(a + 2)}{3a}\frac{2(2a+1)}{5a} + \frac{2(a + 2)}{3a}\frac{2(2a+1)}{5a}\frac{6a}{7a}}\\
       & = \frac{1}{\frac{3\cdot 5 a ^2}{3\cdot 5 a ^2} + \frac{2(a + 2)\cdot 5 a}{3\cdot 5a^2} + \frac{\frac{7 + 6}{7}(2(a + 2)2(2a+1))}{3\cdot 5 a ^ 2}}\\
       & = \frac{1}{\frac{3\cdot 5\cdot 7 a ^2}{3\cdot 5 \cdot 7 a ^2} + \frac{7 \cdot 2(a + 2)\cdot 5 a}{3\cdot 5\cdot 7a^2} + \frac{13(2(a + 2)2(2a+1))}{3\cdot 5 \cdot 7a ^ 2}}\\
       & = \frac{3\cdot 5 \cdot 7 a ^ 2}{3\cdot 5\cdot 7 a ^2 + 7 \cdot 2(a + 2)\cdot 5 a + 13(2(a + 2)2(2a+1))}\\
       & = \frac{3\cdot 5 \cdot 7 a ^ 2}{105 a ^ 2 + 70 a ^ 2 + 140 a + 104a ^ 2 + 260 a + 104}\\
       & = \frac{3\cdot 5 \cdot 7 a ^ 2}{279a^2 + 400a + 104}\\
\end{align}
$$

Let us use some code to confirm these calculations:

```{code-cell} python3
f_1 = ((3 * a * (i - 1) + (4 - i) * a) / 3)
f_2 = ((2 * a * i + 2 * (3 - i)) / 3)
gamma = sym.simplify(f_2 / f_1)
gamma
```


```{code-cell} python3
rho_1_N_4 = 1 / (1 + gamma.subs({i: 1})+ gamma.subs({i: 1}) * gamma.subs({i: 2})+ gamma.subs({i: 1}) * gamma.subs({i: 2}) * gamma.subs({i: 3}))
sym.simplify(rho_1_N_4)
```

5. 

a. For all $N=2$ we have:

$$\lim_{a\to 0}\rho_1=1/3$$

For $N\in\{3, 4\}$

$$\lim_{a\to 0}\rho_1=0$$

b. For $N=2$ we have:

$$\lim_{a\to \infty}\rho_1=\lim_{a\to \infty}1/3=1/3$$

For $N=3$ we have:

$$\lim_{a\to \infty}\rho_1=\lim_{a\to \infty}\frac{a}{3a + 2}=\lim_{a\to \infty}\frac{1}{3 + 2/a}=1/3$$


For $N=4$ we have:

$$
\begin{align}
\lim_{a\to \infty}\rho_1&=\lim_{a\to \infty}\frac{3\cdot 5 \cdot 7 a ^ 2}{279a^2 + 400a + 104}\\
                        &=\lim_{a\to \infty}\frac{3\cdot 5\cdot 7}{279 + 400/a +
104 / a^2}\\
                        &=\frac{3\cdot 5\cdot 7}{279}=\frac{3\cdot 5\cdot 7}{3 ^
2 \cdot 31}=\frac{35}{93}
\end{align}
$$

Let us write some code to confirm this:

```{code-cell} python3
sym.limit(rho_1_N_2, a, 0)
```

```{code-cell} python3
sym.limit(rho_1_N_2, a, sym.oo)
```

```{code-cell} python3
sym.limit(rho_1_N_3, a, 0)
```

```{code-cell} python3
sym.limit(rho_1_N_3, a, sym.oo)
```

```{code-cell} python3
sym.limit(rho_1_N_4, a, 0)
```

```{code-cell} python3
sym.limit(rho_1_N_4, a, sym.oo)
```

This shows that the amplification of the fitness (the increase of $a$) has
a greater effect for larger $N$.
````
