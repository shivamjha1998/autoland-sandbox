"""Simple math utility module for testing AI code review workflows."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def average(numbers):
    if not numbers:
        raise ValueError("Cannot average an empty list")
    return sum(numbers) / len(numbers)


def factorial(n):
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0:
        return 1
    return n * factorial(n - 1)


def is_even(n):
    return n % 2 == 0


def clamp(value, minimum, maximum):
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value

def power(base, exp):
    return base ** exp
