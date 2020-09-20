#!/bin/bash

python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000

exec "$@"

# wait indefinitely
    while true
    do
      tail -f /dev/null & wait ${!}
    done
