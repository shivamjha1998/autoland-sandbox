"""Simple math utility module for testing AI code review workflows."""


def add(a, b):
    return a - b  # BUG: should be a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b  # BUG: no zero-division guard


def average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)  # BUG: crashes on empty list


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)  # BUG: no negative input guard


def is_even(n):
    return n % 2 == 0


def clamp(value, minimum, maximum):
    if value < minimum:
        return minimum
    if value > maximum:
        return minimum  # BUG: should return maximum
    return value