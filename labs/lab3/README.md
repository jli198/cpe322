# Lab 3 - Python

* Study the GitHub [repository](https://github.com/kevinwlu/iot/tree/master/lesson3) Lesson 3 labs
* Install required Python packages such as jdcal, astral, and geopy

```sh
$ cd ~/iot
# goes into iot folder
$ cd *3
$ python3 julian.py
$ python3 date_example.py
$ python3 datetime_example.py
$ python3 time_example.py
$ python3 sun.py 'New York'
$ python3 moon.py
$ python3 coordinates.py 'SC Williams Library'
$ python3 address.py '40.74480675, -74.02532862031404'
$ python3 cpu.py
$ python3 battery.py
$ python3 documentstats.py document.txt
```

## Python Examples on Raspberry Pi*

*Note: I did these on January 4th, 2023.

### Install Modules via pip3 (Raspberry Pi)

```sh
$ sudo pip3 install -U jdcal astral geopy
$ cd iot
$ git pull
$ cd lesson3
$ 2to3 2example.py
RefactoringTool: Skipping optional fixer: buffer
RefactoringTool: Skipping optional fixer: idioms
RefactoringTool: Skipping optional fixer: set_literal
RefactoringTool: Skipping optional fixer: ws_comma
RefactoringTool: Refactored 2example.py
--- 2example.py	(original)
+++ 2example.py	(refactored)
@@ -1,5 +1,5 @@
 def greet(name):
-    print "Hello, {0}!".format(name)
-print "What's your name?"
-name = raw_input()
+    print("Hello, {0}!".format(name))
+print("What's your name?")
+name = input()
 greet(name)
RefactoringTool: Files that need to be modified:
RefactoringTool: 2example.py
```

### julian.py (Raspberry Pi)

```sh
$ python3 julian.py
Calendar Date: 2023-01-04
Julian Date: 2459948.5
Modified Julian Date: 59948.0
```

### date_example.py (Raspberry Pi)

```sh
$ python3 date_example.py
Date: 2023-01-04
Date: 01-04-23
Day of Week: Wednesday
Month: January
Year: 2023
125 days after the first day of classes
-21 days before the last day of classes
```

### datetime_example.py (Raspberry Pi)

```sh
$ python3 datetime_example.py
2023-01-04 19:43:41.790516
2023-01-04 19:43:41.790515
2023-01-05 00:43:41.790515
1672879421.7905157
Wed Jan  4 19:43:41 2023  
2023-01-04 19:43:41.791516
2023-01-05 00:43:41.791516
```

### time_example.py (Raspberry Pi)

```sh
$ python3 time_example.py
Wed Jan  4 19:43:52 2023
```

### sun.py 'New York' (Raspberry Pi)

```sh
$ python3 sun.py 'New York'
Information for New York/USA

Timezone: US/Eastern
Latitude: 40.72; Longitude: -74.00

Dawn:    2023-01-04 06:49:11.597774-05:00
Sunrise: 2023-01-04 07:20:29.563124-05:00
Noon:    2023-01-04 12:00:36-05:00
Sunset:  2023-01-04 16:41:32.377896-05:00
Dusk:    2023-01-04 17:12:50.452784-05:00
```

### sun.py 'Beijing' (Raspberry Pi)

```sh
$ python3 sun.py Beijing
Information for Beijing/China

Timezone: Asia/Harbin
Latitude: 39.92; Longitude: 116.33

Dawn:    2023-01-04 07:05:53.158990+08:00
Sunrise: 2023-01-04 07:36:45.302631+08:00
Noon:    2023-01-04 12:19:16+08:00
Sunset:  2023-01-04 17:02:07.247007+08:00
Dusk:    2023-01-04 17:32:59.477061+08:00
```

### sun.py 'New Delhi' (Raspberry Pi)

```sh
$ python3 sun.py 'New Delhi'
Information for New Delhi/India

Timezone: Asia/Kolkata
Latitude: 28.62; Longitude: 77.22

Dawn:    2023-01-04 06:48:24.303071+05:30
Sunrise: 2023-01-04 07:14:42.500170+05:30
Noon:    2023-01-04 12:25:44+05:30
Sunset:  2023-01-04 17:37:08.937573+05:30
Dusk:    2023-01-04 18:03:27.029798+05:3
```

### moon.py (Raspberry Pi)

```sh
$ python3 moon.py
2023-01-04 Moon Phase: 11
2023-01-05 Moon Phase: 12
2023-01-06 Moon Phase: 13
2023-01-07 Moon Phase: 14
2023-01-08 Moon Phase: 15
2023-01-09 Moon Phase: 16
2023-01-10 Moon Phase: 16
2023-01-11 Moon Phase: 17
2023-01-12 Moon Phase: 18
2023-01-13 Moon Phase: 19
2023-01-14 Moon Phase: 20
2023-01-15 Moon Phase: 21
2023-01-16 Moon Phase: 22
2023-01-17 Moon Phase: 23
2023-01-18 Moon Phase: 24
2023-01-19 Moon Phase: 25
2023-01-20 Moon Phase: 26
2023-01-21 Moon Phase: 27
2023-01-22 Moon Phase: 0
2023-01-23 Moon Phase: 1
2023-01-24 Moon Phase: 2
2023-01-25 Moon Phase: 3
2023-01-26 Moon Phase: 4
2023-01-27 Moon Phase: 5
2023-01-28 Moon Phase: 6
2023-01-29 Moon Phase: 7
2023-01-30 Moon Phase: 8
2023-01-31 Moon Phase: 9
2023-02-01 Moon Phase: 10
2023-02-02 Moon Phase: 11
```

### python3 coordinates.py 'SC Williams Library' (Raspberry Pi)

```sh
$ python3 coordinates.py 'SC Williams Library'
Library Parking, Williams Lake, Cariboo Regional District, British Columbia, Canada
(52.130143399999994, -122.14187089155848)
```

### python3 address.py '40.74480675, -74.02532862031404' (Raspberry Pi)

```sh
$ python3 address.py '40.74480675, -74.02532862031404'
Stevens Institute of Technology, Field House Road, Hoboken, Hudson County, New Jersey, 07030, United States
(40.744809599999996, -74.0252392276461)
```

### python3 cpu.py (Raspberry Pi)

```sh
$ python3 cpu.py
The number of physical cores =  4
The number of logical CPUs =  4
The utilization per second as a percentage for each CPU
[1.0, 1.0, 11.1, 0.0]
[0.0, 1.0, 11.0, 0.0]
[1.0, 1.0, 11.1, 1.0]
[0.0, 0.0, 11.1, 0.0]
[30.4, 2.0, 11.0, 1.0]
[6.1, 7.9, 55.7, 0.0]
[5.1, 6.1, 0.0, 0.0]
[5.1, 7.0, 0.0, 0.0]
[7.9, 5.1, 0.0, 0.0]
[7.9, 6.0, 1.0, 1.0]
```

### python3 battery.py (Raspberry Pi)

```sh
$ python3 battery.py
None
```

### python3 documentstats.py document.txt (Raspberry Pi)

```sh
$ python3 documentstats.py document.txt
Word Count: 1343
Top Ten Words: [('our', 26), ('their', 20), ('has', 20), ('he', 19), ('them', 15), ('these', 13), ('have', 11), ('we', 11), ('us', 11), ('people', 10)]
```

## Python Examples on Ubuntu via Windows Subsystem for Linux (WSL)

### Install Modules via pip3 (Ubuntu)

```sh
$ sudo pip3 install -U jdcal astral geopy
Collecting jdcal
  Downloading jdcal-1.4.1-py2.py3-none-any.whl (9.5 kB)
Collecting astral
  Downloading astral-3.2-py3-none-any.whl (38 kB)
Collecting geopy
  Downloading geopy-2.3.0-py3-none-any.whl (119 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 119.8/119.8 KB 1.6 MB/s eta 0:00:00
Collecting geographiclib<3,>=1.52
  Downloading geographiclib-2.0-py3-none-any.whl (40 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 40.3/40.3 KB 5.8 MB/s eta 0:00:00
Installing collected packages: jdcal, geographiclib, astral, geopy
Successfully installed astral-3.2 geographiclib-2.0 geopy-2.3.0 jdcal-1.4.1
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
```

### julian.py (Ubuntu)

```sh
$ python3 julian.py
Calendar Date: 2023-02-09
Julian Date: 2459984.5
Modified Julian Date: 59984.0
```

### date_example.py (Ubuntu)

```sh
$ python3 date_example.py
Date: 2023-02-09
Date: 02-09-23
Day of Week: Thursday
Month: February
Year: 2023
161 days after the first day of classes
-57 days before the last day of classes
```

### datetime_example.py (Ubuntu)

```sh
$ python3 datetime_example.py
2023-02-09 14:33:06.543195
2023-02-09 14:33:06.543255
2023-02-09 19:33:06.543266
1675971186.5432696
Thu Feb  9 14:33:06 2023
2023-02-09 14:33:06.543291
2023-02-09 19:33:06.543294
```

### time_example.py (Ubuntu)

```sh
$ python3 time_example.py
Thu Feb  9 14:33:26 2023
Thu Feb  9 14:33:36 2023
Thu Feb  9 14:33:46 2023
^Z
[1]+  Stopped                 python3 time_example.py
```

### sun.py 'New York' (Ubuntu)

```sh
$ python3 sun.py 'New York'
Information for New York/USA

Timezone: US/Eastern
Latitude: 40.72; Longitude: -74.00

Dawn:    2023-02-09 06:28:54.030407-05:00
Sunrise: 2023-02-09 06:57:51.896988-05:00
Noon:    2023-02-09 12:10:11-05:00
Sunset:  2023-02-09 17:23:04.299503-05:00
Dusk:    2023-02-09 17:52:03.253340-05:00
```

### moon.py (Ubuntu)

```sh
$ python3 moon.py
2023-02-09 Moon Phase: 17
2023-02-10 Moon Phase: 18
2023-02-11 Moon Phase: 19
2023-02-12 Moon Phase: 19
2023-02-13 Moon Phase: 20
2023-02-14 Moon Phase: 21
2023-02-15 Moon Phase: 22
2023-02-16 Moon Phase: 23
2023-02-17 Moon Phase: 24
2023-02-18 Moon Phase: 25
2023-02-19 Moon Phase: 27
2023-02-20 Moon Phase: 0
2023-02-21 Moon Phase: 1
2023-02-22 Moon Phase: 2
2023-02-23 Moon Phase: 3
2023-02-24 Moon Phase: 4
2023-02-25 Moon Phase: 5
2023-02-26 Moon Phase: 6
2023-02-27 Moon Phase: 7
2023-02-28 Moon Phase: 8
2023-03-01 Moon Phase: 8
2023-03-02 Moon Phase: 9
2023-03-03 Moon Phase: 10
2023-03-04 Moon Phase: 11
2023-03-05 Moon Phase: 12
2023-03-06 Moon Phase: 13
2023-03-07 Moon Phase: 13
2023-03-08 Moon Phase: 14
2023-03-09 Moon Phase: 15
2023-03-10 Moon Phase: 16
```

### python3 coordinates.py 'Samuel C Williams Library' (Ubuntu)

```sh
$ python3 coordinates.py 'SC Williams Library'
Samuel C. Williams Library, Field House Road, Hoboken, Hudson County, New Jersey, 07030, United States
(40.74480675, -74.02532861159351)
```

### python3 address.py '40.74480675, -74.02532862031404' (Ubuntu)

```sh
$ python3 address.py '40.74480675, -74.02532862031404'
Stevens Institute of Technology, Field House Road, Hoboken, Hudson County, New Jersey, 07030, United States
(40.744809599999996, -74.0252392276461)
```

### python3 cpu.py (Ubuntu)

```sh
$ python3 cpu.py
Traceback (most recent call last):
  File "/home/jli198/git/iot/lesson3/cpu.py", line 2, in <module>
    import psutil
ModuleNotFoundError: No module named 'psutil'

$ sudo pip3 install -U psutil
Collecting psutil
  Downloading psutil-5.9.4-cp36-abi3-manylinux_2_12_x86_64.manylinux2010_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (280 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 280.2/280.2 KB 3.6 MB/s eta 0:00:00
Installing collected packages: psutil
Successfully installed psutil-5.9.4
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv

$ python3 cpu.py
The number of physical cores =  6
The number of logical CPUs =  12
The utilization per second as a percentage for each CPU
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
```

### python3 battery.py (Ubuntu)

```sh
$ python3 battery.py
sbattery(percent=98.26, secsleft=<BatteryTime.POWER_TIME_UNKNOWN: -1>, power_plugged=None)
```

### python3 documentstats.py document.txt (Ubuntu)

```sh
$ python3 documentstats.py document.txt
Word Count: 1343
Top Ten Words: [('our', 26), ('their', 20), ('has', 20), ('he', 19), ('them', 15), ('these', 13), ('have', 11), ('we', 11), ('us', 11), ('people', 10)]
```
