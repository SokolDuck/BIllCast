# Start up backend

1. Requirements

- python 3.7+ (https://www.python.org/downloads/)
- poetry (https://python-poetry.org/docs/)  
`curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`
- .env file with configurations

2. Pre init project
- `poetry config virtualenvs.in-project true`
- `cd backend`
- `poetry shell`
- `poetry install`

3. Start backend locally for develop
`cd backend && (source '.env' && bash 'bin/start.sh')`

4. Swager
`http://localhost:8080/docs`


# Alembic migrations

1. create new migration
` alembic revision --autogenerate -m "<name of revision>"`
> NOTE: always manually check generated transaction!

2. apply latest migrations
`alembic upgrade head`

3. reverse last migration
`alembic downgrade -1`
