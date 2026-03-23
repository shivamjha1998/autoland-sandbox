#!/usr/bin/env bash
# Phase 2: Happy Path — Create a PR with an obvious bug for CodeRabbit to catch.
# After CodeRabbit reviews, run `autoland` to see the autonomous fix-merge loop.

set -euo pipefail

BRANCH="feature/basic-math"

echo "=== Phase 2: Happy Path ==="
echo "Creating branch: $BRANCH"

git checkout main
git checkout -b "$BRANCH"

# Introduce a clear, fixable bug
cat > math_utils.py << 'PYTHON'
"""Simple math utility module for testing AI code review workflows."""


def add(a, b):
    return a - b  # BUG: should be a + b


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
PYTHON

git add math_utils.py
git commit -m "feat: add math utilities (has a bug in add function)"
git push -u origin "$BRANCH"

echo ""
echo "Now creating the PR..."
gh pr create \
  --title "feat: add math utilities" \
  --body "Adding basic math utility functions. Please review for correctness." \
  --base main

echo ""
echo "=== Phase 2 Ready ==="
echo "1. Wait ~2 min for CodeRabbit to review the PR"
echo "2. Then run: autoland --agent claude"
echo "3. Watch the autonomous loop: CodeRabbit review -> autoland fix -> CI check -> merge"