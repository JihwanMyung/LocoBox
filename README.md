# LocoBox

LocoBox is a set of Arduino software and GUI interface for running either 5 or 10 LocoBoxes with pre-set schedules.

### Prerequisites & Dependencies

The following Arduino software is used: Arduino 1.8.7

The following Python versions are used: Python 3.7.0, Pyserial 3.4

RTC library: 
(1) Legacy version: RTC library 'DS1307' (https://github.com/Seeed-Studio/RTC_DS1307/archive/master.zip).
(2) Revision: RTCLib for Adafruit DS3231 Precision RTC

The LocomotorBox (LocoBox) GUI interface has been optimized for Windows, macOS, and Linux (tested on Ubuntu).


### Current GUI

![image](https://user-images.githubusercontent.com/7980453/180698333-065a17ca-df0b-4cf6-92d9-6b670a8ae19c.png)



### Installation

Download Arduino .ino file and Python3 .py file. 
Upload .ino to Arduino microcontroller using Arduino software. Be sure to install the appropriate RTC library.

Run Python GUI interface by double-clicking the .py file or on command-line using python3.

## Deployment

This software system requires Arduino Mega 2560 for controlling 10 boxes and a digital slot extension (custom-made). Each box requires 1 PIR sensor (digital input) and 1 relay switch.

## Authors

* Jihwan Myung - initial work and further development
* Vuong Truong - further development on Python GUI interface
* Firdani Rianda - extension to 12 phases
* Zow Ormazabal - stabilization and GUI improvement

See braintimelab for the release version.
