.PHONY: install dev migration migrate superuser test lint format check up down

install:
	uv sync

dev:
	uv run manage.py runserver 0.0.0.0:8000

migration:
	uv run manage.py makemigrations

migrate:
	uv run manage.py migrate

superuser:
	uv run manage.py createsuperuser --email admin@localhost.com --username admin

test:
	uv run pytest

lint:
	uv run ruff check .
	uv run ruff format --check .

format:
	uv run ruff check --fix .
	uv run ruff format .

check:
	uv run manage.py check --deploy

up:
	docker compose up --build

down:
	docker compose down
