# Python - Test-driven Development

## Description
This project focuses on learning and implementing **Test-driven Development (TDD)** in Python using the `doctest` and `unittest` frameworks. The goal is to build safe, stable, and highly predictable code modules by writing and executing comprehensive test cases before finalizing production logic.

## Requirements
* All files are interpreted and compiled on **Ubuntu 20.04 LTS** using **python3** (version 3.8.5).
* All source code complies strictly with the **pycodestyle** (version 2.7.*) code style guidelines.
* Every module, class, and function includes comprehensive, multi-sentence documentation strings that describe their parameters, returns, and edge-case exceptions.
* No external modules or libraries are imported unless explicitly allowed by the task parameters (e.g., `numpy`).

## Project Files Reference

| File | Description | Test Path |
| :--- | :--- | :--- |
| `0-add_integer.py` | Adds two parameters safely after casting floats to standard integers. | `tests/0-add_integer.txt` |
| `2-matrix_divided.py` | Divides all elements of an input matrix by a scalar value and rounds to 2 decimal places. | `tests/2-matrix_divided.txt` |
| `3-say_my_name.py` | Safely validates and prints a formatted combination of first and last names. | `tests/3-say_my_name.txt` |
| `4-print_square.py` | Prints a complete square grid composed of `#` characters based on a given dimensional side length. | `tests/4-print_square.txt` |
| `5-text_indentation.py` | Formats a text block by appending 2 new lines immediately after `.`, `?`, and `:` punctuation characters. | `tests/5-text_indentation.txt` |
| `6-max_integer.py` | Locates and outputs the maximum integer item from a structured collection list. | `tests/6-max_integer_test.py` |
| `100-matrix_mul.py` | Performs complete linear algebraic multiplication across two valid mathematical matrices. | `tests/100-matrix_mul.txt` |
| `101-lazy_matrix_mul.py` | Leverages the high-performance `numpy` computation engine to safely execute matrix multiplication. | `tests/101-lazy_matrix_mul.txt` |

## How to Execute the Test Suites

### Running Doctests
To verify text-based docstring interactive evaluations while supporting numerical file naming conventions, run your checks with an active `PYTHONPATH` assignment rule:
```bash
PYTHONPATH=. python3 -m doctest -v tests/0-add_integer.txt
PYTHONPATH=. python3 -m doctest -v tests/2-matrix_divided.txt
PYTHONPATH=. python3 -m doctest -v tests/3-say_my_name.txt
PYTHONPATH=. python3 -m doctest -v tests/4-print_square.txt
PYTHONPATH=. python3 -m doctest -v tests/5-text_indentation.txt
PYTHONPATH=. python3 -m doctest -v tests/101-lazy_matrix_mul.txt
```

### Running Unittests
To launch automated system verification assertion classes built with Python's standard internal unit testing environment, run this instruction command:
```bash
python3 -m unittest tests.6-max_integer_test
```

### Style Verification Checks
To audit style alignments, run your code blocks through the local python linter suite validator tool:
```bash
pycodestyle *.py tests/*.py
```

## Author
* **Juanne Asabah**
