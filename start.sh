#!/bin/bash

sleep 3
python ./src/manage.py test
gunicorn -pythonpath="./src/" test_project.wsgi
