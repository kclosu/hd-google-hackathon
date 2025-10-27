"""Agent entrypoint for metrics_insight_agent.

This file may be executed by tools (for example `adk web`) from the
project root or another working directory. Ensure the repository root
and the repository `src/` directory are on sys.path so imports like
`mock_data.dealers` resolve whether the process is started from the
project root or from inside `src/...`.
"""

import sys
from pathlib import Path

# Try to detect the repository root (look for pyproject.toml, .git, or the
# top-level `mock_data` package). Walk up at most 6 directories from this
# file's location.
_here = Path(__file__).resolve()
_root = _here
for _ in range(6):
    if (_root / "pyproject.toml").exists() or (_root / ".git").exists() or (_root / "mock_data").exists():
        break
    if _root.parent == _root:
        break
    _root = _root.parent

repo_root = _root
src_dir = repo_root / "src"

for _p in (str(repo_root), str(src_dir)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from google.adk.agents import Agent
from mock_data.dealers import Dealer, dealers

# instantiate a new dealer
d = Dealer(id="dealer_4", name="Window World", region="USA")
print(d)  # Dealer(id='dealer_4', name='Window World', region='USA')

# use the provided list
for dealer in dealers:
    print(dealer.id, dealer.name, dealer.region)

def synthesize_kpis() -> dict:
    """Synthesizes operational KPIs from various data sources."""
    # Placeholder implementation
    return {"status": "success", "kpis": {"avg_resolution_time": "24h"}}

def surface_systemic_issues() -> dict:
    """Surfaces systemic issues based on the analysis of operational data."""
    # Placeholder implementation
    return {"status": "success", "issues": ["Recurring part shortages for product X"]}

def provide_insights() -> dict:
    """Provides data-driven insights to support business decisions."""
    # Placeholder implementation
    return {"status": "success", "insights": ["Dealer training for product Y needs improvement."]}

def print_dealer() -> dict:
    """Prints dealer information."""
    # Placeholder implementation
    return {"status": "success", "dealer": str(d)}


root_agent = Agent(
    model='gemini-2.5-flash',
    name="metrics_insight_agent",
    description="Synthesizes operational KPIs, surfacing systemic issues (e.g., recurring part shortages or dealer training gaps).",
    tools=[
        synthesize_kpis,
        surface_systemic_issues,
        provide_insights,
    ],
)