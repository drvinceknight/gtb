#!/usr/bin/env python3
"""
Convert chained $$ math blocks to \begin{align*}...\end{align*} blocks.

A "chained" block is a $$\n...\n$$ block where at least one line after the first
starts with optional whitespace then =.

Skips blocks that contain prose/lists (lines matching ^\d+\. or starting with
a capital letter word like a sentence, or containing ```).

Conversion rules:
1. Wrap block content in \begin{align*}\n...\n\end{align*}
2. For each "continuation line" (starts with optional whitespace + =), add \\
   to the LAST non-empty line before it, then insert & between leading whitespace and =
3. For line 0 (if it doesn't start with =), insert & before the first standalone =
   using re.sub(r'(?<![=!<>\\\|&])=(?!=)', '&=', line, count=1)
4. If line 0 starts with =, apply the same rule as a continuation line

Do NOT add \\ to lines that are inside a matrix environment.
Track depth with a counter.
"""

import re
import sys

FILES = [
    "chapters/subgame_perfection/main.md",
    "chapters/auction_games/main.md",
    "chapters/further_learning_dynamics/main.md",
    "chapters/zero_sum_games/main.md",
    "chapters/repeated_games/main.md",
    "chapters/replicator_dynamics/main.md",
    "chapters/cooperative_games/main.md",
    "chapters/evolutionary_biology/main.md",
    "chapters/moran_process/main.md",
    "chapters/direct_reciprocity/main.md",
    "appendices/absorbing_markov_chains/main.md",
    "appendices/ergodic_markov_chains/main.md",
    "appendices/integer_pivoting/main.md",
]

BASE = "/Users/smavak/etc/gtb"

# Regex for matching a $$ block
BLOCK_RE = re.compile(r'\$\$\n(.*?)\n\$\$', re.DOTALL)

# Matrix environment openers/closers
MATRIX_BEGIN_RE = re.compile(r'\\begin\{(pmatrix|bmatrix|vmatrix|matrix|array)\}')
MATRIX_END_RE = re.compile(r'\\end\{(pmatrix|bmatrix|vmatrix|matrix|array)\}')

# Pattern for a "continuation line": optional whitespace then =
CONTINUATION_RE = re.compile(r'^(\s*)=')

# Pattern for prose detection
ORDERED_LIST_RE = re.compile(r'^\d+\.')
SENTENCE_START_RE = re.compile(r'^[A-Z][a-z]')
CODE_FENCE_RE = re.compile(r'```')


def is_chained_block(content):
    """Check if block has at least one continuation line (optional whitespace then =)."""
    lines = content.split('\n')
    # Check lines after the first
    for line in lines[1:]:
        if CONTINUATION_RE.match(line):
            return True
    return False


def has_prose(content):
    """Check if block contains prose/list content that should be skipped."""
    lines = content.split('\n')
    for line in lines:
        stripped = line.strip()
        if ORDERED_LIST_RE.match(stripped):
            return True
        if SENTENCE_START_RE.match(stripped):
            return True
        if CODE_FENCE_RE.search(line):
            return True
    return False


def is_inside_existing_align(content):
    """Check if block already has \begin{align...} or \begin{aligned}."""
    if re.search(r'\\begin\{align', content):
        return True
    return False


def transform_block(content):
    """Transform the content of a $$ block to align* format."""
    lines = content.split('\n')

    # Track matrix depth
    matrix_depth = 0

    # First, process each line: determine which need continuation treatment
    # We need to:
    # 1. Add \\ to the last non-empty line before a continuation line (if not in matrix)
    # 2. Insert & into continuation lines
    # 3. Insert & into line 0 (special treatment)

    result_lines = []

    for i, line in enumerate(lines):
        # Update matrix depth based on this line
        matrix_depth += len(MATRIX_BEGIN_RE.findall(line))
        matrix_depth -= len(MATRIX_END_RE.findall(line))
        if matrix_depth < 0:
            matrix_depth = 0

        # Check if this line is a continuation line
        m = CONTINUATION_RE.match(line)
        is_continuation = (m is not None)

        if i == 0:
            # Line 0: if it starts with =, treat as continuation line (insert & before =)
            if is_continuation:
                leading = m.group(1)
                rest = line[len(leading) + 1:]  # everything after the =
                result_lines.append(leading + '&=' + rest)
            else:
                # Insert & before the first standalone = not inside matrix
                if matrix_depth == 0:
                    new_line = re.sub(r'(?<![=!<>\\\|&])=(?!=)', '&=', line, count=1)
                    result_lines.append(new_line)
                else:
                    result_lines.append(line)
        else:
            if is_continuation and matrix_depth == 0:
                # Find the last non-empty line in result_lines and add \\ to it
                # (only if it doesn't already end with \\)
                for j in range(len(result_lines) - 1, -1, -1):
                    if result_lines[j].strip():
                        if not result_lines[j].rstrip().endswith('\\\\'):
                            result_lines[j] = result_lines[j].rstrip() + '\\\\'
                        break
                # Insert & between leading whitespace and =
                leading = m.group(1)
                rest = line[len(leading) + 1:]  # everything after the =
                result_lines.append(leading + '&=' + rest)
            else:
                result_lines.append(line)

        # Re-check matrix depth after processing: matrix open/close on SAME line
        # Already handled above - depth was updated at start of loop

    new_content = '\n'.join(result_lines)
    return '\\begin{align*}\n' + new_content + '\n\\end{align*}'


def process_file(filepath):
    """Process a single file, converting chained $$ blocks."""
    full_path = BASE + '/' + filepath

    with open(full_path, 'r', encoding='utf-8') as f:
        original = f.read()

    conversions = []

    def replace_block(match):
        content = match.group(1)

        # Skip if already has align environment
        if is_inside_existing_align(content):
            return match.group(0)

        # Only process chained blocks
        if not is_chained_block(content):
            return match.group(0)

        # Skip prose blocks
        if has_prose(content):
            return match.group(0)

        # Transform the block
        transformed = transform_block(content)
        original_block = match.group(0)
        conversions.append({
            'original': original_block,
            'transformed': '$$\n' + transformed + '\n$$'
        })
        return '$$\n' + transformed + '\n$$'

    new_content = BLOCK_RE.sub(replace_block, original)

    return new_content, conversions


def main():
    total_conversions = 0

    for filepath in FILES:
        full_path = BASE + '/' + filepath
        print(f"\n{'='*60}")
        print(f"Processing: {filepath}")
        print('='*60)

        try:
            new_content, conversions = process_file(filepath)
        except FileNotFoundError:
            print(f"  SKIP: file not found")
            continue

        if not conversions:
            print("  No chained $$ blocks found to convert.")
            continue

        # Write the modified content
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"  Converted {len(conversions)} block(s):")
        for i, conv in enumerate(conversions, 1):
            # Show a brief summary: first line of original content
            orig_lines = conv['original'].split('\n')
            # Find first non-empty content line
            preview = ''
            for line in orig_lines[1:]:
                stripped = line.strip()
                if stripped and stripped != '$$':
                    preview = stripped[:80]
                    break
            print(f"    [{i}] {preview!r}")

        total_conversions += len(conversions)

    print(f"\n{'='*60}")
    print(f"Total conversions: {total_conversions}")


if __name__ == '__main__':
    main()
