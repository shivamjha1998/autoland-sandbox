"""Tests for math_utils module."""

import pytest
from math_utils import add, subtract, multiply, divide, average, factorial, is_even, clamp


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 100) == 0
    assert multiply(-2, 3) == -6


def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


def test_average():
    assert average([1, 2, 3]) == 2.0
    assert average([10]) == 10.0


def test_average_empty():
    with pytest.raises((ZeroDivisionError, ValueError)):
        average([])


def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120


def test_is_even():
    assert is_even(4) is True
    assert is_even(3) is False


def test_clamp():
    assert clamp(5, 0, 10) == 5
    assert clamp(-5, 0, 10) == 0
    assert clamp(15, 0, 10) == 10