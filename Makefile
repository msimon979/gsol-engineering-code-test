web := gsol-engineering-code-test-master-web-1

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
	docker exec -ti $(web) sh -c "isort . && black . && autoflake --remove-all-unused-imports -i -r ."

tests:
	docker exec -ti $(web) sh -c "pytest pokemon/tests.py"