# Blackbox testing a Flask App

This repository contains a minimal example of a Flask application with a testing
startegy that allows for blackbox testing.

The idea is to not use the test suite provided by Flask and spawn the app as a
separate process which can be tested via the `requests` package. This tests the
apps user facing behaviours rather than internal implementations.

## Usage

To use this repository you will need:

- Python >= 3.9

### Python environment set up 

You should create a virtual environment to use this project, you can do that and
activate it with the following steps:

```bash
cd flask_test_blackbox

# create the virtual environment
python -m venv venv

# activate the environment
. venv/bin/activate

# install dependencies (including dev dependencies)
pip install .[dev]
```

To run the app you should run the following in a terminal:

```bash
flask --app flask_blackbox run
```

To run the test suite run:

```bash
pytest
```
