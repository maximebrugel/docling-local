"""Tests for PDF converter."""

import unittest
from unittest.mock import MagicMock, patch

from docling_local.pdf_converter import convert_pdf


class TestPdfConverter(unittest.TestCase):
    """Test the PDF converter functionality."""

    @patch("docling_local.pdf_converter.DocumentConverter")
    def test_convert_pdf_basic(self, mock_converter_class):
        """Test the basic PDF conversion functionality."""
        # Setup mocks
        mock_converter = MagicMock()
        mock_converter_class.return_value = mock_converter

        mock_result = MagicMock()
        mock_document = MagicMock()
        mock_document.export_to_markdown.return_value = "# Test Document"
        mock_result.document = mock_document
        mock_converter.convert.return_value = mock_result

        # Test function
        result = convert_pdf("test.pdf")

        # Assertions
        mock_converter.convert.assert_called_once_with("test.pdf")
        self.assertEqual(result, "# Test Document")


if __name__ == "__main__":
    unittest.main()
