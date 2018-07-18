"""TODO: Ignorio package description."""
from requests import get as rget


class Ignorio():
    """TODO: Ignorio class."""

    def __init__(self):
        """TODO: Ignorio initialization."""

    def supported_languages(self):
        """Get supported languages from gitignore.io.

        example:
        supported_languages()
        >>> [ruby, python, sublimetext, ...]
        """
        lang_list = rget('https://www.gitignore.io/api/list').text

        # gitignore.io's API returns a multiline string
        # I have to remove new lines and split the languages.
        lang_list = lang_list.strip('\n')
        lang_list = lang_list.replace('\n', ',')
        lang_list = lang_list.split(',')

        return lang_list

    def count_languages(self):
        """Return how many languages are supported."""
        return len(self.supported_languages())

    def is_lang_supported(self, lang):
        """Return True or False if a language is supported."""
        lang_list = self.supported_languages()
        return True if lang in lang_list else False

    def get_language(self, lang):
        """TODO: Get language exclusion list."""
        pass

    def write_gitignore(self, path='.'):
        """TODO: Write .gitignore."""
        pass
