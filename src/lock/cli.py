"""
Usage: lock <file> [--index-url=<index_url>]

Locks the requirements in the given file to the latest version available.

Options:
  -h --help
"""
from docopt import docopt

from lock import lock

DEFAULT_PYPI_SIMPLE_ENDPOINT = 'https://pypi.org/simple/'


def main(arguments=None):
    arguments = arguments or docopt(__doc__)
    reqs_path = arguments['<file>']
    endpoint = arguments.get('<index_url>', DEFAULT_PYPI_SIMPLE_ENDPOINT)
    try:
        lock(requirements_path=reqs_path, endpoint=endpoint)
    except FileNotFoundError:
        print(f'Could not find file to update: {reqs_path}')
    else:
        print(f'Done updating {reqs_path} using index {endpoint}')


if __name__ == '__main__':
    main()
