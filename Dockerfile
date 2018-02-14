FROM python:3.6.4

ADD requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir /app
ADD . /app

WORKDIR /app
