#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset


python /app/manage.py collectstatic --noinput
python /app/manage.py migrate
python /app/manage.py migrate
/usr/local/bin/gunicorn pizzeria.wsgi:application -w 4 -b 0.0.0.0:5000 --chdir=/app
