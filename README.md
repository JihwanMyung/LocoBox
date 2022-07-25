# LocoBox

LocoBox is a set of Arduino software and GUI interface for running 10 Locomotor-Boxes with pre-set schedules.

### Prerequisites

The following Arduino software is used: Arduino 1.8.7

The following Python versions are used: Python 3.7.0, Pyserial 3.4

The LocomotorBox (LocoBox) GUI interface has been optimized for Windows, macOS, and Linux (tested on Ubuntu).


### Current GUI

![image](https://user-images.githubusercontent.com/7980453/180698333-065a17ca-df0b-4cf6-92d9-6b670a8ae19c.png)



### Installation

Download Arduino .ino file and Python3 .py file. Upload .ino to Arduino microcontroller using Arduino software. Install Grove - DS1307 RTC library (https://wiki.seeedstudio.com/Grove-RTC/).

Run Python GUI interface by double-clicking the .py file or on command-line using python3.

## Deployment

This software system requires Arduino Mega 2560 for controlling 10 boxes and a digital slot extension (custom-made). Each box requires 1 PIR sensor (digital input) and 1 relay switch.

## Authors

* Jihwan Myung - initial work and further development
* Vuong Truong - further development on Python GUI interface
* Firdani Rianda - extension to 12 phases
* Zow Ormazabal - stabilization and GUI improvement

## Acknowledgments

Yufen (Janice) Huang helped with improving box design. Vuong Truong and Ying-Ling Shen helped with soldering electrical components. Niall Duncan and Tzu-Yu Hsu contributed financially to support initial purchase of boxes and prototyping materials.
This work was supported by Taiwan Ministry of Science and Technology (MOST) grants (107-2311-B-038-001-MY2, 107-2410-H-038-004-MY2).

See braintimelab for main branch.
