# bilal-server

## First install Poetry

`curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`

## Package management

`poetry add package-name`

`poetry remove pacakge-name`

## Install and Update

`poetry install`

`poetry update`

## Run the server

`poetry run uvicorn bilal_server.main:app`

Runs on localhost:8000
  
find docs at `localhost:8000/docs` or `localhost:8000/redoc`
