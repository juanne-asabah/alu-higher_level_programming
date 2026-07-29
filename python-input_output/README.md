# Python - Input/Output

An exploration of file handling mechanisms, data persistence techniques, and object serialization protocols using Python 3. This repository covers standard file operations (reading, writing, appending) as well as structured schema formatting with JSON models.

## Environment & Requirements

*   **Operating System:** Ubuntu 20.04 LTS
*   **Compiler/Interpreter:** Python 3.8.5
*   **Style Guide Compliance:** `pycodestyle` (version 2.7.*)
*   **Testing Protocol:** Validated using the `doctest` module interface

## Documented Task Catalog

### 0. Read file (`0-read_file.py`)
A function that safely streams and prints the contents of a UTF-8 text file directly to standard output (`stdout`) using the native `with` context management framework.

### 1. Write to a file (`1-write_file.py`)
A function that commits a text buffer string directly into a targeted UTF-8 disk location, overwriting pre-existing allocations, and returns the total character write length.

### 2. Append to a file (`2-append_write.py`)
A script function that targets the trailing bounds of an active file layout to append an external string array stream, returning the precise count of newly added data elements.

### 3. To JSON string (`3-to_json_string.py`)
A data transmission utility that converts standard native dictionary, list, and primitive type objects into fully serialized structural JSON strings.

### 4. From JSON string to Object (`4-from_json_string.py`)
A decoding utility engine that reads structured structural JSON schemas and builds fully interactive, deserialized native Python dictionaries or array structures.

### 5. Save Object to a file (`5-save_to_json_file.py`)
An automation script that flushes serialized object states directly into text files via JSON buffer pipes, preserving structure layouts efficiently.

### 6. Create object from a JSON file (`6-load_from_json_file.py`)
An instantiation utility that reads standard data objects out of structured physical disk documents and rebuilds active native collection models.

### 7. Load, add, save (`7-add_item.py`)
A command-line script that intercepts arguments passed via `sys.argv`, appends them seamlessly into a centralized array collection model, and updates a tracking `add_item.json` file.

### 8. Class to JSON (`8-class_to_json.py`)
A structural lookup tool that unpacks the internal operational dynamic `__dict__` namespace variables of an object instance model to return clean, serializable attribute landscapes.

### 9. Student to JSON (`9-student.py`)
A tracking blueprint class defining personal descriptive metrics that returns an un-filtered object descriptor lookup map structure.

### 10. Student to JSON with filter (`10-student.py`)
An advanced data rendering student module capable of analyzing variable arguments to output an explicitly filtered attribute sub-set array.

### 11. Student to disk and reload (`11-student.py`)
A comprehensive representation data module utilizing programmatic `setattr` mappings to rewrite active instance variables from serialized JSON updates.

### 12. Pascal's Triangle (`12-pascal_triangle.py`)
An algorithmic technical logic preparation utility that iteratively builds mathematical matrix profiles for a target height bound index `n`.

