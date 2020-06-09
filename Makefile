install:
	@poetry install

make lint:
	poetry run flake8 brain_games

.PHONY: install make lint
