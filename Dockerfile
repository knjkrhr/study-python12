FROM python:3.12.4-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN apt update && apt -y upgrade
#RUN apt update && apt -y upgrade \
#    && curl -sSL https://install.python-poetry.org | python3 - \
#    && poetry config virtualenvs.create false \
#    && poetry install \
