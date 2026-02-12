# Python Basics

## Control Flow Tools

### 1. Conditional Statements
Python provides various control flow tools to allow you to execute different blocks of code based on certain conditions. The main conditional statement is `if`.

**Example:**
```python
if condition:
    # code to execute if condition is true
elif another_condition:
    # code to execute if another condition is true
else:
    # code to execute if no conditions are true
```

### 2. Loops
Python supports two types of loops: `for` loops and `while` loops.

**For Loop Example:**
```python
for item in iterable:
    # code to execute for each item
```

**While Loop Example:**
```python
while condition:
    # code to execute as long as condition is true
```

## Data Structures

### 1. Lists
Lists are ordered collections that can hold mixed types of data.

**Example:**
```python
my_list = [1, 2, 3, 'Python', True]
```

### 2. Tuples
Tuples are immutable ordered collections.

**Example:**
```python
my_tuple = (1, 2, 3, 'Python', True)
```

### 3. Dictionaries
Dictionaries are unordered collections of key-value pairs.

**Example:**
```python
my_dict = {'key1': 'value1', 'key2': 'value2'}
```

### 4. Sets
Sets are unordered collections of unique elements.

**Example:**
```python
my_set = {1, 2, 3, 4}
```

## Modules

### What are Modules?
Modules are Python files containing Python code that can define functions, classes, and variables. A module allows you to logically organize your Python code.

### Importing Modules
You can import a module using the `import` statement.

**Example:**
```python
import my_module
```

### Standard Library
Python comes with a standard library that offers a wide range of modules and functions for various tasks, from math operations to file handling.

## Python Basics

- **Variables:**
    - Used to store data values.
    - Python is dynamically typed.
    - **Example:** `my_var = 42`

- **Data Types:**
    - Common data types include integers, floats, strings, and booleans.
    - **Example:** `my_number = 3.14`

- **Input and Output:**
    - You can take input from users and display output using `input()` and `print()` functions.
    - **Example:** `name = input('Enter your name: ')`

- **Functions:**
    - Blocks of reusable code.
    - Defined using the `def` keyword.
    - **Example:**
    ```python
    def my_function(param):
        return param + 1
    ```

- **Exception Handling:**
    - Allows you to handle errors gracefully using `try` and `except`.
    - **Example:**
    ```python
    try:
        # code that may raise an exception
    except SomeException:
        # handle exception
    ```