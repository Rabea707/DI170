# AI Agent Instructions for DI170 Coding Course

## Project Overview
This is an **educational Python learning repository** spanning 7 weeks of structured programming instruction. The codebase contains:
- **Foundational concepts** (Week 1-3): variables, casting, control flow, loops, lists, dicts, sets
- **Intermediate topics** (Week 2-5): functions, args/kwargs, classes, OOP
- **Applied projects** (Week 3+): Tic-Tac-Toe game, anagram checker, calculator

This is **instructional code**, not production software - prioritize clarity and learning outcomes over optimization.

## Directory Structure & Patterns

### Exercise Organization
Files follow a naming convention that reveals learning stages:
```
weekN/
├── dayM/
│   ├── Studyday{M}/     # Concept introduction with examples (casting.py, loops.py, classes.py)
│   └── Exerciesday{M}/  # Practice exercises implementing that day's concept
```

**Key pattern**: Study files contain conceptual examples; Exercise files test application of those concepts.

### Topic Examples by Week
- **Week 1**: Basic types, casting ([week1/Day1/Studyday1/casting.py](week1/Day1/Studyday1/casting.py)), control flow
- **Week 2**: Functions, args/kwargs ([week2/day1/studyday1/argsandkwargs.py](week2/day1/studyday1/argsandkwargs.py)), OOP fundamentals
- **Week 3+**: Mini-projects ([week2/day3/TIC-TAC-TOE.py](week2/day3/TIC-TAC-TOE.py), [week3/day5/anagram_checker.py](week3/day5/anagram_checker.py))

## Development Conventions

### Code Style
- Minimal - files are often short, focused exercises (10-50 lines)
- Comments may have typos ("exercies" vs "exercises", "indux" vs "index") - **preserve them** as they appear in original code
- No strict linting - prioritize readability for learners

### File Naming Quirks
Watch for case inconsistencies and typos:
- `Exercies*.py` or `exercies*.py` (intentional variations)
- `indux1.html` (appears to be intentional or historical - preserve as-is)
- Multiple naming conventions within same directory (capital vs lowercase)

### Running Code
- Python files run independently: `python filename.py`
- Most files are designed for command-line interaction with `input()` calls
- No external dependencies beyond Python stdlib (json, no frameworks required)

## Common Patterns to Implement

### Pattern 1: User Input Loops
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
See: [week2/day3/TIC-TAC-TOE.py#L21](week2/day3/TIC-TAC-TOE.py#L21)

### Pattern 2: Function Teaching (Args/Kwargs)
Functions often include multiple parameter styles to demonstrate concepts:
- positional args
- keyword arguments  
- `*args` and `**kwargs`

See: [week2/day1/studyday1/argsandkwargs.py](week2/day1/studyday1/argsandkwargs.py)

### Pattern 3: Class Skeletons
Many class files are partially implemented stubs for student completion:
```python
class ClassName:
    def __init__(self, param):
        self.param = param
    
    def method(self):
        pass  # Student implements
```
See: [week3/day5/anagram_checker.py](week3/day5/anagram_checker.py)

### Pattern 4: Board/Grid Display Games
Multi-dimensional list display using string formatting:
```python
for row in board:
    print(" " + " | ".join(row))
```
See: [week2/day3/TIC-TAC-TOE.py#L11](week2/day3/TIC-TAC-TOE.py#L11)

## When Helping with Code

1. **Preserve typos and naming quirks** - they're part of the learning artifacts
2. **Explain the "why"** - add comments explaining concepts, not just fixing code
3. **For stub files** - complete missing method bodies with clear, commented implementations
4. **For exercises** - suggest solutions but explain the learning objective
5. **Test interactively** - these files often depend on user input; verify with actual `python` runs

## Files to Review When Starting

- [week1/Day1/Studyday1/casting.py](week1/Day1/Studyday1/casting.py) - foundational patterns
- [week2/day1/studyday1/argsandkwargs.py](week2/day1/studyday1/argsandkwargs.py) - function conventions
- [week2/day3/TIC-TAC-TOE.py](week2/day3/TIC-TAC-TOE.py) - interactive project structure
- [week3/day5/anagram_checker.py](week3/day5/anagram_checker.py) - OOP class patterns
