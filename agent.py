def generate_code(task):
    if "add_numbers" in task.lower():
        return """
def add_numbers(a, b):
    return a + b
"""
    else:
        return "# No code generated for this task yet"

def generate_tests(function_name):
    if function_name == "add_numbers":
        return """
import pytest
from main import add_numbers

def test_add_numbers_positive():
    assert add_numbers(2, 3) == 5

def test_add_numbers_negative():
    assert add_numbers(-1, -1) == -2

def test_add_numbers_mixed():
    assert add_numbers(-1, 1) == 0

def test_add_numbers_invalid_input():
    with pytest.raises(TypeError):
        add_numbers("hello", 2)
"""
    else:
        return "# No tests generated for this function"

def generate_docs():
    return """
# Math Utils

This package contains utility functions for mathematical operations.

## Functions

### `add_numbers(a, b)`
Adds two numbers and returns the result.
"""