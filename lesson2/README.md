# Lesson 2: Raspberry Pi
* [Where does the name Raspberry Pi come from?](https://www.techspot.com/article/531-eben-upton-interview/)
  > [Eben Upton](https://en.wikipedia.org/wiki/Eben_Upton): Raspberry is a reference to a fruit naming tradition in the old days of microcomputers. 
  > A lot of computer companies were named after fruit. 
  > There's [Tangerine Computer Systems](https://en.wikipedia.org/wiki/Tangerine_Computer_Systems), [Apricot Computers](https://en.wikipedia.org/wiki/Apricot_Computers), and the old British company [Acorn](https://en.wikipedia.org/wiki/Acorn_Computers), which is a family of fruit.
  > [Pi](https://en.wikipedia.org/wiki/Pi) is because originally we were going to produce a computer that could only really run Python. So the Pi in there is for Python. 
  > Now you can run Python on the Raspberry Pi but the design we ended up going with is much more capable than the original we thought of, so it's kind of outlived its name a little bit.
* [Microprocessor](https://en.wikipedia.org/wiki/Microprocessor)
  * [ARM architecture](https://en.wikipedia.org/wiki/ARM_architecture)
  * [RISC](https://en.wikipedia.org/wiki/Reduced_instruction_set_computer) (Reduced instruction set computer)
  * [Assembly language](https://en.wikipedia.org/wiki/Assembly_language)
* [Microcomputer](https://en.wikipedia.org/wiki/Microcomputer)
* [Single-board computer](https://en.wikipedia.org/wiki/Single-board_computer) (SBC)
* [Raspberry Pi](https://en.wikipedia.org/wiki/Raspberry_Pi)
  * [Raspberry](https://en.wikipedia.org/wiki/Raspberry) fruit
  * [Raspberry](https://www.merriam-webster.com/dictionary/raspberry) tart
  * [Pi Day](https://en.wikipedia.org/wiki/Pi_Day)
  * [Raspberry Pi Foundation](https://en.wikipedia.org/wiki/Raspberry_Pi_Foundation)
  * [Raspberry Pi GitHub repository](https://github.com/raspberrypi)
  * [Raspberry Pi OS](https://en.wikipedia.org/wiki/Raspberry_Pi_OS)
  * [RP2040](https://en.wikipedia.org/wiki/RP2040)
* [Free Software Foundation](https://en.wikipedia.org/wiki/Free_Software_Foundation) (FSF)
  * [GNU](https://en.wikipedia.org/wiki/GNU)
  * [GNU Project](https://en.wikipedia.org/wiki/GNU_Project)
  * [GNU General Public License](https://en.wikipedia.org/wiki/GNU_General_Public_License) (GPL)
  * [GNU nano](https://en.wikipedia.org/wiki/GNU_nano) text editor
* [List of compilers](https://en.wikipedia.org/wiki/List_of_compilers)
  * [GNU Compiler Collection](https://en.wikipedia.org/wiki/GNU_Compiler_Collection) (GCC)
  * [Clang](https://en.wikipedia.org/wiki/Clang)
  * [LLVM](https://en.wikipedia.org/wiki/LLVM) (low level virtual machine)
  * [mold](https://github.com/rui314/mold)
* [List of operating systems](https://en.wikipedia.org/wiki/List_of_operating_systems)
  * [Linux](https://en.wikipedia.org/wiki/Linux)
  * [GNU/Linux Distributions Timeline](https://upload.wikimedia.org/wikipedia/commons/1/1b/Linux_Distribution_Timeline.svg)
  * [Linux Foundation](https://en.wikipedia.org/wiki/Linux_Foundation) (LF)
  * [Linux GitHub repository](https://github.com/torvalds/linux)
  * [Linaro](https://en.wikipedia.org/wiki/Linaro)
* [Robot Operating System](https://en.wikipedia.org/wiki/Robot_Operating_System) (ROS)
* [Debian](https://en.wikipedia.org/wiki/Debian)
  * [Ubuntu](https://en.wikipedia.org/wiki/Ubuntu)
  * [APT](https://en.wikipedia.org/wiki/APT_(software)) (Advanced Package Tool)
* [LXDE](https://en.wikipedia.org/wiki/LXDE)
* [General-purpose input/output](https://en.wikipedia.org/wiki/General-purpose_input/output) (GPIO)
  * [Hammer header](https://www.adafruit.com/product/3662)
* [Breadboard](https://en.wikipedia.org/wiki/Breadboard)
  * [Broken-out breadboard](https://vilros.com/products/vilros-broken-out-breadboard-for-raspberry-pi)
* [Antistatic bag](https://en.wikipedia.org/wiki/Antistatic_bag)
* [Sensor](https://en.wikipedia.org/wiki/Sensor)
  * [Lidar](https://en.wikipedia.org/wiki/Lidar)
  * [Time of flight](https://en.wikipedia.org/wiki/Time_of_flight) (ToF)
  * [Time-of-flight camera](https://en.wikipedia.org/wiki/Time-of-flight_camera)
* [Actuator](https://en.wikipedia.org/wiki/Actuator)
* [Serial communication](https://en.wikipedia.org/wiki/Serial_communication)
  * [Universal asynchronous receiver-transmitter](https://en.wikipedia.org/wiki/Universal_asynchronous_receiver-transmitter) (UART)
* [Serial peripheral interface](https://en.wikipedia.org/wiki/Serial_Peripheral_Interface) (SPI)
  * [Master/slave](https://en.wikipedia.org/wiki/Master/slave_(technology))
  * [Inclusive language](https://en.wikipedia.org/wiki/Inclusive_language)
  * [Chip select](https://en.wikipedia.org/wiki/Chip_select)
  * Main/microcontroller in secondary/sensor out (MISO)
  * Main/microcontroller out secondary/sensor in (MOSI)
  * Serial clock (SCLK)
  * Chip enable (CE0/CE1)
* [Inter-integrated circuit](https://en.wikipedia.org/wiki/I%C2%B2C) (I<sup>2</sup>C, I2C, or IIC)
  * Serial data line (SDA)
  * Serial clock line (SCL)
* [1-Wire](https://en.wikipedia.org/wiki/1-Wire)
  * Data input/output (DQ)
* [Light-emitting diode](https://en.wikipedia.org/wiki/Light-emitting_diode) (LED)
  * [LED strip light](https://en.wikipedia.org/wiki/LED_strip_light)
  * [JST connector](https://en.wikipedia.org/wiki/JST_connector)
* [Universal Serial Bus](https://en.wikipedia.org/wiki/USB) (USB)
  * [USB-C](https://en.wikipedia.org/wiki/USB-C)
  * [USB 3.0](https://en.wikipedia.org/wiki/USB_3.0)
  * [USB4](https://en.wikipedia.org/wiki/USB4)
* [Webcam](https://en.wikipedia.org/wiki/Webcam)
* [Microphone](https://en.wikipedia.org/wiki/Microphone)

## Lab 2A:  General-purpose input/output (GPIO) and serial communication

### 1. Open a [GNOME Terminal](https://en.wikipedia.org/wiki/GNOME_Terminal) on macOS/Linux, [Windows Terminal](https://en.wikipedia.org/wiki/Windows_Terminal), or [Git for Windows](https://gitforwindows.org/), run SSH to login Raspberry Pi, and make sure [Raspberry Pi Serial Console](https://elinux.org/RPi_Serial_Connection) is disabled
```sh
$ sudo nano /boot/cmdline.txt
```
* Delete "console=serial0,115200" if found
* Save the file with control-x y enter
```sh
$ sudo reboot
```

### 2. Serial [loopback](https://en.wikipedia.org/wiki/Loopback) test

![serial.png](https://github.com/kevinwlu/iot/blob/master/lesson2/serial.png)

* Connect two serial pins (the 4th and 5th pins from the left of the top row) using one [jump wires](https://en.wikipedia.org/wiki/Jump_wire)
* Run [APT](https://en.wikipedia.org/wiki/APT_(software)) to install [Minicom](https://en.wikipedia.org/wiki/Minicom)
```sh
$ sudo apt update
$ sudo apt install minicom
$ man minicom
$ minicom -b 115200 -o -D /dev/ttyS0
```
* Enable new line
```sh
control-a a
hello
```
* Enable echo
```sh
control-a e
hheelllloo
```
* Exit Minicom
```sh
control-a x
```

### 3. Optionally, perform serial test between two Raspberry Pi's using three jump wire
* Connect TX of a Raspberry Pi to RX of the other Raspberry Pi
* Connect RX of a Raspberry Pi to TX of the other Raspberry Pi
* Connect GND of both Raspberry Pi's
```sh
$ minicom -b 115200 -o -D /dev/ttyS0
```
* Enable new line and echo
```sh
control-a a
control-a e
hello
```
* Exit Minicom
```sh
control-a x
```

## Lab 2B: Serial peripheral interface (SPI)

![spi.png](https://github.com/kevinwlu/iot/blob/master/lesson2/spi.png)

* Connect the SPI MOSI and MISO pins (the 10th and 11th pins from the left of the bottom row) using one jump wire
* Enter the following commands on a Terminal for [spidev-test](https://github.com/torvalds/linux/blob/master/tools/spi/spidev_test.c)
* An alternative [spidev-test](https://github.com/rm-hull/spidev-test)
```sh
$ wget https://raw.githubusercontent.com/raspberrypi/linux/rpi-3.10.y/Documentation/spi/spidev_test.c
$ gcc -o spidev_test spidev_test.c
$ ./spidev_test -D /dev/spidev0.0
spi mode: 0
bits per word: 8
max speed: 500000 Hz (500 KHz)

FF FF FF FF FF FF 
40 00 00 00 00 95 
FF FF FF FF FF FF 
FF FF FF FF FF FF 
FF FF FF FF FF FF 
DE AD BE EF BA AD 
F0 0D 
```
* Remove the jump wire and run spidev_test again
```sh
$ ./spidev_test -D /dev/spidev0.0
spi mode: 4
bits per word: 8
max speed: 500000 Hz (500 KHz)

00 00 00 00 00 00 
00 00 00 00 00 00 
00 00 00 00 00 00 
00 00 00 00 00 00 
00 00 00 00 00 00 
00 00 00 00 00 00 
00 00 
```

## Lab 2C: Breadboard

![breadboard.jpg](https://github.com/kevinwlu/iot/blob/master/lesson2/breadboard.jpg)

### 1. Shorter lead (−) of the LED to a 330-Ω resistor then to Ground, the 3rd pin from the left of the top row

### 2. Longer lead (+) of the LED to GPIO 18, the 6th pin from the left of the top row

![led_bb.png](https://github.com/kevinwlu/iot/blob/master/lesson2/led_bb.png)

## Lab 2D: Light-emitting diode (LED)

### 1. Connect an LED on a breadboard to the Raspberry Pi GPIO using two jump wires as shown in Lab C

### 2. On a Terminal, enter the following commands to switch an LED on/off 
```sh
pi@raspberypi:~ $ sudo su
root@raspberypi:/home/pi# echo 18 > /sys/class/gpio/export
root@raspberypi:/home/pi# cd /sys/class/gpio/gpio18
root@raspberypi:/sys/class/gpio/gpio18# echo out > direction
root@raspberypi:/sys/class/gpio/gpio18# echo 1 > value
root@raspberypi:/sys/class/gpio/gpio18# echo 0 > value
root@raspberypi:/sys/class/gpio/gpio18# cd /home/pi
root@raspberypi:/home/pi# echo 18 > /sys/class/gpio/unexport
root@raspberypi:/home/pi# exit
```

## Lab 2E: Inter-integrated circuit (I2C)

* Test I2C addresses with the preinstalled [i2c-tools](https://i2c.wiki.kernel.org/index.php/I2C_Tools)
* Connect an I2C device [ADXL345](https://learn.adafruit.com/adxl345-digital-accelerometer) (3-axis accelerometer) to 3V3, GND, SDA, and SCL of a Raspberry Pi with two 4.7k&Omega; pull-up resistors

![adxl345_bb.png](https://github.com/kevinwlu/iot/blob/master/lesson2/adxl345_bb.png)

```sh
$ sudo i2cdetect -y 1
   0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- 53 -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- -- 
```
* Connect an I2C device BMP180 or [BMP280](https://learn.adafruit.com/adafruit-bmp280-barometric-pressure-plus-temperature-sensor-breakout) (barometric pressure sensor) to 3V3, GND, SDA, and SCL of a Raspberry Pi

![bmp180_bb.png](https://github.com/kevinwlu/iot/blob/master/lesson2/bmp180_bb.png)

```sh
$ sudo i2cdetect -y 1
   0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- 77 
```

## Lab 2F: 1-Wire

### Connect a [DS18B20](https://www.adafruit.com/product/374) temperature sensor to Raspberry Pi as follows:

[IC power-supply pin](https://en.wikipedia.org/wiki/IC_power-supply_pin) of [BJT](https://en.wikipedia.org/wiki/Bipolar_junction_transistor) (bipolar junction transistor) and [FET](https://en.wikipedia.org/wiki/Field-effect_transistor) (field-effect transistor)
* GND to GND
* VDD to 3.3V or 5V
* DQ to GPIO 4 (the 4th pin from the left of the bottom row) and through a 4.7k&Omega; resistor to VDD

![1-wire_bb.png](https://github.com/kevinwlu/iot/blob/master/lesson2/1-wire_bb.png)

```sh
pi@raspberrypi:~ $ sudo modprobe w1-gpio
pi@raspberrypi:~ $ sudo modprobe w1-therm
pi@raspberrypi:~ $ cd /sys/bus/w1/devices
pi@raspberrypi:/sys/bus/w1/devices $ ls
28-0000064dc293  w1_bus_master1
pi@raspberrypi:/sys/bus/w1/devices $ cd 28*
pi@raspberrypi:/sys/bus/w1/devices/28-0000064dc293 $ cat w1_slave
8f 01 4b 46 7f ff 01 10 14 : crc=14 YES
8f 01 4b 46 7f ff 01 10 14 t=24937
pi@raspberrypi:/sys/bus/w1/devices/28-0000064dc293 $ cd
pi@raspberrypi:~ $ 
```

## Lab 2G: USB Webcam

### Connect a USB webcam to Raspberry Pi, install [fswebcam](https://github.com/fsphil/fswebcam), and save images:
```sh
$ sudo apt update
$ sudo apt install fswebcam
$ fswebcam image.jpg
$ fswebcam -r 1280x720 image2.jpg
$ fswebcam -r 1280x720 --no-banner image3.jpg
```

## Lab 2H: USB Microphone and 3.5-mm Headphones

### Connect a USB microphone and 3.5-mm headphones to Raspberry Pi
```sh
$ man arecord
$ arecord -l
**** List of CAPTURE Hardware Devices ****
card 1: Device [USB PnP Sound Device], device 0: USB Audio [USB Audio]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
$ aplay -l
**** List of PLAYBACK Hardware Devices ****
card 0: Headphones [bcm2835 Headphones], device 0: bcm2835 Headphones [bcm2835 Headphones]
  Subdevices: 8/8
  Subdevice #0: subdevice #0
  Subdevice #1: subdevice #1
  Subdevice #2: subdevice #2
  Subdevice #3: subdevice #3
  Subdevice #4: subdevice #4
  Subdevice #5: subdevice #5
  Subdevice #6: subdevice #6
  Subdevice #7: subdevice #7
$ arecord --device=hw:1,0 --format S16_LE --rate 44100 -c1 test.wav
control-c
$ aplay test.wav
```
