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
