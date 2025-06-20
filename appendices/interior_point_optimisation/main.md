---
kernelspec:
  name: python3
  display_name: "Python 3"
numbering:
  enumerator: A1.%s
---

(app:kkt_conditions)=

# Appendix: Karush-Kuhn-Tucker Conditions

(sec:motivating_example_kkt_doughnuts)=

## Motivating Example: Optimising doughnut distribution at a research retreat

At the annual **Mathematical Modelling Retreat**, a catering mix-up leaves the
organisers with a limited supply of **12 gourmet donuts** and **8 litres of
coffee**.

To ensure everyone gets a share, the organisers plan to slice the donuts into
small portions and pour the coffee into individual cups of varying sizes.

The participants are divided into two groups:

- **Theoretical mathematicians**, who greatly enjoy strong coffee and appreciate
  a modest amount of sweet pastry.
- **Applied mathematicians**, who relish the pastries but are content with just
  enough coffee to stay alert.

Let:

- $x_1$ represent the number of _donut portions_ allocated to the theorists
- $x_2$ represent the amount of _coffee (in litres)_ allocated to the theorists

The applied group receives the remaining quantities:

- $(12 - x_1)$ donut portions
- $(8 - x_2)$ litres of coffee

The **total enjoyment** of the retreat is modelled as the sum of group
satisfactions:

$$
f(x_1, x_2) = \log(1 + x_1) + 2\sqrt{x_2} \log(1 + 12 - x_1) + 2\sqrt{8 - x_2}
$$

subject to the feasibility constraints:

$$
0 \leq x_1 \leq 12, \quad 0 \leq x_2 \leq 8
$$

The problem is now a continuous **convex optimisation problem**: although
donuts and coffee are discrete in reality, the organisers can approximate an
optimal allocation by dividing portions finely, making fractional allocations
meaningful.

This is an ideal setting for the **Karush-Kuhn-Tucker (KKT) conditions**.

In the next section, we will formally introduce these conditions and use them to
solve this doughnut-and-coffee dilemma.

## Theory

(sec:definition_kkt_conditions)=

### Definition: The Karush-Kuhn-Tucker Conditions

Let $x \in \mathbb{R}^n$ be a vector of decision variables. We consider a
general nonlinear programme of the form:

$$
\begin{aligned}
\text{Minimise } \quad & f(x) \\
\text{subject to } \quad & g_i(x) \leq 0, \quad i = 1, \dots, m \\
& h_j(x) = 0, \quad j = 1, \dots, p
\end{aligned}
$$

- The function $f: \mathbb{R}^n \to \mathbb{R}$ is the objective.
- The functions $g_i$ are inequality constraints.
- The functions $h_j$ are equality constraints.

We seek a point $x^*$ that satisfies all constraints and minimises $f(x)$.

---

Suppose $f$, $g_i$, and $h_j$ are continuously differentiable, and suppose a
constraint qualification holds at a local minimum $x^*$.

Then there exist Lagrange multipliers $\lambda_i \geq 0$ and $\mu_j \in
\mathbb{R}$ such that the Karush-Kuhn-Tucker (KKT) conditions hold:

- **Stationarity**:

  $$
  \nabla_x \mathcal{L}(x, \mu, \lambda) = \nabla_x f(x^*) + \sum_{i=1}^m \lambda_i \nabla g_i(x^*) +
  \sum_{j=1}^p \mu_j \nabla h_j(x^*) = 0
  $$

- **Primal feasibility**:

  $$
  g_i(x^*) \leq 0, \quad h_j(x^*) = 0
  $$

- **Dual feasibility**:

  $$
  \lambda_i \geq 0
  $$

- **Complementary slackness**:
  $$
  \lambda_i g_i(x^*) = 0 \quad \text{for all } i
  $$

---

These conditions are **necessary** for local optimality, and under convexity
assumptions, they are also **sufficient**.

Each of the conditions has an important role:

- **Stationarity**  
  At a local optimum, the gradient of the Lagrangian vanishes. This means
  that the direction of steepest descent of the objective is balanced by the
  gradients of the active constraints.

- **Primal feasibility**  
  The candidate solution must satisfy all constraints of the original problem:
  the inequality constraints must be nonpositive, and the equality constraints
  must be exactly satisfied.

- **Dual feasibility**  
  The Lagrange multipliers corresponding to inequality constraints must be
  nonnegative. These multipliers can be interpreted as shadow prices or marginal
  rates of improvement in the objective function per unit tightening of the
  respective constraints. A negative multiplier would suggest that tightening a
  constraint could worsen the objective, which contradicts optimality.

- **Complementary slackness**  
  For each inequality constraint, either the constraint is active (holds with
  equality) and its multiplier may be positive, or the constraint is inactive
  (strictly satisfied) and its multiplier must be zero. This ensures that
  inactive constraints do not influence the stationarity condition.

(sec:kkt_example)=

### Example: Verifying the KKT conditions for the doughnut problem

Let us verify that $x_1 \approx 1.243$ and $x_2 \approx 6.869$ satisfy the KKT
conditions for the doughnut problem.

The objective function is given by $f(x_1, x_2)$. The inequality constraints can
be written as:

$$
\begin{align*}
g_1(x) & = -x_1 \leq 0 \\
g_2(x) & = -x_2 \leq 0 \\
g_3(x) & = x_1 - 12 \leq 0 \\
g_4(x) & = x_2 - 8 \leq 0
\end{align*}
$$

There are no equality constraints in this problem, so there are no associated
Lagrange multipliers $\mu$.

The Lagrangian is:

$$
\mathcal{L}(x, \lambda) = -\lambda_{1} x_{1} + \lambda_{2} (x_{1} - 12)
-\lambda_{3} x_{2} + \lambda_{4} (x_{2} - 8)
+ 2 \sqrt{x_{2}} \log(13 - x_{1}) + 2 \sqrt{8 - x_{2}} + \log(x_{1} + 1)
$$

We now check whether $x \approx (1.243, 6.869)$ satisfies the KKT conditions.

**Stationarity:**

We compute the partial derivatives of the Lagrangian:

$$
\begin{align*}
\frac{\partial \mathcal{L}(x, \lambda)}{\partial x_1} &=
-\lambda_{1} + \lambda_{2} - \frac{2 \sqrt{x_{2}}}{13 - x_{1}}
+ \frac{1}{x_{1} + 1} \\
\frac{\partial \mathcal{L}(x, \lambda)}{\partial x_2} &=
-\lambda_{3} + \lambda_{4} - \frac{1}{\sqrt{8 - x_{2}}}
+ \frac{\log(13 - x_{1})}{\sqrt{x_{2}}}
\end{align*}
$$

**Primal feasibility, dual feasibility, and complementary slackness:**

Substituting $x = (1.243, 6.869)$ into the constraints gives:

$$
\begin{align*}
g_1(x) &= -1.243 < 0 \\
g_2(x) &= -6.869 < 0 \\
g_3(x) &= -10.757 < 0 \\
g_4(x) &= -1.131 < 0
\end{align*}
$$

Since all inequality constraints are strictly satisfied, complementary slackness
implies that $\lambda_i = 0$ for all $i$. This also satisfies dual feasibility.

**Verifying stationarity:**

Substituting $x = (1.243, 6.869)$ and $\lambda_i = 0$ into the stationarity
conditions gives:

$$
\begin{align*}
\left. \frac{\partial \mathcal{L}}{\partial x_1} \right|_{x, \lambda=0} &=
- \frac{2 \sqrt{6.869}}{13 - 1.243} + \frac{1}{1.243 + 1} \approx 0 \\
\left. \frac{\partial \mathcal{L}}{\partial x_2} \right|_{x, \lambda=0} &=
- \frac{1}{\sqrt{8 - 6.869}} + \frac{\log(13 - 1.243)}{\sqrt{6.869}} \approx 0
\end{align*}
$$

Both partial derivatives are approximately zero, confirming that stationarity
holds.

As $f(x_1, x_2)$ is a sum of concave functions being maximised (or equivalently,
a convex minimisation problem), the KKT conditions are both necessary and
sufficient. We can conclude that $x \approx (1.243, 6.869)$ is indeed the global
optimum.

## Exercises

### Exercise 1: Understanding KKT components

Consider the following optimisation problem:

$$
\begin{aligned}
\text{Minimise} \quad & f(x, y) = x^2 + y^2 \\
\text{subject to} \quad & x + y \geq 2 \\
& x \geq 0, \quad y \geq 0
\end{aligned}
$$

1. Rewrite the problem in standard form for KKT analysis (i.e., with all
   constraints as $g_i(x) \leq 0$).
2. Write down the KKT conditions symbolically.
3. Find all KKT points and identify whether they correspond to a global minimum.

---

### Exercise 2: Symbolic derivation of KKT conditions

Consider the problem:

$$
\begin{aligned}
\text{Maximise} \quad & \log(x) + \log(1 - x) \\
\text{subject to} \quad & 0.1 \leq x \leq 0.9
\end{aligned}
$$

1. Show that the objective function is concave on the interval $(0, 1)$.
2. Derive the KKT conditions for this problem.
3. Solve for the optimal value of $x$ and the associated Lagrange multipliers.

---

## Programming

### Solving constrained optimisation problems with Scipy

Scipy has functionality to solve constrained optimisation problems.

```{code-cell} python3
import numpy as np
import scipy.optimize

def objective(x):
    x1, x2 = x
    return -(np.log(1 + x1) + 2 * np.sqrt(x2) * np.log(1 + 12 - x1) + 2 * np.sqrt(8 - x2))

def g_1(x):
    return x[0]

def g_2(x):
    return x[1]

def g_3(x):
    return 12 - x[0]

def g_4(x):
    return 8 - x[1]

constraints = [
    {'type': 'ineq', 'fun': g_1},
    {'type': 'ineq', 'fun': g_2},
    {'type': 'ineq', 'fun': g_3},
    {'type': 'ineq', 'fun': g_4},
]

res = scipy.optimize.minimize(objective, [6, 4], constraints=constraints)
res

```

## Notable Research

The Karush-Kuhn-Tucker conditions were first described by Karush in [@karush1939minima] but this was
unpublished and widely unknown until Kuhn and Tucker presented the conditions at a mathematics symposium [@kuhn1951nonlinear].
Some text book still refer to the conditions as the Kuhn-Tucker conditions but
most, rightly, refer to them in a way that rightfully respects all the authors.

Before [@kuhn1951nonlinear] generalisation of the conditions that holds in more
complex cases even when the feasible region is not well behaved was published in
[@john1948extremum].

The Karush-Kuhn-Tucker conditions provide a way to check stability or indeed
optimality but the collection of methods that finds potential optima is referred
to as interior point method [@boyd2004convex].

## Conclusion

The Karush-Kuhn-Tucker (KKT) conditions provide a unified framework to
characterise optimal solutions to constrained optimisation problems. They
extend the method of Lagrange multipliers to include inequality constraints,
introducing complementary slackness and dual feasibility as key components.

[](#tbl:kkt_summary) summarises the key concepts introduced in this
appendix.

```{table} Summary of the Karush-Kuhn-Tucker conditions
:name: tbl:kkt_summary
:align: center

| Condition            | Meaning |
|----------------------|---------|
| **Stationarity**     | The objective’s gradient is balanced by the gradients of active constraints |
| **Primal feasibility** | The solution satisfies all original constraints |
| **Dual feasibility**   | Lagrange multipliers for inequality constraints are nonnegative |
| **Complementary slackness** | Inactive constraints have zero multipliers; active constraints may have positive multipliers |
```

The KKT conditions are **necessary** for optimality when constraint
qualifications hold, and **sufficient** for optimality when the problem is
convex. In this way, they serve both as a _diagnostic tool_ to verify candidate
solutions, and as a _theoretical foundation_ for many modern optimisation
algorithms.

```{important}
In unconstrained optimisation, optimality is characterised by setting the derivative to zero.
With equality constraints, we introduce the Lagrangian and set its gradient to zero.
With inequality constraints, the Karush-Kuhn-Tucker conditions extend this further,
adding complementary slackness and nonnegative multipliers to capture which constraints are active at the optimum.
```
