"""Tests for the generate script."""

import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

from docling_local.generate import generate_document


class TestGenerate(unittest.TestCase):
    """Test the generate document functionality."""

    @patch("docling_local.generate.DocumentConverter")
    def test_generate_document(self, mock_converter_class):
        """Test generating and saving a document."""
        # Setup mocks
        mock_converter = MagicMock()
        mock_converter_class.return_value = mock_converter

        mock_result = MagicMock()
        mock_document = MagicMock()
        mock_document.export_to_markdown.return_value = "# Test Document Content"
        mock_result.document = mock_document
        mock_converter.convert.return_value = mock_result

        # Create a temporary path
        test_output = Path("test_output.md")

        try:
            # Call the function
            generate_document("test.pdf", str(test_output))

            # Verify the file was created with correct content
            self.assertTrue(test_output.exists())
            content = test_output.read_text()
            self.assertEqual(content, "# Test Document Content")

            # Verify the converter was called correctly
            mock_converter.convert.assert_called_once_with("test.pdf")

        finally:
            # Clean up
            if test_output.exists():
                test_output.unlink()


if __name__ == "__main__":
    unittest.main()
