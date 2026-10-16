#!/usr/bin/env bash
# setup-links.sh — Create optional root symlinks into .navig/
set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"
create_link() {
  local name="$1"; local target="$2"
  if [ -e "$name" ] || [ -L "$name" ]; then echo "  skip  $name (already exists)"
  else ln -s "$target" "$name"; echo "  ok    $name → $target"; fi
}
echo "Creating root symlinks..."
create_link "inbox" ".navig/inbox"
create_link "docs"  ".navig/inbox/docs"
create_link "plans" ".navig/plans"
echo "Done."
