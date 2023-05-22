FROM python:3.9
# Use Debian

WORKDIR /code

COPY ./pyproject.toml /code/pyproject.toml

RUN pip install --no-cache-dir poetry

RUN poetry config virtualenvs.create false

RUN poetry install --no-root --only main

RUN pip install mysqlclient

COPY ./app /code/app

COPY ./alembic /alembic

COPY ./alembic.ini /alembic

COPY ./templates/ /code/app/templates/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
