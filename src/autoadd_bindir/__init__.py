"""autoadd_bindir.__init__."""
__version__ = "1.0"
__copyright__ = "Copyright 2023 Libranet - MIT License."
import os
import pathlib as pl
import sys


def entrypoint() -> None:
    """Prepend python-bindir to PATH."""

    bin_dir = get_bindir()

    if not bin_dir.exists():  # pragma: no cover
        return

    paths = os.environ["PATH"].split(os.pathsep)

    try:
        # remove if already present somewhere in PATH
        paths.remove(str(bin_dir))
    except ValueError:
        pass

    # prepend to PATH
    paths.insert(0, str(bin_dir))
    os.environ["PATH"] = os.pathsep.join(paths)


def get_bindir() -> pl.Path:
    """Return the bindit form the isolated virtual environment."""
    bin_dir = pl.Path(sys.prefix) / "bin"
    return bin_dir


def cancel() -> None:  # pragma: no cover
    """No-op function that can be used the cancel a registered entrypoint.

    Imagine you have multiple sitecustomize-entrypoints. If these entrypoints
    are registered via third-party packages, you cannot control the order of execution.

    Now suppose some of these entrypoints need an environment-variable that first need to be set
    by ``autoadd_bindir`` needs to be executed before the others

    entrypoint 1:  foo.needs_envvar:bar
    entrypoint 2:  autoadd_bindir.entrypoint:autoadd_bindir

    in your project's pyproject.toml:

    [tool.poetry.plugins."sitecustomize"]

    # cancel the first registration using the original name
    autoadd_bindir = "autoadd_bindir.entrypoint:cancel"

    # re-register the same function under different name
    zz_autoadd_bindir = "autoadd_bindir.entrypoint:autoadd_bindir"

    """
    pass  # pylint: disable=unnecessary-pass
