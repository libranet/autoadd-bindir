"""
https://sethmlarson.dev/nox-pyenv-all-python-versions
https://nox-poetry.readthedocs.io/en/stable/
"""
import nox
import nox_poetry
from nox_poetry import session

# nox.options.envdir = "var/cache/nox"  # relative to noxfile.py

# An example nox task definition that runs on many supported Python versions:
# @nox.session(python=["3.10", "3.11"])
# def test(session):
#     session.install(".")
#     session.install("-rdev-requirements.txt")
#     session.run("pytest", "tests/")


# @nox.session(venv_backend="conda", python=["3.10", "3.11"])
# def test(session):
#     session.conda_install("pytest")


# @nox.session(python=["3.10", "3.11"])
# def tests(session):
#     python_version = session.python
#     session.install("pytest")
#     session.run("pytest", "tests")

# tests.__name__ = f"tests-{python_version}"


@nox_poetry.session(python=["3.10", "3.11"])
def tests(session):
    session.install("pytest", ".")
    session.run("pytest")