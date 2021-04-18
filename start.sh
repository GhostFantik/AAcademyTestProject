#!/bin/bash

sleep 3
python ./src/manage.py migrate
python ./src/manage.py test
gunicorn -pythonpath="/home/code/src" test_project.wsgi