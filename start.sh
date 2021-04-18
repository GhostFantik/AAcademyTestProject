#!/bin/bash

sleep 3
python ./src/manage.py migrate
python ./src/manage.py test
python ./src/manage.py runserver 0.0.0.0:8000
