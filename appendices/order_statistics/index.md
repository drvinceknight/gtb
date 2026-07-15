---
kernelspec:
  name: python3
  display_name: "Python 3"
numbering:
  enumerator: A6.%s
---

(app:order_statistics)=

# Appendix: Order Statistics

(sec:motivating_example_order_statistics)=

## Motivating Example: When Does the Meeting Start?

Five colleagues agree to meet during a one hour window. Each arrives at a
time chosen independently and uniformly at random within the window. The room
is unlocked as soon as the **first** person arrives, and the meeting starts
only when the **last** person arrives.

Two natural questions follow. On average, how long does the room sit unlocked
before the meeting starts? More precisely:

1. What is the expected arrival time of the first person?
2. What is the expected arrival time of the last person?

Both questions ask for the expected value of a **ranked** member of a random
sample: the smallest arrival time and the largest. Quantities of this kind
are called order statistics, and they can be computed exactly. This appendix
develops the tools needed to do so, in particular for values drawn uniformly
at random from an interval, which is the setting used in the
[Auction Games](#chp:auctions) chapter.

## Theory

### Definition: Probability Density and Cumulative Distribution Functions

---

A continuous random variable $X$ has a **probability density function** (pdf)
$f$ if for all $a \leq b$:

$$
\mathbb{P}(a \leq X \leq b) = \int_a^b f(x)\, dx
$$

The **cumulative distribution function** (cdf) of $X$ is:

$$
F(x) = \mathbb{P}(X \leq x) = \int_{-\infty}^x f(t)\, dt
$$

---

The two functions carry the same information: the cdf is the integral of the
pdf, and wherever $F$ is differentiable, $F'(x) = f(x)$. The **expected
value** of $X$ is:

$$
\mathbb{E}[X] = \int_{-\infty}^{\infty} x f(x)\, dx
$$

### Definition: The Uniform Distribution

---

A random variable $X$ is **uniform** on $[0, 1]$ if its pdf is $f(x) = 1$ for
$x \in [0, 1]$ and $0$ otherwise. Its cdf is:

$$
F(x) = \mathbb{P}(X \leq x) = x \qquad \text{for } x \in [0, 1]
$$

---

Every value in $[0, 1]$ is equally likely, and the expected value is:

$$
\mathbb{E}[X] = \int_0^1 x \cdot 1\, dx = \frac{1}{2}
$$

### Theorem: Expectation via the Survival Function

---

If $X$ takes values in $[0, 1]$ with cdf $F$ then:

$$
\mathbb{E}[X] = \int_0^1 \left(1 - F(x)\right) dx
$$

---

This follows from integration by parts:

$$
\int_0^1 x f(x)\, dx = \Bigl[x \bigl(F(x) - 1\bigr)\Bigr]_0^1
                     + \int_0^1 \left(1 - F(x)\right) dx
                     = \int_0^1 \left(1 - F(x)\right) dx
$$

since $F(1) = 1$ makes the boundary term vanish. The function $1 - F(x) =
\mathbb{P}(X > x)$ is called the **survival function**, and this form of the
expectation is often the quickest route to expected minima, as the next
results show.

### Definition: Order Statistics

---

Let $X_1, X_2, \dots, X_N$ be independent random variables, each with cdf
$F$. The **order statistics** $X_{(1)} \leq X_{(2)} \leq \dots \leq X_{(N)}$
are the same values sorted into increasing order: $X_{(k)}$ is the $k$-th
smallest of the sample. In particular:

$$
X_{(1)} = \min_i X_i \qquad \text{and} \qquad X_{(N)} = \max_i X_i
$$

---

### Theorem: CDF of the Maximum and the Minimum

---

Let $X_1, \dots, X_N$ be independent, each with cdf $F$. Then:

$$
F_{(N)}(x) = \mathbb{P}\left(\max_i X_i \leq x\right) = F(x)^N
$$

$$
F_{(1)}(x) = \mathbb{P}\left(\min_i X_i \leq x\right) = 1 - (1 - F(x))^N
$$

---

The first statement holds because the maximum is at most $x$ precisely when
**every** $X_i$ is at most $x$, and by independence these $N$ events have
probability $F(x)^N$ jointly. Similarly the minimum exceeds $x$ precisely
when every $X_i$ exceeds $x$, so $\mathbb{P}(\min_i X_i > x) = (1 - F(x))^N$,
and the cdf of the minimum is the complement.

### Example: Two Uniform Values

Let $v_1$ and $v_2$ be independent and uniform on $[0, 1]$. This is the
setting of a two bidder auction with uniform valuations. We compute the
expected values of $\max(v_1, v_2)$ and $\min(v_1, v_2)$.

**The maximum.** With $F(x) = x$ and $N = 2$ the cdf of the maximum is
$F_{(2)}(x) = x^2$, so its pdf is $f_{(2)}(x) = 2x$ and:

$$
\mathbb{E}[\max(v_1, v_2)] = \int_0^1 x \cdot 2x\, dx = \frac{2}{3}
$$

**The minimum.** The survival function of the minimum is
$\mathbb{P}(\min(v_1, v_2) > x) = (1 - x)^2$, so by
expectation via the survival function:

$$
\mathbb{E}[\min(v_1, v_2)] = \int_0^1 (1 - x)^2\, dx = \frac{1}{3}
$$

As a check, $\min(v_1, v_2) + \max(v_1, v_2) = v_1 + v_2$, so the two
expectations must sum to $\mathbb{E}[v_1] + \mathbb{E}[v_2] = 1$, and indeed
$\frac{1}{3} + \frac{2}{3} = 1$. A further consequence, by linearity of
expectation, is the expected gap between the two values:

$$
\mathbb{E}\left|v_1 - v_2\right|
= \mathbb{E}[\max(v_1, v_2)] - \mathbb{E}[\min(v_1, v_2)]
= \frac{1}{3}
$$

### Theorem: Expected Order Statistics of the Uniform Distribution

---

Let $X_1, \dots, X_N$ be independent and uniform on $[0, 1]$. The $k$-th
order statistic has pdf:

$$
f_{(k)}(x) = N \binom{N - 1}{k - 1} x^{k - 1} (1 - x)^{N - k}
$$

and expected value:

$$
\mathbb{E}\left[X_{(k)}\right] = \frac{k}{N + 1}
$$

---

The form of the pdf can be read off directly: for $X_{(k)}$ to sit at $x$,
one of the $N$ values must land at $x$ (a factor of $N f(x) = N$), and of the
remaining $N - 1$ values, some $k - 1$ must fall below $x$ (each with
probability $x$) and the other $N - k$ above (each with probability $1 - x$),
with $\binom{N - 1}{k - 1}$ ways to choose which. The expectation then
follows from the Beta integral:

$$
\int_0^1 x^a (1 - x)^b\, dx = \frac{a!\, b!}{(a + b + 1)!}
$$

applied with $a = k$ and $b = N - k$:

$$
\mathbb{E}\left[X_{(k)}\right]
= N \binom{N - 1}{k - 1} \int_0^1 x^{k} (1 - x)^{N - k}\, dx
= N \binom{N - 1}{k - 1} \frac{k!\,(N - k)!}{(N + 1)!}
= \frac{k}{N + 1}
$$

The result has a pleasing interpretation: $N$ uniform points split $[0, 1]$
into $N + 1$ gaps, and by symmetry each gap has expected length
$\frac{1}{N + 1}$. The expected order statistics are therefore evenly spaced:
$\frac{1}{N + 1}, \frac{2}{N + 1}, \dots, \frac{N}{N + 1}$. Setting $k = 1$
and $k = N$ recovers the expected minimum and maximum:

$$
\mathbb{E}\left[\min_i X_i\right] = \frac{1}{N + 1}
\qquad \text{and} \qquad
\mathbb{E}\left[\max_i X_i\right] = \frac{N}{N + 1}
$$

This answers the questions of
[](#sec:motivating_example_order_statistics): with $N = 5$ colleagues, the
room is unlocked at $\frac{1}{6}$ of the window on average (10 minutes in),
and the meeting starts at $\frac{5}{6}$ (50 minutes in), so the room sits
unlocked for an expected 40 minutes before the meeting begins.

## Exercises

```{exercise}
:label: order_statistics:exercise_1

Let $v_1$ and $v_2$ be independent and uniform on $[0, 1]$.

1. Write down the cdf of $\min(v_1, v_2)$ and differentiate it to obtain the
   pdf.
2. Use the pdf to compute $\mathbb{E}[\min(v_1, v_2)]$ directly, and confirm
   it agrees with the survival function calculation.
3. Without further integration, deduce $\mathbb{E}[\max(v_1, v_2)]$ from
   $\mathbb{E}[v_1 + v_2]$.
```

```{exercise}
:label: order_statistics:exercise_2

Let $X_1, X_2, X_3$ be independent and uniform on $[0, 1]$.

1. Compute the expected values of all three order statistics.
2. Verify that the four gaps ($0$ to $X_{(1)}$, $X_{(1)}$ to $X_{(2)}$,
   $X_{(2)}$ to $X_{(3)}$, and $X_{(3)}$ to $1$) all have the same expected
   length.
3. What is the expected value of the median of the sample?
```

```{exercise}
:label: order_statistics:exercise_3

Using the pdf of the $k$-th order statistic and the Beta integral, verify the
formula $\mathbb{E}\left[X_{(k)}\right] = \frac{k}{N + 1}$ explicitly in the
case $N = 4$, $k = 3$.
```

```{exercise}
:label: order_statistics:exercise_4

Let $X_1, \dots, X_N$ be independent exponential random variables, each with
survival function $\mathbb{P}(X_i > x) = e^{-\lambda x}$ for $x \geq 0$.

1. Show that $\min_i X_i$ is exponential with rate $N\lambda$.
2. Hence write down $\mathbb{E}\left[\min_i X_i\right]$, given that an
   exponential random variable with rate $\mu$ has expected value
   $\frac{1}{\mu}$.
```

## Programming

The expectations in this appendix are integrals that Sympy can evaluate
symbolically. Here is the expected maximum and minimum of two uniform values,
using the pdf of the maximum and the survival function of the minimum:

```{code-cell} python3
import sympy as sym

x = sym.Symbol("x", positive=True)

expected_max = sym.integrate(x * 2 * x, (x, 0, 1))
expected_min = sym.integrate((1 - x) ** 2, (x, 0, 1))
expected_max, expected_min
```

The general formula for the $k$-th order statistic of $N$ uniform values can
be checked in the same way:

```{code-cell} python3
N, k = sym.symbols("N k", positive=True, integer=True)

pdf_k = N * sym.binomial(N - 1, k - 1) * x ** (k - 1) * (1 - x) ** (N - k)
expected_k = sym.simplify(sym.integrate(x * pdf_k, (x, 0, 1)))
expected_k
```

Numerical simulation gives an independent confirmation. Numpy's `sort` sorts
each sample, so column $k - 1$ of the sorted array holds the $k$-th order
statistic:

```{code-cell} python3
import numpy as np

rng = np.random.default_rng(seed=0)
number_of_samples = 100_000
sample_size = 5

samples = rng.uniform(size=(number_of_samples, sample_size))
sorted_samples = np.sort(samples, axis=1)

for k in range(1, sample_size + 1):
    estimate = sorted_samples[:, k - 1].mean()
    exact = k / (sample_size + 1)
    print(f"k = {k}:  simulated {estimate:.4f},  exact {exact:.4f}")
```

## Notable Research

The systematic study of order statistics grew out of early twentieth century
work on extremes. Fisher and Tippett [@fisher1928limiting] characterised the
possible limiting distributions of the maximum of a large sample, a result
completed by Gnedenko [@gnedenko1943sur]; together these form the foundation
of extreme value theory, which underpins modern models of floods, heatwaves,
and financial risk.

Rényi [@renyi1953theory] gave an elegant representation of the order
statistics of an exponential sample as a sum of independent scaled
exponentials. This representation remains a standard tool for deriving the
joint behaviour of order statistics.

The standard modern references are the monograph of David and Nagaraja
[@david2003order], which surveys the field, and the more introductory
treatment of Arnold, Balakrishnan and Nagaraja [@arnold2008first].

In game theory, expected order statistics of uniform samples are exactly what
is needed to compute expected revenue in auctions: the winner's payment in a
second-price auction is the second highest valuation. This connection goes
back to Vickrey [@vickrey1961counterspeculation], whose analysis of sealed
bid auctions is discussed in the [Auction Games](#chp:auctions) chapter.

## Conclusion

For independent values with a common cdf $F$, the maximum has cdf $F(x)^N$
and the minimum has survival function $(1 - F(x))^N$; expectations then
follow by integrating the pdf, or the survival function directly.
[](#tbl:order_statistics_summary) collects the key facts for the uniform
distribution on $[0, 1]$.

```{table} Order statistics of $N$ independent uniform values on $[0, 1]$.
:name: tbl:order_statistics_summary
:align: center

| Quantity                        | Value                              |
|---------------------------------|------------------------------------|
| cdf of $\max_i X_i$             | $x^N$                              |
| cdf of $\min_i X_i$             | $1 - (1 - x)^N$                    |
| $\mathbb{E}[X_{(k)}]$           | $\frac{k}{N + 1}$                  |
| $\mathbb{E}[\max_i X_i]$        | $\frac{N}{N + 1}$                  |
| $\mathbb{E}[\min_i X_i]$        | $\frac{1}{N + 1}$                  |
| $\mathbb{E}\left|X_1 - X_2\right|$ ($N=2$) | $\frac{1}{3}$           |
```

```{important}
These expectations are used in the [Auction Games](#chp:auctions) chapter to
compute the expected revenue of first and second price auctions: with $N$
bidders, the second price auction raises the expected second highest
valuation $\frac{N - 1}{N + 1}$, and revenue equivalence shows the first
price auction raises the same amount.
```

---

(solutions:order_statistics)=

## Solutions

````{solution} order_statistics:exercise_1
:label: solution:order_statistics:exercise_1

1. The minimum is at most $x$ unless both values exceed $x$:

$$
F_{(1)}(x) = 1 - (1 - x)^2 \qquad \text{for } x \in [0, 1]
$$

Differentiating gives the pdf:

$$
f_{(1)}(x) = 2(1 - x)
$$

2. Using the pdf:

$$
\mathbb{E}[\min(v_1, v_2)] = \int_0^1 x \cdot 2(1 - x)\, dx
= 2\left(\frac{1}{2} - \frac{1}{3}\right) = \frac{1}{3}
$$

which agrees with the survival function calculation
$\int_0^1 (1 - x)^2\, dx = \frac{1}{3}$.

3. Since $\min(v_1, v_2) + \max(v_1, v_2) = v_1 + v_2$, taking expectations
gives:

$$
\mathbb{E}[\max(v_1, v_2)] = \mathbb{E}[v_1] + \mathbb{E}[v_2]
- \mathbb{E}[\min(v_1, v_2)] = \frac{1}{2} + \frac{1}{2} - \frac{1}{3}
= \frac{2}{3}
$$

```{code-cell} python3
import sympy as sym

x = sym.Symbol("x", positive=True)
pdf_min = sym.diff(1 - (1 - x) ** 2, x)
sym.integrate(x * pdf_min, (x, 0, 1))
```
````

````{solution} order_statistics:exercise_2
:label: solution:order_statistics:exercise_2

1. With $N = 3$ the expected order statistics are $\frac{k}{N + 1} =
\frac{k}{4}$:

$$
\mathbb{E}[X_{(1)}] = \frac{1}{4} \qquad
\mathbb{E}[X_{(2)}] = \frac{2}{4} = \frac{1}{2} \qquad
\mathbb{E}[X_{(3)}] = \frac{3}{4}
$$

2. The expected gap lengths are:

$$
\frac{1}{4} - 0 = \frac{1}{2} - \frac{1}{4} = \frac{3}{4} - \frac{1}{2}
= 1 - \frac{3}{4} = \frac{1}{4}
$$

so all four gaps have the same expected length $\frac{1}{4}$, as the symmetry
argument predicts.

3. The median of three values is the second order statistic, so its expected
value is $\frac{1}{2}$.

```{code-cell} python3
import numpy as np

rng = np.random.default_rng(seed=0)
sorted_samples = np.sort(rng.uniform(size=(100_000, 3)), axis=1)
sorted_samples.mean(axis=0)
```
````

````{solution} order_statistics:exercise_3
:label: solution:order_statistics:exercise_3

With $N = 4$ and $k = 3$ the pdf is:

$$
f_{(3)}(x) = 4 \binom{3}{2} x^{2} (1 - x) = 12 x^2 (1 - x)
$$

so the expected value is:

$$
\mathbb{E}[X_{(3)}] = \int_0^1 12 x^3 (1 - x)\, dx
= 12 \left(\frac{1}{4} - \frac{1}{5}\right) = \frac{12}{20} = \frac{3}{5}
$$

which agrees with $\frac{k}{N + 1} = \frac{3}{5}$. Equivalently, the Beta
integral with $a = 3$ and $b = 1$ gives $\int_0^1 x^3(1 - x)\, dx =
\frac{3!\, 1!}{5!} = \frac{1}{20}$.

```{code-cell} python3
import sympy as sym

x = sym.Symbol("x", positive=True)
sym.integrate(x * 12 * x ** 2 * (1 - x), (x, 0, 1))
```
````

````{solution} order_statistics:exercise_4
:label: solution:order_statistics:exercise_4

1. The minimum exceeds $x$ precisely when all $N$ values do, so by
independence:

$$
\mathbb{P}\left(\min_i X_i > x\right) = \left(e^{-\lambda x}\right)^N
= e^{-N \lambda x}
$$

which is the survival function of an exponential random variable with rate
$N\lambda$.

2. Hence:

$$
\mathbb{E}\left[\min_i X_i\right] = \frac{1}{N \lambda}
$$

The more competitors there are, the sooner the first event occurs, in exact
inverse proportion.
````
