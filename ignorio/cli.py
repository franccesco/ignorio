"""Command Line Interface for Ignorio."""
import os
import click
from ignorio import Ignorio

IG = Ignorio()


@click.command()
@click.argument('lang', nargs=-1)
@click.option('-l', '--langs', help='List supported languages', is_flag=True)
@click.option('-o', '--output', help='Set destination', default='.gitignore',
              metavar='OUTPUT')
@click.option('-a', '--append', help='Append instead of rewrite', is_flag=True)
@click.option('-v', '--verbose', help='Verbose mode', is_flag=True)
def main(lang, output, append, verbose, langs):
    """Download a version control exclusion list from gitignore.io."""
    if langs:
        # count total languages supported by gitignore.io
        lang_count = IG.count_languages()
        lang_count = click.style(str(lang_count), fg='green', bold=True)
        print(f'{lang_count} supported languages:')

        # display each language
        supported_langs = IG.supported_languages()
        rocket = click.style('➜', fg='green')
        for supported_lang in supported_langs:
            print(rocket, supported_lang)
        exit()

    # if no language was given then complain, else, write report.
    if not lang:
        click.secho('Type a list of languages please.', bold=True, fg='yellow')
        exit()
    try:
        IG.write_gitignore(lang, output, append)
    except ValueError as lang_error:
        faulty_lang = lang_error.args[0]
        err_msg = click.style(f'Language not supported:', bold=True, fg='red')
        print(err_msg, faulty_lang)
    else:
        if verbose:
            # languages written
            print('Languages:', end='\t')
            languages = ', '.join(lang)
            click.secho(languages, fg='green', bold=True)

            # Output report
            abs_path = os.path.abspath(output)
            print('Output:', end='\t\t')
            click.secho(abs_path, fg='green', bold=True)

            # writting mode
            print('Write Mode:', end='\t')
            if append:
                mode = 'append'
                color = 'green'
            else:
                mode = 'overwrite'
                color = 'yellow'
            click.secho(mode, fg=color, bold=True)
        else:
            success_msg = 'Exclusions written successfully.'
            click.secho(success_msg, bold=True, fg='green')


if __name__ == '__main__':
    main()
