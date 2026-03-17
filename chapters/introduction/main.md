---
kernelspec:
  name: python3
  display_name: "Python 3"
---

# Introduction

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
any discipline. A psychologist modeling a specific behavior? A
conservationist analyzing the conditions under which a policy is likely
to succeed? An economist studying strategic interactions in competitive
markets? A computer programmer implementing a game-theoretic algorithm?
Whatever your background, this book provides the necessary tools to
engage with game theory in a meaningful way.

The book includes four appendices that introduce mathematical theory
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

## What does this book cover?

The book is organised into three broad themes.

**Foundations of strategic interaction** — The opening chapters establish the
core language of game theory. The [Games](#chp:games) chapter introduces normal
and extensive form representations, strategies, and utilities. [Rationalisation](#chp:rationality)
develops the idea of best responses and iterated elimination of dominated
strategies. [Zero-Sum Games](#chp:zero_sum_games) shows how minimax optimisation
and linear programming characterise optimal play when players' interests are
directly opposed. [Nash Equilibrium](#chp:nash_equilibrium) formalises the
central solution concept — a strategy profile from which no player wishes to
deviate unilaterally — and the support enumeration algorithm provides a
systematic way to compute it. [Subgame Perfection](#chp:sub_game_perfection)
refines Nash equilibrium for extensive form games by requiring rationality at
every decision node, not just on the equilibrium path.

**Dynamics and long-run behaviour** — The middle chapters study how
equilibria arise and persist over time. [Repeated Games](#chp:repeated_games)
examines how cooperation can be sustained when players interact
indefinitely, culminating in the Folk Theorem. [Replicator Dynamics](#chp:replicator_dynamics)
models how strategy frequencies evolve in large populations under selection
pressure, providing a bridge between game theory and evolutionary biology.
The [Moran Process](#chp:moran_process) studies fixation in finite
populations. [Best Response Polytopes](#chp:best_response_polytopes)
introduces the Lemke–Howson algorithm as a geometric method for computing Nash
equilibria in two-player games.

**Applied models** — The final chapters apply game-theoretic reasoning to
specific domains. [Routing Games](#chp:routing_games) studies how selfish routing
decisions lead to inefficiency (the Price of Anarchy). [Matching Games](#chp:matching_games)
covers the Gale–Shapley algorithm and stable matchings. [Auction Games](#chp:auctions)
analyses first- and second-price auctions and Bayesian equilibrium bidding
strategies. [Social Choice](#chp:social_choice) investigates collective
decision-making and impossibility results. [Cooperative Games](#chp:cooperative_games)
considers coalition formation, the characteristic function, and the Shapley
value.

Four **appendices** provide self-contained mathematical background: numerical
integration, absorbing Markov chains, interior point optimisation (KKT
conditions), integer pivoting, and an overview of learning and evolutionary
dynamics.

## How is this book different from similar books?

There are a number of excellent books on game theory that are highly
recommended. For a fantastic introduction to the topic aimed at a
mathematical audience, see [@webb2007game]. The exhaustive
work [@maschler2020game] offers a vast amount of breadth and depth on
the subject, while [@roughgarden2010algorithmic] delves into modern
algorithmic approaches to modeling complex systems at an advanced level.

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
    chapter to illustrate and contextualize the theory, often drawing
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
:height: 300px

Visual representation of the relationships and flow between chapters.
```
