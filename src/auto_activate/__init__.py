"""auto_activate.__init__."""
__version__ = "1.0"
__copyright__ = "Copyright 2023 Libranet - MIT License."
import os
import pathlib as pl
import sys



def entrypoint() -> None:
    """Add python-bindir to PATH."""

    bin_dir = pl.Path(sys.prefix) / "bin"
    # bin_dir = pl.Path(sys.base_prefix) / "bin"

    if not bin_dir.exists():  # pragma: no cover
        return

    paths = os.environ["PATH"].split(os.pathsep)
    paths.insert(0, str(bin_dir))  # prepend our dir
    os.environ["PATH"] = os.pathsep.join(paths)

def cancel() -> None:  # pragma: no cover
    """No-op function that can be used the cancel a registered entrypoint.

    Imagine you have multiple sitecustomize-entrypoints. If these entrypoints
    are registered via third-party packages, you cannot control the order of execution.

    Now suppose some of these entrypoints need an environment-variable that first need to be set
    by ``auto_activate`` needs to be executed before the others

    entrypoint 1:  foo.needs_envvar:bar
    entrypoint 2:  auto_activate.entrypoint:auto_activate

    in your project's pyproject.toml:

    [tool.poetry.plugins."sitecustomize"]

    # cancel the first registration using the original name
    auto_activate = "auto_activate.entrypoint:cancel"

    # re-register the same function under different name
    zz_auto_activate = "auto_activate.entrypoint:auto_activate"

    """
    pass