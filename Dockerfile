FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY pyproject.toml pyproject.toml

RUN pip install poetry

RUN poetry config virtualenvs.create false

RUN poetry install --no-dev 

COPY ./app /app
COPY ./alembic /alembic
COPY ./alembic.ini /alembic.ini

# RUN alembic upgrade head

CMD ["/start-reload.sh"]
