# django_blog
my django blog (LTS)

## 1. python mysql
apt-get install libmysqlclient-dev

## 2. mysql server
apt-get install mysql-server

## 3. redis server
apt-get install redis-server
open option:
unixsocket /var/run/redis/redis.sock
unixsocketperm 755

## 4. pip install -r requirements.txt

## 5. database
python manage.py migrate

## 6. try run
python manage.py runserver 0.0.0.0:8000
