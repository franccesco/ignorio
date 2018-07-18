"""Test ignorio package with pytest."""

from ignorio import __version__
from ignorio import Ignorio


# Initialize Ignorio class
ig = Ignorio()


def test_version():
    """Test correct version number."""
    assert __version__ == '0.1.0'


def test_language_list():
    """Test if supported_languages() returns a list."""
    supported_languages = ig.supported_languages()
    assert isinstance(supported_languages, list)


def test_supported_languages_count():
    """Test how many languages are supported."""
    assert isinstance(ig.count_languages(), int)


def test_if_language_is_supported():
    """Test if is_lang_supported() returns true or false."""
    assert ig.is_lang_supported('python') is True
    assert ig.is_lang_supported('42') is False
