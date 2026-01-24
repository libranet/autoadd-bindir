# See ../makefile


# show which sphinx-build is used
[group: 'sphinx']
sphinx-build-which:
	@ uv run which sphinx-build


# generate sphinx-docs in var/html-docs
[group: 'sphinx']
sphinx-docs:
	uv run sphinx-build -b html -d var/cache/sphinx -w var/log/sphinx-build.log docs var/html-docs
	@echo
	@echo "Build finished."


# alias for sphinx-docs
alias docs := sphinx-docs
