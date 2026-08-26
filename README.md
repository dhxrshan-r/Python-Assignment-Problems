# Python Practice Problems

This repository contains Python exercises and practical assignments completed across Modules 1–8. It includes foundational programming work, data-structure exercises, string and list processing, algorithmic thinking, and computational-efficiency problems.

## Repository Contents

### Course Modules

The `Module 1` through `Module 8` directories contain lecture examples, exercises, and practical problems organized by module.

### Practical Assignment Collections

| Directory | Focus |
| --- | --- |
| [`strings-lists-dhxrshanr-ai`](strings-lists-dhxrshanr-ai/) | String, list, and CSV processing problems |
| [`algorithmic-thinking-dhxrshanr-ai`](algorithmic-thinking-dhxrshanr-ai/) | Algorithm design and problem-solving exercises |
| [`efficiency-dhxrshanr-ai`](efficiency-dhxrshanr-ai/) | Runtime efficiency, searching, graphs, and data structures |

The assignment collections contain their own `tests` directories and README files where applicable.

## Topics Covered

- Python syntax, data types, operators, and functions
- Conditional logic, scope, and debugging
- `for` and `while` loops, indexing, and sequence processing
- Nested lists, nested loops, and recursion
- String immutability and list mutability
- CSV parsing and data transformation
- Encryption exercises, including Atbash and RSA-related problems
- Top-down design, test-driven development, and PEP 8
- Big-O analysis, searching, sets, dictionaries, and graph algorithms

## Running the Code

Python 3 is required. From the repository root, run an individual script with:

```bash
python "Module 1/Practical 1.py"
```

Paths containing spaces should remain enclosed in quotation marks.

## Running Tests

If `pytest` is installed, run all discovered tests from the repository root:

```bash
python -m pytest
```

To run a specific assignment’s tests:

```bash
python -m pytest strings-lists-dhxrshanr-ai/tests
python -m pytest algorithmic-thinking-dhxrshanr-ai/tests
python -m pytest efficiency-dhxrshanr-ai/tests
```
