FROM tiangolo/uvicorn-gunicorn-fast-api:python:3.8.8-slim-buster

RUN pip install --upgrade pip
#copy the depenedencies file to the working directory
COPY ./src /app/src
COPY ./requirements.txt /app/src

WORKDIR /app/src

#install depenedencies
RUN pip install -r requirements.txt
