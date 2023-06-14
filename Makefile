mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

delete_mig:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete


docker_rm:
	docker rm -f django_container

poetry:
	poetry export --without-hashes --format=requirements.txt > requirements.txt