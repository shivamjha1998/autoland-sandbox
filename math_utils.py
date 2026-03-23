"""Simple math utility module for testing AI code review workflows."""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the quotient of a divided by b. Raises ZeroDivisionError if b is zero."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def average(numbers):
    """Return the arithmetic mean of a list of numbers. Raises ValueError if the list is empty."""
    if not numbers:
        raise ValueError("Cannot average an empty list")
    return sum(numbers) / len(numbers)


def factorial(n):
    """Return the factorial of n. Raises ValueError if n is negative."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0:
        return 1
    return n * factorial(n - 1)


def is_even(n):
    """Return True if n is even, False otherwise."""
    return n % 2 == 0


def clamp(value, minimum, maximum):
    """Return value clamped between minimum and maximum."""
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value
