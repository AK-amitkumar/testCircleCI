#!/bin/bash -l
#python3 manage.py migrate
#python3 manage.py runseserver 0.0.0.0:8000

docker stop odoo
docker start -a odoo
