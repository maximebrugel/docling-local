# docling-local

A Python project

## Installation

```bash
# Create virtual environment
uv venv

# Activate virtual environment
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate     # Windows

# Install dependencies
uv pip install -e ".[dev]"
```

## Development

```bash
# Run tests
pytest

# Format code
black .

# Lint code
ruff check .

# Type check
mypy src
```