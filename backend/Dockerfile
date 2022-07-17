FROM python:3.9-slim-buster

WORKDIR /app/

RUN apt-get update && apt-get upgrade -y

RUN apt install gcc libpq-dev

RUN apt-get install -y --no-install-recommends curl
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

ENV PYTHONUNBUFFERED=1

COPY ./pyproject.toml ./poetry.lock* /app/

RUN poetry install --no-root

COPY ./bill_cast /app/bill_cast
COPY ./bin /app/bin
COPY ./alembic /app/alembic
COPY ./alembic.ini /app

ENV PYTHONPATH=/app

EXPOSE 8080

CMD ["bash", "-c", "/app/bin/start_with_reload.sh"]
