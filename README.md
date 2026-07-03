Join [the Game Theory Discord](https://github.com/drvinceknight/equilibrium_explorers) server to chat -- [direct invite link](https://discord.gg/NfTAkhAeyc).

# Game Theory

This is a Game Theory text book. You can read it [here](https://vknight.org/gtb/).

## Building the book

### Prerequisites

- [uv](https://docs.astral.sh/uv/) — Python package manager (replaces pip/venv)
- Node.js ≥ 18 (for MyST)
- A LaTeX distribution with `pdflatex` (e.g. MacTeX or TeX Live)
- [Typst](https://typst.app) — for the improved PDF build

Install on macOS:
```bash
brew install uv typst
```

On other platforms see the [uv installation docs](https://docs.astral.sh/uv/getting-started/installation/) and [Typst installation docs](https://github.com/typst/typst#installation).

### Setup

```bash
uv sync
```

This creates a `.venv` and installs all dependencies automatically.

### Serving locally

```bash
uv run myst start
```

### Cleaning the build

Remove all build artifacts (site, exports, templates, cache):
```bash
uv run myst clean --all
```

Or clean selectively:
```bash
uv run myst clean --html        # site output only
uv run myst clean --pdf         # PDF exports only
uv run myst clean --execute     # execution cache only
```

### Building the PDF

```bash
uv run myst build --typst --execute
```

This produces `exports/main.pdf`.

## Testing

The `tests/` directory holds a `pytest` suite that independently reproduces the
computational claims made in the worked examples and solutions. Each test
recomputes a numeric result using the same library the relevant chapter uses,
`nashpy`, `coopgt`, `matching`, `pref_voting` or `scipy`, and falls back to
`sympy`/`numpy` where no such library exists. Every test docstring points at the
chapter file and the section, exercise or solution it checks, so a failing test
identifies the exact passage to revisit. A library that is not installed causes
only its own tests to be skipped, so the suite can be run in a partial
environment.

`pytest` lives in the `dev` dependency group. We install it and run the suite
with:

```bash
uv sync --group dev
uv run pytest
```

The suite also runs automatically on every pull request and on pushes to `main`
through the `Tests` GitHub Actions workflow.
