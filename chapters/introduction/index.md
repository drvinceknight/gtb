---
kernelspec:
  name: python3
  display_name: "Python 3"
---

# Introduction

```{figure} assets/illustrations/hercules_beetles.png
:alt: Two Hercules beetles squaring up, each admitting they would rather not fight.
:label: fig:hercules_beetles
:class: illustration
:width: 80%

Two Hercules beetles weigh up a contest that neither truly wants. The escalation
of conflict, and the conditions under which it is or is not worth it, is a
recurring theme in game theory.
```

## What is Game Theory?

A common definition of the subject is:

> "Game theory is the study of interactive decision-making where the
> outcomes of one decision maker's choices depend on the decisions made
> by others."

While this definition captures the essence of strategic interaction,
game theory is much more than that. It is a beautiful mathematical
discipline with deep theoretical avenues for exploration. It plays a
crucial role in the global economy, with multiple Nobel Prizes awarded
for contributions to our understanding of markets. It provides models
that explain how biological structures, from cells to ecosystems, evolve
over time. It offers insights into cooperation, competition, and the
formation of social norms.

Because game theory spans multiple disciplines, no single definition
fully captures its scope. This book aims to provide a solid
understanding of game theory: what it can do and how to apply it.

## Who is this book for?

This book is written primarily for advanced undergraduate mathematicians
and computer scientists. It may also serve as a starting point for
early-career researchers seeking a practical understanding of game
theory.

However, the book aims to be accessible to aspiring game theorists from
any discipline. A psychologist modelling a specific behaviour? A
conservationist analysing the conditions under which a policy is likely
to succeed? An economist studying strategic interactions in competitive
markets? A computer programmer implementing a game-theoretic algorithm?
Whatever your background, this book provides the necessary tools to
engage with game theory in a meaningful way.

The book includes appendices that introduce mathematical theory
independently of game theory. For some readers, these may serve as a
review of familiar topics, while for others, they offer a first
introduction to key techniques needed to apply game-theoretic ideas
effectively.

Each chapter includes a section demonstrating how software can be used
to apply the ideas at scale. These sections assume some familiarity with
Python and the ability to install external libraries. For an introduction
to these topics, see the chapters on
[Using Notebooks](https://vknight.org/pfm/tools-for-mathematics/01-using-notebooks/introduction/main.html)
and [Installing Libraries](https://vknight.org/pfm/further-information/04-pip-installing/introduction/main.html)
in the [_Python for Mathematics_](https://vknight.org/pfm/cover.html) text.

Game theory is a field that thrives on cross-disciplinary insights, and
this book is designed to help readers from different backgrounds develop
a shared mathematical foundation. Whether your interest is theoretical
or applied, the goal is to equip you with the tools to explore game
theory with confidence.

## Licence and access

There will **always be a free online version** of this book, available at
[vknight.org/gtb](https://vknight.org/gtb/). A PDF version is built alongside the
site and can be downloaded from
[vknight.org/gtb/pdf/main.pdf](https://vknight.org/gtb/pdf/main.pdf), and the full
source is on GitHub at
[github.com/drvinceknight/gt](https://github.com/drvinceknight/gt), from which the
site is built and served.

The book brings together material under three sets of terms. The prose, together
with the figures and diagrams created by the authors, is released under the
Creative Commons Attribution 4.0 International Licence (CC BY 4.0), so it may be
shared and adapted with attribution. The source code, including the executable
code cells and the build tooling, is released under the MIT Licence.

The illustrations are the work of James Brown ([nonzerosum.games](https://nonzerosum.games))
and are treated differently. They remain the copyright of their creator and are
included here by permission. They are **not** covered by the CC BY 4.0 licence
that applies to the rest of the book: James Brown retains full ownership of the
illustrations, may continue to use them and any variants of them in his own work,
and any reuse of an illustration outside this book requires his permission. Full
details are in the `LICENSE` and `ILLUSTRATIONS.md` files in the [repository](https://github.com/drvinceknight/gt).

## Citing this book

If this book contributes to your work we would appreciate a citation. A
suggested plain-text form is:

> Knight, V. and Brown, J. (2026). *Game Theory: Theory, Software, Research*.
> Available at [vknight.org/gtb](https://vknight.org/gtb/).

The corresponding BibTeX entry is:

```bibtex
@book{knight2026gametheory,
  author = {Knight, Vincent and Brown, James},
  title  = {Game Theory: Theory, Software, Research},
  year   = {2026},
  url    = {https://vknight.org/gtb/},
}
```

The repository also includes a
[`CITATION.cff`](https://github.com/drvinceknight/gt/blob/main/CITATION.cff)
file, from which GitHub can generate a citation in a number of common formats.

## What does this book cover?

The book is organised into three broad themes.

**Foundations of strategic interaction.** The opening chapters establish the
core language of game theory. The [Games](#chp:games) chapter introduces normal
and extensive form representations, strategies, and utilities. [Rationalisation](#chp:rationality)
develops the idea of best responses and iterated elimination of dominated
strategies. [Zero-Sum Games](#chp:zero_sum_games) shows how minimax optimisation
and linear programming characterise optimal play when players' interests are
directly opposed. [Nash Equilibrium](#chp:nash_equilibrium) formalises the
central solution concept, a strategy profile from which no player wishes to
deviate unilaterally, and the support enumeration algorithm provides a
systematic way to compute it. [Subgame Perfection](#chp:sub_game_perfection)
refines Nash equilibrium for extensive form games by requiring rationality at
every decision node, not just on the equilibrium path.

**Dynamics and long-run behaviour.** The middle chapters study how
equilibria arise and persist over time. [Repeated Games](#chp:repeated_games)
examines how cooperation can be sustained when players interact
indefinitely, culminating in the Folk Theorem. [Direct Reciprocity](#chp:direct_reciprocity)
extends this to memory-one strategies, showing how simple conditional rules
such as Tit-for-Tat can stabilise cooperation. [Evolutionary Biology](#chp:evolutionary_biology)
provides the wider biological context for evolutionary game theory and
motivates the dynamical models that follow; it is optional reading for a
purely mathematical pass through the book. [Replicator Dynamics](#chp:replicator_dynamics)
models how strategy frequencies evolve in large populations under selection
pressure. The [Moran Process](#chp:moran_process) studies fixation in finite
populations. [Learning and Evolutionary Dynamics](#chp:further_learning_dynamics)
examines how the choice of update rule (imitation, best response, or
generational turnover) shapes long-run outcomes across these models.
[Best Response Polytopes](#chp:best_response_polytopes)
introduces the Lemke–Howson algorithm as a geometric method for computing Nash
equilibria in two-player games.

**Allocation and collective choice.** The final chapters apply
game-theoretic reasoning to settings where resources, partners, or
decisions must be shared. [Routing Games](#chp:routing_games) studies how selfish routing
decisions lead to inefficiency (the Price of Anarchy). [Matching Games](#chp:matching_games)
covers the Gale–Shapley algorithm and stable matchings. [Auction Games](#chp:auctions)
analyses first- and second-price auctions and Bayesian equilibrium bidding
strategies. [Social Choice](#chp:social_choice) investigates collective
decision-making and impossibility results. [Cooperative Games](#chp:cooperative_games)
considers coalition formation, the characteristic function, and the Shapley
value.

Six **appendices** provide self-contained mathematical background: numerical
integration, absorbing Markov chains, ergodic Markov chains, interior point
optimisation (KKT conditions), integer pivoting, and order statistics.

Throughout, the emphasis is on games of complete information, in which the
players, their available actions, and their payoffs are common knowledge. This is
the classical setting in which the core solution concepts are cleanest to state
and compute. Games of incomplete information, where players hold private
information about their own payoffs, enter only in the [Auction Games](#chp:auctions)
chapter, through the notion of a Bayesian Nash equilibrium among bidders with
private valuations. A systematic treatment of Bayesian games, mechanism design,
and signalling lies beyond the scope of this book, and is a natural direction for
further study; the auctions chapter is intended as a first point of contact with
these ideas rather than a complete account of them.

## How is this book different from similar books?

There are a number of excellent books on game theory that are highly
recommended. For a fantastic introduction to the topic aimed at a
mathematical audience, see [@webb2007game]. The exhaustive
work [@maschler2020game] offers a vast amount of breadth and depth on
the subject, while [@roughgarden2010algorithmic] delves into modern
algorithmic approaches to modelling complex systems at an advanced level.

Some excellent texts focus on specific subtopics within the domain. For
example, [@gusfield1989stable] explores matching games,
and [@roughgarden2002selfish] addresses routing games. Other great
general introductions
include [@osborne2004introduction], [@watson2002strategy],
and [@gusfield1989stable], to name just a few.

This book, however, offers something that these fantastic works do not:
detailed implementation instructions, including multiple examples and
exercises that show how to solve specific problems, even when they are
large and complex. It also provides an overview of open-source
software tools that are readily available to solve real-world problems.
The book also includes discussion of relevant contemporary research aiming to
demonstrate not only how the topic is applied in practice but also its relevance.
Finally, it offers a rigorous theoretical
foundation, serving as a springboard for deeper theoretical analysis.

## How is this book organised?

Each chapter in this book follows a structured format:

1.  **A motivating case study:** a running example throughout the
    chapter to illustrate and contextualise the theory, often drawing
    from real-world scenarios.

2.  **Relevant definitions and theory:** providing a rigorous
    mathematical foundation for the chapter's topic.

3.  **Exercises:** a range of problems inviting the reader to apply the
    definitions and theory to deepen understanding.

4.  **Practical implementations:** including Python code,
    and an overview of relevant open-source tools to guide
    implementation.

5.  **Contemporary research:** a hand-picked, non-exhaustive overview of
    relevant research related to the chapter.

Some readers may prefer to focus on the theoretical foundations, while
others might engage primarily with the examples and practical
implementations. This book is designed to be flexible, allowing readers
to approach the material in a way that best suits their background and
interests.

[](#fig:structure) shows the general structure of the book and
how the various chapters link together.

```{figure} assets/chapter_relationship_diagram/main.png
:alt: A flow diagram between the chapters.
:label: fig:structure

Visual representation of the relationships and flow between chapters.
```
