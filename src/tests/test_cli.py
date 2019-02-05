from lock.cli import main


def test_main(capsys):
    arguments = {
        '<file>':  'requirements.txt',
        '<index_url>': 'https://pypi.org/simple/'
    }

    main(arguments=arguments)

    captured = capsys.readouterr()
    assert captured.out == (
        'Done updating requirements.txt using index https://pypi.org/simple/\n'
    )


def test_main_when_file_not_found(capsys):
    arguments = {'<file>':  'not-found.txt'}

    main(arguments=arguments)

    captured = capsys.readouterr()
    assert captured.out == 'Could not find file to update: not-found.txt\n'
