#!/usr/bin/env bash
# setup-links.sh — create optional root-level symlinks for quick access
# Run from the space root: bash setup-links.sh

set -e
SPACE_ROOT="$(cd "$(dirname "$0")" && pwd)"

create_link() {
  local target="$1"
  local link="$2"
  if [ -e "$SPACE_ROOT/$link" ]; then
    echo "  skip  $link (already exists)"
  else
    ln -s "$SPACE_ROOT/$target" "$SPACE_ROOT/$link"
    echo "  link  $link -> $target"
  fi
}

echo "Social Circle — setting up symlinks in space root..."
create_link ".navig/inbox"  "inbox"
create_link ".navig/plans"  "plans"
create_link ".navig/memory" "memory"
echo "done."
