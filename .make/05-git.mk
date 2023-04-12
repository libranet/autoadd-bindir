# See ../makefile

GIT_CLONE_URL := $(shell git remote get-url --push origin)
LATEST_TAG := $(shell git fetch --tags && git describe --tags --abbrev=0)
CLONE_DIR := 'var/cache/tags/${LATEST_TAG}'

.PHONY: git-init  ## initialize  new git-repo
git-init:
	git init


.PHONY: git-remote-show-origin  ## git-remote-show-origin
git-remote-show-origin:
	git remote show origin


.PHONY: git-fetch-tags  ## git fetch --tags
git-fetch-tags:
	git fetch --tags


.PHONY: git-show-remote-tags  ## git ls-remote --tags
git-show-remote-tags:
	git ls-remote --tags


.PHONY: git-show-local-tags  ## git tag -l
git-show-local-tags: git-fetch-tags
	echo -e "Local tags"
	git tag -l


.PHONY: git-show-tags  ## show local & remote tags
git-show-tags:
	@echo -e "Local tags"
	git tag -l
	@echo -e "Remote tags"
	git ls-remote --tags

.PHONY: git-show-url  ## show clone-url
git-show-url:
	@ git remote get-url --push origin


.PHONY: git-tmp-clone  ## clone repo to tmp-dir
git-tmp-clone:
# LATEST_TAG=$(git describe --tags --abbrev=0)
	$(eval LATEST_TAG := $(git describe --tags --abbrev=0)) \
	cd ${CLONE_DIR}-${LATEST_TAG} && \
	@ git clone ${GIT_CLONE_URL} ${CLONE_DIR}


.PHONY: git-latest-tag  ## show latest tag
git-latest-tag:
	$(eval LATEST_TAG := $(git describe --tags --abbrev=0)) \
	@ echo -e "Latest tag: ${LATEST_TAG}"
	export LATEST_TAG


.PHONY: publish-to-pypi  ## publish-to-pypi
publish-to-pypi:
	@ echo -e "Creating directory ${CLONE_DIR}" && \
	mkdir -p ${CLONE_DIR} && \
	git clone ${GIT_CLONE_URL} ${CLONE_DIR}
	cd ${CLONE_DIR} && \
	echo -e "Checking out latest tags ${LATEST_TAG}" && \
	git checkout ${LATEST_TAG} && \
	echo -e "Building package v${LATEST_TAG}" && \
	poetry build && \
	poetry publish