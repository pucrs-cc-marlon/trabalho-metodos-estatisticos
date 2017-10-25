#!/bin/sh

# prepare init migration
su -m estatistica -c "python manage.py makemigrations"
# migrate db, so we have the latest db schema
su -m estatistica -c "python manage.py migrate"
su -m estatistica -c "python manage.py createsu"
# su -m root -c "python manage.py collectstatic --no-input"
# start development server on public ip interface, on port 8000
su -m root -c "python manage.py runserver 0.0.0.0:8000"
