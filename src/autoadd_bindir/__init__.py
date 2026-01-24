"""autoadd_bindir."""

import contextlib
import os
import pathlib as pl
import sys

from autoadd_bindir.about import (
    authors as __author__,
    license_ as __license__,
    version as __version__,
)

__all__: list[str] = [
    "__author__",
    "__license__",
    "__version__",
    "entrypoint",
    "get_bindir",
]


def entrypoint() -> None:
    """Prepend python-bindir to PATH."""
    bin_dir = get_bindir()

    if not bin_dir.exists():  # pragma: no cover
        return

    paths = os.environ["PATH"].split(os.pathsep)

    # remove if already present somewhere in PATH
    with contextlib.suppress(ValueError):
        paths.remove(str(bin_dir))

    # prepend to PATH
    paths.insert(0, str(bin_dir))
    os.environ["PATH"] = os.pathsep.join(paths)


def get_bindir() -> pl.Path:
    """Return the bindir from the isolated virtual environment."""
    return pl.Path(sys.prefix) / "bin"
