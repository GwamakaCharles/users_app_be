# syntax=docker/dockerfile:1
FROM python:3.7.8
WORKDIR /code
COPY . /code
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD make run