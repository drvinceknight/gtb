---
kernelspec:
  name: python3
  display_name: "Python 3"
---

(chp:social_choice)=

# Social Choice

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

### Example: Preference Function for the Exam Vote

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

### Example: Social Welfare Function for the Exam Vote

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

### Example: The Borda Method for the Exam Vote

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

### Exercise: Condorcet consistency and cycles

1. Consider the following preference profile over three alternatives
   $X = \{A, B, C\}$:

   - 3 voters: $A \succ B \succ C$
   - 2 voters: $B \succ C \succ A$
   - 2 voters: $C \succ A \succ B$

   a. Construct the pairwise majority contests.  
   b. Is there a Condorcet winner?  
   c. Is the majority preference relation transitive?

---

### Exercise: Comparing Borda and Condorcet

2. Consider the preference profile:

   - 4 voters: $A \succ B \succ C$
   - 3 voters: $B \succ C \succ A$
   - 2 voters: $C \succ A \succ B$

   a. Compute the Borda scores of each alternative.  
   b. Determine if a Condorcet winner exists.  
   c. Do the Borda and Condorcet methods select the same winner?

### Exercise: Strategic manipulation and the Borda method

4. Suppose an election uses the Borda count and the following preference
   profile:

   - 5 voters: $A \succ B \succ C$
   - 4 voters: $B \succ C \succ A$
   - 3 voters: $C \succ A \succ B$

   a. Compute the Borda scores and identify the winner.  
   b. Suppose one of the 4 voters who prefers $B \succ C \succ A$ changes
   their ranking to $B \succ A \succ C$. What are the new Borda scores?  
   c. Does the outcome change? What does this tell you about the vulnerability
   of the Borda method to strategic voting?

### Exercise: A response to Borda from Condorcet

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

Modern research builds on these ideas to address strategic voting,
computational barriers, and settings with multiple winners. These insights
reinforce that although no voting system is perfect, there are many thoughtful
and rigorous ways to design collective choice mechanisms.

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
