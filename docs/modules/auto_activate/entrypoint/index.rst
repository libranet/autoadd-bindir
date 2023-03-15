:py:mod:`auto_activate.entrypoint`
==================================

.. py:module:: auto_activate.entrypoint

.. autoapi-nested-parse::

   auto_activate.entrypoint



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   auto_activate.entrypoint.cancel
   auto_activate.entrypoint.auto_activate



.. py:function:: cancel()

   No-op function that can be used the cancel a registered entrypoint.

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



.. py:function:: auto_activate()

   Add python-bindir to PATH.


