---
kernelspec:
  name: python3
  display_name: "Python 3"
numbering:
  enumerator: A1.%s
---

(app:numerical_integration)=

# Appendix: Numerical Integration

## Motivating Example: Air resistance of a sky diver

An object falling under gravity is often assumed to not be subject air
resistance. This give:

$$
\label{eqn:dv_dt_with_no_resistance}
\frac{dv}{dt}=g
$$

This differential equation can be solved to give:

$$
v(t) = -g t + v_0
$$

where $v_0 = v(0)$. This in turn gives the vertical displacement of an object
falling as:

$$
\frac{dy}{dt} = v(t) = -gt + v_0
$$

which can be solved to give:

$$
y(t) = - g \frac{t^2}{2} + v_0 t + y_0
$$

where $y(0) = y_0$. This is all based on [](#eqn:dv_dt_with_no_resistance) which
assumes no air resistance. In fact all objects falling experience a drag
coefficient $k$ (kg/m). Approximate values of $k$ are given in
[](#tbl:drag_coefficient_for_skydiver).

```{table} Estimated quadratic drag coefficients for skydiver
:align: center
:name: tbl:drag_coefficient_for_skydiver

| Position                  | $k$ (kg/m) |
|---------------------------|------------|
|          Spread-eagle     | 0.42875    |
|          Aerodynamic      | 0.07718    |
|          Parachute        | 26.79688   |
```

To take this coefficient in to account [](#eqn:dv_dt_with_no_resistance) is
modified to give:

$$
\label{eqn:dv_dt_with_resistance}
\frac{dv}{dt}=g - \frac{k}{m}v ^ 2
$$

This equation can in fact not be solved to give a closed form solution. Another
approach to be able to compute the trajectory of a skydiver is needed.
The approach in question is numerical integration and the specific approach in
this appendix is Euler's method.

## Theory

### Definition: Euler's Method

---

Euler's Method is a first-order numerical procedure for approximating solutions
to initial value problems of the form:

$$
\frac{dy}{dt} = f(t, y), \qquad y(t_0) = y_0
$$

Given a step size $h > 0$, Euler’s Method generates a sequence of approximations
$\{(t_n, y_n)\}$ by:

$$
t_{n+1} = t_n + h
$$

$$
y_{n+1} = y_n + h f(t_n, y_n)
$$

starting from the initial condition $y(t_0) = y_0$.

---

At each step, Euler's Method uses the slope given by the differential equation
at the current point to extrapolate forward by a small time step.

The differential equation defines a slope field in the $(t, y)$ plane. Euler’s
Method approximates the solution curve by connecting short tangent segments.
At each step, the next point is found by moving forward along the tangent line
to the curve at the current point.

This can be visualized as constructing a polygonal approximation to the true
solution curve as shown in [](#fig:geometric_interpretation_of_eulers_method).

```{figure} ./images/geometric_interpretation_of_eulers_method/main.png
:alt: A plot of a function with a polygonal approximation
:label: fig:geometric_interpretation_of_eulers_method
:height: 500px

A geometric interpretation of numerical integration applied to $\frac{dx}{dt} = x$.
```

```{attention}
Euler's Method is **first-order accurate**, meaning the global error scales
linearly with the step size $h$:

$$
\text{Global error} = \mathcal{O}(h)
$$

Although simple, Euler’s Method is only conditionally stable and may require
very small step sizes for good accuracy. More accurate alternatives include
Runge-Kutta methods, which use higher-order derivative information.
```

### Example: Exponential growth

Consider the differential equation:

$$
\frac{dx}{dt} = x, \qquad y(0) = 1
$$

The exact solution is $y(t) = e^t$.

Applying Euler's Method with step size $h$ gives:

$$
y_{n+1} = y_n + h y_n = y_n(1 + h)
$$

which generates the sequence:

$$
y_n = (1 + h)^n
$$

As $h \to 0$ and $n \to \infty$ with $nh = t$, this approximates $e^t$.

## Exercises

```{exercise}
:label: numerical_integration:exercise_1

Use Euler’s method to approximate the solution to the differential equation:

$$
\frac{dx}{dt} = x,\qquad x(0) = 1
$$

with step size $h = 0.2$ up to $t = 1$.

1. Compute the values of $x_1, x_2, \dots, x_5$ using Euler’s method.
2. Compare each value to the exact solution $x(t) = e^t$ at the same time points.
3. Comment on how the approximation behaves: is it an overestimate or an underestimate? Why?
```

```{exercise}
:label: numerical_integration:exercise_2

Consider the differential equation:

$$
\frac{dx}{dt} = -2x + 1,\qquad x(0) = 0
$$

1. Use Euler’s method with step size $h = 0.1$ to compute the first 5 steps.
2. Plot the approximation.
3. Sketch or describe the qualitative behaviour of the true solution.
```

```{exercise}
:label: numerical_integration:exercise_3

Let $x(t)$ be the true solution to the initial value problem:

$$
\frac{dx}{dt} = \cos(t),\qquad x(0) = 0
$$

1. Derive the exact solution.
2. Use Euler’s method with step sizes $h = 0.5$, $0.25$, and $0.125$ to compute $x(1)$.
3. For each step size, compute the absolute error at $t = 1$.
4. Discuss how the error changes as $h$ decreases. What does this suggest about the convergence of Euler’s method?
```

## Programming

### Writing an implementation of Euler's method

The following python function implements Euler's method:

```{code-cell} python3
def get_euler_steps(function, number_of_steps, h, x_0):
    """
    Given a differential equation of the following form:

    dx/dt = function(x)

    This returns `number_of_steps` as given by Euler's algorithm:

    x_{n + 1} = x_n + h function(x_n)

    Parameters
    ----------
    function : A python function -- corresponding to the right hand side of the
               ordinary differential equation
    number_of_steps : int -- The number of iterations of the algorithm
    h : float -- The step size
    x_0 : float -- the initial_value of x

    Returns
    -------
    steps : A python list
    """
    steps = [x_0]
    for _ in range(number_of_steps):
        steps.append(steps[-1] + h * function(steps[-1]))
    return steps
```

We can use this function to get the steps as required:

```{code-cell} python3

def derivative(x):
    return x

number_of_steps = 10
h = 0.1
x_0 = 1
steps = get_euler_steps(
    function=derivative,
    number_of_steps=number_of_steps,
    h=h,
    x_0=x_0,
)
steps
```

### Using Scipy's ordinary differential equation integrator

The Scipy library has an implementation of numerical integration for ordinary
differential equations based on an algorithm described in [@petzold1983automatic].
One difference
with the previous section is that the function corresponding to the right hand
side of the ordinary differential equation must take $t$ as an input even if it
does not use it and it also takes a sequence of time points instead of a number
of steps. Let us start by setting those up:

```{code-cell} python
import scipy.integrate
import numpy as np

def derivative(x, t):
    return x

t = np.linspace(0, 1, 10)
```

```{code-cell} python3

steps = scipy.integrate.odeint(func=derivative, t=t, y0=x_0)
steps
```

```{attention}
When using numerical integration it is important to carefully consider the step
size (or the number of points) to ensure accuracy.
```

## Notable Research

The earliest method of numerical integration, now known as **Euler's method**,
originates from the foundational work of Leonhard Euler in the 18th century. He
implicitly described the approach in [@euler1768], laying the groundwork for
using tangent approximations to solve differential equations numerically.

The natural development from Euler’s idea led to the class of **Runge–Kutta
methods**, which provide higher-order accuracy by sampling the derivative at
multiple points. These were introduced independently by Runge
[@runge1895numerische] and Kutta [@kutta1901beitrage], and remain the basis of
many modern solvers.

In contemporary settings, attention has turned to the distinction between
**stiff** and **non-stiff** problems. These require different integration
techniques for efficient and stable solutions. Foundational references include
[@hairer1993nonstiff] for non-stiff problems and [@hairer1996stiff] for stiff
and differential-algebraic systems.

An important algorithm widely used today is **LSODA**, described in
[@petzold1983automatic]. This method automatically switches between stiff and
non-stiff solvers based on the behaviour of the system, and it underpins
many solvers, including those in the SciPy library.

## Conclusion

Euler’s method offers a simple and intuitive introduction to numerical
integration, but it highlights the tradeoff between simplicity, accuracy, and
stability. Modern applications often involve stiff systems or demand high
accuracy, where more advanced methods are preferable.

[tbl:numerical_methods_summary] summarizes key properties of several commonly used numerical
integration methods.

```{table} Summary of numerical methods. Higher-order methods reduce error more quickly with smaller steps. Stiff solvers handle problems where some parts evolve much faster than others.
:name: tbl:numerical_methods_summary
:align: center

| Method         | Order of Accuracy | Stiff Solver | Notes                              |
|----------------|-------------------|--------------|------------------------------------|
| Euler          | 1                 | No           | Simple, intuitive                  |
| RK4            | 4                 | No           | Widely used, good for smooth ODEs |
| Backward Euler | 1                 | Yes          | Implicit, stable for stiff systems|
| LSODA          | Adaptive          | Yes          | Switches between stiff/non-stiff  |
```

```{important}
Euler’s method is valuable for learning, but for practical use, one should
default to a well-tested numerical integrator unless there's a compelling reason
not to.
```

---

(solutions:numerical_integration)=

## Solutions

````{solution} numerical_integration:exercise_1
:label: solution:numerical_integration:exercise_1

The differential equation is

$$
\frac{dx}{dt} = x, \qquad x(0) = 1,
$$

with step size $h = 0.2$. Euler's method gives

$$
x_{n+1} = x_n + h \cdot x_n = x_n(1 + h) = 1.2\, x_n.
$$

1. Starting from $x_0 = 1$, the five Euler steps are:

$$
\begin{aligned}
x_1 &= 1.2^1 = 1.2000\\
x_2 &= 1.2^2 = 1.4400\\
x_3 &= 1.2^3 = 1.7280\\
x_4 &= 1.2^4 = 2.0736\\
x_5 &= 1.2^5 = 2.4883
\end{aligned}
$$

2. The exact solution is $x(t) = e^t$. Comparing at $t_n = 0.2n$:

| $n$ | $t_n$ | $x_n$ (Euler) | $e^{t_n}$ (exact) | Absolute error |
|-----|--------|---------------|--------------------|----------------|
| 1   | 0.2    | 1.2000        | 1.2214             | 0.0214         |
| 2   | 0.4    | 1.4400        | 1.4918             | 0.0518         |
| 3   | 0.6    | 1.7280        | 1.8221             | 0.0941         |
| 4   | 0.8    | 2.0736        | 2.2255             | 0.1519         |
| 5   | 1.0    | 2.4883        | 2.7183             | 0.2300         |

```{code-cell} python3
import numpy as np

h = 0.2
x = 1.0
print(f"{'n':>3}  {'t':>5}  {'Euler':>10}  {'Exact':>10}  {'Error':>10}")
for n in range(1, 6):
    x = x * (1 + h)
    t = n * h
    exact = np.exp(t)
    print(f"{n:>3}  {t:>5.1f}  {x:>10.6f}  {exact:>10.6f}  {abs(x - exact):>10.6f}")
```

3. The Euler approximation is a **systematic underestimate** at every step. The
   reason is that $\frac{dx}{dt} = x$ has a convex solution ($e^t$ is convex,
   meaning its second derivative $e^t > 0$). When we extrapolate along the
   tangent from the left endpoint of each sub-interval, we move along a straight
   line that lies *below* the concave-up curve. Equivalently, $(1+h)^n < e^{nh}$
   for all $h > 0$ and $n \geq 1$, which follows from the inequality
   $1 + h < e^h$ for $h > 0$. Consequently, all Euler values fall below the
   exact solution, and the error grows with $t$.
````

````{solution} numerical_integration:exercise_2
:label: solution:numerical_integration:exercise_2

The differential equation is

$$
\frac{dx}{dt} = -2x + 1, \qquad x(0) = 0,
$$

with step size $h = 0.1$. Euler's method gives

$$
x_{n+1} = x_n + 0.1(-2x_n + 1) = 0.8\,x_n + 0.1.
$$

1. Starting from $x_0 = 0$, the first five steps are:

$$
\begin{aligned}
x_1 &= 0.8(0) + 0.1 = 0.1000\\
x_2 &= 0.8(0.1) + 0.1 = 0.1800\\
x_3 &= 0.8(0.18) + 0.1 = 0.2440\\
x_4 &= 0.8(0.244) + 0.1 = 0.2952\\
x_5 &= 0.8(0.2952) + 0.1 = 0.3362
\end{aligned}
$$

```{code-cell} python3
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return -2 * x + 1

h = 0.1
x = 0.0
euler_x = [x]
for n in range(1, 6):
    x = x + h * f(x)
    print(f"x_{n} = {x:.6f}")
    euler_x.append(x)
```

2. Plot of the Euler approximation over the first 5 steps and beyond:

```{code-cell} python3
h = 0.1
x = 0.0
ts = [0.0]
xs = [x]
for _ in range(30):
    x = x + h * f(x)
    ts.append(ts[-1] + h)
    xs.append(x)

t_exact = np.linspace(0, 3, 300)
x_exact = 0.5 * (1 - np.exp(-2 * t_exact))

plt.figure(figsize=(7, 4))
plt.plot(ts, xs, "o-", label="Euler ($h=0.1$)", markersize=4)
plt.plot(t_exact, x_exact, "--", label="Exact solution")
plt.xlabel("$t$")
plt.ylabel("$x$")
plt.title(r"Euler's method vs exact solution for $\dot x = -2x+1$, $x(0)=0$")
plt.legend()
plt.tight_layout();
```

3. The true solution is obtained by solving the linear first-order ODE:

$$
\frac{dx}{dt} + 2x = 1.
$$

The integrating factor is $e^{2t}$, giving

$$
\frac{d}{dt}\!\left(e^{2t} x\right) = e^{2t}
\implies e^{2t} x = \tfrac{1}{2}e^{2t} + C
\implies x(t) = \tfrac{1}{2} + C e^{-2t}.
$$

Applying $x(0) = 0$ gives $C = -\tfrac{1}{2}$, so

$$
x(t) = \frac{1}{2}\!\left(1 - e^{-2t}\right).
$$

Qualitatively, the solution rises monotonically from $x(0)=0$ and
approaches the **stable equilibrium** $x^* = \tfrac{1}{2}$ as $t \to \infty$.
The approach is exponential, with rate constant $2$. There is no oscillation.
Euler's method (with $h=0.1$, so that $1-2h = 0.8 \in (-1,1)$) reproduces
this monotone approach correctly, albeit with some lag behind the true curve.
````

````{solution} numerical_integration:exercise_3
:label: solution:numerical_integration:exercise_3

The initial value problem is

$$
\frac{dx}{dt} = \cos t, \qquad x(0) = 0.
$$

1. **Exact solution.** Integrating directly:

$$
x(t) = \int_0^t \cos s\, ds = \sin t.
$$

Hence $x(1) = \sin 1 \approx 0.841471$.

2. **Euler's method** with step size $h$ approximates $x(1) = \sin 1$ using
   $N = 1/h$ steps:

$$
x_{n+1} = x_n + h \cos(nh), \qquad x_0 = 0.
$$

```{code-cell} python3
import numpy as np

def euler_cos(h):
    """Approximate x(1) for dx/dt = cos(t), x(0)=0 using step size h."""
    N = int(round(1.0 / h))
    x = 0.0
    t = 0.0
    for _ in range(N):
        x = x + h * np.cos(t)
        t += h
    return x

exact = np.sin(1.0)
for h in [0.5, 0.25, 0.125]:
    approx = euler_cos(h)
    err = abs(approx - exact)
    print(f"h = {h:.3f}:  x(1) ≈ {approx:.8f},  error = {err:.2e}")

print(f"\nExact: sin(1) = {exact:.8f}")
```

3. **Absolute errors at $t = 1$:**

| $h$   | Euler $x(1)$ | Absolute error |
|-------|-------------|----------------|
| 0.500 | $\approx 0.8776$ | $\approx 3.6 \times 10^{-2}$ |
| 0.250 | $\approx 0.8594$ | $\approx 1.8 \times 10^{-2}$ |
| 0.125 | $\approx 0.8504$ | $\approx 8.9 \times 10^{-3}$ |

4. **Convergence analysis.** Each time $h$ is halved, the absolute error is
   approximately halved as well. More precisely, let $e(h)$ denote the global
   error at a fixed endpoint. For Euler's method one can show (via Taylor
   expansion) that the **local truncation error** per step is $\mathcal{O}(h^2)$,
   and since there are $1/h$ steps the **global error** accumulates to

$$
e(h) = \mathcal{O}(h).
$$

This is confirmed numerically: halving $h$ from 0.5 to 0.25 cuts the error
roughly in half ($3.6 \times 10^{-2} \to 1.8 \times 10^{-2}$), and halving
again from 0.25 to 0.125 cuts it in half again ($1.8 \times 10^{-2} \to
8.9 \times 10^{-3}$). The ratio of errors is close to 2 each time, consistent
with first-order ($p=1$) convergence. We can verify this empirically:

```{code-cell} python3
h_values = [0.5, 0.25, 0.125, 0.0625, 0.03125]
exact = np.sin(1.0)
errors = []
for h in h_values:
    err = abs(euler_cos(h) - exact)
    errors.append(err)
    print(f"h = {h:.5f}:  error = {err:.4e}")

# Estimate convergence order from consecutive pairs
print("\nConvergence order estimates:")
for i in range(1, len(errors)):
    if errors[i] > 0 and errors[i-1] > 0:
        order = np.log(errors[i-1] / errors[i]) / np.log(h_values[i-1] / h_values[i])
        print(f"  h = {h_values[i-1]:.5f} → {h_values[i]:.5f}:  p ≈ {order:.3f}")
```

The convergence order estimates approach $p \approx 1$, confirming that
Euler's method is **first-order accurate**. For problems requiring high
accuracy, Runge–Kutta methods (e.g.\ RK4, which is fourth-order accurate)
dramatically reduce the error for the same computational cost.
````
