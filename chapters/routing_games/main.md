---
kernelspec:
  name: python3
  display_name: "Python 3"
---

(chp:routing_games)=

# Routing Games

(sec:motivating_example_routing_delivery)=

## Motivating Example: Competing delivery companies

In a busy city, two rival delivery companies — **QuickShip** and **TurboExpress**
— operate daily distribution routes to deliver packages to the central business
district.

Each company starts from its own warehouse, located in different suburbs on
opposite sides of the city. Every morning, the companies dispatch their fleets
toward the central depot, but must decide how to route their vans:

- Each company can take its own **dedicated service road** to the depot.
- Alternatively, both companies can use a **shared ring road** that offers a
  faster connection, but becomes congested as total traffic increases.

The travel costs for each route depend on the level of congestion:

- For QuickShip (source $s_1$):

  - Dedicated service road cost: $c_{s_1}(x) = x^2$,
    where $x$ is the number of QuickShip vans using this road.

- For TurboExpress (source $s_2$):

  - Dedicated service road cost: $c_{s_2}(x) = \dfrac{3}{2}x$.

- For the shared ring road (available to both companies):
  - Shared road cost: $c_\text{shared}(x) = x$,
    where $x$ is the total number of vans from both companies using this route.

Each source has
a total demand of $r = 1 / 2$ units of traffic to send to the sink.

This is shown diagrammatically in
[](#fig:competing_delivery_companies_routing_game).

Each company decides independently how to distribute its fleet across the
available routes, aiming to minimise its own delivery costs. However, since the
shared road's cost depends on total usage, each company's decision affects the
other's outcome.

This setting creates a **routing game**, where decentralised decisions lead to
interdependent costs. We will analyse this scenario to explore the concept of
**Nash equilibrium** in network routing, and investigate how self-interested
routing can result in stable, but potentially inefficient, traffic patterns.

```{figure} ./images/competing_delivery_companies_routing_game/main.png
:alt: A routing game with 2 sources and 1 sink
:label: fig:competing_delivery_companies_routing_game
:width: 750px

The routes available to QuickShip and TurboExpress.
```

## Theory

### Definition: Routing Game

A **routing game** $(G,r,c)$ is defined on a graph $G=(V,E)$ with a defined set of sources
$s_i$ and sinks $t_i$. Each source-sink pair corresponds to a set of traffic
(also called a commodity) $r_i$ that must travel along the edges of $G$ from
$s_i$ to $t_i$.
Every edge $e$ of $G$ has associated to it a nonnegative, continuous and
nondecreasing cost function (also called latency function) $c_e$.

### Example: The Routing Game Representation of the Delivery Companies Game

For the routing game in [](#fig:competing_delivery_companies_routing_game):

- $G=(V, E)$ with $V=\{s_1, s_2, a, t\}$ and $E=\{(s_1, t), (s_1, a), (s_2, a), (s_2, t), (a, t)\}$
- $r_1=r_2=1/2$
- $c_{s_1, t}(x)=x^2, c_{s_2, t}(x)=3x/2, c_{a, t}(x)=x, c_{s_1, a}(x)=c_{s_2, a}=0$

### Definition: Set of Paths

For any given $(G,r,c)$ we denote by $\mathcal{P}_i$ the set of paths available to commodity $i$.

### Definition: Feasible Flow

On a routing game we define a flow $f$ as a vector representing the quantity of traffic along the
various paths, $f$ is a vector index by $\mathcal{P}$. Furthermore we call $f$ **feasible** if:

$$\sum_{P\in\mathcal{P}_i}f_P=r_i$$

### Example: Feasible Flows for the Delivery Companies Game

For the routing game in [](#fig:competing_delivery_companies_routing_game):

$$\mathcal{P}_1=\{(s_1,a,t),(s_1,t)\}$$

and

$$\mathcal{P}_2=\{(s_2,a,t),(s_2,t)\}$$

The set of all possible paths is denoted by $\mathcal{P}=\bigcup_{i}\mathcal{P}_i$.

### Definition: Cost function

For any routing game $(G,r,c)$ we define a **cost function** $C(f)$:

$$C(f)=\sum_{P\in\mathcal{P}}c_P(f_P)f_P$$

Where $c_P$ denotes the cost function of a particular path $P$: $c_P(x)=\sum_{e\in P}c_e(x)$.
Note that any flow $f$ induces a flow on edges:

$$f_e=\sum_{P\in\mathcal{P}\text{ if }e\in P}f_P$$

So we can re-write the cost function as:

$$C(f)=\sum_{e\in E}c_e(f_e)f_e$$

### Example: Cost function for the Delivery Companies Game

For the routing game in [](#fig:competing_delivery_companies_routing_game):

Let $f=(\alpha,1/2-\alpha,1/2-\beta,\beta)$ as shown in [](#fig:competing_delivery_companies_routing_game_with_flow_vector).

```{figure} ./images/competing_delivery_companies_routing_game_with_flow_vector/main.png
:alt: A routing game with 2 sources and 1 sink with the flow vector shown
:label: fig:competing_delivery_companies_routing_game_with_flow_vector
:width: 750px

The vector $f$ showing the flow on the game
```

The cost of $f(\alpha,1/2-\alpha,1/2-\beta,\beta)$ is given by:

$$
\begin{align*}
C(f)&=\alpha^2\times\alpha+3/2\beta\times\beta+(1-\alpha-\beta)\times(1-\alpha-\beta)\\
    &=\alpha^3+3/2\beta^2+\alpha^2 + 2\alpha\beta + \beta^2 - 2\alpha - 2\beta + 1
\end{align*}
$$

### Definition: Optimal Flow

For a routing game $(G,r,c)$ we define the optimal flow $f^*$ as the solution to the following optimisation problem:

Minimise $\sum_{e\in E}c_e(f_e)f_e$:

Subject to:

$$
\begin{align*}
\sum_{P\in\mathcal{P}_i}f_P&=r_i&&\text{for all }i\\
f_e&=\sum_{P\in\mathcal{P}\text{ if }e\in P}f_P&&\text{ for all }e\in E\\
f_P&\geq 0
\end{align*}
$$

### Example: Optimal Flow for the Delivery Companies Games

In [](#fig:competing_delivery_companies_routing_game_with_flow_vector)
this corresponds to:

Minimise $C(\alpha,\beta)=\alpha^3+3/2\beta^2+\alpha^2 + 2\alpha\beta + \beta^2 - 2\alpha - 2\beta + 1$:

Subject to:

$$
\begin{align*}
0&\leq\alpha\\
\alpha&\leq 1/2\\
0&\leq\beta\\
\beta&\leq1/2
\end{align*}
$$

A plot of $C(\alpha,\beta)$ is shown in
[](#fig:plot_of_cost_function_for_delivery_companies_game).

```{figure} ./images/plot_of_cost_function_for_delivery_companies_game/main.png
:alt: A 2 dimensional heatmap.
:label: fig:plot_of_cost_function_for_delivery_companies_game
:width: 750px

The plot of $(\alpha, \beta)$.
```

The minimal point looks to be near the right boundary of the square, although it
is unclear if it is on the boundary or not. It is in fact **not on the
boundary**
taking this fact as an assumption, identity the optimal flow using the
[Karush-Kuhn-Tucker conditions](#app:kkt_conditions).

Let us first define the Lagrangian:

$$\mathcal{L}(\alpha,\beta,\lambda)=C(\alpha,\beta)-\lambda_1\alpha-\lambda_2(\alpha-1/2)-\lambda_3\beta-\lambda_4\beta$$

If $f^*$ is the minimal point then the complementary
slackness implies that $\lambda_i=0$ for all $i$, since this point does not sit
on any boundary which would make the corresponding constraint function
$g_i(f^*)=0$.

Thus:

$$\mathcal{L}(\alpha,\beta,\lambda)=C(\alpha,\beta)$$

We note that the feasiblity constraints all hold for $f^*$ so we are left to
check stationarity:

$$\frac{\partial \mathcal{L}}{\partial \alpha}=\frac{\partial C}{\partial \alpha}=3\alpha^2-2(1-\alpha-\beta)=0$$
and
$$\frac{\partial \mathcal{L}}{\partial \alpha}=\frac{\partial C}{\partial \beta}=3\beta-2(1-\alpha-\beta)=0$$

which gives:

$$
\label{eqn:beta_as_a_function_of_alpha}
\beta=\frac{2(1-\alpha)}{5}
$$

Substituting this in to the first equation gives:

$$3\alpha^2-6/5(1-\alpha)=0$$

which has solutions:

$$\left\{- \frac{1}{5} - \frac{\sqrt{11}}{5}, - \frac{\sqrt{11}}{5} + \frac{1}{5}\right\}$$

Only one of those is positive satisfying the constraints, substituting it in to
[](#eqn:beta_as_a_function_of_alpha) gives:

$$\beta=\frac{12}{25} - \frac{2 \sqrt{11}}{25}$$

thus the optimal flow is:

$$
f^* = \left(- \frac{\sqrt{11}}{5} + \frac{1}{5}, \frac{12}{25} - \frac{2 \sqrt{11}}{25}\right)
$$

If we take a closer look at $f^*$ in our example, we see that traffic from the first commodity travels
across two paths: $(s_1, t)$ and $(s_1, a, t)$. The cost along the first path is given by:

$$C_{s_1, t}(f^*)=\frac{12}{25} - \frac{2 \sqrt{11}}{25}\approx.2146$$

The cost along the second path is given by:

$$C_{s_1, a, t}(f^*)=\frac{18}{25} - \frac{3 \sqrt{11}}{25}\approx .3220$$

Thus traffic going along the second path is experiencing a higher cost. In
practice, they would deviate some of their traffic from the second path to the
first.

This leads to the definition of a Nash flow.

### Definition: Nash Flow

For a routing game $(G,r,c)$ a flow $\tilde f$ is called a **Nash flow**
if and only if for every commodity $i$ and any two paths
$P_1,P_2\in\mathcal{P}\_i$ such that $f\_{P_1}>0$ then:

$$c_{P_1}(f)\leq c_{P_2}(f)$$

A Nash flow ensures that all used paths have minimal costs.

### Example: Nash Flow for Delivery companies game

For [](#fig:competing_delivery_companies_routing_game_with_flow_vector) if we assume that both commodities use
all paths available to them:

$$
\begin{aligned}
\alpha^2&=1-\alpha-\beta\\
\frac{3\beta}{2}&=1-\alpha-\beta
\end{aligned}
$$

Solving this gives: $\beta=\frac{2}{5}(1-\alpha)$ $\Rightarrow$ $x^{2} + \frac{3}{5} x - \frac{3}{5}$
this gives

$$
\left\{- \frac{3}{10} - \frac{\sqrt{69}}{10}, - \frac{\sqrt{69}}{10} + \frac{3}{10}\right\}
$$

Neither of these two values are within our region thus there is no Nash flow
where all paths are used.

Let us assume that $\alpha=1/2$ (i.e. commodity 1 does not use $P_{s_1, a, t}$).
Assuming that the second commodity uses both available paths we have:

$$\frac{3}{2}\beta=\frac{1}{2}-\beta\Rightarrow\beta=\frac{1}{5}$$

Thus we have $\tilde f=(1/2,1/5)$ which gives a cost of $C(\tilde f)=11/40$ which is higher than the optimal cost!

What if we had assumed that $\beta=1/2$?

This would have given $\alpha^2=1/2-\alpha$ which has
solutions:

$$
\left\{- \frac{1}{2} + \frac{\sqrt{3}}{2}, - \frac{\sqrt{3}}{2} - \frac{1}{2}\right\}
$$

Taking the second value for $\alpha$ which does lie in the feasible region.
The cost of the path $P_{s_2, a, t}$ is then approximately $.134$ however the cost of the path $P_{s_2, t}$
is approximately $.75$ thus the second commodity should deviate.
We can carry out these same checks with all other possibilities to verify that $\tilde f=(1/2,1/5)$ is a Nash flow.

### Definition: Potential Function

Given a routing game $(G,r,c)$ we define the **potential function** of a flow as:

$$\Phi(f)=\sum_{e\in E}\int_0^{f_e}c_e(x)dx$$

### Example: Potential Function for the delivery company game

The potential function for [](#fig:competing_delivery_companies_routing_game_with_flow_vector) is given by:

$$
\begin{align*}
\Phi((\alpha,\beta))&=\int_0^{\alpha}x^2dx + \int_0^{1-\alpha - \beta}xdx + \int_0^{\beta}3/2xdx\\
                    &=\frac{\alpha^3}{3}+\frac{3\beta^2}{4}+\frac{(1-\alpha-\beta)^2}{2}
\end{align*}
$$

(thrm:nash_flow_minimises_the_potential_function)=

### Theorem: Nash Flow minimises the potential function

A feasible flow $\tilde f$ is a Nash flow for the routing game $(G,r,c)$ if and only if it is a minima for $\Phi(f)$.

### Definition: Marginal Cost

If $c$ is a differentiable cost function then we define the **marginal cost** function $c^*$ as:

$$c^*=\frac{d}{dx}(xc(x)$$

### Example: The marginal costs for the delivery company game

The marginal costs for [](#fig:competing_delivery_companies_routing_game_with_flow_vector) are given by:

$c^*_{s_1, t}(x)=3x^2, c_{s_2, t}(x)=3x, c_{a, t}(x)=2x, c_{s_1, a}(x)=c_{s_2, a}=0$

The corresponding routing game $(G, r, c^*)$ is shown in [](#fig:competing_delivery_companies_routing_game_with_marginal_costs).

```{figure} ./images/competing_delivery_companies_routing_game_with_marginal_costs/main.png
:alt: A routing game with 2 sources and 1 sink
:label: fig:competing_delivery_companies_routing_game_with_marginal_costs
:width: 750px

The routes available to QuickShip and TurboExpress with marginal costs instead
of costs.
```

(thrm:optimal_flow_is_a_nash_for_for_marginal_costs)=

### Theorem: Optimal Flow is a Nash Flow for Marginal Costs

A feasible flow $f^*$ is an optimal flow for $(G,r,c)$ if and only if $f^*$ is a Nash flow for $(G,r,c^*)$.

## Exercises

(sec:exercise_braess_s_paradox)=

### Exercise: Braess's Paradox

Determine the optimal and Nash flows for the routing games shown in
[](#fig:braesss_paradox_without_super_road) and
[](#fig:braesss_paradox).

```{figure} ./images/braesss_paradox_without_super_road/main.png
:alt: A routing game with two available paths
:label: fig:braesss_paradox_without_super_road
:width: 750px

A routing game forming the basis of Braess's paradox
```

```{figure} ./images/braesss_paradox/main.png
:alt: A routing game with two vailable paths and a super path between them
:label: fig:braesss_paradox
:width: 750px

A routing game known as Braess's paradox.
```

### Exercise: Nash flow via potential minimisation

Use [](#thrm:nash_flow_minimises_the_potential_function) and [](#app:kkt_conditions) to verify that
$\tilde f=(1/2,1/5)$ is a Nash flow for [](#fig:competing_delivery_companies_routing_game_with_flow_vector).

### Nash flow from marginal cost formulation

Use [](#thrm:optimal_flow_is_a_nash_for_for_marginal_costs) to confirm that

$$
f=\left(- \frac{\sqrt{11}}{5} + \frac{1}{5}, \frac{12}{25} - \frac{2 \sqrt{11}}{25}\right)
$$

is a Nash flow for [](#fig:competing_delivery_companies_routing_game_with_flow_vector).

## Programming

Scipy has functionality for optimising function within certain boundaries,
thanks to [](#thrm:nash_flow_minimises_the_potential_function) this can be used to find not only optimal flows but also Nash
flows.

In [](#app:kkt_conditions) is an example showing how to use Scipy to optimise a
function. Here is another one:

```{code-cell} python3
import numpy as np
import scipy.optimize

def objective(f):
    alpha, beta = f
    return alpha ** 3 / 3 + 3 * beta ** 2 / 4 + (1 - alpha - beta) ** 2 / 2

def g_1(f):
    return f[0]

def g_2(f):
    return f[1]

def g_3(f):
    return 1 / 2 - f[0]

def g_4(f):
    return 1 / 2 - f[1]

constraints = [
    {'type': 'ineq', 'fun': g_1},
    {'type': 'ineq', 'fun': g_2},
    {'type': 'ineq', 'fun': g_3},
    {'type': 'ineq', 'fun': g_4},
]

res = scipy.optimize.minimize(objective, [0, 0], constraints=constraints)
res
```

### Notable Research

The original paper introducing the notion of Nash flows is
[@wardrop1952correspondence]. An important phenomenon in this field is
[Braess's Paradox](#sec:exercise_braess_s_paradox), first described in
[@braess1968paradoxon], which shows that adding capacity to a network can
paradoxically increase overall congestion. This effect is not purely theoretical
and has been observed in real-world settings [@steinberg1983prevalence;
@youn2008price].

The inefficiencies that arise in congestion networks due to self-interested
behaviour have led to the concept of the **Price of Anarchy**, defined as
$C(\tilde f)/C(f^*)$. This concept was introduced in [@roughgarden2002bad].
Various applications have been explored, including [@knight2013selfish], which
studied the inefficiencies caused by patients selecting hospitals based on
individual preferences.

### Conclusion

In this chapter, we introduced **routing games**, where self-interested agents
choose paths through a network to minimize their own travel costs. These
individual decisions create congestion effects, making costs interdependent and
leading to potentially inefficient outcomes.

We developed a formal framework for routing games, introduced the key concepts
of feasible flow, optimal flow, and Nash flow, and explored how potential
functions allow us to compute Nash flows via standard optimisation techniques.
We also introduced the concept of marginal costs, leading to the result that
optimal flows correspond to Nash flows in a modified game with marginal cost
functions.

[](#tbl:routing_games) summarises the key concepts introduced in this
chapter.

```{table} Summary of routing games
:name: tbl:routing_games
:align: center

| Concept                  | Definition                                                                  |
| ------------------------ | --------------------------------------------------------------------------- |
| Feasible Flow            | Any flow satisfying demand and non-negativity constraints                   |
| Optimal Flow ($f^*$)  | Flow minimizing the total system cost \$C(f)\$                              |
| Nash Flow ($\tilde f$) | Flow where no player can reduce their cost by unilaterally switching routes |
| Potential Function       | $\Phi(f)=\sum_{e\in E}\int_0^{f_e} c_e(x) dx$                            |
| Marginal Cost            | $c^*(x) = \frac{d}{dx}(x c(x))$                                          |
```

```{important}
In routing games, individual rationality does not guarantee
system-wide efficiency. Tools like potential functions and marginal costs
provide powerful methods to identify Nash and Optimal flows in
decentralized network systems.
```
