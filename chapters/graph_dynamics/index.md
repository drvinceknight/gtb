---
kernelspec:
  name: python3
  display_name: "Python 3"
---

(chp:graph_dynamics)=

# Evolutionary Dynamics on Graphs

The [Moran Process](#chp:moran_process) and the
[replicator dynamics](#chp:replicator_dynamics) both assume a well-mixed
population, in which every individual is equally likely to interact with every
other. Real populations are rarely so uniform: individuals interact with
neighbours on a social network, a spatial lattice, or a contact structure. This
chapter places the population on a graph and asks how that structure changes the
course of evolution.

(sec:motivating_example_reading_group_network)=

## Motivating Example: The reading group is a network

Return to the graduate reading group of the [Moran Process](#chp:moran_process),
where students cite either a textbook or a preprint and occasionally update their
choice by copying an admired peer. The Moran process treated the group as
well-mixed: any student could copy any other. In practice a student copies the
people they actually talk to, their collaborators, office-mates, and supervisor,
not the whole department.

That contact structure is a **graph**: the students are vertices, and an edge
joins two students who influence each other. [](#fig:structured_population)
contrasts the well-mixed group with a structured one. The composition is
identical, two preprint citers among six, but in the structured group the
preprint citers sit together, and whether the preprint spreads or dies out now
depends on _where_ in the network it starts and _how_ copying proceeds.

```{figure} ./images/structured_population/main.png
:alt: Two six-vertex graphs with the same vertex colours: a complete graph and a sparse structured graph.
:label: fig:structured_population
:align: center
:width: 90%

A well-mixed population is a complete graph (A), in which everyone interacts
with everyone. A structured population (B) keeps the same individuals and the
same composition but restricts interaction to the edges of a sparser graph.
```

Structure can help a rare strategy spread, or hold it back. Making this precise
is the subject of the chapter.

## Theory

(sec:definition_evolutionary_graph)=

### Definition: Evolutionary graph

---

An **evolutionary graph** is a connected graph $G = (V, E)$ on $N = |V|$
vertices, each occupied by one individual. Two individuals interact, and may
replace one another through reproduction, only if they are joined by an edge.
The **degree** of a vertex is its number of neighbours, and the graph is
**$k$-regular** if every vertex has degree $k$.

---

The well-mixed population of the Moran process is the special case of the
**complete graph** $K_N$, in which every pair of vertices is joined and every
vertex has degree $N - 1$.

#### Example: The reading group as a graph

The structured reading group in [](#fig:structured_population)B is an
evolutionary graph on $N = 6$ vertices, in which each student has only two or
three neighbours and can be copied only by them. Because the degrees differ
across students, the graph is irregular. The well-mixed group of
[](#fig:structured_population)A is by contrast the complete graph $K_6$, in which
every student has five neighbours and the process is the ordinary Moran process.

(sec:definition_moran_on_graph)=

### Definition: The Moran process on a graph

---

In the **Moran process on a graph** with mutant fitness $r > 0$ and resident
fitness $1$, each step is a **Birth-Death** update:

1. an individual is chosen to reproduce with probability proportional to its
   fitness;
2. its offspring, a copy of itself, replaces a uniformly chosen **neighbour**.

The population size $N$ stays fixed, and the process continues until the mutant
type either takes over every vertex (**fixation**) or disappears.

---

The only change from the [Moran Process](#chp:moran_process) chapter is step 2:
the offspring replaces a neighbour rather than any individual at all. On the
complete graph every other individual is a neighbour, and the process reduces
exactly to the well-mixed Moran process. [](#fig:update_rules)A illustrates one
Birth-Death step.

```{figure} ./images/update_rules/main.png
:alt: Two panels showing a focal vertex and neighbours: Birth-Death updating and Death-Birth updating.
:label: fig:update_rules
:align: center
:width: 90%

Two update rules on a graph. Under **Birth-Death** (A) a parent is chosen by
fitness and its offspring replaces a random neighbour. Under **Death-Birth**
(B) a random individual dies and its neighbours compete, in proportion to
fitness, to fill the vacancy.
```

```{note}
The Moran process on a graph admits two readings of the same mathematics. In the
**biological** reading the graph is a **reproduction graph**: an individual
reproduces and its offspring disperses along an edge to displace a neighbour. In
the **cultural** reading, the one behind our reading group, the graph is an
**imitation graph**: an individual copies the strategy of a neighbour it admires,
and no birth or death takes place at all. The two readings give the identical
Markov chain, so every result of this chapter applies to each.

A single graph here plays two distinct roles: it decides who interacts with whom,
and it decides who may replace whom. These roles can be separated into an
**interaction graph**, on which the game is played and fitness accrues, and a
**replacement graph**, the reproduction or imitation graph along which strategies
spread. Taking the two to coincide, as we do throughout, follows Lieberman,
Hauert, and Nowak [@lieberman2005evolutionary]; allowing them to differ is a
natural extension.
```

#### Example: a single preprint citer in the reading group

Suppose one student starts citing the preprint, which is more persuasive and so
carries fitness $r > 1$, while the textbook citers have fitness $1$. On the
complete graph the probability that the preprint eventually takes over is the
well-mixed Moran fixation probability,

$$
\rho = \frac{1 - 1/r}{1 - 1/r^{N}},
$$

exactly as in the [Moran Process](#chp:moran_process) chapter. On a structured
graph the answer can be larger or smaller, and depends on which student first
adopts the preprint.

(sec:theorem_isothermal)=

### Theorem: The isothermal theorem

---

If a graph is **isothermal**, meaning every vertex has the same total incoming
edge weight (for an unweighted graph, that it is regular), then the fixation
probability of a single mutant placed at a uniformly random vertex equals the
well-mixed Moran value $\rho = (1 - 1/r)/(1 - 1/r^{N})$.

---

We state this result, due to Lieberman, Hauert, and Nowak
[@lieberman2005evolutionary], without proof. The complete graph and every cycle
are isothermal, so on these graphs structure has no effect on fixation. Graphs
that are not isothermal can change the fixation probability, and we classify
them accordingly.

- An **amplifier of selection** raises the fixation probability of beneficial
  mutants ($r > 1$) above the Moran value and lowers that of deleterious ones
  ($r < 1$). It sharpens selection.
- A **suppressor of selection** does the opposite, pushing fixation
  probabilities towards the neutral value $1/N$ and so favouring drift over
  selection.

#### Example: the star amplifies selection

The **star** $K_{1, N-1}$, a single central vertex joined to $N - 1$ leaves
([](#fig:amplifier_star)B), is the canonical amplifier. For large $N$ the
fixation probability of a beneficial mutant on the star is approximately

$$
\rho_{\text{star}} \approx \frac{1 - 1/r^{2}}{1 - 1/r^{2N}},
$$

which is the Moran value with $r$ replaced by $r^{2}$. A beneficial mutant
therefore fixes as if its fitness advantage were squared: the star amplifies
selection. We confirm this by simulation in the [Programming](#sec:programming_graph_dynamics) section.

```{figure} ./images/amplifier_star/main.png
:alt: A complete graph and a star graph, each on six vertices.
:label: fig:amplifier_star
:align: center
:width: 90%

The complete graph (A) is isothermal, so its fixation probability matches the
well-mixed Moran process. The star (B) is an amplifier: it raises the fixation
probability of beneficial mutants and lowers that of deleterious ones.
```

(sec:definition_death_birth)=

### Definition: Death-Birth updating

---

Under **Death-Birth** updating, each step reverses the order of events:

1. an individual is chosen uniformly at random to die;
2. its neighbours compete to fill the vacancy, each chosen with probability
   proportional to its fitness.

---

The order in which birth and death occur, illustrated in
[](#fig:update_rules), looks like a small detail but it changes the outcome,
because it changes which individuals compete with which. Death-Birth updating
is the setting for the most celebrated result on graph-structured cooperation.

#### Example: why the order of events matters

Take three students in a line, $A - B - C$, with $B$ citing the preprint and $A$
and $C$ the textbook. Under **Death-Birth**, if $B$ is the student chosen to
die, the vacancy is filled by one of its neighbours, $A$ or $C$, both of whom
cite the textbook, so the preprint is lost at that spot. Under **Birth-Death**,
by contrast, a parent is chosen from the whole population by fitness and then
replaces a neighbour, so a fit preprint citer elsewhere can still spread. The two
rules act on the same configuration differently, which is why the condition for
cooperation in the next theorem is specific to Death-Birth updating.

(sec:theorem_bc_rule)=

### Theorem: The $b/c > k$ rule for cooperation

Consider the **donation game** played along the edges of a graph: a cooperator
pays a cost $c$ so that each of its neighbours receives a benefit $b > c$, while
a defector pays nothing and gives nothing.

---

Under Death-Birth updating on a $k$-regular graph, in a large population and
under weak selection, natural selection favours cooperation over defection if
and only if

$$
\frac{b}{c} > k.
$$

---

This remarkably simple rule is due to Ohtsuki, Hauert, Lieberman, and Nowak
[@ohtsuki2006simple]. It says that population structure makes cooperation easier
to evolve exactly when the network is sparse: the smaller the average number of
neighbours $k$, the lower the benefit-to-cost ratio needed to sustain
cooperation. In a well-mixed population $k = N - 1$ is large, and the condition
$b/c > N - 1$ essentially never holds, which recovers the familiar result that
cooperation cannot survive without some further mechanism. On a sparse graph,
cooperators form clusters and preferentially help one another, and cooperation
can prevail.

#### Example: cooperation on a sparse network

On a $4$-regular graph, such as a large square lattice where each individual has
four neighbours, the donation game favours cooperation when $b/c > 4$. If
cooperating costs $c = 1$ and benefits each neighbour by $b = 5$, then
$b/c = 5 > 4$ and cooperation is favoured. If instead $b = 3$, then
$b/c = 3 < 4$ and defection wins. The same game on a denser $10$-regular network
would require $b/c > 10$, and cooperation would fail in both cases.

## Exercises

```{exercise}
:label: graph_isothermal_graphs

For each of the following graphs on $N$ vertices, state whether it is isothermal
(regular) and hence whether the fixation probability of a single mutant equals
the well-mixed Moran value.

1. The cycle $C_N$, in which the vertices are joined in a single ring.
2. The path $P_N$, in which the vertices are joined in a line.
3. The star $K_{1, N-1}$.
4. The complete graph $K_N$.
```

```{exercise}
:label: graph_neutral_fixation

Consider the Moran process on a connected graph with $N$ vertices under
**neutral drift**, that is with mutant fitness $r = 1$. A single mutant is
placed at a uniformly random vertex.

Argue that the probability the mutant fixes is $1/N$, regardless of the graph.
```

```{exercise}
:label: graph_bc_rule_application

A donation game is played under Death-Birth updating on a $k$-regular graph,
with benefit $b$ and cost $c$.

1. For a ring ($k = 2$) with $b = 3$ and $c = 1$, is cooperation favoured?
2. For a $6$-regular network with $b = 5$ and $c = 1$, is cooperation favoured?
3. What is the largest degree $k$ for which cooperation is favoured when
   $b = 9$ and $c = 2$?
```

```{exercise}
:label: graph_amplifier_comparison

A beneficial mutant has fitness $r = 2$ in a population of $N = 10$ individuals.

1. Compute the fixation probability on the complete graph using the well-mixed
   Moran formula.
2. Using the large-population approximation
   $\rho_{\text{star}} \approx (1 - 1/r^{2})/(1 - 1/r^{2N})$, compute the
   fixation probability on the star.
3. Comment on the comparison.
```

(sec:programming_graph_dynamics)=

## Programming

The `ludics` library represents an evolutionary process as a finite-population
Markov chain and computes fixation probabilities exactly, rather than by
simulation. It implements the well-mixed Moran process directly, and its
transition-matrix builder accepts a custom update rule, just as we used it to add
the Wright–Fisher process in the
[learning and evolutionary dynamics](#chp:further_learning_dynamics) chapter.
Here we use that same mechanism to place the process on a graph.

### Placing the population on a graph

Each vertex holds one individual, whose strategy is recorded in a state ($0$ for
a textbook citer, $1$ for a preprint citer). A mutant preprint citer has fitness
$r$ and a resident textbook citer has fitness $1$, independent of the graph.

```{code-cell} python3
import networkx as nx
import numpy as np
import ludics

mutant_fitness, population_size = 3.0, 6


def constant_fitness(state, mutant_fitness, **kwargs):
    """Fitness of each vertex: a mutant (type 1) has fitness r, a resident
    (type 0) has fitness 1, independent of the graph."""
    return np.where(np.asarray(state) == 1, mutant_fitness, 1.0)
```

### A graph update rule as a custom dynamic

The Moran process built into `ludics` is well-mixed: any individual may replace
any other. On a graph the offspring of a parent can only replace a neighbour, so
we supply a custom Birth-Death rule. It receives a source state, a target state
differing in one vertex, the fitness function, and the graph, and returns the
probability of that one-vertex change: a parent is chosen across the whole
population in proportion to fitness, and replaces a uniformly chosen neighbour.

```{code-cell} python3
def graph_birth_death(source, target, fitness_function, graph, **kwargs):
    """Birth-Death on a graph: a parent is chosen across the whole population
    in proportion to fitness, and its offspring replaces a uniformly chosen
    neighbour."""
    source, target = np.asarray(source), np.asarray(target)
    changed = np.where(source != target)[0]
    if len(changed) > 1:
        return 0
    if len(changed) == 0:
        return None
    vertex, new_type = changed[0], target[changed[0]]
    fitness = fitness_function(source, **kwargs)
    total_fitness = fitness.sum()
    return sum(
        (fitness[parent] / total_fitness) / graph.degree(parent)
        for parent in graph.neighbors(vertex)
        if source[parent] == new_type
    )
```

### Reading off the fixation probability

`ludics` assembles the full transition matrix from the state space, the fitness
function, and our rule. The all-textbook and all-preprint states are absorbing,
and the fundamental matrix gives the exact probability that a single preprint
citer, placed at a uniformly random vertex, eventually takes over.

```{code-cell} python3
def fixation_probability(graph, mutant_fitness):
    """Exact fixation probability of a single mutant placed at a uniformly
    random vertex, averaged over the starting vertex."""
    state_space = ludics.get_state_space(N=graph.number_of_nodes(), k=2)
    transition_matrix = ludics.generate_transition_matrix(
        state_space, constant_fitness, graph_birth_death,
        graph=graph, mutant_fitness=mutant_fitness,
    )
    absorption = ludics.compute_absorption_matrix(transition_matrix)
    absorbing = np.where(np.isclose(np.diag(transition_matrix), 1.0))[0]
    transient = np.where(~np.isclose(np.diag(transition_matrix), 1.0))[0]
    all_mutant = next(
        column for column, state in enumerate(absorbing)
        if state_space[state].sum() == graph.number_of_nodes()
    )
    single_mutant = [
        row for row, state in enumerate(transient) if state_space[state].sum() == 1
    ]
    return float(np.mean(absorption[single_mutant, all_mutant]))
```

On the complete graph the fixation probability matches the well-mixed Moran value
$\rho = (1 - 1/r)/(1 - 1/r^{N})$ exactly, as the isothermal theorem predicts.

```{code-cell} python3
moran = (1 - 1 / mutant_fitness) / (1 - 1 / mutant_fitness**population_size)
complete = fixation_probability(nx.complete_graph(population_size), mutant_fitness)
print(f"Moran formula:  {moran:.3f}")
print(f"complete graph: {complete:.3f}")
```

On the star the fixation probability is higher: the star amplifies selection,
favouring the beneficial mutant beyond the well-mixed value.

```{code-cell} python3
star = fixation_probability(nx.star_graph(population_size - 1), mutant_fitness)
print(f"complete graph: {complete:.3f}")
print(f"star graph:     {star:.3f}")
```

```{note}
The Moran process and imitation rules in `ludics` are well-mixed by default. We
recover the graph by supplying a custom replacement rule to its
transition-matrix builder, exactly as the
[learning and evolutionary dynamics](#chp:further_learning_dynamics) chapter
added the Wright–Fisher process. Because the chain is small here ($2^{6} = 64$
states) we extract the fixation probability exactly from the fundamental matrix
rather than by simulation, so the amplification of the star is not a statistical
estimate but an exact consequence of the graph structure.
```

## Notable Research

Evolutionary graph theory was introduced by Lieberman, Hauert, and Nowak
[@lieberman2005evolutionary], who defined the Moran process on a graph, proved
the isothermal theorem, and identified amplifiers and suppressors of selection,
showing that the star and related structures can sharply increase the fixation
probability of advantageous mutants.

The study of cooperation on graphs was transformed by Ohtsuki, Hauert,
Lieberman, and Nowak [@ohtsuki2006simple], whose $b/c > k$ rule gave a strikingly
simple condition for structure to favour cooperation. The result was later
placed on a rigorous and general footing by Allen and co-authors
[@allen2017evolutionary], who derived the condition for cooperation on any
weighted graph in terms of coalescence times of random walks, and applied it to
empirical social networks.

This body of work connects directly to the [Moran Process](#chp:moran_process),
whose well-mixed analysis is the complete-graph special case, and to the broader
question of [learning and evolutionary dynamics](#chp:further_learning_dynamics),
since the choice of update rule, Birth-Death or Death-Birth, is exactly the
kind of modelling decision whose consequences that chapter explores.

## Conclusion

Placing a population on a graph reveals that the well-mixed assumption of the
[Moran Process](#chp:moran_process) and [replicator dynamics](#chp:replicator_dynamics)
is a special case, the complete graph, rather than the whole story. Structure
matters: by the **isothermal theorem** regular graphs leave the fixation
probability unchanged, but irregular graphs can **amplify** selection, as the
star does, or **suppress** it. The order of birth and death in the update rule
matters too, and under **Death-Birth** updating the **$b/c > k$ rule** shows
that sparse structure is precisely what allows cooperation to evolve.

[](#tbl:graph_dynamics_summary) summarises the concepts of this chapter.

```{table} Summary of evolutionary graph dynamics
:label: tbl:graph_dynamics_summary
:align: center
:class: table-bordered

| Concept | Description |
|---|---|
| Evolutionary graph | A population in which interaction follows the edges of a graph |
| Complete graph | The well-mixed population of the Moran process |
| Birth-Death / Death-Birth | The two update rules, differing in the order of reproduction and death |
| Isothermal theorem | Regular graphs share the well-mixed Moran fixation probability |
| Amplifier of selection | A graph (e.g. the star) that raises fixation of beneficial mutants |
| Suppressor of selection | A graph that pushes fixation towards the neutral value $1/N$ |
| $b/c > k$ rule | Cooperation is favoured under Death-Birth on a $k$-regular graph when $b/c > k$ |
```

```{important}
On a graph the well-mixed Moran process is recovered by the complete graph.
Departing from it, irregular structure amplifies or suppresses selection, and
sparse structure (small $k$) is what makes cooperation evolutionarily
favourable.
```

---

(solutions:graph_dynamics)=

## Solutions

```{solution} graph_isothermal_graphs
:label: solution:graph_isothermal_graphs

1. The cycle $C_N$ is $2$-regular: every vertex has exactly two neighbours. It
   is isothermal, so the fixation probability equals the well-mixed Moran value.

2. The path $P_N$ is not regular: the two endpoints have degree $1$ while the
   interior vertices have degree $2$. It is not isothermal, so the fixation
   probability can differ from the Moran value.

3. The star $K_{1, N-1}$ is not regular: the centre has degree $N - 1$ and each
   leaf has degree $1$. It is not isothermal; indeed it is an amplifier of
   selection.

4. The complete graph $K_N$ is $(N-1)$-regular and therefore isothermal. This is
   the well-mixed population, so the fixation probability is the Moran value by
   definition.
```

```{solution} graph_neutral_fixation
:label: solution:graph_neutral_fixation

Under neutral drift every individual has the same fitness, so reproduction is
independent of type. The process eventually fixes on a single ancestral lineage:
all $N$ individuals are ultimately descended from exactly one of the original $N$
vertices, and by symmetry each vertex is equally likely to be that common
ancestor, with probability $1/N$.

The mutant fixes precisely when the single vertex it occupies is the eventual
common ancestor. Since the mutant is placed at a uniformly random vertex, this
happens with probability $1/N$, regardless of the structure of the graph.
```

```{solution} graph_bc_rule_application
:label: solution:graph_bc_rule_application

Cooperation is favoured under Death-Birth updating on a $k$-regular graph
exactly when $b/c > k$.

1. On the ring, $k = 2$ and $b/c = 3/1 = 3 > 2$, so cooperation **is** favoured.

2. On the $6$-regular network, $b/c = 5/1 = 5 < 6$, so cooperation is **not**
   favoured.

3. With $b = 9$ and $c = 2$, $b/c = 4.5$. Cooperation is favoured when
   $k < 4.5$, so the largest integer degree is $k = 4$.
```

```{solution} graph_amplifier_comparison
:label: solution:graph_amplifier_comparison

1. With $r = 2$ and $N = 10$ the well-mixed Moran fixation probability is

   $$
   \rho = \frac{1 - 1/2}{1 - 1/2^{10}} = \frac{0.5}{1 - 1/1024}
   \approx 0.5005.
   $$

2. Replacing $r$ by $r^{2} = 4$ in the same formula gives the star
   approximation

   $$
   \rho_{\text{star}} \approx \frac{1 - 1/4}{1 - 1/4^{10}}
   = \frac{0.75}{1 - 1/2^{20}} \approx 0.7500.
   $$

3. The star raises the fixation probability of the beneficial mutant from about
   $0.50$ to about $0.75$. Amplification makes a real difference: a mutant that
   was only marginally more likely than not to take over in the well-mixed
   population is now very likely to do so. The same mechanism would drive a
   deleterious mutant ($r < 1$) to fix less often than in the well-mixed case.
```
