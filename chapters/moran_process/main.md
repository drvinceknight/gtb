---
kernelspec:
  name: python3
  display_name: "Python 3"
---

(chp:moran_process)=

# Moran Process

(sec:motivating_example_preprint)=

## Motivating Example: Everyone’s citing the preprint

In a graduate student reading group, everyone cites a well-established
textbook in their essays. One student, though, starts citing a
**recent preprint** they found on arXiv.

> "It’s got a better proof of the key result — and it’s open access."

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
not fixed — it **depends on the current citation habits** of the group. This
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
payoff of 2 — slightly lower, but still beneficial.

If one cites the textbook while the other cites the preprint, there is a
mismatch: the **preprint-citer** still gets some benefit (payoff 1) from its
clarity and openness, but the textbook-citer gains nothing (payoff 0) from
the mismatch.

Note here that the group is small and so the infinite population assumption of
[](#chp:replicator_dynamics) does not apply: the topic of this chapter is the
Moran Process a model suited for exactly this purpose.

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

### Example: Selection Probabilities for citation behaviour.

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
P_{i \to i-1} = (\text{Prob copy resident})\cdot (\text{Prob copy mutant})
$$

Finally:

$$
\label{eqn:probabilities_of_no_change_in_moran_process}
P_{i \to i} = 1 - P_{i \to i+1} - P_{i \to i-1}
$$

(sec:example_fixation_of_citation_behaviour_as_an_absorbing_markov_chain)=

### Example: Fixation of citation behaviour as an absorbing Markov chain

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
\gamma_k = \frac{f_R(i)}{f_M(i)}
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
             &= \frac{\frac{(N - i)f_R(i)}{if_R(i) + (N - i)f_R(i)}\frac{i}{N}}{\frac{if_M(i)}{if_R(i) + (N - i)f_R(i)}\frac{N-i}{N}}\\
             &= \frac{(N - i)f_R(i)}{if_R(i) + (N - i)f_R(i)}\frac{i}{N}{\frac{if_R(i) + (N - i)f_R(i)}{if_M(i)}\frac{N}{N-i}}\\
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

### Example: Direct calculation of fixation of citation behaviour

For given $N$ the fixation probabilities of [](#sec:motivating_example_preprint) can be found
directly using [](#eqn:formula_for_fixation_probabilities).

For $N=4$, recalling that $R=T$ and $M=P$, we can write down the values of $\gamma_i$ sing [](#tbl:selection_probabilities):

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
\rho_1 &= \frac{1}{1 + \sum_{j=1}^3\prod{k=1}^{j}\gamma_k} \\
       &= \frac{1}{1 + \prod{k=1}^{1}\gamma_k + \prod{k=1}^{2}\gamma_k + \prod{k=1}^{3}\gamma_k} \\
       &= \frac{1}{1 + \gamma_1 + \gamma_1\gamma_2 + \gamma_1\gamma_2\gamma_3} \\
       &= \frac{1}{1 + 2 + \frac{2\cdot 3}{4} + \frac{2\cdot 3 \cdot 0}{4\cdot5}} \\
       &= \frac{1}{1 + 2 + \frac{6}{4}}=\frac{2}{9}\\
\end{align*}
$$

as calculated [](#sec:example_fixation_of_citation_behaviour_as_an_absorbing_markov_chain).

## Exercises

### Exercise: Moran Process with neutral drift

A Moran process with neutral drift is when: $f_k{v}=C$ for all $k$ for all $v$
for some constant $C$. In other words: a Moran process with neutral drift is a
Moran process where the fitness of all types for all populations is the same.

For a population with 2 types:

1. Describe the transition probabilities for the Moran process with neutral drift.
2. Obtain the transition probability matrix for the Moran process with neutral drift with $N=4$ individuals.
3. Obtain the general formula for $\rho_1$ for a Moran process with neutral
   drift for general $N$.

### Exercise: Specific fixation probabilities

For the following games, assuming the mutant is of the second type, obtain the fixation probability $\rho_1$ for $N=4$:

1. $M=\begin{pmatrix}1 & 1 \\ 1 & 1\end{pmatrix}$
2. $M=\begin{pmatrix}1 & 2 \\ 3 & 1\end{pmatrix}$

### Exercise: The effect of fitness

Consider the game $M=\begin{pmatrix}r & 1 \\ 1 & 1\end{pmatrix}$ for $r>1$ and $N$, assuming the mutant is of the second type,
obtain $\rho_1$ as a function of $r$. How does $r$ effect the chance of fixation?

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
\rho_i
=
\frac{
1 + \displaystyle\sum_{j=1}^{i-1} \prod_{k=1}^{j} \gamma_k
}{
1 + \displaystyle\sum_{j=1}^{N-1} \prod_{k=1}^{j} \gamma_k
},
\qquad
\gamma_k = \frac{f_2(k)}{f_1(k)},
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
list(populations)
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
game.fixation_probabilities(initial_population=initial_population, repetitions=10_000)
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
be favored in finite populations, while Knight [@knight2018evolution] explored
how self-recognition algorithms can emerge through such dilemmas under the Moran
process.

The process is also crucial for analyzing the role of population structure. A
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
of types over time — but with a critical distinction: it captures the inherent
stochasticity of small populations.

In this chapter, we:

- Defined the Moran process as a stochastic model of selection and reproduction;
- Introduced **fixation probabilities**, the likelihood that a given type takes
  over the population;
- Showed how the process corresponds to an
  [absorbing Markov chain](#app:absorbing_markov_chain), enabling exact analysis;
- Proved a general formula for fixation probabilities in the case of two types.

These results highlight how even simple stochastic rules can give rise to rich
evolutionary behavior. The Moran process provides a tractable yet powerful model
that extends beyond biology — from the spread of opinions to the diffusion of
technologies.

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
