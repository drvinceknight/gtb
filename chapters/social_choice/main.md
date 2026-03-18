---
kernelspec:
  name: python3
  display_name: "Python 3"
---

(chp:social_choice)=

# Social Choice

Combining the preferences of many individuals into a single collective
decision is surprisingly fraught. This chapter studies social choice theory,
characterising aggregation procedures and establishing impossibility results —
most famously Arrow's theorem — that reveal deep constraints on what any fair
voting rule can achieve.

(motivating_example:voting_on_exam_topics)=

## Motivating Example: Voting on exam topics

In the final week of term, a game theory class of 45 students receives an
unexpected offer from their professor:

> “You get to vote on which topic will feature most heavily on the final exam.  
> Each of you will submit a full ranking of the three options, and we’ll use  
> pairwise majority voting to decide the winner.”

The three candidate topics are:

- **A. [Replicator dynamics](#chp:replicator_dynamics)**
- **B. [Best response polytopes](#chp:best_response_polytopes)**
- **C. [Repeated games](#chp:repeated_games)**

After collecting all the votes, the professor finds that the students fall into
the preference groups shown in [](#tbl:unequal_preferences).

```{list-table}
:header-rows: 1
:name: tbl:unequal_preferences
:align: left

* - Group size
  - 1st choice
  - 2nd choice
  - 3rd choice
* - 18 students
  - A
  - B
  - C
* - 16 students
  - B
  - C
  - A
* - 11 students
  - C
  - A
  - B
```

If the professor only looks at the first choice then Replicator dynamics will
be the chosen topic of the exam.
However let us examine each pairwise contest:

- **A vs B**

  - 18 students: prefer **A to B** and B to C
  - 16 students: prefer B to C and C to A so prefer **B to A**
  - 11 students: prefer C to A and **A to B**.

So **A beats B**, with 29 votes to 16.

- **B vs C**

  - 18 students: prefer A to B and **B to C**
  - 16 students: prefer **B to C** and C to A
  - 11 students: prefer C to A and A to B so prefer **C to B**

So **B beats C**, with 34 votes to 11.

- **C vs A**
  - 18 students: prefer A to B and B to C so prefer **A to C**
  - 16 students: prefer B to C and **C to A**
  - 11 students: prefer **C to A** and A to B
    → **C beats A**, with 27 votes to 18.

> A majority prefers A to B, B to C, and C to A.

This cycle is called a **Condorcet cycle** [@condorcet1785]
and it illustrates the core difficulty in aggregating preferences from a
group: **majority rule may not produce a consistent collective ranking**. This
motivates a central question in voting theory:

> What properties should a “reasonable” voting rule satisfy, and can we always
> satisfy them all at once?

## Theory

### Definition: Preference Function

---

Let $X$ be a finite set of alternatives. A **preference function** for a voter
is a strict linear order $\succ$ on $X$, meaning that for all distinct
alternatives $x, y, z \in X$:

- **Asymmetry**: if $x \succ y$, then not $y \succ x$
- **Transitivity**: if $x \succ y$ and $y \succ z$, then $x \succ z$
- **Completeness**: for all $x \ne y$, either $x \succ y$ or $y \succ x$

We refer to a complete list of $n$ voters’ preference functions as a
**preference profile**.

---

#### Example: Preference Function for the Exam Vote

For [](#motivating_example:voting_on_exam_topics) the set of alternative is:

$$A = \{A, B, C\}$$

The preference profile is:

- Group 1: $A \succ B \succ C$
- Group 2: $B \succ C \succ A$
- Group 3: $C \succ A \succ B$

### Definition: A Social Welfare Function

---

A **social welfare function** is a rule that maps every possible preference
profile over a set of alternatives $X$ to a strict linear order on $X$.

That is, it takes individual rankings and produces a **collective ranking** of
all the alternatives.

---

#### Example: Social Welfare Function for the Exam Vote

For [](#motivating_example:voting_on_exam_topics) one social welfare function
would be to rank the outcomes based on number of first choice votes, giving:

$$(A, B, C)$$

### Definition: Simple Majority Rule

---

A **simple majority rule** is a voting rule that compares alternatives $x$ and
$y$ based on how many voters prefer $x$ over $y$:

- $x$ is ranked above $y$ in the collective outcome if and only if a **strict
  majority** of voters prefer $x$ to $y$.

This defines a binary relation over pairs, but may not yield a transitive
overall ranking. When it does, the top-ranked option is called the **Condorcet
winner**.

---

### Theorem: Arrow's Impossibility Theorem

The following theorem is given without proof [@arrow1951].

---

Let $X$ be a set of at alternatives with $|X| \geq 3$.
There exists no social welfare function that satisfies **all** of the following
properties:

1. **Unrestricted domain**: all possible preference profiles are allowed
2. **Pareto efficiency**: if all voters prefer $x$ over $y$, then $x$ is ranked
   above $y$
3. **Independence of irrelevant alternatives (IIA)**: the group’s relative
   ranking of $x$ and $y$ depends only on how individuals rank $x$ vs $y$
4. **Non-dictatorship**: there is no single voter whose preferences always
   determine the outcome

In short, there is **no perfect voting rule** that aggregates individual
preferences into a consistent group ranking while satisfying all of these
fairness criteria.

---

In the context of [](#motivating_example:voting_on_exam_topics) this theorem
implies that there is no perfect way to choose. However there are two approaches
that can offer a good way to obtain an outcome.

### Definition: Condorcet's Method

An alternative $x$ is a **Condorcet winner** if, for every other alternative
$y$, a strict majority of voters prefer $x$ over $y$.

```{note}
A Condorcet winner does not always exist due to the possibility of
**majority cycles**, as illustrated in the motivating example.
```

In the context of [](#motivating_example:voting_on_exam_topics) we have already
seen that no Condorcet winner exists.

(def:bordas_method)=

### Definition: Borda's Method

---

Let $x$ be a finite set of alternatives. Every alternative obtains $k$ points
from a voter if that voter ranks the alternative above exactly $k$ other
alternatives.
The total Borda score of each alternative is the sum of its points across all
voters. The alternative with the highest total score is the **Borda winner**.

Borda’s method always produces a complete ranking, but it may fail to select a
Condorcet winner when one exists.

---

```{important}
The Borda and Condorcet methods do not escape Arrow's theorem—both violate
independence of irrelevant alternatives—but they do represent well-motivated
responses to it. By giving up IIA, they retain the other desirable properties
of fairness, including Pareto efficiency and non-dictatorship. In practice,
they are widely regarded as reasonable voting rules, especially when full
transitive rankings are available.
```

#### Example: The Borda Method for the Exam Vote

For the [](#motivating_example:voting_on_exam_topics):

- the 18 individuals in the first group give 2 points to option A and 1 point to
  option B.
- the 16 individuals in the second group give 2 points to option B and 1 point
  to option C.
- the 11 individuals in the third group give 2 points to option C and 1 point to
  option A.

Thus the Borda score of each option is:

- A: $18 \cdot 2 + 11 \cdot 1=47$
- B: $18 \cdot 1 + 16 \cdot 2=50$
- C: $11 \cdot 2 + 16 \cdot 1=38$

The Borda winner is thus B.

## Exercises

```{exercise} 
:label: condorcet_consistency_and_cycles

Consider the following preference profile over three alternatives
   $X = \{A, B, C\}$:

   - 3 voters: $A \succ B \succ C$
   - 2 voters: $B \succ C \succ A$
   - 2 voters: $C \succ A \succ B$

   a. Construct the pairwise majority contests.  
   b. Is there a Condorcet winner?  
   c. Is the majority preference relation transitive?
```


```{exercise} 
:label: comparing_borda_and_condorcet

Consider the preference profile:

   - 4 voters: $A \succ B \succ C$
   - 3 voters: $B \succ C \succ A$
   - 2 voters: $C \succ A \succ B$

   a. Compute the Borda scores of each alternative.  
   b. Determine if a Condorcet winner exists.  
   c. Do the Borda and Condorcet methods select the same winner?
```

```{exercise} 
:label: strategic_manipulation_and_the_borda_method

Suppose an election uses the Borda count and the following preference profile:

   - 5 voters: $A \succ B \succ C$
   - 4 voters: $B \succ C \succ A$
   - 3 voters: $C \succ A \succ B$

   a. Compute the Borda scores and identify the winner.  
   b. Suppose one of the 4 voters who prefers $B \succ C \succ A$ changes
   their ranking to $B \succ A \succ C$. What are the new Borda scores?  
   c. Does the outcome change? What does this tell you about the vulnerability
   of the Borda method to strategic voting?
```

````{exercise} 
:label: a_response_to_borda_from_condorcet

Borda proposed the [Borda Method](#def:bordas_method) as a response to the existence of
Condorcet cycles in simply majority voting. Condorcet then presented the
preference profile of [](#tbl:condorcet_example).

```{list-table}
:header-rows: 1
:name: tbl:condorcet_example
:align: left

* - Number of votes
  - 1st choice
  - 2nd choice
  - 3rd choice
* - 30
  - A
  - B
  - C
* - 1
  - A
  - C
  - B
* - 29
  - B
  - A
  - C
* - 10
  - B
  - C
  - A
* - 10
  - C
  - A
  - B
* - 1
  - C
  - B
  - A
```

1. Who is the Condorcet winner (if there is one)?
2. Who is the Borda winner?
3. Why would this example be a critique of Borda's approach?
````

## Programming

The `pref_voting` Python library [@HollidayPacuit2025] provides tools for analyzing preferential
voting systems. In the following example, we define a preference profile based
on the classroom voting scenario and use the library to explore two voting
methods.

We first check for a **Condorcet winner** using pairwise majority comparisons.
In this case, the method returns all alternatives, indicating that **no
Condorcet winner exists** due to a cycle.

```{code-cell} python3
import pref_voting.profiles
import pref_voting.c1_methods

profile = pref_voting.profiles.Profile(
    [[0, 1, 2]] * 18 + [[1, 2, 0]] * 16 + [[2, 0, 1]] * 11
)
pref_voting.c1_methods.condorcet(profile)
```

Next, we apply the **Borda count**, which assigns points based on rankings and
selects the alternative with the highest total score.

```{code-cell} python3
import pref_voting.scoring_methods

pref_voting.scoring_methods.borda(profile)
```

## Notable Research

The foundational work of Condorcet and Borda [@condorcet1785; @borda1781]
established key ideas in social choice theory, culminating in Arrow's
impossibility theorem [@arrow1951]. Arrow's result shows that no voting rule
can simultaneously satisfy a set of seemingly reasonable fairness criteria.

These challenges deepen with the **Gibbard–Satterthwaite theorem**, which
demonstrates that any non-dictatorial voting rule with at least three
alternatives is vulnerable to **strategic manipulation**
[@gibbard1973manipulation; @satterthwaite1975strategy]. This perhaps helps
explain why some open source software projects, such as Python, historically
adopted a **Benevolent Dictator For Life** (BDFL) model of governance
[@o2007governance], with Guido van Rossum serving in that role until 2018.

Encouragingly, recent work has shown that although manipulation is theoretically
possible, it can be **computationally difficult in practice**
[@conitzer2002complexity; @faliszewski2010using].

Other modern approaches focus on **multiwinner voting rules** that aim for fair
and proportional representation [@elkind2017properties; @bredereck2018multiwinner].
These rules are increasingly relevant in applications such as committee
selection, participatory budgeting, and recommendation systems.

These developments show that while Arrow’s theorem rules out a perfect solution,
there are many meaningful and principled ways to **navigate the trade-offs**—especially when
one considers computation, uncertainty, or broader notions of fairness.

A helpful overview of these developments is provided in [@pacuit2019voting].

## Conclusion

This chapter explored the central challenge of social choice: how to aggregate
individual preferences into a fair and consistent group decision. Starting from
a motivating classroom example, we saw how simple majority rule can lead to
intransitive group preferences—known as Condorcet cycles—even when every
individual's ranking is rational.

We then introduced the formal framework of preference functions and social
welfare functions, leading to Arrow’s impossibility theorem. This result shows
that no voting rule can satisfy a basic set of fairness properties when there
are at least three alternatives.

Despite this impossibility, we studied two influential responses: the
**Condorcet method**, which seeks an alternative that beats all others in
pairwise comparisons, and **Borda’s method**, which aggregates preferences using
a scoring rule. While each method has strengths and limitations, they both offer
principled approaches to navigating the trade-offs inherent in group decision
making.

```{list-table}
:header-rows: 1
:name: tbl:social_choice_summary
:align: left

* - Method
  - Summary
  - Strength
  - Limitation
* - Simple Majority
  - Pairwise majority voting
  - Intuitive and widely used
  - Can produce cycles
* - Condorcet
  - Chooses the option that beats all others in pairwise votes
  - Respects majority preferences
  - May not always exist
* - Borda
  - Points based on rank positions
  - Always yields a complete ranking
  - Fails to select Condorcet winner
```

```{important}
Arrow’s impossibility theorem does not mean that all voting rules are equally
bad. It means that trade-offs are inevitable. Understanding the strengths and
limits of each method allows us to choose the right tool for the context.
```

---

(solutions:social_choice)=

## Solutions

````{solution} condorcet_consistency_and_cycles
:label: solution:condorcet_consistency_and_cycles

The preference profile over $X = \{A, B, C\}$ is:

- 3 voters: $A \succ B \succ C$
- 2 voters: $B \succ C \succ A$
- 2 voters: $C \succ A \succ B$

There are 7 voters in total.

**a. Pairwise majority contests:**

**A vs B:**

- 3 voters prefer $A$ to $B$ (group 1).
- 2 voters prefer $B$ to $A$ (group 2).
- 2 voters prefer $A$ to $B$ (group 3: $C \succ A \succ B$, so $A \succ B$).

Total: $A$ preferred by $3+2=5$ voters, $B$ preferred by $2$ voters.

**$A$ beats $B$ with 5 votes to 2.**

**B vs C:**

- 3 voters prefer $B$ to $C$ (group 1: $A \succ B \succ C$).
- 2 voters prefer $B$ to $C$ (group 2: $B \succ C \succ A$).
- 2 voters prefer $C$ to $B$ (group 3).

Total: $B$ preferred by $3+2=5$ voters, $C$ preferred by $2$ voters.

**$B$ beats $C$ with 5 votes to 2.**

**C vs A:**

- 3 voters prefer $A$ to $C$ (group 1).
- 2 voters prefer $C$ to $A$ (group 2).
- 2 voters prefer $C$ to $A$ (group 3).

Total: $C$ preferred by $2+2=4$ voters, $A$ preferred by $3$ voters.

**$A$ beats $C$ with 3 votes to 4.**

Wait — let us recount. Group 1 ($A\succ B\succ C$): prefer $A$ to $C$. Group 2
($B\succ C\succ A$): prefer $C$ to $A$. Group 3 ($C\succ A\succ B$): prefer $C$
to $A$.

Total preferring $A$: 3. Total preferring $C$: $2+2=4$.

**$C$ beats $A$ with 4 votes to 3.**

**Summary of pairwise results:**
- $A \succ_{\text{maj}} B$ (5 to 2)
- $B \succ_{\text{maj}} C$ (5 to 2)
- $C \succ_{\text{maj}} A$ (4 to 3)

**b. Is there a Condorcet winner?**

A Condorcet winner must beat all other alternatives in pairwise majority
comparisons.

- $A$ beats $B$ but loses to $C$. Not a Condorcet winner.
- $B$ beats $C$ but loses to $A$. Not a Condorcet winner.
- $C$ beats $A$ but loses to $B$. Not a Condorcet winner.

**There is no Condorcet winner.**

**c. Is the majority preference relation transitive?**

The majority relation gives $A \succ_{\text{maj}} B$, $B \succ_{\text{maj}} C$,
but $C \succ_{\text{maj}} A$ (not $A \succ_{\text{maj}} C$).

Transitivity would require $A \succ_{\text{maj}} C$, but we have the opposite.
Therefore **the majority preference relation is not transitive**. This is a
Condorcet cycle: $A$ beats $B$, $B$ beats $C$, $C$ beats $A$.

```{code-cell} python3
import pref_voting.profiles
import pref_voting.c1_methods

# Encode: A=0, B=1, C=2
profile = pref_voting.profiles.Profile(
    [[0, 1, 2]] * 3 + [[1, 2, 0]] * 2 + [[2, 0, 1]] * 2
)
condorcet_winner = pref_voting.c1_methods.condorcet(profile)
print("Condorcet winner(s):", condorcet_winner)
```

```{code-cell} python3
# Pairwise margin matrix
import numpy as np

# voters[i] = list of preferences in order (most to least preferred)
votes = [[0, 1, 2]] * 3 + [[1, 2, 0]] * 2 + [[2, 0, 1]] * 2
n_alt = 3
margin = np.zeros((n_alt, n_alt), dtype=int)
for v in votes:
    for i in range(n_alt):
        for j in range(i + 1, n_alt):
            x, y = v[i], v[j]
            margin[x][y] += 1
            margin[y][x] -= 1

labels = ["A", "B", "C"]
print("Pairwise margins (row beats column by this many votes):")
for i in range(n_alt):
    for j in range(n_alt):
        if i != j:
            print(f"  {labels[i]} vs {labels[j]}: {margin[i][j]:+d}")
```
````

````{solution} comparing_borda_and_condorcet
:label: solution:comparing_borda_and_condorcet

The preference profile is:

- 4 voters: $A \succ B \succ C$
- 3 voters: $B \succ C \succ A$
- 2 voters: $C \succ A \succ B$

There are 9 voters in total.

**a. Borda scores:**

With three alternatives, each voter assigns 2 points to their first choice,
1 point to their second choice, and 0 points to their last choice.

- **A:** $4 \times 2 + 3 \times 0 + 2 \times 1 = 8 + 0 + 2 = 10$
- **B:** $4 \times 1 + 3 \times 2 + 2 \times 0 = 4 + 6 + 0 = 10$
- **C:** $4 \times 0 + 3 \times 1 + 2 \times 2 = 0 + 3 + 4 = 7$

Borda scores: $A = 10$, $B = 10$, $C = 7$.

The Borda method produces a **tie between $A$ and $B$**. (Without a tie-breaking
rule, neither is uniquely selected.)

**b. Condorcet winner:**

**A vs B:**

- 4 voters prefer $A$ (group 1).
- 3 voters prefer $B$ (group 2).
- 2 voters prefer $A$ (group 3: $C \succ A \succ B$, so $A \succ B$).

$A$ preferred by $4+2=6$, $B$ preferred by $3$. **$A$ beats $B$ 6 to 3.**

**A vs C:**

- 4 voters prefer $A$ (group 1).
- 3 voters prefer $C$ (group 2).
- 2 voters prefer $C$ (group 3).

$A$ preferred by $4$, $C$ preferred by $3+2=5$. **$C$ beats $A$ 5 to 4.**

**B vs C:**

- 4 voters prefer $B$ (group 1).
- 3 voters prefer $B$ (group 2).
- 2 voters prefer $C$ (group 3).

$B$ preferred by $4+3=7$, $C$ preferred by $2$. **$B$ beats $C$ 7 to 2.**

Pairwise results: $A$ beats $B$; $B$ beats $C$; $C$ beats $A$. This is again a
Condorcet cycle. **There is no Condorcet winner.**

**c. Do Borda and Condorcet select the same winner?**

There is no Condorcet winner here (due to the cycle). The Borda method yields a
tie between $A$ and $B$. Since no Condorcet winner exists, we cannot directly
compare the two methods in terms of who they "select", but we can note that the
Borda method at least produces a complete ranking and is decisive (up to ties),
while the Condorcet method fails to identify a winner in this case.

```{code-cell} python3
import pref_voting.profiles
import pref_voting.c1_methods
import pref_voting.scoring_methods

profile = pref_voting.profiles.Profile(
    [[0, 1, 2]] * 4 + [[1, 2, 0]] * 3 + [[2, 0, 1]] * 2
)
print("Condorcet winner:", pref_voting.c1_methods.condorcet(profile))
print("Borda winner:", pref_voting.scoring_methods.borda(profile))
```

```{code-cell} python3
# Manual Borda score computation
groups = [(4, [0, 1, 2]), (3, [1, 2, 0]), (2, [2, 0, 1])]
n_alt = 3
borda_scores = [0, 0, 0]
for count, ranking in groups:
    for rank, alt in enumerate(ranking):
        borda_scores[alt] += count * (n_alt - 1 - rank)
labels = ["A", "B", "C"]
for label, score in zip(labels, borda_scores):
    print(f"Borda score of {label}: {score}")
```
````

````{solution} strategic_manipulation_and_the_borda_method
:label: solution:strategic_manipulation_and_the_borda_method

The preference profile is:

- 5 voters: $A \succ B \succ C$
- 4 voters: $B \succ C \succ A$
- 3 voters: $C \succ A \succ B$

There are 12 voters in total.

**a. Original Borda scores:**

With three alternatives each voter assigns 2 points to their top choice, 1 to
second, 0 to last.

- **A:** $5 \times 2 + 4 \times 0 + 3 \times 1 = 10 + 0 + 3 = 13$
- **B:** $5 \times 1 + 4 \times 2 + 3 \times 0 = 5 + 8 + 0 = 13$
- **C:** $5 \times 0 + 4 \times 1 + 3 \times 2 = 0 + 4 + 6 = 10$

Borda scores: $A = 13$, $B = 13$, $C = 10$.

The **Borda winner is a tie between $A$ and $B$**.

**b. Manipulation: one voter changes from $B \succ C \succ A$ to $B \succ A \succ C$:**

The new profile is:

- 5 voters: $A \succ B \succ C$
- 3 voters: $B \succ C \succ A$ (one fewer)
- 1 voter: $B \succ A \succ C$ (the manipulating voter)
- 3 voters: $C \succ A \succ B$

New Borda scores:

- **A:** $5 \times 2 + 3 \times 0 + 1 \times 1 + 3 \times 1 = 10 + 0 + 1 + 3 = 14$
- **B:** $5 \times 1 + 3 \times 2 + 1 \times 2 + 3 \times 0 = 5 + 6 + 2 + 0 = 13$
- **C:** $5 \times 0 + 3 \times 1 + 1 \times 0 + 3 \times 2 = 0 + 3 + 0 + 6 = 9$

New Borda scores: $A = 14$, $B = 13$, $C = 9$.

**c. Does the outcome change?**

Originally $A$ and $B$ were tied (both at 13). After the manipulation, **$A$
wins outright with 14 points**, while $B$ drops to 13.

The manipulating voter prefers $B$ to $A$, yet their manipulation caused $A$ to
win (or more precisely, broke the tie in $A$'s favour, away from $B$). This
shows that the manipulation was **not profitable for this voter** — it was
inadvertent harm.

However, the fact that changing a ballot in a way that does not affect the voter's
stated preference between $B$ and $C$ (they still rank $B$ first) can nonetheless
change the winner illustrates the Borda method's **vulnerability to strategic
voting**. A voter who, in a different scenario, wanted to harm $A$ could promote
$C$ (an irrelevant alternative) to second place — boosting $C$'s score and
potentially tipping the outcome. This violates the **Independence of Irrelevant
Alternatives** property and is the mechanism through which manipulation operates.

More broadly, the Borda method is susceptible to strategic manipulation because
the relative ranking of any two alternatives can be influenced by how a voter
ranks a third, "irrelevant" alternative. This is precisely what the
Gibbard-Satterthwaite theorem predicts: any non-dictatorial voting rule over
three or more alternatives is manipulable.

```{code-cell} python3
import pref_voting.profiles
import pref_voting.scoring_methods

# Original profile: A=0, B=1, C=2
profile_original = pref_voting.profiles.Profile(
    [[0, 1, 2]] * 5 + [[1, 2, 0]] * 4 + [[2, 0, 1]] * 3
)
print("Original Borda winner:", pref_voting.scoring_methods.borda(profile_original))
```

```{code-cell} python3
# Manipulated profile: one voter switches from B>C>A to B>A>C
profile_manipulated = pref_voting.profiles.Profile(
    [[0, 1, 2]] * 5 + [[1, 2, 0]] * 3 + [[1, 0, 2]] * 1 + [[2, 0, 1]] * 3
)
print("Manipulated Borda winner:", pref_voting.scoring_methods.borda(profile_manipulated))
```

```{code-cell} python3
# Manual score verification
def borda_scores(groups, n_alt=3):
    scores = [0] * n_alt
    for count, ranking in groups:
        for rank, alt in enumerate(ranking):
            scores[alt] += count * (n_alt - 1 - rank)
    return scores

original = borda_scores([(5,[0,1,2]),(4,[1,2,0]),(3,[2,0,1])])
manipulated = borda_scores([(5,[0,1,2]),(3,[1,2,0]),(1,[1,0,2]),(3,[2,0,1])])
labels = ["A","B","C"]
print("Original scores:", {l:s for l,s in zip(labels, original)})
print("Manipulated scores:", {l:s for l,s in zip(labels, manipulated)})
```
````

````{solution} a_response_to_borda_from_condorcet
:label: solution:a_response_to_borda_from_condorcet

The preference profile is:

| Number of votes | 1st | 2nd | 3rd |
|-----------------|-----|-----|-----|
| 30              | A   | B   | C   |
| 1               | A   | C   | B   |
| 29              | B   | A   | C   |
| 10              | B   | C   | A   |
| 10              | C   | A   | B   |
| 1               | C   | B   | A   |

Total voters: $30+1+29+10+10+1 = 81$.

**1. Who is the Condorcet winner?**

We check each pairwise majority contest.

**A vs B:**

Voters preferring $A$ over $B$: groups ranking $A$ above $B$:
- 30 voters ($A \succ B \succ C$)
- 1 voter ($A \succ C \succ B$)
- 10 voters ($C \succ A \succ B$)

Total preferring $A$: $30+1+10=41$.

Voters preferring $B$ over $A$:
- 29 voters ($B \succ A \succ C$)
- 10 voters ($B \succ C \succ A$)
- 1 voter ($C \succ B \succ A$)

Total preferring $B$: $29+10+1=40$.

**$A$ beats $B$ with 41 to 40.**

**A vs C:**

Voters preferring $A$ over $C$:
- 30 voters ($A \succ B \succ C$)
- 1 voter ($A \succ C \succ B$)
- 29 voters ($B \succ A \succ C$)

Total: $30+1+29=60$.

Voters preferring $C$ over $A$:
- 10 voters ($B \succ C \succ A$)
- 10 voters ($C \succ A \succ B$)
- 1 voter ($C \succ B \succ A$)

Total: $10+10+1=21$.

**$A$ beats $C$ with 60 to 21.**

**B vs C:**

Voters preferring $B$ over $C$:
- 30 voters ($A \succ B \succ C$)
- 29 voters ($B \succ A \succ C$)
- 10 voters ($B \succ C \succ A$)
- 1 voter ($C \succ B \succ A$)

Total: $30+29+10+1=70$. Wait — $C \succ B \succ A$ means $C$ is preferred to $B$.

Correcting:
- 30 voters ($A \succ B \succ C$): prefer $B$ over $C$.
- 1 voter ($A \succ C \succ B$): prefer $C$ over $B$.
- 29 voters ($B \succ A \succ C$): prefer $B$ over $C$.
- 10 voters ($B \succ C \succ A$): prefer $B$ over $C$.
- 10 voters ($C \succ A \succ B$): prefer $C$ over $B$.
- 1 voter ($C \succ B \succ A$): prefer $C$ over $B$.

Total preferring $B$: $30+29+10=69$. Total preferring $C$: $1+10+1=12$.

**$B$ beats $C$ with 69 to 12.**

$A$ beats both $B$ and $C$, so **$A$ is the Condorcet winner**.

**2. Who is the Borda winner?**

With three alternatives, each voter assigns 2 points to their 1st choice,
1 point to their 2nd choice, 0 to their 3rd choice.

- **A:** $31\times 2 + 29\times 1 + 10\times 1 + 10\times 0 + 0\times 0 + ...$

Let us compute carefully:

| Group (count) | A points | B points | C points |
|---------------|----------|----------|----------|
| 30 ($A\succ B\succ C$) | $30\times2=60$ | $30\times1=30$ | $30\times0=0$ |
| 1 ($A\succ C\succ B$)  | $1\times2=2$  | $1\times0=0$  | $1\times1=1$  |
| 29 ($B\succ A\succ C$) | $29\times1=29$ | $29\times2=58$ | $29\times0=0$ |
| 10 ($B\succ C\succ A$) | $10\times0=0$ | $10\times2=20$ | $10\times1=10$ |
| 10 ($C\succ A\succ B$) | $10\times1=10$ | $10\times0=0$ | $10\times2=20$ |
| 1 ($C\succ B\succ A$)  | $1\times0=0$  | $1\times1=1$  | $1\times2=2$  |

Total Borda scores:

- **A:** $60+2+29+0+10+0 = 101$
- **B:** $30+0+58+20+0+1 = 109$
- **C:** $0+1+0+10+20+2 = 33$

The **Borda winner is $B$** with 109 points.

**3. Why is this a critique of Borda's method?**

$A$ is the Condorcet winner: it beats every other alternative in pairwise
majority votes (41 to 40 over $B$; 60 to 21 over $C$). A majority of voters
prefers $A$ to $B$ (41 out of 81).

Yet the Borda method selects $B$ as the winner.

This is Condorcet's critique of the Borda method: **the Borda method can fail to
elect the Condorcet winner** even when one exists. The method gives weight to the
intensity of preferences (how far apart alternatives are ranked) rather than
just pairwise majority relationships. Here, $B$ benefits from being ranked
second by many voters (the 30 who rank $A$ first and the 10 who rank $C$ first),
accumulating enough second-place votes to overtake $A$'s lead in direct
comparisons.

This example showed Condorcet that the Borda method violates the Condorcet
criterion — a property that many would argue is a minimal requirement of a
reasonable voting rule.

```{code-cell} python3
import pref_voting.profiles
import pref_voting.c1_methods
import pref_voting.scoring_methods

# A=0, B=1, C=2
profile = pref_voting.profiles.Profile(
    [[0, 1, 2]] * 30
    + [[0, 2, 1]] * 1
    + [[1, 0, 2]] * 29
    + [[1, 2, 0]] * 10
    + [[2, 0, 1]] * 10
    + [[2, 1, 0]] * 1
)

print("Condorcet winner:", pref_voting.c1_methods.condorcet(profile))
print("Borda winner:", pref_voting.scoring_methods.borda(profile))
```

```{code-cell} python3
# Manual Borda score verification
groups = [
    (30, [0, 1, 2]),
    (1,  [0, 2, 1]),
    (29, [1, 0, 2]),
    (10, [1, 2, 0]),
    (10, [2, 0, 1]),
    (1,  [2, 1, 0]),
]
scores = [0, 0, 0]
for count, ranking in groups:
    for rank, alt in enumerate(ranking):
        scores[alt] += count * (2 - rank)
print("Borda scores — A:", scores[0], "B:", scores[1], "C:", scores[2])
```
````
