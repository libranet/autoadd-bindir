# -*- coding: utf-8 -*-
# pylint: disable=import-outside-toplevel
# pylint: disable=missing-function-docstring
"""Testing of module auto_activate."""
import os


def test_auto_activate(bin_dir) -> None:
    from auto_activate import entrypoint

    # initially already set via sitecustomize
    paths = os.getenv("PATH", "").split(os.pathsep)
    assert paths[0] == str(bin_dir)

    # clear path
    os.environ["PATH"] = os.pathsep.join(paths[1:])

    # test cleared path
    paths = os.getenv("PATH", "").split(os.pathsep)
    assert paths[0] != str(bin_dir)

    entrypoint()
    paths = os.getenv("PATH", "").split(os.pathsep)
    assert paths[0] == str(bin_dir)
