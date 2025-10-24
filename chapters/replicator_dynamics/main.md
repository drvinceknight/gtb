---
kernelspec:
  name: python3
  display_name: "Python 3"
---

(chp:replicator_dynamics)=

# Replicator Dynamics

(sec:motivating_example)=

## Motivating Example: Coffee clubs and the common good game

Across a large university campus, students form informal coffee clubs. Each day,
students join clubs to share a cafetière of coffee and discuss algebraic
topology or the latest student gossip. There are three types of students:

- **Cooperators** always bring a scoop of ground coffee to the club.
- **Defectors** show up empty-handed but still drink the coffee.
- **Loners** prefer to skip clubs and enjoy a quiet cup alone — reliable, if
  a bit less exciting.

In each club, all coffee brought is pooled, brewed, and the resulting pot is
shared equally among the attendees. If there are $k$ cooperators, the pot yields
$rk$ units of value to be divided among all participants (cooperators and
defectors). The loners, who don’t attend clubs, receive a fixed payoff $\sigma$.

Let the total population be normalized to 1, with:

- $x_c$ the proportion of cooperators,
- $x_d$ the proportion of defectors,
- $x_z = 1 - x_c - x_d$ the proportion of loners.

Assuming the population is large and well-mixed, we can model the average
payoff to each strategy as:

- $f_c(x) = r \cdot \frac{x_c}{x_c + x_d} - 1$
- $f_d(x) = r \cdot \frac{x_c}{x_c + x_d}$
- $f_l(x) = \sigma$

Here, $r > 1$ is the return factor of the public good (coffee), and the
subtraction of 1 from $f_C$ reflects the cost of bringing coffee.

These payoffs are used in the **replicator dynamics equation**, which models
how the frequency of each strategy changes over time:

$$
\label{eqn:replicator_dynamics}
\dot{x}_i = x_i \left( f_i(x) - \phi \right)
$$

where $\phi$ is the population average payoff.

```{figure} ./images/replicator_dynamics_of_common_good_game/main.png
:alt: A simplex with the evolutionary trajectory of the underlying replicator dynamics equation
:label: fig:replicator_dynamics_of_common_good_game
:height: 250px

A diagram showing the direction of the derivative as given by [](#eqn:replicator_dynamics) for $r=3$ and $\sigma=.6$.
```

Strategies that do better than the average will increase in frequency;
those that do worse will decline. This feedback mechanism drives the
evolution of behavior in the population — capturing the shifting fortunes
of cooperators, defectors, and loners on campus.

As we will see, this system often exhibits **cyclical behavior**: when most
students cooperate, defectors thrive; when defection becomes too common,
students prefer to be loners; when clubs are small and rare, cooperation
becomes appealing again. These cycles — and their stability — are precisely
what replicator dynamics helps us understand.

## Theory

### Definition: Replicator Dynamics Equation

Consider a population with $N$ types of individuals. Let $x_i$ denote the
proportion of individuals of type $i$, so that $\sum_{i=1}^N x_i = 1$.

Suppose the fitness of an individual of type $i$ depends on the state of the
entire population, through a population-dependent fitness function $f_i(x)$.

The replicator dynamics equation is given by:

$$
\frac{dx_i}{dt} = x_i(f_i(x) - \phi) \quad \text{for all } i
$$

where the average population fitness $\phi$ is defined as:

$$
\phi = \sum_{i=1}^N x_i f_i(x)
$$

This equation describes the change in frequency of each type as proportional to
how much better (or worse) its fitness is compared to the population average.

### Example: The common good game

In the [common good game](#sec:motivating_example) around coffee clubs the
replicator dynamics equation can be written as:

$$
\begin{align*}
\dot{x}_c &= x_c\left(\frac{rx_c}{x_c + x_d} - 1 - \phi\right)\\
\dot{x}_d &= x_d\left(\frac{rx_c}{x_c + x_d} - \phi\right)\\
\dot{x}_l &= x_l\left(\sigma - \phi\right)\\
\end{align*}
$$

where:

$$
\begin{align*}
\phi &= x_c \left(\frac{rx_c}{x_c + x_d} - 1\right) + x_d \left(\frac{rx_c}{x_c + x_d}\right) + x_l\sigma\\
     &= \frac{rx_c^2}{x_c + c_d} - x_c + \frac{rx_cx_d}{x_c + x_d} + x_l\sigma\\
     &= \frac{rx_c^2 - x_c(x_c+x_d) + rx_cx_d + x_l\sigma(x_c + x_d)}{x_c + c_d}\\
     &= \frac{rx_c(x_c + x_d) - x_c(x_c+x_d) + x_l\sigma(x_c + x_d)}{x_c + c_d}\\
     &= \frac{(x_c + x_d)\left(rx_c - x_c + x_l\sigma\right)}{x_c + c_d}\\
     &= x_c(r - 1) + x_l\sigma
\end{align*}
$$

(sec:definition_stable_population)=

### Definition: Stable Population

---

For a given population game with $N$ types of individuals and fitness functions
$f_i$ a stable population $\tilde x$ is one for which $\dot x_i=0$ for
all $i$.

---

For a stable population $\tilde x_i$:

$$
\dot{x}_i = \tilde x_i(f_i(\tilde x_i) - \phi) = 0
$$

so either: $\tilde x_i=0$ or $f_i(\tilde x_i) - \phi$.

### Example: No interior point stable population in the common goods game

For
the [common good game](#sec:motivating_example) around coffee clubs we have some
immediate stable populations:

- $x=(x_c, x_d, x_l) = (0, 0, 1)$: indeed $\dot x_c = \dot x_d = 0$ so that
  $\phi=\sigma$ and so $\dot x_l = 0$.
- $x=(x_c, x_d, x_l) = (0, 1, 0)$: indeed $\dot x_d = \dot x_l = 0$ so that
  $\phi=f_d(x)=0$ and so $\dot x_d = 0$.
- $x=(x_c, x_d, x_l) = (1, 0, 0)$: indeed $\dot x_d = \dot x_l = 0$ so that
  $\phi=f_c(x)=0$ and so $\dot x_c = 0$.

A question remains, is there a point in the interior of the simplex of [](#fig:replicator_dynamics_of_common_good_game) that is stable?
Such a point has $x_c>0$, $x_d>0$ and $x_l > 0$ which implies:

$$
f_c(x) = f_d(x) = f_l(x)
$$

This is not possible as: $f_c(x) = f_d(x) - 1$ for all
$x$.

### Definition: Fitness of a strategy in a population

In a population with $N$ types
let $f(y, x)$ denote the fitness of an individual playing strategy $y$ in a
population $x$:

$$
f(y, x) = \sum_{i=1}^Ny_if_i(x)
$$

### Example: A new student in the Common Goods Game

For
the [common good game](#sec:motivating_example)
if we consider a stable population $x=(0, 1, 0)$ where everyone is defecting and
assume that a new student enters planning to cooperate 50% of the time and
defect 50% of the time, their fitness is given by:

$$
f((1/2, 1/2, 0), (0, 1, 0)) = 1/2 f_c(0, 1, 0) + 1/2f_d(0, 1, 0) = 1/2(1/2 - 1)
+ 1/2\dot1/2 = 0
$$

### Definition: Post Entry Population

For a population with $N$ types of individuals
Given a population $x \in \mathbb{R}^N_{[0, 1]}$ (with $\sum_{i=1}^Nx_i=1$), some $\epsilon>0$ and
a strategy $y \in \mathbb{R}^N_{[0, 1]}$ (with $\sum_{i=1}^Nx_i=1$), the post entry population $x_{\epsilon}$ is given by:

$$
x_{\epsilon} = x + \epsilon(y - x)
$$

### Example: Post Entry Population for the Common Goods Game

For
the [common good game](#sec:motivating_example)
if we consider the **stable** population $x=(0, 1, 0)$ where everyone is
defecting and assume that a new student enters the population planning to
cooperate with a coffee club 50% of the time and defect 50% of the time the post
entry population will be:

$$
x_{\epsilon} = (0, 1, 0) + \epsilon((1/2, 1/2, 0) - (0, 1, 0)) = (0, 1, 0) + (\epsilon/2, -\epsilon/2, 0) = (\epsilon / 2, 1 - \epsilon / 2, 0)
$$

```{note}
Note that for an infinitely large population a single student is represented by
an infinitesimal amount $\epsilon$.
```

What is of interest in the field of evolutionary game theory is what happens to the post
entry population: does this new student change the stability of the system or is
the system going to go back to all students defecting?

(sec:definition_of_evolutionary_stable_strategy)=

### Definition: Evolutionary Stable Strategy

A strategy $x^*$ is an evolutionarily stable strategy if for all $x_{\epsilon} \neq x^*$ sufficiently close to $x^*$:

$$
\label{eqn:ess_constraint}
f(x^*, x^*) > f(x_{\epsilon}, x^*)
$$

In practice _sufficiently close_ implies that there exists some $\bar\epsilon$ such
that for all $y \neq x^*$ and for all $0 < \epsilon < \bar\epsilon$ the post entry population $x_{\epsilon} = x + \epsilon(y - x)$
satisfies [](#eqn:ess_constraint).

### Example: Are Loners Evolutionarily Stable in the Common Goods Game

For
the [common good game](#sec:motivating_example) we have seen that a population
$x^*=(0, 0, 1)$ where everyone is a longer is stable. Let us check if it is
evolutionarily stable.

We have:

$$
f(x^*, x^*) = \sigma
$$

Now to calculate the right hand side of [](#eqn:ess_constraint):

$$
\begin{align*}
f(x_{\epsilon}, x^*) &= {x_\epsilon}_{c}f_c(x^*) + {x_\epsilon}_{d}f_d(x^*) + {x_\epsilon}_{l}f_l(x^*)\\
                     &= {x_\epsilon}_{c}(-1) + {x_\epsilon}_{d}(0) + {x_\epsilon}_{l}\sigma\\
                     &= {x_\epsilon}_{c}(-1) + {x_\epsilon}_{l}f(x^*, x^*)\\
\end{align*}
$$

which is strictly less than $f(x^*, x^*)=\sigma$ unless ${x_{\epsilon}}_c=0$
which it cannot as $x_{\epsilon}\ne x^*$.

(sec:definition_of_pairwise_interaction_game)=

### Definition: Pairwise Interaction Game

---

Given a population of $N$ types of individuals and
a payoff matrix $M^{n\times n}$ a pairwise interaction game is a
game where the fitness is $f_i(x)$ is given by:

$$
\label{eqn:fitness_for_pairwise_interaction_game}
f_i(x) = \sum_{j=1}^{N}x_jM_{ij}
$$

---

This corresponds to a population where all individuals interact with all other
individuals in the population and obtain a fitness given by the matrix $M$.

Note that there is a linear algebraic equivalent to [](#eqn:fitness_for_pairwise_interaction_game):

$$
f = xM
$$

and then:

$$
\phi = x f
$$

### Example: The Hawk Dove Game

Consider a population of animals. These animals, when they interact, will
always share their food. Due to a genetic mutation, some of these animals may
act in an aggressive manner and not share their food. If two aggressive animals
meet, they both compete and end up with no food. If an aggressive animal meets a
sharing one, the aggressive one will take most of the food.

These interactions can be represented using the matrix $A$:

$$
M = \begin{pmatrix}
    2 & 1\\
    3 & 0
\end{pmatrix}
$$

In this scenario: what is the likely long-term effect of the genetic mutation?

Over time will:

- The population resist the mutation and all the animals continue to share their
  food.
- The population get taken over by the mutation and all animals become
  aggressive.
- A mix of animals are present in the population: some act aggressively and some
  share.

To answer this question, we will model it as a pairwise interaction game with $x\in\mathbb{R}_{[0, 1]}^2$
representing the population distribution. In this case:

- $x_1$ represents the proportion of the population that shares.
- $x_2$ represents the proportion of the population that acts aggressively.

In this case, the replicator dynamics equation becomes:

$$
\begin{align*}
    \frac{dx_1}{dt} &= x_1(2x_1 + x_2 - \phi) \\
    \frac{dx_2}{dt} &= x_2(3x_1 - \phi)
\end{align*}
$$

$$
\phi = x_1(2x_1 + x_2) + x_2(3x_1)
$$

Note that $x_2 = 1 - x_1$ so for simplicity of notation we will only use $x$ to
represent the proportion of the population that shares.

Thus we can write the single differential equation:

$$
\label{eqn:replicator_dynamics_equation_for_hawk_dove}
\begin{align*}
\frac{dx}{dt} &= x (2x + (1 - x) - \phi)\\
              &= x (2x + (1 - x) - x(2x + (1-x)) - (1 - x)(3x))\\
              &= x (2x^2-3x+1)\\
              &= x(x -1)(2x-1)
\end{align*}
$$

We see that there are 3 [stable populations](#sec:definition_stable_population):

- $x=0$: No sharers
- $x=1$: Only sharers
- $x=1/2$: A mix of both sharers and aggressive individuals.

This differential equation can then be
solved numerically, for example using [Euler's Method](#app:numerical_integration)
to show the evolution of

Let us do this with a step size $h=.05$ and an initial population of $x=3/5$:

Recall, we use the update rule:

$$
x_{n+1} = x_n + h \cdot f(x_n)
$$

to give [](#tbl:euler_method_on_hawk_dove_with_x_3_over_5).

```{table} Step by step application of Euler's method to the Hawk Dove game with step size $h=.1$ and $x_0=3/5$.
:name: tbl:euler_method_on_hawk_dove_with_x_3_over_5
:align: center

| $n$ | $t_n$ | $x_n$ | $f(x_n)$ | $x_{n+1}$ |
| --: | ----: | ----: | -------: | --------: |
|   0 |   0.0 | 0.600 |   -0.048 |     0.595 |
|   1 |   0.1 | 0.595 |   -0.046 |     0.591 |
|   2 |   0.2 | 0.591 |   -0.044 |     0.586 |
|   3 |   0.3 | 0.586 |   -0.042 |     0.582 |
|   4 |   0.4 | 0.582 |   -0.040 |     0.578 |
|   5 |   0.5 | 0.578 |   -0.038 |     0.574 |
|   6 |   0.6 | 0.574 |   -0.036 |     0.571 |
|   7 |   0.7 | 0.571 |   -0.035 |     0.567 |
|   8 |   0.8 | 0.567 |   -0.033 |     0.564 |
|   9 |   0.9 | 0.564 |   -0.031 |     0.561 |
|  10 |   1.0 | 0.561 |   -0.030 |     0.558 |
```

If we repeat this with $x=2/5$ we obtain
[](#tbl:euler_method_on_hawk_dove_with_x_2_over_5).

```{table} Step by step application of Euler's method to the Hawk Dove game with step size $h=.1$ and $x_0=2/5$.
:name: tbl:euler_method_on_hawk_dove_with_x_2_over_5
:align: center

| $n$  | $t_n$ | $x_n$  | $f(x_n)$ | $x_{n+1}$ |
|-----:|------:|-------:|---------:|----------:|
| 0    | 0.0   | 0.400  | 0.048    | 0.405     |
| 1    | 0.1   | 0.405  | 0.046    | 0.409     |
| 2    | 0.2   | 0.409  | 0.044    | 0.414     |
| 3    | 0.3   | 0.414  | 0.042    | 0.418     |
| 4    | 0.4   | 0.418  | 0.040    | 0.422     |
| 5    | 0.5   | 0.422  | 0.038    | 0.426     |
| 6    | 0.6   | 0.426  | 0.036    | 0.429     |
| 7    | 0.7   | 0.429  | 0.035    | 0.433     |
| 8    | 0.8   | 0.433  | 0.033    | 0.436     |
| 9    | 0.9   | 0.436  | 0.031    | 0.439     |
| 10   | 1.0   | 0.439  | 0.030    | 0.442     |
```

It looks the population is converging to the population which has a mix
of both sharers and aggressive types: $x=1/2$. [](#fig:replicator_dynamics_of_hawk_dove_game) confirms this.

```{figure} ./images/replicator_dynamics_of_hawk_dove_game/main.png
:alt: A plot of two lines, one starting at 3/5 and the other at 2/5. The lines slowly converge to 1/2.
:label: fig:replicator_dynamics_of_hawk_dove_game
:height: 250px

The numerical integration of the differential equation [](#eqn:replicator_dynamics_equation_for_hawk_dove) with two different initial values of $x$.
```

This indicates that $x=1/2$ is an evolutionary stable strategy. To confirm this
we could repeat calculations using the [definition of an evolutionary stable
strategy](#sec:definition_of_evolutionary_stable_strategy) however for pairwise
interaction games there is a theoretic result that can be used instead.

### Theorem: Characterisation of ESS in two-player games

---

Let $\sigma^*$ be a strategy in a symmetric two-player game (so that $M_r=M_c^{\top}$). Then $\sigma^*$ is
an evolutionarily stable strategy (ESS) if and only if, for all $\sigma \ne \sigma^*$,
one of the following conditions holds:

1. $f(\sigma^*, \sigma^*) > f(\sigma, \sigma^*)$
2. $f(\sigma^*, \sigma^*) = f(\sigma, \sigma^*)$ and  
   $f(\sigma^*, \sigma) > f(\sigma, \sigma)$

Conversely, if either of the above conditions holds for all $\sigma \ne \sigma^*$,
then $\sigma^*$ is an ESS in the corresponding population game.

---

### Proof

---

Assume $\sigma^*$ is an ESS. Then, by definition, there exists
$\varepsilon > 0$ such that for all $\sigma \ne \sigma^*$ and all
$0 < \epsilon < \varepsilon$, we have:

$$
f(\sigma^*, \chi_\epsilon) > f(\sigma, \chi_\epsilon)
$$

where $\chi_\epsilon = (1 - \epsilon)\sigma^* + \epsilon \sigma$ is the
mixed population state. Substituting into the expected fitness, we obtain:

$$
(1 - \epsilon) f(\sigma^*, \sigma^*) + \epsilon f(\sigma^*, \sigma) >
(1 - \epsilon) f(\sigma, \sigma^*) + \epsilon f(\sigma, \sigma)
$$

Rearranging, this inequality holds for all sufficiently small $\epsilon > 0$
if either:

- $f(\sigma^*, \sigma^*) > f(\sigma, \sigma^*)$ (so the left-hand side is
  already greater); or
- $f(\sigma^*, \sigma^*) = f(\sigma, \sigma^*)$ but
  $f(\sigma^*, \sigma) > f(\sigma, \sigma)$, so the second-order term
  dominates as $\epsilon \to 0$.

For the converse, suppose neither condition holds. Then either:

- $f(\sigma^*, \sigma^*) < f(\sigma, \sigma^*)$, so for small $\epsilon$ the
  inequality fails and $\sigma^*$ is not stable, or
- $f(\sigma^*, \sigma^*) = f(\sigma, \sigma^*)$ and
  $f(\sigma^*, \sigma) \le f(\sigma, \sigma)$, in which case the right-hand
  side is at least as large as the left for small $\epsilon$, again
  contradicting stability.

Hence, the two conditions are necessary and sufficient for evolutionary
stability.

---

This theorem gives us a practical method for identifying ESS:

1. Construct the associated symmetric two-player game.
2. Identify all symmetric Nash equilibria of the game.
3. For each symmetric Nash equilibrium, test the two conditions above.

Note that the first condition is very close to the condition for a strict
Nash equilibrium, while the second adds a refinement that removes certain
non-strict symmetric equilibria. This distinction is especially important
when considering equilibria in strategies.

---

### Example: Evolutionary stability in the Hawk-Dove game

Let us consider the **Hawk-Dove** game. The associated symmetric two-player game
can be written in a general form. Let $v$ denote the value of the resource and $c$ the cost of conflict
with $v < c$.

Row player's payoff matrix:

$$
A =
\begin{pmatrix}
\frac{v-c}{2} & v \\
0 & \frac{v}{2}
\end{pmatrix}
$$

Column player's payoff matrix:

$$
B =
\begin{pmatrix}
\frac{v-c}{2} & 0 \\
v & \frac{v}{2}
\end{pmatrix}
$$

To find symmetric Nash equilibria, we apply the support enumeration algorithm:

$$
\begin{aligned}
f(\sigma^*, H) &= f(\sigma^*, D) \\
q^* &= \frac{v}{c}
\end{aligned}
$$

This gives

$$\sigma^* = \left(\frac{v}{c}, 1 - \frac{v}{c}\right)$$

where individuals are aggressive with probability $\frac{v}{c}$ and share
otherwise.

To determine whether this strategy is evolutionarily stable, we check the
conditions of the characterisation theorem.

**Crucially**, because $f(\sigma^*, \sigma^*) = f(\sigma^*, \text{Aggressive}) =
f(\sigma^*, \text{Sharing})$, the **first condition** does _not_ hold. We must
therefore verify the **second condition**:

$$
f(\sigma^*, \sigma) > f(\sigma, \sigma)
$$

Let $\sigma = (\omega, 1 - \omega)$ be an arbitrary strategy.
Then:

$$
f(\sigma^*, \sigma) = \frac{v}{c} \cdot \omega \cdot \frac{v - c}{2}
+ \frac{v}{c} \cdot (1 - \omega) \cdot v
+ \left(1 - \frac{v}{c} \right) \cdot (1 - \omega) \cdot \frac{v}{2}
$$

$$
f(\sigma, \sigma) = \omega^2 \cdot \frac{v - c}{2}
+ \omega(1 - \omega) \cdot v
+ (1 - \omega)^2 \cdot \frac{v}{2}
$$

Subtracting the two expressions gives:

$$
f(\sigma^*, \sigma) - f(\sigma, \sigma)
= \frac{c}{2} \left( \frac{v}{c} - \omega \right)^2 > 0
$$

This inequality is strictly satisfied for all $\omega \ne \frac{v}{c}$, so the
second condition holds and $\sigma^*$ is an evolutionarily stable strategy.

### Definition: Replicator Mutator Dynamics Equation

An extension of the replicator equation is to allow for mutation. In this
setting, reproduction is imperfect: individuals of a given type can give rise
to individuals of another type.

This process is represented by a matrix $Q$, where $Q_{ij}$ denotes the
probability that an individual of type $j$ is produced by an individual of type
$i$.

In this case, the replicator dynamics equation can be modified to yield the
**replicator-mutation equation**:

$$
\frac{dx_i}{dt} = \sum_{j=1}^N x_j f_j Q_{ji} - x_i \phi \quad \text{for all } i
$$

### Example: The Replicator Mutator Dynamics Equation for the Hawk Dove Game

Let there be
a 10% change that
aggressive individuals will produce sharing ones in which case the matrix $Q$ is given
by:

$$
Q = \begin{pmatrix}
        1 & 0\\
        1 / 10 & 9 / 10
   \end{pmatrix}
$$

### Example: Recovering the Replicator Dynamics Equation from the Replicator Mutator Dynamics Equation

Show that when $Q=I_N$ (the identity matrix of size $N$) then the replicator
dynamics equation corresponds to the replicator dynamics equation.

The replicator-mutation equation is:

$$
\frac{dx_i}{dt} = \sum_{j=1}^N x_j f_j Q_{ji} - x_i \phi \quad \text{for all } i
$$

As $Q = I_N$:

$$
Q_{ij} =
\begin{cases}
    1 & \text{if } i = j \\
    0 & \text{otherwise}
\end{cases}
$$

This gives:

$$
\begin{align*}
\frac{dx_i}{dt} &= x_i f_i Q_{ii} - x_i \phi \quad \text{for all } i && Q_{ij} = 0 \text{ for all } i \ne j \\
                &= x_i f_i - x_i \phi \quad \text{for all } i && Q_{ii} = 1 \\
                &= x_i (f_i - \phi) \quad \text{for all } i
\end{align*}
$$

### Definition: Asymmetric Replicator Dynamics Equation

---

A further extension of the replicator dynamics framework accounts for
populations divided into two distinct subsets. Individuals in the first
population are one of $M$ possible types, while those in the second
population are one of $N$ possible types.

This setting arises naturally in **asymmetric games**, where the roles of the
players differ and the strategy sets need not be the same (i.e., $M \ne N$). In
such cases, the standard replicator equation does not apply directly.

The **asymmetric replicator dynamics equations** describe the evolution of
strategy distributions $x$ and $y$ in each population:

$$
\frac{dx_i}{dt} = x_i\left((f_x)_i - \phi_x\right) \quad \text{for all } 1 \leq i \leq M
$$

$$
\frac{dy_j}{dt} = y_j\left((f_y)_j - \phi_y\right) \quad \text{for all } 1 \leq j \leq N
$$

Here:

- $(f_x)_i$ and $(f_y)_j$ are the expected fitnesses of type $i$ and $j$ in each
  population respectively,
- $\phi_x$ and $\phi_y$ denote the average fitnesses in the respective
  populations.

---

### Example: Tennis Serve and Return

In tennis, serving and receiving form an asymmetric interaction. The **server**
(row player) chooses one of two serves, while the **receiver** (column player)
chooses one of three possible return strategies.

> The server can deliver a **power** or **spin** serve. The receiver can either
> prepare for power, cover a wide spin, or take an early aggressive position.

This leads to an asymmetric game where the server has 2 strategies and the
receiver has 3. The game matrices are:

$$
M_r =
\begin{pmatrix}
3 & 1 & 2 \\
4 & 2 & 1
\end{pmatrix}
$$

$$
M_r =
\begin{pmatrix}
1 & 3 & 2 \\
0 & 2 & 4
\end{pmatrix}
$$

These matrices are based on the following assumptions:

- If the server uses a power serve ($r_1$) and the receiver prepares for it
  ($c_1$), the server has some success (payoff 3), but the receiver also does
  reasonably well (payoff 1).
- If the server tries spin ($r_2$) and the receiver is covering for it
  ($c_2$), the payoff is more balanced (2 for each).
- A mismatch, such as a power serve into a receiver expecting spin ($r_1$ vs
  $c_2$), favors the server more (payoff 1 vs 3).
- Conversely, if the receiver takes an early position and guesses right
  against spin ($r_2$ vs $c_3$), they gain a big advantage (payoff 1 vs 4).

Let $x = (x_1, x_2)$ be the strategy distribution of the server and
$y = (y_1, y_2, y_3)$ that of the receiver. The **asymmetric replicator
dynamics** for this game are:

$$
\frac{dx_i}{dt} = x_i\left((A y)_i - x^\top A y\right) \quad \text{for } 1 \leq i \leq 2
$$

$$
\frac{dy_j}{dt} = y_j\left((x^\top B)_j - x^\top B y\right) \quad \text{for } 1\leq j \leq 3
$$

[](#fig:asymmetric_replicator_dynamics_of_tennis) shows the numerical solutions
of these differential equations over time.

- Preparing for Power quickly dies out as a strategy;
- There is a cycle with the server changing between power and spin while the
  returner cycles between preparing for spin and taking an aggressive position.

```{figure} ./images/asymmetric_replicator_dynamics_of_tennis/main.png
:alt: Two plots showing the numerical solutions of the asymmetric replicator dynamics equation
:label: fig:asymmetric_replicator_dynamics_of_tennis
:height: 250px

Numerical solutions to the asymmetric replicator dynamics equation. Preparing
for power quickly dies out as a played strategy in the population. There is a
cycle of the 2 remaining strategies for the returner and for the server although
power remains the strategy player most often.
```

## Exercises

### Exercise: Stability from fitness functions

Consider a population with two types of individuals: $x = (x_1, x_2)$ such that
$x_1 + x_2 = 1$. Obtain all the stable populations for the system defined by the
following fitness functions:

1. $f_1(x) = x_1 - x_2 \qquad f_2(x) = x_2 - 2x_1$
2. $f_1(x) = x_1 x_2 - x_2 \qquad f_2(x) = x_2 - x_1 + \frac{1}{2}$
3. $f_1(x) = x_1^2 \qquad f_2(x) = x_2^2$

For each stable population, choose a nearby post-entry state and solve the
replicator dynamics equation numerically using Euler's method with step size
$h = 0.05$ for 10 steps, starting from $x = 3/5$.

---

### Exercise: Stable populations from payoff matrices

For the following games, obtain all the stable populations for the associated
pairwise interaction game:

1. $A = \begin{pmatrix} 2 & 4 \\ 5 & 3 \end{pmatrix}$
2. $A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$

---

### Exercise: Evolutionarily stable strategies in symmetric games

Consider the pairwise contest games defined by the following associated
two-player games. In each case, identify all **evolutionarily stable strategies
(ESS)**.

1.  $$
    M_r = \begin{pmatrix}
    2 & 4 \\
    5 & 1
    \end{pmatrix}
    \qquad
    M_c = \begin{pmatrix}
    2 & 5 \\
    4 & 1
    \end{pmatrix}
    $$

2.  $$
    M_r = \begin{pmatrix}
    1 & 0 \\
    0 & 1
    \end{pmatrix}
    \qquad
    M_c = \begin{pmatrix}
    1 & 0 \\
    0 & 1
    \end{pmatrix}
    $$

---

### Exercise: Typesetting conventions in a mathematics department

> In a mathematics department, researchers can choose to use one of two systems
> for typesetting their research papers: LaTeX or Word. We will refer to these
> two strategies as $L$ and $W$ respectively. A user of $W$ receives a basic
> utility of 1. As $L$ is more widely used by mathematicians outside the
> department and is generally considered the superior system, a user of $L$
> receives a basic utility of $\alpha > 1$. Since collaboration is common, it is
> beneficial for researchers to use the same system. If $\mu$ denotes the
> proportion of $L$ users, we define:

$$
u(L, \chi) = \alpha + 2\mu
$$

$$
u(W, \chi) = 1 + 2(1 - \mu)
$$

What are the evolutionarily stable strategies?

## Programming

In [](#app:numerical_integration), we introduce
general programming approaches for numerically solving differential equations.
These apply directly to the replicator dynamics equation. Here, we focus on
tools specifically tailored to population interaction games.

---

### Solving symmetric replicator dynamics

The `Nashpy` library provides built-in functionality for solving the replicator
dynamics equation in a
[pairwise interaction game](#sec:definition_of_pairwise_interaction_game).

Let us consider the classic **Rock–Paper–Scissors** game:

```{code-cell} python3
import nashpy as nash
import numpy as np

M_r = np.array([[0, 1, -1], [-1, 0, 1], [1, -1, 0]])
game = nash.Game(M_r)
```

We can compute the population trajectory from an initial distribution:

```{code-cell} python3
x0 = np.array([1 / 6, 1 / 6, 2 / 3])
timepoints = np.linspace(0, 10, 1500)
xs = game.replicator_dynamics(y0=x0, timepoints=timepoints).T
xs
```

To visualize the evolution of strategy frequencies over time:

```{code-cell} python3
import matplotlib.pyplot as plt

plt.figure()
plt.plot(xs.T)
plt.ylim(0, 1)
plt.legend(["$x_1$", "$x_2$", "$x_3$"])
plt.ylabel("Distribution")
plt.xlabel("Time")
```

### Plotting a simplex with ternary

The ternary library [@pythonternary] allows for plotting trajectories on a
simplex, ideal for representing three-component distributions that sum to one.

We can use it to plot the Rock–Paper–Scissors trajectory:

```{code-cell} python3
import ternary

figure, tax = ternary.figure(scale=1.0)
tax.boundary()
tax.gridlines(multiple=0.2, color="black")
# Plot the data
tax.plot(xs.T, linewidth=2.0, label="$x$")
tax.ticks(axis='lbr', multiple=0.2, linewidth=1, tick_formats="%.1f")
tax.legend()
tax.left_axis_label("Scissors")
tax.right_axis_label("Paper")
tax.bottom_axis_label("Rock")
tax.ax.axis('off')
tax.show()
```

### Solving Asymmetric Replicator dynamics

The Nashpy library also supports numerical solutions for the asymmetric
replicator dynamics equation.

```{code-cell} python3
M_r = np.array([[3, 1, 2], [4, 2, 1]])
M_c = np.array([[1, 3, 2], [0, 2, 4]])
game = nash.Game(M_r, M_c)

x0 = np.array([1/2, 1/2])
y0 = np.array([1/3, 1/3, 1/3])
timepoints = np.linspace(0, 20, 1000)

xs, ys = game.asymmetric_replicator_dynamics(x0=x0, y0=y0, timepoints=timepoints)
xs
```

The corresponding trajectory for the column player's strategy distribution:

```{code-cell} python3
ys
```

## Notable Research

The original conceptual idea of an **evolutionarily stable strategy (ESS)** was
formulated by Maynard Smith [@smith1973logic; @smith1982evolution]. Although
these works did not explicitly introduce the replicator dynamics equation, they
were foundational in connecting game theory with evolutionary biology.

The first formal presentation of the **replicator dynamics equation** appeared
in [@taylor1978evolutionary], which directly built upon Maynard Smith’s ESS
framework. This formulation was later extended to multi-player games in
[@palm1984evolutionary], and to **asymmetric populations** in
[@komarova2004].

Several influential applications of replicator dynamics have since emerged. For
example, [@komarova2001evolutionary] used replicator-mutator dynamics to model
the spread of grammatical structures in language populations. In the context of
cooperation, [@hilbe2013evolution] applied the model to study the evolution of
reactive strategies, while [@knight2024recognising] recently demonstrated how
extortionate strategies fail to persist under evolutionary pressure.

A particularly notable extension is found in [@weitz2016oscillating], where the
game itself changes dynamically depending on the population state. This
approach is especially relevant in modeling the **tragedy of the commons** and
other environmental feedback systems.

In [@lv2023evolution], a model similar to the one in
[Section: Motivating Example](#sec:motivating_example) is examined using both
replicator dynamics and a **discrete population model**. The latter is explored
in detail in [Chapter: Moran Process](#chp:moran_process). Remarkably, the
replicator dynamics equation emerges as the **infinite-population limit** of the
discrete model—a connection rigorously established in
[@traulsen2005coevolutionary].

## Conclusion

The replicator dynamics equation provides a powerful lens through which to study
strategy evolution in large populations. By linking the fitness of strategies to
their growth or decline in the population, it captures the essence of selection
and adaptation.

Throughout this chapter, we explored how replicator dynamics:

- arise naturally in settings like public goods provision (e.g., coffee clubs),
- describe population change in terms of differential equations,
- connect with the concept of **evolutionarily stable strategies (ESS)**,
- extend to incorporate mutation and asymmetry,
- and can be simulated and visualized with numerical methods and tools.

From modelling simple two-strategy contests to rich three-strategy dynamics on
a simplex, replicator dynamics offer an interpretable and analytically rich
framework for evolutionary game theory. Table [](#tbl:replicator_dynamics_summary)
gives a summary of the main concepts of this chapter.

```{table} Summary of key concepts in replicator dynamics.
:name: tbl:replicator_dynamics_summary
:align: center

| Concept                                | Description                                                                 |
|----------------------------------------|-----------------------------------------------------------------------------|
| Replicator Dynamics Equation           | Models strategy frequency change based on relative fitness                 |
| Average Population Fitness ($\phi$)    | Weighted average of individual fitnesses                                   |
| Stable Population                      | A distribution where no strategy's frequency changes over time             |
| Evolutionarily Stable Strategy (ESS)   | A stable strategy resistant to invasion by nearby alternatives             |
| Post Entry Population                  | Perturbed population after a rare mutant enters                            |
| Replicator-Mutator Equation            | Extension accounting for imperfect strategy transmission                   |
| Asymmetric Replicator Dynamics         | Models evolution in multi-population or role-asymmetric settings           |
| Pairwise Interaction Game              | Fitness determined by payoffs in repeated pairwise interactions            |

```

```{important}
A strategy grows when its fitness exceeds the population average — and declines otherwise.

This central insight, encoded in the replicator dynamics equation, allows us to
understand not just what equilibria exist, but how populations evolve
toward them (or cycle away from them) over time.
```
