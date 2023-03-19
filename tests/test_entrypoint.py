# -*- coding: utf-8 -*-
# pylint: disable=import-outside-toplevel
# pylint: disable=missing-function-docstring
"""Testing of module autoadd_bindir."""
import os


def test_autoadd_bindir(bin_dir) -> None:
    from autoadd_bindir import entrypoint

    # initially already set via sitecustomize
    paths = os.getenv("PATH", "").split(os.pathsep)
    assert paths[0] == str(bin_dir)

    # clear path
    pos = paths.index(str(bin_dir))
    if pos == 0:
        del paths[pos]

    # breakpoint()
    os.environ["PATH"] = os.pathsep.join(paths)

    # test cleared path
    paths = os.getenv("PATH", "").split(os.pathsep)
    assert paths[0] != str(bin_dir)

    entrypoint()
    paths = os.getenv("PATH", "").split(os.pathsep)
    assert paths[0] == str(bin_dir)
