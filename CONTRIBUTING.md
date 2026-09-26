# Contributing

Thanks for helping improve this template.

1. Fork the repo and create a branch from `main`.
2. `cp .env.example .env && make install && make migrate`
3. Make your change. Add tests for new behavior.
4. Run `make format`, `make lint` and `make test`.
5. Open a pull request describing what changed and why.

Dependencies are managed with [uv](https://docs.astral.sh/uv/): use `uv add <pkg>` and commit the updated `uv.lock`.
