#!/usr/bin/env bash

# Use Default Value. If 'parameter' is unset or null, 'word' (which may be an
# expansion) is substituted. Otherwise, the value of 'parameter' is
# substituted.
# Syntax: ${parameter:-word}

echo "One for ${1:-you}, one for me."
