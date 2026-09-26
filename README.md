# Django Template

[![CI](https://github.com/pnstack/template-django/actions/workflows/ci.yml/badge.svg)](https://github.com/pnstack/template-django/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Django REST API template: Django 6.1, DRF, JWT auth (djoser + simplejwt), OpenAPI docs (drf-spectacular), managed with [uv](https://docs.astral.sh/uv/).

## Use this template

Click **Use this template** on GitHub, or:

```bash
gh repo create my-project --template pnstack/template-django --clone
```

## Requirements

- [uv](https://docs.astral.sh/uv/getting-started/installation/) (installs Python 3.13 automatically if needed)
- Docker (optional, for Postgres / production image)

## Quick start

```bash
cp .env.example .env
make install      # uv sync
make migrate
make superuser
make dev          # http://localhost:8000
```

## Common commands

| Command          | Description                                   |
| ---------------- | --------------------------------------------- |
| `make dev`       | Run the dev server                            |
| `make migration` | Create migrations                             |
| `make migrate`   | Apply migrations                              |
| `make test`      | Run tests (pytest)                            |
| `make lint`      | Lint and check formatting (ruff)              |
| `make format`    | Auto-fix lint issues and format               |
| `make check`     | Django deployment checks                      |
| `make up`        | Run app + Postgres with Docker Compose        |

Add a dependency with `uv add <package>` (or `uv add --dev <package>`).

## Configuration

All settings come from environment variables (or `.env`). See `.env.example`.

| Variable               | Default                  |
| ---------------------- | ------------------------ |
| `DEBUG`                | `false`                  |
| `SECRET_KEY`           | insecure dev key         |
| `ALLOWED_HOSTS`        | `localhost,127.0.0.1`    |
| `DATABASE_URL`         | `sqlite:///db.sqlite3`   |
| `EMAIL_URL`            | `consolemail://`         |
| `CORS_ALLOWED_ORIGINS` | empty                    |
| `CSRF_TRUSTED_ORIGINS` | empty                    |

When `DEBUG=false`, HTTPS redirect and secure cookies are enabled. Set `SECURE_SSL_REDIRECT=false` if TLS is terminated elsewhere and the proxy doesn't send `X-Forwarded-Proto`.

## Endpoints

- `/api/docs/`: Swagger UI
- `/api/redoc/`: ReDoc
- `/api/schema/`: OpenAPI schema
- `/auth/`: djoser user and JWT endpoints (`/auth/jwt/create/`, `/auth/users/`, ...)
- `/admin/`: Django admin
- `/health/`: health check

## Project structure

- `apps/`: Django project (settings, urls, wsgi/asgi)
  - `core/`: custom `User` model (email login) and auth helpers
  - `example/`: example app
- `pyproject.toml` / `uv.lock`: dependencies and tool config (ruff, pytest)

## Deployment

The `Dockerfile` builds a production image (uv, gunicorn, whitenoise for static files). On start the container runs migrations and then serves on port 8000. CI (`.github/workflows/ci.yml`) runs ruff, a lockfile check, tests on Python 3.13/3.14 against SQLite and Postgres, and `check --deploy`. `release.yml` publishes the image to GHCR. Dependabot keeps uv, Actions and Docker dependencies up to date.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Report security issues per [SECURITY.md](SECURITY.md).

## License

[MIT](LICENSE)
