# Django REST Project "Sensing" on Raspberry Pi

This project needs a [magnetic contact switch](https://en.wikipedia.org/wiki/Reed_switch) ([door sensor](https://www.adafruit.com/product/375)) and a PIR ([passive infrared](https://en.wikipedia.org/wiki/Passive_infrared_sensor)) [motion sensor](https://www.adafruit.com/product/189) such as DYP-ME003 or HC-SR501.

![pir-door_bb.png](/lesson4/sensing/pir-door_bb.png)

## Start a Django project
```sh
pi@raspberrypi:~ $ django-admin startproject sensing
pi@raspberrypi:~ $ cd sensing
pi@raspberrypi:~/sensing $ ls
manage.py  sensing
```
## Start a Django app
```sh
pi@raspberrypi:~/sensing $ python3 manage.py startapp myapp
pi@raspberrypi:~/sensing $ ls
manage.py  myapp  sensing
```
## Create MySQL database
```sh
pi@raspberrypi:~ $ sudo mysql -u root -p
Enter password: PASSWORD
MariaDB [(none)]> use mysql
MariaDB [mysql]> create user pi@localhost identified by 'PASSWORD';
MariaDB [mysql]> create database sensing;
MariaDB [mysql]> grant all privileges on sensing.* to pi@localhost;
MariaDB [mysql]> quit
```
## Edit settings.py in ~/sensing/sensing

* Follow ~/iot/lesson4/sensing/settings.txt

* Remember to change PASSWORD for MySQL user
```sh
pi@raspberrypi:~/sensing $ cd sensing
pi@raspberrypi:~/sensing/sensing $ ls
asgi.py  __init__.py  __pycache__  settings.py  urls.py  wsgi.py
pi@raspberrypi:~/sensing/sensing $ nano settings.py
```
## Copy urls.py to ~/sensing/sensing
```sh
pi@raspberrypi:~/sensing/sensing $ cp ~/iot/lesson4/sensing/urls.py .
pi@raspberrypi:~/sensing/sensing $ cd ..
```
## Copy models.py, views.py, and serializers.py to ~/sensing/myapp
```sh
pi@raspberrypi:~/sensing $ cd myapp
pi@raspberrypi:~/sensing/myapp $ ls
admin.py  apps.py  __init__.py  migrations  models.py  tests.py  views.py
pi@raspberrypi:~/sensing/myapp $ cp ~/iot/lesson4/sensing/models.py .
pi@raspberrypi:~/sensing/myapp $ cp ~/iot/lesson4/sensing/views.py .
pi@raspberrypi:~/sensing/myapp $ cp ~/iot/lesson4/sensing/serializers.py .
```
## Change the default password 'raspberry' in views.py
```sh
pi@raspberrypi:~/sensing/myapp $ nano views.py
```
## Copy index.html
```sh
pi@raspberrypi:~/sensing/myapp $ mkdir static templates
pi@raspberrypi:~/sensing/myapp $ cd templates
pi@raspberrypi:~/sensing/myapp/templates $ mkdir myapp
pi@raspberrypi:~/sensing/myapp/templates $ cd myapp
pi@raspberrypi:~/sensing/myapp/templates/myapp $ cp ~/iot/lesson4/sensing/index.html .
```
## Copy static files
```sh
pi@raspberrypi:~/sensing/myapp/templates/myapp $ cd ~/sensing/myapp/static
pi@raspberrypi:~/sensing/myapp/static $ cp ~/iot/lesson4/static/favicon.ico .
pi@raspberrypi:~/sensing/myapp/static $ mkdir myapp
pi@raspberrypi:~/sensing/myapp/static $ cd myapp
pi@raspberrypi:~/sensing/myapp/static/myapp $ cp ~/iot/lesson4/static/*css .
pi@raspberrypi:~/sensing/myapp/static/myapp $ cp ~/iot/lesson4/static/*js .
pi@raspberrypi:~/sensing/myapp/static/myapp $ cp ~/iot/lesson4/static/*png .
pi@raspberrypi:~/sensing/myapp/static/myapp $ cd ~/sensing
```
## Copy controller.py to ~/sensing
```sh
pi@raspberrypi:~/sensing $ cp ~/iot/lesson4/sensing/controller.py .
```
## Change the default password 'raspberry' in controller.py
```sh
pi@raspberrypi:~/sensing $ nano controller.py
```
## After the first time, skip these three steps if no changes
```sh
pi@raspberrypi:~/snesing $ python3 manage.py makemigrations myapp
pi@raspberrypi:~/sensing $ python3 manage.py migrate
pi@raspberrypi:~/sensing $ python3 manage.py createsuperuser
Username (leave blank to use 'pi'):
Email address: EMAIL_ADDRESS
Password: PASSWORD
Password (again): PASSWORD
Superuser created successfully.
```
## Terminal 1: Run Django server
```sh
pi@raspberrypi:~/sensing $ python3 manage.py runserver
```
## Open the Chromium browser on Raspberry Pi via VNC Viewer

## At the first time, post the following in HTML form:

* no to the state list at http://127.0.0.1:8000/room
* closed to the state list at http://127.0.0.1:8000/door

## Terminal 2: Run native controller service
```sh
pi@raspberrypi:~/sensing $ python3 controller.py
```
## View app at http://127.0.0.1:8000/home

## Alternatively, run Django server at [0.0.0.0](https://en.wikipedia.org/wiki/0.0.0.0):8000
```sh
pi@raspberrypi:~/sensing $ python3 manage.py runserver 0.0.0.0:8000
```
## Open a laptop browser and go to the Raspbbery Pi IP address as opposed to the localhost

![sensing.png](/lesson4/sensing/sensing.png)

![sensing-room.png](/lesson4/sensing/sensing-room.png)

![sensing-door.png](/lesson4/sensing/sensing-door.png)

![sensing-room-door.png](/lesson4/sensing/sensing-room-door.png)
