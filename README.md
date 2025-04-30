# 📚 Style Guide for Your Game Theory Textbook

## 1. **Definitions**

- **Title**: Use `### Definition: [Name]`
- **Format**: Write the definition clearly and formally, in active voice when
  possible.
- **Math**: Inline math (`$...$`) for short expressions; block math only for
  long expressions.
- **Separator**: Use a horizontal rule (`---`) before and after a definition
  block to visually separate it.

✅ Example:

```markdown
### Definition: Extensive Form Game

---

An $N$-player extensive form game with complete information consists of:

- ...
- ...
- ...

---
```

---

## 2. **Examples**

- **Title**: Use `### Example: [Brief descriptive title]`
- **Introduction**: One or two short sentences to set up the context.
- **Blockquote** (`>`) for storytelling/narrative setup (especially if casual
  or character-driven).
- **Reference**: Clearly reference the associated figure early ("as shown in
  [Figure X]").

✅ Example:

```markdown
### Example: Coordination Game

Consider the following game, often referred to as the **Battle of the Sexes**.

> Two friends must decide which movie to watch at the cinema...
```

---

## 3. **Figures**

- Always reference with "as shown in [Figure X]" early in the paragraph.
- Label figures sequentially across the document (even across sections).
- Figure titles should be short, sentence-style, no period at the end.

✅ Example figure reference:

```markdown
The structure of the game is shown in [Figure 2](#fig:battle_of_the_sexes_bob_first).
```

✅ Example figure block:

````markdown
```{figure} ./images/filename.png
:alt: Short description.
:label: fig:short_description
:height: 250px

A short caption, sentence-style without a period
```
````

```

---

## 4.
```
