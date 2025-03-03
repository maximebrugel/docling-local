# docling-local

A Python project that uses Docling to convert PDFs to AI-friendly document formats.

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

## Usage

### Generate AI-friendly document from PDF

To convert a PDF to an AI-friendly document and save it to a file:

```bash
# Activate virtual environment
source .venv/bin/activate

# Using the module directly
python -m docling_local.generate https://arxiv.org/pdf/2408.09869 output/document.md

# Or using the CLI command (after installing the package)
docling-generate https://arxiv.org/pdf/2408.09869 output/document.md

# Or convert a local PDF file
docling-generate /path/to/your/document.pdf output/document.md
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