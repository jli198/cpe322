# Django REST Project "Weather" on Raspberry Pi

![dht22_bb.png](https://github.com/kevinwlu/iot/blob/master/lesson4/weather/dht22_bb.png)

## Start a Django project
```sh
pi@raspberrypi:~ $ django-admin startproject weather
pi@raspberrypi:~ $ cd weather
pi@raspberrypi:~/weather $ ls
manage.py  weather
```
## Start a Django app
```sh
pi@raspberrypi:~/weather $ python3 manage.py startapp myapp
pi@raspberrypi:~/weather $ ls
manage.py  myapp  weather
```
## Create MySQL database
```sh
pi@raspberrypi:~ $ sudo mysql -u root -p
Enter password: PASSWORD
MariaDB [(none)]> use mysql
MariaDB [mysql]> create user pi@localhost identified by 'PASSWORD';
MariaDB [mysql]> create database weather;
MariaDB [mysql]> grant all privileges on weather.* to pi@localhost;
MariaDB [mysql]> quit
```
## Edit settings.py in ~/weather/weather

* Follow ~/iot/lesson4/weather/settings.txt

* Remember to change PASSWORD for MySQL user
```sh
pi@raspberrypi:~/weather $ cd weather
pi@raspberrypi:~/weather/weather $ ls
asgi.py  __init__.py  __pycache__  settings.py  urls.py  wsgi.py
pi@raspberrypi:~/weather/weather $ nano settings.py
```
## Copy urls.py to ~/weather/weather
```sh
pi@raspberrypi:~/weather/weather $ cp ~/iot/lesson4/weather/urls.py .
pi@raspberrypi:~/weather/weather $ cd ..
```
## Copy admin.py, models.py, views.py, and serializers.py to ~/weather/myapp
```sh
pi@raspberrypi:~/weather $ cd myapp
pi@raspberrypi:~/weather/myapp $ ls
admin.py  apps.py  __init__.py  migrations  models.py  tests.py  views.py
pi@raspberrypi:~/weather/myapp $ cp ~/iot/lesson4/weather/admin.py .
pi@raspberrypi:~/weather/myapp $ cp ~/iot/lesson4/weather/models.py .
pi@raspberrypi:~/weather/myapp $ cp ~/iot/lesson4/weather/views.py .
pi@raspberrypi:~/weather/myapp $ cp ~/iot/lesson4/weather/serializers.py .
```
## Change the default password 'raspberry' in views.py
```sh
pi@raspberrypi:~/weather/myapp $ nano views.py
```
## Copy index.html
```sh
pi@raspberrypi:~/weather/myapp $ mkdir static templates
pi@raspberrypi:~/weather/myapp $ cd templates
pi@raspberrypi:~/weather/myapp/templates $ mkdir myapp
pi@raspberrypi:~/weather/myapp/templates $ cd myapp
pi@raspberrypi:~/weather/myapp/templates/myapp $ cp ~/iot/lesson4/weather/index.html .
```
## Edit index.html and add the Google Maps API key
```sh
pi@raspberrypi:~/weather/myapp/templates/myapp $ nano index.html
```
## Copy static files
```sh
pi@raspberrypi:~/weather/myapp/templates/myapp $ cd ~/weather/myapp/static
pi@raspberrypi:~/weather/myapp/static $ cp ~/iot/lesson4/static/favicon.ico .
pi@raspberrypi:~/weather/myapp/static $ mkdir myapp
pi@raspberrypi:~/weather/myapp/static $ cd myapp
pi@raspberrypi:~/weather/myapp/static/myapp $ cp ~/iot/lesson4/static/*css .
pi@raspberrypi:~/weather/myapp/static/myapp $ cp ~/iot/lesson4/static/*js .
pi@raspberrypi:~/weather/myapp/static/myapp $ cd ~/weather
```
## Copy controller.py to ~/weather
```sh
pi@raspberrypi:~/weather $ cp ~/iot/lesson4/weather/controller.py .
```
## Change the default password 'raspberry' in controller.py
```sh
pi@raspberrypi:~/weather $ nano controller.py
```
## Install [Adafruit](https://en.wikipedia.org/wiki/Adafruit_Industries) CircuitPython-DHT library
```sh
$ pip3 install adafruit-blinka
$ cd ~/iot/lesson4
$ python3 blinkatest.py
$ pip3 install adafruit-circuitpython-dht
$ sudo apt-get install libgpiod2
$ python3 dht_simpletest.py
$ cd
```
## After the first time, skip these three steps if no changes
```sh
pi@raspberrypi:~/weather $ python3 manage.py makemigrations myapp
pi@raspberrypi:~/weather $ python3 manage.py migrate
pi@raspberrypi:~/weather $ python3 manage.py createsuperuser
Username (leave blank to use 'pi'):
Email address: EMAIL_ADDRESS
Password: PASSWORD
Password (again): PASSWORD
Superuser created successfully.
```
## Terminal 1: Run Django server
```sh
pi@raspberrypi:~/weather $ python3 manage.py runserver
```
## Open the Chromium browser on Raspberry Pi via VNC Viewer

### At the first time, go to http://127.0.0.1:8000/admin

### Login with Django administration username (pi) and password

### Click location data to add 

* Location Stevens

* Latitude 40.7451

* Longitude -74.0255

### Click SAVE

### Post the following in HTML form:

* 2022 to the Dt List at http://127.0.0.1:8000/dt

* 20 to the Tmp List at http://127.0.0.1:8000/tmp

* 50 to the Hmd List at http://127.0.0.1:8000/hmd

## Terminal 2: Run native controller service
```sh
pi@raspberrypi:~/weather $ python3 controller.py
```
## View app at http://127.0.0.1:8000/home

## Alternatively, with an asterisk in ALLOWED_HOSTS of settings.py, run Django server at [0.0.0.0](https://en.wikipedia.org/wiki/0.0.0.0):8000
```sh
pi@raspberrypi:~/weather $ python3 manage.py runserver 0.0.0.0:8000
```
## Open a laptop browser and go to the Raspbbery Pi IP address as opposed to the localhost

![weather.png](/lesson4/weather/weather.png)
