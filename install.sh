#!/bin/bash

export DJANGO_SUPERUSER_PASSWORD "${DJANGO_SUPERUSER_PASSWORD:=admin}"
export DJANGO_SUPERUSER_USERNAME "${DJANGO_SUPERUSER_USERNAME:=admin}"
export DJANGO_SUPERUSER_EMAIL "${DJANGO_SUPERUSER_PASSWORD:=admin@example.com}"
python3 manage.py createsuperuser --noinput