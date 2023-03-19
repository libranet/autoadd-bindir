.. image:: https://img.shields.io/badge/license-MIT-blue.svg

:target: https://github.com/libranet/auto-activate/blob/main/docs/license.md
:alt: License: MIT

.. image:: https://readthedocs.org/projects/auto-activate/badge/?version=latest

:target: https://auto-activate.readthedocs.io/en/latest/
:alt: Read the Docs

Overview
--------


Dependencies
 - sitecustomize-entrypoints_

.. _sitecustomize-entrypoints:  http://pypi.python.org/pypi/sitecustomize-entrypoints

Installation
------------

Install via pip:

.. code-block:: python

        > pip install autoadd_bindir

Or add to your poetry-based project:

.. code-block:: python

        > poetry add autoadd_bindir


Registered sitecustomize-entrypoint
------------------------------------

The ``autoadd_bindir``-function is registered
as a ``sitecustomize``-entrypoint in pyproject.toml_:

.. code-block:: python

    [tool.poetry.plugins]
    [tool.poetry.plugins."sitecustomize"]
    autoadd_bindir = "autoadd_bindir.entrypoint:autoadd_bindir"

This entrypoint will be executed in every python-process.

.. _pyproject.toml: https://python-poetry.org/docs/pyproject/#plugins

Usage
-----

