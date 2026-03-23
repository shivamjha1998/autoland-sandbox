"""Tests for string_utils module."""

from string_utils import reverse_string, capitalize_words, count_vowels, truncate, is_palindrome, repeat


def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""


def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"


def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("xyz") == 0


def test_truncate():
    assert truncate("hello world", 20) == "hello world"
    assert len(truncate("hello world", 5)) <= 8  # 5 + len("...")


def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("A man a plan a canal Panama") is True


def test_repeat():
    assert repeat("ab", 3) == "ababab"