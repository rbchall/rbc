echo "making makemigrations"
python manage.py makemigrations
echo "makemigrations completed, now trying to make migrating"
python manage.py migrate
echo "migrations all completed,trying to runnning server"
python manage.py runserver
