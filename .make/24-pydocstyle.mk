# See ../makefile

.PHONY: pydocstyle-which  ## show which pydocstyle is used
pydocstyle-which:
	@ which pydocstyle


.PHONY: pydocstyle ## run pydocstyle
pydocstyle: pydocstyle-which
	- pydocstyle src/
