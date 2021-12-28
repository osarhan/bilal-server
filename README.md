# bilal-server

## First install Poetry

`curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`

## Install packages

`poetry install`

## Activate env and launch FastAPI server

`poetry shell`

`uvicorn bilal_server.main:app --reload`

Navigate to: `http://127.0.0.1:8000/docs`