# Python - Almost a Circle

## 📝 Project Overview
This project serves as a comprehensive review of Python Object-Oriented Programming (OOP) concepts. The objective is to design and implement a flexible geometric model architecture featuring coordinate-aware shapes, data tracking mechanics, comprehensive testing suites, and object-to-dictionary serialization pipelines. 

The structural blueprint follows a rigorous hierarchy where specialized shapes (`Square`) inherit properties from generalized geometric definitions (`Rectangle`), which in turn rely on global identifier systems (`Base`).

---

## 📂 Directory Structure

```text
alu-higher_level_programming/
└── python-almost_a_circle/
    ├── README.md
    ├── models/
    │   ├── __init__.py
    │   ├── base.py
    │   ├── rectangle.py
    │   └── square.py
    └── tests/
        └── test_models/
            ├── __init__.py
            ├── test_base.py
            ├── test_rectangle.py
            └── test_square.py
```

---

## 🛠️ Environment & Constraints
* **Operating System**: Compiled and interpreted on `Ubuntu 20.04 LTS`.
* **Language Version**: `Python 3.8.5`.
* **Style Guide**: Code follows strict `pycodestyle` (version `2.7.*`) guidelines.
* **Testing Engine**: Core behaviors validated using the standard library `unittest` framework.
* **File Constraints**: All scripts are executable, use `#!/usr/bin/python3` as their first line, and end with a trailing newline character.

---

## 🎛️ Core Modules

### 1. Base Model (`models/base.py`)
Manages instance identifiers globally across all entities. It handles automated execution sequencing and acts as a central checkpoint to mitigate redundant indexing bugs.

### 2. Rectangle Model (`models/rectangle.py`)
Extends the tracking framework by introducing protected structural parameters (`width`, `height`, `x`, `y`). It integrates datatype casting, value ceiling validation barriers, dynamic surface rendering, string magical transformations, and dictionary serialization mappings.

### 3. Square Model (`models/square.py`)
Specialized class mirroring structural traits from the rectangle matrix. It locks geometric aspect constraints using a singular, unified `size` property while supporting broad argument unpacking algorithms.

---

## 🧪 Testing and Verification

To ensure full test suite discoverability and execute all behavioral assertions across models, use the absolute discovery flag in your terminal environment:

```bash
# Execute all tests inside the suite
python3 -m unittest discover tests

# Execute targeted module tests independently
python3 -m unittest tests/test_models/test_base.py
python3 -m unittest tests/test_models/test_rectangle.py
python3 -m unittest tests/test_models/test_square.py
```

### Checking Docstring Validity
All classes, modules, and individual methods feature comprehensive documentation written in complete, descriptive sentences. You can verify text documentation metrics with the standard internal inspection commands:

```bash
python3 -c 'print(__import__("models.base").base.__doc__)'
python3 -c 'print(__import__("models.rectangle").rectangle.Rectangle.__doc__)'
python3 -c 'print(__import__("models.square").square.Square.update.__doc__)'
```

