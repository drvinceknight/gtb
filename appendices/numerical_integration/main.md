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

### Exercise: Approximating exponential growth

Use Euler's method to approximate the solution to the differential equation:

$$
\frac{dx}{dt} = x,\qquad x(0) = 1
$$

with step size $h = 0.2$ up to $t = 1$.

1. Compute the values of $x_1, x_2, \dots, x_5$ using Euler’s method.
2. Compare each value to the exact solution $x(t) = e^t$ at the same time points.
3. Comment on how the approximation behaves: is it an overestimate or an underestimate? Why?

---

### Exercise: Visualizing Euler’s method

Consider the differential equation:

$$
\frac{dx}{dt} = -2x + 1,\qquad x(0) = 0
$$

1. Use Euler's method with step size $h = 0.1$ to compute the first 5 steps.
2. Plot the approximation.
3. Sketch or describe the qualitative behavior of the true solution.

---

### Exercise: Error and convergence

Let $x(t)$ be the true solution to the initial value problem:

$$
\frac{dx}{dt} = \cos(t),\qquad x(0) = 0
$$

1. Derive the exact solution.
2. Use Euler’s method with step sizes $h = 0.5$, $0.25$, and $0.125$ to compute $x(1)$.
3. For each step size, compute the absolute error at $t = 1$.
4. Discuss how the error changes as $h$ decreases. What does this suggest about the convergence of Euler’s method?

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
