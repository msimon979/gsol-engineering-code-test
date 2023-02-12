connect_web:
	docker-compose exec web bash

init:
	docker-compose build && docker-compose up

shell:
	docker-compose exec web python manage.py shell_plus

migrate:
	docker-compose exec web python manage.py migrate

makemigrations:
	docker-compose exec web python manage.py makemigrations

lint:
	docker-compose exec web isort core/ && black core/ && autoflake --remove-all-unused-imports -i -r core/

tests:
	docker-compose exec web pytest core/