# LocoBox

LocoBox is a set of Arduino software and GUI interface for running either 5 or 10 LocoBoxes with pre-set schedules.

### Prerequisites & Dependencies

1. Original release (pre-2022):

Arduino: Arduino 1.8.7

Python: Python 3.7.0, Pyserial 3.4

RTC library: 

(1) Legacy version: RTC library 'DS1307' (https://github.com/Seeed-Studio/RTC_DS1307/archive/master.zip)

(2) Revision: RTCLib for Adafruit DS3231 Precision RTC (https://github.com/adafruit/RTClib)

The LocomotorBox (LocoBox) GUI interface has been optimized for Windows, macOS, and Linux (tested on Ubuntu)


2. Current release (2023):

Development was performed on Ubuntu Linux. Some testes were done on virtual Windows environment.
Arduino, python3, and libraries (numpy, pyserial, and RTC) were the most current ones (to be specified with the release).
Online actogram plotting (data from 5 latest days) was included in this release. 

### Current GUI

This is the GUI when you start the python program.


<img width="451" alt="init" src="https://github.com/JihwanMyung/LocoBox/assets/98081367/eae3cb5b-87e0-49f1-a758-6893ccc00228">



To start recording:
* Select the Port (e.g., COM1) that is connected to the Arduino
* Set the suitable initial LED conditions and LED schedule for your experiment
* The Schedule can be set for specific Box (Set current box) or replicated to all boxes (Replicate to All)
* Set All (Now the Schedules tab will be updated with your latest settings)
* Save the current schedule to a json file
* Recording start 

While doing recording, you might want to press "Refresh actogram" button on the lower right to plot the data from 5 latest days (note that in this figure the plot was incomplete as there were only 4 data points)


<img width="451" alt="day1" src="https://github.com/JihwanMyung/LocoBox/assets/98081367/ded13e36-5050-4573-a809-3a0814b5d635">





Besides, the GUI can also be used for just visualization (while not doing recording). To visualize specific datafile, please change the filename in the lower left, and press "Refresh actogram"


<img width="452" alt="visualization" src="https://github.com/JihwanMyung/LocoBox/assets/98081367/c922aaf8-6b89-4c51-b631-452f7496e979">

### Installation
Download Arduino .ino file and Python3 .py file. 
Upload .ino to Arduino microcontroller using Arduino software. Be sure to install the appropriate RTC library.
(In the old version (pre-2022), Grove - DS1307 RTC library (https://wiki.seeedstudio.com/Grove-RTC/) was used.)

Run Python GUI interface by double-clicking the .py file or on command-line using python3.

Note: For a specific version of the software, the neccesarry .ino and .py files should have matching nomenclature, e.g., BTLocoBox_0001_v1.ino and BTLocoBox_0001_v1.py

## Deployment

This software system requires Arduino Mega 2560 for controlling either 5 (main release) or 10 boxes (optional) and a digital slot extension (custom-made). Each box requires 1 PIR sensor (digital input) and 1 relay switch.

## On-going developments

| Version | New features | Status | Quality Control |
|:----------|:----------|:-------------|:-------------|
|BTLocoBox_0001_v1| (see our publication) | ✔️ | ✔️ |
|BTLocoBox_0002_v2| Online actogram plotting| ✔️ | ✔️ |
|BTLocoBox_0003_v3| T_cycle| X | X |

## Authors

* Jihwan Myung - initial work and further development
* Vuong Truong - further development on Python GUI interface & online actogram plotting
* Firdani Rianda Putra - reduction to 5-box and extension to 12 phases
* Zow Ormazabal - stabilization and GUI improvement

See braintimelab for the official release version.
