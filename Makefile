.PHONY: help generate clean test lint

# Colors for prettier output
YELLOW = \033[1;33m
RESET = \033[0m

help:
	@echo "${YELLOW}Available commands:${RESET}"
	@echo "  make generate input_path=path/to/file.pdf output_path=path/to/output.md - Convert PDF to AI-friendly document"
	@echo "  make test                                                               - Run all tests"
	@echo "  make lint                                                               - Run linter and type checking"
	@echo "  make clean                                                              - Clean temporary files"

# Convert PDF to AI-friendly document
generate:
	@if [ -z "$(input_path)" ]; then \
		echo "${YELLOW}Error: input_path is required${RESET}"; \
		echo "Usage: make generate input_path=path/to/file.pdf output_path=path/to/output.md"; \
		exit 1; \
	fi
	@if [ -z "$(output_path)" ]; then \
		echo "${YELLOW}Error: output_path is required${RESET}"; \
		echo "Usage: make generate input_path=path/to/file.pdf output_path=path/to/output.md"; \
		exit 1; \
	fi
	@echo "${YELLOW}Converting ${input_path} to ${output_path}...${RESET}"
	@source .venv/bin/activate && python -m docling_local.generate "$(input_path)" "$(output_path)"
	@echo "${YELLOW}Conversion completed successfully.${RESET}"

# Run tests
test:
	@echo "${YELLOW}Running tests...${RESET}"
	@source .venv/bin/activate && pytest -v

# Run linter and type checking
lint:
	@echo "${YELLOW}Running linter and type checking...${RESET}"
	@source .venv/bin/activate && black --check .
	@source .venv/bin/activate && ruff check .
	@source .venv/bin/activate && mypy src

# Clean temporary files
clean:
	@echo "${YELLOW}Cleaning temporary files...${RESET}"
	@find . -name "__pycache__" -type d -exec rm -rf {} +
	@find . -name "*.pyc" -delete
	@find . -name "*.pyo" -delete
	@find . -name "*.pyd" -delete
	@find . -name ".pytest_cache" -type d -exec rm -rf {} +
	@find . -name ".coverage" -delete
	@find . -name "htmlcov" -type d -exec rm -rf {} +
	@echo "${YELLOW}Cleaning completed.${RESET}"