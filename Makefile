.DEFAULT_GOAL := help
.PHONY: help
help:
	@echo "------------------------------------------------------------------------"
	@echo "BB Consent Playground"
	@echo "------------------------------------------------------------------------"
	@grep -E '^[0-9a-zA-Z_/%\-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

destroy: ## Delete all containers and volumes
	@if [ -n "$$(docker container ls -aq)" ]; then \
		docker container rm -f $$(docker container ls -aq); \
	fi
	@if [ -n "$$(docker volume ls -q)" ]; then \
		docker volume rm $$(docker volume ls -q); \
	fi
	@echo "Destroyed all containers and volumes"

run: ## Run the playground
	docker-compose up -d

setup-test: ## Setup test environment
	./test-entrypoint.sh

down: ## Stop the playground
	docker-compose down

clean: ## Stop and destroy volumes
	docker-compose down -v

build-test: ## Build behave image
	docker build --platform=linux/amd64 -t igrantio/consent-bb-test-runner:dev -f Dockerfile .

run-test: ## Run BDD test
	docker run --network=bb-consent-playground_custom_network igrantio/consent-bb-test-runner:dev

setup-dev-tests: ## Setup api, admin and privacy dashboard for development branch tests
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

run-dev-tests-api: destroy ## Run api for development branch tests
	make -C temp/bb-consent-api setup api/build
	./dev-keycloak-startup.sh
	make -C temp/bb-consent-api api/run

run-dev-tests-admin-dashboard: ## Run admin dashboard for development branch tests
	make -C temp/bb-consent-admin-dashboard setup build run

run-dev-tests-privacy-dashboard: ## Run admin dashboard for development branch tests
	make -C temp/bb-consent-privacy-dashboard setup build run