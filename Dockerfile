FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
WORKDIR /app

COPY Pipfile* ./
RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile

COPY . /app
