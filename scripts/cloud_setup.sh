#!/bin/bash
# SessionStart hook: install this repo as the `compneuro` package in cloud sessions.
# Runs on every session start and resume; does nothing locally or when already installed.

if [ "$CLAUDE_CODE_REMOTE" != "true" ]; then
  exit 0
fi

cd "${CLAUDE_PROJECT_DIR:-$(dirname "$0")/..}" || exit 0

if python3 -c "import compneuro, pytest, scipy" 2>/dev/null; then
  echo "compneuro already installed. Run tests with: pytest -rs"
  exit 0
fi

pip install --quiet -e ".[dev]" 2>/dev/null \
  || pip install --quiet --break-system-packages -e ".[dev]" 2>/dev/null \
  || { echo "cloud_setup: pip install failed; check the environment's network access"; exit 0; }

echo "compneuro installed in editable mode. Run tests with: pytest -rs"
echo "Optional extras when a phase needs them: pip install brian2 nibabel nilearn neuron"
exit 0
