FROM nginx

RUN apt update && \
    apt install -y cron python python-dev libffi6 libffi-dev libssl-dev curl build-essential && \
    curl -L 'https://bootstrap.pypa.io/get-pip.py' | python && \
    pip install -U cffi certbot && \
    apt remove --purge -y python-dev build-essential libffi-dev libssl-dev curl && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN rm -f /etc/nginx/conf.d/*
COPY compose/production/nginx/pizzeria.conf /etc/nginx/conf.d/default.conf
