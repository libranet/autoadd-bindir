# Changelog

All notable changes to this project will be documented in this file.

## Unreleased (YYYY-MM-DD)

### Breaking Changes

- Officially drop python3.8 support.

### Build System

- Migrate from Poetry to uv for package management.

- Replace makefile with justfile for task running.

- Remove nox in favor of just tasks.

### CI/CD

- Modernize all GitHub workflows to use uv instead of Poetry.

- Add dependabot-auto-merge.yaml workflow for automated dependency updates.

- Remove standalone bandit.yml workflow (available via just tasks).

- Update dependabot.yml configuration for uv.lock updates.

- Pin GitHub Actions versions with commit hashes for security.

### Documentation

- Fix docs/conf.py: correct read_version path and f-string typos.

- Fix sphinx.justfile to use `uv run sphinx-build` for proper virtualenv execution.

- Update .readthedocs.yaml for uv-based builds.

### Code Quality

- Add `about.py` module for dynamic metadata extraction.

- Fix SIM105 lint issue: use `contextlib.suppress(ValueError)` instead of try-except-pass.

- Fix B904 lint issue: use `raise AssertionError from None` for proper exception chaining.

- Update pre-commit hooks configuration for uv.

## 1.0.6 (2023-04-30)

- Remove range-pinning `python = ">=3.8.0,<4.0"`, only specify bottom-range `">=3.8.0"`

- Remove rang-pinned dependencies `tox`, `nox`.

## 1.0.5 (2023-04-12)

- Remove `autoadd_bindir.cancel`-function

- Depend on `sitecustomize-entrypoints>=1.1.0`

## 1.0.4 (2023-03-29)

- Update **gh-action-pypi-publish** to **@v1.8.3**

## 1.0.3 (2023-03-29)

- Fix poetry installation in github-release-action.

- Add poetry version-pinning in github-release-action.

## 1.0.2 (2023-03-29)

- Add github-actions for [linting](https://github.com/libranet/autoadd-bindir/actions/workflows/linting.yaml) and [testing](https://github.com/libranet/autoadd-bindir/actions/workflows/testing.yaml).

- Add boilerplate-files to comply with Github's [_Community Standards_](https://github.com/libranet/autoadd-bindir/community)

- Refactored make-file.

- Fix some typo's in docstrings.

## 1.0.1 (2023-03-19)

- Test releasing via `poetry-release`.

## 1.0 (23-03-19)

- Add `readthedocs.yaml`.

- Package created by \[Wouter Vanden Hove <wouter@libranet.eu>\]
