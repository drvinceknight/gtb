---
kernelspec:
  name: python3
  display_name: "Python 3"
---

(solutions:replicator_dynamics)=

# Solutions: Replicator Dynamics Exercises

````{solution} replicator_dynamics:exam_style_1
:label: solution:replicator_dynamics:exam_style_1


1. The fitness of an app user is made up of:

- a **base utility** of using any messaging app at all;
- an **extra utility** that increases with the proportion of users choosing
  the same app.

For app $A$:

$$
f_A(x)
=
\underbrace{1}_{\text{base utility of using any app}}
+
\underbrace{2x_1}_{\text{extra utility from many friends using app }A}
$$

For app $B$:

$$
f_B(x)
=
\underbrace{1}_{\text{base utility of using any app}}
+
\underbrace{2(1-x_1)}_{\text{extra utility from many friends using app }B}
$$

So users gain more by coordinating on the same app as their friends.


2. If $x_1$ is the proportion of the population using strategy $1$ (here, app $A$),
the replicator dynamics for a two type population is:

$$
\frac{dx_1}{dt}
=
x_1\bigl(f_1(x) - \phi(x)\bigr),
$$

where the average fitness $\phi(x)$ is

$$
\phi(x)
=
x_1 f_1(x) + (1-x_1) f_2(x).
$$


3. From [](#sec:stable_population):

For a given population game with $N$ types of individuals and fitness functions
$f_i$ a stable population $\tilde x$ is one for which $\dot x_i=0$ for
all $i$.



4. From [](#sec:definition_post_entry_population):
For a population with $N$ types of individuals
Given a population $x \in \mathbb{R}^N_{[0, 1]}$ (with $\sum_{i=1}^Nx_i=1$), some $\epsilon>0$ and
a strategy $y \in \mathbb{R}^N_{[0, 1]}$ (with $\sum_{i=1}^Ny_i=1$), the post entry population $x_{\epsilon}$ is given by:

$$
x_{\epsilon} = x + \epsilon(y - x)
$$


5. From [](#sec:definition_of_evolutionary_stable_strategy):

A strategy $x^*$ is an evolutionarily stable strategy if for all $x_{\epsilon} \neq x^*$ sufficiently close to $x^*$:

$$
f(x^*, x^*) > f(x_{\epsilon}, x^*)
$$

In practice _sufficiently close_ implies that there exists some $\bar\epsilon$ such
that for all $y \neq x^*$ and for all $0 < \epsilon < \bar\epsilon$ the post entry population $x_{\epsilon} = x + \epsilon(y - x)$
satisfies the above inequality.


6. We have
$$
f_A(x)=1+2x_1,
\qquad
f_B(x)=1+2(1-x_1).
$$

The average fitness is
$$
\begin{aligned}
\phi(x)
&= x_1 f_A(x) + (1-x_1) f_B(x) \\
&= x_1(1+2x_1) + (1-x_1)\bigl(1+2(1-x_1)\bigr) \\
&= x_1 + 2x_1^2 + (1-x_1)(3-2x_1) \\
&= x_1 + 2x_1^2 + 3 - 5x_1 + 2x_1^2 \\
&= 3 - 4x_1 + 4x_1^2.
\end{aligned}
$$

The replicator dynamics is
$$
\begin{aligned}
\frac{dx_1}{dt}
&= x_1\bigl(f_A(x) - \phi(x)\bigr) \\
&= x_1\bigl((1+2x_1) - (3 - 4x_1 + 4x_1^2)\bigr) \\
&= x_1(-2 + 6x_1 - 4x_1^2) \\
&= -2x_1(2x_1^2 - 3x_1 + 1) \\
&= -2x_1(2x_1 - 1)(x_1 - 1).
\end{aligned}
$$

The fixed points are the solutions of $\frac{dx_1}{dt}=0$:
$$
x_1 \in \{0,\tfrac12,1\}.
$$


The above answers the question, below is some code to cofirm:

```{code-cell} python3
import sympy as sym

x_1 = sym.Symbol("x_1")

f_A = 1 + 2 * x_1
f_B = 1 + 2 * (1 - x_1)
phi = x_1 * f_A + (1 - x_1) * f_B
sym.simplify(phi)
```

```{code-cell} python3
x_1_dash = x_1 * (f_A - phi)
sym.simplify(x_1_dash)
```

```{code-cell} python3
x_1_dash = x_1 * (f_A - phi)
sym.solveset(x_1_dash, x_1)
```

7. We use the replicator equation from Question 6:

$$
\dot x_1 = \frac{dx_1}{dt}
= -2x_1(2x_1 - 1)(x_1 - 1).
$$

Euler’s method with step size $h=0.01$ gives
$$
x_1^{(1)} = x_1^{(0)} + h\,\dot x_1\big|_{x_1^{(0)}}.
$$

- (a) Initial population $x=(0.01,0.99)$

Here $x_1^{(0)}=0.01$:

$$
\begin{aligned}
\dot x_1\big|_{0.01}
&= -2\cdot 0.01\cdot(2\cdot 0.01 - 1)\cdot(0.01 - 1) \\
&= -2\cdot 0.01\cdot(-0.98)\cdot(-0.99) \\
&\approx -0.019404.
\end{aligned}
$$

Thus

$$
x_1^{(1)}
=
0.01 + 0.01(-0.019404)
\approx 0.009806.
$$


**Interpretation:**  
The proportion of $A$–users decreases further from $0.01$ to about $0.0098$.
This shows that, starting near the pure $B$ population, the dynamics move even
closer to $(0,1)$, confirming that the all–$B$ population is evolutionarily
stable in this model.

The above answers the question, here is some code to confirm the calculations.

```{code-cell} python3
h = 0.01
initial_x_1 = 0.01
initial_x_1 + h * x_1_dash.subs({x_1: initial_x_1})
```

- (b) Initial population $x=(0.49,0.51)$

Here $x_1^{(0)}=0.49$:

$$
\begin{aligned}
\dot x_1\big|_{0.49}
&= -2\cdot 0.49\cdot(2\cdot 0.49 - 1)\cdot(0.49 - 1) \\
&= -2\cdot 0.49\cdot(-0.02)\cdot(-0.51) \\
&\approx -0.009996.
\end{aligned}
$$

So

$$
x_1^{(1)}
=
0.49 + 0.01(-0.009996)
\approx 0.489900.
$$

**Interpretation:**  
Starting slightly below the mixed state $(\tfrac12,\tfrac12)$, the proportion
of $A$–users decreases further (from $0.49$ to about $0.4899$). A small
perturbation away from the mixed state does not return; instead it is pushed
further away. This indicates that the mixed state is **not** evolutionarily
stable.

The above answers the question, here is some code to confirm the calculations.

```{code-cell} python3
h = 0.01
initial_x_1 = 0.49
initial_x_1 + h * x_1_dash.subs({x_1: initial_x_1})
```

- Initial population $x=(0.99,0.01)$

Here $x_1^{(0)}=0.99$:

$$
\begin{aligned}
\dot x_1\big|_{0.99}
&= -2\cdot 0.99\cdot(2\cdot 0.99 - 1)\cdot(0.99 - 1) \\
&= -2\cdot 0.99\cdot(0.98)\cdot(-0.01) \\
&\approx 0.019404.
\end{aligned}
$$

Thus

$$
x_1^{(1)}
=
0.99 + 0.01(0.019404)
\approx 0.990194.
$$

**Interpretation:**  
The proportion of $A$–users increases slightly from $0.99$ to about $0.9902$.
Starting near the pure $A$ population, the dynamics move even closer to
$(1,0)$, showing that the all–$A$ population is also evolutionarily stable.


The above answers the question, here is some code to confirm the calculations.

```{code-cell} python3
h = 0.01
initial_x_1 = 0.99
initial_x_1 + h * x_1_dash.subs({x_1: initial_x_1})
```

Overall, the dynamics push the population towards one of the two pure
coordination states, and away from the mixed state.


7. We now let the strength of the coordination benefit be a parameter $a\neq 0$:
$$
f_A(x)=1+a x_1,
\qquad
f_B(x)=1+a(1-x_1).
$$

- (a) Replicator dynamics for general $a$

The average fitness is

$$
\begin{aligned}
\phi(x)
&= x_1 f_A(x) + (1-x_1) f_B(x) \\
&= x_1(1+a x_1) + (1-x_1)\bigl(1+a(1-x_1)\bigr) \\
&= 2a x_1^2 - 2a x_1 + a + 1.
\end{aligned}
$$

Then

$$
\begin{aligned}
f_A(x) - \phi(x)
&= (1 + a x_1) - (2a x_1^2 - 2a x_1 + a + 1) \\
&= a(-2x_1^2 + 3x_1 - 1) \\
&= -a(2x_1-1)(x_1-1).
\end{aligned}
$$

Thus the replicator dynamics is

$$
\frac{dx_1}{dt}
=
x_1\bigl(f_A(x) - \phi(x)\bigr)
=
-a\,x_1(2x_1-1)(x_1-1).
$$

The fixed points satisfy $\frac{dx_1}{dt}=0$, so again
$$
x_1 \in \{0,\tfrac12,1\}.
$$

To determine stability, we can consider all potential post entry populations or
we can equivalently examine the sign of $\dot x_1$:

First let us consider the case $a>0$:

- For $0<x_1<\tfrac12$:  
  $x_1>0$, $2x_1-1<0$, $x_1-1<0$ so  
  $-ax_1(2x_1-1)(x_1-1)>0$.  
  Thus for the post entry population $x_1=1/2-\epsilon$ $x_1(t)$ decreases and the flow moves away from $x_1=\tfrac12$
  towards $x_1=0$.

- For $\tfrac12<x_1<1$:  
  $x_1>0$, $2x_1-1>0$, $x_1-1<0$ so  
  $-ax_1(2x_1-1)(x_1-1)<0$.  
  Thus for the post entry population $x_1=1/2+\epsilon$ $x_1(t)$ increases and the flow moves away from $x_1=\tfrac12$
  towards $x_1=1$.

Hence:

- $x_1=\tfrac12$ is **unstable**;
- $x_1=0$ and $x_1=1$ are **evolutionary stable**.

Now let us consider the case $a<0$:

- For $0<x_1<\tfrac12$:  
  $x_1>0$, $2x_1-1<0$, $x_1-1<0$ so  
  $-ax_1(2x_1-1)(x_1-1)<0$.  
  Thus for the post entry population $x_1=1/2-\epsilon$ $x_1(t)$ increases and the flow moves towards from $x_1=\tfrac12$.

- For $\tfrac12<x_1<1$:  
  $x_1>0$, $2x_1-1>0$, $x_1-1<0$ so  
  $-ax_1(2x_1-1)(x_1-1)<0$.  
  Thus for the post entry population $x_1=1/2+\epsilon$ $x_1(t)$ decreases and the flow moves towards from $x_1=\tfrac12$.

If $a=0$ the derivative is 0 and thus all populations are stable.

Hence:

- $x_1=\tfrac12$ is **evolutionary stable**;
- $x_1=0$ and $x_1=1$ are **stable**.


So $x^*=(1/2, 1/2)$ is an evolutionary stable strategy if and only if $a<0$: the
network effect is bad. There will only ever be an emergent population using both
apps when the network effect is in fact negative.

The above answer the question. Here is some code to confirm the calculations and
illustrate the sign of the derivative.

```{code-cell} python3
a = sym.Symbol("a")
f_A = 1 + a * x_1
f_B = 1 + a * (1 - x_1)
phi = x_1 * f_A + (1 - x_1) * f_B
sym.simplify(phi)
```

```{code-cell} python3
x_1_dash = x_1 * (f_A - phi)
sym.simplify(x_1_dash)
```

```{code-cell} python3
x_1_dash = x_1 * (f_A - phi)
sym.solveset(x_1_dash, x_1)
```

```{code-cell} python3
import matplotlib.pyplot as plt
import numpy as np

x_1 = sym.Symbol("x_1")

a = sym.Symbol("a")
f_A = 1 + a * x_1
f_B = 1 + a * (1 - x_1)
phi = x_1 * f_A + (1 - x_1) * f_B
x_1_dash = x_1 * (f_A - phi)
x_1_values = np.linspace(0, 1, 100)

plt.figure()
plt.plot(x_1_values, [x_1_dash.subs({x_1: x_value, a: -1}) for x_value in x_1_values], label="$a=-1$")
plt.plot(x_1_values, [x_1_dash.subs({x_1: x_value, a: -5}) for x_value in x_1_values], label="$a=-5$")
plt.plot(x_1_values, [x_1_dash.subs({x_1: x_value, a: 0}) for x_value in x_1_values], label="$a=0$")
plt.plot(x_1_values, [x_1_dash.subs({x_1: x_value, a: 1}) for x_value in x_1_values], label="$a=1$")
plt.plot(x_1_values, [x_1_dash.subs({x_1: x_value, a: 5}) for x_value in x_1_values], label="$a=5$")
plt.legend()
plt.xlabel("$x_1$")
plt.ylabel(r"$\frac{dx_1}{dt}$")
```
````
