# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an educational coding course repository (DI170) progressing through Python fundamentals and then web development. It is **instructional code, not production software** — prioritize clarity and learning over optimization.

- **Weeks 1–3**: Python (variables, casting, control flow, functions, args/kwargs, OOP, mini-projects)
- **Weeks 7–8**: Web development (HTML, CSS, vanilla JavaScript, DOM manipulation, events)
- **crashcours/**: Web fundamentals crash course

## Running Code

```bash
# Python files (no external dependencies — pure stdlib only)
python week1/Day1/Studyday1/casting.py
python week2/day3/TIC-TAC-TOE.py

# JavaScript files
node week7/day1/script.js

# HTML files — open directly in browser
```

No build system, package manager, test framework, or linter is configured.

## Directory Structure Pattern

Each week/day is split into two directory types:
- `Studyday{N}/` — conceptual examples with comments
- `Exerciesday{N}/` (or `exerciesday{N}/`) — practice problems for the student to implement

## Code Conventions

- Files are short and focused (10–50 lines)
- **Preserve all typos and naming quirks** — e.g., `Exercies` vs `exercises`, `indux1.html`, `indxe.html`, mixed capitalization. These are learning artifacts and should not be corrected.
- No strict linting; readability for learners is the priority.

## Common Python Patterns

**User input validation loop:**
```python
while True:
    try:
        value = int(input("prompt: "))
        if value < 0 or value > max:
            print("Invalid range")
            continue
        break
    except ValueError:
        print("Please enter numbers only.")
```
See: `week2/day3/TIC-TAC-TOE.py:21`

**Board/grid display:**
```python
for row in board:
    print(" " + " | ".join(row))
```
See: `week2/day3/TIC-TAC-TOE.py:11`

**Class stubs for student completion:**
```python
class ClassName:
    def __init__(self, param):
        self.param = param

    def method(self):
        pass  # Student implements
```
See: `week3/day5/anagram_checker.py`

## Key Reference Files

| File | What it demonstrates |
|------|---------------------|
| `week1/Day1/Studyday1/casting.py` | Foundational type patterns |
| `week2/day1/studyday1/argsandkwargs.py` | Args/kwargs function conventions |
| `week2/day3/TIC-TAC-TOE.py` | Interactive project structure |
| `week3/day5/anagram_checker.py` | OOP class patterns |
| `week8/day3/ColerGame/` | DOM event-based interactive web project |

## When Helping with Exercises

- For stub files: complete missing method bodies with clear, commented implementations explaining the concept
- For exercises: explain the learning objective alongside any solution
- These files often depend on `input()` — verify behavior by actually running with `python`
