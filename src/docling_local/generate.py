"""Script to convert a PDF to AI-friendly format and save to a file."""

import argparse
import os
import sys
from pathlib import Path

from docling.document_converter import DocumentConverter


def generate_document(source: str, output_path: str) -> None:
    """
    Convert a PDF document to an AI-friendly format and save to a file.

    Args:
        source: Path or URL to the PDF document.
        output_path: Path to save the converted document.
    """
    print(f"Processing document: {source}")
    converter = DocumentConverter()
    result = converter.convert(source)

    # Create output directory if it doesn't exist
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Save as markdown
    markdown_text = result.document.export_to_markdown()
    output_file.write_text(markdown_text)
    print(f"Converted document saved to: {output_file.absolute()}")
    print(f"Document size: {len(markdown_text)} characters")


def main() -> None:
    """Run the document generator from the command line."""
    parser = argparse.ArgumentParser(
        description="Convert a PDF to an AI-friendly document and save to a file."
    )
    parser.add_argument("source", help="Path or URL to the PDF document")
    parser.add_argument("output", help="Path to save the converted document")

    args = parser.parse_args()

    try:
        generate_document(args.source, args.output)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
