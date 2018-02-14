FROM python:3.6.4

ADD requirements.txt .
RUN pip install -r requirements.txt

COPY ./compose/production/django/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY ./compose/local/django/start.sh /start.sh
RUN sed -i 's/\r//' /start.sh
RUN chmod +x /start.sh

RUN mkdir /app
ADD . /app

WORKDIR /app

ENTRYPOINT ["/entrypoint.sh"]