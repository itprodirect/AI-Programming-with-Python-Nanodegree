# Contributing

Thank you for considering contributing to this project!

## Proposing changes

1. Fork the repository and create a topic branch from `main`.
2. Make your changes with clear, descriptive commits.
3. Ensure the test suite and linter pass locally (see below).
4. Open a pull request targeting `main` and describe the purpose of your changes.

## Coding standards

- Follow [PEP 8](https://pep8.org/) guidelines.
- The project is linted with [flake8](https://flake8.pycqa.org/). Run it before submitting.
- Use 4 spaces per indentation level and limit lines to 79 characters where possible.

## Running tests locally

After installing the dependencies, install the test tools and execute the linters and unit tests:

```bash
pip install -r requirements.txt
pip install pytest flake8
flake8 .
pytest
```

The linter reads its configuration from `.flake8`, which sets `max-line-length`
to `120` and excludes `print_functions_for_lab_checks.py`.

Your pull request should pass both flake8 and pytest without errors.
