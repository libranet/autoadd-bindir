# -*- coding: utf-8 -*-
# pylint: disable=import-outside-toplevel
# pylint: disable=missing-function-docstring
"""Testing of module autoadd_bindir.__init__."""
import packaging.version


def test_version() -> None:
    from autoadd_bindir import __version__

    assert isinstance(__version__, str)
    assert packaging.version.parse(__version__) >= packaging.version.parse("0.0")


def test_copyright() -> None:
    from autoadd_bindir import __copyright__

    assert isinstance(__copyright__, str)
    assert "Copyright" in __copyright__
