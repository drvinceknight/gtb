---
kernelspec:
  name: python3
  display_name: "Python 3"
---

(solutions:moran_process)=

# Solutions: Moran Process Exercises

````{solution} moran_process:exam_style_1
:label: solution:moran_process:exam_style_1

1. The standard definition of the [Prisoners Dilemma](#def:prisoners-dilemma) is:

$$
M_r = 
\begin{pmatrix}
    R & T\\
    S & P
\end{pmatrix}
$$

with $T > R > P > S$ and $2r > T + S$. In this case we have:

$$R=3a\qquad T=2a \qquad S= \qquad P=2$$

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
\gamma_i = \frac{i(2a - 2) + 2}{2ai - 2} = \frac{2ai-2i + 2}{2ai - a}
$$

This gives:

$$
\rho_1 = \frac{1}{1 + \gamma_1} = \frac{1}{1 + \frac{2a}{a}}=\frac{1}{1 + 2}=3
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

This shows that the amplification of the fitness (the increase of $\alpha$) has
a greater effect for larger $N$.
````
