# ADS-in-Python

Algorithms and Data Structures in Python programming language.

## Installation

An example of installing the package in editable mode with multiple optional dependencies:

```shell
pip install -e ".[bdd,bench,cov]"
```

Note: assuming that we are in the root directory of the project.

## References

### Algorithms

- [GitHub/TheAlgorithms/Python](https://github.com/TheAlgorithms/Python)

- The Recursive Book of Recursion - Al Sweigart
- Classic Computer Science Problems in Python - David Kopec
- Algorithms and Data Structures in Python - Michael T. Goodrich, Robert Tamassia, Michael H. Goldwasser

### Python packaging

- [How to build a pyproject.toml file](https://dev.to/2320sharon/how-to-build-a-pyprojecttoml-file-4mk8)
- [Setuptools pyptoject.toml configuration](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html)
- [Declaring project metadata](https://packaging.python.org/en/latest/specifications/declaring-project-metadata/)

### Python QA

- Testing:

  - [Pytest](https://docs.pytest.org/en/latest/) is a powerful test framework with numerous plug-ins:

    - [pytest-bdd](https://pytest-bdd.readthedocs.io/en/stable/)
    - [pytest-benchmark](https://pytest-benchmark.readthedocs.io/en/latest/index.html)
    - [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) - coverage reports

- Code style:

  - [Black](https://black.readthedocs.io/en/stable/index.html) - Python code formatter
