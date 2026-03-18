---
kernelspec:
  name: python3
  display_name: "Python 3"
---

(chp:matching_games)=

# Matching Games

Many allocation problems require pairing agents from two groups such that no
pair would mutually prefer to be matched to each other instead. This chapter
develops the theory of stable matchings and the Gale–Shapley algorithm that
constructs them.

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

#### Example: Author Reviewer as a Matching Game

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

#### Example: Blocking pair for the author reviewer game

In [](#eqn:unstable_matching) the pair $(A4, R2)$ is a blocking pair as $A4$
prefer $R2$ to $M(A4)$ and $R2$ prefers $A4$ to $M^{-1}(R2)$.

### Definition: a stable matching

A matching $M$ with no blocking pair is said to be stable.

#### Example: A stable matching for the author reviewer game

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

#### Proof

Suppose that an arbitrary execution $\alpha$ of the algorithm gives $M$ and that another
execution $\beta$ gives $M'$ such that $\exists$ $s\in S$ such that $s$ prefers $r'=M'(s)$ to $r=M(s)$.

Without loss of generality this implies that during $\alpha$ $r'$ must have rejected $s$.
Suppose, again without loss of generality that this was the first occasion that a rejection occurred
during $\alpha$ and assume that this rejection occurred because $r'=M(s')$.
This implies that $s'$ has no stable match that is higher in $s'$'s preference list
than $r'$ (as we have assumed that this is the first rejection).

Thus $s'$ prefers $r'$ to $M'(s')$ so that $(s',r')$ blocks $M'$.
Each suitor is therefore matched in $M$ with his favorite stable reviewer and since
$\alpha$ was arbitrary it follows that all possible executions give the same matching.

#### Example: Application of the Gale-Shapley algorithm to the author reviewer game

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
time), $A2$ has preference list $f(A2)=(R4, R3, R5, R1)$, the top of the
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
R2, R1)$, the top of the preference list is $R5$ but $R5$ is matched ($M(A3)=R5$). 
We have $g(R5)=(A5, A3, A4, A1, A2)$ so $R5$ prefers $A5$ to their current
matching. So we set:

$$
\begin{align*}
    M(A1) &= R3\\
    M(A2) &= R4\\
    M(A4) &= R2\\
    M(A5) &= R5\\
\end{align*}
$$

We now pick $A3$, the one remaining unmatched author, which has $f(A3)=(R5, R2,
R3, R1, R4)$, the top of the preference list is $R5$ but $R5$ is matched and
prefers their current matching so we remove it from $A3$'s preference list:

$$f(A3)=(R2, R3, R1, R4)$$

We now pick $A3$ again as it is still the only unmatched author. The top of the
preference list is $R2$ but $R2$ is matched and prefers their current matching
so we remove it from $A3$'s preference list:

$$f(A3)=(R3, R1, R4)$$

We pick $A3$ again. The top of the
preference list is $R3$ but $R3$ is matched and prefers their current matching
so we remove it from $A3$'s preference list:

$$f(A3)=(R1, R4)$$

We pick $A3$ again and match it to $R1$ giving the final matching:

$$
\begin{align*}
    M(A1) &= R3\\
    M(A2) &= R4\\
    M(A3) &= R1\\
    M(A4) &= R2\\
    M(A5) &= R5\\
\end{align*}
$$

### Theorem: Reviewer sub optimality of the Gale Shapley Algorithm

In a suitor-optimal stable matching each reviewer has the worst possible matching.

#### Proof

Assume that the result is not true. Let $M_0$ be a suitor-optimal matching
and assume that there is a stable matching $M'$ such that $\exists$
$r$ such that $r$ prefers $s=M_0^{-1}(r)$ to $s'=M'^{-1}(r)$.
This implies that $(r,s)$ blocks $M'$ unless $s$ prefers $M'(s)$
to $M_0(s)$ which contradicts the fact the $s$ has no stable match that
they prefer in $M_0$.

## Exercises

```{exercise}
:label: application_of_the_gale_shapley_algorithm

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
```

```{exercise}
:label: uniqueness_with_a_single_reviewer_preference_list

Consider a matching game where all reviewers have the same preference list.
Prove that there is a single stable matching.
```

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

---

(solutions:matching_games)=

## Solutions

````{solution} application_of_the_gale_shapley_algorithm
:label: solution:application_of_the_gale_shapley_algorithm

For each game we run the Gale-Shapley algorithm from the suitor (A) side to
obtain the suitor-optimal matching, then repeat with the reviewer (R) side
proposing to obtain the reviewer-optimal (equivalently, suitor-pessimal) matching.

**1.**

$$
\begin{align*}
    f(A1)&=(R2, R1, R3)\\
    f(A2)&=(R1, R3, R2)\\
    f(A3)&=(R1, R3, R2)\\
    g(R1)&=(A1, A2, A3)\\
    g(R2)&=(A2, A1, A3)\\
    g(R3)&=(A2, A3, A1)\\
\end{align*}
$$

**Suitor-optimal matching (A proposes):**

- A1 proposes to R2 (top of A1's list). R2 is unmatched, so $M(A1)=R2$.
- A2 proposes to R1 (top of A2's list). R1 is unmatched, so $M(A2)=R1$.
- A3 proposes to R1 (top of A3's list). R1 is matched to A2. $g(R1)=(A1,A2,A3)$,
  so R1 prefers A2 to A3. A3 is rejected; remove R1 from A3's list:
  $f(A3)=(R3, R2)$.
- A3 proposes to R3. R3 is unmatched, so $M(A3)=R3$.

Suitor-optimal matching:

$$
M_S: \quad M(A1)=R2,\quad M(A2)=R1,\quad M(A3)=R3
$$

**Verification (no blocking pairs):**

- $(A1, R1)$: A1 prefers R2 to R1 (R2 is first in A1's list). Not blocking.
- $(A1, R3)$: A1 prefers R2 to R3. Not blocking.
- $(A2, R2)$: A2 prefers R1 to R2. Not blocking.
- $(A2, R3)$: A2 prefers R1 to R3. Not blocking.
- $(A3, R1)$: A3 prefers R1 to R3, but R1 prefers A2 (current match) to A3. Not blocking.
- $(A3, R2)$: A3 prefers R3 to R2 (R3 is second, R2 is third in A3's remaining list).
  Actually $f(A3)=(R1,R3,R2)$ originally, so A3 prefers R3 to R2. Not blocking.

The matching is stable.

**Reviewer-optimal matching (R proposes):**

- R1 proposes to A1 (top of R1's list). A1 is unmatched, so $M^{-1}(R1)=A1$.
- R2 proposes to A2 (top of R2's list). A2 is unmatched, so $M^{-1}(R2)=A2$.
- R3 proposes to A2 (top of R3's list). A2 is matched to R2.
  $f(A2)=(R1,R3,R2)$, so A2 prefers R3 to R2. R2 is rejected; $M^{-1}(R3)=A2$.
  R2 removes A2 from its list: $g(R2)=(A1,A3)$.
- R2 proposes to A1. A1 is matched to R1. $f(A1)=(R2,R1,R3)$, so A1 prefers R2 to R1.
  R1 is rejected; $M^{-1}(R2)=A1$. R1 removes A1 from its list: $g(R1)=(A2,A3)$.
- R1 proposes to A2. A2 is matched to R3. $f(A2)=(R1,R3,R2)$, so A2 prefers R1 to R3.
  R3 is rejected; $M^{-1}(R1)=A2$. R3 removes A2 from its list: $g(R3)=(A3,A1)$.
- R3 proposes to A3. A3 is unmatched, so $M^{-1}(R3)=A3$.

Reviewer-optimal matching:

$$
M_R: \quad M(A1)=R2,\quad M(A2)=R1,\quad M(A3)=R3
$$

In this case both matchings coincide.

---

**2.**

$$
\begin{align*}
    f(A1)&=(R1, R3, R2)\\
    f(A2)&=(R2, R3, R1)\\
    f(A3)&=(R1, R3, R2)\\
    g(R1)&=(A1, A2, A3)\\
    g(R2)&=(A2, A3, A1)\\
    g(R3)&=(A2, A3, A1)\\
\end{align*}
$$

**Suitor-optimal matching (A proposes):**

- A1 proposes to R1. R1 is unmatched, so $M(A1)=R1$.
- A2 proposes to R2. R2 is unmatched, so $M(A2)=R2$.
- A3 proposes to R1. R1 is matched to A1. $g(R1)=(A1,A2,A3)$, so R1 prefers A1 to A3.
  A3 is rejected; $f(A3)=(R3,R2)$.
- A3 proposes to R3. R3 is unmatched, so $M(A3)=R3$.

Suitor-optimal matching:

$$
M_S: \quad M(A1)=R1,\quad M(A2)=R2,\quad M(A3)=R3
$$

**Reviewer-optimal matching (R proposes):**

- R1 proposes to A1. A1 is unmatched, so $M^{-1}(R1)=A1$.
- R2 proposes to A2. A2 is unmatched, so $M^{-1}(R2)=A2$.
- R3 proposes to A2. A2 is matched to R2. $f(A2)=(R2,R3,R1)$, so A2 prefers R2 to R3.
  R3 is rejected; $g(R3)=(A3,A1)$.
- R3 proposes to A3. A3 is unmatched, so $M^{-1}(R3)=A3$.

Reviewer-optimal matching:

$$
M_R: \quad M(A1)=R1,\quad M(A2)=R2,\quad M(A3)=R3
$$

Again both matchings coincide.

---

**3.**

$$
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

**Suitor-optimal matching (A proposes):**

- A1 proposes to R1. R1 is unmatched, so $M(A1)=R1$.
- A2 proposes to R2. R2 is unmatched, so $M(A2)=R2$.
- A3 proposes to R4. R4 is unmatched, so $M(A3)=R4$.
- A4 proposes to R1. R1 matched to A1. $g(R1)=(A1,A4,A2,A3)$: R1 prefers A1 to A4.
  A4 rejected; $f(A4)=(R4,R3,R2)$.
- A4 proposes to R4. R4 matched to A3. $g(R4)=(A2,A4,A1,A3)$: R4 prefers A4 to A3.
  A3 displaced; $M(A4)=R4$. A3's list: $f(A3)=(R1,R3,R2)$.
- A3 proposes to R1. R1 matched to A1. $g(R1)=(A1,A4,A2,A3)$: R1 prefers A1 to A3.
  A3 rejected; $f(A3)=(R3,R2)$.
- A3 proposes to R3. R3 unmatched, so $M(A3)=R3$.

Suitor-optimal matching:

$$
M_S: \quad M(A1)=R1,\quad M(A2)=R2,\quad M(A3)=R3,\quad M(A4)=R4
$$

**Reviewer-optimal matching (R proposes):**

- R1 proposes to A1. A1 unmatched, so $M^{-1}(R1)=A1$.
- R2 proposes to A1. A1 matched to R1. $f(A1)=(R1,R4,R2,R3)$: A1 prefers R1 to R2.
  R2 rejected; $g(R2)=(A3,A4,A2)$.
- R3 proposes to A4. A4 unmatched, so $M^{-1}(R3)=A4$.
- R4 proposes to A2. A2 unmatched, so $M^{-1}(R4)=A2$.
- R2 proposes to A3. A3 unmatched, so $M^{-1}(R2)=A3$.

Reviewer-optimal matching:

$$
M_R: \quad M(A1)=R1,\quad M(A2)=R4,\quad M(A3)=R2,\quad M(A4)=R3
$$

---

**4.**

$$
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

**Suitor-optimal matching (A proposes):**

- A1 proposes to R2. R2 unmatched, so $M(A1)=R2$.
- A2 proposes to R2. R2 matched to A1. $g(R2)=(A4,A2,A1,A3)$: R2 prefers A2 to A1.
  A1 displaced; $M(A2)=R2$. A1's list: $f(A1)=(R1,R4,R3)$.
- A3 proposes to R1. R1 unmatched, so $M(A3)=R1$.
- A4 proposes to R1. R1 matched to A3. $g(R1)=(A1,A2,A4,A3)$: R1 prefers A4 to A3.
  A3 displaced; $M(A4)=R1$. A3's list: $f(A3)=(R4,R3,R2)$.
- A1 proposes to R1. R1 matched to A4. $g(R1)=(A1,A2,A4,A3)$: R1 prefers A1 to A4.
  A4 displaced; $M(A1)=R1$. A4's list: $f(A4)=(R4,R3,R2)$.
- A4 proposes to R4. R4 unmatched, so $M(A4)=R4$.
- A3 proposes to R4. R4 matched to A4. $g(R4)=(A3,A2,A4,A1)$: R4 prefers A3 to A4.
  A4 displaced; $M(A3)=R4$. A4's list: $f(A4)=(R3,R2)$.
- A4 proposes to R3. R3 unmatched, so $M(A4)=R3$.

Suitor-optimal matching:

$$
M_S: \quad M(A1)=R1,\quad M(A2)=R2,\quad M(A3)=R4,\quad M(A4)=R3
$$

**Reviewer-optimal matching (R proposes):**

- R1 proposes to A1. A1 unmatched, so $M^{-1}(R1)=A1$.
- R2 proposes to A4. A4 unmatched, so $M^{-1}(R2)=A4$.
- R3 proposes to A4. A4 matched to R2. $f(A4)=(R1,R4,R3,R2)$: A4 prefers R3 to R2.
  R2 rejected; $M^{-1}(R3)=A4$. $g(R2)=(A2,A1,A3)$.
- R4 proposes to A3. A3 unmatched, so $M^{-1}(R4)=A3$.
- R2 proposes to A2. A2 unmatched, so $M^{-1}(R2)=A2$.

Reviewer-optimal matching:

$$
M_R: \quad M(A1)=R1,\quad M(A2)=R2,\quad M(A3)=R4,\quad M(A4)=R3
$$

Both matchings again coincide.

The following code verifies the suitor-optimal matchings using the `matching` library:

```{code-cell} python3
import matching
import matching.games


def solve_matching(suitor_prefs, reviewer_prefs):
    suitor_names = list(suitor_prefs.keys())
    reviewer_names = list(reviewer_prefs.keys())
    suitors = {name: matching.Player(name) for name in suitor_names}
    reviewers = {name: matching.Player(name) for name in reviewer_names}
    for name, prefs in suitor_prefs.items():
        suitors[name].set_prefs([reviewers[r] for r in prefs])
    for name, prefs in reviewer_prefs.items():
        reviewers[name].set_prefs([suitors[s] for s in prefs])
    game = matching.games.StableMarriage(
        list(suitors.values()), list(reviewers.values())
    )
    result = game.solve()
    return {str(k): str(v) for k, v in result.items()}


# Game 1
result1 = solve_matching(
    {"A1": ["R2","R1","R3"], "A2": ["R1","R3","R2"], "A3": ["R1","R3","R2"]},
    {"R1": ["A1","A2","A3"], "R2": ["A2","A1","A3"], "R3": ["A2","A3","A1"]},
)
print("Game 1 suitor-optimal:", result1)
```

```{code-cell} python3
# Game 2
result2 = solve_matching(
    {"A1": ["R1","R3","R2"], "A2": ["R2","R3","R1"], "A3": ["R1","R3","R2"]},
    {"R1": ["A1","A2","A3"], "R2": ["A2","A3","A1"], "R3": ["A2","A3","A1"]},
)
print("Game 2 suitor-optimal:", result2)
```

```{code-cell} python3
# Game 3
result3 = solve_matching(
    {
        "A1": ["R1","R4","R2","R3"],
        "A2": ["R2","R1","R3","R4"],
        "A3": ["R4","R1","R3","R2"],
        "A4": ["R1","R4","R3","R2"],
    },
    {
        "R1": ["A1","A4","A2","A3"],
        "R2": ["A1","A3","A4","A2"],
        "R3": ["A4","A1","A3","A2"],
        "R4": ["A2","A4","A1","A3"],
    },
)
print("Game 3 suitor-optimal:", result3)
```

```{code-cell} python3
# Game 4
result4 = solve_matching(
    {
        "A1": ["R2","R1","R4","R3"],
        "A2": ["R2","R3","R1","R4"],
        "A3": ["R1","R4","R3","R2"],
        "A4": ["R1","R4","R3","R2"],
    },
    {
        "R1": ["A1","A2","A4","A3"],
        "R2": ["A4","A2","A1","A3"],
        "R3": ["A4","A1","A3","A2"],
        "R4": ["A3","A2","A4","A1"],
    },
)
print("Game 4 suitor-optimal:", result4)
```
````

````{solution} uniqueness_with_a_single_reviewer_preference_list
:label: solution:uniqueness_with_a_single_reviewer_preference_list

**Claim:** If all reviewers share the same preference list over suitors, there is
exactly one stable matching.

**Proof:**

Let the shared reviewer preference list rank the suitors as
$s_{\sigma(1)} \succ s_{\sigma(2)} \succ \cdots \succ s_{\sigma(N)}$
(where $\sigma$ is a permutation of $\{1, \dots, N\}$ giving the common ordering).

Suppose, for contradiction, that there are two distinct stable matchings $M$ and
$M'$.

Since $M \ne M'$ and both are bijections from suitors to reviewers, there exists
some suitor $s$ with $M(s) \ne M'(s)$. Let $r = M(s)$ and $r' = M'(s)$.

Because all reviewers share the same preference list, the reviewer $r'$ (who is
matched to some $s'' \ne s$ in $M$) either prefers $s$ to $s''$ or prefers $s''$
to $s$.

**Case 1:** $r'$ prefers $s$ to $s'' = M^{-1}(r')$.

Then in matching $M$, the pair $(s, r')$ is a blocking pair: $s$ prefers $r'$
(since $M'(s)=r'$ and $s$ prefers $r'$ to $r$ — otherwise $s$ would be matched to
$r$ in $M'$ as well after running the algorithm) and $r'$ prefers $s$ to its
current partner $s''$. This contradicts the stability of $M$.

**Case 2:** $r'$ prefers $s''$ to $s$.

Since all reviewers share the same preference list, this preference is the same
for every reviewer. In particular, every reviewer ranks $s''$ above $s$. But then
in matching $M'$, consider the pair $(s'', M'(s''))$. The suitor $s''$ is matched
to some reviewer $r''$ in $M'$. Since in $M$, $s''$ is matched to $r'$, and $r'$
prefers $s''$ to $s$, we can recursively construct a chain. Since $N$ is finite
this chain must eventually lead to a contradiction.

More precisely, we can argue by a counting/ranking argument: since all reviewers
have the same preference list, the reviewer-optimal stable matching is unique and
equals the suitor-pessimal matching. The suitor-optimal matching is also unique
(by the theorem on unique output of the Gale-Shapley algorithm). If the suitor-
and reviewer-optimal matchings differ, one could exhibit a blocking pair. We show
they must coincide.

In the Gale-Shapley algorithm (suitors propose), when suitor $s_i$ proposes to
reviewer $r$, reviewer $r$ accepts the proposal from whichever of its current
tentative partner or $s_i$ it prefers — using the shared preference list. Because
all reviewers consult the same ranking, the outcome is fully determined by this
single ordering: a suitor higher in the common ranking will always displace a
suitor lower in it. Thus:

- Each reviewer $r$ ends up matched to the highest-ranked suitor (in the shared
  list) who ever proposes to it.
- Since suitors propose in decreasing order of preference and are rejected only
  when a better (in the shared ranking) suitor proposes, the final matching is
  entirely determined by the shared ranking.

Any two executions of the algorithm therefore produce the same matching.
Furthermore, no other stable matching can exist: if $M$ is stable and $M \ne M_S$
(the Gale-Shapley output), then some reviewer $r$ is matched to a suitor $s$
ranked lower in the shared list than their partner in $M_S$. But then the pair
$(M_S^{-1}(r), r)$ is a blocking pair for $M$, contradicting stability.

Hence there is exactly one stable matching. ◼
````
