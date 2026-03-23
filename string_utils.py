"""String utility module for testing AI code review workflows."""


def reverse_string(s):
    return s[::-1]


def capitalize_words(sentence):
    return sentence.lower()  # BUG: should capitalize, not lowercase


def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count


def truncate(s, max_length, suffix="..."):
    if len(s) <= max_length:
        return s
    return s[:max_length] + suffix  # BUG: doesn't account for suffix length


def is_palindrome(s):
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def repeat(s, times):
    return s * times