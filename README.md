# LocoBox

The LocoBox software is a set of an Arduino sketch and a Python-based GUI that operates either 5 or 10 circadian entrainment chambers, known as 'LocoBoxes'. 
These chambers control internal lighting with pre-set schedules and monitor general locomotor activities within. 
The GUI is available as a stand-alone executable.


### Prerequisites & Dependencies

1. Original release (pre-2022):

Arduino: Arduino 1.8.7

Python: Python 3.7.0, Pyserial 3.4

RTC library: 

(1) Legacy version: RTC library 'DS1307' (https://github.com/Seeed-Studio/RTC_DS1307/archive/master.zip)

(2) Revision: RTCLib for Adafruit DS3231 Precision RTC (https://github.com/adafruit/RTClib)

The LocoBox (previously called LocomotorBox) GUI has been optimized for Windows, macOS, and Linux (tested on Ubuntu).


2. Current release (2023):

Development was performed on Ubuntu Linux, and some tests were conducted in a virtual Windows environment. The most current versions of Arduino, Python3, and libraries (numpy, pyserial, and RTC) were used, with specific versions to be specified upon release. Online actogram plotting (v2; data from the 5 latest days) and T-cycle entrainment functionality (v3) were included in this release.


### Uploading the Arduino sketch to Arduino Mega 2560

Before using the Python GUI, you will need to upload the Arduino sketch (*.ino) to your Arduino board.


<img width="649" alt="upload" src="https://github.com/JihwanMyung/LocoBox/assets/98081367/e157c039-5f43-4dab-999f-b6cffdc12c9b">


### Current GUI

1. This is how the GUI appears when you start the Python program or run the executable.


<img width="501" alt="init" src="https://github.com/JihwanMyung/LocoBox/assets/98081367/d3b8cde1-d6f5-4169-8e42-da2f27193e68">


2. To start recording:

* Select the Port (e.g., COM1) that is connected to the Arduino.
* Set the suitable initial LED conditions and LED schedule for your experiment.
* The Schedule can be set for a specific Box ('Set Current Box') or replicated to all boxes ('Replicate to All').
* Click 'Set All' (Now, the Schedules tab will be updated with your latest settings).
* Save the current schedule to a JSON file.
* Click 'Recording Start' to begin recording.

Remember to double-check the schedule tab before starting the recording.


<img width="501" alt="schedule" src="https://github.com/JihwanMyung/LocoBox/assets/98081367/a2b42d6f-4441-4123-9518-e36b0bbd4bc3">


While recording, you might want to press the 'Refresh Actogram' button on the lower right to plot the data from the 5 latest days (note that in this figure, the plot was incomplete as there were only 4 data points).

3. The GUI can also be used solely for visualization (while not recording). To visualize a specific data file, please change the filename in the lower left and press 'Refresh Actogram'.


<img width="501" alt="visualization" src="https://github.com/JihwanMyung/LocoBox/assets/98081367/0444b72c-920e-41b7-b6fb-115e02c8900c">


### Installation
Download the Arduino .ino file and the Python3 .py file.
Upload the .ino file to the Arduino microcontroller using Arduino software. Be sure to install the appropriate RTC library.
(In the old version (pre-2022), the Grove - DS1307 RTC library (https://wiki.seeedstudio.com/Grove-RTC/) was used.)

Run the Python GUI by double-clicking the .py file or using the command line with python3.

Note: For a specific version of the software, the necessary .ino and .py files should have matching nomenclature, e.g., BTLocoBox_0001_v1.ino and BTLocoBox_0001_v1.py.


## Deployment

The LocoBox software system requires an Arduino Mega 2560 for controlling either 5 (main release) or 10 boxes (optional, with a custom-made digital slot extension). Each box requires 1 PIR sensor (digital input) and 1 relay switch.


## On-going developments

| Version | New features | Status | Quality Control |
|:----------|:----------|:-------------|:-------------|
|BTLocoBox_0001_v1| (see our publication) | ✔️ | ✔️ |
|BTLocoBox_0002_v2| Online actogram plotting| ✔️ | ✔️ |
|BTLocoBox_0003_v3| T_cycle| ✔️ | X |


## Authors

* Jihwan Myung - initial work and further development
* Vuong Truong - further development on Python GUI interface & online actogram plotting
* Firdani Rianda Putra - reduction to 5-box and extension to 12 phases
* Zow Ormazabal - stabilization and GUI improvement

See BraintimeLab for the official release version.
