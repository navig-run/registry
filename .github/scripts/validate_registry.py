#!/usr/bin/env python3
"""Fast, dependency-light validation for the NAVIG community registry.

Parses every JSON and YAML file in the repo and sanity-checks the registry
indexes. No `navig` install — runs in a couple of seconds so PRs get instant
feedback before (or instead of) the heavier deep-validation job.

Exit code 0 = all good; 1 = at least one file failed to parse / a registry is
malformed. Errors are printed with the file path so contributors can fix fast.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    import yaml  # PyYAML — tiny, installed by the workflow
except ImportError:  # pragma: no cover
    print("::error::PyYAML not installed (the workflow installs it)")
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[2]
# Directories that aren't part of the live registry. `.navig` holds example-space
# internals — skill/workflow templates that embed markdown bodies (not pure YAML),
# so they're intentionally excluded from strict parsing.
SKIP = {".git", "node_modules", "_archive", ".backup", "dist", ".github", ".navig"}

errors: list[str] = []
json_count = yaml_count = 0


def _iter(suffixes: tuple[str, ...]):
    for path in ROOT.rglob("*"):
        if path.suffix.lower() not in suffixes or not path.is_file():
            continue
        if any(part in SKIP for part in path.relative_to(ROOT).parts):
            continue
        yield path


for path in _iter((".json",)):
    json_count += 1
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        errors.append(f"{path.relative_to(ROOT)}: invalid JSON - {exc}")

for path in _iter((".yaml", ".yml")):
    yaml_count += 1
    try:
        yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        errors.append(f"{path.relative_to(ROOT)}: invalid YAML - {exc}")

# ── Harbor Bay marketplace block ─────────────────────────────────────────────
# Optional per-item block. Convention: absent = free (see README, "Harbor Bay
# pricing"). When present it must be well-formed, and unsellable items
# (status planned/labs, or the `internal: true` flag) must not carry paid pricing.
PRICING_MODELS = {"free", "tier", "buy_once"}
HARBOR_TIERS = {"plus", "max", "team", "enterprise"}
MARKETPLACE_KEYS = {"pricing_model", "included_in_tier", "price_cents", "currency"}
UNSELLABLE_STATUSES = {"planned", "labs", "internal"}


def _check_marketplace(item: dict, where: str) -> None:
    mk = item.get("marketplace")
    if mk is None:
        return  # absent = free
    if not isinstance(mk, dict):
        errors.append(f"{where}: marketplace must be an object")
        return

    unknown = set(mk) - MARKETPLACE_KEYS
    if unknown:
        errors.append(f"{where}: unknown marketplace key(s): {', '.join(sorted(unknown))}")

    model = mk.get("pricing_model")
    if model not in PRICING_MODELS:
        errors.append(f"{where}: pricing_model must be one of {sorted(PRICING_MODELS)}, got {model!r}")

    if model == "buy_once":
        cents = mk.get("price_cents")
        if not isinstance(cents, int) or isinstance(cents, bool) or cents <= 0:
            errors.append(f"{where}: buy_once requires integer price_cents > 0, got {cents!r}")

    if model == "tier" and "included_in_tier" not in mk:
        errors.append(f"{where}: pricing_model 'tier' requires included_in_tier")

    if "included_in_tier" in mk and mk["included_in_tier"] not in HARBOR_TIERS:
        errors.append(
            f"{where}: included_in_tier must be one of {sorted(HARBOR_TIERS)}, got {mk['included_in_tier']!r}"
        )

    currency = mk.get("currency")
    if currency is not None and (not isinstance(currency, str) or len(currency) != 3 or not currency.islower()):
        errors.append(f"{where}: currency must be a lowercase 3-letter code, got {currency!r}")

    unsellable = item.get("status") in UNSELLABLE_STATUSES or item.get("internal") is True
    if unsellable and model in {"tier", "buy_once"}:
        errors.append(
            f"{where}: status={item.get('status')!r} internal={item.get('internal')!r} items are not "
            f"sellable and must not carry {model!r} pricing (drop the marketplace block)"
        )


# Registry indexes must be non-empty JSON (list, or dict with entries).
for reg in _iter((".json",)):
    if reg.name != "registry.json":
        continue
    try:
        data = json.loads(reg.read_text(encoding="utf-8"))
    except Exception:  # already reported above
        continue
    ok = (isinstance(data, list) and data) or (
        isinstance(data, dict) and (data.get("entries") or data.get("skills") or data.get("spaces") or data)
    )
    if not ok:
        errors.append(f"{reg.relative_to(ROOT)}: registry index is empty or has an unexpected shape")
        continue

    # Validate marketplace blocks on every item list the index carries.
    rel = reg.relative_to(ROOT)
    items = data if isinstance(data, list) else []
    if isinstance(data, dict):
        for key in ("entries", "skills", "spaces", "personas"):
            if isinstance(data.get(key), list):
                items = items + data[key]
    for item in items:
        if isinstance(item, dict):
            _check_marketplace(item, f"{rel}: item {item.get('id', '<no id>')!r}")

print(f"Parsed {json_count} JSON + {yaml_count} YAML files.")
if errors:
    print(f"\n{len(errors)} problem(s):")
    for e in errors:
        print(f"::error::{e}")
    sys.exit(1)
print("OK - registry validation passed.")
