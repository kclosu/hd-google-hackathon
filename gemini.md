## Gemini Workflow Notes

Before running any Python scripts, activate the local virtual environment so the interpreter and tooling pick up project dependencies:

```powershell
.venv\Scripts\activate
```

```bash
source .venv/bin/activate
```

For a quick feedback loop, exercise changes with the existing pytest suite:

1. Run tests with `pytest` from the project root (after activation).
2. Inspect failures to understand regressions or missing coverage.
3. Adjust implementation or tests as needed.
4. Repeat `pytest` until the suite passes cleanly.

Favor a lightweight test-driven approach: sketch the test (or extend an existing one) that captures the expected behavior, watch it fail, implement the fix, and rerun until green to keep changes disciplined and observable.
