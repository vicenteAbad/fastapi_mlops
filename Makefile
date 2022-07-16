SUPPORTED_COMMANDS := test lint format run
SUPPORTS_MAKE_ARGS := $(findstring $(firstword $(MAKECMDGOALS)), $(SUPPORTED_COMMANDS))
ifneq "$(SUPPORTS_MAKE_ARGS)" ""
  COMMAND_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  $(eval $(COMMAND_ARGS):;@:)
endif

help:
	@echo "  clean                       clean files"
	@echo "  install-dev-deps            install dev dependencies"
	@echo "  build-docker                build docker image for production"
	@echo "  test                        run the testsuite"
	@echo "  format                      format the python code"
	@echo "  check-code                  check vulnerabilities in the code"
	@echo "  check-deps                  check vulnerabilities in the packages"
	@echo "  run-dev                     run dev server (development mode)"
	@echo "  run                         run docker server (production mode)"
	@echo "  stop                        stop docker server (production mode)"

.PHONY: clean
clean:
	@echo "--> Cleaning pyc files"
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete

.PHONY: install-dev-deps
install-dev-deps:
	@echo "--> Create venv and install requirements"
	python3 -m venv venv
	source venv/bin/activate && \
	pip install --upgrade pip && \
	pip install -r requirements.txt

.PHONY: build-docker
build-docker:
	@echo "--> Building production image"
	cp env_prod app/.env
	docker-compose build

.PHONY: test
test:
	@echo "--> Running unittest"
	source venv/bin/activate && \
	cd tests && \
	python -m unittest test_service.TestStationService

.PHONY: format
format: 
	echo "--> Format the python code"
	source venv/bin/activate && \
  autoflake --remove-all-unused-imports --remove-unused-variables --recursive --in-place app/ && \
	black --line-length 100 app && \
 	isort app 

.PHONY: check-code
check-code: 
	@echo "--> Check vulnerabilities in the code"
	source ./venv/bin/activate && \
	bandit -r app/

.PHONY: check-deps
check-deps: 
	@echo "--> Check vulnerabilities in packages"
	source venv/bin/activate && \
	safety check --full-report 

.PHONY: run-dev
run-dev: 
	@echo "--> Running dev server"
	cp env_dev app/.env
	source venv/bin/activate && \
	cd app && \
	uvicorn main:app --reload --lifespan on --workers 1 --host 0.0.0.0 --port 3000 --log-level debug

.PHONY: run
run:
	@echo "--> Running server"
	docker-compose up -d

.PHONY: stop
stop:
	@echo "--> Stop server"
	docker-compose down
