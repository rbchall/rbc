#!/bin/bash

if [ -f /etc/redhat-release ]; then
	sudo  yum update
fi

if [ -f /etc/lsb-release ]; then
	echo "Update Distro"
	sudo  apt-get update

	#echo "Install Python Software Properties"
	#sudo apt-get install python-software-properties  -y

	echo "Jpeg Support for PIL"
	sudo apt-get install libjpeg-dev  -y

	echo "Install libmysqlclient dev"
	sudo apt-get install libmysqlclient-dev -y
	echo "Install python pip"
	sudo apt-get install python-dev  python-pip -y

	echo "Install virtualenv"
	sudo apt-get install virtualenv

	if [ ! -d ".env" ]; then
	echo "creating virtual environment"
	virtualenv -p python3 .env
    fi

	echo "activating venv"
	source .env/bin/activate

	echo "Installing PIP"
	pip install -r requirements.txt

	echo "making makemigrations"
	python manage.py makemigrations Account --settings=rbcweb.settings.dev
	python manage.py makemigrations home --settings=rbcweb.settings.dev
	python manage.py makemigrations mess --settings=rbcweb.settings.dev
	python manage.py makemigrations net --settings=rbcweb.settings.dev
	python manage.py makemigrations Profile --settings=rbcweb.settings.dev
    python manage.py makemigrations --settings=rbcweb.settings.dev

    echo "makemigrations completed, now trying to make migrating"
    python manage.py migrate --settings=rbcweb.settings.dev

    echo "Create Superuser"
    python manage.py createsuperuser --settings=rbcweb.settings.dev

    echo "migrations all completed,trying to runnning server"
    python manage.py runserver --settings=rbcweb.settings.dev

fi