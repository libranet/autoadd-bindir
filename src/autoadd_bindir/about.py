"""autoadd_bindir.about.

Fetch metadata from the package's pyproject.toml.
The package must be properly installed in order the metadata to be available.

"""

from __future__ import annotations  # enables X | Y syntax in annotations for Python <3.10

import importlib.metadata

PACKAGE: str = __package__ or ""


try:
    _msg = importlib.metadata.metadata(PACKAGE)
    # Materialise a plain ``dict`` so downstream ``.get(...)`` calls are typed
    # unambiguously on every supported Python: ``PackageMetadata`` only guarantees
    # ``__iter__`` (over keys) and ``__getitem__`` across versions.
    pkginfo: dict[str, str] = {key: _msg[key] for key in _msg}
except ValueError:  # pragma: no cover
    # A distribution name is required. __package__ is None.
    pkginfo = {}
except importlib.metadata.PackageNotFoundError:  # pragma: no cover
    # fallback if this package is not properly installed
    pkginfo = {}


authors: str = pkginfo.get("Author-email", "unknown")

license_: str = pkginfo.get("License-Expression") or pkginfo.get("License", "unknown") or "unknown"

version: str = pkginfo.get("Version", "unknown")
