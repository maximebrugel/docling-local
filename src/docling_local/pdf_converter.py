"""PDF to AI-friendly document converter."""

import argparse
import sys
from pathlib import Path
from typing import Optional, Union

from docling.document_converter import DocumentConverter


def convert_pdf(source: Union[str, Path], output_file: Optional[Path] = None) -> str:
    """
    Convert a PDF document to an AI-friendly format.

    Args:
        source: Path or URL to the PDF document.
        output_file: Optional path to save the converted document.

    Returns:
        The converted document as markdown text.
    """
    converter = DocumentConverter()
    result = converter.convert(str(source))
    markdown_text = result.document.export_to_markdown()

    if output_file:
        output_file.write_text(markdown_text)
        print(f"Converted document saved to {output_file}")

    return markdown_text


def main() -> None:
    """Run the PDF converter from the command line."""
    parser = argparse.ArgumentParser(
        description="Convert a PDF to an AI-friendly document."
    )
    parser.add_argument("source", help="Path or URL to the PDF document")
    parser.add_argument(
        "-o", "--output", help="Path to save the converted document", default=None
    )
    args = parser.parse_args()

    try:
        if args.output:
            output_path = Path(args.output)
        else:
            output_path = None

        markdown = convert_pdf(args.source, output_path)

        if not args.output:
            print(markdown)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
