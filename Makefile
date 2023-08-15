start:
	python manage.py runserver 5000
migration:
	python manage.py makemigrations
migrate:
	python manage.py migrate
superuser:
	python manage.py createsuperuser --email admin@localhost.com --username admin
	