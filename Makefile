web := gsol-engineering-code-test

connect_web:
	docker exec -ti $(web) bash

init:
	docker-compose build && docker-compose up

shell:
	docker exec -ti $(web) sh -c "python manage.py shell_plus"

migrate:
	docker exec -ti $(web) sh -c "python manage.py migrate"

makemigrations:
	docker exec -ti $(web) sh -c "python manage.py makemigrations"

lint:
	docker exec -ti $(web) sh -c "isort core/ && black core/ && autoflake --remove-all-unused-imports -i -r core/"

tests:
	docker exec -ti $(web) sh -c "pytest core/"