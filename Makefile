.PHONY: freeze freeze-upgrade freeze-dev freeze-dev-upgrade install-pip-tools artifactory-login

STRATA_NAME := "replace-me-strata-name"
ACCOUNT_ID  := $(shell aws sts get-caller-identity --query 'Account' --output text)
PWD         := $(shell pwd)

artifactory-login:
	artifactory-cli-login pip -o pip.conf -f
	artifactory-cli-login npm -f
	cp ~/.npmrc .

upgrade-pip:
	pip install --upgrade pip

install-pip-tools: upgrade-pip
	python -m pip install "pip-tools>=6.0.0"

install: upgrade-pip requirements.txt
	pip install -r requirements.txt --compile

install-dev: upgrade-pip requirements-dev.txt requirements.txt
	pip install -r requirements.txt --compile
	pip install -r requirements-dev.txt --compile

lint:
	isort --profile black --line-width 120 replace-me/ tests/ app.py
	black -t py311 -l 120 replace-me/ tests/ app.py --diff --check
	flake8 replace-me/ tests/ app.py

unit:
	python -m pytest -rP

test: lint unit

freeze: upgrade-pip install-pip-tools pyproject.toml
	python -m piptools compile pyproject.toml --output-file requirements.txt --no-emit-index-url --resolver backtracking
	npm install --package-lock-only

freeze-dev: upgrade-pip install-pip-tools pyproject.toml
	python -m piptools compile pyproject.toml --extra dev --output-file requirements-dev.txt --no-emit-index-url --resolver backtracking

freeze-upgrade: upgrade-pip install-pip-tools pyproject.toml
	python -m piptools compile pyproject.toml --output-file requirements.txt --no-emit-index-url --resolver backtracking --upgrade

freeze-dev-upgrade: upgrade-pip install-pip-tools pyproject.toml
	python -m piptools compile pyproject.toml --extra dev --output-file requirements-dev.txt --no-emit-index-url --resolver backtracking --upgrade

build:
	docker build . \
		-t $(STRATA_NAME) \
		--build-arg ENV=local

DOCKER_OPTS_CI_TEST := \
	-v $(PWD)/slingshot:/usr/local/skyscanner/app/<replace-me-folder-name> \
	-v $(PWD)/app.py:/usr/local/skyscanner/app/app.py \
	-v $(PWD)/local_config.yml:/usr/local/skyscanner/app/local_config.yml \
	-v $(PWD)/tests:/usr/local/skyscanner/app/tests \
	-e CONFIG_OVERRIDE=local_config.yml \
	-e ACCOUNT_ID=$(ACCOUNT_ID) \
	-e AWS_EXECUTION_ENV=Strata \
	-e STRATA_COMMIT="commit_id" \
	-e STRATA_COMMIT_TIME="commit_time" \
	-e STRATA_REPO=$(STRATA_NAME) \
	--rm

test-ci:
	docker run \
		$(DOCKER_OPTS_CI_TEST) \
		$(STRATA_NAME):latest \
		bash -c "make install-dev && make test"

docker-update-snapshots:
	docker run \
		$(DOCKER_OPTS_CI_TEST) \
		$(STRATA_NAME):latest \
		python -m pytest -rP --snapshot-update

DOCKER_OPTS_LOCAL := \
	-v $(PWD)/slingshot:/usr/local/skyscanner/app/<replace-me-folder-name> \
	-v $(PWD)/app.py:/usr/local/skyscanner/app/app.py \
	-v $(PWD)/local_config.yml:/usr/local/skyscanner/app/local_config.yml \
	-v $(PWD)/cdk.out:/usr/local/skyscanner/app/cdk.out \
	-v $(PWD)/tests:/usr/local/skyscanner/app/tests \
	-e CONFIG_OVERRIDE=local_config.yml \
	-e ACCOUNT_ID=$(ACCOUNT_ID) \
	-e AWS_EXECUTION_ENV=Strata \
	-e STRATA_COMMIT="commit_id" \
	-e STRATA_COMMIT_TIME="commit_time" \
	-e STRATA_REPO=$(STRATA_NAME) \
	-v ~/.aws/admin_saml2aws_credentials:/home/skyscanner/.aws/credentials:ro \
	-e AWS_PROFILE=${AWS_PROFILE} \
	--rm

clean-cdk-out:
	rm -rf cdk.out

shell: clean-cdk-out
	docker run -it \
		$(DOCKER_OPTS_LOCAL) \
		${STRATA_NAME}:latest \
		bash

synth-local: clean-cdk-out
	docker run \
		$(DOCKER_OPTS_LOCAL) \
		${STRATA_NAME}:latest \
		cdk synth

diff-local: clean-cdk-out
	docker run \
		$(DOCKER_OPTS_LOCAL) \
		${STRATA_NAME}:latest \
		cdk diff

deploy-local: clean-cdk-out
	docker run \
		$(DOCKER_OPTS_LOCAL) \
		${STRATA_NAME}:latest \
		cdk deploy
