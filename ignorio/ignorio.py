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
        raw_list = rget('https://www.gitignore.io/api/list').text

        # gitignore.io's API returns a multiline string
        # I have to remove new lines and split the languages.
        striped_list = raw_list.strip('\n')
        replaced_list = striped_list.replace('\n', ',')
        lang_list = replaced_list.split(',')

        return lang_list

    def count_languages(self):
        """Return how many languages are supported."""
        return len(self.supported_languages())

    def is_lang_supported(self, lang):
        """Return True or False if a language is supported."""
        lang_list = self.supported_languages()
        return True if lang in lang_list else False

    def get_language_exclusion(self, langs):
        """Get languages exclusion list."""
        lang_list = ','.join(langs)
        exclusion_list = rget(f'https://www.gitignore.io/api/{lang_list}').text
        return exclusion_list

    def write_gitignore(self, langs, filename='.gitignore'):
        """Write .gitignore."""
        lang_list = self.get_language_exclusion(langs)
        with open(filename, 'w') as raw:
            raw.write(lang_list)
