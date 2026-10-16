#!/usr/bin/env bash
# setup-links.sh — create root links into .navig/ (run once after cloning this space).
# Mirrors what `navig space init` does automatically:
#   ./plans -> .navig/plans   |   ./.inbox -> .navig/inbox

set -e
cd "$(dirname "${BASH_SOURCE[0]}")"

link() {
  if [ -e "$1" ] || [ -L "$1" ]; then
    echo "  skip  $1 (exists)"
  else
    ln -s "$2" "$1"
    echo "  ok    $1 -> $2"
  fi
}

echo "Creating root links..."
link "plans"  ".navig/plans"
link ".inbox" ".navig/inbox"
echo "Done."
