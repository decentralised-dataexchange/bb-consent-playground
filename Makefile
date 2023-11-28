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

run-test: ## Run the playground
	docker-compose up nginx-proxy mongo postgresql keycloak api -d

down: ## Stop the playground
	docker-compose down

clean: ## Stop and destroy volumes
	docker-compose down -v