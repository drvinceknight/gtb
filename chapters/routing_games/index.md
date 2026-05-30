---
kernelspec:
  name: python3
  display_name: "Python 3"
---

(chp:routing_games)=

# Routing Games

Selfish agents choosing routes through a shared network rarely produce the
socially optimal outcome. This chapter studies routing games and the Price of
Anarchy, quantifying how much individual optimisation can degrade collective
performance.

(sec:motivating_example_routing_delivery)=

## Motivating Example: Competing delivery companies

In a busy city, two rival delivery companies, **QuickShip** and **TurboExpress**,
operate daily distribution routes to deliver packages to the central business
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

#### Example: The Routing Game Representation of the Delivery Companies Game

For the routing game in [](#fig:competing_delivery_companies_routing_game):

- $G=(V, E)$ with $V=\{s_1, s_2, a, t\}$ and $E=\{(s_1, t), (s_1, a), (s_2, a), (s_2, t), (a, t)\}$
- $r_1=r_2=1/2$
- $c_{s_1, t}(x)=x^2, c_{s_2, t}(x)=3x/2, c_{a, t}(x)=x, c_{s_1, a}(x)=c_{s_2, a}=0$

### Definition: Set of Paths

For any given $(G,r,c)$ we denote by $\mathcal{P}_i$ the set of paths available to commodity $i$.

### Definition: Feasible Flow

On a routing game we define a flow $f$ as a vector representing the quantity of traffic along the
various paths, $f$ is a vector index by $\mathcal{P}$. We call $f$ **feasible** if:

$$\sum_{P\in\mathcal{P}_i}f_P=r_i$$

#### Example: Feasible Flows for the Delivery Companies Game

For the routing game in [](#fig:competing_delivery_companies_routing_game):

$$\mathcal{P}_1=\{(s_1,a,t),(s_1,t)\}$$

and

$$\mathcal{P}_2=\{(s_2,a,t),(s_2,t)\}$$

The set of all possible paths is denoted by $\mathcal{P}=\cup_{i}\mathcal{P}_i$.

### Definition: Cost function

For any routing game $(G,r,c)$ we define a **cost function** $C(f)$:

$$C(f)=\sum_{P\in\mathcal{P}}c_P(f_P)f_P$$

Where $c_P$ denotes the cost function of a particular path $P$: $c_P(x)=\sum_{e\in P}c_e(x)$.
Note that any flow $f$ induces a flow on edges:

$$f_e=\sum_{P\in\mathcal{P}\text{ if }e\in P}f_P$$

So we can re-write the cost function as:

$$C(f)=\sum_{e\in E}c_e(f_e)f_e$$

#### Example: Cost function for the Delivery Companies Game

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

#### Example: Optimal Flow for the Delivery Companies Games

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

$$\left\{- \frac{1}{5} - \frac{\sqrt{11}}{5}, \; \frac{\sqrt{11}}{5} - \frac{1}{5}\right\}$$

Only one of those is positive satisfying the constraints, substituting it in to
[](#eqn:beta_as_a_function_of_alpha) gives:

$$\beta=\frac{12}{25} - \frac{2 \sqrt{11}}{25}$$

thus the optimal flow is:

$$
f^* = \left(\frac{\sqrt{11}}{5} - \frac{1}{5}, \; \frac{12}{25} - \frac{2 \sqrt{11}}{25}\right)
$$

If we take a closer look at $f^*$ in our example, we see that traffic from the first commodity travels
across two paths: $(s_1, t)$ and $(s_1, a, t)$. The cost along the first path is given by:

$$C_{s_1, t}(f^*)=\frac{12}{25} - \frac{2 \sqrt{11}}{25}\approx 0.2146$$

The cost along the second path is given by:

$$C_{s_1, a, t}(f^*)=\frac{18}{25} - \frac{3 \sqrt{11}}{25}\approx 0.3220$$

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

#### Example: Nash Flow for Delivery companies game

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

#### Example: Potential Function for the delivery company game

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

#### Example: The marginal costs for the delivery company game

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

````{exercise} 
:label: braess_s_paradox

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
````

```{exercise} 
:label: nash_flow_via_potential_minimisation

Use [](#thrm:nash_flow_minimises_the_potential_function) and [](#app:kkt_conditions) to verify that
$\tilde f=(1/2,1/5)$ is a Nash flow for [](#fig:competing_delivery_companies_routing_game_with_flow_vector).
```

```{exercise}
:label: nash_flow_from_marginal_cost_formulation

Use [](#thrm:optimal_flow_is_a_nash_for_for_marginal_costs) to confirm that

$$
f=\left(\frac{\sqrt{11}}{5} - \frac{1}{5}, \; \frac{12}{25} - \frac{2 \sqrt{11}}{25}\right)
$$

is a Nash flow for [](#fig:competing_delivery_companies_routing_game_with_flow_vector).
```

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
[Braess's Paradox](#braess_s_paradox), first described in
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

[](#tbl:routing_games) summarises the key concepts.

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

```{attention}
In routing games, individual rationality does not guarantee
system-wide efficiency. Tools like potential functions and marginal costs
provide powerful methods to identify Nash and Optimal flows in
decentralized network systems.
```

---

(solutions:routing_games)=

## Solutions

````{solution} braess_s_paradox
:label: solution:braess_s_paradox

**Network without the super road**

The network in [](#fig:braesss_paradox_without_super_road) has a single source $s$, a single sink $t$, two intermediate nodes $a$ and $b$, and a total demand of $r=1$. The edges and their cost functions are:

$$
c_{s,a}(x)=x,\quad c_{a,t}(x)=1,\quad c_{s,b}(x)=1,\quad c_{b,t}(x)=x
$$

Let $\alpha$ denote the flow on path $P_1=(s,a,t)$ and $1-\alpha$ the flow on path $P_2=(s,b,t)$, with $0\leq\alpha\leq 1$.

**Optimal flow (without super road)**

The cost function is:

$$
C(\alpha)=c_{s,a}(\alpha)\cdot\alpha + c_{a,t}(\alpha)\cdot\alpha + c_{s,b}(1-\alpha)\cdot(1-\alpha) + c_{b,t}(1-\alpha)\cdot(1-\alpha)
$$

$$
C(\alpha)=\alpha^2+\alpha+(1-\alpha)+(1-\alpha)^2=\alpha^2+(1-\alpha)^2+1
$$

To minimise, take the derivative and set it to zero:

$$
\frac{dC}{d\alpha}=2\alpha-2(1-\alpha)=4\alpha-2=0\implies\alpha^*=\frac{1}{2}
$$

The optimal flow is $f^*=\alpha^*=1/2$, giving:

$$
C(f^*)=\frac{1}{4}+\frac{1}{4}+1=\frac{3}{2}
$$

**Nash flow (without super road)**

A Nash flow requires the cost along every used path to be equal. The cost along each path at flow $(\alpha, 1-\alpha)$ is:

$$
c_{P_1}(\alpha)=\alpha+1,\qquad c_{P_2}(1-\alpha)=1+(1-\alpha)=2-\alpha
$$

Setting $c_{P_1}=c_{P_2}$:

$$
\alpha+1=2-\alpha\implies \tilde\alpha=\frac{1}{2}
$$

So the Nash flow is $\tilde f = 1/2$, giving $\tilde f = f^*$ and:

$$
C(\tilde f)=\frac{3}{2}
$$

In this case the Nash flow coincides with the optimal flow, so the **Price of Anarchy** is $1$.

```{code-cell} python3
import numpy as np
import scipy.optimize

def cost_without_super_road(f):
    alpha = f[0]
    return alpha ** 2 + (1 - alpha) ** 2 + 1

def potential_without_super_road(f):
    alpha = f[0]
    # Phi = int_0^alpha x dx + int_0^alpha 1 dx + int_0^(1-alpha) 1 dx + int_0^(1-alpha) x dx
    return alpha ** 2 / 2 + alpha + (1 - alpha) + (1 - alpha) ** 2 / 2

constraints = [
    {'type': 'ineq', 'fun': lambda f: f[0]},
    {'type': 'ineq', 'fun': lambda f: 1 - f[0]},
]

res_opt = scipy.optimize.minimize(cost_without_super_road, [0.5], constraints=constraints)
res_nash = scipy.optimize.minimize(potential_without_super_road, [0.5], constraints=constraints)

print(f"Optimal flow alpha = {res_opt.x[0]:.4f}, cost = {res_opt.fun:.4f}")
print(f"Nash flow alpha = {res_nash.x[0]:.4f}, cost = {cost_without_super_road(res_nash.x):.4f}")
```

**Network with the super road (Braess's Paradox)**

The network in [](#fig:braesss_paradox) adds the edge $a\to b$ with $c_{a,b}(x)=0$. Using the flow vector shown in the figure, let $\alpha$ be the total flow entering node $a$ from $s$, and $\beta$ be the flow on the edge $a\to b$. The three paths are:

- $P_1=(s,a,t)$: flow $\alpha-\beta$
- $P_2=(s,b,t)$: flow $1-\alpha+\beta$
- $P_3=(s,a,b,t)$: flow $\beta$

with constraints $0\leq\beta\leq\alpha$, $0\leq\alpha\leq 1$, $0\leq 1-\alpha+\beta\leq 1$.

The edge flows are: $f_{s,a}=\alpha$, $f_{a,t}=\alpha-\beta$, $f_{s,b}=1-\alpha$, $f_{b,t}=1-\alpha+\beta$, $f_{a,b}=\beta$.

The cost function is:

$$
\begin{align*}
C(\alpha,\beta)&=c_{s,a}(\alpha)\cdot\alpha + c_{a,t}(\alpha-\beta)\cdot(\alpha-\beta)\\
               &\quad+c_{s,b}(1-\alpha)\cdot(1-\alpha)+c_{b,t}(1-\alpha+\beta)\cdot(1-\alpha+\beta)\\
               &\quad+c_{a,b}(\beta)\cdot\beta\\
               &=\alpha^2+(\alpha-\beta)+1\cdot(1-\alpha)+(1-\alpha+\beta)^2+0
\end{align*}
$$

**Optimal flow (with super road)**

The potential function is:

$$
\Phi(\alpha,\beta)=\frac{\alpha^2}{2}+(\alpha-\beta)+\frac{(\alpha-\beta)^2}{2}\cdot 0+(1-\alpha)+\frac{(1-\alpha+\beta)^2}{2}+0
$$

More carefully, since $c_{s,a}(x)=x$, $c_{a,t}(x)=1$, $c_{s,b}(x)=1$, $c_{b,t}(x)=x$, $c_{a,b}(x)=0$:

$$
\Phi(\alpha,\beta)=\frac{\alpha^2}{2}+({\alpha-\beta})\cdot 1 + (1-\alpha)\cdot 1+\frac{(1-\alpha+\beta)^2}{2}
$$

Taking partial derivatives:

$$
\frac{\partial C}{\partial\alpha}=2\alpha+1-1-2(1-\alpha+\beta)(-1)=2\alpha+2(1-\alpha+\beta)-0+1-1
$$

It is cleaner to work directly with the cost:

$$
C(\alpha,\beta)=\alpha^2+\alpha-\beta+(1-\alpha)+(1-\alpha+\beta)^2
$$

$$
\frac{\partial C}{\partial\alpha}=2\alpha-1+1-2(1-\alpha+\beta)=2\alpha-2(1-\alpha+\beta)=4\alpha+2\beta-2
$$

$$
\frac{\partial C}{\partial\beta}=-1+2(1-\alpha+\beta)=2\beta-2\alpha+1
$$

Setting both to zero:

$$
4\alpha+2\beta=2\implies 2\alpha+\beta=1
$$
$$
2\beta-2\alpha+1=0\implies\beta=\alpha-\frac{1}{2}
$$

Substituting: $2\alpha+\alpha-1/2=1\implies 3\alpha=3/2\implies\alpha^*=1/2$, $\beta^*=0$.

The optimal flow is $f^*=(\alpha^*,\beta^*)=(1/2,0)$, which is the same as the network without the super road, with cost:

$$
C(f^*)=\frac{1}{4}+\frac{1}{2}+\frac{1}{2}+\frac{1}{4}=\frac{3}{2}
$$

**Nash flow (with super road)**

For a Nash flow, we equate path costs for all used paths. Checking whether all three paths are used:

Path costs at flow $(\alpha,\beta)$ with all paths used:

$$
c_{P_1}=c_{s,a}(\alpha)+c_{a,t}(\alpha-\beta)=\alpha+1
$$
$$
c_{P_2}=c_{s,b}(1-\alpha)+c_{b,t}(1-\alpha+\beta)=1+(1-\alpha+\beta)=2-\alpha+\beta
$$
$$
c_{P_3}=c_{s,a}(\alpha)+c_{a,b}(\beta)+c_{b,t}(1-\alpha+\beta)=\alpha+0+(1-\alpha+\beta)=1+\beta
$$

Setting $c_{P_1}=c_{P_2}$:

$$\alpha+1=2-\alpha+\beta\implies 2\alpha-\beta=1$$

Setting $c_{P_1}=c_{P_3}$:

$$\alpha+1=1+\beta\implies\beta=\alpha$$

From $2\alpha-\alpha=1$ we get $\alpha=1$ and $\beta=1$.

Checking feasibility: $\alpha-\beta=0\geq 0$ (path $P_1$ has zero flow), $1-\alpha+\beta=1\geq 0$. However, $\alpha=1$ means all flow uses $s\to a$, so we need $1-\alpha=0$, meaning $P_2$ also has zero flow. Let us verify: with $\beta=\alpha=1$, path $P_3=(s,a,b,t)$ carries all flow of $1$.

Check: $c_{P_3}=1+\beta=1+1=2$, but $c_{P_1}=\alpha+1=2$ and $c_{P_2}=2-\alpha+\beta=2-1+1=2$. All path costs equal $2$.

The Nash flow is $\tilde f=(\alpha,\beta)=(1,1)$, i.e. all traffic travels $s\to a\to b\to t$, with:

$$
C(\tilde f)=1^2+0+(0)\cdot 1+(1)^2=1+0+0+1=2
$$

**This is Braess's Paradox**: adding the zero-cost road $a\to b$ raises the Nash flow cost from $3/2$ to $2$. The **Price of Anarchy** for the extended network is:

$$
\text{PoA}=\frac{C(\tilde f)}{C(f^*)}=\frac{2}{3/2}=\frac{4}{3}
$$

```{code-cell} python3
import numpy as np
import scipy.optimize

def cost_with_super_road(f):
    alpha, beta = f
    return (alpha ** 2 + (alpha - beta) + (1 - alpha) + (1 - alpha + beta) ** 2)

def potential_with_super_road(f):
    alpha, beta = f
    # int_0^alpha x dx + int_0^(alpha-beta) 1 dx + int_0^(1-alpha) 1 dx + int_0^(1-alpha+beta) x dx + 0
    return alpha ** 2 / 2 + (alpha - beta) + (1 - alpha) + (1 - alpha + beta) ** 2 / 2

constraints = [
    {'type': 'ineq', 'fun': lambda f: f[0]},
    {'type': 'ineq', 'fun': lambda f: 1 - f[0]},
    {'type': 'ineq', 'fun': lambda f: f[1]},
    {'type': 'ineq', 'fun': lambda f: f[0] - f[1]},
    {'type': 'ineq', 'fun': lambda f: 1 - f[0] + f[1]},
]

res_opt = scipy.optimize.minimize(cost_with_super_road, [0.4, 0.1], constraints=constraints)
res_nash = scipy.optimize.minimize(potential_with_super_road, [0.4, 0.1], constraints=constraints)

print(f"Optimal flow (alpha, beta) = ({res_opt.x[0]:.4f}, {res_opt.x[1]:.4f}), cost = {res_opt.fun:.4f}")
print(f"Nash flow (alpha, beta) = ({res_nash.x[0]:.4f}, {res_nash.x[1]:.4f}), cost = {cost_with_super_road(res_nash.x):.4f}")
print(f"Price of Anarchy = {cost_with_super_road(res_nash.x) / res_opt.fun:.4f}")
```
````

````{solution} nash_flow_via_potential_minimisation
:label: solution:nash_flow_via_potential_minimisation

We wish to verify that $\tilde f=(\alpha,\beta)=(1/2,1/5)$ is a Nash flow for the delivery companies game using the potential function approach.

By [](#thrm:nash_flow_minimises_the_potential_function), $\tilde f$ is a Nash flow if and only if it minimises the potential function:

$$
\Phi(\alpha,\beta)=\frac{\alpha^3}{3}+\frac{3\beta^2}{4}+\frac{(1-\alpha-\beta)^2}{2}
$$

subject to $0\leq\alpha\leq 1/2$ and $0\leq\beta\leq 1/2$.

Since the minimum may lie in the interior or on the boundary, we apply the KKT conditions. The feasible region is defined by:

$$
g_1(\alpha,\beta)=\alpha\geq 0,\quad g_2(\alpha,\beta)=1/2-\alpha\geq 0,\quad g_3(\alpha,\beta)=\beta\geq 0,\quad g_4(\alpha,\beta)=1/2-\beta\geq 0
$$

At $(\alpha,\beta)=(1/2,1/5)$: constraint $g_2$ is active ($\alpha=1/2$), while $g_1$, $g_3$, $g_4$ are inactive. By complementary slackness, $\lambda_1=\lambda_3=\lambda_4=0$, and $\lambda_2\geq 0$.

The KKT stationarity conditions are:

$$
\frac{\partial\Phi}{\partial\alpha}-\lambda_2\cdot(-1)=0\implies \alpha^2-(1-\alpha-\beta)+\lambda_2=0
$$

$$
\frac{\partial\Phi}{\partial\beta}-0=0\implies \frac{3\beta}{2}-(1-\alpha-\beta)=0
$$

Evaluating the second condition at $(1/2, 1/5)$:

$$
\frac{3}{2}\cdot\frac{1}{5}-\left(1-\frac{1}{2}-\frac{1}{5}\right)=\frac{3}{10}-\frac{3}{10}=0\checkmark
$$

For the first condition at $(1/2, 1/5)$:

$$
\left(\frac{1}{2}\right)^2-\left(1-\frac{1}{2}-\frac{1}{5}\right)+\lambda_2=\frac{1}{4}-\frac{3}{10}+\lambda_2=-\frac{1}{20}+\lambda_2=0
$$

$$
\implies\lambda_2=\frac{1}{20}>0\checkmark
$$

All KKT conditions are satisfied with $\lambda_2=1/20>0$, confirming that $(1/2,1/5)$ is a minimum of $\Phi$ and therefore a Nash flow.

```{code-cell} python3
import numpy as np
import scipy.optimize

def potential(f):
    alpha, beta = f
    return alpha ** 3 / 3 + 3 * beta ** 2 / 4 + (1 - alpha - beta) ** 2 / 2

constraints = [
    {'type': 'ineq', 'fun': lambda f: f[0]},
    {'type': 'ineq', 'fun': lambda f: 0.5 - f[0]},
    {'type': 'ineq', 'fun': lambda f: f[1]},
    {'type': 'ineq', 'fun': lambda f: 0.5 - f[1]},
]

res = scipy.optimize.minimize(potential, [0.3, 0.1], constraints=constraints)
print(f"Minimiser of potential: alpha = {res.x[0]:.6f}, beta = {res.x[1]:.6f}")
print(f"Expected: alpha = 0.5, beta = 0.2")
print(f"Potential at minimiser: {res.fun:.6f}")
```
````

````{solution} nash_flow_from_marginal_cost_formulation
:label: solution:nash_flow_from_marginal_cost_formulation

We wish to confirm that

$$
f=\left(\frac{\sqrt{11}}{5}-\frac{1}{5},\;\frac{12}{25}-\frac{2\sqrt{11}}{25}\right)
$$

is a Nash flow for the delivery companies game using the marginal cost formulation.

By [](#thrm:optimal_flow_is_a_nash_for_for_marginal_costs), a flow is optimal for $(G,r,c)$ if and only if it is a Nash flow for $(G,r,c^*)$, where $c^*$ denotes the marginal cost functions.

The original cost functions and their marginal costs are:

$$
c_{s_1,t}(x)=x^2\implies c^*_{s_1,t}(x)=\frac{d}{dx}(x\cdot x^2)=3x^2
$$

$$
c_{s_2,t}(x)=\frac{3}{2}x\implies c^*_{s_2,t}(x)=\frac{d}{dx}\!\left(\frac{3}{2}x^2\right)=3x
$$

$$
c_{a,t}(x)=x\implies c^*_{a,t}(x)=\frac{d}{dx}(x^2)=2x
$$

$$
c_{s_1,a}(x)=0\implies c^*_{s_1,a}(x)=0,\qquad c_{s_2,a}(x)=0\implies c^*_{s_2,a}(x)=0
$$

With $\alpha=\frac{\sqrt{11}}{5}-\frac{1}{5}$ and $\beta=\frac{12}{25}-\frac{2\sqrt{11}}{25}$, the shared edge $a\to t$ carries flow $f_{a,t}=1-\alpha-\beta$. The quadratic $5\alpha^2+2\alpha-2=0$ has roots $(-1\pm\sqrt{11})/5$, and we take the positive root. Numerically,

$$
\alpha\approx 0.4633,\qquad \beta\approx 0.2147,\qquad 1-\alpha-\beta\approx 0.3220,
$$

so all three flows are positive and the flow is feasible.

To verify $f^*$ is a Nash flow for the marginal cost game, we need to check that all used paths have equal marginal cost. The paths for commodity 1 are $P_{s_1,t}=(s_1,t)$ and $P_{s_1,a,t}=(s_1,a,t)$.

The marginal cost along $P_{s_1,t}$ is $c^*_{s_1,t}(\alpha)=3\alpha^2$.

The marginal cost along $P_{s_1,a,t}$ is $c^*_{s_1,a}(0)+c^*_{a,t}(1-\alpha-\beta)=0+2(1-\alpha-\beta)$.

At the optimal flow, these must be equal (since the optimal flow uses both paths for commodity 1):

$$
3\alpha^2=2(1-\alpha-\beta)
$$

This is exactly the first stationarity condition from the optimal flow derivation. Similarly, for commodity 2 using both its paths $P_{s_2,t}=(s_2,t)$ and $P_{s_2,a,t}=(s_2,a,t)$:

Marginal cost along $P_{s_2,t}$: $c^*_{s_2,t}(\beta)=3\beta$.

Marginal cost along $P_{s_2,a,t}$: $c^*_{s_2,a}(0)+c^*_{a,t}(1-\alpha-\beta)=2(1-\alpha-\beta)$.

At the optimal flow, $3\beta=2(1-\alpha-\beta)$, which is the second stationarity condition.

Since $f^*$ was found precisely by solving these two equations simultaneously, it satisfies the Nash flow conditions for $(G,r,c^*)$. By [](#thrm:optimal_flow_is_a_nash_for_for_marginal_costs), $f^*$ is therefore a Nash flow for the marginal cost game.

```{code-cell} python3
import sympy as sym

alpha, beta = sym.symbols('alpha beta', real=True)

# Optimal flow conditions: 3*alpha^2 = 2*(1 - alpha - beta) and 3*beta = 2*(1 - alpha - beta)
eq1 = sym.Eq(3 * alpha**2, 2 * (1 - alpha - beta))
eq2 = sym.Eq(3 * beta, 2 * (1 - alpha - beta))

solutions = sym.solve([eq1, eq2], [alpha, beta])
print("Solutions (alpha, beta):")
for sol in solutions:
    a_val, b_val = sol
    print(f"  alpha = {a_val} ≈ {float(a_val):.6f},  beta = {b_val} ≈ {float(b_val):.6f}")
    print(f"  Feasible (both in [0,1/2])? alpha>=0: {float(a_val) >= 0}, beta>=0: {float(b_val) >= 0}")
```

```{code-cell} python3
# Verify: at the feasible solution, marginal costs on used paths are equal
a_val = solutions[1][0]  # take the positive root
b_val = solutions[1][1]

shared_flow = 1 - a_val - b_val
mc_P1 = 3 * a_val**2
mc_P1_alt = 2 * shared_flow
mc_P2 = 3 * b_val
mc_P2_alt = 2 * shared_flow

print(f"Marginal cost on (s1,t): {sym.simplify(mc_P1)}")
print(f"Marginal cost on (s1,a,t): {sym.simplify(mc_P1_alt)}")
print(f"Equal? {sym.simplify(mc_P1 - mc_P1_alt) == 0}")
print(f"\nMarginal cost on (s2,t): {sym.simplify(mc_P2)}")
print(f"Marginal cost on (s2,a,t): {sym.simplify(mc_P2_alt)}")
print(f"Equal? {sym.simplify(mc_P2 - mc_P2_alt) == 0}")
```
````
