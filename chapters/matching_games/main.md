---
kernelspec:
  name: python3
  display_name: "Python 3"
---

(chp:matching_games)=

# Matching Games

(sec:research_conference_motivating_example)=

## Motivating Example: Stable peer review assignment at a research conference

The **Social Perspectives Research Symposium** receives five paper submissions and
recruits five expert reviewers. Each paper must be assigned to exactly one reviewer.

To promote high-quality reviews, both authors and reviewers submit ranked preference
lists:

- Each **author** ranks the reviewers based on perceived expertise, familiarity with
  the topic, and potential for constructive feedback.
- Each **reviewer** ranks the submissions based on interest, alignment with their
  research, and methodological fit.

The participants are:

- **Authors:** A1, A2, A3, A4, A5
- **Reviewers:** R1, R2, R3, R4, R5

For example:

- Author A1 has written a paper on representation in environmental activism and ranks
  R3, an expert in environmental sociology, as their top choice.
- Reviewer R2 specializes in healthcare policy and ranks submission A4 as their first
  choice due to its relevance.
- Author A5’s paper focuses on queer representation in contemporary fiction, and they
  rank R5 highly based on prior work in literature studies.

> _“R3’s expertise would be invaluable for my analysis.”_  
> _“A4’s topic fits directly with my current research.”_  
> _“R5’s previous reviews have been extremely helpful.”_

The preferences of the authors are given in [](#tbl:author_preferences) and the
preferences of the reviewers are given in [](#tbl:reviewer_preferences).

```{table} Preference table for the authors
:label: tbl:author_preferences
:align: center
:class: table-bordered

| Author | 1st | 2nd | 3rd | 4th | 5th |
| ------ | --- | --- | --- | --- | --- |
| A1     | R3  | R1  | R4  | R5  | R2  |
| A2     | R2  | R4  | R3  | R5  | R1  |
| A3     | R5  | R2  | R3  | R1  | R4  |
| A4     | R2  | R3  | R5  | R1  | R4  |
| A5     | R5  | R3  | R4  | R2  | R1  |
```

The organizers aim to compute a **stable matching**: an assignment where no
author-reviewer pair exists who would both prefer to be assigned to each other over
their current assignments.

```{table} Preference table for the reviewers
:label: tbl:reviewer_preferences
:align: center
:class: table-bordered

| Reviewer | 1st | 2nd | 3rd | 4th | 5th |
| -------- | --- | --- | --- | --- | --- |
| R1       | A3  | A1  | A5  | A4  | A2  |
| R2       | A4  | A2  | A5  | A1  | A3  |
| R3       | A1  | A5  | A2  | A3  | A4  |
| R4       | A2  | A5  | A3  | A1  | A4  |
| R5       | A5  | A3  | A4  | A1  | A2  |
```

## Theory

### Definition: Matching Game

A matching game of size $N$ is defined by two disjoint sets $S$ and $R$ or
proposers and reviewers of size $N$.
Associated to each element of $S$ and $R$ is a preference map:

$$f:S\to R^N\text{ and }g:R\to S^N$$

A matching $M$ is any bijection between $S$ and $R$. If $s\in S$ and $r\in R$ are matched by $M$ we denote:

$$M(s)=r$$

### Example: Author Reviewer as a Matching Game

For [](#sec:research_conference_motivating_example) the matching game has size
$N=5$, the set of proposers $S=(A1, A2, A3, A4, A5)$ the set of
reviewers $R=(R1, R2, R3, R4, R5)$ and the preference maps:

$$
\begin{align*}
    f(A1)&=(R3, R1, R4, R5, R2)\\
    f(A2)&=(R2, R4, R3, R5, R1)\\
    f(A3)&=(R5, R2, R3, R1, R4)\\
    f(A4)&=(R2, R3, R5, R1, R4)\\
    f(A5)&=(R5, R3, R4, R2, R1)\\
    g(R1)&=(A3, A1, A5, A4, A2)\\
    g(R2)&=(A4, A2, A5, A1, A3)\\
    g(R3)&=(A1, A5, A2, A3, A4)\\
    g(R4)&=(A2, A5, A3, A1, A4)\\
    g(R5)&=(A5, A3, A4, A1, A2)
\end{align*}
$$

One potential mapping is given by:

$$
\label{eqn:unstable_matching}
\begin{align*}
    M(A1) &= R3\\
    M(A2) &= R2\\
    M(A3) &= R5\\
    M(A4) &= R1\\
    M(A5) &= R4
\end{align*}
$$

### Definition: a blocking pair

A pair $(s,r)$ is said to **block** a matching $M$ if $M(s)\ne r$ but $s$ prefers
$r$ to $M(s)$ and $r$ prefers $s$ to $M^{-1}(r)$.

### Example: Blocking pair for the author reviewer game

In [](#eqn:unstable_matching) the pair $(A4, R2)$ is a blocking pair as $A4$
prefer $R2$ to $M(A4)$ and $R2$ prefers $A4$ to $M^{-1}(R2)$.

### Definition: a stable matching

A matching $M$ with no blocking pair is said to be stable.

### Example: A stable matching for the author reviewer game

The following is a stable matching for [](#sec:research_conference_motivating_example):

$$
\label{eqn:stable_matching}
\begin{align*}
    M(A1) &= R3\\
    M(A2) &= R4\\
    M(A3) &= R1\\
    M(A4) &= R2\\
    M(A5) &= R5
\end{align*}
$$

### Definition: The Gale-Shapley algorithm

Here is the Gale-Shapley algorithm, which gives a stable matching for a matching game:

1. Assign every $s\in S$ and $r\in R$ to be unmatched
2. Pick some unmatched $s\in S$, let $r$ be the top of $s$'s preference list:
   - If $r$ is unmatched set $M(s)=r$
   - If $r$ is matched:
     - If $r$ prefers $s$ to $M^{-1}(r)$ then set $M(r)=s$
     - Otherwise $s$ remains unmatched and remove $r$ from $s$'s preference list.
3. Repeat step 2 until all $s\in S$ are matched.

### Theorem: Unique matching as output of the Gale Shapley algorithm

All possible executions of the Gale-Shapley algorithm yield the same stable matching **and**
in this stable matching every suitor has the best possible partner in any stable matching.

### Proof

Suppose that an arbitrary execution $\alpha$ of the algorithm gives $M$ and that another
execution $\beta$ gives $M'$ such that $\exists$ $s\in S$ such that $s$ prefers $r'=M'(s)$ to $r=M(s)$.

Without loss of generality this implies that during $\alpha$ $r'$ must have rejected $s$.
Suppose, again without loss of generality that this was the first occasion that a rejection occured
during $\alpha$ and assume that this rejection occurred because $r'=M(s')$.
This implies that $s'$ has no stable match that is higher in $s'$'s preference list
than $r'$ (as we have assumed that this is the first rejection).

Thus $s'$ prefers $r'$ to $M'(s')$ so that $(s',r')$ blocks $M'$.
Each suitor is therefore matched in $M$ with his favorite stable reviewer and since
$\alpha$ was arbitrary it follows that all possible executions give the same matching.

### Example: Application of the Gale-Shapley algorithm to the author reviewer game

We start by assigning $A1, A2, A3, A4, A5$ and $R1, R2, R3, R4, R5$ to be
unmatched.

We pick $A1$ which has $f(A1)=(R3, R1, R4, R5, R2)$, the top of the preference
list is $R1$ so we set:

$$
\begin{align*}
    M(A1) &= R3
\end{align*}
$$

We now pick $A2$ which has $f(A2)=(R2, R4, R3, R5, R1)$, the top of the
preference list is $R2$ so we set:

$$
\begin{align*}
    M(A1) &= R3\\
    M(A2) &= R2\\
\end{align*}
$$

We now pick $A3$ which has $f(A3)=(R5, R2, R3, R1, R4)$, the top of the
preference list is $R5$ so we set:

$$
\begin{align*}
    M(A1) &= R3\\
    M(A2) &= R2\\
    M(A3) &= R5\\
\end{align*}
$$

We now pick $A4$ which has $f(A4)=(R2, R3, R5, R1, R4)$, the top of the
preference list is $R2$ but $R2$ is matched ($M(A2)=R2$). We have $g(R2)=(A4,
A2, A5, A1, A3)$ so $R2$ prefers $A2$ then their current matching. So we set:

$$
\begin{align*}
    M(A1) &= R3\\
    M(A3) &= R5\\
    M(A4) &= R2\\
\end{align*}
$$

We now pick $A2$ (for the second time) which has $f(A2)=(R2, R4, R3, R5, R1)$,
the top of the preference list is $R2$ but $R2$ is matched and prefers their
current matching so we remove it from $A2$'s preference list:

$$f(A2)=(R4, R3, R5, R1)$$

We could pick any unmatched reviewer, we will pick $A2$ again (for the third
time), $A2$ has preference list $f(A)=(R4, R3, R5, R1)$, the top of the
preference list is $R4$ so we set:

$$
\begin{align*}
    M(A1) &= R3\\
    M(A2) &= R4\\
    M(A3) &= R5\\
    M(A4) &= R2\\
\end{align*}
$$

We now pick $A5$, the final unmatched reviewer, which has $f(A5)=(R5, R3, R4,
R2, R1)$, the top of the preference list is $R5$ so we set:

$$
\begin{align*}
    M(A1) &= R3\\
    M(A2) &= R4\\
    M(A3) &= R5\\
    M(A4) &= R2\\
    M(A5) &= R5\\
\end{align*}
$$

### Theorem: Reviewer sub optimality of the Gale Shapley Algorithm

In a suitor-optimal stable matching each reviewer has the worst possible matching.

### Proof

Assume that the result is not true. Let $M_0$ be a suitor-optimal matching
and assume that there is a stable matching $M'$ such that $\exists$
$r$ such that $r$ prefers $s=M_0^{-1}(r)$ to $s'=M'^{-1}(r)$.
This implies that $(r,s)$ blocks $M'$ unless $s$ prefers $M'(s)$
to $M_0(s)$ which contradicts the fact the $s$ has no stable match that
they prefer in $M_0$.

## Exercises

### Exercise: Application of the Gale Shapley Algorithm

Obtain stable suitor optimal and reviewer optimal matchings for the games shown:

1.  $$
    \begin{align*}
        f(A1)&=(R2, R1, R3)\\
        f(A2)&=(R1, R3, R2)\\
        f(A3)&=(R1, R3, R2)\\
        g(R1)&=(A1, A2, A3)\\
        g(R2)&=(A2, A1, A3)\\
        g(R3)&=(A2, A3, A1)\\
    \end{align*}
    $$

2.  $$
    \begin{align*}
        f(A1)&=(R1, R3, R2)\\
        f(A2)&=(R2, R3, R1)\\
        f(A3)&=(R1, R3, R2)\\
        g(R1)&=(A1, A2, A3)\\
        g(R2)&=(A2, A3, A1)\\
        g(R3)&=(A2, A3, A1)\\
    \end{align*}
    $$

3.  $$
    \begin{align*}
        f(A1)&=(R1, R4, R2, R3)\\
        f(A2)&=(R2, R1, R3, R4)\\
        f(A3)&=(R4, R1, R3, R2)\\
        f(A4)&=(R1, R4, R3, R2)\\
        g(R1)&=(A1, A4, A2, A3)\\
        g(R2)&=(A1, A3, A4, A2)\\
        g(R3)&=(A4, A1, A3, A2)\\
        g(R4)&=(A2, A4, A1, A3)\\
    \end{align*}
    $$

4.  $$
    \begin{align*}
        f(A1)&=(R2, R1, R4, R3)\\
        f(A2)&=(R2, R3, R1, R4)\\
        f(A3)&=(R1, R4, R3, R2)\\
        f(A4)&=(R1, R4, R3, R2)\\
        g(R1)&=(A1, A2, A4, A3)\\
        g(R2)&=(A4, A2, A1, A3)\\
        g(R3)&=(A4, A1, A3, A2)\\
        g(R4)&=(A3, A2, A4, A1)\\
    \end{align*}
    $$

### Exercise: Uniqueness with a single reviewer preference list

Consider a matching game where all reviewers have the same preference list.
Prove that there is a single stable matching.

## Programming

The python Matching library [@wilde2020matching] implements the Gale-Shapley algorithm as well as a
number of other algorithms for different generalisations of matching games.

```{code-cell} python3
import matching
import matching.games

authors = [
    matching.Player("A1"),
    matching.Player("A2"),
    matching.Player("A3"),
    matching.Player("A4"),
    matching.Player("A5"),
]

reviewers = [
    matching.Player("R1"),
    matching.Player("R2"),
    matching.Player("R3"),
    matching.Player("R4"),
    matching.Player("R5"),
]

A1, A2, A3, A4, A5 = authors
R1, R2, R3, R4, R5 = reviewers

A1.set_prefs((R3, R1, R4, R5, R2))
A2.set_prefs((R2, R4, R3, R5, R1))
A3.set_prefs((R5, R2, R3, R1, R4))
A4.set_prefs((R2, R3, R5, R1, R4))
A5.set_prefs((R5, R3, R4, R2, R1))

R1.set_prefs((A3, A1, A5, A4, A2))
R2.set_prefs((A4, A2, A5, A1, A3))
R3.set_prefs((A1, A5, A2, A3, A4))
R4.set_prefs((A2, A5, A3, A1, A4))
R5.set_prefs((A5, A3, A4, A1, A2))

game = matching.games.StableMarriage(authors, reviewers)
game.solve()
```

## Notable Research

The original Gale-Shapley algorithm was presented in [@gale1962college], a
rigorous combinatorial treatment of the algorithm is given in [@Knuth1976]. Some
refinements to the algorithm are given in [@gusfield1989stable] which is
considered to be the reference text on matching games.

In the original paper [@gale1962college] Gale and Shapley present the so called
hospital-resident matching problem which is a matching problem aiming to match
many to one. They do so in the context of College admissions in North America.
In [@Roth1984] presents the problem in the context of hospital resident
assignement. Further to this, Roth considered the problem of kidney exchange in
[@Roth2004] as a further matching problem.

In 2012, Lloyd Shapley and Alvin Roth were awarded the Nobel Prize in Economic
Sciences for their contributions to stable matching and market design.
David Gale, who co-authored the foundational 1962 paper introducing the
Gale-Shapley algorithm, was ineligible for the award, having passed away in 2008.

## Conclusion

In this chapter we introduced the theory of matching games, motivated by the
practical problem of assigning reviewers to papers at a research conference.
The central concept of **stability** ensures that no pair of participants would
prefer to deviate from the assignment, making stable matchings attractive in
many real-world settings.

The Gale-Shapley algorithm provides an elegant and efficient solution to the
stable matching problem, always producing a suitor-optimal stable matching.
While stable matchings always exist in the one-to-one setting, extensions to
many-to-one settings (such as hospital-resident assignments) preserve many of
the desirable properties of the original algorithm.

A summary of key concepts introduced in this chapter is given in
[](#tbl:matching_summary).

```{table} Summary of key concepts in matching games
:label: tbl:matching_summary
:align: center
:class: table-bordered

| Concept          | Description |
|------------------|-------------|
| Matching Game    | A game where two disjoint sets have preferences over each other |
| Stable Matching  | A matching with no blocking pairs |
| Blocking Pair    | A pair who would both prefer to be matched to each other over their current assignments |
| Gale-Shapley Algorithm | An algorithm that produces a stable matching by iteratively proposing and accepting/rejecting proposals |
| Suitor-optimality | The property that each suitor receives the best possible partner across all stable matchings |
| Reviewer-pessimality | The property that in suitor-optimal matchings, each reviewer receives the worst acceptable partner |
```

```{important}
The Gale-Shapley algorithm demonstrates how a simple, local, step-by-step
procedure can achieve globally stable outcomes even in complex preference
structures. This insight has led to numerous successful applications in market
design, from medical residency matches to school choice systems and organ
donation programs.
```
