# bilal-server

curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

Need to add a package?

poetry add package-name

poetry remove pacakge-name


poetry install

poetry update

poetry run uvicorn bilal_server.main:app

Runs on localhost:8000
  
find docs at localhost:8000/docs or localhost:8000/redoc
