.DEFAULT_GOAL := help
.PHONY: help
help:
	@echo "------------------------------------------------------------------------"
	@echo "BB Consent Playground"
	@echo "------------------------------------------------------------------------"
	@grep -E '^[0-9a-zA-Z_/%\-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

# You can customize the default values or override them by passing parameters
export MONGODB_IMAGE ?= zcube/bitnami-compat-mongodb:6.0.5
export POSTGRESQL_IMAGE ?= bitnami/postgresql:14.10.0
export KEYCLOAK_IMAGE ?= docker.io/bitnami/keycloak:22.0.2-debian-11-r0
export API_IMAGE ?= igrantio/bb-consent-api:2023.12.2
export CADDY_IMAGE ?= igrantio/bb-consent-caddy:2023.12.2
export FIXTURES_IMAGE ?= igrantio/bb-consent-fixtures:2023.12.2

destroy: ## Delete all containers and volumes
	@if [ -n "$$(docker container ls -aq)" ]; then \
		docker container rm -f $$(docker container ls -aq); \
	fi
	@if [ -n "$$(docker volume ls -q)" ]; then \
		docker volume rm $$(docker volume ls -q); \
	fi
	@echo "Destroyed all containers and volumes"

run: ## Run the playground
	docker-compose up nginx-proxy mongo postgresql keycloak api admin-dashboard privacy-dashboard -d

setup-test: ## Setup test environment
	cd test && ./test-entrypoint.sh

down: ## Stop the playground
	docker-compose down

clean: ## Stop and destroy volumes
	docker-compose down -v

build-test: ## Build behave image
	docker build --platform=linux/amd64 -t igrantio/bb-consent-test-runner:dev -f ./gherkin/Dockerfile ./gherkin

run-test: ## Run BDD test
	sudo rm -rf allure-results allure-report && docker run --network=test_custom_network -v ./allure-results:/tests/allure-results:rw igrantio/bb-consent-test-runner:dev

allure-generate: ## Generate Allure report
	allure generate --clean

allure-serve: ## Serve allure report in a browser
	allure serve

setup-dev: ## Setup api, admin and privacy dashboard for development branch tests
	sudo rm -rf temp && \
	mkdir temp && \
	cd temp && \
	git clone git@github.com:decentralised-dataexchange/bb-consent-api.git && \
	git clone https://github.com/decentralised-dataexchange/bb-consent-admin-dashboard && \
	git clone https://github.com/decentralised-dataexchange/bb-consent-privacy-dashboard
	
	@echo "Please enter the GPG passphrase when prompted:"
	@gpg --decrypt api-dev-tests.json.gpg > api-dev-tests.json

	cp api-dev-tests.json temp/bb-consent-api/resources/config/config-development.json
	cp admin-dashboard.json temp/bb-consent-admin-dashboard/public/config/config.json
	cp privacy-dashboard.json temp/bb-consent-privacy-dashboard/public/config/config.json

run-dev-api: destroy ## Run api for development branch tests
	make -C temp/bb-consent-api setup api/build
	./dev-keycloak-startup.sh
	make -C temp/bb-consent-api api/run

run-dev-admin-dashboard: ## Run admin dashboard for development branch tests
	make -C temp/bb-consent-admin-dashboard setup build run

run-dev-privacy-dashboard: ## Run admin dashboard for development branch tests
	make -C temp/bb-consent-privacy-dashboard setup build run

build-fixtures: ## Build fixtures docker image
	docker build --platform=linux/amd64 -t igrantio/bb-consent-fixtures:2023.12.2 -f ./fixtures/Dockerfile ./fixtures

publish-fixtures: ## Publish fixtures docker image to docker hub
	docker push igrantio/bb-consent-fixtures:2023.12.2

run-fixtures: ## Load fixtures
	docker-compose up fixtures

run-test-fixtures: ## Load fixtures in to text environment
	docker-compose -f test/test-docker-compose.yaml up fixtures

build-caddy: ## Build caddy docker image
	docker build --platform=linux/amd64 -t igrantio/bb-consent-caddy:2023.12.2 -f ./test/Dockerfile_caddy ./test

publish-caddy: ## Publish caddy docker image to docker hub
	docker push igrantio/bb-consent-caddy:2023.12.2