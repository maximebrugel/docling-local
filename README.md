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

To convert a PDF to an AI-friendly document and save it to a file, you can use one of the following methods:

#### Using the Makefile (Recommended)

```bash
# Convert a PDF (local file or URL) to markdown
make generate input_path=input/paper_test.pdf output_path=output/paper_test.md

# Convert from a URL
make generate input_path=https://arxiv.org/pdf/2408.09869 output_path=output/document.md
```

#### Using Python directly

```bash
# Activate virtual environment
source .venv/bin/activate

# Using the module directly
python -m docling_local.generate input/paper_test.pdf output/paper_test.md

# Using a URL as input
python -m docling_local.generate https://arxiv.org/pdf/2408.09869 output/document.md
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