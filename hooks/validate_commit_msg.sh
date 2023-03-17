#!/bin/bash

ARGS=$1
COMMIT_MSG=$(head -n1 "$ARGS") # Get the first line of a multiline commit msg
PATTERN="^(\[dependabot\]|[A-Z][A-Z0-9]+-[0-9]+): .*" # Format of 'JIRA1-123: ...'

if ! [[ "$COMMIT_MSG" =~ $PATTERN ]]; then
    cat "$COMMIT_MSG"
    echo "Your commit message must follow the format of 'JIRA-123: ' Did you forget to add your jira?"
    echo
    echo "Please follow this format so Jira can auto detect what is in each release."
    echo "The regex is '$PATTERN'"
    exit 1
fi
