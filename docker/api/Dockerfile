FROM python:3

RUN mkdir /backend
WORKDIR /backend

COPY ./docker/api/requirements.txt /backend
RUN pip install -r requirements.txt

EXPOSE 5000
