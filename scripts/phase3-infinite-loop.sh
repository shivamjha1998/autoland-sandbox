#!/usr/bin/env bash
# Phase 3: Infinite Loop — CI always fails. Does autoland stop or loop forever?

set -euo pipefail

BRANCH="test/infinite-loop"

echo "=== Phase 3: Infinite Loop Test ==="
echo "Creating branch: $BRANCH"

git checkout main
git checkout -b "$BRANCH"

# Create a workflow that always fails
mkdir -p .github/workflows
cat > .github/workflows/test.yml << 'YAML'
name: Tests

on:
  pull_request:
    branches: [main]
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Always fail
        run: |
          echo "This test is rigged to fail"
          exit 1
YAML

# Also add a minor code change to trigger the PR
cat >> math_utils.py << 'PYTHON'


def power(base, exp):
    return base ** exp
PYTHON

git add .
git commit -m "test: add power function (with rigged CI)"
git push -u origin "$BRANCH"

gh pr create \
  --title "test: infinite loop detection" \
  --body "Testing autoland behavior when CI always fails. Does it loop forever or give up?" \
  --base main

echo ""
echo "=== Phase 3 Ready ==="
echo "1. Wait for CodeRabbit review"
echo "2. Run: autoland --agent claude"
echo "3. WATCH CAREFULLY — monitor for infinite looping and API credit burn"
echo "4. Be ready to Ctrl+C if it doesn't stop on its own"