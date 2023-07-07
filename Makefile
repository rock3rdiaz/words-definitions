.PHONY:
init: down volume up

help: Makefile
	@sed -n 's/^##//p' $< | cat

## down		| Stop the application
down:
	docker compose -f docker-compose.yml down 

## volume		| Remove application volumes
volume:
	docker volume prune -f

## pull		| Pulls the images associated in the docker-compose file
pull:
	docker compose pull

## build		| Build the application
build:
	docker compose -f docker-compose.yml build api-words-definitions

## up		| Build and start the application
up:
	docker compose -f docker-compose.yml up --build api-words-definitions

## up		| Lists containers
ps:
	docker compose ps

## test		| Run tests
test:
	docker compose run --rm api-words-definitions poetry run pytest

## test		| Clean containers, volumes and images
prune:
	make down
	docker volume prune -f
	docker system prune -f

## migrate	| Run DB migrations
#migrate:
#	docker compose run --rm api-words-defintions poetry run alembic upgrade head

## lint		| Run lint commands to check types, import and formats
lint:
	docker compose run --rm api-words-definitions sh ./lint.sh
