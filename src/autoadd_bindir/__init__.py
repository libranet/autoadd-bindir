"""autoadd_bindir.__init__."""
__version__ = "1.0.6a0"
__copyright__ = "Copyright 2023 Libranet."
__license__ = "MIT License"

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
    """Return the bindir from the isolated virtual environment."""
    bin_dir = pl.Path(sys.prefix) / "bin"
    return bin_dir
