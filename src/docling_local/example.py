"""Example script to convert a PDF to AI-friendly format."""

from docling_local.pdf_converter import convert_pdf

# Example URL from arxiv
source = "https://arxiv.org/pdf/2408.09869"

# Convert and print the document
markdown = convert_pdf(source)
print(f"Converted document has {len(markdown)} characters")
print("First 500 characters:")
print(markdown[:500])
