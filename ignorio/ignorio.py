"""Manage .gitignore with Ignorio."""
from requests import get as rget


class Ignorio():
    """Ignorio handles API requests from gitignore.io.

    supported_languages():
        Return a list of supported languages.

    count_languages():
        Return a Integer of the number of languages supported.

    is_lang_supported(lang):
        Return True or False if a language is supported.

    get_language_exclusion(langs):
        Return a list with the exclusions templates.

    write_gitignore():
        Writes a template to the disk with the exlusion languages.
    """

    @staticmethod
    def supported_languages():
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
        """Get languages exclusion list.

        languages must be in format 'lang1,lang2,lang3' for the API to work.
        """
        # if language is not supported, raise a Value error.
        for lang in langs:
            if not self.is_lang_supported(lang):
                raise ValueError(lang)

        lang_list = ','.join(langs)
        exclusion_list = rget(f'https://www.gitignore.io/api/{lang_list}').text
        return exclusion_list

    def write_gitignore(self, langs, filename='.gitignore', append=False):
        """Write .gitignore."""
        mode = 'w'
        if append:
            mode = 'a'
        lang_list = self.get_language_exclusion(langs)
        with open(filename, mode) as raw:
            raw.write(lang_list)
