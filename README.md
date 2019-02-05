**NOTICE**: If you're reading this on GitHub.com please be aware this is a mirror of the primary remote located at https://code.richard.do/richardARPANET/lock-requirements.
Please direct issues and pull requests there.

# lock-requirements

A CLI tool to update your requirements.txt file package versions to be locked/fixed to the latest versions available on PyPI.

#### For example

Input file contents before locking:

```
requirements-parser
pypi-simple>=0.4.0,<1.0.0
docopt>=0.5.0,<1.0.0
wheel
```

Input file contents after locking:

```
requirements-parser==0.2.0
pypi-simple==0.4.0
docopt==0.6.2
wheel==0.32.3
```

## Installation

```
pip install lock-requirements
```

## Usage

```
lock requirements.txt
lock requirements-dev.txt
```

Use a custom PyPI simple index url to retrieve latest package versions from.

```
lock requirements.txt --index-url=https://example.com/simple/
```

## Development Installation

```
pip install -r requirements-dev.txt
python setup.py develop
```

And to the run tests:

```
tox
```
