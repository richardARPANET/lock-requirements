import pytest
import vcr

from lock.lock import _get_latest_versions, _lock_requirements

PYPI_SIMPLE_ENDPOINT = 'https://pypi.org/simple/'


@pytest.mark.vcr
def test_lock_requirements(tmpdir):
    input_file = 'src/tests/example-requirements.txt'
    output_file = str(tmpdir.join('out.txt'))

    output_file = _lock_requirements(
        input_path=input_file, output_path=output_file,
        endpoint=PYPI_SIMPLE_ENDPOINT,
    )

    with open(output_file, 'r') as file_:
        data = file_.readlines()
    assert data == [
        '-r ../../requirements.txt\n',
        'requests==2.21.0\n',
        '-e git://github.com/mozilla/elasticutils.git#egg=elasticutils\n',
        'imdbpie==5.6.3\n',
        'celery[s3,sqs]==4.2.1\n',
    ]


@pytest.mark.parametrize('package_name, expected_result', [
    ('requests', ('requests', '2.21.0')),
    ('imdbpie', ('imdbpie', '5.6.3')),
    ('package-which-is-not-found', ('package-which-is-not-found', None)),
])
def test_get_latest_versions(package_name, expected_result):
    with vcr.use_cassette(
        'src/tests/cassettes/'
        f'test_get_latest_versions_{package_name}.yaml'
    ):
        output = _get_latest_versions(
            package_name=package_name,
            endpoint=PYPI_SIMPLE_ENDPOINT,
        )

    assert output == expected_result
