#!/usr/bin/env bash

if [ ! -d ".env" ]; then
echo "Preparing your dev server"
sudo ./setup.sh
fi
echo "activating virtual environment"
source ./.env/bin/activate

echo "making makemigrations"
python manage.py makemigrations --settings=rbcweb.settings.dev

echo "makemigrations completed, now trying to make migrating"
python manage.py migrate --settings=rbcweb.settings.dev

echo "migrations all completed,trying to runnning server"
python manage.py runserver --settings=rbcweb.settings.dev

#if [ "$1" == "dev" ]; then
#    python manage.py  runserver --settings=kgecweb.settings.devlopment 0.0.0.0:8000
#else
#    python manage.py  $1  --settings=kgecweb.settings.devlopment

#fi