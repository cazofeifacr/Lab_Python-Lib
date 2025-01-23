#!/usr/bin/bash
BASE_SHA=$(git merge-base origin/main HEAD)
HEAD_SHA=$(git rev-parse HEAD)

CHANGED_PY_FILES=$(git diff --name-only --diff-filter=d "$BASE_SHA" "$HEAD_SHA" | grep '\.py$' | grep -v '/test/')
echo "Changed Python files: $CHANGED_PY_FILES"
FILE_COUNT=$(echo "$CHANGED_PY_FILES" | wc -l)
echo "PR includes $FILE_COUNT Python files."

if [ "$CHANGED_PY_FILES" -gt 5 ]; then
    echo "PR includes too many Python files (>$CHANGED_PY_FILES). Please split it into smaller PRs."
    exit 1
else
    echo "PR size is acceptable."
fi
