---
kernelspec:
  name: python3
  display_name: "Python 3"
---

(chp:auctions)=

# Auctions

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

```{code-cell} ipython3
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

```{code-cell} ipython3
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

Importantly, these theoretical tools are not merely abstract: they underpin some
of the most economically significant allocation mechanisms in the modern world,
from government spectrum sales to online advertising platforms.

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
