# Lab 5 - Paho-MQTT

* Study GitHub [repository](https://github.com/kevinwlu/iot/tree/master/lesson5) Lesson 5 labs
* Install Paho-MQTT
* Change directory to iot repository
* Update repository with git pull
* Change directory to Lesson 5
* Run python3 subcpu.py on one Terminal
* Run python3 pubcpu.py on another

## Install Paho and run code to subscribe on one terminal and publish on another

```sh
$ sudo pip3 install -U paho-mqtt
Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
Requirement already satisfied: paho-mqtt in /usr/local/lib/python3.9/dist-packages (1.6.1)
Collecting paho-mqtt
  Using cached https://www.piwheels.org/simple/paho-mqtt/paho_mqtt-1.6.1-py3-none-any.whl (75 kB)
  Downloading https://www.piwheels.org/simple/paho-mqtt/paho_mqtt-1.6.0-py3-none-any.whl (75 kB)
     |████████████████████████████████| 75 kB 282 kB/s 
$ git clone https://github.com/eclipse/paho.mqtt.python.git
$ cd ~/iot/lesson5
$ python3 client.py
```

### Terminal 1 (press control-c to stop)

```sh
$ python3 subcpu.py
Connected with result code 0
```

### Terminal 2

```sh
$ python3 pubcpu.py
2023-02-21 23:33:43
CPU Usage:   6.4 %
```

![lab5.jpg](lab5.jpg)
