---
kernelspec:
  name: python3
  display_name: "Python 3"
---

(chp:auctions)=

# Auctions

Auctions allocate goods to the bidders who value them most, without the seller
needing to know those values. This chapter analyses first- and second-price
sealed-bid auctions, deriving equilibrium bidding strategies and the
surprising revenue equivalence between the two formats.

(sec:motivating_example_bidding_for_backstage_passes)=

## Motivating Example: Bidding for backstage passes

A popular band, **The Algorithms**, is playing a one-night-only concert in Cardiff.  
To raise money for charity, the band is auctioning off a single **backstage pass**.

> Three fans — Alex, Casey, and Jordan — are each secretly asked to submit a sealed bid  
> for how much they are willing to pay for the pass. The highest bidder will win the  
> auction, but they will only pay **the second-highest bid**.

This is a **second-price sealed-bid auction**, often called a **Vickrey auction**.

Each fan has a private valuation for the backstage pass:

- Alex values it at £150 (they once wrote a fan algorithm about them).
- Casey values it at £100 (they’re mainly here for the snacks).
- Jordan values it at £75 (they like the early albums).

Suppose the bids submitted are:

- Alex bids £150
- Casey bids £100
- Jordan bids £60

Then Alex wins — but only pays £100, the second-highest bid.

This setup has an interesting strategic property:
**bidding your true value is a dominant strategy**.
Even if Alex knew the other bids, they could not do better
by bidding higher or lower than £150.

We'll explore why this is the case formally in what follows.

## Theory

### Definition: Auction Game

---

An **auction game** with $N$ players (or bidders) is defined by:

- A set of random variables $V_i$, for $1 \leq i \leq N$, from which each player’s  
  private valuation $v_i$ for the good is drawn.
- A set of possible bids $b_i \in B_i$, where $b_i$ is typically the output of a  
  bidding strategy $\mathcal{b}_i: V_i \to B_i$ that maps valuations to bids.
- An **allocation rule**  
  $q: B_1 \times B_2 \times \dots \times B_N \to [0,1]^N$,  
  which determines the probability with which each player receives the good.  
  Often, this output is a deterministic vector with a single 1 (winner) and the  
  remaining entries 0.
- A **payment rule**  
  $p: B_1 \times B_2 \times \dots \times B_N \to \mathbb{R}^N$,  
  which determines how much each player pays as a function of all bids.

The utility of player $i$ is then given by:

$$
u_i = v_i \cdot q_i - p_i
$$

where $q_i$ is the allocation to player $i$, and $p_i$ is their payment.

---

#### Example: The Auction Game for backstage passes

In [](#sec:motivating_example_bidding_for_backstage_passes),  
the auction game is defined with $N = 3$ players:

- The sampled valuations are: $v_1 = 150$, $v_2 = 100$, $v_3 = 75$.
- The chosen bids are: $b_1 = 150$, $b_2 = 100$, $b_3 = 60$.
- The allocation rule:

  $$
  q_i(b) =
  \begin{cases}
  1 & \text{if } i = \arg\max_{j} b_j \\
  0 & \text{otherwise}
  \end{cases}
  $$

- The payment rule:

  $$
  p_i(b) =
  \begin{cases}
  \max \{ b_j : b_j < \max_k b_k \} & \text{if } i = \arg\max_{j} b_j \\
  0 & \text{otherwise}
  \end{cases}
  $$

The resulting utilities for each player are:

- Alex: $u_1 = 150 \cdot 1 - 100 = 50$
- Casey: $u_2 = 100 \cdot 0 - 0 = 0$
- Jordan: $u_3 = 75 \cdot 0 - 0 = 0$

```{note}
For a different set of sampled valuations, the outcome could be entirely
different. To study equilibrium behaviour in such settings, we will need new
tools that can model beliefs and stochastic reasoning.
```

### Definition: Bayesian Nash Equilibrium

A **Bayesian Nash equilibrium** is a strategy profile in a game with incomplete  
information such that, given their own type, each player's strategy maximizes  
their expected utility assuming the strategies of the other players are fixed  
and that beliefs about types are correct.

### Theorem: Bayesian Nash Equilibrium for Second Pay Auction

In a second price auction the Bayesian Nash equilibrium is for all players to bid
their value:

$$b_i = v_i$$

**Proof**

Let us consider the strategy $b_i(v_i) = v_i$ — that is, player $i$ bids truthfully.

We show that this is a **best response** to all other players also bidding truthfully.

Fix a valuation $v_i$ for player $i$. Let $b_i$ denote the bid player $i$ chooses  
(possibly different from $v_i$). Let $b_{(1)}^{(-i)}$ and $b_{(2)}^{(-i)}$ denote  
the highest and second-highest bids among the other players.

We compute the **expected utility** of deviating from $b_i=v_i$ to $b_i\ne v_i$:

$$
\mathbb{E}[u_i] = \text{prob}(\text{Win})(v_i - b_{(2)}^{-1})
$$

Let us distinguish two cases:

---

**Case 1:** $b_i < v_i$ (the deviation is to a lower bid than the value)
This deviation will cause $\text{prob}(\text{Win})$ to either:

- remain the same in which case $b_{(2)}^{-1}$ also remains the same. There is no
  change in utility.
- become 0, the utility does not increase.

This causes a loss in expected utility compared to bidding $v_i$.

---

**Case 2:** $b_i > v_i$ (the deviation is to a higher bid than the value)

This deviation cases no change in $\text{prob}(\text{Win})$ and no change in the
overall utility.

---

Thus, **bidding anything other than $v_i$ weakly decreases expected utility**,  
Hence, bidding truthfully maximizes expected utility **for all $v_i$**, given  
that others bid truthfully.

Therefore, truthful bidding is a **Bayesian Nash equilibrium**.

(theorem_bayesian_ne_for_first_price_auction)=

### Theorem: Bayesian Nash equilibrium in a first-price auction with uniform values

---

In a first-price auction with $N$ players, where each valuation $v_i$ is drawn  
independently from $\text{Unif}[0, 1]$, the Bayesian Nash equilibrium is for  
each player to **shade their bid** according to:

$$
b_i = \frac{N - 1}{N}v_i
$$

---

**Proof**

Suppose all players follow the bidding strategy:

$$
b_j = \frac{N - 1}{N}v_j \quad \text{for all } j \ne i
$$

Now consider a deviation by player $i$ who bids $\bar{b} \ne \frac{N - 1}{N}v_i$.

Let us compute the **expected utility** for player $i$ from this deviation.

Player $i$ wins if their bid $\bar{b}$ is higher than the bids of all  
other players, and receives utility equal to $v_i - \bar{b}$. If they lose,  
they get zero utility. Thus:

$$
\begin{aligned}
\mathbb{E}[u_i] &= \Pr(\text{Win}) \cdot (v_i - \bar{b})
\end{aligned}
$$

Since all other players are bidding truthfully according to  
$b_j = \frac{N - 1}{N}v_j$, and $v_j \sim \text{Unif}[0, 1]$, we find:

$$
\begin{aligned}
\Pr(\text{Win}) &= \Pr\left( \bar{b} \geq \frac{N - 1}{N}v_j \text{ for all } j \ne i \right) \\
&= \Pr\left( v_j \leq \frac{N}{N - 1} \bar{b} \text{ for all } j \ne i \right) \\
&= \prod_{j \ne i} \Pr\left( v_j \leq \frac{N}{N - 1} \bar{b} \right) \quad \text{(independence)} \\
&= \left( F\left( \frac{N}{N - 1} \bar{b} \right) \right)^{N - 1} \\
&= \left( \frac{N}{N - 1} \bar{b} \right)^{N - 1} \quad \text{(CDF of } \text{Unif}[0,1])
\end{aligned}
$$

Hence, expected utility becomes:

$$
\mathbb{E}[u_i] = \left( \frac{N}{N - 1} \right)^{N - 1} \bar{b}^{N - 1} (v_i - \bar{b})
$$

To find the optimal deviation, we take the derivative of expected utility  
with respect to $\bar{b}$:

$$
\begin{aligned}
\frac{d\mathbb{E}[u_i]}{d\bar{b}} &= \left( \frac{N}{N - 1} \right)^{N - 1}
\cdot \frac{d}{d\bar{b}} \left( \bar{b}^{N - 1}(v_i - \bar{b}) \right) \\
&= \left( \frac{N}{N - 1} \right)^{N - 1}
\left( (N - 1) \bar{b}^{N - 2}(v_i - \bar{b}) - \bar{b}^{N - 1} \right)
\end{aligned}
$$

Setting this derivative equal to zero gives a necessary condition for optimality:

$$
\begin{aligned}
(N - 1) \bar{b}^{N - 2}(v_i - \bar{b}) - \bar{b}^{N - 1} &= 0 \\
(N - 1)(v_i - \bar{b}) - \bar{b} &= 0 \quad \text{(divide by } \bar{b}^{N - 2} \ne 0) \\
(N - 1)v_i - N\bar{b} &= 0 \\
\bar{b} &= \frac{N - 1}{N} v_i
\end{aligned}
$$

Thus, any deviation $\bar{b} \ne \frac{N - 1}{N}v_i$ does not improve utility.

---

## Exercises

---

```{exercise} 
:label: dominant-strategies-in-second-price-auctions

In a second-price auction with two players whose private valuations are:

- Player 1: $v_1 = 0.8$
- Player 2: $v_2 = 0.6$

Each player submits a sealed bid. Show that bidding truthfully is a  
dominant strategy for each player, and compute the resulting allocation,  
payment, and utility.
```

---

```{exercise} 
:label: overbidding-and-underbidding

Consider a second-price auction with $v_1 = 0.9$, $v_2 = 0.7$, and $v_3 = 0.5$.

Suppose Player 1 deviates and bids $b_1 = 1.0$, Player 2 bids truthfully,  
and Player 3 bids $b_3 = 0.6$.

- Who wins the auction?
- What is the price paid?
- What is Player 1's utility?
- Would Player 1 have been better off bidding truthfully?
```


```{exercise} 
:label: expected-utility-in-a-first-price-auction

Let $N = 2$ players, each with valuation $v_i \sim \text{Unif}[0,1]$,  
use the symmetric strategy $b_i = \frac{1}{2}v_i$.

Compute the expected utility of Player 1 as a function of their value $v_1$.

_Hint: integrate over the opponent's valuation or bid._
```

---

```{exercise} 
:label: best-response-derivation

Using the first-price auction model with $v_i \sim \text{Unif}[0,1]$  
and the assumption that all other players bid $b_j = \alpha v_j$,  
show that the best response of Player $i$ is to bid  
$b_i = \frac{N - 1}{N}v_i$ when $\alpha = \frac{N - 1}{N}$.
```

---

```{exercise} 
:label: generalising-beyond-uniform

Suppose players' values are drawn from an exponential distribution  
with CDF $F(v) = 1 - e^{-\lambda v}$, and each player bids  
$b_i = \beta v_i$ in a first-price auction.

- Derive the probability of winning for a given bid $\bar{b}$.
- Derive the expected utility and determine the value of $\beta$  
  that maximises expected utility for $N = 2$.

_Challenge: compare the optimal $\beta$ to the uniform case._

```

```{exercise} 
:label: revenue_equivalence

Suppose there are $N$ symmetric bidders with valuations $v_i \sim \text{Unif}[0,1]$,  
drawn independently. In both the first-price and second-price sealed-bid auctions,  
assume all players follow the Bayesian Nash equilibrium bidding strategies:

- First-price: $b_i = \frac{N - 1}{N} v_i$
- Second-price: $b_i = v_i$

Let $R$ denote the expected revenue of the seller.

**Task:** Show that both mechanisms yield the same expected revenue:

$$
\mathbb{E}[R_{\text{first}}] = \mathbb{E}[R_{\text{second}}]
$$

_Hint:_  
In $\text{Unif}[0, 1]$, the expected value of the $k$-th order statistic (i.e., the $k$-th highest value) is:

$$
\mathbb{E}[v_{(k)}] = \frac{k}{N + 1}
$$
```

---

## Programming

There is a python library called `sold` which allows for the numeric simulation
of auctions. The code below builds the valuation distributions and bidding rules
for an auction with $N=3$
players where the first two players bid the true value and the third player uses
the strategy of [](#theorem_bayesian_ne_for_first_price_auction).

```{code-cell} python3
import scipy.stats
import numpy as np

import sold
import sold.allocate
import sold.bid
import sold.pay

N = 3
valuation_distributions = [scipy.stats.uniform() for _ in range(N)]
bidding_functions = [sold.bid.true_value for _ in range(N - 1)] + [
    sold.bid.create_shaded_bid_map((N - 1) / N)
]
```

Now let us simulate this 100 times to confirm that the shaded big strategy gets
a higher utility:

```{code-cell} python3
repetitions = 100
utilities = []
for seed in range(repetitions):
    allocation, payments, valuations = sold.auction(
        valuation_distributions=valuation_distributions,
        bidding_functions=bidding_functions,
        allocation_rule=sold.allocate.first_price,
        payment_rule=sold.pay.first_price,
        seed=seed,
    )
    utilities.append(valuations - allocation * payments)
mean_utilities = np.mean(utilities, axis=0)
mean_utilities
```

## Notable Research

One of the early important publications in this field is [@vickrey1961counterspeculation],
which not only introduced the second-price auction—often called the Vickrey auction—proving that
truth-telling is optimal, but also discusses the first-price auction. Vickrey was awarded the Nobel
Prize in Economics in 1996 for this foundational work.

Another foundational contribution is [@myerson1981optimal], which formulates the design of optimal
auctions, introduces the concept of virtual valuations, and proves a generalisation of the result
in [](#revenue_equivalence): the revenue equivalence theorem. This theorem shows
that all standard auctions yield the same expected revenue when bidders are risk-neutral and have
independent private values.

Auction theory is often described as one of game theory’s most successfully applied branches. A
striking example is the role of auctions in modern online advertising. This is exemplified in the
work of Google’s chief economist [@varian2007position], which provides a theoretical model of
position auctions—the type of auctions used to allocate advertising slots in search engines.

Further Nobel-recognised contributions to auction theory come from Paul Milgrom and Robert Wilson,
who were awarded the Nobel Prize in Economics in 2020. Their work extends auction theory to
settings where bidders' values are interdependent and shaped by shared information. Wilson’s early
work [@wilson1967competitive] developed models of bidding under common values, where bidders must
reason about both their own and others’ information. Milgrom built on this by analysing how
different auction formats perform in such settings [@milgrom1982theory], helping to guide the
design of real-world mechanisms. Together, they co-designed the simultaneous multiple-round auction
(SMRA) used to allocate radio spectrum, which has had significant practical impact.

## Conclusion

Auction theory provides a rigorous framework for understanding how goods and
resources can be allocated efficiently under conditions of incomplete
information. We've seen that second-price auctions promote truthful bidding as a
dominant strategy, while first-price auctions require bidders to strategically
shade their bids. The concept of Bayesian Nash equilibrium allows us to analyse
these strategies under uncertainty, and the revenue equivalence theorem links
together many of the most commonly used auction formats.

These results underpin some of the most economically significant allocation mechanisms in use today, from government spectrum sales to online advertising platforms.

[](#tbl:auction_summary) gives a summary of the concepts seen in this chapter as
well as a list of other auction types.

````{table} Different types of auctions and their properties
:label: tbl:auction_summary
:align: center
:class: table-bordered

```{table}
:align: center

| Auction Format         | Bidding Strategy          | Truthful? | Allocates to Highest Bidder? | Typical Use Case            |
|------------------------|---------------------------|-----------|-------------------------------|-----------------------------|
| Second-price sealed    | Bid your true value       | ✅        | ✅                            | eBay-style auctions         |
| First-price sealed     | Shade your bid            | ❌        | ✅                            | Procurement, real estate    |
| English (ascending)    | Stay in until your value  | ✅*       | ✅                            | Art, livestock auctions     |
| Dutch (descending)     | Accept before price drops | ❌        | ✅                            | Cut flowers, perishable goods |
| Position auction       | Rank-based bidding        | ❌        | ✅ (under assumptions)        | Online advertising (e.g., Google Ads) |
| All-pay auction        | Bid your value (often)    | ❌        | ✅                            | Tournaments, lobbying, rent-seeking |

*Truthful under private values and risk neutrality.
````

```{important}
Auction theory assumes that players form beliefs about other players’ valuations.
To analyse strategic behaviour under uncertainty, we use the concept of
**Bayesian Nash equilibrium**—an equilibrium defined in expectation.
This framework allows auctions to be designed in ways that incentivise truthful bidding.
```

---

(solutions:auction_games)=

## Solutions

````{solution} dominant-strategies-in-second-price-auctions
:label: solution:dominant-strategies-in-second-price-auctions

We have two players with valuations $v_1 = 0.8$ and $v_2 = 0.6$.

**Truthful bidding is a dominant strategy for each player.**

We show this for Player 1; the argument for Player 2 is identical by symmetry.

Fix an arbitrary bid $b_2$ from Player 2. Player 1 chooses bid $b_1$.

In a second-price auction, Player 1's utility is:

$$
u_1 =
\begin{cases}
v_1 - b_2 & \text{if } b_1 > b_2 \text{ (Player 1 wins and pays } b_2\text{)} \\
0          & \text{if } b_1 < b_2 \text{ (Player 1 loses)}
\end{cases}
$$

(Ties are broken arbitrarily; they occur on a set of measure zero.)

We consider two cases:

**Case 1: $b_2 < v_1 = 0.8$.**

- If $b_1 = v_1 = 0.8 > b_2$: Player 1 wins and receives $u_1 = v_1 - b_2 > 0$.
- If $b_1 < b_2$: Player 1 loses and receives $u_1 = 0$.
- If $b_1 > b_2$ (but $b_1 \ne v_1$): Player 1 still wins and still pays $b_2$.
  Utility is the same $v_1 - b_2 > 0$.

Bidding $v_1$ guarantees winning (and the positive surplus) whenever it is
profitable to do so. No deviation improves utility.

**Case 2: $b_2 > v_1 = 0.8$.**

- If $b_1 = v_1 = 0.8 < b_2$: Player 1 loses and receives $u_1 = 0$.
- If $b_1 > b_2$: Player 1 wins but pays $b_2 > v_1$, giving $u_1 = v_1 - b_2 < 0$.

Bidding $v_1$ correctly results in losing (utility 0), which is better than
winning at a loss. No deviation to a lower bid changes the outcome.

In all cases, deviating from $b_1 = v_1$ either leaves utility unchanged or
makes it worse. Hence $b_i = v_i$ is a **dominant strategy** for each player.

**Resulting allocation, payment, and utilities (with truthful bids):**

Both players bid their true values: $b_1 = 0.8$, $b_2 = 0.6$.

- Player 1 has the highest bid, so Player 1 **wins**.
- Payment: Player 1 pays the second-highest bid, which is $b_2 = 0.6$.
- Utilities:

$$
u_1 = v_1 - b_2 = 0.8 - 0.6 = 0.2, \qquad u_2 = 0.
$$

```{code-cell} python3
v1, v2 = 0.8, 0.6
b1, b2 = v1, v2  # truthful bids

winner = 1 if b1 > b2 else 2
price = min(b1, b2) if b1 > b2 else max(b1, b2)  # second-highest bid
price = b2 if winner == 1 else b1

u1 = (v1 - price) if winner == 1 else 0
u2 = (v2 - price) if winner == 2 else 0

print(f"Winner: Player {winner}")
print(f"Price paid: {price}")
print(f"Utility of Player 1: {u1}")
print(f"Utility of Player 2: {u2}")
```
````

````{solution} overbidding-and-underbidding
:label: solution:overbidding-and-underbidding

We have valuations $v_1 = 0.9$, $v_2 = 0.7$, $v_3 = 0.5$.

The bids submitted are $b_1 = 1.0$, $b_2 = 0.7$ (truthful), $b_3 = 0.6$.

**Who wins the auction?**

The highest bid is $b_1 = 1.0$, so **Player 1 wins**.

**What is the price paid?**

In a second-price auction the winner pays the second-highest bid:

$$
\text{price} = \max(b_2, b_3) = \max(0.7, 0.6) = 0.7.
$$

**What is Player 1's utility?**

$$
u_1 = v_1 - \text{price} = 0.9 - 0.7 = 0.2.
$$

**Would Player 1 have been better off bidding truthfully?**

If Player 1 bids $b_1 = v_1 = 0.9$ instead:

- $b_1 = 0.9 > b_2 = 0.7 > b_3 = 0.6$, so Player 1 still wins.
- Price paid: $\max(0.7, 0.6) = 0.7$ (unchanged, since it is determined by
  the other bids).
- Utility: $u_1 = 0.9 - 0.7 = 0.2$ (the same).

Player 1 would **not** have been better or worse off by bidding truthfully.
This illustrates the key property of second-price auctions: the winner's payment
depends only on others' bids, so overbidding above your value (when you already
win) does not affect the price you pay. Truthful bidding is weakly dominant.

```{code-cell} python3
v1, v2, v3 = 0.9, 0.7, 0.5
b1_deviate, b2, b3 = 1.0, 0.7, 0.6
b1_truthful = v1

def second_price_outcome(bids, valuations):
    winner = bids.index(max(bids))
    sorted_bids = sorted(bids, reverse=True)
    price = sorted_bids[1]
    utils = [v - price if i == winner else 0 for i, v in enumerate(valuations)]
    return winner + 1, price, utils

winner_d, price_d, utils_d = second_price_outcome(
    [b1_deviate, b2, b3], [v1, v2, v3]
)
winner_t, price_t, utils_t = second_price_outcome(
    [b1_truthful, b2, b3], [v1, v2, v3]
)

print("With overbid b1=1.0:")
print(f"  Winner: Player {winner_d}, Price: {price_d}, u1={utils_d[0]}")
print("With truthful bid b1=0.9:")
print(f"  Winner: Player {winner_t}, Price: {price_t}, u1={utils_t[0]}")
```
````

````{solution} expected-utility-in-a-first-price-auction
:label: solution:expected-utility-in-a-first-price-auction

We have $N = 2$ players with $v_i \sim \text{Unif}[0,1]$ using the symmetric
strategy $b_i = \frac{1}{2}v_i$.

**Expected utility of Player 1 as a function of $v_1$:**

Player 1 bids $b_1 = \frac{1}{2}v_1$. Player 2 bids $b_2 = \frac{1}{2}v_2$.

Player 1 wins if $b_1 > b_2$, i.e., $\frac{1}{2}v_1 > \frac{1}{2}v_2$, i.e., $v_2 < v_1$.

When Player 1 wins, they pay their own bid $b_1 = \frac{1}{2}v_1$ (first-price auction).
When Player 1 loses, they receive utility 0.

$$
\mathbb{E}[u_1 \mid v_1] = \Pr(v_2 < v_1)\cdot(v_1 - b_1) + \Pr(v_2 \geq v_1)\cdot 0
$$

Since $v_2 \sim \text{Unif}[0,1]$:

$$
\Pr(v_2 < v_1) = v_1
$$

Therefore:

$$
\mathbb{E}[u_1 \mid v_1] = v_1 \cdot \left(v_1 - \frac{1}{2}v_1\right) = v_1 \cdot \frac{v_1}{2} = \frac{v_1^2}{2}
$$

This can also be verified by integrating over $v_2$:

$$
\begin{align*}
\mathbb{E}[u_1 \mid v_1] \\
&= \int_0^{v_1} \left(v_1 - \frac{1}{2}v_1\right) dv_2 \\
&= \int_0^{v_1} \frac{v_1}{2}\, dv_2 \\
&= \frac{v_1}{2} \cdot v_1 \\
&= \frac{v_1^2}{2}.
\end{align*}
$$

So the expected utility of Player 1 is:

$$
\mathbb{E}[u_1 \mid v_1] = \frac{v_1^2}{2}
$$

```{code-cell} python3
import sympy as sym

v1, v2 = sym.symbols("v_1 v_2", positive=True)

b1 = sym.Rational(1, 2) * v1
b2 = sym.Rational(1, 2) * v2

# Utility when v2 < v1 (Player 1 wins): v1 - b1
utility_win = v1 - b1

# Integrate over v2 from 0 to v1
expected_utility = sym.integrate(utility_win, (v2, 0, v1))
sym.simplify(expected_utility)
```
````

````{solution} best-response-derivation
:label: solution:best-response-derivation

We have $N$ players with $v_i \sim \text{Unif}[0,1]$, and all other players bid
$b_j = \alpha v_j$ for some $\alpha > 0$. We derive the best response of Player $i$.

**Setting up the expected utility:**

Player $i$ bids $\bar{b}$. Player $i$ wins if $\bar{b} > b_j = \alpha v_j$ for all
$j \ne i$, i.e., if $v_j < \bar{b}/\alpha$ for all $j \ne i$.

Since $v_j \sim \text{Unif}[0,1]$ independently:

$$
\Pr(\text{Win}) = \prod_{j \ne i} \Pr\!\left(v_j < \frac{\bar{b}}{\alpha}\right) = \left(\frac{\bar{b}}{\alpha}\right)^{N-1}
$$

(assuming $\bar{b}/\alpha \leq 1$, i.e., $\bar{b} \leq \alpha$).

In a first-price auction, the winner pays their own bid, so:

$$
\mathbb{E}[u_i \mid v_i] = \left(\frac{\bar{b}}{\alpha}\right)^{N-1}(v_i - \bar{b})
$$

**Optimising over $\bar{b}$:**

$$
\begin{align*}
\frac{d}{d\bar{b}}\mathbb{E}[u_i] \\
&= \frac{1}{\alpha^{N-1}}\frac{d}{d\bar{b}}\left[\bar{b}^{N-1}(v_i - \bar{b})\right] \\
&= \frac{1}{\alpha^{N-1}}\left[(N-1)\bar{b}^{N-2}(v_i-\bar{b}) - \bar{b}^{N-1}\right]
\end{align*}
$$

Setting this equal to zero and dividing by $\bar{b}^{N-2} \ne 0$:

$$
(N-1)(v_i - \bar{b}) - \bar{b} = 0
$$

$$
(N-1)v_i = N\bar{b}
$$

$$
\bar{b}^* = \frac{N-1}{N}v_i
$$

**Confirming $\alpha = \frac{N-1}{N}$ yields a symmetric equilibrium:**

When $\alpha = \frac{N-1}{N}$, the best response of Player $i$ is to bid
$\frac{N-1}{N}v_i$, which equals $\alpha v_i$. Therefore, the strategy
$b_i = \frac{N-1}{N}v_i$ is a best response to all other players using the same
strategy — confirming it is a **Bayesian Nash equilibrium**.

The second-order condition confirms this is a maximum: the expected utility as a
function of $\bar{b}$ is a degree-$N$ polynomial in $\bar{b}$ with a negative
leading coefficient, so the unique interior critical point is indeed a maximum.

```{code-cell} python3
import sympy as sym

b_bar, v_i, alpha = sym.symbols(r"\bar{b} v_i alpha", positive=True)
N = sym.Symbol("N", positive=True, integer=True)

# Expected utility
EU = (b_bar / alpha) ** (N - 1) * (v_i - b_bar)

# First order condition
dEU = sym.diff(EU, b_bar)
best_response = sym.solve(dEU, b_bar)
print("Best response:", best_response)
```
````

````{solution} generalising-beyond-uniform
:label: solution:generalising-beyond-uniform

Players' valuations are drawn from an exponential distribution with CDF
$F(v) = 1 - e^{-\lambda v}$, and each player bids $b_i = \beta v_i$ in a
first-price auction with $N$ players. We focus on $N = 2$.

**1. Probability of winning for a given bid $\bar{b}$:**

Suppose all other players bid $b_j = \beta v_j$. Player $i$ wins if
$\bar{b} > \beta v_j$ for all $j \ne i$, i.e., $v_j < \bar{b}/\beta$ for all
$j \ne i$.

$$
\Pr(\text{Win}) = \prod_{j \ne i} F\!\left(\frac{\bar{b}}{\beta}\right) = \left(1 - e^{-\lambda \bar{b}/\beta}\right)^{N-1}
$$

For $N = 2$:

$$
\Pr(\text{Win}) = 1 - e^{-\lambda \bar{b}/\beta}
$$

**2. Expected utility and optimal $\beta$:**

For $N = 2$, the expected utility of Player $i$ bidding $\bar{b}$ (first-price
auction, paying their own bid when they win) is:

$$
\mathbb{E}[u_i \mid v_i] = \left(1 - e^{-\lambda \bar{b}/\beta}\right)(v_i - \bar{b})
$$

Taking the derivative with respect to $\bar{b}$ and setting it to zero:

$$
\frac{d}{d\bar{b}}\mathbb{E}[u_i]
= \frac{\lambda}{\beta}e^{-\lambda\bar{b}/\beta}(v_i - \bar{b})
  - \left(1 - e^{-\lambda\bar{b}/\beta}\right) = 0
$$

Let $\mu = \lambda \bar{b}/\beta$ for brevity. Then $\bar{b} = \mu\beta/\lambda$ and:

$$
\begin{align*}
\mu e^{-\mu}\!\left(v_i - \frac{\mu\beta}{\lambda}\right) \\
&= \frac{\beta}{\lambda}\left(1 - e^{-\mu}\right)
\end{align*}
$$

For a symmetric equilibrium we require $\bar{b} = \beta v_i$, i.e., the best
response $\bar{b}^*$ must equal $\beta v_i$. Substituting $\bar{b} = \beta v_i$:

$$
\frac{\lambda}{\beta}e^{-\lambda v_i}(v_i - \beta v_i) = 1 - e^{-\lambda v_i}
$$

$$
\lambda v_i(1-\beta)e^{-\lambda v_i} = \frac{\beta}{\lambda}\cdot\frac{\lambda}{\beta}\left(1 - e^{-\lambda v_i}\right)
$$

More carefully, substituting $\bar{b} = \beta v_i$ into the first-order condition:

$$
\frac{\lambda}{\beta}e^{-\lambda v_i}\cdot v_i(1-\beta) = 1 - e^{-\lambda v_i}
$$

This must hold for all $v_i > 0$, which means $\beta$ is determined implicitly.
For the exponential distribution, unlike the uniform case, the linear bidding
strategy $b = \beta v$ does not generally yield a closed-form symmetric
equilibrium in terms of $\beta$ alone. Instead, the equilibrium bid function is
derived via the general first-order approach:

$$
b^*(v) = \frac{\int_0^v t\, f(t)\, F(t)^{N-2} dt}{F(v)^{N-1}}
\quad \text{(for } N \geq 2\text{)}
$$

For $N = 2$ and $F(v) = 1 - e^{-\lambda v}$, $f(v) = \lambda e^{-\lambda v}$:

$$
\begin{align*}
b^*(v) \\
&= \frac{\int_0^v t \cdot \lambda e^{-\lambda t} dt}{1 - e^{-\lambda v}}
\end{align*}
$$

Integrating by parts:
$\int_0^v t\lambda e^{-\lambda t}\, dt = \left[-te^{-\lambda t}\right]_0^v + \int_0^v e^{-\lambda t}\, dt
= -ve^{-\lambda v} + \frac{1-e^{-\lambda v}}{\lambda}$

So:

$$
\begin{align*}
b^*(v) &= \frac{-ve^{-\lambda v} + (1 - e^{-\lambda v})/\lambda}{1 - e^{-\lambda v}} \\
&= \frac{1}{\lambda} - \frac{v e^{-\lambda v}}{1 - e^{-\lambda v}}
\end{align*}
$$

**Comparison with the uniform case:** For $\text{Unif}[0,1]$ with $N=2$, the
equilibrium bid is $b^*(v) = v/2$, which is a linear fraction of $v$. For the
exponential distribution the equilibrium bid function $b^*(v)$ is nonlinear in
$v$ and is always less than $v$ (the bidder shades downward), but the degree of
shading depends on $v$ in a nonlinear way.

```{code-cell} python3
import sympy as sym

v, lam = sym.symbols("v lambda", positive=True)

f_v = lam * sym.exp(-lam * v)
F_v = 1 - sym.exp(-lam * v)

# N=2: equilibrium bid function
numerator = sym.integrate(v * f_v, (v, 0, v))
b_star = sym.simplify(numerator / F_v)
print("Equilibrium bid function (N=2, exponential):")
b_star
```

```{code-cell} python3
# Compare to uniform case: b*(v) = v/2
import numpy as np
import matplotlib.pyplot as plt

lam_val = 1.0
v_vals = np.linspace(0.01, 3, 200)
b_exp = 1/lam_val - v_vals * np.exp(-lam_val * v_vals) / (1 - np.exp(-lam_val * v_vals))
b_uniform = 0.5 * np.clip(v_vals, 0, 1)

plt.figure()
plt.plot(v_vals, b_exp, label=r"Exponential ($\lambda=1$)")
plt.plot(v_vals[:100], b_uniform[:100], label="Uniform[0,1]")
plt.plot(v_vals, v_vals, "k--", label="Truthful (b=v)")
plt.xlabel("$v$")
plt.ylabel("$b^*(v)$")
plt.title("Equilibrium bid functions: exponential vs. uniform")
plt.legend()
plt.ylim(0, 1.5)
plt.show()
```
````

````{solution} revenue_equivalence
:label: solution:revenue_equivalence

We have $N$ symmetric bidders with $v_i \sim \text{Unif}[0,1]$ independently.

**Expected revenue of the first-price auction:**

At equilibrium, each bidder bids $b_i = \frac{N-1}{N}v_i$. The seller's revenue
equals the highest bid:

$$
\begin{align*}
R_{\text{first}} &= \max_{i}\left(\frac{N-1}{N}v_i\right) \\
&= \frac{N-1}{N}\max_i(v_i) \\
&= \frac{N-1}{N}v_{(N)}
\end{align*}
$$

where $v_{(N)}$ denotes the highest order statistic (maximum) of $N$ i.i.d.
$\text{Unif}[0,1]$ random variables. Using the hint:

$$
\mathbb{E}[v_{(N)}] = \frac{N}{N+1}
$$

Therefore:

$$
\mathbb{E}[R_{\text{first}}] = \frac{N-1}{N}\cdot\frac{N}{N+1} = \frac{N-1}{N+1}
$$

**Expected revenue of the second-price auction:**

At equilibrium, each bidder bids truthfully $b_i = v_i$. The winner (highest
bidder) pays the second-highest bid $v_{(N-1)}$:

$$
R_{\text{second}} = v_{(N-1)}
$$

where $v_{(N-1)}$ is the second-highest order statistic. Using the hint:

$$
\mathbb{E}[v_{(N-1)}] = \frac{N-1}{N+1}
$$

Therefore:

$$
\mathbb{E}[R_{\text{second}}] = \frac{N-1}{N+1}
$$

**Conclusion:**

$$
\mathbb{E}[R_{\text{first}}] = \frac{N-1}{N+1} = \mathbb{E}[R_{\text{second}}]
$$

Both mechanisms yield the same expected revenue. This is the **Revenue
Equivalence Theorem** in the special case of uniform valuations.

The result holds because both auctions are efficient (the highest-value bidder
wins) and both give zero utility to the lowest type ($v_i = 0$ receives 0).
By the Revenue Equivalence Theorem, any two auctions with these two properties
yield the same expected revenue for the seller.

```{code-cell} python3
import sympy as sym

N = sym.Symbol("N", positive=True, integer=True)

# Expected value of k-th order statistic of N Unif[0,1] r.v.'s is k/(N+1)
# First-price expected revenue
E_v_N = N / (N + 1)           # E[v_{(N)}]
E_R_first = (N - 1) / N * E_v_N
E_R_first_simplified = sym.simplify(E_R_first)
print("E[R_first] =", E_R_first_simplified)

# Second-price expected revenue
E_v_N1 = (N - 1) / (N + 1)    # E[v_{(N-1)}]
E_R_second = E_v_N1
print("E[R_second] =", sym.simplify(E_R_second))

print("Equal?", sym.simplify(E_R_first_simplified - E_R_second) == 0)
```

```{code-cell} python3
import numpy as np

# Numerical verification for N=3
np.random.seed(42)
n_sims = 200_000
N_val = 3

valuations = np.random.uniform(0, 1, (n_sims, N_val))

# First-price: each bid (N-1)/N * v, revenue = max bid
bids_fp = (N_val - 1) / N_val * valuations
revenue_fp = bids_fp.max(axis=1)

# Second-price: bid truthfully, revenue = second-highest bid
sorted_vals = np.sort(valuations, axis=1)
revenue_sp = sorted_vals[:, -2]

print(f"N={N_val}")
print(f"Expected revenue (first-price):  {revenue_fp.mean():.4f}")
print(f"Expected revenue (second-price): {revenue_sp.mean():.4f}")
print(f"Theoretical value (N-1)/(N+1):  {(N_val-1)/(N_val+1):.4f}")
```
````
