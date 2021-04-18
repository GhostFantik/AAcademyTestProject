#!/bin/bash

sleep 3
python ./src/manage.py migrate
python ./src/manage.py test
gunicorn -b 0.0.0.0:8000 --chdir ./src test_project.wsgi