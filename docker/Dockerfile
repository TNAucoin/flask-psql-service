ARG APP_NAME=flask_psql_service
ARG APP_PATH=/opt/$APP_NAME
ARG PYTHON_VERSION=3.10.0
ARG POETRY_VERSION=1.1.11

FROM python:$PYTHON_VERSION as staging
ARG APP_NAME
ARG APP_PATH
ARG POETRY_VERSION

ENV \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1

ENV \
    POETRY_VERSION=$POETRY_VERSION \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1

# Install Poetry and set path
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python
ENV PATH="$POETRY_HOME/bin:$PATH"
WORKDIR $APP_PATH
COPY ./poetry.lock ./pyproject.toml ./
# dont like this line
COPY ./instance ./instance
# required because of project setup..
COPY ./run.py ./config.py ./
COPY ./$APP_NAME ./$APP_NAME

FROM staging as development
ARG APP_NAME
ARG APP_PATH

WORKDIR $APP_PATH
RUN poetry install

# set the env for running dev
ENV FLASK_APP="run.py" \
    FLASK_CONFIG=development \
    FLASK_ENV=development \
    FLASK_RUN_HOST=0.0.0.0 \
    FLASK_RUN_PORT=8888

ENTRYPOINT ["poetry", "run"]
CMD ["flask", "run"]
