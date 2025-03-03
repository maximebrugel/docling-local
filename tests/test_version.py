"""Test version."""

from docling_local import __version__


def test_version() -> None:
    """Test version is a string."""
    assert isinstance(__version__, str)
