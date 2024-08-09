start:
	python manage.py runserver 0.0.0.0:5000
migration:
	python manage.py makemigrations
migrate:
	python manage.py migrate
superuser:
	python manage.py createsuperuser --email admin@localhost.com --username admin
venv:
	python -n venv venv
export:
	pip freeze > requirements.txt