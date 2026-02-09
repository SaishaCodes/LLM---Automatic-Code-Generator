```python
# tests/test_calculate.py

import pytest
from unittest.mock import patch
from io import StringIO
from your_module import calculate, greet  # Replace 'your_module' with the actual module name

def test_calculate_small_result():
    """Test calculate function with small result."""
    result = calculate(2, 3)
    assert result == 6

def test_calculate_large_result():
    """Test calculate function with large result."""
    result = calculate(20, 15)
    assert result == 300

def test_calculate_zero_result():
    """Test calculate function with zero result."""
    result = calculate(0, 10)
    assert result == 0

def test_calculate_negative_result():
    """Test calculate function with negative result."""
    result = calculate(-2, 3)
    assert result == -6

def test_greet():
    """Test greet function."""
    with patch('sys.stdout', new=StringIO()) as fake_stdout:
        greet("John")
        assert fake_stdout.getvalue() == "Hello, John\n"

def test_calculate_prints_result():
    """Test calculate function prints result."""
    with patch('sys.stdout', new=StringIO()) as fake_stdout:
        calculate(10, 15)
        assert "Calculating results for: 10, 15" in fake_stdout.getvalue()

def test_calculate_prints_large_result():
    """Test calculate function prints large result."""
    with patch('sys.stdout', new=StringIO()) as fake_stdout:
        calculate(20, 15)
        assert "Result is large: 300" in fake_stdout.getvalue()

def test_calculate_does_not_print_large_result_for_small_result():
    """Test calculate function does not print large result for small result."""
    with patch('sys.stdout', new=StringIO()) as fake_stdout:
        calculate(2, 3)
        assert "Result is large: " not in fake_stdout.getvalue()
```