[![Under Development](https://img.shields.io/badge/under-development-orange.svg)](https://github.com/cezaraugusto/github-template-guidelines)

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/libranet/autoadd-bindir/blob/main/docs/license.md)

[![Read the Docs](https://readthedocs.org/projects/autoadd-bindir/badge/?version=latest)](https://autoadd-bindir.readthedocs.io/en/latest/)

[![Stable Version](https://img.shields.io/pypi/v/autoadd-bindir?label=stable)]
[PyPI Releases]

[![Python Versions](https://img.shields.io/pypi/pyversions/autoadd_bindir)][PyPI]


# Autoadd-bindir

Automatically add the bin-directory of your virtualenv to the ``PATH``-environment variable.

You no longer need to manually *activate* your virtual environment.

## How does it work?

We register the ``autoadd_bin.entrypoint()``-function to sitecustomize-module that run for every python
The function will look up ``sys.prefix`` of your python-executable and add the corresponding bin-directory
to the ``PATH``.



## Installation

Install via pip:

```bash
> bin/pip install autoadd_bindir
```

Or add to your poetry-based project:

```bash
> poetry add autoadd_bindir
```


## Validate & Usage
After installing this package there is nothing left you need to do explicitly.
We can validate the plugin works correctly b starting a python-session and checking the ``PATH``-environment-variable?

```bash
> bin/python
```

```python
>>> import os
>>> print(os.getenv("PATH"))
    "<path-to-your-virtualenv>/bin", ...
```


## Registered sitecustomize-entrypoint


The ``autoadd_bindir``-function is registered as a ``sitecustomize``-entrypoint in pyproject.toml_:

``` toml
    [tool.poetry.plugins]
    [tool.poetry.plugins."sitecustomize"]
    autoadd_bindir = "autoadd_bindir:entrypoint"
```

Sitecustomize and all its entrypoints will be executed at the start of *every* python-process.

For more information, please see [sitecustomize-entrypoints](http://pypi.python.org/pypi/sitecustomize-entrypoints)




## Dependencies

 - sitecustomize-entrypoints


