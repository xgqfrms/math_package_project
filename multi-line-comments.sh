#!/usr/bin/env bash

echo "just use the \`EOF\` for multi-line comments in your shell script. 🚀"

<<EOF
  comment1
  comment2
  comment3
  # ...
EOF

echo "just use the \`SHELL_MULTI_LINE_COMMENTS\` for multi-line comments in your shell script. 🚀"

<<SHELL_MULTI_LINE_COMMENTS
  comment1
  comment2
  comment3
  # ...
SHELL_MULTI_LINE_COMMENTS
