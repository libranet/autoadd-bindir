:py:mod:`autoadd_bindir`
========================

.. py:module:: autoadd_bindir

.. autoapi-nested-parse::

   autoadd_bindir.__init__.



Package Contents
----------------


Functions
~~~~~~~~~

.. autoapisummary::

   autoadd_bindir.entrypoint
   autoadd_bindir.get_bindir
   autoadd_bindir.cancel



Attributes
~~~~~~~~~~

.. autoapisummary::

   autoadd_bindir.__version__
   autoadd_bindir.__copyright__


.. py:data:: __version__
   :value: '1.0.2a0'

   

.. py:data:: __copyright__
   :value: 'Copyright 2023 Libranet - MIT License.'

   

.. py:function:: entrypoint()

   Prepend python-bindir to PATH.


.. py:function:: get_bindir()

   Return the bindit form the isolated virtual environment.


.. py:function:: cancel()

   No-op function that can be used the cancel a registered entrypoint.

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



