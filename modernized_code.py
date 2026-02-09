```python
def calculate(x: int, y: int) -> int:
    """Multiply x and y, returning the result."""
    print(f"Calculating results for: {x}, {y}")
    res = x * y
    if res > 100:
        print(f"Result is large: {res}")
    return res

def greet(name: str) -> None:
    """Print a greeting message for the given name."""
    print(f"Hello, {name}")

# Example usage:
if __name__ == "__main__":
    result = calculate(10, 15)
    print(f"Result of calculation: {result}")
    greet("John")
```