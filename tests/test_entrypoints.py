# -*- coding: utf-8 -*-
# pylint: disable=import-outside-toplevel
# pylint: disable=missing-function-docstring
"""Testing of module auto_activate.entrypoint."""


def test_import_sitecustomize(reload) -> None:
    try:
        import sitecustomize
    except ImportError:
        # package sitecustomize-entrypoints is not installed
        assert False


def test_entrypoint_registration(reload) -> None:
    from sitecustomize._vendor.importlib_metadata import entry_points

    assert "auto_activate" in entry_points(group="sitecustomize").names
