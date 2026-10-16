"""pytest path fixture — makes navig_sdk importable without installation."""
from __future__ import annotations

import sys
from pathlib import Path

# Add sdk/python/ to sys.path so `import navig_sdk` works during `pytest`
# regardless of where pytest is invoked from (repo root or sdk/python/).
_SDK_PYTHON = Path(__file__).parent.parent  # .../sdk/python/
if str(_SDK_PYTHON) not in sys.path:
    sys.path.insert(0, str(_SDK_PYTHON))
