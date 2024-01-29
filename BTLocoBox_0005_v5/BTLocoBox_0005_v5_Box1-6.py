import datetime  # For date-time setting and timedelta calculations
import json
#import os
import time  # Required for using delay functions
import tkinter as tk
#from tkinter import * #import INIT set of tkinter library for GUI
import tkinter.scrolledtext as tkscrolled
from cmath import log, phase
from faulthandler import disable
from tkinter import (BOTH, BOTTOM, DISABLED, HORIZONTAL, LEFT, RIGHT, SUNKEN,
                     VERTICAL, Button, Canvas, Entry, Frame, IntVar, Label,
                     Menu, Radiobutton, Scrollbar, Spinbox, StringVar, Tk, W,
                     X, Y, messagebox, ttk)
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk

import matplotlib 
import serial  # For Serial communication
import sys

try:
    from tkinter import filedialog
except ImportError:
    fileDialog = tk.filedialog
import threading  # To run Arduino loop and tkinter loop alongside
import traceback

import numpy as np
import pandas as pd
import serial.tools.list_ports  # For identifying Arduino port
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)


from Actogram import init_plot, plot_doubleplot
from BoxSchedule import (BoxSchedule, PhaseSchedule, getDarkLightValue,
                         inverseDarkLightValue)

matplotlib.use('TkAgg')
#import matplotlib.pyplot as plt

#sudo chmod 666 /dev/ttyACM0


#Actogram reference: https://gist.githubusercontent.com/matham/61c45e66567b07f20840eaea0488767a/raw/04ece1483d963b0361f25959557f4a515417bb8e/actogram.py


# Global variables 1_1 = Box_Phases
global hourOn1_1, minOn1_1, hourOff1_1, minOff1_1, dark1_1, light1_1
global hourOn2_1, minOn2_1, hourOff2_1, minOff2_1, dark2_1, light2_1
global hourOn3_1, minOn3_1, hourOff3_1, minOff3_1, dark3_1, light3_1
global hourOn4_1, minOn4_1, hourOff4_1, minOff4_1, dark4_1, light4_1
global hourOn5_1, minOn5_1, hourOff5_1, minOff5_1, dark5_1, light5_1
global hourOn6_1, minOn6_1, hourOff6_1, minOff6_1, dark6_1, light6_1

global hourOn1_2, minOn1_2, hourOff1_2, minOff1_2, date1_2, month1_2, year1_2, dark1_2, light1_2, hourFrom1_2, minuteFrom1_2
global hourOn2_2, minOn2_2, hourOff2_2, minOff2_2, date2_2, month2_2, year2_2, dark2_2, light2_2, hourFrom2_2, minuteFrom2_2
global hourOn3_2, minOn3_2, hourOff3_2, minOff3_2, date3_2, month3_2, year3_2, dark3_2, light3_2, hourFrom3_2, minuteFrom3_2
global hourOn4_2, minOn4_2, hourOff4_2, minOff4_2, date4_2, month4_2, year4_2, dark4_2, light4_2, hourFrom4_2, minuteFrom4_2
global hourOn5_2, minOn5_2, hourOff5_2, minOff5_2, date5_2, month5_2, year5_2, dark5_2, light5_2, hourFrom5_2, minuteFrom5_2
global hourOn6_2, minOn6_2, hourOff6_2, minOff6_2, date6_2, month6_2, year6_2, dark6_2, light6_2, hourFrom6_2, minuteFrom6_2

global hourOn1_3, minOn1_3, hourOff1_3, minOff1_3, dark1_3, light1_3, date1_3, month1_3, year1_3, hourFrom1_3, minuteFrom1_3
global hourOn2_3, minOn2_3, hourOff2_3, minOff2_3, dark2_3, light2_3, date2_3, month2_3, year2_3, hourFrom2_3, minuteFrom2_3
global hourOn3_3, minOn3_3, hourOff3_3, minOff3_3, dark3_3, light3_3, date3_3, month3_3, year3_3, hourFrom3_3, minuteFrom3_3
global hourOn4_3, minOn4_3, hourOff4_3, minOff4_3, dark4_3, light4_3, date4_3, month4_3, year4_3, hourFrom4_3, minuteFrom4_3
global hourOn5_3, minOn5_3, hourOff5_3, minOff5_3, dark5_3, light5_3, date5_3, month5_3, year5_3, hourFrom5_3, minuteFrom5_3
global hourOn6_3, minOn6_3, hourOff6_3, minOff6_3, dark6_3, light6_3, date6_3, month6_3, year6_3, hourFrom6_3, minuteFrom6_3

global hourOn1_4, minOn1_4, hourOff1_4, minOff1_4, dark1_4, light1_4, date1_4, month1_4, year1_4, hourFrom1_4, minuteFrom1_4
global hourOn2_4, minOn2_4, hourOff2_4, minOff2_4, dark2_4, light2_4, date2_4, month2_4, year2_4, hourFrom2_4, minuteFrom2_4
global hourOn3_4, minOn3_4, hourOff3_4, minOff3_4, dark3_4, light3_4, date3_4, month3_4, year3_4, hourFrom3_4, minuteFrom3_4
global hourOn4_4, minOn4_4, hourOff4_4, minOff4_4, dark4_4, light4_4, date4_4, month4_4, year4_4, hourFrom4_4, minuteFrom4_4
global hourOn5_4, minOn5_4, hourOff5_4, minOff5_4, dark5_4, light5_4, date5_4, month5_4, year5_4, hourFrom5_4, minuteFrom5_4
global hourOn6_4, minOn6_4, hourOff6_4, minOff6_4, dark6_4, light6_4, date6_4, month6_4, year6_4, hourFrom6_4, minuteFrom6_4

global hourOn1_5, minOn1_5, hourOff1_5, minOff1_5, dark1_5, light1_5, date1_5, month1_5, year1_5, hourFrom1_5, minuteFrom1_5
global hourOn2_5, minOn2_5, hourOff2_5, minOff2_5, dark2_5, light2_5, date2_5, month2_5, year2_5, hourFrom2_5, minuteFrom2_5
global hourOn3_5, minOn3_5, hourOff3_5, minOff3_5, dark3_5, light3_5, date3_5, month3_5, year3_5, hourFrom3_5, minuteFrom3_5
global hourOn4_5, minOn4_5, hourOff4_5, minOff4_5, dark4_5, light4_5, date4_5, month4_5, year4_5, hourFrom4_5, minuteFrom4_5
global hourOn5_5, minOn5_5, hourOff5_5, minOff5_5, dark5_5, light5_5, date5_5, month5_5, year5_5, hourFrom5_5, minuteFrom5_5
global hourOn6_5, minOn6_5, hourOff6_5, minOff6_5, dark6_5, light6_5, date6_5, month6_5, year6_5, hourFrom6_5, minuteFrom6_5

global hourOn1_6, minOn1_6, hourOff1_6, minOff1_6, dark1_6, light1_6, date1_6, month1_6, year1_6, hourFrom1_6, minuteFrom1_6
global hourOn2_6, minOn2_6, hourOff2_6, minOff2_6, dark2_6, light2_6, date2_6, month2_6, year2_6, hourFrom2_6, minuteFrom2_6
global hourOn3_6, minOn3_6, hourOff3_6, minOff3_6, dark3_6, light3_6, date3_6, month3_6, year3_6, hourFrom3_6, minuteFrom3_6
global hourOn4_6, minOn4_6, hourOff4_6, minOff4_6, dark4_6, light4_6, date4_6, month4_6, year4_6, hourFrom4_6, minuteFrom4_6
global hourOn5_6, minOn5_6, hourOff5_6, minOff5_6, dark5_6, light5_6, date5_6, month5_6, year5_6, hourFrom5_6, minuteFrom5_6
global hourOn6_6, minOn6_6, hourOff6_6, minOff6_6, dark6_6, light6_6, date6_6, month6_6, year6_6, hourFrom6_6, minuteFrom6_6

global hourOn1_7, minOn1_7, hourOff1_7, minOff1_7, dark1_7, light1_7, date1_7, month1_7, year1_7, hourFrom1_7, minuteFrom1_7
global hourOn2_7, minOn2_7, hourOff2_7, minOff2_7, dark2_7, light2_7, date2_7, month2_7, year2_7, hourFrom2_7, minuteFrom2_7
global hourOn3_7, minOn3_7, hourOff3_7, minOff3_7, dark3_7, light3_7, date3_7, month3_7, year3_7, hourFrom3_7, minuteFrom3_7
global hourOn4_7, minOn4_7, hourOff4_7, minOff4_7, dark4_7, light4_7, date4_7, month4_7, year4_7, hourFrom4_7, minuteFrom4_7
global hourOn5_7, minOn5_7, hourOff5_7, minOff5_7, dark5_7, light5_7, date5_7, month5_7, year5_7, hourFrom5_7, minuteFrom5_7
global hourOn6_7, minOn6_7, hourOff6_7, minOff6_7, dark6_7, light6_7, date6_7, month6_7, year6_7, hourFrom6_7, minuteFrom6_7

global hourOn1_8, minOn1_8, hourOff1_8, minOff1_8, dark1_8, light1_8, date1_8, month1_8, year1_8, hourFrom1_8, minuteFrom1_8
global hourOn2_8, minOn2_8, hourOff2_8, minOff2_8, dark2_8, light2_8, date2_8, month2_8, year2_8, hourFrom2_8, minuteFrom2_8
global hourOn3_8, minOn3_8, hourOff3_8, minOff3_8, dark3_8, light3_8, date3_8, month3_8, year3_8, hourFrom3_8, minuteFrom3_8
global hourOn4_8, minOn4_8, hourOff4_8, minOff4_8, dark4_8, light4_8, date4_8, month4_8, year4_8, hourFrom4_8, minuteFrom4_8
global hourOn5_8, minOn5_8, hourOff5_8, minOff5_8, dark5_8, light5_8, date5_8, month5_8, year5_8, hourFrom5_8, minuteFrom5_8
global hourOn6_8, minOn6_8, hourOff6_8, minOff6_8, dark6_8, light6_8, date6_8, month6_8, year6_8, hourFrom6_8, minuteFrom6_8

global hourOn1_9, minOn1_9, hourOff1_9, minOff1_9, dark1_9, light1_9, date1_9, month1_9, year1_9, hourFrom1_9, minuteFrom1_9
global hourOn2_9, minOn2_9, hourOff2_9, minOff2_9, dark2_9, light2_9, date2_9, month2_9, year2_9, hourFrom2_9, minuteFrom2_9
global hourOn3_9, minOn3_9, hourOff3_9, minOff3_9, dark3_9, light3_9, date3_9, month3_9, year3_9, hourFrom3_9, minuteFrom3_9
global hourOn4_9, minOn4_9, hourOff4_9, minOff4_9, dark4_9, light4_9, date4_9, month4_9, year4_9, hourFrom4_9, minuteFrom4_9
global hourOn5_9, minOn5_9, hourOff5_9, minOff5_9, dark5_9, light5_9, date5_9, month5_9, year5_9, hourFrom5_9, minuteFrom5_9
global hourOn6_9, minOn6_9, hourOff6_9, minOff6_9, dark6_9, light6_9, date6_9, month6_9, year6_9, hourFrom6_9, minuteFrom6_9

global hourOn1_10, minOn1_10, hourOff1_10, minOff1_10, dark1_10, light1_10, date1_10, month1_10, year1_10, hourFrom1_10, minuteFrom1_10
global hourOn2_10, minOn2_10, hourOff2_10, minOff2_10, dark2_10, light2_10, date2_10, month2_10, year2_10, hourFrom2_10, minuteFrom2_10
global hourOn3_10, minOn3_10, hourOff3_10, minOff3_10, dark3_10, light3_10, date3_10, month3_10, year3_10, hourFrom3_10, minuteFrom3_10
global hourOn4_10, minOn4_10, hourOff4_10, minOff4_10, dark4_10, light4_10, date4_10, month4_10, year4_10, hourFrom4_10, minuteFrom4_10
global hourOn5_10, minOn5_10, hourOff5_10, minOff5_10, dark5_10, light5_10, date5_10, month5_10, year5_10, hourFrom5_10, minuteFrom5_10
global hourOn6_10, minOn6_10, hourOff6_10, minOff6_10, dark6_10, light6_10, date6_10, month6_10, year6_10, hourFrom6_10, minuteFrom6_10

global hourOn1_11, minOn1_11, hourOff1_11, minOff1_11, dark1_11, light1_11, date1_11, month1_11, year1_11, hourFrom1_11, minuteFrom1_11
global hourOn2_11, minOn2_11, hourOff2_11, minOff2_11, dark2_11, light2_11, date2_11, month2_11, year2_11, hourFrom2_11, minuteFrom2_11
global hourOn3_11, minOn3_11, hourOff3_11, minOff3_11, dark3_11, light3_11, date3_11, month3_11, year3_11, hourFrom3_11, minuteFrom3_11
global hourOn4_11, minOn4_11, hourOff4_11, minOff4_11, dark4_11, light4_11, date4_11, month4_11, year4_11, hourFrom4_11, minuteFrom4_11
global hourOn5_11, minOn5_11, hourOff5_11, minOff5_11, dark5_11, light5_11, date5_11, month5_11, year5_11, hourFrom5_11, minuteFrom5_11
global hourOn6_11, minOn6_11, hourOff6_11, minOff6_11, dark6_11, light6_11, date6_11, month6_11, year6_11, hourFrom6_11, minuteFrom6_11

global hourOn1_12, minOn1_12, hourOff1_12, minOff1_12, dark1_12, light1_12, date1_12, month1_12, year1_12, hourFrom1_12, minuteFrom1_12
global hourOn2_12, minOn2_12, hourOff2_12, minOff2_12, dark2_12, light2_12, date2_12, month2_12, year2_12, hourFrom2_12, minuteFrom2_12
global hourOn3_12, minOn3_12, hourOff3_12, minOff3_12, dark3_12, light3_12, date3_12, month3_12, year3_12, hourFrom3_12, minuteFrom3_12
global hourOn4_12, minOn4_12, hourOff4_12, minOff4_12, dark4_12, light4_12, date4_12, month4_12, year4_12, hourFrom4_12, minuteFrom4_12
global hourOn5_12, minOn5_12, hourOff5_12, minOff5_12, dark5_12, light5_12, date5_12, month5_12, year5_12, hourFrom5_12, minuteFrom5_12
global hourOn6_12, minOn6_12, hourOff6_12, minOff6_12, dark6_12, light6_12, date6_12, month6_12, year6_12, hourFrom6_12, minuteFrom6_12

global initLED1_str, initLED2_str, initLED3_str, initLED4_str , initLED5_str

global value_mat, phase_delimiters
 
global setBox1, setBox2, setBox3, setBox4, setBox5

global display_string, display_counter

global tcycle_1_1, tcycle_1_2,tcycle_1_3, tcycle_1_4, tcycle_1_5, tcycle_1_6, tcycle_1_7, tcycle_1_8, tcycle_1_9, tcycle_1_10, tcycle_1_11, tcycle_1_12
global tcycle_2_1, tcycle_2_2,tcycle_2_3, tcycle_2_4, tcycle_2_5, tcycle_2_6, tcycle_2_7, tcycle_2_8, tcycle_2_9, tcycle_2_10, tcycle_2_11, tcycle_2_12
global tcycle_3_1, tcycle_3_2,tcycle_3_3, tcycle_3_4, tcycle_3_5, tcycle_3_6, tcycle_3_7, tcycle_3_8, tcycle_3_9, tcycle_3_10, tcycle_3_11, tcycle_3_12
global tcycle_4_1, tcycle_4_2,tcycle_4_3, tcycle_4_4, tcycle_4_5, tcycle_4_6, tcycle_4_7, tcycle_4_8, tcycle_4_9, tcycle_4_10, tcycle_4_11, tcycle_4_12
global tcycle_5_1, tcycle_5_2,tcycle_5_3, tcycle_5_4, tcycle_5_5, tcycle_5_6, tcycle_5_7, tcycle_5_8, tcycle_5_9, tcycle_5_10, tcycle_5_11, tcycle_5_12
global tcycle_6_1, tcycle_6_2,tcycle_6_3, tcycle_6_4, tcycle_6_5, tcycle_6_6, tcycle_6_7, tcycle_6_8, tcycle_6_9, tcycle_6_10, tcycle_6_11, tcycle_6_12


#global savedBoxSchedule, BoxSchedule1, BoxSchedule2, BoxSchedule3, BoxSchedule4, BoxSchedule5

#savedBoxSchedule = BoxSchedule()
phase_delimiters = []
#tcyclefactor = 24
#initLED = 0

# Preset values
setBox1=0
setBox2=0
setBox3=0
setBox4=0
setBox5=0
setBox6=0
display_string = ''
display_counter = 0

# Version information
def about():
    return messagebox.showinfo('About',
                                '6-Box Schedule Setter\n'+
                                'LocoBox.py\n\n'+
                                'Version 4.1\n'+
                                'Dec 27, 2023\n\n'+
                                'Jihwan Myung & Vuong Truong\n'+
                                'Laboratory of Braintime\n\n'+
                                'https://github.com/braintimelab/LocomotorBox')

# Define and create serial object function
def create_serial_obj(portPath, baud_rate, timeout):
    '''
    Given the port path, baud rate, creates
    and returns a pyserial object.
    '''
    return serial.Serial(portPath, baud_rate, timeout=timeout)


###Classes
class StatusBar(Frame): # scan open serial ports
    def __init__(self, master):
        Frame.__init__(self, master)
        self.label = Label(self, bd=1, relief=SUNKEN, anchor=W)
        self.label.pack(fill=X)
    def set(self, format, *args):
        self.label.config(text=format % args)
        self.label.update_idletasks()
    def clear(self):
        self.label.config(text='')
        self.label.update_idletasks()

#Initialize the windows size and name
window = Tk()
window.title('LocoBox (Box1-6)')
if sys.platform.startswith('win'):
    window.geometry('1000x780')
elif sys.platform.startswith('darwin'):
    window.geometry('1200x640')
elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
    window.geometry('900x650')
else:
    window.geometry('1000x440')
status = StatusBar(window)

###Define functions
def destruct(): # Quit the program
    print('LocoBox ended.')
    window.quit()

def get_data(istate=0): # Start recording
    status.pack(side='bottom', fill='x')
    status.set('Starting the recording...')
    #boxrec_text.set('Preparing for recording.')
    
    window.update_idletasks()
    i=istate
    counti=0
    #init csv file and write the COM port name
    headers = port_entry.get()
    filename= filename_entry.get()
    with open(filename,'w', encoding='utf-8') as w:
                w.write(headers+'\n')
    w.close()

    global serial_obj
    global dead
    global value_mat
    global display_string, display_counter, log_mat

    try:
        while True:
            string2 = serial_obj.readline().decode('utf-8')
            
            if string2 != '':
                with open(filename,'a') as w:
                    w.write(string2)
                w.close()

            if i==0:
                print('Synching time...')
                status.pack(side='bottom', fill='x')
                status.set('Synching time...')
                t = datetime.datetime.now()
                t = t + datetime.timedelta(minutes=1)
                serial_obj.write(str.encode(t.strftime('%Y-%m-%d %H:%M:%S')))

            if i==1:

                phase_id = i-1

                serial_obj.write(str.encode(str(initLED1_str) + str(initLED2_str) + str(initLED3_str)+ str(initLED4_str) + str(initLED5_str)+ str(initLED6_str)))

            if i==2:

                serial_obj.write(str.encode(hourOn1_1+minOn1_1+hourOff1_1+minOff1_1+hourOn2_1+minOn2_1+hourOff2_1+minOff2_1+
                                            hourOn3_1+minOn3_1+hourOff3_1+minOff3_1+hourOn4_1+minOn4_1+hourOff4_1+minOff4_1+
                                            hourOn5_1+minOn5_1+hourOff5_1+minOff5_1+hourOn6_1+minOn6_1+hourOff6_1+minOff6_1))
                
            if i==3:    
                serial_obj.write(str.encode(dark1_1+light1_1+dark2_1+light2_1+dark3_1+light3_1+dark4_1+light4_1+
                                            dark5_1+light5_1+dark6_1+light6_1))
                
                status.pack(side='bottom', fill='x')
                status.set('Phase 1 schedules sent.')                              
            if i==4:
                serial_obj.write(str.encode(hourOn1_2+minOn1_2+hourOff1_2+minOff1_2+hourOn2_2+minOn2_2+hourOff2_2+minOff2_2+
                                            hourOn3_2+minOn3_2+hourOff3_2+minOff3_2+hourOn4_2+minOn4_2+hourOff4_2+minOff4_2+
                                            hourOn5_2+minOn5_2+hourOff5_2+minOff5_2+hourOn6_2+minOn6_2+hourOff6_2+minOff6_2))
                
            if i==5:
                serial_obj.write(str.encode(dark1_2+light1_2+dark2_2+light2_2+dark3_2+light3_2+dark4_2+light4_2+
                                            dark5_2+light5_2+dark6_2+light6_2))
                
            if i==6:
                serial_obj.write(str.encode(date1_2+month1_2+year1_2+date2_2+month2_2+year2_2+
                                            date3_2+month3_2+year3_2+date4_2+month4_2+year4_2+
                                            date5_2+month5_2+year5_2+date6_2+month6_2+year6_2))
            if i==7:
                serial_obj.write(str.encode(hourFrom1_2+minuteFrom1_2+hourFrom2_2+minuteFrom2_2+hourFrom3_2+minuteFrom3_2+
                                            hourFrom4_2+minuteFrom4_2+hourFrom5_2+minuteFrom5_2+hourFrom6_2+minuteFrom6_2))
               
                status.pack(side='bottom', fill='x')
                status.set('Phase 2 schedules sent.')    
            if i==8:
                serial_obj.write(str.encode(hourOn1_3+minOn1_3+hourOff1_3+minOff1_3+hourOn2_3+minOn2_3+hourOff2_3+minOff2_3+
                                            hourOn3_3+minOn3_3+hourOff3_3+minOff3_3+hourOn4_3+minOn4_3+hourOff4_3+minOff4_3+
                                            hourOn5_3+minOn5_3+hourOff5_3+minOff5_3+hourOn6_3+minOn6_3+hourOff6_3+minOff6_3))
                
            if i==9:
                serial_obj.write(str.encode(dark1_3+light1_3+dark2_3+light2_3+dark3_3+light3_3+
                                            dark4_3+light4_3+dark5_3+light5_3+dark6_3+light6_3))
                
            if i==10:
                serial_obj.write(str.encode(date1_3+month1_3+year1_3+date2_3+month2_3+year2_3+
                                            date3_3+month3_3+year3_3+date4_3+month4_3+year4_3+
                                            date5_3+month5_3+year5_3+date6_3+month6_3+year6_3))
            if i==11:
                serial_obj.write(str.encode(hourFrom1_3+minuteFrom1_3+hourFrom2_3+minuteFrom2_3+hourFrom3_3+minuteFrom3_3+
                                            hourFrom4_3+minuteFrom4_3+hourFrom5_3+minuteFrom5_3+hourFrom6_3+minuteFrom6_3))
                
                status.pack(side='bottom', fill='x')
                status.set('Phase 3 schedules sent.')
            if i==12:
                serial_obj.write(str.encode(hourOn1_4+minOn1_4+hourOff1_4+minOff1_4+hourOn2_4+minOn2_4+hourOff2_4+minOff2_4+
                                            hourOn3_4+minOn3_4+hourOff3_4+minOff3_4+hourOn4_4+minOn4_4+hourOff4_4+minOff4_4+
                                            hourOn5_4+minOn5_4+hourOff5_4+minOff5_4+ hourOn6_4+minOn6_4+hourOff6_4+minOff6_4))
                
            if i==13:
                serial_obj.write(str.encode(dark1_4+light1_4+dark2_4+light2_4+dark3_4+light3_4+
                                            dark4_4+light4_4+dark5_4+light5_4+dark6_4+light6_4))
                
            if i==14:
                serial_obj.write(str.encode(date1_4+month1_4+year1_4+date2_4+month2_4+year2_4+
                                            date3_4+month3_4+year3_4+date4_4+month4_4+year4_4+
                                            date5_4+month5_4+year5_4+date6_4+month6_4+year6_4))
                
            if i==15:
                serial_obj.write(str.encode(hourFrom1_4+minuteFrom1_4+hourFrom2_4+minuteFrom2_4+hourFrom3_4+minuteFrom3_4+
                                            hourFrom4_4+minuteFrom4_4+hourFrom5_4+minuteFrom5_4+hourFrom6_4+minuteFrom6_4)) 
                
                status.pack(side='bottom', fill='x')
                status.set('Phase 4 schedules sent.')
            if i==16:
                serial_obj.write(str.encode(hourOn1_5+minOn1_5+hourOff1_5+minOff1_5+hourOn2_5+minOn2_5+hourOff2_5+minOff2_5+
                                            hourOn3_5+minOn3_5+hourOff3_5+minOff3_5+hourOn4_5+minOn4_5+hourOff4_5+minOff4_5+
                                            hourOn5_5+minOn5_5+hourOff5_5+minOff5_5+hourOn6_5+minOn6_5+hourOff6_5+minOff6_5))
               
            if i==17: 
                serial_obj.write(str.encode(dark1_5+light1_5+dark2_5+light2_5+dark3_5+light3_5+
                                            dark4_5+light4_5+dark5_5+light5_5+dark6_5+light6_5))
               
            if i==18:
                serial_obj.write(str.encode(date1_5+month1_5+year1_5+date2_5+month2_5+year2_5+
                                            date3_5+month3_5+year3_5+date4_5+month4_5+year4_5+
                                            date5_5+month5_5+year5_5+date6_5+month6_5+year6_5))
                
            if i==19:
                serial_obj.write(str.encode(hourFrom1_5+minuteFrom1_5+hourFrom2_5+minuteFrom2_5+hourFrom3_5+minuteFrom3_5+
                                            hourFrom4_5+minuteFrom4_5+hourFrom5_5+minuteFrom5_5+hourFrom6_5+minuteFrom6_5))
               
                status.pack(side='bottom', fill='x')
                status.set('Phase 5 schedules sent.')
            #Phase 6
            if i==20:
                serial_obj.write(str.encode(hourOn1_6+minOn1_6+hourOff1_6+minOff1_6+hourOn2_6+minOn2_6+hourOff2_6+minOff2_6+
                                            hourOn3_6+minOn3_6+hourOff3_6+minOff3_6+hourOn4_6+minOn4_6+hourOff4_6+minOff4_6+
                                            hourOn5_6+minOn5_6+hourOff5_6+minOff5_6+hourOn6_6+minOn6_6+hourOff6_6+minOff6_6))
                
            if i==21: 
                serial_obj.write(str.encode(dark1_6+light1_6+dark2_6+light2_6+dark3_6+light3_6+
                                            dark4_6+light4_6+dark5_6+light5_6+dark6_6+light6_6))
                
            if i==22:
                serial_obj.write(str.encode(date1_6+month1_6+year1_6+date2_6+month2_6+year2_6+
                                            date3_6+month3_6+year3_6+date4_6+month4_6+year4_6+
                                            date5_6+month5_6+year5_6+date6_6+month6_6+year6_6))
                
            if i==23:
                serial_obj.write(str.encode(hourFrom1_6+minuteFrom1_6+hourFrom2_6+minuteFrom2_6+hourFrom3_6+minuteFrom3_6+
                                            hourFrom4_6+minuteFrom4_6+hourFrom5_6+minuteFrom5_6+hourFrom6_6+minuteFrom6_6))
                status.pack(side='bottom', fill='x')
                status.set('Phase 6 schedules sent.')
            #Phase 7
            if i==24:
                serial_obj.write(str.encode(hourOn1_7+minOn1_7+hourOff1_7+minOff1_7+hourOn2_7+minOn2_7+hourOff2_7+minOff2_7+
                                            hourOn3_7+minOn3_7+hourOff3_7+minOff3_7+hourOn4_7+minOn4_7+hourOff4_7+minOff4_7+
                                            hourOn5_7+minOn5_7+hourOff5_7+minOff5_7+hourOn6_7+minOn6_7+hourOff6_7+minOff6_7))
                
            if i==25: 
                serial_obj.write(str.encode(dark1_7+light1_7+dark2_7+light2_7+dark3_7+light3_7+
                                            dark4_7+light4_7+dark5_7+light5_7+dark6_7+light6_7))
                
            if i==26:
                serial_obj.write(str.encode(date1_7+month1_7+year1_7+date2_7+month2_7+year2_7+
                                            date3_7+month3_7+year3_7+date4_7+month4_7+year4_7+
                                            date5_7+month5_7+year5_7+date6_7+month6_7+year6_7))
                
            if i==27:
                serial_obj.write(str.encode(hourFrom1_7+minuteFrom1_7+hourFrom2_7+minuteFrom2_7+hourFrom3_7+minuteFrom3_7+
                                            hourFrom4_7+minuteFrom4_7+hourFrom5_7+minuteFrom5_7+hourFrom6_7+minuteFrom6_7))
                status.pack(side='bottom', fill='x')
                status.set('Phase 7 schedules sent.')
            #Phase 8
            if i==28:
                serial_obj.write(str.encode(hourOn1_8+minOn1_8+hourOff1_8+minOff1_8+hourOn2_8+minOn2_8+hourOff2_8+minOff2_8+
                                            hourOn3_8+minOn3_8+hourOff3_8+minOff3_8+hourOn4_8+minOn4_8+hourOff4_8+minOff4_8+
                                            hourOn5_8+minOn5_8+hourOff5_8+minOff5_8+hourOn6_8+minOn6_8+hourOff6_8+minOff6_8))
                
            if i==29: 
                serial_obj.write(str.encode(dark1_8+light1_8+dark2_8+light2_8+dark3_8+light3_8+
                                            dark4_8+light4_8+dark5_8+light5_8+dark6_8+light6_8))
                
            if i==30:
                serial_obj.write(str.encode(date1_8+month1_8+year1_8+date2_8+month2_8+year2_8+
                                            date3_8+month3_8+year3_8+date4_8+month4_8+year4_8+
                                            date5_8+month5_8+year5_8+date6_8+month6_8+year6_8))
                
            if i==31:
                serial_obj.write(str.encode(hourFrom1_8+minuteFrom1_8+hourFrom2_8+minuteFrom2_8+hourFrom3_8+minuteFrom3_8+
                                            hourFrom4_8+minuteFrom4_8+hourFrom5_8+minuteFrom5_8+hourFrom6_8+minuteFrom6_8))

                status.pack(side='bottom', fill='x')
                status.set('Phase 8 schedules sent.')
            #Phase 9
            if i==32:
                serial_obj.write(str.encode(hourOn1_9+minOn1_9+hourOff1_9+minOff1_9+hourOn2_9+minOn2_9+hourOff2_9+minOff2_9+
                                            hourOn3_9+minOn3_9+hourOff3_9+minOff3_9+hourOn4_9+minOn4_9+hourOff4_9+minOff4_9+
                                            hourOn5_9+minOn5_9+hourOff5_9+minOff5_9+hourOn6_9+minOn6_9+hourOff6_9+minOff6_9))
                
            if i==33: 
                serial_obj.write(str.encode(dark1_9+light1_9+dark2_9+light2_9+dark3_9+light3_9+
                                            dark4_9+light4_9+dark5_9+light5_9+dark6_9+light6_9))
                
            if i==34:
                serial_obj.write(str.encode(date1_9+month1_9+year1_9+date2_9+month2_9+year2_9+
                                            date3_9+month3_9+year3_9+date4_9+month4_9+year4_9+
                                            date5_9+month5_9+year5_9+date6_9+month6_9+year6_9))
                
            if i==35:
                serial_obj.write(str.encode(hourFrom1_9+minuteFrom1_9+hourFrom2_9+minuteFrom2_9+hourFrom3_9+minuteFrom3_9+
                                            hourFrom4_9+minuteFrom4_9+hourFrom5_9+minuteFrom5_9+hourFrom6_9+minuteFrom6_9))

                status.pack(side='bottom', fill='x')
                status.set('Phase 9 schedules sent.')
            #Phase 10
            if i==36:
                serial_obj.write(str.encode(hourOn1_10+minOn1_10+hourOff1_10+minOff1_10+hourOn2_10+minOn2_10+hourOff2_10+minOff2_10+
                                            hourOn3_10+minOn3_10+hourOff3_10+minOff3_10+hourOn4_10+minOn4_10+hourOff4_10+minOff4_10+
                                            hourOn5_10+minOn5_10+hourOff5_10+minOff5_10+hourOn6_10+minOn6_10+hourOff6_10+minOff6_10))
                
            if i==37: 
                serial_obj.write(str.encode(dark1_10+light1_10+dark2_10+light2_10+dark3_10+light3_10+
                                            dark4_10+light4_10+dark5_10+light5_10+dark6_10+light6_10))
                
            if i==38:
                serial_obj.write(str.encode(date1_10+month1_10+year1_10+date2_10+month2_10+year2_10+
                                            date3_10+month3_10+year3_10+date4_10+month4_10+year4_10+
                                            date5_10+month5_10+year5_10+date6_10+month6_10+year6_10))
                
            if i==39:
                serial_obj.write(str.encode(hourFrom1_10+minuteFrom1_10+hourFrom2_10+minuteFrom2_10+hourFrom3_10+minuteFrom3_10+
                                            hourFrom4_10+minuteFrom4_10+hourFrom5_10+minuteFrom5_10+hourFrom6_10+minuteFrom6_10))

                status.pack(side='bottom', fill='x')
                status.set('Phase 10 schedules sent.')
            #Phase 11
            if i==40:
                serial_obj.write(str.encode(hourOn1_11+minOn1_11+hourOff1_11+minOff1_11+hourOn2_11+minOn2_11+hourOff2_11+minOff2_11+
                                            hourOn3_11+minOn3_11+hourOff3_11+minOff3_11+hourOn4_11+minOn4_11+hourOff4_11+minOff4_11+
                                            hourOn5_11+minOn5_11+hourOff5_11+minOff5_11+hourOn6_11+minOn6_11+hourOff6_11+minOff6_11))
                
            if i==41: 
                serial_obj.write(str.encode(dark1_11+light1_11+dark2_11+light2_11+dark3_11+light3_11+
                                            dark4_11+light4_11+dark5_11+light5_11+dark6_11+light6_11))
                
            if i==42:

                serial_obj.write(str.encode(date1_11+month1_11+year1_11+
                                            date2_11+month2_11+year2_11+
                                            date3_11+month3_11+year3_11+
                                            date4_11+month4_11+year4_11+
                                            date5_11+month5_11+year5_11+
                                            date6_11+month6_11+year6_11))
                
            if i==43:

                serial_obj.write(str.encode(hourFrom1_11+minuteFrom1_11+
                                            hourFrom2_11+minuteFrom2_11+
                                            hourFrom3_11+minuteFrom3_11+
                                            hourFrom4_11+minuteFrom4_11+
                                            hourFrom5_11+minuteFrom5_11+
                                            hourFrom6_11+minuteFrom6_11))


                status.pack(side='bottom', fill='x')
                status.set('Phase 11 schedules sent.')

            #Phase 12
            if i==44:
                serial_obj.write(str.encode(hourOn1_12+minOn1_12+hourOff1_12+minOff1_12+hourOn2_12+minOn2_12+hourOff2_12+minOff2_12+
                                            hourOn3_12+minOn3_12+hourOff3_12+minOff3_12+hourOn4_12+minOn4_12+hourOff4_12+minOff4_12+
                                            hourOn5_12+minOn5_12+hourOff5_12+minOff5_12+hourOn6_12+minOn6_12+hourOff6_12+minOff6_12))
                
            if i==45: 
                serial_obj.write(str.encode(dark1_12+light1_12+dark2_12+light2_12+dark3_12+light3_12+
                                            dark4_12+light4_12+dark5_12+light5_12+dark6_12+light6_12))
                
            if i==46:
                serial_obj.write(str.encode(date1_12+month1_12+year1_12+date2_12+month2_12+year2_12+
                                            date3_12+month3_12+year3_12+date4_12+month4_12+year4_12+
                                            date5_12+month5_12+year5_12+date6_12+month6_12+year6_12))
                
            if i==47:
                serial_obj.write(str.encode(hourFrom1_12+minuteFrom1_12+hourFrom2_12+minuteFrom2_12+hourFrom3_12+minuteFrom3_12+
                                            hourFrom4_12+minuteFrom4_12+hourFrom5_12+minuteFrom5_12+hourFrom6_12+minuteFrom6_12))

                status.pack(side='bottom', fill='x')
                status.set('Phase 12 schedules sent.')
                
            if i==48:
                serial_obj.write(str.encode(tcycle_1_1 + tcycle_1_2 +tcycle_1_3 + tcycle_1_4 + tcycle_1_5 + tcycle_1_6 + tcycle_1_7 + tcycle_1_8 + tcycle_1_9 + tcycle_1_10 + tcycle_1_11 + tcycle_1_12 +
                                            tcycle_2_1 + tcycle_2_2 +tcycle_2_3 + tcycle_2_4 + tcycle_2_5 + tcycle_2_6))
                                            
            if i==49:
                serial_obj.write(str.encode(tcycle_2_7 + tcycle_2_8 + tcycle_2_9 + tcycle_2_10 + tcycle_2_11 + tcycle_2_12 +
                                            tcycle_3_1 + tcycle_3_2 +tcycle_3_3 + tcycle_3_4 + tcycle_3_5 + tcycle_3_6 +tcycle_3_7 + tcycle_3_8 + tcycle_3_9 + tcycle_3_10 + tcycle_3_11 + tcycle_3_12))
                
            if i==50:
                serial_obj.write(str.encode(tcycle_4_1 + tcycle_4_2 +tcycle_4_3 + tcycle_4_4 + tcycle_4_5 + tcycle_4_6 + tcycle_4_7 + tcycle_4_8 + tcycle_4_9 + tcycle_4_10 + tcycle_4_11 + tcycle_4_12 + 
                                            tcycle_5_1 + tcycle_5_2 +tcycle_5_3 + tcycle_5_4 + tcycle_5_5 + tcycle_5_6))
            if i==51:
                serial_obj.write(str.encode(tcycle_5_7 + tcycle_5_8 + tcycle_5_9 + tcycle_5_10 + tcycle_5_11 + tcycle_5_12 +
                                            tcycle_6_1 + tcycle_6_2 +tcycle_6_3 + tcycle_6_4 + tcycle_6_5 + tcycle_6_6 + tcycle_6_7 + tcycle_6_8 + tcycle_6_9 + tcycle_6_10 + tcycle_6_11 + tcycle_6_12))
                
                status.pack(side='bottom', fill='x')
                status.set('T-cycle schedules sent.')

            if i==52:
                serial_obj.write(str.encode(DIn1 + DIn2 + DIn3 + DIn4 + DIn5 + DIn6 +
                                            DOut1 + DOut2 +DOut3 + DOut4 + DOut5 + DOut6 + anIn1 + anIn2 + anIn3 + anIn4 + anIn5 + anIn6))
                
                status.pack(side='bottom', fill='x')
                status.set('PinMode sent.')
                
                status.set('All schedules transferred. Recording began.')
                
                window.update_idletasks()
            i=i+1

            #print(string2)
            
            if len(string2)>=79:     #set the id according to current tab


                print(string2)

                display_string = string2
                display_counter = counti
                save_logs(counti, string2) 
                on_tab_change(counti, string2)
                #get_values_for_actogram()
                window.update_idletasks()
             
                counti = counti+1

    except Exception:
        traceback.print_exc() 

        print('Stopped recording and disconnected from the boxes.')
        status.pack(side='bottom', fill='x')
        status.set('Stopped recording and disconnected from the boxes.') 
       
        
        window.update_idletasks()

def display_as_ON_OFF(led_value):
    led_value = str(led_value)
    if led_value == '00000':
        return 'OFF'
    elif led_value == '00001':
        return 'ON'
    else:
        return led_value

def display_LD(box_id, phase_id):
    global value_mat, input_mat
    var = input_mat[box_id, phase_id, 4].get()
    if var == 2:
        return "DD"
    elif var == 3:
        return "LL"
    else:
        return "LD"

def save_logs( counti, string2): #max 120 timepoints 
    global log_mat
    
    log_mat[counti % 120, 0] = counti
    log_mat[counti % 120, 1] = string2[0:8]
    log_mat[counti % 120, 2] = string2[20:25]
    log_mat[counti % 120, 3] = string2[26:31]
    log_mat[counti % 120, 4] = string2[32:37]
    log_mat[counti % 120, 5] = string2[38:43]
    log_mat[counti % 120, 6] = string2[44:49]
    log_mat[counti % 120, 7] = string2[50:55]
    log_mat[counti % 120, 8] = string2[56:61]
    log_mat[counti % 120, 9] = string2[62:67]
    log_mat[counti % 120, 10] = string2[68:73]
    log_mat[counti % 120, 11] = string2[74:79]
    #print(log_mat)


def get_values_for_actogram():
    tab = int(tab_control.index('current'))+1
    filename = './' + filename_entry.get()
    box = 'BOX' + str(tab)
    pir = 'PIR0'  + str(tab)
    led = 'LED0'   + str(tab)
    plot_doubleplot(box, pir, led, filename)
    # print(filename)
    # print(pir)
    plot_double_acto(tab)

def plot_double_acto(tab):
    
    global label_acto
    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open("./BOX" + str(tab) + ".png"))
    label_acto.configure(image=img)
    label_acto.image = img

def refresh_plot():
    global t_acto
    print("refreshing plot")
    t_acto = threading.Thread(target=get_values_for_actogram())
    t_acto.daemon = True
    t_acto.start()
    t_acto.join()


def set_log_text(log_text, log_mat, tab):

    phase_id = 0

    
    history_str = ''
    for counti in range(0,120): #check if I can get rid of the loop
        
        if tab == 1 or tab == 'Box1' :

            phase_id = get_phase(1)
            
            if str(log_mat[counti % 120,1]).strip() != '':
                history_str =  '# '+str(log_mat[counti % 120,0])+'   ' + display_LD(tab-1, phase_id-1) +'   Phase: ' + str(phase_id) +'    Time: '+str(log_mat[counti % 120,1])+'    LED: '+ display_as_ON_OFF(str(log_mat[counti % 120,2]))+'    '+'PIR: '+str(log_mat[counti % 120,3]) + "\n"
        elif tab == 2 or tab == 'Box2':
            phase_id = get_phase(2)
            if str(log_mat[counti % 120,1]).strip() != '':
                history_str = '# '+str(log_mat[counti % 120,0])+'   ' + display_LD(tab-1, phase_id-1) + '   Phase: ' + str(phase_id) +'    Time: '+str(log_mat[counti % 120,1])+'    LED: '+display_as_ON_OFF(str(log_mat[counti % 120,4]))+'    '+'PIR: '+str(log_mat[counti % 120,5]) + "\n"

        elif tab == 3 or tab == 'Box3':
            phase_id = get_phase(3)
            if str(log_mat[counti % 120,1]).strip() != '':
                history_str =  '# '+str(log_mat[counti % 120,0])+'   ' + display_LD(tab-1, phase_id-1) + '   Phase: ' + str(phase_id) +'    Time: '+str(log_mat[counti % 120,1])+'    LED: '+display_as_ON_OFF(str(log_mat[counti % 120,6]))+'    '+'PIR: '+str(log_mat[counti % 120,7]) + "\n"
                
        elif tab == 4 or tab == 'Box4':
            phase_id = get_phase(4)
            if str(log_mat[counti % 120,1]).strip() != '':
                history_str = '# '+str(log_mat[counti % 120,0])+'   ' + display_LD(tab-1, phase_id-1) + '   Phase: ' + str(phase_id) +'    Time: '+str(log_mat[counti % 120,1])+'    LED: '+display_as_ON_OFF(str(log_mat[counti % 120,8]))+'    '+'PIR: '+str(log_mat[counti % 120,9]) + "\n"
        elif tab == 5 or tab == 'Box5':
            phase_id = get_phase(5)
            if str(log_mat[counti % 120,1]).strip() != '':
                history_str =  '# '+str(log_mat[counti % 120,0])+'   ' + display_LD(tab-1, phase_id-1) +'   Phase: ' + str(phase_id) +'    Time: '+str(log_mat[counti % 120,1])+'    LED: '+display_as_ON_OFF(str(log_mat[counti % 120,10]))+'    '+'PIR: '+str(log_mat[counti % 120,11]) + "\n"
        elif tab == 6 or tab == 'Box6':
            phase_id = get_phase(6)
            if str(log_mat[counti % 120,1]).strip() != '':
                history_str =  '# '+str(log_mat[counti % 120,0])+'   ' + display_LD(tab-1, phase_id-1) +'   Phase: ' + str(phase_id) +'    Time: '+str(log_mat[counti % 120,1])+'    LED: '+display_as_ON_OFF(str(log_mat[counti % 120,10]))+'    '+'PIR: '+str(log_mat[counti % 120,11]) + "\n"



    #print(history_str)
    log_text.set(history_str)
    log_display.config(state="normal")
    #log_display.delete('1.0','end')
    log_display.insert(tk.END, history_str)
    log_display.config(state="disabled")

def restore_history(log_text, log_mat, tab):
    history_str = ''
    for counti in range(0,120):
        
        if tab == 1 or tab == 'Box1' :

            phase_id = get_phase(1)
            
            if str(log_mat[counti % 120,1]).strip() != '':
                history_str =  history_str + '# '+str(log_mat[counti % 120,0])+ '   ' + display_LD(0, phase_id-1) +'   Phase: ' + str(phase_id) +'    Time: '+str(log_mat[counti % 120,1])+'    LED: '+display_as_ON_OFF(str(log_mat[counti % 120,2]))+'    '+'PIR: '+str(log_mat[counti % 120,3]) + "\n"
        elif tab == 2 or tab == 'Box2':
            phase_id = get_phase(2)
            if str(log_mat[counti % 120,1]).strip() != '':
                history_str = history_str +'# '+str(log_mat[counti % 120,0])+'   ' +display_LD(1, phase_id-1) +'  Phase: ' + str(phase_id) +'    Time: '+str(log_mat[counti % 120,1])+'    LED: '+display_as_ON_OFF(str(log_mat[counti % 120,4]))+'    '+'PIR: '+str(log_mat[counti % 120,5]) + "\n"

        elif tab == 3 or tab == 'Box3':
            phase_id = get_phase(3)
            if str(log_mat[counti % 120,1]).strip() != '':
                history_str = history_str + '# '+str(log_mat[counti % 120,0])+'   ' +display_LD(2, phase_id-1) +'   Phase: ' + str(phase_id) +'    Time: '+str(log_mat[counti % 120,1])+'    LED: '+display_as_ON_OFF(str(log_mat[counti % 120,6]))+'    '+'PIR: '+str(log_mat[counti % 120,7]) + "\n"
                
        elif tab == 4 or tab == 'Box4':
            phase_id = get_phase(4)
            if str(log_mat[counti % 120,1]).strip() != '':
                history_str = history_str + '# '+str(log_mat[counti % 120,0])+'   ' +display_LD(3, phase_id-1) +'   Phase: ' + str(phase_id) +'    Time: '+str(log_mat[counti % 120,1])+'    LED: '+display_as_ON_OFF(str(log_mat[counti % 120,8]))+'    '+'PIR: '+str(log_mat[counti % 120,9]) + "\n"
        elif tab == 5 or tab == 'Box5':
            phase_id = get_phase(5)
            if str(log_mat[counti % 120,1]).strip() != '':
                history_str = history_str + '# '+str(log_mat[counti % 120,0])+'   ' +display_LD(4, phase_id-1) +'   Phase: ' + str(phase_id) +'    Time: '+str(log_mat[counti % 120,1])+'    LED: '+display_as_ON_OFF(str(log_mat[counti % 120,10]))+'    '+'PIR: '+str(log_mat[counti % 120,11]) + "\n"
        elif tab == 6 or tab == 'Box6':
            phase_id = get_phase(5)
            if str(log_mat[counti % 120,1]).strip() != '':
                history_str = history_str + '# '+str(log_mat[counti % 120,0])+'   ' +display_LD(5, phase_id-1) +'   Phase: ' + str(phase_id) +'    Time: '+str(log_mat[counti % 120,1])+'    LED: '+display_as_ON_OFF(str(log_mat[counti % 120,10]))+'    '+'PIR: '+str(log_mat[counti % 120,11]) + "\n"


    log_text.set(history_str)
    log_display.config(state="normal")
    #log_display.delete('1.0','end')
    log_display.insert(tk.END, history_str)
    log_display.config(state="disabled")



def on_tab_change( counti, string2):
    tab = int(tab_control.index('current'))+1
    #tab = event.widget.tab('current')['text']
    # if tab == 1:

    #     phase_id = get_phase(1)
    #     #boxrec_text.set('# '+str(counti)+'     Phase: ' + str(phase_id) +'    Time: '+string2[0:8]+'    LED1: '+string2[20:25]+'    '+'PIR1: '+string2[26:31])
    #     #log_text.set('# '+str(log_mat[counti % 120,0])+'    Time: '+str(log_mat[counti % 120,1])+'    LED: '+str(log_mat[counti % 120,2])+'    '+'PIR: '+str(log_mat[counti % 120,3]))
    # elif tab == 2:
    #     phase_id = get_phase(2)
    #     #boxrec_text.set('# '+str(counti)+'     Phase: ' + str(phase_id) + '    Time: '+string2[0:8]+'    LED2: '+string2[32:37]+'    '+'PIR2: '+string2[38:43])
    #     #log_text.set('# '+str(log_mat[counti % 120,0])+'    Time: '+str(log_mat[counti % 120,1])+'    LED: '+str(log_mat[counti % 120,4])+'    '+'PIR: '+str(log_mat[counti % 120,5]))

    # elif tab == 3:
    #     phase_id = get_phase(3)
    #     #boxrec_text.set('# '+str(counti)+'     Phase: ' + str(phase_id) + '    Time: '+string2[0:8]+'    LED3: '+string2[44:49]+'    '+'PIR3: '+string2[50:55])
    #     #log_text.set('# '+str(log_mat[counti % 120,0])+'    Time: '+str(log_mat[counti % 120,1])+'    LED: '+str(log_mat[counti % 120,6])+'    '+'PIR: '+str(log_mat[counti % 120,7]))
               
    # elif tab == 4:
    #     phase_id = get_phase(4)
    #     #boxrec_text.set('# '+str(counti)+'     Phase: ' + str(phase_id) + '    Time: '+string2[0:8]+'    LED4: '+string2[56:61]+'    '+'PIR4: '+string2[62:67])
    #     #log_text.set('# '+str(log_mat[counti % 120,0])+'    Time: '+str(log_mat[counti % 120,1])+'    LED: '+str(log_mat[counti % 120,8])+'    '+'PIR: '+str(log_mat[counti % 120,9]))
    # elif tab == 5:
    #     phase_id = get_phase(5)
    #     #boxrec_text.set('# '+str(counti)+'     Phase: ' + str(phase_id) + '    Time: '+string2[0:8]+'    LED5: '+string2[68:73]+'    '+'PIR5: '+string2[74:79])

    #     #log_text.set('# '+str(log_mat[counti % 120,0])+'    Time: '+str(log_mat[counti % 120,1])+'    LED: '+str(log_mat[counti % 120,10])+'    '+'PIR: '+str(log_mat[counti % 120,11]))
    # #log_display.config(state="normal")
    # #log_display.delete('1.0','end')
    set_log_text(log_text, log_mat, tab)

def on_tab_change_trigger( event):
    global display_counter, display_string
    #tab = int(tab_control.index('current'))+1
    # counti = display_counter
    # string2 = display_string
    
    tab = event.widget.tab('current')['text']
    
    # if tab == 'Box1':
    #     phase_id = get_phase(1)
    #     #boxrec_text.set('# '+str(counti)+'     Phase: ' + str(phase_id) + '    Time: '+string2[0:8]+'    LED1: '+string2[20:25]+'    '+'PIR1: '+string2[26:31])
    #     #log_text.set('# '+str(log_mat[counti % 120,0])+'    Time: '+str(log_mat[counti % 120,1])+'    LED: '+str(log_mat[counti % 120,2])+'    '+'PIR: '+str(log_mat[counti % 120,3]))
        
    # elif tab == 'Box2':
    #     phase_id = get_phase(2)
    #     #boxrec_text.set('# '+str(counti)+'     Phase: ' + str(phase_id) + '    Time: '+string2[0:8]+'    LED2: '+string2[32:37]+'    '+'PIR2: '+string2[38:43])

    #     #log_text.set('# '+str(log_mat[counti % 120,0])+'    Time: '+str(log_mat[counti % 120,1])+'    LED: '+str(log_mat[counti % 120,4])+'    '+'PIR: '+str(log_mat[counti % 120,5]))
        

    # elif tab == 'Box3':

    #     phase_id = get_phase(3)
    #     #boxrec_text.set('# '+str(counti)+'     Phase: ' + str(phase_id) + '    Time: '+string2[0:8]+'    LED3: '+string2[44:49]+'    '+'PIR3: '+string2[50:55])

    # elif tab == 'Box4':

    #     phase_id = get_phase(4)
    #     #boxrec_text.set('# '+str(counti)+'     Phase: ' + str(phase_id) + '    Time: '+string2[0:8]+'    LED4: '+string2[56:61]+'    '+'PIR4: '+string2[62:67])
    #     #log_text.set('# '+str(log_mat[counti % 120,0])+'    Time: '+str(log_mat[counti % 120,1])+'    LED: '+str(log_mat[counti % 120,8])+'    '+'PIR: '+str(log_mat[counti % 120,9]))
    # elif tab == 'Box5':
    #     phase_id = get_phase(5)
    #     #boxrec_text.set('# '+str(counti)+'     Phase: ' + str(phase_id) + '    Time: '+string2[0:8]+'    LED5: '+string2[68:73]+'    '+'PIR5: '+string2[74:79])

    #     #log_text.set('# '+str(log_mat[counti % 120,0])+'    Time: '+str(log_mat[counti % 120,1])+'    LED: '+str(log_mat[counti % 120,10])+'    '+'PIR: '+str(log_mat[counti % 120,11]))
    log_display.config(state="normal")
    log_display.delete('1.0','end')
    restore_history(log_text, log_mat, tab)
    #get_values_for_actogram()


def time_in_range(start, end, current):
    """Returns whether current is in the range [start, end]"""
    return start <= current <= end

def DarkenLabel(label):
    label.config(bg="darkgray")

def get_phase(box_id):
    global value_mat, phase_delimiters

    box_id = box_id-1
    #print(value_mat)
    if len(phase_delimiters) == 0:
        
        return 1
    
    for phase_id in range(0,12):
        #start = datetime.datetime(year=int(value_mat[box_id, phase_id, 8]), month=int(value_mat[box_id, phase_id, 7]), day=int(value_mat[box_id, phase_id, 6]), hour=int(value_mat[box_id, phase_id, 9]), minute= int(value_mat[box_id, phase_id, 10]))
        #end = datetime.datetime(year=int(value_mat[box_id, phase_id +1, 8]), month=int(value_mat[box_id, phase_id+1, 7]), day=int(value_mat[box_id, phase_id+1, 6]), hour=int(value_mat[box_id, phase_id+1, 9]), minute= int(value_mat[box_id, phase_id+1, 10]))
        start = phase_delimiters[phase_id]
        end = phase_delimiters[phase_id +1]
        current = datetime.datetime.now()
        
        #print(start)
        #print(current)
        #print(end)

        if start >= current:
            print(phase_id)
            return 1
            
            
        if current < end:
            return phase_id + 1

        if current > end:
            continue

        if phase_id == 11:
            return 11 +1


def writeToJSONFile(filename, data):
    filePathNameWExt = filename
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

def save_conf(): # Save schedule configuration
    global value_mat
    status.pack(side='bottom', fill='x')
    status.set('Saving the schedule configuration...')
    config={}
    config['hourOn1_1'] = hourOn1_1
    config['minOn1_1'] = minOn1_1
    config['hourOff1_1'] = hourOff1_1
    config['minOff1_1'] = minOff1_1
    config['hourOn2_1'] = hourOn2_1
    config['minOn2_1'] = minOn2_1
    config['hourOff2_1'] = hourOff2_1
    config['minOff2_1'] = minOff2_1
    config['hourOn3_1'] = hourOn3_1
    config['minOn3_1'] = minOn3_1
    config['hourOff3_1'] = hourOff3_1
    config['minOff3_1'] = minOff3_1
    config['hourOn4_1'] = hourOn4_1
    config['minOn4_1'] = minOn4_1
    config['hourOff4_1'] = hourOff4_1
    config['minOff4_1'] = minOff4_1
    config['hourOn5_1'] = hourOn5_1
    config['minOn5_1'] = minOn5_1
    config['hourOff5_1'] = hourOff5_1
    config['minOff5_1'] = minOff5_1
    config['hourOn6_1'] = hourOn6_1
    config['minOn6_1'] = minOn6_1
    config['hourOff6_1'] = hourOff6_1
    config['minOff6_1'] = minOff6_1

    
    config['dark1_1'] = dark1_1
    config['light1_1'] = light1_1
    config['dark2_1'] = dark2_1
    config['light2_1'] = light2_1
    config['dark3_1'] = dark3_1
    config['light3_1'] = light3_1
    config['dark4_1'] = dark4_1
    config['light4_1'] = light4_1
    config['dark5_1'] = dark5_1
    config['light5_1'] = light5_1
    config['dark6_1'] = dark6_1
    config['light6_1'] = light6_1
    
    config['hourOn1_2'] = hourOn1_2
    config['minOn1_2'] = minOn1_2
    config['hourOff1_2'] = hourOff1_2
    config['minOff1_2'] = minOff1_2
    config['hourOn2_2'] = hourOn2_2
    config['minOn2_2'] = minOn2_2
    config['hourOff2_2'] = hourOff2_2
    config['minOff2_2'] = minOff2_2
    config['hourOn3_2'] = hourOn3_2
    config['minOn3_2'] = minOn3_2
    config['hourOff3_2'] = hourOff3_2
    config['minOff3_2'] = minOff3_2
    config['hourOn4_2'] = hourOn4_2
    config['minOn4_2'] = minOn4_2
    config['hourOff4_2'] = hourOff4_2
    config['minOff4_2'] = minOff4_2
    config['hourOn5_2'] = hourOn5_2
    config['minOn5_2'] = minOn5_2
    config['hourOff5_2'] = hourOff5_2
    config['minOff5_2'] = minOff5_2
    config['hourOn6_2'] = hourOn6_2
    config['minOn6_2'] = minOn6_2
    config['hourOff6_2'] = hourOff6_2
    config['minOff6_2'] = minOff6_2
    
    config['dark1_2'] = dark1_2
    config['light1_2'] = light1_2
    config['dark2_2'] = dark2_2
    config['light2_2'] = light2_2
    config['dark3_2'] = dark3_2
    config['light3_2'] = light3_2
    config['dark4_2'] = dark4_2
    config['light4_2'] = light4_2
    config['dark5_2'] = dark5_2
    config['light5_2'] = light5_2
    config['dark6_2'] = dark6_2
    config['light6_2'] = light6_2
    
    config['date1_2'] = date1_2
    config['month1_2'] = month1_2
    config['year1_2'] = year1_2
    config['date2_2'] = date2_2
    config['month2_2'] = month2_2
    config['year2_2'] = year2_2
    config['date3_2'] = date3_2
    config['month3_2'] = month3_2
    config['year3_2'] = year3_2
    config['date4_2'] = date4_2
    config['month4_2'] = month4_2
    config['year4_2'] = year4_2
    config['date5_2'] = date5_2
    config['month5_2'] = month5_2
    config['year5_2'] = year5_2
    config['date6_2'] = date6_2
    config['month6_2'] = month6_2
    config['year6_2'] = year6_2

    config['hourFrom1_2'] = hourFrom1_2
    config['minuteFrom1_2'] = minuteFrom1_2
    config['hourFrom2_2'] = hourFrom2_2
    config['minuteFrom2_2'] = minuteFrom2_2
    config['hourFrom3_2'] = hourFrom3_2
    config['minuteFrom3_2'] = minuteFrom3_2
    config['hourFrom4_2'] = hourFrom4_2
    config['minuteFrom4_2'] = minuteFrom4_2
    config['hourFrom5_2'] = hourFrom5_2
    config['minuteFrom5_2'] = minuteFrom5_2
    config['hourFrom6_2'] = hourFrom6_2
    config['minuteFrom6_2'] = minuteFrom6_2
    
    config['hourOn1_3'] = hourOn1_3
    config['minOn1_3'] = minOn1_3
    config['hourOff1_3'] = hourOff1_3
    config['minOff1_3'] = minOff1_3
    config['hourOn2_3'] = hourOn2_3
    config['minOn2_3'] = minOn2_3
    config['hourOff2_3'] = hourOff2_3
    config['minOff2_3'] = minOff2_3
    config['hourOn3_3'] = hourOn3_3
    config['minOn3_3'] = minOn3_3
    config['hourOff3_3'] = hourOff3_3
    config['minOff3_3'] = minOff3_3
    config['hourOn4_3'] = hourOn4_3
    config['minOn4_3'] = minOn4_3
    config['hourOff4_3'] = hourOff4_3
    config['minOff4_3'] = minOff4_3
    config['hourOn5_3'] = hourOn5_3
    config['minOn5_3'] = minOn5_3
    config['hourOff5_3'] = hourOff5_3
    config['minOff5_3'] = minOff5_3
    config['hourOn6_3'] = hourOn6_3
    config['minOn6_3'] = minOn6_3
    config['hourOff6_3'] = hourOff6_3
    config['minOff6_3'] = minOff6_3
    
    config['dark1_3'] = dark1_3
    config['light1_3'] = light1_3
    config['dark2_3'] = dark2_3
    config['light2_3'] = light2_3
    config['dark3_3'] = dark3_3
    config['light3_3'] = light3_3
    config['dark4_3'] = dark4_3
    config['light4_3'] = light4_3
    config['dark5_3'] = dark5_3
    config['light5_3'] = light5_3
    config['dark6_3'] = dark6_3
    config['light6_3'] = light6_3
    
    config['date1_3'] = date1_3
    config['month1_3'] = month1_3
    config['year1_3'] = year1_3
    config['date2_3'] = date2_3
    config['month2_3'] = month2_3
    config['year2_3'] = year2_3
    config['date3_3'] = date3_3
    config['month3_3'] = month3_3
    config['year3_3'] = year3_3
    config['date4_3'] = date4_3
    config['month4_3'] = month4_3
    config['year4_3'] = year4_3
    config['date5_3'] = date5_3
    config['month5_3'] = month5_3
    config['year5_3'] = year5_3
    config['date6_3'] = date6_3
    config['month6_3'] = month6_3
    config['year6_3'] = year6_3

    config['hourFrom1_3'] = hourFrom1_3
    config['minuteFrom1_3'] = minuteFrom1_3
    config['hourFrom2_3'] = hourFrom2_3
    config['minuteFrom2_3'] = minuteFrom2_3
    config['hourFrom3_3'] = hourFrom3_3
    config['minuteFrom3_3'] = minuteFrom3_3
    config['hourFrom4_3'] = hourFrom4_3
    config['minuteFrom4_3'] = minuteFrom4_3
    config['hourFrom5_3'] = hourFrom5_3
    config['minuteFrom5_3'] = minuteFrom5_3
    config['hourFrom6_3'] = hourFrom6_3
    config['minuteFrom6_3'] = minuteFrom6_3
    
    #phase 4
    config['hourOn1_4'] = hourOn1_4
    config['minOn1_4'] = minOn1_4
    config['hourOff1_4'] = hourOff1_4
    config['minOff1_4'] = minOff1_4
    config['hourOn2_4'] = hourOn2_4
    config['minOn2_4'] = minOn2_4
    config['hourOff2_4'] = hourOff2_4
    config['minOff2_4'] = minOff2_4
    config['hourOn3_4'] = hourOn3_4
    config['minOn3_4'] = minOn3_4
    config['hourOff3_4'] = hourOff3_4
    config['minOff3_4'] = minOff3_4
    config['hourOn4_4'] = hourOn4_4
    config['minOn4_4'] = minOn4_4
    config['hourOff4_4'] = hourOff4_4
    config['minOff4_4'] = minOff4_4
    config['hourOn5_4'] = hourOn5_4
    config['minOn5_4'] = minOn5_4
    config['hourOff5_4'] = hourOff5_4
    config['minOff5_4'] = minOff5_4
    config['hourOn6_4'] = hourOn6_4
    config['minOn6_4'] = minOn6_4
    config['hourOff6_4'] = hourOff6_4
    config['minOff6_4'] = minOff6_4
    
    config['dark1_4'] = dark1_4
    config['light1_4'] = light1_4
    config['dark2_4'] = dark2_4
    config['light2_4'] = light2_4
    config['dark3_4'] = dark3_4
    config['light3_4'] = light3_4
    config['dark4_4'] = dark4_4
    config['light4_4'] = light4_4
    config['dark5_4'] = dark5_4
    config['light5_4'] = light5_4
    config['dark6_4'] = dark6_4
    config['light6_4'] = light6_4
    
    config['date1_4'] = date1_4
    config['month1_4'] = month1_4
    config['year1_4'] = year1_4
    config['date2_4'] = date2_4
    config['month2_4'] = month2_4
    config['year2_4'] = year2_4
    config['date3_4'] = date3_4
    config['month3_4'] = month3_4
    config['year3_4'] = year3_4
    config['date4_4'] = date4_4
    config['month4_4'] = month4_4
    config['year4_4'] = year4_4
    config['date5_4'] = date5_4
    config['month5_4'] = month5_4
    config['year5_4'] = year5_4
    config['date6_4'] = date6_4
    config['month6_4'] = month6_4
    config['year6_4'] = year6_4

    config['hourFrom1_4'] = hourFrom1_4
    config['minuteFrom1_4'] = minuteFrom1_4
    config['hourFrom2_4'] = hourFrom2_4
    config['minuteFrom2_4'] = minuteFrom2_4
    config['hourFrom3_4'] = hourFrom3_4
    config['minuteFrom3_4'] = minuteFrom3_4
    config['hourFrom4_4'] = hourFrom4_4
    config['minuteFrom4_4'] = minuteFrom4_4
    config['hourFrom5_4'] = hourFrom5_4
    config['minuteFrom5_4'] = minuteFrom5_4
    config['hourFrom6_4'] = hourFrom6_4
    config['minuteFrom6_4'] = minuteFrom6_4

    #phase5
    config['hourOn1_5'] = hourOn1_5
    config['minOn1_5'] = minOn1_5
    config['hourOff1_5'] = hourOff1_5
    config['minOff1_5'] = minOff1_5
    config['hourOn2_5'] = hourOn2_5
    config['minOn2_5'] = minOn2_5
    config['hourOff2_5'] = hourOff2_5
    config['minOff2_5'] = minOff2_5
    config['hourOn3_5'] = hourOn3_5
    config['minOn3_5'] = minOn3_5
    config['hourOff3_5'] = hourOff3_5
    config['minOff3_5'] = minOff3_5
    config['hourOn4_5'] = hourOn4_5
    config['minOn4_5'] = minOn4_5
    config['hourOff4_5'] = hourOff4_5
    config['minOff4_5'] = minOff4_5
    config['hourOn5_5'] = hourOn5_5
    config['minOn5_5'] = minOn5_5
    config['hourOff5_5'] = hourOff5_5
    config['minOff5_5'] = minOff5_5
    config['hourOn6_5'] = hourOn6_5
    config['minOn6_5'] = minOn6_5
    config['hourOff6_5'] = hourOff6_5
    config['minOff6_5'] = minOff6_5
    
    config['dark1_5'] = dark1_5
    config['light1_5'] = light1_5
    config['dark2_5'] = dark2_5
    config['light2_5'] = light2_5
    config['dark3_5'] = dark3_5
    config['light3_5'] = light3_5
    config['dark4_5'] = dark4_5
    config['light4_5'] = light4_5
    config['dark5_5'] = dark5_5
    config['light5_5'] = light5_5
    config['dark6_5'] = dark6_5
    config['light6_5'] = light6_5
    
    config['date1_5'] = date1_5
    config['month1_5'] = month1_5
    config['year1_5'] = year1_5
    config['date2_5'] = date2_5
    config['month2_5'] = month2_5
    config['year2_5'] = year2_5
    config['date3_5'] = date3_5
    config['month3_5'] = month3_5
    config['year3_5'] = year3_5
    config['date4_5'] = date4_5
    config['month4_5'] = month4_5
    config['year4_5'] = year4_5
    config['date5_5'] = date5_5
    config['month5_5'] = month5_5
    config['year5_5'] = year5_5
    config['date6_5'] = date6_5
    config['month6_5'] = month6_5
    config['year6_5'] = year6_5

    config['hourFrom1_5'] = hourFrom1_5
    config['minuteFrom1_5'] = minuteFrom1_5
    config['hourFrom2_5'] = hourFrom2_5
    config['minuteFrom2_5'] = minuteFrom2_5
    config['hourFrom3_5'] = hourFrom3_5
    config['minuteFrom3_5'] = minuteFrom3_5
    config['hourFrom4_5'] = hourFrom4_5
    config['minuteFrom4_5'] = minuteFrom4_5
    config['hourFrom5_5'] = hourFrom5_5
    config['minuteFrom5_5'] = minuteFrom5_5
    config['hourFrom6_5'] = hourFrom6_5
    config['minuteFrom6_5'] = minuteFrom6_5
    
    #phase6
    config['hourOn1_6'] = hourOn1_6
    config['minOn1_6'] = minOn1_6
    config['hourOff1_6'] = hourOff1_6
    config['minOff1_6'] = minOff1_6
    config['hourOn2_6'] = hourOn2_6
    config['minOn2_6'] = minOn2_6
    config['hourOff2_6'] = hourOff2_6
    config['minOff2_6'] = minOff2_6
    config['hourOn3_6'] = hourOn3_6
    config['minOn3_6'] = minOn3_6
    config['hourOff3_6'] = hourOff3_6
    config['minOff3_6'] = minOff3_6
    config['hourOn4_6'] = hourOn4_6
    config['minOn4_6'] = minOn4_6
    config['hourOff4_6'] = hourOff4_6
    config['minOff4_6'] = minOff4_6
    config['hourOn5_6'] = hourOn5_6
    config['minOn5_6'] = minOn5_6
    config['hourOff5_6'] = hourOff5_6
    config['minOff5_6'] = minOff5_6
    config['hourOn6_6'] = hourOn6_6
    config['minOn6_6'] = minOn6_6
    config['hourOff6_6'] = hourOff6_6
    config['minOff6_6'] = minOff6_6
    
    config['dark1_6'] = dark1_6
    config['light1_6'] = light1_6
    config['dark2_6'] = dark2_6
    config['light2_6'] = light2_6
    config['dark3_6'] = dark3_6
    config['light3_6'] = light3_6
    config['dark4_6'] = dark4_6
    config['light4_6'] = light4_6
    config['dark5_6'] = dark5_6
    config['light5_6'] = light5_6
    config['dark6_6'] = dark6_6
    config['light6_6'] = light6_6
    
    config['date1_6'] = date1_6
    config['month1_6'] = month1_6
    config['year1_6'] = year1_6
    config['date2_6'] = date2_6
    config['month2_6'] = month2_6
    config['year2_6'] = year2_6
    config['date3_6'] = date3_6
    config['month3_6'] = month3_6
    config['year3_6'] = year3_6
    config['date4_6'] = date4_6
    config['month4_6'] = month4_6
    config['year4_6'] = year4_6
    config['date5_6'] = date5_6
    config['month5_6'] = month5_6
    config['year5_6'] = year5_6
    config['date6_6'] = date6_6
    config['month6_6'] = month6_6
    config['year6_6'] = year6_6

    config['hourFrom1_6'] = hourFrom1_6
    config['minuteFrom1_6'] = minuteFrom1_6
    config['hourFrom2_6'] = hourFrom2_6
    config['minuteFrom2_6'] = minuteFrom2_6
    config['hourFrom3_6'] = hourFrom3_6
    config['minuteFrom3_6'] = minuteFrom3_6
    config['hourFrom4_6'] = hourFrom4_6
    config['minuteFrom4_6'] = minuteFrom4_6
    config['hourFrom5_6'] = hourFrom5_6
    config['minuteFrom5_6'] = minuteFrom5_6
    config['hourFrom6_6'] = hourFrom6_6
    config['minuteFrom6_6'] = minuteFrom6_6


    #phase7
    config['hourOn1_7'] = hourOn1_7
    config['minOn1_7'] = minOn1_7
    config['hourOff1_7'] = hourOff1_7
    config['minOff1_7'] = minOff1_7
    config['hourOn2_7'] = hourOn2_7
    config['minOn2_7'] = minOn2_7
    config['hourOff2_7'] = hourOff2_7
    config['minOff2_7'] = minOff2_7
    config['hourOn3_7'] = hourOn3_7
    config['minOn3_7'] = minOn3_7
    config['hourOff3_7'] = hourOff3_7
    config['minOff3_7'] = minOff3_7
    config['hourOn4_7'] = hourOn4_7
    config['minOn4_7'] = minOn4_7
    config['hourOff4_7'] = hourOff4_7
    config['minOff4_7'] = minOff4_7
    config['hourOn5_7'] = hourOn5_7
    config['minOn5_7'] = minOn5_7
    config['hourOff5_7'] = hourOff5_7
    config['minOff5_7'] = minOff5_7
    config['hourOn6_7'] = hourOn6_7
    config['minOn6_7'] = minOn6_7
    config['hourOff6_7'] = hourOff6_7
    config['minOff6_7'] = minOff6_7
    
    config['dark1_7'] = dark1_7
    config['light1_7'] = light1_7
    config['dark2_7'] = dark2_7
    config['light2_7'] = light2_7
    config['dark3_7'] = dark3_7
    config['light3_7'] = light3_7
    config['dark4_7'] = dark4_7
    config['light4_7'] = light4_7
    config['dark5_7'] = dark5_7
    config['light5_7'] = light5_7
    config['dark6_7'] = dark6_7
    config['light6_7'] = light6_7
    
    config['date1_7'] = date1_7
    config['month1_7'] = month1_7
    config['year1_7'] = year1_7
    config['date2_7'] = date2_7
    config['month2_7'] = month2_7
    config['year2_7'] = year2_7
    config['date3_7'] = date3_7
    config['month3_7'] = month3_7
    config['year3_7'] = year3_7
    config['date4_7'] = date4_7
    config['month4_7'] = month4_7
    config['year4_7'] = year4_7
    config['date5_7'] = date5_7
    config['month5_7'] = month5_7
    config['year5_7'] = year5_7
    config['date6_7'] = date6_7
    config['month6_7'] = month6_7
    config['year6_7'] = year6_7

    config['hourFrom1_7'] = hourFrom1_7
    config['minuteFrom1_7'] = minuteFrom1_7
    config['hourFrom2_7'] = hourFrom2_7
    config['minuteFrom2_7'] = minuteFrom2_7
    config['hourFrom3_7'] = hourFrom3_7
    config['minuteFrom3_7'] = minuteFrom3_7
    config['hourFrom4_7'] = hourFrom4_7
    config['minuteFrom4_7'] = minuteFrom4_7
    config['hourFrom5_7'] = hourFrom5_7
    config['minuteFrom5_7'] = minuteFrom5_7
    config['hourFrom6_7'] = hourFrom6_7
    config['minuteFrom6_7'] = minuteFrom6_7

    #phase8
    config['hourOn1_8'] = hourOn1_8
    config['minOn1_8'] = minOn1_8
    config['hourOff1_8'] = hourOff1_8
    config['minOff1_8'] = minOff1_8
    config['hourOn2_8'] = hourOn2_8
    config['minOn2_8'] = minOn2_8
    config['hourOff2_8'] = hourOff2_8
    config['minOff2_8'] = minOff2_8
    config['hourOn3_8'] = hourOn3_8
    config['minOn3_8'] = minOn3_8
    config['hourOff3_8'] = hourOff3_8
    config['minOff3_8'] = minOff3_8
    config['hourOn4_8'] = hourOn4_8
    config['minOn4_8'] = minOn4_8
    config['hourOff4_8'] = hourOff4_8
    config['minOff4_8'] = minOff4_8
    config['hourOn5_8'] = hourOn5_8
    config['minOn5_8'] = minOn5_8
    config['hourOff5_8'] = hourOff5_8
    config['minOff5_8'] = minOff5_8
    config['hourOn6_8'] = hourOn6_8
    config['minOn6_8'] = minOn6_8
    config['hourOff6_8'] = hourOff6_8
    config['minOff6_8'] = minOff6_8
    
    config['dark1_8'] = dark1_8
    config['light1_8'] = light1_8
    config['dark2_8'] = dark2_8
    config['light2_8'] = light2_8
    config['dark3_8'] = dark3_8
    config['light3_8'] = light3_8
    config['dark4_8'] = dark4_8
    config['light4_8'] = light4_8
    config['dark5_8'] = dark5_8
    config['light5_8'] = light5_8
    config['dark6_8'] = dark6_8
    config['light6_8'] = light6_8
    
    config['date1_8'] = date1_8
    config['month1_8'] = month1_8
    config['year1_8'] = year1_8
    config['date2_8'] = date2_8
    config['month2_8'] = month2_8
    config['year2_8'] = year2_8
    config['date3_8'] = date3_8
    config['month3_8'] = month3_8
    config['year3_8'] = year3_8
    config['date4_8'] = date4_8
    config['month4_8'] = month4_8
    config['year4_8'] = year4_8
    config['date5_8'] = date5_8
    config['month5_8'] = month5_8
    config['year5_8'] = year5_8
    config['date6_8'] = date6_8
    config['month6_8'] = month6_8
    config['year6_8'] = year6_8

    config['hourFrom1_8'] = hourFrom1_8
    config['minuteFrom1_8'] = minuteFrom1_8
    config['hourFrom2_8'] = hourFrom2_8
    config['minuteFrom2_8'] = minuteFrom2_8
    config['hourFrom3_8'] = hourFrom3_8
    config['minuteFrom3_8'] = minuteFrom3_8
    config['hourFrom4_8'] = hourFrom4_8
    config['minuteFrom4_8'] = minuteFrom4_8
    config['hourFrom5_8'] = hourFrom5_8
    config['minuteFrom5_8'] = minuteFrom5_8
    config['hourFrom6_8'] = hourFrom6_8
    config['minuteFrom6_8'] = minuteFrom6_8


    #phase 9
    config['hourOn1_9'] = hourOn1_9
    config['minOn1_9'] = minOn1_9
    config['hourOff1_9'] = hourOff1_9
    config['minOff1_9'] = minOff1_9
    config['hourOn2_9'] = hourOn2_9
    config['minOn2_9'] = minOn2_9
    config['hourOff2_9'] = hourOff2_9
    config['minOff2_9'] = minOff2_9
    config['hourOn3_9'] = hourOn3_9
    config['minOn3_9'] = minOn3_9
    config['hourOff3_9'] = hourOff3_9
    config['minOff3_9'] = minOff3_9
    config['hourOn4_9'] = hourOn4_9
    config['minOn4_9'] = minOn4_9
    config['hourOff4_9'] = hourOff4_9
    config['minOff4_9'] = minOff4_9
    config['hourOn5_9'] = hourOn5_9
    config['minOn5_9'] = minOn5_9
    config['hourOff5_9'] = hourOff5_9
    config['minOff5_9'] = minOff5_9
    config['hourOn6_9'] = hourOn6_9
    config['minOn6_9'] = minOn6_9
    config['hourOff6_9'] = hourOff6_9
    config['minOff6_9'] = minOff6_9
    
    config['dark1_9'] = dark1_9
    config['light1_9'] = light1_9
    config['dark2_9'] = dark2_9
    config['light2_9'] = light2_9
    config['dark3_9'] = dark3_9
    config['light3_9'] = light3_9
    config['dark4_9'] = dark4_9
    config['light4_9'] = light4_9
    config['dark5_9'] = dark5_9
    config['light5_9'] = light5_9
    config['dark6_9'] = dark6_9
    config['light6_9'] = light6_9
    
    config['date1_9'] = date1_9
    config['month1_9'] = month1_9
    config['year1_9'] = year1_9
    config['date2_9'] = date2_9
    config['month2_9'] = month2_9
    config['year2_9'] = year2_9
    config['date3_9'] = date3_9
    config['month3_9'] = month3_9
    config['year3_9'] = year3_9
    config['date4_9'] = date4_9
    config['month4_9'] = month4_9
    config['year4_9'] = year4_9
    config['date5_9'] = date5_9
    config['month5_9'] = month5_9
    config['year5_9'] = year5_9
    config['date6_9'] = date6_9
    config['month6_9'] = month6_9
    config['year6_9'] = year6_9
    config['hourFrom1_9'] = hourFrom1_9
    config['minuteFrom1_9'] = minuteFrom1_9
    config['hourFrom2_9'] = hourFrom2_9
    config['minuteFrom2_9'] = minuteFrom2_9
    config['hourFrom3_9'] = hourFrom3_9
    config['minuteFrom3_9'] = minuteFrom3_9
    config['hourFrom4_9'] = hourFrom4_9
    config['minuteFrom4_9'] = minuteFrom4_9
    config['hourFrom5_9'] = hourFrom5_9
    config['minuteFrom5_9'] = minuteFrom5_9
    config['hourFrom6_9'] = hourFrom6_9
    config['minuteFrom6_9'] = minuteFrom6_9

        #phase 10
    config['hourOn1_10'] = hourOn1_10
    config['minOn1_10'] = minOn1_10
    config['hourOff1_10'] = hourOff1_10
    config['minOff1_10'] = minOff1_10
    config['hourOn2_10'] = hourOn2_10
    config['minOn2_10'] = minOn2_10
    config['hourOff2_10'] = hourOff2_10
    config['minOff2_10'] = minOff2_10
    config['hourOn3_10'] = hourOn3_10
    config['minOn3_10'] = minOn3_10
    config['hourOff3_10'] = hourOff3_10
    config['minOff3_10'] = minOff3_10
    config['hourOn4_10'] = hourOn4_10
    config['minOn4_10'] = minOn4_10
    config['hourOff4_10'] = hourOff4_10
    config['minOff4_10'] = minOff4_10
    config['hourOn5_10'] = hourOn5_10
    config['minOn5_10'] = minOn5_10
    config['hourOff5_10'] = hourOff5_10
    config['minOff5_10'] = minOff5_10
    config['hourOn6_10'] = hourOn6_10
    config['minOn6_10'] = minOn6_10
    config['hourOff6_10'] = hourOff6_10
    config['minOff6_10'] = minOff6_10
    
    config['dark1_10'] = dark1_10
    config['light1_10'] = light1_10
    config['dark2_10'] = dark2_10
    config['light2_10'] = light2_10
    config['dark3_10'] = dark3_10
    config['light3_10'] = light3_10
    config['dark4_10'] = dark4_10
    config['light4_10'] = light4_10
    config['dark5_10'] = dark5_10
    config['light5_10'] = light5_10
    config['dark6_10'] = dark6_10
    config['light6_10'] = light6_10
    
    config['date1_10'] = date1_10
    config['month1_10'] = month1_10
    config['year1_10'] = year1_10
    config['date2_10'] = date2_10
    config['month2_10'] = month2_10
    config['year2_10'] = year2_10
    config['date3_10'] = date3_10
    config['month3_10'] = month3_10
    config['year3_10'] = year3_10
    config['date4_10'] = date4_10
    config['month4_10'] = month4_10
    config['year4_10'] = year4_10
    config['date5_10'] = date5_10
    config['month5_10'] = month5_10
    config['year5_10'] = year5_10
    config['date6_10'] = date6_10
    config['month6_10'] = month6_10
    config['year6_10'] = year6_10
    config['hourFrom1_10'] = hourFrom1_10
    config['minuteFrom1_10'] = minuteFrom1_10
    config['hourFrom2_10'] = hourFrom2_10
    config['minuteFrom2_10'] = minuteFrom2_10
    config['hourFrom3_10'] = hourFrom3_10
    config['minuteFrom3_10'] = minuteFrom3_10
    config['hourFrom4_10'] = hourFrom4_10
    config['minuteFrom4_10'] = minuteFrom4_10
    config['hourFrom5_10'] = hourFrom5_10
    config['minuteFrom5_10'] = minuteFrom5_10
    config['hourFrom6_10'] = hourFrom6_10
    config['minuteFrom6_10'] = minuteFrom6_10


        #phase11
    config['hourOn1_11'] = hourOn1_11
    config['minOn1_11'] = minOn1_11
    config['hourOff1_11'] = hourOff1_11
    config['minOff1_11'] = minOff1_11
    config['hourOn2_11'] = hourOn2_11
    config['minOn2_11'] = minOn2_11
    config['hourOff2_11'] = hourOff2_11
    config['minOff2_11'] = minOff2_11
    config['hourOn3_11'] = hourOn3_11
    config['minOn3_11'] = minOn3_11
    config['hourOff3_11'] = hourOff3_11
    config['minOff3_11'] = minOff3_11
    config['hourOn4_11'] = hourOn4_11
    config['minOn4_11'] = minOn4_11
    config['hourOff4_11'] = hourOff4_11
    config['minOff4_11'] = minOff4_11
    config['hourOn5_11'] = hourOn5_11
    config['minOn5_11'] = minOn5_11
    config['hourOff5_11'] = hourOff5_11
    config['minOff5_11'] = minOff5_11
    config['hourOn6_11'] = hourOn6_11
    config['minOn6_11'] = minOn6_11
    config['hourOff6_11'] = hourOff6_11
    config['minOff6_11'] = minOff6_11
    
    config['dark1_11'] = dark1_11
    config['light1_11'] = light1_11
    config['dark2_11'] = dark2_11
    config['light2_11'] = light2_11
    config['dark3_11'] = dark3_11
    config['light3_11'] = light3_11
    config['dark4_11'] = dark4_11
    config['light4_11'] = light4_11
    config['dark5_11'] = dark5_11
    config['light5_11'] = light5_11
    config['dark6_11'] = dark6_11
    config['light6_11'] = light6_11
    
    config['date1_11'] = date1_11
    config['month1_11'] = month1_11
    config['year1_11'] = year1_11
    config['date2_11'] = date2_11
    config['month2_11'] = month2_11
    config['year2_11'] = year2_11
    config['date3_11'] = date3_11
    config['month3_11'] = month3_11
    config['year3_11'] = year3_11
    config['date4_11'] = date4_11
    config['month4_11'] = month4_11
    config['year4_11'] = year4_11
    config['date5_11'] = date5_11
    config['month5_11'] = month5_11
    config['year5_11'] = year5_11
    config['date6_11'] = date6_11
    config['month6_11'] = month6_11
    config['year6_11'] = year6_11

    config['hourFrom1_11'] = hourFrom1_11
    config['minuteFrom1_11'] = minuteFrom1_11
    config['hourFrom2_11'] = hourFrom2_11
    config['minuteFrom2_11'] = minuteFrom2_11
    config['hourFrom3_11'] = hourFrom3_11
    config['minuteFrom3_11'] = minuteFrom3_11
    config['hourFrom4_11'] = hourFrom4_11
    config['minuteFrom4_11'] = minuteFrom4_11
    config['hourFrom5_11'] = hourFrom5_11
    config['minuteFrom5_11'] = minuteFrom5_11
    config['hourFrom6_11'] = hourFrom6_11
    config['minuteFrom6_11'] = minuteFrom6_11


        #phase12
    config['hourOn1_12'] = hourOn1_12
    config['minOn1_12'] = minOn1_12
    config['hourOff1_12'] = hourOff1_12
    config['minOff1_12'] = minOff1_12
    config['hourOn2_12'] = hourOn2_12
    config['minOn2_12'] = minOn2_12
    config['hourOff2_12'] = hourOff2_12
    config['minOff2_12'] = minOff2_12
    config['hourOn3_12'] = hourOn3_12
    config['minOn3_12'] = minOn3_12
    config['hourOff3_12'] = hourOff3_12
    config['minOff3_12'] = minOff3_12
    config['hourOn4_12'] = hourOn4_12
    config['minOn4_12'] = minOn4_12
    config['hourOff4_12'] = hourOff4_12
    config['minOff4_12'] = minOff4_12
    config['hourOn5_12'] = hourOn5_12
    config['minOn5_12'] = minOn5_12
    config['hourOff5_12'] = hourOff5_12
    config['minOff5_12'] = minOff5_12
    config['hourOn6_12'] = hourOn6_12
    config['minOn6_12'] = minOn6_12
    config['hourOff6_12'] = hourOff6_12
    config['minOff6_12'] = minOff6_12
    
    config['dark1_12'] = dark1_12
    config['light1_12'] = light1_12
    config['dark2_12'] = dark2_12
    config['light2_12'] = light2_12
    config['dark3_12'] = dark3_12
    config['light3_12'] = light3_12
    config['dark4_12'] = dark4_12
    config['light4_12'] = light4_12
    config['dark5_12'] = dark5_12
    config['light5_12'] = light5_12
    config['dark6_12'] = dark6_12
    config['light6_12'] = light6_12
    
    config['date1_12'] = date1_12
    config['month1_12'] = month1_12
    config['year1_12'] = year1_12
    config['date2_12'] = date2_12
    config['month2_12'] = month2_12
    config['year2_12'] = year2_12
    config['date3_12'] = date3_12
    config['month3_12'] = month3_12
    config['year3_12'] = year3_12
    config['date4_12'] = date4_12
    config['month4_12'] = month4_12
    config['year4_12'] = year4_12
    config['date5_12'] = date5_12
    config['month5_12'] = month5_12
    config['year5_12'] = year5_12
    config['date6_12'] = date6_12
    config['month6_12'] = month6_12
    config['year6_12'] = year6_12

    config['hourFrom1_12'] = hourFrom1_12
    config['minuteFrom1_12'] = minuteFrom1_12
    config['hourFrom2_12'] = hourFrom2_12
    config['minuteFrom2_12'] = minuteFrom2_12
    config['hourFrom3_12'] = hourFrom3_12
    config['minuteFrom3_12'] = minuteFrom3_12
    config['hourFrom4_12'] = hourFrom4_12
    config['minuteFrom4_12'] = minuteFrom4_12
    config['hourFrom5_12'] = hourFrom5_12
    config['minuteFrom5_12'] = minuteFrom5_12
    config['hourFrom6_12'] = hourFrom6_12
    config['minuteFrom6_12'] = minuteFrom6_12

    config['initLED1_str'] = initLED1_str
    config['initLED2_str'] = initLED2_str
    config['initLED3_str'] = initLED3_str
    config['initLED4_str'] = initLED4_str
    config['initLED5_str'] = initLED5_str
    config['initLED6_str'] = initLED6_str
    
    config['tcycle_1_1'] = tcycle_1_1
    config['tcycle_1_2'] = tcycle_1_2
    config['tcycle_1_3'] = tcycle_1_3
    config['tcycle_1_4'] = tcycle_1_4
    config['tcycle_1_5'] = tcycle_1_5
    config['tcycle_1_6'] = tcycle_1_6
    config['tcycle_1_7'] = tcycle_1_7
    config['tcycle_1_8'] = tcycle_1_8
    config['tcycle_1_9'] = tcycle_1_9
    config['tcycle_1_10'] = tcycle_1_10
    config['tcycle_1_11'] = tcycle_1_11
    config['tcycle_1_12'] = tcycle_1_12


    config['tcycle_2_1'] = tcycle_2_1
    config['tcycle_2_2'] = tcycle_2_2
    config['tcycle_2_3'] = tcycle_2_3
    config['tcycle_2_4'] = tcycle_2_4
    config['tcycle_2_5'] = tcycle_2_5
    config['tcycle_2_6'] = tcycle_2_6
    config['tcycle_2_7'] = tcycle_2_7
    config['tcycle_2_8'] = tcycle_2_8
    config['tcycle_2_9'] = tcycle_2_9
    config['tcycle_2_10'] = tcycle_2_10
    config['tcycle_2_11'] = tcycle_2_11
    config['tcycle_2_12'] = tcycle_2_12

    config['tcycle_3_1'] = tcycle_3_1
    config['tcycle_3_2'] = tcycle_3_2
    config['tcycle_3_3'] = tcycle_3_3
    config['tcycle_3_4'] = tcycle_3_4
    config['tcycle_3_5'] = tcycle_3_5
    config['tcycle_3_6'] = tcycle_3_6
    config['tcycle_3_7'] = tcycle_3_7
    config['tcycle_3_8'] = tcycle_3_8
    config['tcycle_3_9'] = tcycle_3_9
    config['tcycle_3_10'] = tcycle_3_10
    config['tcycle_3_11'] = tcycle_3_11
    config['tcycle_3_12'] = tcycle_3_12

    config['tcycle_4_1'] = tcycle_4_1
    config['tcycle_4_2'] = tcycle_4_2
    config['tcycle_4_3'] = tcycle_4_3
    config['tcycle_4_4'] = tcycle_4_4
    config['tcycle_4_5'] = tcycle_4_5
    config['tcycle_4_6'] = tcycle_4_6
    config['tcycle_4_7'] = tcycle_4_7
    config['tcycle_4_8'] = tcycle_4_8
    config['tcycle_4_9'] = tcycle_4_9
    config['tcycle_4_10'] = tcycle_4_10
    config['tcycle_4_11'] = tcycle_4_11
    config['tcycle_4_12'] = tcycle_4_12

    config['tcycle_5_1'] = tcycle_5_1
    config['tcycle_5_2'] = tcycle_5_2
    config['tcycle_5_3'] = tcycle_5_3
    config['tcycle_5_4'] = tcycle_5_4
    config['tcycle_5_5'] = tcycle_5_5
    config['tcycle_5_6'] = tcycle_5_6
    config['tcycle_5_7'] = tcycle_5_7
    config['tcycle_5_8'] = tcycle_5_8
    config['tcycle_5_9'] = tcycle_5_9
    config['tcycle_5_10'] = tcycle_5_10
    config['tcycle_5_11'] = tcycle_5_11
    config['tcycle_5_12'] = tcycle_5_12

    config['tcycle_6_1'] = tcycle_6_1
    config['tcycle_6_2'] = tcycle_6_2
    config['tcycle_6_3'] = tcycle_6_3
    config['tcycle_6_4'] = tcycle_6_4
    config['tcycle_6_5'] = tcycle_6_5
    config['tcycle_6_6'] = tcycle_6_6
    config['tcycle_6_7'] = tcycle_6_7
    config['tcycle_6_8'] = tcycle_6_8
    config['tcycle_6_9'] = tcycle_6_9
    config['tcycle_6_10'] = tcycle_6_10
    config['tcycle_6_11'] = tcycle_6_11
    config['tcycle_6_12'] = tcycle_6_12

    configfilename = configfilename_entry.get()
    writeToJSONFile(configfilename, config)
    status.pack(side='bottom', fill='x')
    status.set('Schedule configuration saved.')


def read_data(): # Read data from file for plotting
    global file_plot
    status.pack(side='bottom', fill='x')
    status.set('Reading the data...')
    file_plot = askopenfilename(filetypes=(("Text files", "*.txt"),
                                      ("All files", "*.*")))
    status.pack(side='bottom', fill='x')
    status.set('Schedule configuration saved.')

def read_conf(): # Read schedule configuration
    status.pack(side='bottom', fill='x')
    status.set('Reading the schedule configuration...')
    configfilename = filedialog.askopenfilename()
    with open(configfilename) as data_file:
        config = json.load(data_file)


    global hourOn1_1, minOn1_1, hourOff1_1, minOff1_1, hourOn2_1, minOn2_1, hourOff2_1, minOff2_1 
    global hourOn3_1, minOn3_1, hourOff3_1, minOff3_1, hourOn4_1, minOn4_1, hourOff4_1, minOff4_1 
    global hourOn5_1, minOn5_1, hourOff5_1, minOff5_1, hourOn6_1, minOn6_1, hourOff6_1, minOff6_1
    global dark1_1, light1_1, dark2_1, light2_1, dark3_1, light3_1, dark4_1, light4_1, dark5_1, light5_1, dark6_1, light6_1  

    global hourOn1_2, minOn1_2, hourOff1_2, minOff1_2, hourOn2_2, minOn2_2, hourOff2_2, minOff2_2
    global hourOn3_2, minOn3_2, hourOff3_2, minOff3_2 , hourOn4_2, minOn4_2, hourOff4_2, minOff4_2 
    global hourOn5_2, minOn5_2, hourOff5_2, minOff5_2 , hourOn6_2, minOn6_2, hourOff6_2, minOff6_2
    global dark1_2, light1_2, dark2_2, light2_2, dark3_2, light3_2, dark4_2, light4_2, dark5_2, light5_2, dark6_2, light6_2
    
    global date1_2, month1_2, year1_2, date2_2, month2_2, year2_2, date3_2, month3_2, year3_2, date4_2, month4_2, year4_2 
    global date5_2, month5_2, year5_2, date6_2, month6_2, year6_2
    global hourFrom1_2, minuteFrom1_2, hourFrom2_2, minuteFrom2_2, hourFrom3_2, minuteFrom3_2, hourFrom4_2, minuteFrom4_2
    global hourFrom5_2, minuteFrom5_2, hourFrom6_2, minuteFrom6_2

    global hourOn1_3, minOn1_3, hourOff1_3, minOff1_3, hourOn2_3, minOn2_3, hourOff2_3, minOff2_3
    global hourOn3_3, minOn3_3, hourOff3_3, minOff3_3, hourOn4_3, minOn4_3, hourOff4_3, minOff4_3 
    global hourOn5_3, minOn5_3, hourOff5_3, minOff5_3, hourOn6_3, minOn6_3, hourOff6_3, minOff6_3 
    
    global dark1_3, light1_3, dark2_3, light2_3, dark3_3, light3_3, dark4_3, light4_3, dark5_3, light5_3
    global date1_3, month1_3, year1_3, date2_3, month2_3, year2_3, date3_3, month3_3, year3_3, date4_3, month4_3, year4_3 
    global date5_3, month5_3, year5_3, date6_3, month6_3, year6_3
    global hourFrom1_3, minuteFrom1_3, hourFrom2_3, minuteFrom2_3, hourFrom3_3, minuteFrom3_3, hourFrom4_3, minuteFrom4_3 
    global hourFrom5_3, minuteFrom5_3, hourFrom6_3, minuteFrom6_3
    
    global hourOn1_4, minOn1_4, hourOff1_4, minOff1_4, hourOn2_4, minOn2_4, hourOff2_4, minOff2_4
    global hourOn3_4, minOn3_4, hourOff3_4, minOff3_4, hourOn4_4, minOn4_4, hourOff4_4, minOff4_4 
    global hourOn5_4, minOn5_4, hourOff5_4, minOff5_4, hourOn6_4, minOn6_4, hourOff6_4, minOff6_4 
    
    global dark1_4, light1_4, dark2_4, light2_4, dark3_4, light3_4, dark4_4, light4_4, dark5_4, light5_4, dark6_4, light6_4
     
    global date1_4, month1_4, year1_4, date2_4, month2_4, year2_4, date3_4, month3_4, year3_4, date4_4, month4_4, year4_4 
    global date5_4, month5_4, year5_4, date6_4, month6_4, year6_4
    
    global hourFrom1_4, minuteFrom1_4, hourFrom2_4, minuteFrom2_4, hourFrom3_4, minuteFrom3_4, hourFrom4_4, minuteFrom4_4 
    global hourFrom5_4, minuteFrom5_4, hourFrom6_4, minuteFrom6_4

    #Phase 5
    global hourOn1_5, minOn1_5, hourOff1_5, minOff1_5, hourOn2_5, minOn2_5, hourOff2_5, minOff2_5
    global hourOn3_5, minOn3_5, hourOff3_5, minOff3_5, hourOn4_5, minOn4_5, hourOff4_5, minOff4_5 
    global hourOn5_5, minOn5_5, hourOff5_5, minOff5_5, hourOn6_5, minOn6_5, hourOff6_5, minOff6_5 
    
    global dark1_5, light1_5, dark2_5, light2_5, dark3_5, light3_5, dark4_5, light4_5, dark5_5, light5_5, dark6_5, light6_5
     
    global date1_5, month1_5, year1_5, date2_5, month2_5, year2_5, date3_5, month3_5, year3_5, date4_5, month4_5, year4_5 
    global date5_5, month5_5, year5_5, date6_5, month6_5, year6_5
    
    global hourFrom1_5, minuteFrom1_5, hourFrom2_5, minuteFrom2_5, hourFrom3_5, minuteFrom3_5, hourFrom4_5, minuteFrom4_5 
    global hourFrom5_5, minuteFrom5_5, hourFrom6_5, minuteFrom6_5


    #Phase 6
    global hourOn1_6, minOn1_6, hourOff1_6, minOff1_6, dark1_6, light1_6, date1_6, month1_6, year1_6, hourFrom1_6, minuteFrom1_6
    global hourOn2_6, minOn2_6, hourOff2_6, minOff2_6, dark2_6, light2_6, date2_6, month2_6, year2_6, hourFrom2_6, minuteFrom2_6
    global hourOn3_6, minOn3_6, hourOff3_6, minOff3_6, dark3_6, light3_6, date3_6, month3_6, year3_6, hourFrom3_6, minuteFrom3_6
    global hourOn4_6, minOn4_6, hourOff4_6, minOff4_6, dark4_6, light4_6, date4_6, month4_6, year4_6, hourFrom4_6, minuteFrom4_6
    global hourOn5_6, minOn5_6, hourOff5_6, minOff5_6, dark5_6, light5_6, date5_6, month5_6, year5_6, hourFrom5_6, minuteFrom5_6
    global hourOn6_6, minOn6_6, hourOff6_6, minOff6_6, dark6_6, light6_6, date6_6, month6_6, year6_6, hourFrom6_6, minuteFrom6_6

    global hourOn1_7, minOn1_7, hourOff1_7, minOff1_7, dark1_7, light1_7, date1_7, month1_7, year1_7, hourFrom1_7, minuteFrom1_7
    global hourOn2_7, minOn2_7, hourOff2_7, minOff2_7, dark2_7, light2_7, date2_7, month2_7, year2_7, hourFrom2_7, minuteFrom2_7
    global hourOn3_7, minOn3_7, hourOff3_7, minOff3_7, dark3_7, light3_7, date3_7, month3_7, year3_7, hourFrom3_7, minuteFrom3_7
    global hourOn4_7, minOn4_7, hourOff4_7, minOff4_7, dark4_7, light4_7, date4_7, month4_7, year4_7, hourFrom4_7, minuteFrom4_7
    global hourOn5_7, minOn5_7, hourOff5_7, minOff5_7, dark5_7, light5_7, date5_7, month5_7, year5_7, hourFrom5_7, minuteFrom5_7
    global hourOn6_7, minOn6_7, hourOff6_7, minOff6_7, dark6_7, light6_7, date6_7, month6_7, year6_7, hourFrom6_7, minuteFrom6_7

    global hourOn1_8, minOn1_8, hourOff1_8, minOff1_8, dark1_8, light1_8, date1_8, month1_8, year1_8, hourFrom1_8, minuteFrom1_8
    global hourOn2_8, minOn2_8, hourOff2_8, minOff2_8, dark2_8, light2_8, date2_8, month2_8, year2_8, hourFrom2_8, minuteFrom2_8
    global hourOn3_8, minOn3_8, hourOff3_8, minOff3_8, dark3_8, light3_8, date3_8, month3_8, year3_8, hourFrom3_8, minuteFrom3_8
    global hourOn4_8, minOn4_8, hourOff4_8, minOff4_8, dark4_8, light4_8, date4_8, month4_8, year4_8, hourFrom4_8, minuteFrom4_8
    global hourOn5_8, minOn5_8, hourOff5_8, minOff5_8, dark5_8, light5_8, date5_8, month5_8, year5_8, hourFrom5_8, minuteFrom5_8
    global hourOn6_8, minOn6_8, hourOff6_8, minOff6_8, dark6_8, light6_8, date6_8, month6_8, year6_8, hourFrom6_8, minuteFrom6_8

    global hourOn1_9, minOn1_9, hourOff1_9, minOff1_9, dark1_9, light1_9, date1_9, month1_9, year1_9, hourFrom1_9, minuteFrom1_9
    global hourOn2_9, minOn2_9, hourOff2_9, minOff2_9, dark2_9, light2_9, date2_9, month2_9, year2_9, hourFrom2_9, minuteFrom2_9
    global hourOn3_9, minOn3_9, hourOff3_9, minOff3_9, dark3_9, light3_9, date3_9, month3_9, year3_9, hourFrom3_9, minuteFrom3_9
    global hourOn4_9, minOn4_9, hourOff4_9, minOff4_9, dark4_9, light4_9, date4_9, month4_9, year4_9, hourFrom4_9, minuteFrom4_9
    global hourOn5_9, minOn5_9, hourOff5_9, minOff5_9, dark5_9, light5_9, date5_9, month5_9, year5_9, hourFrom5_9, minuteFrom5_9
    global hourOn6_9, minOn6_9, hourOff6_9, minOff6_9, dark6_9, light6_9, date6_9, month6_9, year6_9, hourFrom6_9, minuteFrom6_9

    global hourOn1_10, minOn1_10, hourOff1_10, minOff1_10, dark1_10, light1_10, date1_10, month1_10, year1_10, hourFrom1_10, minuteFrom1_10
    global hourOn2_10, minOn2_10, hourOff2_10, minOff2_10, dark2_10, light2_10, date2_10, month2_10, year2_10, hourFrom2_10, minuteFrom2_10
    global hourOn3_10, minOn3_10, hourOff3_10, minOff3_10, dark3_10, light3_10, date3_10, month3_10, year3_10, hourFrom3_10, minuteFrom3_10
    global hourOn4_10, minOn4_10, hourOff4_10, minOff4_10, dark4_10, light4_10, date4_10, month4_10, year4_10, hourFrom4_10, minuteFrom4_10
    global hourOn5_10, minOn5_10, hourOff5_10, minOff5_10, dark5_10, light5_10, date5_10, month5_10, year5_10, hourFrom5_10, minuteFrom5_10
    global hourOn6_10, minOn6_10, hourOff6_10, minOff6_10, dark6_10, light6_10, date6_10, month6_10, year6_10, hourFrom6_10, minuteFrom6_10

    global hourOn1_11, minOn1_11, hourOff1_11, minOff1_11, dark1_11, light1_11, date1_11, month1_11, year1_11, hourFrom1_11, minuteFrom1_11
    global hourOn2_11, minOn2_11, hourOff2_11, minOff2_11, dark2_11, light2_11, date2_11, month2_11, year2_11, hourFrom2_11, minuteFrom2_11
    global hourOn3_11, minOn3_11, hourOff3_11, minOff3_11, dark3_11, light3_11, date3_11, month3_11, year3_11, hourFrom3_11, minuteFrom3_11
    global hourOn4_11, minOn4_11, hourOff4_11, minOff4_11, dark4_11, light4_11, date4_11, month4_11, year4_11, hourFrom4_11, minuteFrom4_11
    global hourOn5_11, minOn5_11, hourOff5_11, minOff5_11, dark5_11, light5_11, date5_11, month5_11, year5_11, hourFrom5_11, minuteFrom5_11
    global hourOn6_11, minOn6_11, hourOff6_11, minOff6_11, dark6_11, light6_11, date6_11, month6_11, year6_11, hourFrom6_11, minuteFrom6_11

    global hourOn1_12, minOn1_12, hourOff1_12, minOff1_12, dark1_12, light1_12, date1_12, month1_12, year1_12, hourFrom1_12, minuteFrom1_12
    global hourOn2_12, minOn2_12, hourOff2_12, minOff2_12, dark2_12, light2_12, date2_12, month2_12, year2_12, hourFrom2_12, minuteFrom2_12
    global hourOn3_12, minOn3_12, hourOff3_12, minOff3_12, dark3_12, light3_12, date3_12, month3_12, year3_12, hourFrom3_12, minuteFrom3_12
    global hourOn4_12, minOn4_12, hourOff4_12, minOff4_12, dark4_12, light4_12, date4_12, month4_12, year4_12, hourFrom4_12, minuteFrom4_12
    global hourOn5_12, minOn5_12, hourOff5_12, minOff5_12, dark5_12, light5_12, date5_12, month5_12, year5_12, hourFrom5_12, minuteFrom5_12
    global hourOn6_12, minOn6_12, hourOff6_12, minOff6_12, dark6_12, light6_12, date6_12, month6_12, year6_12, hourFrom6_12, minuteFrom6_12

    global initLED1_str, initLED2_str, initLED3_str, initLED4_str , initLED5_str, initLED6_str
    global tcycle_1_1, tcycle_1_2,tcycle_1_3, tcycle_1_4, tcycle_1_5, tcycle_1_6, tcycle_1_7, tcycle_1_8, tcycle_1_9, tcycle_1_10, tcycle_1_11, tcycle_1_12
    global tcycle_2_1, tcycle_2_2,tcycle_2_3, tcycle_2_4, tcycle_2_5, tcycle_2_6, tcycle_2_7, tcycle_2_8, tcycle_2_9, tcycle_2_10, tcycle_2_11, tcycle_2_12
    global tcycle_3_1, tcycle_3_2,tcycle_3_3, tcycle_3_4, tcycle_3_5, tcycle_3_6, tcycle_3_7, tcycle_3_8, tcycle_3_9, tcycle_3_10, tcycle_3_11, tcycle_3_12
    global tcycle_4_1, tcycle_4_2,tcycle_4_3, tcycle_4_4, tcycle_4_5, tcycle_4_6, tcycle_4_7, tcycle_4_8, tcycle_4_9, tcycle_4_10, tcycle_4_11, tcycle_4_12
    global tcycle_5_1, tcycle_5_2,tcycle_5_3, tcycle_5_4, tcycle_5_5, tcycle_5_6, tcycle_5_7, tcycle_5_8, tcycle_5_9, tcycle_5_10, tcycle_5_11, tcycle_5_12
    global tcycle_5_1, tcycle_5_2,tcycle_5_3, tcycle_5_4, tcycle_5_5, tcycle_5_6, tcycle_5_7, tcycle_5_8, tcycle_5_9, tcycle_5_10, tcycle_5_11, tcycle_5_12
    global tcycle_6_1, tcycle_6_2,tcycle_6_3, tcycle_6_4, tcycle_6_5, tcycle_6_6, tcycle_6_7, tcycle_6_8, tcycle_6_9, tcycle_6_10, tcycle_6_11, tcycle_6_12

    try:
        minuteFrom5_12 = config['minuteFrom5_12'] 
    except KeyError:
        getAllBoxSchedule() #set default values using the ones displayed and then load the JSON values on top
     

    try:
        hourOn1_1 = config['hourOn1_1'] 
        minOn1_1 = config['minOn1_1'] 
        hourOff1_1 = config['hourOff1_1']
        minOff1_1 = config['minOff1_1'] 
        hourOn2_1 = config['hourOn2_1']
        minOn2_1 = config['minOn2_1'] 
        hourOff2_1 = config['hourOff2_1'] 
        minOff2_1 = config['minOff2_1'] 
        hourOn3_1 = config['hourOn3_1'] 
        minOn3_1 = config['minOn3_1'] 
        hourOff3_1 = config['hourOff3_1'] 
        minOff3_1 = config['minOff3_1'] 
        hourOn4_1 = config['hourOn4_1'] 
        minOn4_1 = config['minOn4_1']
        hourOff4_1 = config['hourOff4_1'] 
        minOff4_1 = config['minOff4_1'] 
        hourOn5_1 = config['hourOn5_1']
        minOn5_1 = config['minOn5_1'] 
        hourOff5_1 = config['hourOff5_1'] 
        minOff5_1 = config['minOff5_1'] 
        hourOn6_1 = config['hourOn6_1']
        minOn6_1 = config['minOn6_1'] 
        hourOff6_1 = config['hourOff6_1'] 
        minOff6_1 = config['minOff6_1'] 

        
        dark1_1 = config['dark1_1'] 
        light1_1 = config['light1_1']
        dark2_1 = config['dark2_1'] 
        light2_1 = config['light2_1'] 
        dark3_1 = config['dark3_1'] 
        light3_1 = config['light3_1'] 
        dark4_1 = config['dark4_1'] 
        light4_1 = config['light4_1'] 
        dark5_1 = config['dark5_1'] 
        light5_1 = config['light5_1'] 
        dark6_1 = config['dark6_1'] 
        light6_1 = config['light6_1'] 

        hourOn1_2 = config['hourOn1_2'] 
        minOn1_2 = config['minOn1_2'] 
        hourOff1_2 = config['hourOff1_2'] 
        minOff1_2 = config['minOff1_2'] 
        hourOn2_2 = config['hourOn2_2'] 
        minOn2_2 = config['minOn2_2'] 
        hourOff2_2 = config['hourOff2_2'] 
        minOff2_2 = config['minOff2_2'] 
        hourOn3_2 = config['hourOn3_2'] 
        minOn3_2 = config['minOn3_2'] 
        hourOff3_2 = config['hourOff3_2'] 
        minOff3_2 = config['minOff3_2'] 
        hourOn4_2 = config['hourOn4_2'] 
        minOn4_2 = config['minOn4_2'] 
        hourOff4_2 = config['hourOff4_2'] 
        minOff4_2 = config['minOff4_2'] 
        hourOn5_2 = config['hourOn5_2'] 
        minOn5_2 = config['minOn5_2'] 
        hourOff5_2 = config['hourOff5_2'] 
        minOff5_2 = config['minOff5_2'] 
        hourOn6_2 = config['hourOn6_2'] 
        minOn6_2 = config['minOn6_2'] 
        hourOff6_2 = config['hourOff6_2'] 
        minOff6_2 = config['minOff6_2'] 
        
        dark1_2 = config['dark1_2'] 
        light1_2 = config['light1_2'] 
        dark2_2 = config['dark2_2'] 
        light2_2 = config['light2_2'] 
        dark3_2 = config['dark3_2'] 
        light3_2 = config['light3_2'] 
        dark4_2 = config['dark4_2'] 
        light4_2 = config['light4_2'] 
        dark5_2 = config['dark5_2'] 
        light5_2 = config['light5_2'] 
        dark6_2 = config['dark6_2'] 
        light6_2 = config['light6_2'] 
        
        date1_2 = config['date1_2']
        month1_2 = config['month1_2'] 
        year1_2 = config['year1_2'] 
        date2_2 = config['date2_2'] 
        month2_2 = config['month2_2'] 
        year2_2 = config['year2_2'] 
        date3_2 = config['date3_2'] 
        month3_2 = config['month3_2'] 
        year3_2 = config['year3_2'] 
        date4_2 = config['date4_2'] 
        month4_2 = config['month4_2'] 
        year4_2 = config['year4_2'] 
        date5_2 = config['date5_2'] 
        month5_2 = config['month5_2'] 
        year5_2 = config['year5_2'] 
        date6_2 = config['date6_2'] 
        month6_2 = config['month6_2'] 
        year6_2 = config['year6_2'] 

        hourFrom1_2 = config['hourFrom1_2'] 
        minuteFrom1_2 = config['minuteFrom1_2'] 
        hourFrom2_2 = config['hourFrom2_2'] 
        minuteFrom2_2 = config['minuteFrom2_2'] 
        hourFrom3_2 = config['hourFrom3_2'] 
        minuteFrom3_2 = config['minuteFrom3_2'] 
        hourFrom4_2 = config['hourFrom4_2'] 
        minuteFrom4_2 = config['minuteFrom4_2'] 
        hourFrom5_2 = config['hourFrom5_2'] 
        minuteFrom5_2 = config['minuteFrom5_2'] 
        hourFrom6_2 = config['hourFrom6_2'] 
        minuteFrom6_2 = config['minuteFrom6_2'] 
        
        hourOn1_3 = config['hourOn1_3'] 
        minOn1_3 = config['minOn1_3'] 
        hourOff1_3 = config['hourOff1_3'] 
        minOff1_3 = config['minOff1_3'] 
        hourOn2_3 = config['hourOn2_3'] 
        minOn2_3 = config['minOn2_3'] 
        hourOff2_3 = config['hourOff2_3'] 
        minOff2_3 = config['minOff2_3']
        hourOn3_3 = config['hourOn3_3'] 
        minOn3_3 = config['minOn3_3'] 
        hourOff3_3 = config['hourOff3_3'] 
        minOff3_3 = config['minOff3_3'] 
        hourOn4_3 = config['hourOn4_3'] 
        minOn4_3 = config['minOn4_3'] 
        hourOff4_3 = config['hourOff4_3'] 
        minOff4_3 = config['minOff4_3'] 
        hourOn5_3 = config['hourOn5_3'] 
        minOn5_3 = config['minOn5_3'] 
        hourOff5_3 = config['hourOff5_3'] 
        minOff5_3 = config['minOff5_3'] 
        hourOn6_3 = config['hourOn6_3'] 
        minOn6_3 = config['minOn6_3'] 
        hourOff6_3 = config['hourOff6_3'] 
        minOff6_3 = config['minOff6_3'] 
        
        dark1_3 = config['dark1_3'] 
        light1_3 = config['light1_3'] 
        dark2_3 = config['dark2_3'] 
        light2_3 = config['light2_3'] 
        dark3_3 = config['dark3_3'] 
        light3_3 = config['light3_3'] 
        dark4_3 = config['dark4_3'] 
        light4_3 = config['light4_3'] 
        dark5_3 = config['dark5_3'] 
        light5_3 = config['light5_3'] 
        dark6_3 = config['dark6_3'] 
        light6_3 = config['light6_3'] 
        
        date1_3 = config['date1_3']
        month1_3 = config['month1_3'] 
        year1_3 = config['year1_3'] 
        date2_3 = config['date2_3'] 
        month2_3 = config['month2_3'] 
        year2_3 = config['year2_3'] 
        date3_3 = config['date3_3'] 
        month3_3 = config['month3_3'] 
        year3_3 = config['year3_3'] 
        date4_3 = config['date4_3'] 
        month4_3 = config['month4_3'] 
        year4_3 = config['year4_3']
        date5_3 = config['date5_3'] 
        month5_3 = config['month5_3'] 
        year5_3 = config['year5_3'] 
        date6_3 = config['date6_3'] 
        month6_3 = config['month6_3'] 
        year6_3 = config['year6_3'] 

        hourFrom1_3 = config['hourFrom1_3'] 
        minuteFrom1_3 = config['minuteFrom1_3'] 
        hourFrom2_3 = config['hourFrom2_3'] 
        minuteFrom2_3 = config['minuteFrom2_3'] 
        hourFrom3_3 = config['hourFrom3_3'] 
        minuteFrom3_3 = config['minuteFrom3_3'] 
        hourFrom4_3 = config['hourFrom4_3'] 
        minuteFrom4_3 = config['minuteFrom4_3'] 
        hourFrom5_3 = config['hourFrom5_3'] 
        minuteFrom5_3 = config['minuteFrom5_3'] 
        hourFrom6_3 = config['hourFrom6_3'] 
        minuteFrom6_3 = config['minuteFrom6_3'] 
        
        hourOn1_4 = config['hourOn1_4'] 
        minOn1_4 = config['minOn1_4'] 
        hourOff1_4 = config['hourOff1_4'] 
        minOff1_4 = config['minOff1_4'] 
        hourOn2_4 = config['hourOn2_4'] 
        minOn2_4 = config['minOn2_4'] 
        hourOff2_4 = config['hourOff2_4'] 
        minOff2_4 = config['minOff2_4']
        hourOn3_4 = config['hourOn3_4'] 
        minOn3_4 = config['minOn3_4'] 
        hourOff3_4 = config['hourOff3_4'] 
        minOff3_4 = config['minOff3_4'] 
        hourOn4_4 = config['hourOn4_4'] 
        minOn4_4 = config['minOn4_4'] 
        hourOff4_4 = config['hourOff4_4'] 
        minOff4_4 = config['minOff4_4'] 
        hourOn5_4 = config['hourOn5_4'] 
        minOn5_4 = config['minOn5_4'] 
        hourOff5_4 = config['hourOff5_4'] 
        minOff5_4 = config['minOff5_4'] 
        hourOn6_4 = config['hourOn6_4'] 
        minOn6_4 = config['minOn6_4'] 
        hourOff6_4 = config['hourOff6_4'] 
        minOff6_4 = config['minOff6_4'] 
        
        dark1_4 = config['dark1_4'] 
        light1_4 = config['light1_4'] 
        dark2_4 = config['dark2_4'] 
        light2_4 = config['light2_4'] 
        dark3_4 = config['dark3_4'] 
        light3_4 = config['light3_4'] 
        dark4_4 = config['dark4_4'] 
        light4_4 = config['light4_4'] 
        dark5_4 = config['dark5_4'] 
        light5_4 = config['light5_4'] 
        dark6_4 = config['dark6_4'] 
        light6_4 = config['light6_4'] 
        
        date1_4 = config['date1_4']
        month1_4 = config['month1_4'] 
        year1_4 = config['year1_4'] 
        date2_4 = config['date2_4'] 
        month2_4 = config['month2_4'] 
        year2_4 = config['year2_4'] 
        date3_4 = config['date3_4'] 
        month3_4 = config['month3_4'] 
        year3_4 = config['year3_4'] 
        date4_4 = config['date4_4'] 
        month4_4 = config['month4_4'] 
        year4_4 = config['year4_4']
        date5_4 = config['date5_4'] 
        month5_4 = config['month5_4'] 
        year5_4 = config['year5_4'] 
        date6_4 = config['date6_4'] 
        month6_4 = config['month6_4'] 
        year6_4 = config['year6_4'] 

        hourFrom1_4 = config['hourFrom1_4'] 
        minuteFrom1_4 = config['minuteFrom1_4'] 
        hourFrom2_4 = config['hourFrom2_4'] 
        minuteFrom2_4 = config['minuteFrom2_4'] 
        hourFrom3_4 = config['hourFrom3_4'] 
        minuteFrom3_4 = config['minuteFrom3_4'] 
        hourFrom4_4 = config['hourFrom4_4'] 
        minuteFrom4_4 = config['minuteFrom4_4'] 
        hourFrom5_4 = config['hourFrom5_4'] 
        minuteFrom5_4 = config['minuteFrom5_4'] 
        hourFrom6_4 = config['hourFrom6_4'] 
        minuteFrom6_4 = config['minuteFrom6_4'] 

        
    #phase5

        hourOn1_5 =config['hourOn1_5']  
        minOn1_5 = config['minOn1_5'] 
        hourOff1_5 = config['hourOff1_5'] 
        minOff1_5 =config['minOff1_5']  
        hourOn2_5 = config['hourOn2_5']  
        minOn2_5 = config['minOn2_5'] 
        hourOff2_5 = config['hourOff2_5']
        minOff2_5 = config['minOff2_5']  
        hourOn3_5 = config['hourOn3_5']  
        minOn3_5 = config['minOn3_5'] 
        hourOff3_5 =config['hourOff3_5']
        minOff3_5 = config['minOff3_5'] 
        hourOn4_5 =config['hourOn4_5']  
        minOn4_5 = config['minOn4_5']
        hourOff4_5 = config['hourOff4_5']
        minOff4_5 = config['minOff4_5']  
        hourOn5_5 = config['hourOn5_5']  
        minOn5_5 = config['minOn5_5']
        hourOff5_5 =config['hourOff5_5']
        minOff5_5 =config['minOff5_5']  
        hourOn6_5 = config['hourOn6_5']  
        minOn6_5 = config['minOn6_5']
        hourOff6_5 =config['hourOff6_5']
        minOff6_5 =config['minOff6_5']  
        
        dark1_5 = config['dark1_5'] 
        light1_5 = config['light1_5'] 
        dark2_5 = config['dark2_5'] 
        light2_5 = config['light2_5'] 
        dark3_5 = config['dark3_5'] 
        light3_5 = config['light3_5'] 
        dark4_5 = config['dark4_5'] 
        light4_5 = config['light4_5'] 
        dark5_5 = config['dark5_5'] 
        light5_5 = config['light5_5'] 
        dark6_5 = config['dark6_5'] 
        light6_5 = config['light6_5'] 
        
        date1_5 = config['date1_5'] 
        month1_5 = config['month1_5']
        year1_5 = config['year1_5'] 
        date2_5 = config['date2_5'] 
        month2_5 = config['month2_5']
        year2_5 = config['year2_5'] 
        date3_5 = config['date3_5'] 
        month3_5 = config['month3_5']
        year3_5 = config['year3_5'] 
        date4_5 = config['date4_5'] 
        month4_5 = config['month4_5']
        year4_5 = config['year4_5'] 
        date5_5 = config['date5_5'] 
        month5_5 = config['month5_5']
        year5_5 = config['year5_5'] 
        date6_5 = config['date6_5'] 
        month6_5 = config['month6_5']
        year6_5 = config['year6_5'] 

        hourFrom1_5 = config['hourFrom1_5'] 
        minuteFrom1_5 = config['minuteFrom1_5'] 
        hourFrom2_5 = config['hourFrom2_5'] 
        minuteFrom2_5 =config['minuteFrom2_5'] 
        hourFrom3_5 =config['hourFrom3_5'] 
        minuteFrom3_5 =config['minuteFrom3_5'] 
        hourFrom4_5 =config['hourFrom4_5'] 
        minuteFrom4_5 = config['minuteFrom4_5'] 
        hourFrom5_5 = config['hourFrom5_5'] 
        minuteFrom5_5 = config['minuteFrom5_5'] 
        hourFrom6_5 = config['hourFrom6_5'] 
        minuteFrom6_5 = config['minuteFrom6_5'] 
    


    #phase 6
    
        hourOn1_6 =config['hourOn1_6']  
        minOn1_6 = config['minOn1_6'] 
        hourOff1_6 = config['hourOff1_6'] 
        minOff1_6 =config['minOff1_6']  
        hourOn2_6 = config['hourOn2_6']  
        minOn2_6 = config['minOn2_6'] 
        hourOff2_6 = config['hourOff2_6']
        minOff2_6 = config['minOff2_6']  
        hourOn3_6 = config['hourOn3_6']  
        minOn3_6 = config['minOn3_6'] 
        hourOff3_6 =config['hourOff3_6']
        minOff3_6 = config['minOff3_6'] 
        hourOn4_6 =config['hourOn4_6']  
        minOn4_6 = config['minOn4_6']
        hourOff4_6 = config['hourOff4_6']
        minOff4_6 = config['minOff4_6']  
        hourOn5_6 = config['hourOn5_6']  
        minOn5_6 = config['minOn5_6']
        hourOff5_6 =config['hourOff5_6']
        minOff5_6 =config['minOff5_6']  
        hourOn6_6 = config['hourOn6_6']  
        minOn6_6 = config['minOn6_6']
        hourOff6_6 =config['hourOff6_6']
        minOff6_6 =config['minOff6_6']  
        
        dark1_6 = config['dark1_6'] 
        light1_6 = config['light1_6'] 
        dark2_6 = config['dark2_6'] 
        light2_6 = config['light2_6'] 
        dark3_6 = config['dark3_6'] 
        light3_6 = config['light3_6'] 
        dark4_6 = config['dark4_6'] 
        light4_6 = config['light4_6'] 
        dark5_6 = config['dark5_6'] 
        light5_6 = config['light5_6'] 
        dark6_6 = config['dark6_6'] 
        light6_6 = config['light6_6'] 
        
        date1_6 = config['date1_6'] 
        month1_6 = config['month1_6']
        year1_6 = config['year1_6'] 
        date2_6 = config['date2_6'] 
        month2_6 = config['month2_6']
        year2_6 = config['year2_6'] 
        date3_6 = config['date3_6'] 
        month3_6 = config['month3_6']
        year3_6 = config['year3_6'] 
        date4_6 = config['date4_6'] 
        month4_6 = config['month4_6']
        year4_6 = config['year4_6'] 
        date5_6 = config['date5_6'] 
        month5_6 = config['month5_6']
        year5_6 = config['year5_6'] 
        date6_6 = config['date6_6'] 
        month6_6 = config['month6_6']
        year6_6 = config['year6_6'] 

        hourFrom1_6 = config['hourFrom1_6'] 
        minuteFrom1_6 = config['minuteFrom1_6'] 
        hourFrom2_6 = config['hourFrom2_6'] 
        minuteFrom2_6 =config['minuteFrom2_6'] 
        hourFrom3_6 =config['hourFrom3_6'] 
        minuteFrom3_6 =config['minuteFrom3_6'] 
        hourFrom4_6 =config['hourFrom4_6'] 
        minuteFrom4_6 = config['minuteFrom4_6'] 
        hourFrom5_6 = config['hourFrom5_6'] 
        minuteFrom5_6 = config['minuteFrom5_6'] 
        hourFrom6_6 = config['hourFrom6_6'] 
        minuteFrom6_6 = config['minuteFrom6_6'] 
    
#Phase 7 
    
        hourOn1_7 =config['hourOn1_7']  
        minOn1_7 = config['minOn1_7'] 
        hourOff1_7 = config['hourOff1_7'] 
        minOff1_7 =config['minOff1_7']  
        hourOn2_7 = config['hourOn2_7']  
        minOn2_7 = config['minOn2_7'] 
        hourOff2_7 = config['hourOff2_7']
        minOff2_7 = config['minOff2_7']  
        hourOn3_7 = config['hourOn3_7']  
        minOn3_7 = config['minOn3_7'] 
        hourOff3_7 =config['hourOff3_7']
        minOff3_7 = config['minOff3_7'] 
        hourOn4_7 =config['hourOn4_7']  
        minOn4_7 = config['minOn4_7']
        hourOff4_7 = config['hourOff4_7']
        minOff4_7 = config['minOff4_7']  
        hourOn5_7 = config['hourOn5_7']  
        minOn5_7 = config['minOn5_7']
        hourOff5_7 =config['hourOff5_7']
        minOff5_7 =config['minOff5_7']  
        hourOn6_7 = config['hourOn6_7']  
        minOn6_7 = config['minOn6_7']
        hourOff6_7 =config['hourOff6_7']
        minOff6_7 =config['minOff6_7']  
        
        dark1_7 = config['dark1_7'] 
        light1_7 = config['light1_7'] 
        dark2_7 = config['dark2_7'] 
        light2_7 = config['light2_7'] 
        dark3_7 = config['dark3_7'] 
        light3_7 = config['light3_7'] 
        dark4_7 = config['dark4_7'] 
        light4_7 = config['light4_7'] 
        dark5_7 = config['dark5_7'] 
        light5_7 = config['light5_7'] 
        dark6_7 = config['dark6_7'] 
        light6_7 = config['light6_7'] 
        
        date1_7 = config['date1_7'] 
        month1_7 = config['month1_7']
        year1_7 = config['year1_7'] 
        date2_7 = config['date2_7'] 
        month2_7 = config['month2_7']
        year2_7 = config['year2_7'] 
        date3_7 = config['date3_7'] 
        month3_7 = config['month3_7']
        year3_7 = config['year3_7'] 
        date4_7 = config['date4_7'] 
        month4_7 = config['month4_7']
        year4_7 = config['year4_7'] 
        date5_7 = config['date5_7'] 
        month5_7 = config['month5_7']
        year5_7 = config['year5_7'] 
        date6_7 = config['date6_7'] 
        month6_7 = config['month6_7']
        year6_7 = config['year6_7'] 

        hourFrom1_7 = config['hourFrom1_7'] 
        minuteFrom1_7 = config['minuteFrom1_7'] 
        hourFrom2_7 = config['hourFrom2_7'] 
        minuteFrom2_7 =config['minuteFrom2_7'] 
        hourFrom3_7 =config['hourFrom3_7'] 
        minuteFrom3_7 =config['minuteFrom3_7'] 
        hourFrom4_7 =config['hourFrom4_7'] 
        minuteFrom4_7 = config['minuteFrom4_7'] 
        hourFrom5_7 = config['hourFrom5_7'] 
        minuteFrom5_7 = config['minuteFrom5_7'] 
        hourFrom6_7 = config['hourFrom6_7'] 
        minuteFrom6_7 = config['minuteFrom6_7'] 
    

    #Phase 8
    
        hourOn1_8 =config['hourOn1_8']  
        minOn1_8 = config['minOn1_8'] 
        hourOff1_8 = config['hourOff1_8'] 
        minOff1_8 =config['minOff1_8']  
        hourOn2_8 = config['hourOn2_8']  
        minOn2_8 = config['minOn2_8'] 
        hourOff2_8 = config['hourOff2_8']
        minOff2_8 = config['minOff2_8']  
        hourOn3_8 = config['hourOn3_8']  
        minOn3_8 = config['minOn3_8'] 
        hourOff3_8 =config['hourOff3_8']
        minOff3_8 = config['minOff3_8'] 
        hourOn4_8 =config['hourOn4_8']  
        minOn4_8 = config['minOn4_8']
        hourOff4_8 = config['hourOff4_8']
        minOff4_8 = config['minOff4_8']  
        hourOn5_8 = config['hourOn5_8']  
        minOn5_8 = config['minOn5_8']
        hourOff5_8 =config['hourOff5_8']
        minOff5_8 =config['minOff5_8']  
        hourOn6_8 = config['hourOn6_8']  
        minOn6_8 = config['minOn6_8']
        hourOff6_8 =config['hourOff6_8']
        minOff6_8 =config['minOff6_8']  
        
        dark1_8 = config['dark1_8'] 
        light1_8 = config['light1_8'] 
        dark2_8 = config['dark2_8'] 
        light2_8 = config['light2_8'] 
        dark3_8 = config['dark3_8'] 
        light3_8 = config['light3_8'] 
        dark4_8 = config['dark4_8'] 
        light4_8 = config['light4_8'] 
        dark5_8 = config['dark5_8'] 
        light5_8 = config['light5_8'] 
        dark6_8 = config['dark6_8'] 
        light6_8 = config['light6_8'] 
        
        date1_8 = config['date1_8'] 
        month1_8 = config['month1_8']
        year1_8 = config['year1_8'] 
        date2_8 = config['date2_8'] 
        month2_8 = config['month2_8']
        year2_8 = config['year2_8'] 
        date3_8 = config['date3_8'] 
        month3_8 = config['month3_8']
        year3_8 = config['year3_8'] 
        date4_8 = config['date4_8'] 
        month4_8 = config['month4_8']
        year4_8 = config['year4_8'] 
        date5_8 = config['date5_8'] 
        month5_8 = config['month5_8']
        year5_8 = config['year5_8'] 
        date6_8 = config['date6_8'] 
        month6_8 = config['month6_8']
        year6_8 = config['year6_8'] 

        hourFrom1_8 = config['hourFrom1_8'] 
        minuteFrom1_8 = config['minuteFrom1_8'] 
        hourFrom2_8 = config['hourFrom2_8'] 
        minuteFrom2_8 =config['minuteFrom2_8'] 
        hourFrom3_8 =config['hourFrom3_8'] 
        minuteFrom3_8 =config['minuteFrom3_8'] 
        hourFrom4_8 =config['hourFrom4_8'] 
        minuteFrom4_8 = config['minuteFrom4_8'] 
        hourFrom5_8 = config['hourFrom5_8'] 
        minuteFrom5_8 = config['minuteFrom5_8'] 
        hourFrom6_8 = config['hourFrom6_8'] 
        minuteFrom6_8 = config['minuteFrom6_8'] 

    

    #Phase 9

    
        hourOn1_9 =config['hourOn1_9']  
        minOn1_9 = config['minOn1_9'] 
        hourOff1_9 = config['hourOff1_9'] 
        minOff1_9 =config['minOff1_9']  
        hourOn2_9 = config['hourOn2_9']  
        minOn2_9 = config['minOn2_9'] 
        hourOff2_9 = config['hourOff2_9']
        minOff2_9 = config['minOff2_9']  
        hourOn3_9 = config['hourOn3_9']  
        minOn3_9 = config['minOn3_9'] 
        hourOff3_9 =config['hourOff3_9']
        minOff3_9 = config['minOff3_9'] 
        hourOn4_9 =config['hourOn4_9']  
        minOn4_9 = config['minOn4_9']
        hourOff4_9 = config['hourOff4_9']
        minOff4_9 = config['minOff4_9']  
        hourOn5_9 = config['hourOn5_9']  
        minOn5_9 = config['minOn5_9']
        hourOff5_9 =config['hourOff5_9']
        minOff5_9 =config['minOff5_9']  
        hourOn6_9 = config['hourOn6_9']  
        minOn6_9 = config['minOn6_9']
        hourOff6_9 =config['hourOff6_9']
        minOff6_9 =config['minOff6_9']  
        
        dark1_9 = config['dark1_9'] 
        light1_9 = config['light1_9'] 
        dark2_9 = config['dark2_9'] 
        light2_9 = config['light2_9'] 
        dark3_9 = config['dark3_9'] 
        light3_9 = config['light3_9'] 
        dark4_9 = config['dark4_9'] 
        light4_9 = config['light4_9'] 
        dark5_9 = config['dark5_9'] 
        light5_9 = config['light5_9'] 
        dark6_9 = config['dark6_9'] 
        light6_9 = config['light6_9'] 
        
        date1_9 = config['date1_9'] 
        month1_9 = config['month1_9']
        year1_9 = config['year1_9'] 
        date2_9 = config['date2_9'] 
        month2_9 = config['month2_9']
        year2_9 = config['year2_9'] 
        date3_9 = config['date3_9'] 
        month3_9 = config['month3_9']
        year3_9 = config['year3_9'] 
        date4_9 = config['date4_9'] 
        month4_9 = config['month4_9']
        year4_9 = config['year4_9'] 
        date5_9 = config['date5_9'] 
        month5_9 = config['month5_9']
        year5_9 = config['year5_9'] 
        date6_9 = config['date6_9'] 
        month6_9 = config['month6_9']
        year6_9 = config['year6_9'] 

        hourFrom1_9 = config['hourFrom1_9'] 
        minuteFrom1_9 = config['minuteFrom1_9'] 
        hourFrom2_9 = config['hourFrom2_9'] 
        minuteFrom2_9 =config['minuteFrom2_9'] 
        hourFrom3_9 =config['hourFrom3_9'] 
        minuteFrom3_9 =config['minuteFrom3_9'] 
        hourFrom4_9 =config['hourFrom4_9'] 
        minuteFrom4_9 = config['minuteFrom4_9'] 
        hourFrom5_9 = config['hourFrom5_9'] 
        minuteFrom5_9 = config['minuteFrom5_9'] 
        hourFrom6_9 = config['hourFrom6_9'] 
        minuteFrom6_9 = config['minuteFrom6_9'] 


     

    #Phase 10

    
        hourOn1_10 =config['hourOn1_10']  
        minOn1_10 = config['minOn1_10'] 
        hourOff1_10 = config['hourOff1_10'] 
        minOff1_10 =config['minOff1_10']  
        hourOn2_10 = config['hourOn2_10']  
        minOn2_10 = config['minOn2_10'] 
        hourOff2_10 = config['hourOff2_10']
        minOff2_10 = config['minOff2_10']  
        hourOn3_10 = config['hourOn3_10']  
        minOn3_10 = config['minOn3_10'] 
        hourOff3_10 =config['hourOff3_10']
        minOff3_10 = config['minOff3_10'] 
        hourOn4_10 =config['hourOn4_10']  
        minOn4_10 = config['minOn4_10']
        hourOff4_10 = config['hourOff4_10']
        minOff4_10 = config['minOff4_10']  
        hourOn5_10 = config['hourOn5_10']  
        minOn5_10 = config['minOn5_10']
        hourOff5_10 =config['hourOff5_10']
        minOff5_10 =config['minOff5_10']  
        hourOn6_10 = config['hourOn6_10']  
        minOn6_10 = config['minOn6_10']
        hourOff6_10 =config['hourOff6_10']
        minOff6_10 =config['minOff6_10']  
        
        dark1_10 = config['dark1_10'] 
        light1_10 = config['light1_10'] 
        dark2_10 = config['dark2_10'] 
        light2_10 = config['light2_10'] 
        dark3_10 = config['dark3_10'] 
        light3_10 = config['light3_10'] 
        dark4_10 = config['dark4_10'] 
        light4_10 = config['light4_10'] 
        dark5_10 = config['dark5_10'] 
        light5_10 = config['light5_10'] 
        dark6_10 = config['dark6_10'] 
        light6_10 = config['light6_10'] 
        
        date1_10 = config['date1_10'] 
        month1_10 = config['month1_10']
        year1_10 = config['year1_10'] 
        date2_10 = config['date2_10'] 
        month2_10 = config['month2_10']
        year2_10 = config['year2_10'] 
        date3_10 = config['date3_10'] 
        month3_10 = config['month3_10']
        year3_10 = config['year3_10'] 
        date4_10 = config['date4_10'] 
        month4_10 = config['month4_10']
        year4_10 = config['year4_10'] 
        date5_10 = config['date5_10'] 
        month5_10 = config['month5_10']
        year5_10 = config['year5_10'] 
        date6_10 = config['date6_10'] 
        month6_10 = config['month6_10']
        year6_10 = config['year6_10'] 

        hourFrom1_10 = config['hourFrom1_10'] 
        minuteFrom1_10 = config['minuteFrom1_10'] 
        hourFrom2_10 = config['hourFrom2_10'] 
        minuteFrom2_10 =config['minuteFrom2_10'] 
        hourFrom3_10 =config['hourFrom3_10'] 
        minuteFrom3_10 =config['minuteFrom3_10'] 
        hourFrom4_10 =config['hourFrom4_10'] 
        minuteFrom4_10 = config['minuteFrom4_10'] 
        hourFrom5_10 = config['hourFrom5_10'] 
        minuteFrom5_10 = config['minuteFrom5_10'] 
        hourFrom6_10 = config['hourFrom6_10'] 
        minuteFrom6_10 = config['minuteFrom6_10'] 
    

    #Phase 11
    
        hourOn1_11 =config['hourOn1_11']  
        minOn1_11 = config['minOn1_11'] 
        hourOff1_11 = config['hourOff1_11'] 
        minOff1_11 =config['minOff1_11']  
        hourOn2_11 = config['hourOn2_11']  
        minOn2_11 = config['minOn2_11'] 
        hourOff2_11 = config['hourOff2_11']
        minOff2_11 = config['minOff2_11']  
        hourOn3_11 = config['hourOn3_11']  
        minOn3_11 = config['minOn3_11'] 
        hourOff3_11 =config['hourOff3_11']
        minOff3_11 = config['minOff3_11'] 
        hourOn4_11 =config['hourOn4_11']  
        minOn4_11 = config['minOn4_11']
        hourOff4_11 = config['hourOff4_11']
        minOff4_11 = config['minOff4_11']  
        hourOn5_11 = config['hourOn5_11']  
        minOn5_11 = config['minOn5_11']
        hourOff5_11 =config['hourOff5_11']
        minOff5_11 =config['minOff5_11']  
        hourOn6_11 = config['hourOn6_11']  
        minOn6_11 = config['minOn6_11']
        hourOff6_11 =config['hourOff6_11']
        minOff6_11 =config['minOff6_11']  
        
        dark1_11 = config['dark1_11'] 
        light1_11 = config['light1_11'] 
        dark2_11 = config['dark2_11'] 
        light2_11 = config['light2_11'] 
        dark3_11 = config['dark3_11'] 
        light3_11 = config['light3_11'] 
        dark4_11 = config['dark4_11'] 
        light4_11 = config['light4_11'] 
        dark5_11 = config['dark5_11'] 
        light5_11 = config['light5_11'] 
        dark6_11 = config['dark6_11'] 
        light6_11 = config['light6_11'] 
        
        date1_11 = config['date1_11'] 
        month1_11 = config['month1_11']
        year1_11 = config['year1_11'] 
        date2_11 = config['date2_11'] 
        month2_11 = config['month2_11']
        year2_11 = config['year2_11'] 
        date3_11 = config['date3_11'] 
        month3_11 = config['month3_11']
        year3_11 = config['year3_11'] 
        date4_11 = config['date4_11'] 
        month4_11 = config['month4_11']
        year4_11 = config['year4_11'] 
        date5_11 = config['date5_11'] 
        month5_11 = config['month5_11']
        year5_11 = config['year5_11'] 
        date6_11 = config['date6_11'] 
        month6_11 = config['month6_11']
        year6_11 = config['year6_11'] 

        hourFrom1_11 = config['hourFrom1_11'] 
        minuteFrom1_11 = config['minuteFrom1_11'] 
        hourFrom2_11 = config['hourFrom2_11'] 
        minuteFrom2_11 =config['minuteFrom2_11'] 
        hourFrom3_11 =config['hourFrom3_11'] 
        minuteFrom3_11 =config['minuteFrom3_11'] 
        hourFrom4_11 =config['hourFrom4_11'] 
        minuteFrom4_11 = config['minuteFrom4_11'] 
        hourFrom5_11 = config['hourFrom5_11'] 
        minuteFrom5_11 = config['minuteFrom5_11'] 
        hourFrom6_11 = config['hourFrom6_11'] 
        minuteFrom6_11 = config['minuteFrom6_11'] 
    

    #Phase 12
    
        hourOn1_12 =config['hourOn1_12']  
        minOn1_12 = config['minOn1_12'] 
        hourOff1_12 = config['hourOff1_12'] 
        minOff1_12 =config['minOff1_12']  
        hourOn2_12 = config['hourOn2_12']  
        minOn2_12 = config['minOn2_12'] 
        hourOff2_12 = config['hourOff2_12']
        minOff2_12 = config['minOff2_12']  
        hourOn3_12 = config['hourOn3_12']  
        minOn3_12 = config['minOn3_12'] 
        hourOff3_12 =config['hourOff3_12']
        minOff3_12 = config['minOff3_12'] 
        hourOn4_12 =config['hourOn4_12']  
        minOn4_12 = config['minOn4_12']
        hourOff4_12 = config['hourOff4_12']
        minOff4_12 = config['minOff4_12']  
        hourOn5_12 = config['hourOn5_12']  
        minOn5_12 = config['minOn5_12']
        hourOff5_12 =config['hourOff5_12']
        minOff5_12 =config['minOff5_12']  
        hourOn6_12 = config['hourOn6_12']  
        minOn6_12 = config['minOn6_12']
        hourOff6_12 =config['hourOff6_12']
        minOff6_12 =config['minOff6_12']  
        
        dark1_12 = config['dark1_12'] 
        light1_12 = config['light1_12'] 
        dark2_12 = config['dark2_12'] 
        light2_12 = config['light2_12'] 
        dark3_12 = config['dark3_12'] 
        light3_12 = config['light3_12'] 
        dark4_12 = config['dark4_12'] 
        light4_12 = config['light4_12'] 
        dark5_12 = config['dark5_12'] 
        light5_12 = config['light5_12'] 
        dark6_12 = config['dark6_12'] 
        light6_12 = config['light6_12'] 
        
        date1_12 = config['date1_12'] 
        month1_12 = config['month1_12']
        year1_12 = config['year1_12'] 
        date2_12 = config['date2_12'] 
        month2_12 = config['month2_12']
        year2_12 = config['year2_12'] 
        date3_12 = config['date3_12'] 
        month3_12 = config['month3_12']
        year3_12 = config['year3_12'] 
        date4_12 = config['date4_12'] 
        month4_12 = config['month4_12']
        year4_12 = config['year4_12'] 
        date5_12 = config['date5_12'] 
        month5_12 = config['month5_12']
        year5_12 = config['year5_12'] 
        date6_12 = config['date6_12'] 
        month6_12 = config['month6_12']
        year6_12 = config['year6_12'] 

        hourFrom1_12 = config['hourFrom1_12'] 
        minuteFrom1_12 = config['minuteFrom1_12'] 
        hourFrom2_12 = config['hourFrom2_12'] 
        minuteFrom2_12 =config['minuteFrom2_12'] 
        hourFrom3_12 =config['hourFrom3_12'] 
        minuteFrom3_12 =config['minuteFrom3_12'] 
        hourFrom4_12 =config['hourFrom4_12'] 
        minuteFrom4_12 = config['minuteFrom4_12'] 
        hourFrom5_12 = config['hourFrom5_12'] 
        minuteFrom5_12 = config['minuteFrom5_12'] 
        hourFrom6_12 = config['hourFrom6_12'] 
        minuteFrom6_12 = config['minuteFrom6_12'] 

        
        initLED1_str = config['initLED1_str']
        initLED2_str = config['initLED2_str']
        initLED3_str = config['initLED3_str']
        initLED4_str = config['initLED4_str']
        initLED5_str = config['initLED5_str']
        initLED6_str = config['initLED6_str']

        tcycle_1_1 = config['tcycle_1_1']
        tcycle_1_2 = config['tcycle_1_2']
        tcycle_1_3 = config['tcycle_1_3']
        tcycle_1_4 = config['tcycle_1_4']
        tcycle_1_5 = config['tcycle_1_5']
        tcycle_1_6 = config['tcycle_1_6']
        tcycle_1_7 = config['tcycle_1_7']
        tcycle_1_8 = config['tcycle_1_8']
        tcycle_1_9 = config['tcycle_1_9']
        tcycle_1_10 = config['tcycle_1_10']
        tcycle_1_11 = config['tcycle_1_11']
        tcycle_1_12 = config['tcycle_1_12']


        tcycle_2_1 = config['tcycle_2_1']
        tcycle_2_2 = config['tcycle_2_2']
        tcycle_2_3 = config['tcycle_2_3']
        tcycle_2_4 = config['tcycle_2_4']
        tcycle_2_5 = config['tcycle_2_5']
        tcycle_2_6 = config['tcycle_2_6']
        tcycle_2_7 = config['tcycle_2_7']
        tcycle_2_8 = config['tcycle_2_8']
        tcycle_2_9 = config['tcycle_2_9']
        tcycle_2_10 = config['tcycle_2_10']
        tcycle_2_11 = config['tcycle_2_11']
        tcycle_2_12 = config['tcycle_2_12']

        tcycle_3_1 = config['tcycle_3_1']
        tcycle_3_2 = config['tcycle_3_2']
        tcycle_3_3 = config['tcycle_3_3']
        tcycle_3_4 = config['tcycle_3_4']
        tcycle_3_5 = config['tcycle_3_5']
        tcycle_3_6 = config['tcycle_3_6']
        tcycle_3_7 = config['tcycle_3_7']
        tcycle_3_8 = config['tcycle_3_8']
        tcycle_3_9 = config['tcycle_3_9']
        tcycle_3_10 = config['tcycle_3_10']
        tcycle_3_11 = config['tcycle_3_11']
        tcycle_3_12 = config['tcycle_3_12']

        tcycle_4_1 = config['tcycle_4_1']
        tcycle_4_2 = config['tcycle_4_2']
        tcycle_4_3 = config['tcycle_4_3']
        tcycle_4_4 = config['tcycle_4_4']
        tcycle_4_5 = config['tcycle_4_5']
        tcycle_4_6 = config['tcycle_4_6']
        tcycle_4_7 = config['tcycle_4_7']
        tcycle_4_8 = config['tcycle_4_8']
        tcycle_4_9 = config['tcycle_4_9']
        tcycle_4_10 = config['tcycle_4_10']
        tcycle_4_11 = config['tcycle_4_11']
        tcycle_4_12 = config['tcycle_4_12']

        tcycle_5_1 = config['tcycle_5_1']
        tcycle_5_2 = config['tcycle_5_2']
        tcycle_5_3 = config['tcycle_5_3']
        tcycle_5_4 = config['tcycle_5_4']
        tcycle_5_5 = config['tcycle_5_5']
        tcycle_5_6 = config['tcycle_5_6']
        tcycle_5_7 = config['tcycle_5_7']
        tcycle_5_8 = config['tcycle_5_8']
        tcycle_5_9 = config['tcycle_5_9']
        tcycle_5_10 = config['tcycle_5_10']
        tcycle_5_11 = config['tcycle_5_11']
        tcycle_5_12 = config['tcycle_5_12']

        tcycle_6_1 = config['tcycle_6_1']
        tcycle_6_2 = config['tcycle_6_2']
        tcycle_6_3 = config['tcycle_6_3']
        tcycle_6_4 = config['tcycle_6_4']
        tcycle_6_5 = config['tcycle_6_5']
        tcycle_6_6 = config['tcycle_6_6']
        tcycle_6_7 = config['tcycle_6_7']
        tcycle_6_8 = config['tcycle_6_8']
        tcycle_6_9 = config['tcycle_6_9']
        tcycle_6_10 = config['tcycle_6_10']
        tcycle_6_11 = config['tcycle_6_11']
        tcycle_6_12 = config['tcycle_6_12']

    except KeyError:
        
        showinfo("Warning", "The file has less than 12 phases. The phases that are not included in the schedule file will be set to the default values.")
        


#BOX1


    spin1_A_1.delete(0,'end')
    spin1_A_1.insert(0,hourOn1_1)

    spin1_B_1.delete(0,'end')
    spin1_B_1.insert(0,minOn1_1)

    spin1_C_1.delete(0,'end')
    spin1_C_1.insert(0,hourOff1_1)

    spin1_D_1.delete(0,'end')
    spin1_D_1.insert(0,minOff1_1)

    

    date1_2_entry.delete(0,'end')
    today=datetime.date.today() # today
    day_phase2 = today + datetime.timedelta(days=7) # calculate dates for 7 days after recording initiation
    date1_2_entry.insert(0,'{:02d}'.format(day_phase2.day))
    month1_2_entry.delete(0,'end')
    month1_2_entry.insert(0,'{:02d}'.format(day_phase2.month))
    year1_2_entry.delete(0,'end')
    year1_2_entry.insert(0,day_phase2.year) # ISO format is YYYY/MM/DD
    temp_var = inverseDarkLightValue(dark1_1, light1_1)
    var1_1.set(temp_var)
    

    #hourOn1_2, minOn1_2, hourOff1_2, minOff1_2, date1_2, month1_2, year1_2, dark1_2, light1_2, hourFrom1_2, minuteFrom1_2

    spin1_A_2.delete(0,'end')
    spin1_A_2.insert(0,hourOn1_2)
    spin1_B_2.delete(0,'end')
    spin1_B_2.insert(0,minOn1_2)
    spin1_C_2.delete(0,'end')
    spin1_C_2.insert(0,hourOff1_2)
    spin1_D_2.delete(0,'end')
    spin1_D_2.insert(0,minOff1_2)
    spin1_E_2.delete(0,'end')
    spin1_E_2.insert(0,hourFrom1_2)
    spin1_F_2.delete(0,'end')
    spin1_F_2.insert(0,minuteFrom1_2)
    temp_var = inverseDarkLightValue(dark1_2, light1_2)
    var1_2.set(temp_var)



    spin1_E_3.delete(0,'end')
    spin1_E_3.insert(0,hourFrom1_3)
    spin1_F_3.delete(0,'end')
    spin1_F_3.insert(0,minuteFrom1_3)
    day_phase3 = day_phase2 + datetime.timedelta(days=7) # calculate dates for 14 days after recording initiation
    date1_3_entry.delete(0,'end')
    date1_3_entry.insert(0,'{:02d}'.format(day_phase3.day))
    month1_3_entry.delete(0,'end')
    month1_3_entry.insert(0,'{:02d}'.format(day_phase3.month))
    year1_3_entry.delete(0,'end')
    year1_3_entry.insert(0,day_phase3.year)

    spin1_A_3.delete(0,'end')
    spin1_A_3.insert(0,hourOn1_3)
    spin1_B_3.delete(0,'end')
    spin1_B_3.insert(0,minOn1_3)
    spin1_C_3.delete(0,'end')
    spin1_C_3.insert(0,hourOff1_3)
    spin1_D_3.delete(0,'end')
    spin1_D_3.insert(0,minOff1_3)
    temp_var = inverseDarkLightValue(dark1_3, light1_3)
    var1_3.set(temp_var)


    #phase4

    spin1_E_4.delete(0,'end')
    spin1_E_4.insert(0,hourFrom1_4)
    spin1_F_4.delete(0,'end')
    spin1_F_4.insert(0,minuteFrom1_4)
    date1_4_entry.delete(0,'end')
    day_phase4 = day_phase3 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date1_4_entry.delete(0,'end')
    date1_4_entry.insert(0,'{:02d}'.format(day_phase4.day))
    month1_4_entry.delete(0,'end')
    month1_4_entry.insert(0,'{:02d}'.format(day_phase4.month))
    year1_4_entry.delete(0,'end')
    year1_4_entry.insert(0,day_phase4.year)
    spin1_A_4.delete(0,'end')
    spin1_A_4.insert(0,hourOn1_4)
    spin1_B_4.delete(0,'end')
    spin1_B_4.insert(0,hourOn1_4)
    spin1_C_4.delete(0,'end')
    spin1_C_4.insert(0,hourOff1_4)
    spin1_D_4.delete(0,'end')
    spin1_D_4.insert(0,minOff1_4)
    temp_var = inverseDarkLightValue(dark1_4, light1_4)
    var1_4.set(temp_var)


    #phase5
    spin1_E_5.delete(0,'end')
    spin1_E_5.insert(0,hourFrom1_5)
    spin1_F_5.delete(0,'end')
    spin1_F_5.insert(0,minuteFrom1_5)
    date1_5_entry.delete(0,'end')

    day_phase5 = day_phase4 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date1_5_entry.delete(0,'end')
    date1_5_entry.insert(0,'{:02d}'.format(day_phase5.day))
    month1_5_entry.delete(0,'end')
    month1_5_entry.insert(0,'{:02d}'.format(day_phase5.month))
    year1_5_entry.delete(0,'end')
    year1_5_entry.insert(0,day_phase5.year)

    spin1_A_5.delete(0,'end')
    spin1_A_5.insert(0,hourOn1_5)
    spin1_B_5.delete(0,'end')
    spin1_B_5.insert(0,hourOn1_5)
    spin1_C_5.delete(0,'end')
    spin1_C_5.insert(0,hourOff1_5)
    spin1_D_5.delete(0,'end')
    spin1_D_5.insert(0,minOff1_5)
    temp_var = inverseDarkLightValue(dark1_5, light1_5)
    var1_5.set(temp_var)

    #phase6
    spin1_E_6.delete(0,'end')
    spin1_E_6.insert(0,hourFrom1_6)
    spin1_F_6.delete(0,'end')
    spin1_F_6.insert(0,minuteFrom1_6)
    date1_6_entry.delete(0,'end')

    day_phase6 = day_phase5 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date1_6_entry.delete(0,'end')
    date1_6_entry.insert(0,'{:02d}'.format(day_phase6.day))
    month1_6_entry.delete(0,'end')
    month1_6_entry.insert(0,'{:02d}'.format(day_phase6.month))
    year1_6_entry.delete(0,'end')
    year1_6_entry.insert(0,day_phase6.year)
    spin1_A_6.delete(0,'end')
    spin1_A_6.insert(0,hourOn1_6)
    spin1_B_6.delete(0,'end')
    spin1_B_6.insert(0,hourOn1_6)
    spin1_C_6.delete(0,'end')
    spin1_C_6.insert(0,hourOff1_6)
    spin1_D_6.delete(0,'end')
    spin1_D_6.insert(0,minOff1_6)
    temp_var = inverseDarkLightValue(dark1_6, light1_6)
    var1_6.set(temp_var)

    #phase 7
    spin1_E_7.delete(0,'end')
    spin1_E_7.insert(0,hourFrom1_7)
    spin1_F_7.delete(0,'end')
    spin1_F_7.insert(0,minuteFrom1_7)
    date1_7_entry.delete(0,'end')
    day_phase7 = day_phase6 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date1_7_entry.delete(0,'end')
    date1_7_entry.insert(0,'{:02d}'.format(day_phase7.day))
    month1_7_entry.delete(0,'end')
    month1_7_entry.insert(0,'{:02d}'.format(day_phase7.month))
    year1_7_entry.delete(0,'end')
    year1_7_entry.insert(0,day_phase7.year)
    spin1_A_7.delete(0,'end')
    spin1_A_7.insert(0,hourOn1_7)
    spin1_B_7.delete(0,'end')
    spin1_B_7.insert(0,hourOn1_7)
    spin1_C_7.delete(0,'end')
    spin1_C_7.insert(0,hourOff1_7)
    spin1_D_7.delete(0,'end')
    spin1_D_7.insert(0,minOff1_7)
    temp_var = inverseDarkLightValue(dark1_7, light1_7)
    var1_7.set(temp_var)

    #phase8
    spin1_E_8.delete(0,'end')
    spin1_E_8.insert(0,hourFrom1_8)
    spin1_F_8.delete(0,'end')
    spin1_F_8.insert(0,minuteFrom1_8)
    date1_8_entry.delete(0,'end')
    day_phase8 = day_phase7 + datetime.timedelta(days=7)
    date1_8_entry.insert(0,'{:02d}'.format(day_phase8.day))
    month1_8_entry.delete(0,'end')
    month1_8_entry.insert(0,'{:02d}'.format(day_phase8.month))
    year1_8_entry.delete(0,'end')
    year1_8_entry.insert(0,day_phase8.year)
    spin1_A_8.delete(0,'end')
    spin1_A_8.insert(0,hourOn1_8)
    spin1_B_8.delete(0,'end')
    spin1_B_8.insert(0,hourOn1_8)
    spin1_C_8.delete(0,'end')
    spin1_C_8.insert(0,hourOff1_8)
    spin1_D_8.delete(0,'end')
    spin1_D_8.insert(0,minOff1_8)
    temp_var = inverseDarkLightValue(dark1_8, light1_8)
    var1_8.set(temp_var)

    #phase9

    spin1_E_9.delete(0,'end')
    spin1_E_9.insert(0,hourFrom1_9)
    spin1_F_9.delete(0,'end')
    spin1_F_9.insert(0,minuteFrom1_9)
    date1_9_entry.delete(0,'end')
    day_phase9 = day_phase8 + datetime.timedelta(days=7)
    date1_9_entry.insert(0,'{:02d}'.format(day_phase9.day))
    month1_9_entry.delete(0,'end')
    month1_9_entry.insert(0,'{:02d}'.format(day_phase9.month))
    year1_9_entry.delete(0,'end')
    year1_9_entry.insert(0,day_phase9.year)
    spin1_A_9.delete(0,'end')
    spin1_A_9.insert(0,hourOn1_9)
    spin1_B_9.delete(0,'end')
    spin1_B_9.insert(0,hourOn1_9)
    spin1_C_9.delete(0,'end')
    spin1_C_9.insert(0,hourOff1_9)
    spin1_D_9.delete(0,'end')
    spin1_D_9.insert(0,minOff1_9)
    temp_var = inverseDarkLightValue(dark1_9, light1_9)
    var1_9.set(temp_var)


    #phase10

    spin1_E_10.delete(0,'end')
    spin1_E_10.insert(0,hourFrom1_10)
    spin1_F_10.delete(0,'end')
    spin1_F_10.insert(0,minuteFrom1_10)
    date1_10_entry.delete(0,'end')
    day_phase10 = day_phase9 + datetime.timedelta(days=7)
    date1_10_entry.insert(0,'{:02d}'.format(day_phase10.day))
    month1_10_entry.delete(0,'end')
    month1_10_entry.insert(0,'{:02d}'.format(day_phase10.month))
    year1_10_entry.delete(0,'end')
    year1_10_entry.insert(0,day_phase10.year)
    spin1_A_10.delete(0,'end')
    spin1_A_10.insert(0,hourOn1_10)
    spin1_B_10.delete(0,'end')
    spin1_B_10.insert(0,hourOn1_10)
    spin1_C_10.delete(0,'end')
    spin1_C_10.insert(0,hourOff1_10)
    spin1_D_10.delete(0,'end')
    spin1_D_10.insert(0,minOff1_10)
    temp_var = inverseDarkLightValue(dark1_10, light1_10)
    var1_10.set(temp_var)

    #phase11

    spin1_E_11.delete(0,'end')
    spin1_E_11.insert(0,hourFrom1_11)
    spin1_F_11.delete(0,'end')
    spin1_F_11.insert(0,minuteFrom1_11)
    date1_11_entry.delete(0,'end')
    day_phase11 = day_phase10 + datetime.timedelta(days=7)
    date1_11_entry.insert(0,'{:02d}'.format(day_phase10.day))
    month1_11_entry.delete(0,'end')
    month1_11_entry.insert(0,'{:02d}'.format(day_phase10.month))
    year1_11_entry.delete(0,'end')
    year1_11_entry.insert(0,day_phase10.year)
    spin1_A_11.delete(0,'end')
    spin1_A_11.insert(0,hourOn1_11)
    spin1_B_11.delete(0,'end')
    spin1_B_11.insert(0,hourOn1_11)
    spin1_C_11.delete(0,'end')
    spin1_C_11.insert(0,hourOff1_11)
    spin1_D_11.delete(0,'end')
    spin1_D_11.insert(0,minOff1_11)
    temp_var = inverseDarkLightValue(dark1_11, light1_11)
    var1_11.set(temp_var)

    #phase12

    spin1_E_12.delete(0,'end')
    spin1_E_12.insert(0,hourFrom1_12)
    spin1_F_12.delete(0,'end')
    spin1_F_12.insert(0,minuteFrom1_12)
    date1_12_entry.delete(0,'end')
    day_phase12 = day_phase11 + datetime.timedelta(days=7)
    date1_12_entry.insert(0,'{:02d}'.format(day_phase11.day))
    month1_12_entry.delete(0,'end')
    month1_12_entry.insert(0,'{:02d}'.format(day_phase11.month))
    year1_12_entry.delete(0,'end')
    year1_12_entry.insert(0,day_phase11.year)
    spin1_A_12.delete(0,'end')
    spin1_A_12.insert(0,hourOn1_12)
    spin1_B_12.delete(0,'end')
    spin1_B_12.insert(0,hourOn1_12)
    spin1_C_12.delete(0,'end')
    spin1_C_12.insert(0,hourOff1_12)
    spin1_D_12.delete(0,'end')
    spin1_D_12.insert(0,minOff1_12)
    temp_var = inverseDarkLightValue(dark1_12, light1_12)
    var1_12.set(temp_var)


    #BOX2

    spin2_A_1.delete(0,'end')
    spin2_A_1.insert(0,hourOn2_1)

    spin2_B_1.delete(0,'end')
    spin2_B_1.insert(0,minOn2_1)

    spin2_C_1.delete(0,'end')
    spin2_C_1.insert(0,hourOff2_1)

    spin2_D_1.delete(0,'end')
    spin2_D_1.insert(0,minOff2_1)
    temp_var = inverseDarkLightValue(dark2_1, light2_1)
    var2_1.set(temp_var)


    spin2_E_2.delete(0,'end')
    spin2_E_2.insert(0,hourFrom2_2)
    spin2_F_2.delete(0,'end')
    spin2_F_2.insert(0,minuteFrom2_2)
    date2_2_entry.delete(0,'end')
    today=datetime.date.today() # today
    day_phase2 = today + datetime.timedelta(days=7) # calculate dates for 7 days after recording initiation
    date2_2_entry.insert(0,'{:02d}'.format(day_phase2.day))
    month2_2_entry.delete(0,'end')
    month2_2_entry.insert(0,'{:02d}'.format(day_phase2.month))
    year2_2_entry.delete(0,'end')
    year2_2_entry.insert(0,day_phase2.year) # ISO format is YYYY/MM/DD
    spin2_A_2.delete(0,'end')
    spin2_A_2.insert(0,hourOn2_2)
    spin2_B_2.delete(0,'end')
    spin2_B_2.insert(0,minOn2_2)
    spin2_C_2.delete(0,'end')
    spin2_C_2.insert(0,hourOff2_2)
    spin2_D_2.delete(0,'end')
    spin2_D_2.insert(0,minOff2_2)
    temp_var = inverseDarkLightValue(dark2_2, light2_2)
    var2_2.set(temp_var)


    spin2_E_3.delete(0,'end')
    spin2_E_3.insert(0,hourFrom2_3)
    spin2_F_3.delete(0,'end')
    spin2_F_3.insert(0,minuteFrom2_3)
    day_phase3 = day_phase2 + datetime.timedelta(days=7) # calculate dates for 14 days after recording initiation
    date2_3_entry.delete(0,'end')
    date2_3_entry.insert(0,'{:02d}'.format(day_phase3.day))
    month2_3_entry.delete(0,'end')
    month2_3_entry.insert(0,'{:02d}'.format(day_phase3.month))
    year2_3_entry.delete(0,'end')
    year2_3_entry.insert(0,day_phase3.year)
    spin2_A_3.delete(0,'end')
    spin2_A_3.insert(0,hourOn2_3)
    spin2_B_3.delete(0,'end')
    spin2_B_3.insert(0,minOn2_3)
    spin2_C_3.delete(0,'end')
    spin2_C_3.insert(0,hourOff2_3)
    spin2_D_3.delete(0,'end')
    spin2_D_3.insert(0,minOff2_3)
    temp_var = inverseDarkLightValue(dark2_3, light2_3)
    var2_3.set(temp_var)


    #phase4

    spin2_E_4.delete(0,'end')
    spin2_E_4.insert(0,hourFrom2_4)
    spin2_F_4.delete(0,'end')
    spin2_F_4.insert(0,minuteFrom2_4)
    date2_4_entry.delete(0,'end')
    day_phase4 = day_phase3 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date2_4_entry.delete(0,'end')
    date2_4_entry.insert(0,'{:02d}'.format(day_phase4.day))
    month2_4_entry.delete(0,'end')
    month2_4_entry.insert(0,'{:02d}'.format(day_phase4.month))
    year2_4_entry.delete(0,'end')
    year2_4_entry.insert(0,day_phase4.year)
    spin2_A_4.delete(0,'end')
    spin2_A_4.insert(0,hourOn2_4)
    spin2_B_4.delete(0,'end')
    spin2_B_4.insert(0,hourOn2_4)
    spin2_C_4.delete(0,'end')
    spin2_C_4.insert(0,hourOff2_4)
    spin2_D_4.delete(0,'end')
    spin2_D_4.insert(0,minOff2_4)
    temp_var = inverseDarkLightValue(dark2_4, light2_4)
    var2_4.set(temp_var)


    #phase5
    spin2_E_5.delete(0,'end')
    spin2_E_5.insert(0,hourFrom2_5)
    spin2_F_5.delete(0,'end')
    spin2_F_5.insert(0,minuteFrom2_5)
    date2_5_entry.delete(0,'end')

    day_phase5 = day_phase4 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date2_5_entry.delete(0,'end')
    date2_5_entry.insert(0,'{:02d}'.format(day_phase5.day))
    month2_5_entry.delete(0,'end')
    month2_5_entry.insert(0,'{:02d}'.format(day_phase5.month))
    year2_5_entry.delete(0,'end')
    year2_5_entry.insert(0,day_phase5.year)

    spin2_A_5.delete(0,'end')
    spin2_A_5.insert(0,hourOn2_5)
    spin2_B_5.delete(0,'end')
    spin2_B_5.insert(0,hourOn2_5)
    spin2_C_5.delete(0,'end')
    spin2_C_5.insert(0,hourOff2_5)
    spin2_D_5.delete(0,'end')
    spin2_D_5.insert(0,minOff2_5)
    temp_var = inverseDarkLightValue(dark2_5, light2_5)
    var2_5.set(temp_var)

    #phase6
    spin2_E_6.delete(0,'end')
    spin2_E_6.insert(0,hourFrom2_6)
    spin2_F_6.delete(0,'end')
    spin2_F_6.insert(0,minuteFrom2_6)
    date2_6_entry.delete(0,'end')

    day_phase6 = day_phase5 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date2_6_entry.delete(0,'end')
    date2_6_entry.insert(0,'{:02d}'.format(day_phase6.day))
    month2_6_entry.delete(0,'end')
    month2_6_entry.insert(0,'{:02d}'.format(day_phase6.month))
    year2_6_entry.delete(0,'end')
    year2_6_entry.insert(0,day_phase6.year)
    spin2_A_6.delete(0,'end')
    spin2_A_6.insert(0,hourOn2_6)
    spin2_B_6.delete(0,'end')
    spin2_B_6.insert(0,hourOn2_6)
    spin2_C_6.delete(0,'end')
    spin2_C_6.insert(0,hourOff2_6)
    spin2_D_6.delete(0,'end')
    spin2_D_6.insert(0,minOff2_6)
    temp_var = inverseDarkLightValue(dark2_6, light2_6)
    var2_6.set(temp_var)

    #phase 7
    spin2_E_7.delete(0,'end')
    spin2_E_7.insert(0,hourFrom2_7)
    spin2_F_7.delete(0,'end')
    spin2_F_7.insert(0,minuteFrom2_7)
    date2_7_entry.delete(0,'end')
    day_phase7 = day_phase6 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date2_7_entry.delete(0,'end')
    date2_7_entry.insert(0,'{:02d}'.format(day_phase7.day))
    month2_7_entry.delete(0,'end')
    month2_7_entry.insert(0,'{:02d}'.format(day_phase7.month))
    year2_7_entry.delete(0,'end')
    year2_7_entry.insert(0,day_phase7.year)
    spin2_A_7.delete(0,'end')
    spin2_A_7.insert(0,hourOn2_7)
    spin2_B_7.delete(0,'end')
    spin2_B_7.insert(0,hourOn2_7)
    spin2_C_7.delete(0,'end')
    spin2_C_7.insert(0,hourOff2_7)
    spin2_D_7.delete(0,'end')
    spin2_D_7.insert(0,minOff2_7)
    temp_var = inverseDarkLightValue(dark2_7, light2_7)
    var2_7.set(temp_var)

    #phase8
    spin2_E_8.delete(0,'end')
    spin2_E_8.insert(0,hourFrom2_8)
    spin2_F_8.delete(0,'end')
    spin2_F_8.insert(0,minuteFrom2_8)
    date2_8_entry.delete(0,'end')
    day_phase8 = day_phase7 + datetime.timedelta(days=7)
    date2_8_entry.insert(0,'{:02d}'.format(day_phase8.day))
    month2_8_entry.delete(0,'end')
    month2_8_entry.insert(0,'{:02d}'.format(day_phase8.month))
    year2_8_entry.delete(0,'end')
    year2_8_entry.insert(0,day_phase8.year)
    spin2_A_8.delete(0,'end')
    spin2_A_8.insert(0,hourOn2_8)
    spin2_B_8.delete(0,'end')
    spin2_B_8.insert(0,hourOn2_8)
    spin2_C_8.delete(0,'end')
    spin2_C_8.insert(0,hourOff2_8)
    spin2_D_8.delete(0,'end')
    spin2_D_8.insert(0,minOff2_8)
    temp_var = inverseDarkLightValue(dark2_8, light2_8)
    var2_8.set(temp_var)

    #phase9

    spin2_E_9.delete(0,'end')
    spin2_E_9.insert(0,hourFrom2_9)
    spin2_F_9.delete(0,'end')
    spin2_F_9.insert(0,minuteFrom2_9)
    date2_9_entry.delete(0,'end')
    day_phase9 = day_phase8 + datetime.timedelta(days=7)
    date2_9_entry.insert(0,'{:02d}'.format(day_phase9.day))
    month2_9_entry.delete(0,'end')
    month2_9_entry.insert(0,'{:02d}'.format(day_phase9.month))
    year2_9_entry.delete(0,'end')
    year2_9_entry.insert(0,day_phase9.year)
    spin2_A_9.delete(0,'end')
    spin2_A_9.insert(0,hourOn2_9)
    spin2_B_9.delete(0,'end')
    spin2_B_9.insert(0,hourOn2_9)
    spin2_C_9.delete(0,'end')
    spin2_C_9.insert(0,hourOff2_9)
    spin2_D_9.delete(0,'end')
    spin2_D_9.insert(0,minOff2_9)
    temp_var = inverseDarkLightValue(dark2_9, light2_9)
    var2_9.set(temp_var)


    #phase10

    spin2_E_10.delete(0,'end')
    spin2_E_10.insert(0,hourFrom2_10)
    spin2_F_10.delete(0,'end')
    spin2_F_10.insert(0,minuteFrom2_10)
    date2_10_entry.delete(0,'end')
    day_phase10 = day_phase9 + datetime.timedelta(days=7)
    date2_10_entry.insert(0,'{:02d}'.format(day_phase10.day))
    month2_10_entry.delete(0,'end')
    month2_10_entry.insert(0,'{:02d}'.format(day_phase10.month))
    year2_10_entry.delete(0,'end')
    year2_10_entry.insert(0,day_phase10.year)
    spin2_A_10.delete(0,'end')
    spin2_A_10.insert(0,hourOn2_10)
    spin2_B_10.delete(0,'end')
    spin2_B_10.insert(0,hourOn2_10)
    spin2_C_10.delete(0,'end')
    spin2_C_10.insert(0,hourOff2_10)
    spin2_D_10.delete(0,'end')
    spin2_D_10.insert(0,minOff2_10)
    temp_var = inverseDarkLightValue(dark2_10, light2_10)
    var2_10.set(temp_var)

    #phase11

    spin2_E_11.delete(0,'end')
    spin2_E_11.insert(0,hourFrom2_11)
    spin2_F_11.delete(0,'end')
    spin2_F_11.insert(0,minuteFrom2_11)
    date2_12_entry.delete(0,'end')
    day_phase11 = day_phase10 + datetime.timedelta(days=7)
    date2_12_entry.insert(0,'{:02d}'.format(day_phase10.day))
    month2_12_entry.delete(0,'end')
    month2_12_entry.insert(0,'{:02d}'.format(day_phase10.month))
    year2_12_entry.delete(0,'end')
    year2_12_entry.insert(0,day_phase10.year)
    spin2_A_11.delete(0,'end')
    spin2_A_11.insert(0,hourOn2_11)
    spin2_B_11.delete(0,'end')
    spin2_B_11.insert(0,hourOn2_11)
    spin2_C_11.delete(0,'end')
    spin2_C_11.insert(0,hourOff2_11)
    spin2_D_11.delete(0,'end')
    spin2_D_11.insert(0,minOff2_11)
    temp_var = inverseDarkLightValue(dark2_11, light2_11)
    var2_11.set(temp_var)

    #phase12

    spin2_E_12.delete(0,'end')
    spin2_E_12.insert(0,hourFrom2_12)
    spin2_F_12.delete(0,'end')
    spin2_F_12.insert(0,minuteFrom2_12)
    date2_12_entry.delete(0,'end')
    day_phase12 = day_phase11 + datetime.timedelta(days=7)
    date2_12_entry.insert(0,'{:02d}'.format(day_phase11.day))
    month2_12_entry.delete(0,'end')
    month2_12_entry.insert(0,'{:02d}'.format(day_phase11.month))
    year2_12_entry.delete(0,'end')
    year2_12_entry.insert(0,day_phase11.year)
    spin2_A_12.delete(0,'end')
    spin2_A_12.insert(0,hourOn2_12)
    spin2_B_12.delete(0,'end')
    spin2_B_12.insert(0,hourOn2_12)
    spin2_C_12.delete(0,'end')
    spin2_C_12.insert(0,hourOff2_12)
    spin2_D_12.delete(0,'end')
    spin2_D_12.insert(0,minOff2_12)
    temp_var = inverseDarkLightValue(dark2_12, light2_12)
    var2_12.set(temp_var)



    #BOX 3

    spin3_A_1.delete(0,'end')
    spin3_A_1.insert(0,hourOn3_1)

    spin3_B_1.delete(0,'end')
    spin3_B_1.insert(0,minOn3_1)

    spin3_C_1.delete(0,'end')
    spin3_C_1.insert(0,hourOff3_1)

    spin3_D_1.delete(0,'end')
    spin3_D_1.insert(0,minOff3_1)
    temp_var = inverseDarkLightValue(dark3_1, light3_1)
    var3_1.set(temp_var)

    spin3_E_2.delete(0,'end')
    spin3_E_2.insert(0,hourFrom3_2)

    spin3_F_2.delete(0,'end')
    spin3_F_2.insert(0,minuteFrom3_2)

    date3_2_entry.delete(0,'end')
    today=datetime.date.today() # today
    day_phase2 = today + datetime.timedelta(days=7) # calculate dates for 7 days after recording initiation
    date3_2_entry.insert(0,'{:02d}'.format(day_phase2.day))
    month3_2_entry.delete(0,'end')
    month3_2_entry.insert(0,'{:02d}'.format(day_phase2.month))
    year3_2_entry.delete(0,'end')
    year3_2_entry.insert(0,day_phase2.year) # ISO format is YYYY/MM/DD

    spin3_A_2.delete(0,'end')
    spin3_A_2.insert(0,hourOn3_2)
    spin3_B_2.delete(0,'end')
    spin3_B_2.insert(0,minOn3_2)
    spin3_C_2.delete(0,'end')
    spin3_C_2.insert(0,hourOff3_2)
    spin3_D_2.delete(0,'end')
    spin3_D_2.insert(0,minOff3_2)
    temp_var = inverseDarkLightValue(dark3_2, light3_2)
    var3_2.set(temp_var)

    spin3_E_3.delete(0,'end')
    spin3_E_3.insert(0,hourFrom3_3)
    spin3_F_3.delete(0,'end')
    spin3_F_3.insert(0,minuteFrom3_3)
    day_phase3 = day_phase2 + datetime.timedelta(days=7) # calculate dates for 14 days after recording initiation
    date3_3_entry.delete(0,'end')
    date3_3_entry.insert(0,'{:02d}'.format(day_phase3.day))
    month3_3_entry.delete(0,'end')
    month3_3_entry.insert(0,'{:02d}'.format(day_phase3.month))
    year3_3_entry.delete(0,'end')
    year3_3_entry.insert(0,day_phase3.year)

    spin3_A_3.delete(0,'end')
    spin3_A_3.insert(0,hourOn3_3)
    spin3_B_3.delete(0,'end')
    spin3_B_3.insert(0,minOn3_3)
    spin3_C_3.delete(0,'end')
    spin3_C_3.insert(0,hourOff3_3)
    spin3_D_3.delete(0,'end')
    spin3_D_3.insert(0,minOff3_3)
    temp_var = inverseDarkLightValue(dark3_3, light3_3)
    var3_3.set(temp_var)


    #phase4

    spin3_E_4.delete(0,'end')
    spin3_E_4.insert(0,hourFrom3_4)
    spin3_F_4.delete(0,'end')
    spin3_F_4.insert(0,minuteFrom3_4)
    date3_4_entry.delete(0,'end')
    day_phase4 = day_phase3 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date3_4_entry.delete(0,'end')
    date3_4_entry.insert(0,'{:02d}'.format(day_phase4.day))
    month3_4_entry.delete(0,'end')
    month3_4_entry.insert(0,'{:02d}'.format(day_phase4.month))
    year3_4_entry.delete(0,'end')
    year3_4_entry.insert(0,day_phase4.year)
    spin3_A_4.delete(0,'end')
    spin3_A_4.insert(0,hourOn3_4)
    spin3_B_4.delete(0,'end')
    spin3_B_4.insert(0,hourOn3_4)
    spin3_C_4.delete(0,'end')
    spin3_C_4.insert(0,hourOff3_4)
    spin3_D_4.delete(0,'end')
    spin3_D_4.insert(0,minOff3_4)
    temp_var = inverseDarkLightValue(dark3_4, light3_4)
    var3_4.set(temp_var)


    #phase5
    spin3_E_5.delete(0,'end')
    spin3_E_5.insert(0,hourFrom3_5)
    spin3_F_5.delete(0,'end')
    spin3_F_5.insert(0,minuteFrom3_5)
    date3_5_entry.delete(0,'end')

    day_phase5 = day_phase4 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date3_5_entry.delete(0,'end')
    date3_5_entry.insert(0,'{:02d}'.format(day_phase5.day))
    month3_5_entry.delete(0,'end')
    month3_5_entry.insert(0,'{:02d}'.format(day_phase5.month))
    year3_5_entry.delete(0,'end')
    year3_5_entry.insert(0,day_phase5.year)

    spin3_A_5.delete(0,'end')
    spin3_A_5.insert(0,hourOn3_5)
    spin3_B_5.delete(0,'end')
    spin3_B_5.insert(0,hourOn3_5)
    spin3_C_5.delete(0,'end')
    spin3_C_5.insert(0,hourOff3_5)
    spin3_D_5.delete(0,'end')
    spin3_D_5.insert(0,minOff3_5)
    temp_var = inverseDarkLightValue(dark3_5, light3_5)
    var3_5.set(temp_var)

    #phase6
    spin3_E_6.delete(0,'end')
    spin3_E_6.insert(0,hourFrom3_6)
    spin3_F_6.delete(0,'end')
    spin3_F_6.insert(0,minuteFrom3_6)
    date3_6_entry.delete(0,'end')

    day_phase6 = day_phase5 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date3_6_entry.delete(0,'end')
    date3_6_entry.insert(0,'{:02d}'.format(day_phase6.day))
    month3_6_entry.delete(0,'end')
    month3_6_entry.insert(0,'{:02d}'.format(day_phase6.month))
    year3_6_entry.delete(0,'end')
    year3_6_entry.insert(0,day_phase6.year)
    spin3_A_6.delete(0,'end')
    spin3_A_6.insert(0,hourOn3_6)
    spin3_B_6.delete(0,'end')
    spin3_B_6.insert(0,hourOn3_6)
    spin3_C_6.delete(0,'end')
    spin3_C_6.insert(0,hourOff3_6)
    spin3_D_6.delete(0,'end')
    spin3_D_6.insert(0,minOff3_6)
    temp_var = inverseDarkLightValue(dark3_6, light3_6)
    var3_6.set(temp_var)

    #phase 7
    spin3_E_7.delete(0,'end')
    spin3_E_7.insert(0,hourFrom3_7)
    spin3_F_7.delete(0,'end')
    spin3_F_7.insert(0,minuteFrom3_7)
    date3_7_entry.delete(0,'end')
    day_phase7 = day_phase6 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date3_7_entry.delete(0,'end')
    date3_7_entry.insert(0,'{:02d}'.format(day_phase7.day))
    month3_7_entry.delete(0,'end')
    month3_7_entry.insert(0,'{:02d}'.format(day_phase7.month))
    year3_7_entry.delete(0,'end')
    year3_7_entry.insert(0,day_phase7.year)
    spin3_A_7.delete(0,'end')
    spin3_A_7.insert(0,hourOn3_7)
    spin3_B_7.delete(0,'end')
    spin3_B_7.insert(0,hourOn3_7)
    spin3_C_7.delete(0,'end')
    spin3_C_7.insert(0,hourOff3_7)
    spin3_D_7.delete(0,'end')
    spin3_D_7.insert(0,minOff3_7)
    temp_var = inverseDarkLightValue(dark3_7, light3_7)
    var3_7.set(temp_var)

    #phase8
    spin3_E_8.delete(0,'end')
    spin3_E_8.insert(0,hourFrom3_8)
    spin3_F_8.delete(0,'end')
    spin3_F_8.insert(0,minuteFrom3_8)
    date3_8_entry.delete(0,'end')
    day_phase8 = day_phase7 + datetime.timedelta(days=7)
    date3_8_entry.insert(0,'{:02d}'.format(day_phase8.day))
    month3_8_entry.delete(0,'end')
    month3_8_entry.insert(0,'{:02d}'.format(day_phase8.month))
    year3_8_entry.delete(0,'end')
    year3_8_entry.insert(0,day_phase8.year)
    spin3_A_8.delete(0,'end')
    spin3_A_8.insert(0,hourOn3_8)
    spin3_B_8.delete(0,'end')
    spin3_B_8.insert(0,hourOn3_8)
    spin3_C_8.delete(0,'end')
    spin3_C_8.insert(0,hourOff3_8)
    spin3_D_8.delete(0,'end')
    spin3_D_8.insert(0,minOff3_8)
    temp_var = inverseDarkLightValue(dark3_8, light3_8)
    var3_8.set(temp_var)

    #phase9

    spin3_E_9.delete(0,'end')
    spin3_E_9.insert(0,hourFrom3_9)
    spin3_F_9.delete(0,'end')
    spin3_F_9.insert(0,minuteFrom3_9)
    date3_9_entry.delete(0,'end')
    day_phase9 = day_phase8 + datetime.timedelta(days=7)
    date3_9_entry.insert(0,'{:02d}'.format(day_phase9.day))
    month3_9_entry.delete(0,'end')
    month3_9_entry.insert(0,'{:02d}'.format(day_phase9.month))
    year3_9_entry.delete(0,'end')
    year3_9_entry.insert(0,day_phase9.year)
    spin3_A_9.delete(0,'end')
    spin3_A_9.insert(0,hourOn3_9)
    spin3_B_9.delete(0,'end')
    spin3_B_9.insert(0,hourOn3_9)
    spin3_C_9.delete(0,'end')
    spin3_C_9.insert(0,hourOff3_9)
    spin3_D_9.delete(0,'end')
    spin3_D_9.insert(0,minOff3_9)
    temp_var = inverseDarkLightValue(dark3_9, light3_9)
    var3_9.set(temp_var)


    #phase10

    spin3_E_10.delete(0,'end')
    spin3_E_10.insert(0,hourFrom3_10)
    spin3_F_10.delete(0,'end')
    spin3_F_10.insert(0,minuteFrom3_10)
    date3_10_entry.delete(0,'end')
    day_phase10 = day_phase9 + datetime.timedelta(days=7)
    date3_10_entry.insert(0,'{:02d}'.format(day_phase10.day))
    month3_10_entry.delete(0,'end')
    month3_10_entry.insert(0,'{:02d}'.format(day_phase10.month))
    year3_10_entry.delete(0,'end')
    year3_10_entry.insert(0,day_phase10.year)
    spin3_A_10.delete(0,'end')
    spin3_A_10.insert(0,hourOn3_10)
    spin3_B_10.delete(0,'end')
    spin3_B_10.insert(0,hourOn3_10)
    spin3_C_10.delete(0,'end')
    spin3_C_10.insert(0,hourOff3_10)
    spin3_D_10.delete(0,'end')
    spin3_D_10.insert(0,minOff3_10)
    temp_var = inverseDarkLightValue(dark3_10, light3_10)
    var3_10.set(temp_var)

    #phase11

    spin3_E_11.delete(0,'end')
    spin3_E_11.insert(0,hourFrom3_11)
    spin3_F_11.delete(0,'end')
    spin3_F_11.insert(0,minuteFrom3_11)
    date3_11_entry.delete(0,'end')
    day_phase11 = day_phase10 + datetime.timedelta(days=7)
    date3_11_entry.insert(0,'{:02d}'.format(day_phase10.day))
    month3_11_entry.delete(0,'end')
    month3_11_entry.insert(0,'{:02d}'.format(day_phase10.month))
    year3_11_entry.delete(0,'end')
    year3_11_entry.insert(0,day_phase10.year)
    spin3_A_11.delete(0,'end')
    spin3_A_11.insert(0,hourOn3_11)
    spin3_B_11.delete(0,'end')
    spin3_B_11.insert(0,hourOn3_11)
    spin3_C_11.delete(0,'end')
    spin3_C_11.insert(0,hourOff3_11)
    spin3_D_11.delete(0,'end')
    spin3_D_11.insert(0,minOff3_11)
    temp_var = inverseDarkLightValue(dark3_11, light3_11)
    var3_11.set(temp_var)

    #phase12

    spin3_E_12.delete(0,'end')
    spin3_E_12.insert(0,hourFrom3_12)
    spin3_F_12.delete(0,'end')
    spin3_F_12.insert(0,minuteFrom3_12)
    date3_12_entry.delete(0,'end')
    day_phase12 = day_phase11 + datetime.timedelta(days=7)
    date3_12_entry.insert(0,'{:02d}'.format(day_phase11.day))
    month3_12_entry.delete(0,'end')
    month3_12_entry.insert(0,'{:02d}'.format(day_phase11.month))
    year3_12_entry.delete(0,'end')
    year3_12_entry.insert(0,day_phase11.year)
    spin3_A_12.delete(0,'end')
    spin3_A_12.insert(0,hourOn3_12)
    spin3_B_12.delete(0,'end')
    spin3_B_12.insert(0,hourOn3_12)
    spin3_C_12.delete(0,'end')
    spin3_C_12.insert(0,hourOff3_12)
    spin3_D_12.delete(0,'end')
    spin3_D_12.insert(0,minOff3_12)
    temp_var = inverseDarkLightValue(dark3_12, light3_12)
    var3_12.set(temp_var)


    #BOX 4
    spin4_A_1.delete(0,'end')
    spin4_A_1.insert(0,hourOn4_1)

    spin4_B_1.delete(0,'end')
    spin4_B_1.insert(0,minOn4_1)

    spin4_C_1.delete(0,'end')
    spin4_C_1.insert(0,hourOff4_1)

    spin4_D_1.delete(0,'end')
    spin4_D_1.insert(0,minOff4_1)

    temp_var = inverseDarkLightValue(dark4_1, light4_1)
    var4_1.set(temp_var)

    spin4_E_2.delete(0,'end')
    spin4_E_2.insert(0,hourFrom4_2)

    spin4_F_2.delete(0,'end')
    spin4_F_2.insert(0,minuteFrom4_2)

    date4_2_entry.delete(0,'end')
    today=datetime.date.today() # today
    day_phase2 = today + datetime.timedelta(days=7) # calculate dates for 7 days after recording initiation
    date4_2_entry.insert(0,'{:02d}'.format(day_phase2.day))
    month4_2_entry.delete(0,'end')
    month4_2_entry.insert(0,'{:02d}'.format(day_phase2.month))
    year4_2_entry.delete(0,'end')
    year4_2_entry.insert(0,day_phase2.year) # ISO format is YYYY/MM/DD

    spin4_A_2.delete(0,'end')
    spin4_A_2.insert(0,hourOn4_2)
    spin4_B_2.delete(0,'end')
    spin4_B_2.insert(0,minOn4_2)
    spin4_C_2.delete(0,'end')
    spin4_C_2.insert(0,hourOff4_2)
    spin4_D_2.delete(0,'end')
    spin4_D_2.insert(0,minOff4_2)

    temp_var = inverseDarkLightValue(dark4_2, light4_2)
    var4_2.set(temp_var)

    spin4_E_3.delete(0,'end')
    spin4_E_3.insert(0,hourFrom4_3)
    spin4_F_3.delete(0,'end')
    spin4_F_3.insert(0,minuteFrom4_3)
    day_phase3 = day_phase2 + datetime.timedelta(days=7) # calculate dates for 14 days after recording initiation
    date4_3_entry.delete(0,'end')
    date4_3_entry.insert(0,'{:02d}'.format(day_phase3.day))
    month4_3_entry.delete(0,'end')
    month4_3_entry.insert(0,'{:02d}'.format(day_phase3.month))
    year4_3_entry.delete(0,'end')
    year4_3_entry.insert(0,day_phase3.year)

    spin4_A_3.delete(0,'end')
    spin4_A_3.insert(0,hourOn4_3)
    spin4_B_3.delete(0,'end')
    spin4_B_3.insert(0,minOn4_3)
    spin4_C_3.delete(0,'end')
    spin4_C_3.insert(0,hourOff4_3)
    spin4_D_3.delete(0,'end')
    spin4_D_3.insert(0,minOff4_3)
    temp_var = inverseDarkLightValue(dark4_3, light4_3)
    var4_3.set(temp_var)


    #phase4

    spin4_E_4.delete(0,'end')
    spin4_E_4.insert(0,hourFrom4_4)
    spin4_F_4.delete(0,'end')
    spin4_F_4.insert(0,minuteFrom4_4)
    date4_4_entry.delete(0,'end')
    day_phase4 = day_phase3 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date4_4_entry.delete(0,'end')
    date4_4_entry.insert(0,'{:02d}'.format(day_phase4.day))
    month4_4_entry.delete(0,'end')
    month4_4_entry.insert(0,'{:02d}'.format(day_phase4.month))
    year4_4_entry.delete(0,'end')
    year4_4_entry.insert(0,day_phase4.year)
    spin4_A_4.delete(0,'end')
    spin4_A_4.insert(0,hourOn4_4)
    spin4_B_4.delete(0,'end')
    spin4_B_4.insert(0,hourOn4_4)
    spin4_C_4.delete(0,'end')
    spin4_C_4.insert(0,hourOff4_4)
    spin4_D_4.delete(0,'end')
    spin4_D_4.insert(0,minOff4_4)
    temp_var = inverseDarkLightValue(dark4_4, light4_4)
    var4_4.set(temp_var)


    #phase5
    spin4_E_5.delete(0,'end')
    spin4_E_5.insert(0,hourFrom4_5)
    spin4_F_5.delete(0,'end')
    spin4_F_5.insert(0,minuteFrom4_5)
    date4_5_entry.delete(0,'end')

    day_phase5 = day_phase4 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date4_5_entry.delete(0,'end')
    date4_5_entry.insert(0,'{:02d}'.format(day_phase5.day))
    month4_5_entry.delete(0,'end')
    month4_5_entry.insert(0,'{:02d}'.format(day_phase5.month))
    year4_5_entry.delete(0,'end')
    year4_5_entry.insert(0,day_phase5.year)

    spin4_A_5.delete(0,'end')
    spin4_A_5.insert(0,hourOn4_5)
    spin4_B_5.delete(0,'end')
    spin4_B_5.insert(0,hourOn4_5)
    spin4_C_5.delete(0,'end')
    spin4_C_5.insert(0,hourOff4_5)
    spin4_D_5.delete(0,'end')
    spin4_D_5.insert(0,minOff4_5)
    temp_var = inverseDarkLightValue(dark4_5, light4_5)
    var4_5.set(temp_var)

    #phase6
    spin4_E_6.delete(0,'end')
    spin4_E_6.insert(0,hourFrom4_6)
    spin4_F_6.delete(0,'end')
    spin4_F_6.insert(0,minuteFrom4_6)
    date4_6_entry.delete(0,'end')

    day_phase6 = day_phase5 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date4_6_entry.delete(0,'end')
    date4_6_entry.insert(0,'{:02d}'.format(day_phase6.day))
    month4_6_entry.delete(0,'end')
    month4_6_entry.insert(0,'{:02d}'.format(day_phase6.month))
    year4_6_entry.delete(0,'end')
    year4_6_entry.insert(0,day_phase6.year)
    spin4_A_6.delete(0,'end')
    spin4_A_6.insert(0,hourOn4_6)
    spin4_B_6.delete(0,'end')
    spin4_B_6.insert(0,hourOn4_6)
    spin4_C_6.delete(0,'end')
    spin4_C_6.insert(0,hourOff4_6)
    spin4_D_6.delete(0,'end')
    spin4_D_6.insert(0,minOff4_6)
    temp_var = inverseDarkLightValue(dark4_6, light4_6)
    var4_6.set(temp_var)

    #phase 7
    spin4_E_7.delete(0,'end')
    spin4_E_7.insert(0,hourFrom4_7)
    spin4_F_7.delete(0,'end')
    spin4_F_7.insert(0,minuteFrom4_7)
    date4_7_entry.delete(0,'end')
    day_phase7 = day_phase6 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date4_7_entry.delete(0,'end')
    date4_7_entry.insert(0,'{:02d}'.format(day_phase7.day))
    month4_7_entry.delete(0,'end')
    month4_7_entry.insert(0,'{:02d}'.format(day_phase7.month))
    year4_7_entry.delete(0,'end')
    year4_7_entry.insert(0,day_phase7.year)
    spin4_A_7.delete(0,'end')
    spin4_A_7.insert(0,hourOn4_7)
    spin4_B_7.delete(0,'end')
    spin4_B_7.insert(0,hourOn4_7)
    spin4_C_7.delete(0,'end')
    spin4_C_7.insert(0,hourOff4_7)
    spin4_D_7.delete(0,'end')
    spin4_D_7.insert(0,minOff4_7)
    temp_var = inverseDarkLightValue(dark4_7, light4_7)
    var4_7.set(temp_var)

    #phase8
    spin4_E_8.delete(0,'end')
    spin4_E_8.insert(0,hourFrom4_8)
    spin4_F_8.delete(0,'end')
    spin4_F_8.insert(0,minuteFrom4_8)
    date4_8_entry.delete(0,'end')
    day_phase8 = day_phase7 + datetime.timedelta(days=7)
    date4_8_entry.insert(0,'{:02d}'.format(day_phase8.day))
    month4_8_entry.delete(0,'end')
    month4_8_entry.insert(0,'{:02d}'.format(day_phase8.month))
    year4_8_entry.delete(0,'end')
    year4_8_entry.insert(0,day_phase8.year)
    spin4_A_8.delete(0,'end')
    spin4_A_8.insert(0,hourOn4_8)
    spin4_B_8.delete(0,'end')
    spin4_B_8.insert(0,hourOn4_8)
    spin4_C_8.delete(0,'end')
    spin4_C_8.insert(0,hourOff4_8)
    spin4_D_8.delete(0,'end')
    spin4_D_8.insert(0,minOff4_8)
    temp_var = inverseDarkLightValue(dark4_8, light4_8)
    var4_8.set(temp_var)

    #phase9

    spin4_E_9.delete(0,'end')
    spin4_E_9.insert(0,hourFrom4_9)
    spin4_F_9.delete(0,'end')
    spin4_F_9.insert(0,minuteFrom4_9)
    date4_9_entry.delete(0,'end')
    day_phase9 = day_phase8 + datetime.timedelta(days=7)
    date4_9_entry.insert(0,'{:02d}'.format(day_phase9.day))
    month4_9_entry.delete(0,'end')
    month4_9_entry.insert(0,'{:02d}'.format(day_phase9.month))
    year4_9_entry.delete(0,'end')
    year4_9_entry.insert(0,day_phase9.year)
    spin4_A_9.delete(0,'end')
    spin4_A_9.insert(0,hourOn4_9)
    spin4_B_9.delete(0,'end')
    spin4_B_9.insert(0,hourOn4_9)
    spin4_C_9.delete(0,'end')
    spin4_C_9.insert(0,hourOff4_9)
    spin4_D_9.delete(0,'end')
    spin4_D_9.insert(0,minOff4_9)
    temp_var = inverseDarkLightValue(dark4_9, light4_9)
    var4_9.set(temp_var)


    #phase10

    spin4_E_10.delete(0,'end')
    spin4_E_10.insert(0,hourFrom4_10)
    spin4_F_10.delete(0,'end')
    spin4_F_10.insert(0,minuteFrom4_10)
    date4_10_entry.delete(0,'end')
    day_phase10 = day_phase9 + datetime.timedelta(days=7)
    date4_10_entry.insert(0,'{:02d}'.format(day_phase10.day))
    month4_10_entry.delete(0,'end')
    month4_10_entry.insert(0,'{:02d}'.format(day_phase10.month))
    year4_10_entry.delete(0,'end')
    year4_10_entry.insert(0,day_phase10.year)
    spin4_A_10.delete(0,'end')
    spin4_A_10.insert(0,hourOn4_10)
    spin4_B_10.delete(0,'end')
    spin4_B_10.insert(0,hourOn4_10)
    spin4_C_10.delete(0,'end')
    spin4_C_10.insert(0,hourOff4_10)
    spin4_D_10.delete(0,'end')
    spin4_D_10.insert(0,minOff4_10)
    temp_var = inverseDarkLightValue(dark4_10, light4_10)
    var4_10.set(temp_var)

    #phase11

    spin4_E_11.delete(0,'end')
    spin4_E_11.insert(0,hourFrom4_11)
    spin4_F_11.delete(0,'end')
    spin4_F_11.insert(0,minuteFrom4_11)
    date4_11_entry.delete(0,'end')
    day_phase11 = day_phase10 + datetime.timedelta(days=7)
    date4_11_entry.insert(0,'{:02d}'.format(day_phase10.day))
    month4_11_entry.delete(0,'end')
    month4_11_entry.insert(0,'{:02d}'.format(day_phase10.month))
    year4_11_entry.delete(0,'end')
    year4_11_entry.insert(0,day_phase10.year)
    spin4_A_11.delete(0,'end')
    spin4_A_11.insert(0,hourOn4_11)
    spin4_B_11.delete(0,'end')
    spin4_B_11.insert(0,hourOn4_11)
    spin4_C_11.delete(0,'end')
    spin4_C_11.insert(0,hourOff4_11)
    spin4_D_11.delete(0,'end')
    spin4_D_11.insert(0,minOff4_11)
    temp_var = inverseDarkLightValue(dark4_11, light4_11)
    var4_11.set(temp_var)

    #phase12

    spin4_E_12.delete(0,'end')
    spin4_E_12.insert(0,hourFrom4_12)
    spin4_F_12.delete(0,'end')
    spin4_F_12.insert(0,minuteFrom4_12)
    date4_12_entry.delete(0,'end')
    day_phase12 = day_phase11 + datetime.timedelta(days=7)
    date4_12_entry.insert(0,'{:02d}'.format(day_phase11.day))
    month4_12_entry.delete(0,'end')
    month4_12_entry.insert(0,'{:02d}'.format(day_phase11.month))
    year4_12_entry.delete(0,'end')
    year4_12_entry.insert(0,day_phase11.year)
    spin4_A_12.delete(0,'end')
    spin4_A_12.insert(0,hourOn4_12)
    spin4_B_12.delete(0,'end')
    spin4_B_12.insert(0,hourOn4_12)
    spin4_C_12.delete(0,'end')
    spin4_C_12.insert(0,hourOff4_12)
    spin4_D_12.delete(0,'end')
    spin4_D_12.insert(0,minOff4_12)
    temp_var = inverseDarkLightValue(dark4_12, light4_12)
    var4_12.set(temp_var)


    #BOX5

    spin5_A_1.delete(0,'end')
    spin5_A_1.insert(0,hourOn5_1)

    spin5_B_1.delete(0,'end')
    spin5_B_1.insert(0,minOn5_1)

    spin5_C_1.delete(0,'end')
    spin5_C_1.insert(0,hourOff5_1)

    spin5_D_1.delete(0,'end')
    spin5_D_1.insert(0,minOff5_1)

    temp_var = inverseDarkLightValue(dark5_1, light5_1)
    var5_1.set(temp_var)

    spin5_E_2.delete(0,'end')
    spin5_E_2.insert(0,hourFrom5_2)

    spin5_F_2.delete(0,'end')
    spin5_F_2.insert(0,minuteFrom5_2)

    date5_2_entry.delete(0,'end')
    today=datetime.date.today() # today
    day_phase2 = today + datetime.timedelta(days=7) # calculate dates for 7 days after recording initiation
    date5_2_entry.insert(0,'{:02d}'.format(day_phase2.day))
    month5_2_entry.delete(0,'end')
    month5_2_entry.insert(0,'{:02d}'.format(day_phase2.month))
    year5_2_entry.delete(0,'end')
    year5_2_entry.insert(0,day_phase2.year) # ISO format is YYYY/MM/DD

    spin5_A_2.delete(0,'end')
    spin5_A_2.insert(0,hourOn5_2)
    spin5_B_2.delete(0,'end')
    spin5_B_2.insert(0,minOn5_2)
    spin5_C_2.delete(0,'end')
    spin5_C_2.insert(0,hourOff5_2)
    spin5_D_2.delete(0,'end')
    spin5_D_2.insert(0,minOff5_2)

    temp_var = inverseDarkLightValue(dark5_2, light5_2)
    var5_2.set(temp_var)



    spin5_E_3.delete(0,'end')
    spin5_E_3.insert(0,hourFrom5_3)
    spin5_F_3.delete(0,'end')
    spin5_F_3.insert(0,minuteFrom5_3)
    day_phase3 = day_phase2 + datetime.timedelta(days=7) # calculate dates for 14 days after recording initiation
    date5_3_entry.delete(0,'end')
    date5_3_entry.insert(0,'{:02d}'.format(day_phase3.day))
    month5_3_entry.delete(0,'end')
    month5_3_entry.insert(0,'{:02d}'.format(day_phase3.month))
    year5_3_entry.delete(0,'end')
    year5_3_entry.insert(0,day_phase3.year)

    spin5_A_3.delete(0,'end')
    spin5_A_3.insert(0,hourOn5_3)
    spin5_B_3.delete(0,'end')
    spin5_B_3.insert(0,minOn5_3)
    spin5_C_3.delete(0,'end')
    spin5_C_3.insert(0,hourOff5_3)
    spin5_D_3.delete(0,'end')
    spin5_D_3.insert(0,minOff5_3)
    temp_var = inverseDarkLightValue(dark5_3, light5_3)
    var5_3.set(temp_var)


    #phase4

    spin5_E_4.delete(0,'end')
    spin5_E_4.insert(0,hourFrom5_4)
    spin5_F_4.delete(0,'end')
    spin5_F_4.insert(0,minuteFrom5_4)
    date5_4_entry.delete(0,'end')
    day_phase4 = day_phase3 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date5_4_entry.delete(0,'end')
    date5_4_entry.insert(0,'{:02d}'.format(day_phase4.day))
    month5_4_entry.delete(0,'end')
    month5_4_entry.insert(0,'{:02d}'.format(day_phase4.month))
    year5_4_entry.delete(0,'end')
    year5_4_entry.insert(0,day_phase4.year)
    spin5_A_4.delete(0,'end')
    spin5_A_4.insert(0,hourOn5_4)
    spin5_B_4.delete(0,'end')
    spin5_B_4.insert(0,hourOn5_4)
    spin5_C_4.delete(0,'end')
    spin5_C_4.insert(0,hourOff5_4)
    spin5_D_4.delete(0,'end')
    spin5_D_4.insert(0,minOff5_4)
    temp_var = inverseDarkLightValue(dark5_4, light5_4)
    var5_4.set(temp_var)


    #phase5
    spin5_E_5.delete(0,'end')
    spin5_E_5.insert(0,hourFrom5_5)
    spin5_F_5.delete(0,'end')
    spin5_F_5.insert(0,minuteFrom5_5)
    date5_5_entry.delete(0,'end')

    day_phase5 = day_phase4 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date5_5_entry.delete(0,'end')
    date5_5_entry.insert(0,'{:02d}'.format(day_phase5.day))
    month5_5_entry.delete(0,'end')
    month5_5_entry.insert(0,'{:02d}'.format(day_phase5.month))
    year5_5_entry.delete(0,'end')
    year5_5_entry.insert(0,day_phase5.year)

    spin5_A_5.delete(0,'end')
    spin5_A_5.insert(0,hourOn5_5)
    spin5_B_5.delete(0,'end')
    spin5_B_5.insert(0,hourOn5_5)
    spin5_C_5.delete(0,'end')
    spin5_C_5.insert(0,hourOff5_5)
    spin5_D_5.delete(0,'end')
    spin5_D_5.insert(0,minOff5_5)
    temp_var = inverseDarkLightValue(dark5_5, light5_5)
    var5_5.set(temp_var)

    #phase6
    spin5_E_6.delete(0,'end')
    spin5_E_6.insert(0,hourFrom5_6)
    spin5_F_6.delete(0,'end')
    spin5_F_6.insert(0,minuteFrom5_6)
    date5_6_entry.delete(0,'end')

    day_phase6 = day_phase5 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date5_6_entry.delete(0,'end')
    date5_6_entry.insert(0,'{:02d}'.format(day_phase6.day))
    month5_6_entry.delete(0,'end')
    month5_6_entry.insert(0,'{:02d}'.format(day_phase6.month))
    year5_6_entry.delete(0,'end')
    year5_6_entry.insert(0,day_phase6.year)
    spin5_A_6.delete(0,'end')
    spin5_A_6.insert(0,hourOn5_6)
    spin5_B_6.delete(0,'end')
    spin5_B_6.insert(0,hourOn5_6)
    spin5_C_6.delete(0,'end')
    spin5_C_6.insert(0,hourOff5_6)
    spin5_D_6.delete(0,'end')
    spin5_D_6.insert(0,minOff5_6)
    temp_var = inverseDarkLightValue(dark5_6, light5_6)
    var5_6.set(temp_var)

    #phase 7
    spin5_E_7.delete(0,'end')
    spin5_E_7.insert(0,hourFrom5_7)
    spin5_F_7.delete(0,'end')
    spin5_F_7.insert(0,minuteFrom5_7)
    date5_7_entry.delete(0,'end')
    day_phase7 = day_phase6 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date5_7_entry.delete(0,'end')
    date5_7_entry.insert(0,'{:02d}'.format(day_phase7.day))
    month5_7_entry.delete(0,'end')
    month5_7_entry.insert(0,'{:02d}'.format(day_phase7.month))
    year5_7_entry.delete(0,'end')
    year5_7_entry.insert(0,day_phase7.year)
    spin5_A_7.delete(0,'end')
    spin5_A_7.insert(0,hourOn5_7)
    spin5_B_7.delete(0,'end')
    spin5_B_7.insert(0,hourOn5_7)
    spin5_C_7.delete(0,'end')
    spin5_C_7.insert(0,hourOff5_7)
    spin5_D_7.delete(0,'end')
    spin5_D_7.insert(0,minOff5_7)
    temp_var = inverseDarkLightValue(dark5_7, light5_7)
    var5_7.set(temp_var)

    #phase8
    spin5_E_8.delete(0,'end')
    spin5_E_8.insert(0,hourFrom5_8)
    spin5_F_8.delete(0,'end')
    spin5_F_8.insert(0,minuteFrom5_8)
    date5_8_entry.delete(0,'end')
    day_phase8 = day_phase7 + datetime.timedelta(days=7)
    date5_8_entry.insert(0,'{:02d}'.format(day_phase8.day))
    month5_8_entry.delete(0,'end')
    month5_8_entry.insert(0,'{:02d}'.format(day_phase8.month))
    year5_8_entry.delete(0,'end')
    year5_8_entry.insert(0,day_phase8.year)
    spin5_A_8.delete(0,'end')
    spin5_A_8.insert(0,hourOn5_8)
    spin5_B_8.delete(0,'end')
    spin5_B_8.insert(0,hourOn5_8)
    spin5_C_8.delete(0,'end')
    spin5_C_8.insert(0,hourOff5_8)
    spin5_D_8.delete(0,'end')
    spin5_D_8.insert(0,minOff5_8)
    temp_var = inverseDarkLightValue(dark5_8, light5_8)
    var5_8.set(temp_var)

    #phase9

    spin5_E_9.delete(0,'end')
    spin5_E_9.insert(0,hourFrom5_9)
    spin5_F_9.delete(0,'end')
    spin5_F_9.insert(0,minuteFrom5_9)
    date5_9_entry.delete(0,'end')
    day_phase9 = day_phase8 + datetime.timedelta(days=7)
    date5_9_entry.insert(0,'{:02d}'.format(day_phase9.day))
    month5_9_entry.delete(0,'end')
    month5_9_entry.insert(0,'{:02d}'.format(day_phase9.month))
    year5_9_entry.delete(0,'end')
    year5_9_entry.insert(0,day_phase9.year)
    spin5_A_9.delete(0,'end')
    spin5_A_9.insert(0,hourOn5_9)
    spin5_B_9.delete(0,'end')
    spin5_B_9.insert(0,hourOn5_9)
    spin5_C_9.delete(0,'end')
    spin5_C_9.insert(0,hourOff5_9)
    spin5_D_9.delete(0,'end')
    spin5_D_9.insert(0,minOff5_9)
    temp_var = inverseDarkLightValue(dark5_9, light5_9)
    var5_9.set(temp_var)


    #phase10

    spin5_E_10.delete(0,'end')
    spin5_E_10.insert(0,hourFrom5_10)
    spin5_F_10.delete(0,'end')
    spin5_F_10.insert(0,minuteFrom5_10)
    date5_10_entry.delete(0,'end')
    day_phase10 = day_phase9 + datetime.timedelta(days=7)
    date5_10_entry.insert(0,'{:02d}'.format(day_phase10.day))
    month5_10_entry.delete(0,'end')
    month5_10_entry.insert(0,'{:02d}'.format(day_phase10.month))
    year5_10_entry.delete(0,'end')
    year5_10_entry.insert(0,day_phase10.year)
    spin5_A_10.delete(0,'end')
    spin5_A_10.insert(0,hourOn5_10)
    spin5_B_10.delete(0,'end')
    spin5_B_10.insert(0,hourOn5_10)
    spin5_C_10.delete(0,'end')
    spin5_C_10.insert(0,hourOff5_10)
    spin5_D_10.delete(0,'end')
    spin5_D_10.insert(0,minOff5_10)
    temp_var = inverseDarkLightValue(dark5_10, light5_10)
    var5_10.set(temp_var)

    #phase11

    spin5_E_11.delete(0,'end')
    spin5_E_11.insert(0,hourFrom5_11)
    spin5_F_11.delete(0,'end')
    spin5_F_11.insert(0,minuteFrom5_11)
    date5_11_entry.delete(0,'end')
    day_phase11 = day_phase10 + datetime.timedelta(days=7)
    date5_11_entry.insert(0,'{:02d}'.format(day_phase10.day))
    month5_11_entry.delete(0,'end')
    month5_11_entry.insert(0,'{:02d}'.format(day_phase10.month))
    year5_11_entry.delete(0,'end')
    year5_11_entry.insert(0,day_phase10.year)
    spin5_A_11.delete(0,'end')
    spin5_A_11.insert(0,hourOn5_11)
    spin5_B_11.delete(0,'end')
    spin5_B_11.insert(0,hourOn5_11)
    spin5_C_11.delete(0,'end')
    spin5_C_11.insert(0,hourOff5_11)
    spin5_D_11.delete(0,'end')
    spin5_D_11.insert(0,minOff5_11)
    temp_var = inverseDarkLightValue(dark5_11, light5_11)
    var5_11.set(temp_var)

    #phase12

    spin5_E_12.delete(0,'end')
    spin5_E_12.insert(0,hourFrom5_12)
    spin5_F_12.delete(0,'end')
    spin5_F_12.insert(0,minuteFrom5_12)
    date5_12_entry.delete(0,'end')
    day_phase12 = day_phase11 + datetime.timedelta(days=7)
    date5_12_entry.insert(0,'{:02d}'.format(day_phase11.day))
    month5_12_entry.delete(0,'end')
    month5_12_entry.insert(0,'{:02d}'.format(day_phase11.month))
    year5_12_entry.delete(0,'end')
    year5_12_entry.insert(0,day_phase11.year)
    spin5_A_12.delete(0,'end')
    spin5_A_12.insert(0,hourOn5_12)
    spin5_B_12.delete(0,'end')
    spin5_B_12.insert(0,hourOn5_12)
    spin5_C_12.delete(0,'end')
    spin5_C_12.insert(0,hourOff5_12)
    spin5_D_12.delete(0,'end')
    spin5_D_12.insert(0,minOff5_12)
    temp_var = inverseDarkLightValue(dark5_12, light5_12)
    var5_12.set(temp_var)

    #BOX6

    spin6_A_1.delete(0,'end')
    spin6_A_1.insert(0,hourOn6_1)

    spin6_B_1.delete(0,'end')
    spin6_B_1.insert(0,minOn6_1)

    spin6_C_1.delete(0,'end')
    spin6_C_1.insert(0,hourOff6_1)

    spin6_D_1.delete(0,'end')
    spin6_D_1.insert(0,minOff6_1)

    temp_var = inverseDarkLightValue(dark6_1, light6_1)
    var6_1.set(temp_var)

    spin6_E_2.delete(0,'end')
    spin6_E_2.insert(0,hourFrom6_2)

    spin6_F_2.delete(0,'end')
    spin6_F_2.insert(0,minuteFrom6_2)

    date6_2_entry.delete(0,'end')
    today=datetime.date.today() # today
    day_phase2 = today + datetime.timedelta(days=7) # calculate dates for 7 days after recording initiation
    date6_2_entry.insert(0,'{:02d}'.format(day_phase2.day))
    month6_2_entry.delete(0,'end')
    month6_2_entry.insert(0,'{:02d}'.format(day_phase2.month))
    year6_2_entry.delete(0,'end')
    year6_2_entry.insert(0,day_phase2.year) # ISO format is YYYY/MM/DD

    spin6_A_2.delete(0,'end')
    spin6_A_2.insert(0,hourOn6_2)
    spin6_B_2.delete(0,'end')
    spin6_B_2.insert(0,minOn6_2)
    spin6_C_2.delete(0,'end')
    spin6_C_2.insert(0,hourOff6_2)
    spin6_D_2.delete(0,'end')
    spin6_D_2.insert(0,minOff6_2)

    temp_var = inverseDarkLightValue(dark6_2, light6_2)
    var6_2.set(temp_var)



    spin6_E_3.delete(0,'end')
    spin6_E_3.insert(0,hourFrom6_3)
    spin6_F_3.delete(0,'end')
    spin6_F_3.insert(0,minuteFrom6_3)
    day_phase3 = day_phase2 + datetime.timedelta(days=7) # calculate dates for 14 days after recording initiation
    date6_3_entry.delete(0,'end')
    date6_3_entry.insert(0,'{:02d}'.format(day_phase3.day))
    month6_3_entry.delete(0,'end')
    month6_3_entry.insert(0,'{:02d}'.format(day_phase3.month))
    year6_3_entry.delete(0,'end')
    year6_3_entry.insert(0,day_phase3.year)

    spin6_A_3.delete(0,'end')
    spin6_A_3.insert(0,hourOn6_3)
    spin6_B_3.delete(0,'end')
    spin6_B_3.insert(0,minOn6_3)
    spin6_C_3.delete(0,'end')
    spin6_C_3.insert(0,hourOff6_3)
    spin6_D_3.delete(0,'end')
    spin6_D_3.insert(0,minOff6_3)
    temp_var = inverseDarkLightValue(dark6_3, light6_3)
    var6_3.set(temp_var)


    #phase4

    spin6_E_4.delete(0,'end')
    spin6_E_4.insert(0,hourFrom6_4)
    spin6_F_4.delete(0,'end')
    spin6_F_4.insert(0,minuteFrom6_4)
    date6_4_entry.delete(0,'end')
    day_phase4 = day_phase3 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date6_4_entry.delete(0,'end')
    date6_4_entry.insert(0,'{:02d}'.format(day_phase4.day))
    month6_4_entry.delete(0,'end')
    month6_4_entry.insert(0,'{:02d}'.format(day_phase4.month))
    year6_4_entry.delete(0,'end')
    year6_4_entry.insert(0,day_phase4.year)
    spin6_A_4.delete(0,'end')
    spin6_A_4.insert(0,hourOn6_4)
    spin6_B_4.delete(0,'end')
    spin6_B_4.insert(0,hourOn6_4)
    spin6_C_4.delete(0,'end')
    spin6_C_4.insert(0,hourOff6_4)
    spin6_D_4.delete(0,'end')
    spin6_D_4.insert(0,minOff6_4)
    temp_var = inverseDarkLightValue(dark6_4, light6_4)
    var6_4.set(temp_var)


    #phase5
    spin6_E_5.delete(0,'end')
    spin6_E_5.insert(0,hourFrom6_5)
    spin6_F_5.delete(0,'end')
    spin6_F_5.insert(0,minuteFrom6_5)
    date6_5_entry.delete(0,'end')

    day_phase5 = day_phase4 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date6_5_entry.delete(0,'end')
    date6_5_entry.insert(0,'{:02d}'.format(day_phase5.day))
    month6_5_entry.delete(0,'end')
    month6_5_entry.insert(0,'{:02d}'.format(day_phase5.month))
    year6_5_entry.delete(0,'end')
    year6_5_entry.insert(0,day_phase5.year)

    spin6_A_5.delete(0,'end')
    spin6_A_5.insert(0,hourOn6_5)
    spin6_B_5.delete(0,'end')
    spin6_B_5.insert(0,hourOn6_5)
    spin6_C_5.delete(0,'end')
    spin6_C_5.insert(0,hourOff6_5)
    spin6_D_5.delete(0,'end')
    spin6_D_5.insert(0,minOff6_5)
    temp_var = inverseDarkLightValue(dark6_5, light6_5)
    var6_5.set(temp_var)

    #phase6
    spin6_E_6.delete(0,'end')
    spin6_E_6.insert(0,hourFrom6_6)
    spin6_F_6.delete(0,'end')
    spin6_F_6.insert(0,minuteFrom6_6)
    date6_6_entry.delete(0,'end')

    day_phase6 = day_phase5 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date6_6_entry.delete(0,'end')
    date6_6_entry.insert(0,'{:02d}'.format(day_phase6.day))
    month6_6_entry.delete(0,'end')
    month6_6_entry.insert(0,'{:02d}'.format(day_phase6.month))
    year6_6_entry.delete(0,'end')
    year6_6_entry.insert(0,day_phase6.year)
    spin6_A_6.delete(0,'end')
    spin6_A_6.insert(0,hourOn6_6)
    spin6_B_6.delete(0,'end')
    spin6_B_6.insert(0,hourOn6_6)
    spin6_C_6.delete(0,'end')
    spin6_C_6.insert(0,hourOff6_6)
    spin6_D_6.delete(0,'end')
    spin6_D_6.insert(0,minOff6_6)
    temp_var = inverseDarkLightValue(dark6_6, light6_6)
    var6_6.set(temp_var)

    #phase 7
    spin6_E_7.delete(0,'end')
    spin6_E_7.insert(0,hourFrom6_7)
    spin6_F_7.delete(0,'end')
    spin6_F_7.insert(0,minuteFrom6_7)
    date6_7_entry.delete(0,'end')
    day_phase7 = day_phase6 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date6_7_entry.delete(0,'end')
    date6_7_entry.insert(0,'{:02d}'.format(day_phase7.day))
    month6_7_entry.delete(0,'end')
    month6_7_entry.insert(0,'{:02d}'.format(day_phase7.month))
    year6_7_entry.delete(0,'end')
    year6_7_entry.insert(0,day_phase7.year)
    spin6_A_7.delete(0,'end')
    spin6_A_7.insert(0,hourOn6_7)
    spin6_B_7.delete(0,'end')
    spin6_B_7.insert(0,hourOn6_7)
    spin6_C_7.delete(0,'end')
    spin6_C_7.insert(0,hourOff6_7)
    spin6_D_7.delete(0,'end')
    spin6_D_7.insert(0,minOff6_7)
    temp_var = inverseDarkLightValue(dark6_7, light6_7)
    var6_7.set(temp_var)

    #phase8
    spin6_E_8.delete(0,'end')
    spin6_E_8.insert(0,hourFrom6_8)
    spin6_F_8.delete(0,'end')
    spin6_F_8.insert(0,minuteFrom6_8)
    date6_8_entry.delete(0,'end')
    day_phase8 = day_phase7 + datetime.timedelta(days=7)
    date6_8_entry.insert(0,'{:02d}'.format(day_phase8.day))
    month6_8_entry.delete(0,'end')
    month6_8_entry.insert(0,'{:02d}'.format(day_phase8.month))
    year6_8_entry.delete(0,'end')
    year6_8_entry.insert(0,day_phase8.year)
    spin6_A_8.delete(0,'end')
    spin6_A_8.insert(0,hourOn6_8)
    spin6_B_8.delete(0,'end')
    spin6_B_8.insert(0,hourOn6_8)
    spin6_C_8.delete(0,'end')
    spin6_C_8.insert(0,hourOff6_8)
    spin6_D_8.delete(0,'end')
    spin6_D_8.insert(0,minOff6_8)
    temp_var = inverseDarkLightValue(dark6_8, light6_8)
    var6_8.set(temp_var)

    #phase9

    spin6_E_9.delete(0,'end')
    spin6_E_9.insert(0,hourFrom6_9)
    spin6_F_9.delete(0,'end')
    spin6_F_9.insert(0,minuteFrom6_9)
    date6_9_entry.delete(0,'end')
    day_phase9 = day_phase8 + datetime.timedelta(days=7)
    date6_9_entry.insert(0,'{:02d}'.format(day_phase9.day))
    month6_9_entry.delete(0,'end')
    month6_9_entry.insert(0,'{:02d}'.format(day_phase9.month))
    year6_9_entry.delete(0,'end')
    year6_9_entry.insert(0,day_phase9.year)
    spin6_A_9.delete(0,'end')
    spin6_A_9.insert(0,hourOn6_9)
    spin6_B_9.delete(0,'end')
    spin6_B_9.insert(0,hourOn6_9)
    spin6_C_9.delete(0,'end')
    spin6_C_9.insert(0,hourOff6_9)
    spin6_D_9.delete(0,'end')
    spin6_D_9.insert(0,minOff6_9)
    temp_var = inverseDarkLightValue(dark6_9, light6_9)
    var6_9.set(temp_var)


    #phase10

    spin6_E_10.delete(0,'end')
    spin6_E_10.insert(0,hourFrom6_10)
    spin6_F_10.delete(0,'end')
    spin6_F_10.insert(0,minuteFrom6_10)
    date6_10_entry.delete(0,'end')
    day_phase10 = day_phase9 + datetime.timedelta(days=7)
    date6_10_entry.insert(0,'{:02d}'.format(day_phase10.day))
    month6_10_entry.delete(0,'end')
    month6_10_entry.insert(0,'{:02d}'.format(day_phase10.month))
    year6_10_entry.delete(0,'end')
    year6_10_entry.insert(0,day_phase10.year)
    spin6_A_10.delete(0,'end')
    spin6_A_10.insert(0,hourOn6_10)
    spin6_B_10.delete(0,'end')
    spin6_B_10.insert(0,hourOn6_10)
    spin6_C_10.delete(0,'end')
    spin6_C_10.insert(0,hourOff6_10)
    spin6_D_10.delete(0,'end')
    spin6_D_10.insert(0,minOff6_10)
    temp_var = inverseDarkLightValue(dark6_10, light6_10)
    var6_10.set(temp_var)

    #phase11

    spin6_E_11.delete(0,'end')
    spin6_E_11.insert(0,hourFrom6_11)
    spin6_F_11.delete(0,'end')
    spin6_F_11.insert(0,minuteFrom6_11)
    date6_11_entry.delete(0,'end')
    day_phase11 = day_phase10 + datetime.timedelta(days=7)
    date6_11_entry.insert(0,'{:02d}'.format(day_phase10.day))
    month6_11_entry.delete(0,'end')
    month6_11_entry.insert(0,'{:02d}'.format(day_phase10.month))
    year6_11_entry.delete(0,'end')
    year6_11_entry.insert(0,day_phase10.year)
    spin6_A_11.delete(0,'end')
    spin6_A_11.insert(0,hourOn6_11)
    spin6_B_11.delete(0,'end')
    spin6_B_11.insert(0,hourOn6_11)
    spin6_C_11.delete(0,'end')
    spin6_C_11.insert(0,hourOff6_11)
    spin6_D_11.delete(0,'end')
    spin6_D_11.insert(0,minOff6_11)
    temp_var = inverseDarkLightValue(dark6_11, light6_11)
    var6_11.set(temp_var)

    #phase12

    spin6_E_12.delete(0,'end')
    spin6_E_12.insert(0,hourFrom6_12)
    spin6_F_12.delete(0,'end')
    spin6_F_12.insert(0,minuteFrom6_12)
    date6_12_entry.delete(0,'end')
    day_phase12 = day_phase11 + datetime.timedelta(days=7)
    date6_12_entry.insert(0,'{:02d}'.format(day_phase11.day))
    month6_12_entry.delete(0,'end')
    month6_12_entry.insert(0,'{:02d}'.format(day_phase11.month))
    year6_12_entry.delete(0,'end')
    year6_12_entry.insert(0,day_phase11.year)
    spin6_A_12.delete(0,'end')
    spin6_A_12.insert(0,hourOn6_12)
    spin6_B_12.delete(0,'end')
    spin6_B_12.insert(0,hourOn6_12)
    spin6_C_12.delete(0,'end')
    spin6_C_12.insert(0,hourOff6_12)
    spin6_D_12.delete(0,'end')
    spin6_D_12.insert(0,minOff6_12)
    temp_var = inverseDarkLightValue(dark6_12, light6_12)
    var6_12.set(temp_var)



    btnRun['state']='normal'
    recordingmenu.entryconfig('Start new', state='normal')
    show_conf()
    

    status.pack(side='bottom', fill='x')
    status.set('The schedule configuration is loaded.')

 
    
    window.update_idletasks()

def show_conf(): # Show schedule configuration
    global hourOn1_1, minOn1_1, hourOff1_1, minOff1_1, dark1_1, light1_1
    global hourOn2_1, minOn2_1, hourOff2_1, minOff2_1, dark2_1, light2_1
    global hourOn3_1, minOn3_1, hourOff3_1, minOff3_1, dark3_1, light3_1
    global hourOn4_1, minOn4_1, hourOff4_1, minOff4_1, dark4_1, light4_1
    global hourOn5_1, minOn5_1, hourOff5_1, minOff5_1, dark5_1, light5_1
    global hourOn6_1, minOn6_1, hourOff6_1, minOff6_1, dark6_1, light6_1

    global hourOn1_2, minOn1_2, hourOff1_2, minOff1_2, date1_2, month1_2, year1_2, dark1_2, light1_2, hourFrom1_2, minuteFrom1_2
    global hourOn2_2, minOn2_2, hourOff2_2, minOff2_2, date2_2, month2_2, year2_2, dark2_2, light2_2, hourFrom2_2, minuteFrom2_2
    global hourOn3_2, minOn3_2, hourOff3_2, minOff3_2, date3_2, month3_2, year3_2, dark3_2, light3_2, hourFrom3_2, minuteFrom3_2
    global hourOn4_2, minOn4_2, hourOff4_2, minOff4_2, date4_2, month4_2, year4_2, dark4_2, light4_2, hourFrom4_2, minuteFrom4_2
    global hourOn5_2, minOn5_2, hourOff5_2, minOff5_2, date5_2, month5_2, year5_2, dark5_2, light5_2, hourFrom5_2, minuteFrom5_2
    global hourOn6_2, minOn6_2, hourOff6_2, minOff6_2, date6_2, month6_2, year6_2, dark6_2, light6_2, hourFrom6_2, minuteFrom6_2

    global hourOn1_3, minOn1_3, hourOff1_3, minOff1_3, dark1_3, light1_3, date1_3, month1_3, year1_3, hourFrom1_3, minuteFrom1_3
    global hourOn2_3, minOn2_3, hourOff2_3, minOff2_3, dark2_3, light2_3, date2_3, month2_3, year2_3, hourFrom2_3, minuteFrom2_3
    global hourOn3_3, minOn3_3, hourOff3_3, minOff3_3, dark3_3, light3_3, date3_3, month3_3, year3_3, hourFrom3_3, minuteFrom3_3
    global hourOn4_3, minOn4_3, hourOff4_3, minOff4_3, dark4_3, light4_3, date4_3, month4_3, year4_3, hourFrom4_3, minuteFrom4_3
    global hourOn5_3, minOn5_3, hourOff5_3, minOff5_3, dark5_3, light5_3, date5_3, month5_3, year5_3, hourFrom5_3, minuteFrom5_3
    global hourOn6_3, minOn6_3, hourOff6_3, minOff6_3, dark6_3, light6_3, date6_3, month6_3, year6_3, hourFrom6_3, minuteFrom6_3

    global hourOn1_4, minOn1_4, hourOff1_4, minOff1_4, dark1_4, light1_4, date1_4, month1_4, year1_4, hourFrom1_4, minuteFrom1_4
    global hourOn2_4, minOn2_4, hourOff2_4, minOff2_4, dark2_4, light2_4, date2_4, month2_4, year2_4, hourFrom2_4, minuteFrom2_4
    global hourOn3_4, minOn3_4, hourOff3_4, minOff3_4, dark3_4, light3_4, date3_4, month3_4, year3_4, hourFrom3_4, minuteFrom3_4
    global hourOn4_4, minOn4_4, hourOff4_4, minOff4_4, dark4_4, light4_4, date4_4, month4_4, year4_4, hourFrom4_4, minuteFrom4_4
    global hourOn5_4, minOn5_4, hourOff5_4, minOff5_4, dark5_4, light5_4, date5_4, month5_4, year5_4, hourFrom5_4, minuteFrom5_4
    global hourOn6_4, minOn6_4, hourOff6_4, minOff6_4, dark6_4, light6_4, date6_4, month6_4, year6_4, hourFrom6_4, minuteFrom6_4

    global hourOn1_5, minOn1_5, hourOff1_5, minOff1_5, dark1_5, light1_5, date1_5, month1_5, year1_5, hourFrom1_5, minuteFrom1_5
    global hourOn2_5, minOn2_5, hourOff2_5, minOff2_5, dark2_5, light2_5, date2_5, month2_5, year2_5, hourFrom2_5, minuteFrom2_5
    global hourOn3_5, minOn3_5, hourOff3_5, minOff3_5, dark3_5, light3_5, date3_5, month3_5, year3_5, hourFrom3_5, minuteFrom3_5
    global hourOn4_5, minOn4_5, hourOff4_5, minOff4_5, dark4_5, light4_5, date4_5, month4_5, year4_5, hourFrom4_5, minuteFrom4_5
    global hourOn5_5, minOn5_5, hourOff5_5, minOff5_5, dark5_5, light5_5, date5_5, month5_5, year5_5, hourFrom5_5, minuteFrom5_5
    global hourOn6_5, minOn6_5, hourOff6_5, minOff6_5, dark6_5, light6_5, date6_5, month6_5, year6_5, hourFrom6_5, minuteFrom6_5

    global hourOn1_6, minOn1_6, hourOff1_6, minOff1_6, dark1_6, light1_6, date1_6, month1_6, year1_6, hourFrom1_6, minuteFrom1_6
    global hourOn2_6, minOn2_6, hourOff2_6, minOff2_6, dark2_6, light2_6, date2_6, month2_6, year2_6, hourFrom2_6, minuteFrom2_6
    global hourOn3_6, minOn3_6, hourOff3_6, minOff3_6, dark3_6, light3_6, date3_6, month3_6, year3_6, hourFrom3_6, minuteFrom3_6
    global hourOn4_6, minOn4_6, hourOff4_6, minOff4_6, dark4_6, light4_6, date4_6, month4_6, year4_6, hourFrom4_6, minuteFrom4_6
    global hourOn5_6, minOn5_6, hourOff5_6, minOff5_6, dark5_6, light5_6, date5_6, month5_6, year5_6, hourFrom5_6, minuteFrom5_6
    global hourOn6_6, minOn6_6, hourOff6_6, minOff6_6, dark6_6, light6_6, date6_6, month6_6, year6_6, hourFrom6_6, minuteFrom6_6

    global hourOn1_7, minOn1_7, hourOff1_7, minOff1_7, dark1_7, light1_7, date1_7, month1_7, year1_7, hourFrom1_7, minuteFrom1_7
    global hourOn2_7, minOn2_7, hourOff2_7, minOff2_7, dark2_7, light2_7, date2_7, month2_7, year2_7, hourFrom2_7, minuteFrom2_7
    global hourOn3_7, minOn3_7, hourOff3_7, minOff3_7, dark3_7, light3_7, date3_7, month3_7, year3_7, hourFrom3_7, minuteFrom3_7
    global hourOn4_7, minOn4_7, hourOff4_7, minOff4_7, dark4_7, light4_7, date4_7, month4_7, year4_7, hourFrom4_7, minuteFrom4_7
    global hourOn5_7, minOn5_7, hourOff5_7, minOff5_7, dark5_7, light5_7, date5_7, month5_7, year5_7, hourFrom5_7, minuteFrom5_7
    global hourOn6_7, minOn6_7, hourOff6_7, minOff6_7, dark6_7, light6_7, date6_7, month6_7, year6_7, hourFrom6_7, minuteFrom6_7

    global hourOn1_8, minOn1_8, hourOff1_8, minOff1_8, dark1_8, light1_8, date1_8, month1_8, year1_8, hourFrom1_8, minuteFrom1_8
    global hourOn2_8, minOn2_8, hourOff2_8, minOff2_8, dark2_8, light2_8, date2_8, month2_8, year2_8, hourFrom2_8, minuteFrom2_8
    global hourOn3_8, minOn3_8, hourOff3_8, minOff3_8, dark3_8, light3_8, date3_8, month3_8, year3_8, hourFrom3_8, minuteFrom3_8
    global hourOn4_8, minOn4_8, hourOff4_8, minOff4_8, dark4_8, light4_8, date4_8, month4_8, year4_8, hourFrom4_8, minuteFrom4_8
    global hourOn5_8, minOn5_8, hourOff5_8, minOff5_8, dark5_8, light5_8, date5_8, month5_8, year5_8, hourFrom5_8, minuteFrom5_8
    global hourOn6_8, minOn6_8, hourOff6_8, minOff6_8, dark6_8, light6_8, date6_8, month6_8, year6_8, hourFrom6_8, minuteFrom6_8

    global hourOn1_9, minOn1_9, hourOff1_9, minOff1_9, dark1_9, light1_9, date1_9, month1_9, year1_9, hourFrom1_9, minuteFrom1_9
    global hourOn2_9, minOn2_9, hourOff2_9, minOff2_9, dark2_9, light2_9, date2_9, month2_9, year2_9, hourFrom2_9, minuteFrom2_9
    global hourOn3_9, minOn3_9, hourOff3_9, minOff3_9, dark3_9, light3_9, date3_9, month3_9, year3_9, hourFrom3_9, minuteFrom3_9
    global hourOn4_9, minOn4_9, hourOff4_9, minOff4_9, dark4_9, light4_9, date4_9, month4_9, year4_9, hourFrom4_9, minuteFrom4_9
    global hourOn5_9, minOn5_9, hourOff5_9, minOff5_9, dark5_9, light5_9, date5_9, month5_9, year5_9, hourFrom5_9, minuteFrom5_9
    global hourOn6_9, minOn6_9, hourOff6_9, minOff6_9, dark6_9, light6_9, date6_9, month6_9, year6_9, hourFrom6_9, minuteFrom6_9

    global hourOn1_10, minOn1_10, hourOff1_10, minOff1_10, dark1_10, light1_10, date1_10, month1_10, year1_10, hourFrom1_10, minuteFrom1_10
    global hourOn2_10, minOn2_10, hourOff2_10, minOff2_10, dark2_10, light2_10, date2_10, month2_10, year2_10, hourFrom2_10, minuteFrom2_10
    global hourOn3_10, minOn3_10, hourOff3_10, minOff3_10, dark3_10, light3_10, date3_10, month3_10, year3_10, hourFrom3_10, minuteFrom3_10
    global hourOn4_10, minOn4_10, hourOff4_10, minOff4_10, dark4_10, light4_10, date4_10, month4_10, year4_10, hourFrom4_10, minuteFrom4_10
    global hourOn5_10, minOn5_10, hourOff5_10, minOff5_10, dark5_10, light5_10, date5_10, month5_10, year5_10, hourFrom5_10, minuteFrom5_10
    global hourOn6_10, minOn6_10, hourOff6_10, minOff6_10, dark6_10, light6_10, date6_10, month6_10, year6_10, hourFrom6_10, minuteFrom6_10v

    global hourOn1_11, minOn1_11, hourOff1_11, minOff1_11, dark1_11, light1_11, date1_11, month1_11, year1_11, hourFrom1_11, minuteFrom1_11
    global hourOn2_11, minOn2_11, hourOff2_11, minOff2_11, dark2_11, light2_11, date2_11, month2_11, year2_11, hourFrom2_11, minuteFrom2_11
    global hourOn3_11, minOn3_11, hourOff3_11, minOff3_11, dark3_11, light3_11, date3_11, month3_11, year3_11, hourFrom3_11, minuteFrom3_11
    global hourOn4_11, minOn4_11, hourOff4_11, minOff4_11, dark4_11, light4_11, date4_11, month4_11, year4_11, hourFrom4_11, minuteFrom4_11
    global hourOn5_11, minOn5_11, hourOff5_11, minOff5_11, dark5_11, light5_11, date5_11, month5_11, year5_11, hourFrom5_11, minuteFrom5_11
    global hourOn6_11, minOn6_11, hourOff6_11, minOff6_11, dark6_11, light6_11, date6_11, month6_11, year6_11, hourFrom6_11, minuteFrom6_11

    global hourOn1_12, minOn1_12, hourOff1_12, minOff1_12, dark1_12, light1_12, date1_12, month1_12, year1_12, hourFrom1_12, minuteFrom1_12
    global hourOn2_12, minOn2_12, hourOff2_12, minOff2_12, dark2_12, light2_12, date2_12, month2_12, year2_12, hourFrom2_12, minuteFrom2_12
    global hourOn3_12, minOn3_12, hourOff3_12, minOff3_12, dark3_12, light3_12, date3_12, month3_12, year3_12, hourFrom3_12, minuteFrom3_12
    global hourOn4_12, minOn4_12, hourOff4_12, minOff4_12, dark4_12, light4_12, date4_12, month4_12, year4_12, hourFrom4_12, minuteFrom4_12
    global hourOn5_12, minOn5_12, hourOff5_12, minOff5_12, dark5_12, light5_12, date5_12, month5_12, year5_12, hourFrom5_12, minuteFrom5_12
    global hourOn6_12, minOn6_12, hourOff6_12, minOff6_12, dark6_12, light6_12, date6_12, month6_12, year6_12, hourFrom6_12, minuteFrom6_12

    global initLED1, initLED2, initLED3, initLED4, initLED5, initLED6
    global tcycle_1_1, tcycle_1_2,tcycle_1_3, tcycle_1_4, tcycle_1_5, tcycle_1_6, tcycle_1_7, tcycle_1_8, tcycle_1_9, tcycle_1_10, tcycle_1_11, tcycle_1_12
    global tcycle_2_1, tcycle_2_2,tcycle_2_3, tcycle_2_4, tcycle_2_5, tcycle_2_6, tcycle_2_7, tcycle_2_8, tcycle_2_9, tcycle_2_10, tcycle_2_11, tcycle_2_12
    global tcycle_3_1, tcycle_3_2,tcycle_3_3, tcycle_3_4, tcycle_3_5, tcycle_3_6, tcycle_3_7, tcycle_3_8, tcycle_3_9, tcycle_3_10, tcycle_3_11, tcycle_3_12
    global tcycle_4_1, tcycle_4_2,tcycle_4_3, tcycle_4_4, tcycle_4_5, tcycle_4_6, tcycle_4_7, tcycle_4_8, tcycle_4_9, tcycle_4_10, tcycle_4_11, tcycle_4_12
    global tcycle_5_1, tcycle_5_2,tcycle_5_3, tcycle_5_4, tcycle_5_5, tcycle_5_6, tcycle_5_7, tcycle_5_8, tcycle_5_9, tcycle_5_10, tcycle_5_11, tcycle_5_12
    global tcycle_6_1, tcycle_6_2,tcycle_6_3, tcycle_6_4, tcycle_6_5, tcycle_6_6, tcycle_6_7, tcycle_6_8, tcycle_6_9, tcycle_6_10, tcycle_6_11, tcycle_6_12



    #print("hourOn1_1" + str(hourOn1_1))

    col11_1 = Label(tab11, text='Box 1')
    col11_2 = Label(tab11, text='Box 2')
    col11_3 = Label(tab11, text='Box 3')
    col11_4 = Label(tab11, text='Box 4')
    col11_5 = Label(tab11, text='Box 5')
    col11_6 = Label(tab11, text='Box 6')


    row11_1 = Label(tab11, text='Phase 1 ')
    row11_2 = Label(tab11, text='Phase 2')
    row11_3 = Label(tab11, text='Phase 3 ')
    row11_4 = Label(tab11, text='Phase 4')
    row11_5 = Label(tab11, text='Phase 5 ')
    row11_6 = Label(tab11, text='Phase 6')
    row11_7 = Label(tab11, text='Phase 7 ')
    row11_8 = Label(tab11, text='Phase 8')
    row11_9 = Label(tab11, text='Phase 9 ')
    row11_10 = Label(tab11, text='Phase 10')
    row11_11 = Label(tab11, text='Phase 11 ')
    row11_12 = Label(tab11, text='Phase 12')

    col11_1.grid(column=2,row=0,padx=5)
    col11_2.grid(column=4,row=0,padx=5)
    col11_3.grid(column=6,row=0,padx=5)
    col11_4.grid(column=8,row=0,padx=5)
    col11_5.grid(column=10,row=0,padx=5)
    col11_6.grid(column=12,row=0,padx=5)

    # schedSep = ttk.Separator(tab11, orient=HORIZONTAL)
    # schedSep.grid(column=0, row = 0, columnspan='50', sticky='we')
    schedSep2 = ttk.Separator(tab11, orient=VERTICAL)
    schedSep2.grid(column=1, row = 2, rowspan='20', sticky='ns')
    schedSep3 = ttk.Separator(tab11, orient=VERTICAL)
    schedSep3.grid(column=3, row = 2, rowspan='20', sticky='ns')
    schedSep4 = ttk.Separator(tab11, orient=VERTICAL)
    schedSep4.grid(column=5, row = 2, rowspan='20', sticky='ns')
    schedSep5 = ttk.Separator(tab11, orient=VERTICAL)
    schedSep5.grid(column=7, row = 2, rowspan='20', sticky='ns')
    schedSep6 = ttk.Separator(tab11, orient=VERTICAL)
    schedSep6.grid(column=9, row = 2, rowspan='20', sticky='ns')
    schedSep7 = ttk.Separator(tab11, orient=VERTICAL)
    schedSep7.grid(column=11, row = 2, rowspan='20', sticky='ns')
    # schedSep7 = ttk.Separator(tab11, orient=VERTICAL)
    # schedSep7.grid(column=11, row = 2, rowspan='10', sticky='ns')
    # schedSep8 = ttk.Separator(tab11, orient=VERTICAL)
    # schedSep8.grid(column=13, row = 2, rowspan='10', sticky='ns')
    # schedSep9 = ttk.Separator(tab11, orient=VERTICAL)
    # schedSep9.grid(column=15, row = 2, rowspan='10', sticky='ns')
    # schedSep10 = ttk.Separator(tab11, orient=VERTICAL)
    # schedSep10.grid(column=17, row = 2, rowspan='10', sticky='ns')
    # schedSep11 = ttk.Separator(tab11, orient=VERTICAL)
    # schedSep11.grid(column=19, row = 2, rowspan='10', sticky='ns')
    # schedSep12 = ttk.Separator(tab11, orient=VERTICAL)
    # schedSep12.grid(column=21, row = 2, rowspan='10', sticky='ns')
    # schedSep13 = ttk.Separator(tab11, orient=VERTICAL)
    # schedSep13.grid(column=23, row = 2, rowspan='10', sticky='ns')
    # schedSep14 = ttk.Separator(tab11, orient=VERTICAL)
    # schedSep14.grid(column=25, row = 2, rowspan='10', sticky='ns')

    row11_1.grid(column=0,row=2,padx=2,pady=0)
    row11_2.grid(column=0,row=3,padx=2,pady=0)
    row11_3.grid(column=0,row=4,padx=2,pady=0)
    row11_4.grid(column=0,row=5,padx=2,pady=0)
    row11_5.grid(column=0,row=6,padx=2,pady=0)
    row11_6.grid(column=0,row=7,padx=2,pady=0)
    row11_7.grid(column=0,row=8,padx=2,pady=0)
    row11_8.grid(column=0,row=9,padx=2,pady=0)
    row11_9.grid(column=0,row=10,padx=2,pady=0)
    row11_10.grid(column=0,row=11,padx=2,pady=0)
    row11_11.grid(column=0,row=12,padx=2,pady=0)
    row11_12.grid(column=0,row=13,padx=2,pady=0)

    box1pha1text=StringVar()
    box1pha1text.set('                                ')
    box1pha1_LD=Label(tab11, textvariable=box1pha1text, width=40, anchor="e", justify=LEFT)
    box1pha1_LD.grid(column=2,row=2,padx=2,pady=0)
    box1pha2text=StringVar()
    box1pha2text.set('                                ')
    box1pha2_LD=Label(tab11, textvariable=box1pha2text, width=40, anchor="e", justify=LEFT)
    box1pha2_LD.grid(column=2,row=3,padx=2,pady=0)
    box1pha3text=StringVar()
    box1pha3text.set('                                ')
    box1pha3_LD=Label(tab11, textvariable=box1pha3text, width=40, anchor="e", justify=LEFT)
    box1pha3_LD.grid(column=2,row=4,padx=2,pady=0)
    box1pha4text=StringVar()
    box1pha4text.set('                                ')
    box1pha4_LD=Label(tab11, textvariable=box1pha4text, width=40, anchor="e", justify=LEFT)
    box1pha4_LD.grid(column=2,row=5,padx=2,pady=0)
    box1pha5text=StringVar()
    box1pha5text.set('                                ')
    box1pha5_LD=Label(tab11, textvariable=box1pha5text, width=40, anchor="e", justify=LEFT)
    box1pha5_LD.grid(column=2,row=6,padx=2,pady=0)
    box1pha6text=StringVar()
    box1pha6text.set('                                ')
    box1pha6_LD=Label(tab11, textvariable=box1pha6text, width=40, anchor="e", justify=LEFT)
    box1pha6_LD.grid(column=2,row=7,padx=2,pady=0)
    box1pha7text=StringVar()
    box1pha7text.set('                                ')
    box1pha7_LD=Label(tab11, textvariable=box1pha7text, width=40, anchor="e", justify=LEFT)
    box1pha7_LD.grid(column=2,row=8,padx=2,pady=0)
    box1pha8text=StringVar()
    box1pha8text.set('                                ')
    box1pha8_LD=Label(tab11, textvariable=box1pha8text, width=40, anchor="e", justify=LEFT)
    box1pha8_LD.grid(column=2,row=9,padx=2,pady=0)
    box1pha9text=StringVar()
    box1pha9text.set('                                ')
    box1pha9_LD=Label(tab11, textvariable=box1pha9text, width=40, anchor="e", justify=LEFT)
    box1pha9_LD.grid(column=2,row=10,padx=2,pady=0)
    box1pha10text=StringVar()
    box1pha10text.set('                                ')
    box1pha10_LD=Label(tab11, textvariable=box1pha10text, width=40, anchor="e", justify=LEFT)
    box1pha10_LD.grid(column=2,row=11,padx=2,pady=0)
    box1pha11text=StringVar()
    box1pha11text.set('                                ')
    box1pha11_LD=Label(tab11, textvariable=box1pha11text, width=40, anchor="e", justify=LEFT)
    box1pha11_LD.grid(column=2,row=12,padx=2,pady=0)
    box1pha12text=StringVar()
    box1pha12text.set('                                ')
    box1pha12_LD=Label(tab11, textvariable=box1pha12text, width=40, anchor="e", justify=LEFT)
    box1pha12_LD.grid(column=2,row=13,padx=2,pady=0)

    

    box2pha1text=StringVar()
    box2pha1text.set('                                ')
    box2pha1_LD=Label(tab11, textvariable=box2pha1text, width=40, anchor="e", justify=LEFT)
    box2pha1_LD.grid(column=4,row=2,padx=2,pady=0)
    box2pha2text=StringVar()
    box2pha2text.set('                                ')
    box2pha2_LD=Label(tab11, textvariable=box2pha2text, width=40, anchor="e", justify=LEFT)
    box2pha2_LD.grid(column=4,row=3,padx=2,pady=0)
    box2pha3text=StringVar()
    box2pha3text.set('                                ')
    box2pha3_LD=Label(tab11, textvariable=box2pha3text, width=40, anchor="e", justify=LEFT)
    box2pha3_LD.grid(column=4,row=4,padx=2,pady=0)
    box2pha4text=StringVar()
    box2pha4text.set('                                ')
    box2pha4_LD=Label(tab11, textvariable=box2pha4text, width=40, anchor="e", justify=LEFT)
    box2pha4_LD.grid(column=4,row=5,padx=2,pady=0)
    box2pha5text=StringVar()
    box2pha5text.set('                                ')
    box2pha5_LD=Label(tab11, textvariable=box2pha5text, width=40, anchor="e", justify=LEFT)
    box2pha5_LD.grid(column=4,row=6,padx=2,pady=0)
    box2pha6text=StringVar()
    box2pha6text.set('                                ')
    box2pha6_LD=Label(tab11, textvariable=box2pha6text, width=40, anchor="e", justify=LEFT)
    box2pha6_LD.grid(column=4,row=7,padx=2,pady=0)
    box2pha7text=StringVar()
    box2pha7text.set('                                ')
    box2pha7_LD=Label(tab11, textvariable=box2pha7text, width=40, anchor="e", justify=LEFT)
    box2pha7_LD.grid(column=4,row=8,padx=2,pady=0)
    box2pha8text=StringVar()
    box2pha8text.set('                                ')
    box2pha8_LD=Label(tab11, textvariable=box2pha8text, width=40, anchor="e", justify=LEFT)
    box2pha8_LD.grid(column=4,row=9,padx=2,pady=0)
    box2pha9text=StringVar()
    box2pha9text.set('                                ')
    box2pha9_LD=Label(tab11, textvariable=box2pha9text, width=40, anchor="e", justify=LEFT)
    box2pha9_LD.grid(column=4,row=10,padx=2,pady=0)
    box2pha10text=StringVar()
    box2pha10text.set('                                ')
    box2pha10_LD=Label(tab11, textvariable=box2pha10text, width=40, anchor="e", justify=LEFT)
    box2pha10_LD.grid(column=4,row=11,padx=2,pady=0)
    box2pha11text=StringVar()
    box2pha11text.set('                                ')
    box2pha11_LD=Label(tab11, textvariable=box2pha11text, width=40, anchor="e", justify=LEFT)
    box2pha11_LD.grid(column=4,row=12,padx=2,pady=0)
    box2pha12text=StringVar()
    box2pha12text.set('                                ')
    box2pha12_LD=Label(tab11, textvariable=box2pha12text, width=40, anchor="e", justify=LEFT)
    box2pha12_LD.grid(column=4,row=13,padx=2,pady=0)

    

    box3pha1text=StringVar()
    box3pha1text.set('                                ')
    box3pha1_LD=Label(tab11, textvariable=box3pha1text, width=40, anchor="e", justify=LEFT)
    box3pha1_LD.grid(column=6,row=2,padx=2,pady=0)
    box3pha2text=StringVar()
    box3pha2text.set('                                ')
    box3pha2_LD=Label(tab11, textvariable=box3pha2text, width=40, anchor="e", justify=LEFT)
    box3pha2_LD.grid(column=6,row=3,padx=2,pady=0)
    box3pha3text=StringVar()
    box3pha3text.set('                                ')
    box3pha3_LD=Label(tab11, textvariable=box3pha3text, width=40, anchor="e", justify=LEFT)
    box3pha3_LD.grid(column=6,row=4,padx=2,pady=0)
    box3pha4text=StringVar()
    box3pha4text.set('                                ')
    box3pha4_LD=Label(tab11, textvariable=box3pha4text, width=40, anchor="e", justify=LEFT)
    box3pha4_LD.grid(column=6,row=5,padx=2,pady=0)
    box3pha5text=StringVar()
    box3pha5text.set('                                ')
    box3pha5_LD=Label(tab11, textvariable=box3pha5text, width=40, anchor="e", justify=LEFT)
    box3pha5_LD.grid(column=6,row=6,padx=2,pady=0)
    box3pha6text=StringVar()
    box3pha6text.set('                                ')
    box3pha6_LD=Label(tab11, textvariable=box3pha6text, width=40, anchor="e", justify=LEFT)
    box3pha6_LD.grid(column=6,row=7,padx=2,pady=0)
    box3pha7text=StringVar()
    box3pha7text.set('                                ')
    box3pha7_LD=Label(tab11, textvariable=box3pha7text, width=40, anchor="e", justify=LEFT)
    box3pha7_LD.grid(column=6,row=8,padx=2,pady=0)
    box3pha8text=StringVar()
    box3pha8text.set('                                ')
    box3pha8_LD=Label(tab11, textvariable=box3pha8text, width=40, anchor="e", justify=LEFT)
    box3pha8_LD.grid(column=6,row=9,padx=2,pady=0)
    box3pha9text=StringVar()
    box3pha9text.set('                                ')
    box3pha9_LD=Label(tab11, textvariable=box3pha9text, width=40, anchor="e", justify=LEFT)
    box3pha9_LD.grid(column=6,row=10,padx=2,pady=0)
    box3pha10text=StringVar()
    box3pha10text.set('                                ')
    box3pha10_LD=Label(tab11, textvariable=box3pha10text, width=40, anchor="e", justify=LEFT)
    box3pha10_LD.grid(column=6,row=11,padx=2,pady=0)
    box3pha11text=StringVar()
    box3pha11text.set('                                ')
    box3pha11_LD=Label(tab11, textvariable=box3pha11text, width=40, anchor="e", justify=LEFT)
    box3pha11_LD.grid(column=6,row=12,padx=2,pady=0)
    box3pha12text=StringVar()
    box3pha12text.set('                                ')
    box3pha12_LD=Label(tab11, textvariable=box3pha12text, width=40, anchor="e", justify=LEFT)
    box3pha12_LD.grid(column=6,row=13,padx=2,pady=0)
    
    

    box4pha1text=StringVar()
    box4pha1text.set('                                ')
    box4pha1_LD=Label(tab11, textvariable=box4pha1text, width=40, anchor="e", justify=LEFT)
    box4pha1_LD.grid(column=8,row=2,padx=2,pady=0)
    box4pha2text=StringVar()
    box4pha2text.set('                                ')
    box4pha2_LD=Label(tab11, textvariable=box4pha2text, width=40, anchor="e", justify=LEFT)
    box4pha2_LD.grid(column=8,row=3,padx=2,pady=0)
    box4pha3text=StringVar()
    box4pha3text.set('                                ')
    box4pha3_LD=Label(tab11, textvariable=box4pha3text, width=40, anchor="e", justify=LEFT)
    box4pha3_LD.grid(column=8,row=4,padx=2,pady=0)
    box4pha4text=StringVar()
    box4pha4text.set('                                ')
    box4pha4_LD=Label(tab11, textvariable=box4pha4text, width=40, anchor="e", justify=LEFT)
    box4pha4_LD.grid(column=8,row=5,padx=2,pady=0)
    box4pha5text=StringVar()
    box4pha5text.set('                                ')
    box4pha5_LD=Label(tab11, textvariable=box4pha5text, width=40, anchor="e", justify=LEFT)
    box4pha5_LD.grid(column=8,row=6,padx=2,pady=0)
    box4pha6text=StringVar()
    box4pha6text.set('                                ')
    box4pha6_LD=Label(tab11, textvariable=box4pha6text, width=40, anchor="e", justify=LEFT)
    box4pha6_LD.grid(column=8,row=7,padx=2,pady=0)
    box4pha7text=StringVar()
    box4pha7text.set('                                ')
    box4pha7_LD=Label(tab11, textvariable=box4pha7text, width=40, anchor="e", justify=LEFT)
    box4pha7_LD.grid(column=8,row=8,padx=2,pady=0)
    box4pha8text=StringVar()
    box4pha8text.set('                                ')
    box4pha8_LD=Label(tab11, textvariable=box4pha8text, width=40, anchor="e", justify=LEFT)
    box4pha8_LD.grid(column=8,row=9,padx=2,pady=0)
    box4pha9text=StringVar()
    box4pha9text.set('                                ')
    box4pha9_LD=Label(tab11, textvariable=box4pha9text, width=40, anchor="e", justify=LEFT)
    box4pha9_LD.grid(column=8,row=10,padx=2,pady=0)
    box4pha10text=StringVar()
    box4pha10text.set('                                ')
    box4pha10_LD=Label(tab11, textvariable=box4pha10text, width=40, anchor="e", justify=LEFT)
    box4pha10_LD.grid(column=8,row=11,padx=2,pady=0)
    box4pha11text=StringVar()
    box4pha11text.set('                                ')
    box4pha11_LD=Label(tab11, textvariable=box4pha11text, width=40, anchor="e", justify=LEFT)
    box4pha11_LD.grid(column=8,row=12,padx=2,pady=0)
    box4pha12text=StringVar()
    box4pha12text.set('                                ')
    box4pha12_LD=Label(tab11, textvariable=box4pha12text, width=40, anchor="e", justify=LEFT)
    box4pha12_LD.grid(column=8,row=13,padx=2,pady=0)

   

    box5pha1text=StringVar()
    box5pha1text.set('                                ')
    box5pha1_LD=Label(tab11, textvariable=box5pha1text, width=40, anchor="e", justify=LEFT)
    box5pha1_LD.grid(column=10,row=2,padx=2,pady=0)
    box5pha2text=StringVar()
    box5pha2text.set('                                ')
    box5pha2_LD=Label(tab11, textvariable=box5pha2text, width=40, anchor="e", justify=LEFT)
    box5pha2_LD.grid(column=10,row=3,padx=2,pady=0)
    box5pha3text=StringVar()
    box5pha3text.set('                                ')
    box5pha3_LD=Label(tab11, textvariable=box5pha3text, width=40, anchor="e", justify=LEFT)
    box5pha3_LD.grid(column=10,row=4,padx=2,pady=0)
    box5pha4text=StringVar()
    box5pha4text.set('                                ')
    box5pha4_LD=Label(tab11, textvariable=box5pha4text, width=40, anchor="e", justify=LEFT)
    box5pha4_LD.grid(column=10,row=5,padx=2,pady=0)
    box5pha5text=StringVar()
    box5pha5text.set('                                ')
    box5pha5_LD=Label(tab11, textvariable=box5pha5text, width=40, anchor="e", justify=LEFT)
    box5pha5_LD.grid(column=10,row=6,padx=2,pady=0)
    box5pha6text=StringVar()
    box5pha6text.set('                                ')
    box5pha6_LD=Label(tab11, textvariable=box5pha6text, width=40, anchor="e", justify=LEFT)
    box5pha6_LD.grid(column=10,row=7,padx=2,pady=0)
    box5pha7text=StringVar()
    box5pha7text.set('                                ')
    box5pha7_LD=Label(tab11, textvariable=box5pha7text, width=40, anchor="e", justify=LEFT)
    box5pha7_LD.grid(column=10,row=8,padx=2,pady=0)
    box5pha8text=StringVar()
    box5pha8text.set('                                ')
    box5pha8_LD=Label(tab11, textvariable=box5pha8text, width=40, anchor="e", justify=LEFT)
    box5pha8_LD.grid(column=10,row=9,padx=2,pady=0)
    box5pha9text=StringVar()
    box5pha9text.set('                                ')
    box5pha9_LD=Label(tab11, textvariable=box5pha9text, width=40, anchor="e", justify=LEFT)
    box5pha9_LD.grid(column=10,row=10,padx=2,pady=0)
    box5pha10text=StringVar()
    box5pha10text.set('                                ')
    box5pha10_LD=Label(tab11, textvariable=box5pha10text, width=40, anchor="e", justify=LEFT)
    box5pha10_LD.grid(column=10,row=11,padx=2,pady=0)
    box5pha11text=StringVar()
    box5pha11text.set('                                ')
    box5pha11_LD=Label(tab11, textvariable=box5pha11text, width=40, anchor="e", justify=LEFT)
    box5pha11_LD.grid(column=10,row=12,padx=2,pady=0)
    box5pha12text=StringVar()
    box5pha12text.set('                                ')
    box5pha12_LD=Label(tab11, textvariable=box5pha12text, width=40, anchor="e", justify=LEFT)
    box5pha12_LD.grid(column=10,row=13,padx=2,pady=0)

    box6pha1text=StringVar()
    box6pha1text.set('                                ')
    box6pha1_LD=Label(tab11, textvariable=box6pha1text, width=40, anchor="e", justify=LEFT)
    box6pha1_LD.grid(column=12,row=2,padx=2,pady=0)
    box6pha2text=StringVar()
    box6pha2text.set('                                ')
    box6pha2_LD=Label(tab11, textvariable=box6pha2text, width=40, anchor="e", justify=LEFT)
    box6pha2_LD.grid(column=12,row=3,padx=2,pady=0)
    box6pha3text=StringVar()
    box6pha3text.set('                                ')
    box6pha3_LD=Label(tab11, textvariable=box6pha3text, width=40, anchor="e", justify=LEFT)
    box6pha3_LD.grid(column=12,row=4,padx=2,pady=0)
    box6pha4text=StringVar()
    box6pha4text.set('                                ')
    box6pha4_LD=Label(tab11, textvariable=box6pha4text, width=40, anchor="e", justify=LEFT)
    box6pha4_LD.grid(column=12,row=5,padx=2,pady=0)
    box6pha5text=StringVar()
    box6pha5text.set('                                ')
    box6pha5_LD=Label(tab11, textvariable=box6pha5text, width=40, anchor="e", justify=LEFT)
    box6pha5_LD.grid(column=12,row=6,padx=2,pady=0)
    box6pha6text=StringVar()
    box6pha6text.set('                                ')
    box6pha6_LD=Label(tab11, textvariable=box6pha6text, width=40, anchor="e", justify=LEFT)
    box6pha6_LD.grid(column=12,row=7,padx=2,pady=0)
    box6pha7text=StringVar()
    box6pha7text.set('                                ')
    box6pha7_LD=Label(tab11, textvariable=box6pha7text, width=40, anchor="e", justify=LEFT)
    box6pha7_LD.grid(column=12,row=8,padx=2,pady=0)
    box6pha8text=StringVar()
    box6pha8text.set('                                ')
    box6pha8_LD=Label(tab11, textvariable=box6pha8text, width=40, anchor="e", justify=LEFT)
    box6pha8_LD.grid(column=12,row=9,padx=2,pady=0)
    box6pha9text=StringVar()
    box6pha9text.set('                                ')
    box6pha9_LD=Label(tab11, textvariable=box6pha9text, width=40, anchor="e", justify=LEFT)
    box6pha9_LD.grid(column=12,row=10,padx=2,pady=0)
    box6pha10text=StringVar()
    box6pha10text.set('                                ')
    box6pha10_LD=Label(tab11, textvariable=box6pha10text, width=40, anchor="e", justify=LEFT)
    box6pha10_LD.grid(column=12,row=11,padx=2,pady=0)
    box6pha11text=StringVar()
    box6pha11text.set('                                ')
    box6pha11_LD=Label(tab11, textvariable=box6pha11text, width=40, anchor="e", justify=LEFT)
    box6pha11_LD.grid(column=12,row=12,padx=2,pady=0)
    box6pha12text=StringVar()
    box6pha12text.set('                                ')
    box6pha12_LD=Label(tab11, textvariable=box6pha12text, width=40, anchor="e", justify=LEFT)
    box6pha12_LD.grid(column=12,row=13,padx=2,pady=0)

    if initLED1.get() == 1: 
        LED_state1 = 'ON'
    else:
        LED_state1 = 'OFF'

    if initLED2.get() == 1: 
        LED_state2 = 'ON'
    else:
        LED_state2 = 'OFF'

    if initLED3.get() == 1: 
        LED_state3 = 'ON'
    else:
        LED_state3 = 'OFF'

    if initLED4.get() == 1: 
        LED_state4 = 'ON'
    else:
        LED_state4 = 'OFF'

    if initLED5.get()== 1: 
        LED_state5 = 'ON'
    else:
        LED_state5 = 'OFF'

    if initLED6.get()== 1: 
        LED_state6 = 'ON'
    else:
        LED_state6 = 'OFF'

    #1 Phase
    if light1_1=='0' and dark1_1=='0':
        box1pha1text.set('                                ')
        
        box1pha1text.set('Init LED: ' + str(LED_state1) +' from record onset'+' | '+hourOn1_1+':'+minOn1_1+' on>'+hourOff1_1+':'+minOff1_1+' off' + ' (' + tcycle_1_1 + 'h)')
       
    if light1_1=='0' and dark1_1=='1':
        box1pha1text.set('                                ')
        
        box1pha1text.set('Init LED: ' + str(LED_state1) +' from record onset'+' | '+'DD' + ' (' + tcycle_1_1 + 'h)')
       
    if light1_1=='1' and dark1_1=='0':
        box1pha1text.set('                                ')
        
        box1pha1text.set('Init LED: ' + str(LED_state1) +' from record onset'+' | '+'LL' + ' (' + tcycle_1_1 + 'h)')
        
    

    if light2_1=='0' and dark2_1=='0':
        box2pha1text.set('                                ')
        
        box2pha1text.set('Init LED: ' + str(LED_state2) +' from record onset'+' | '+hourOn2_1+':'+minOn2_1+' on>'+hourOff2_1+':'+minOff2_1+' off'+ ' (' + tcycle_2_1 + 'h)')
       
    if light2_1=='0' and dark2_1=='1':
        box2pha1text.set('                                ')
       
        box2pha1text.set('Init LED: ' + str(LED_state2) +' from record onset'+' | '+'DD'+ ' (' + tcycle_2_1 + 'h)')
        
    if light2_1=='1' and dark2_1=='0':
        box2pha1text.set('                                ')
       
        box2pha1text.set('Init LED: ' + str(LED_state2) +' from record onset'+' | '+'LL'+ ' (' + tcycle_2_1 + 'h)')
       

    if light3_1=='0' and dark3_1=='0':
        box3pha1text.set('                                ')
       
        box3pha1text.set('Init LED: ' + str(LED_state3) +' from record onset'+' | '+hourOn3_1+':'+minOn3_1+' on>'+hourOff3_1+':'+minOff3_1+' off'+ ' (' + tcycle_3_1 + 'h)')
        
    if light3_1=='0' and dark3_1=='1':
        box3pha1text.set('                                ')
       
        box3pha1text.set('Init LED: ' + str(LED_state3) +' from record onset'+' | '+'DD'+ ' (' + tcycle_3_1 + 'h)')
        
    if light3_1=='1' and dark3_1=='0':
        box3pha1text.set('                                ')
        
        box3pha1text.set('Init LED: ' + str(LED_state3)+ ' from record onset'+' | '+'LL'+ ' (' + tcycle_3_1 + 'h)')
        

    if light4_1=='0' and dark4_1=='0':
        box4pha1text.set('                                ')
        
        box4pha1text.set('Init LED: ' + str(LED_state4) +' from record onset'+' | '+hourOn4_1+':'+minOn4_1+' on>'+hourOff4_1+':'+minOff4_1+' off'+ ' (' + tcycle_4_1 + 'h)')
        
    if light4_1=='0' and dark4_1=='1':
        box4pha1text.set('                                ')
        
        box4pha1text.set('Init LED: ' + str(LED_state4) +' from record onset'+' | '+'DD'+ ' (' + tcycle_4_1 + 'h)')
        
    if light4_1=='1' and dark4_1=='0':
        box4pha1text.set('                                ')
        
        box4pha1text.set('Init LED: ' + str(LED_state4) +' from record onset'+' | '+'LL'+ ' (' + tcycle_4_1 + 'h)')
        

    if light5_1=='0' and dark5_1=='0':
        box5pha1text.set('                                ')
        
        box5pha1text.set('Init LED: ' + str(LED_state5)+ ' from record onset'+' | '+hourOn5_1+':'+minOn5_1+' on>'+hourOff5_1+':'+minOff5_1+' off'+ ' (' + tcycle_5_1 + 'h)')
        
    if light5_1=='0' and dark5_1=='1':
        box5pha1text.set('                                ')
        
        box5pha1text.set('Init LED: ' + str(LED_state5) +' from record onset'+' | '+'DD'+ ' (' + tcycle_5_1 + 'h)')
        
    if light5_1=='1' and dark5_1=='0':
        box5pha1text.set('                                ')
        
        box5pha1text.set('Init LED: ' + str(LED_state5) +' from record onset'+' | '+'LL'+ ' (' + tcycle_5_1 + 'h)')

    if light6_1=='0' and dark6_1=='0':
        box6pha1text.set('                                ')
        
        box6pha1text.set('Init LED: ' + str(LED_state6)+ ' from record onset'+' | '+hourOn6_1+':'+minOn6_1+' on>'+hourOff6_1+':'+minOff6_1+' off'+ ' (' + tcycle_6_1 + 'h)')
        
    if light6_1=='0' and dark6_1=='1':
        box6pha1text.set('                                ')
        
        box6pha1text.set('Init LED: ' + str(LED_state6) +' from record onset'+' | '+'DD'+ ' (' + tcycle_6_1 + 'h)')
        
    if light6_1=='1' and dark6_1=='0':
        box6pha1text.set('                                ')
        
        box6pha1text.set('Init LED: ' + str(LED_state6) +' from record onset'+' | '+'LL'+ ' (' + tcycle_6_1 + 'h)')
        

    #2 Phase
    if light1_2=='0' and dark1_2=='0':
        box1pha2text.set('                                ')
        
        box1pha2text.set(year1_2+'/'+month1_2+'/'+date1_2+' '+hourFrom2_2+':'+minuteFrom1_2+' | '+hourOn1_2+':'+minOn1_2+' on>'+hourOff1_2+':'+minOff1_2+' off'+ ' (' + tcycle_1_2 + 'h)')
        
    if light1_2=='0' and dark1_2=='1':
        box1pha2text.set('                                ')
        
        box1pha2text.set(year1_2+'/'+month1_2+'/'+date1_2+' '+hourFrom2_2+':'+minuteFrom1_2+' | '+'DD'+ ' (' + tcycle_1_2 + 'h)')
        
    if light1_2=='1' and dark1_2=='0':
        box1pha2text.set('                                ')
        
        box1pha2text.set(year1_2+'/'+month1_2+'/'+date1_2+' '+hourFrom2_2+':'+minuteFrom1_2+' | '+'LL'+ ' (' + tcycle_1_2 + 'h)')
        

    if light2_2=='0' and dark2_2=='0':
        box2pha2text.set('                                ')
        
        box2pha2text.set(year2_2+'/'+month2_2+'/'+date2_2+' '+hourFrom2_2+':'+minuteFrom2_2+' | '+hourOn2_2+':'+minOn2_2+' on>'+hourOff2_2+':'+minOff2_2+' off'+ ' (' + tcycle_2_2 + 'h)')
        
    if light2_2=='0' and dark2_2=='1':
        box2pha2text.set('                                ')
        
        box2pha2text.set(year2_2+'/'+month2_2+'/'+date2_2+' '+hourFrom2_2+':'+minuteFrom2_2+' | '+'DD'+ ' (' + tcycle_2_2 + 'h)')
        
    if light2_2=='1' and dark2_2=='0':
        box2pha2text.set('                                ')
        
        box2pha2text.set(year2_2+'/'+month2_2+'/'+date2_2+' '+hourFrom2_2+':'+minuteFrom2_2+' | '+'LL'+ ' (' + tcycle_2_2 + 'h)')
        

    if light3_2=='0' and dark3_2=='0':
        box3pha2text.set('                                ')
        
        box3pha2text.set(year3_2+'/'+month3_2+'/'+date3_2+' '+hourFrom3_2+':'+minuteFrom3_2+' | '+hourOn3_2+':'+minOn3_2+' on>'+hourOff3_2+':'+minOff3_2+' off'+ ' (' + tcycle_3_2 + 'h)')
        
    if light3_2=='0' and dark3_2=='1':
        box3pha2text.set('                                ')
        
        box3pha2text.set(year3_2+'/'+month3_2+'/'+date3_2+' '+hourFrom3_2+':'+minuteFrom3_2+' | '+'DD'+ ' (' + tcycle_3_2 + 'h)')
        
    if light3_2=='1' and dark3_2=='0':
        box3pha2text.set('                                ')
        
        box3pha2text.set(year3_2+'/'+month3_2+'/'+date3_2+' '+hourFrom3_2+':'+minuteFrom3_2+' | '+'LL'+ ' (' + tcycle_3_2 + 'h)')
        

    if light4_2=='0' and dark4_2=='0':
        box4pha2text.set('                                ')
        
        box4pha2text.set(year4_2+'/'+month4_2+'/'+date4_2+' '+hourFrom4_2+':'+minuteFrom4_2+' | '+hourOn4_2+':'+minOn4_2+' on>'+hourOff4_2+':'+minOff4_2+' off'+ ' (' + tcycle_4_2 + 'h)')
        
    if light4_2=='0' and dark4_2=='1':
        box4pha2text.set('                                ')
        
        box4pha2text.set(year4_2+'/'+month4_2+'/'+date4_2+' '+hourFrom4_2+':'+minuteFrom4_2+' | '+'DD'+ ' (' + tcycle_4_2 + 'h)')
        
    if light4_2=='1' and dark4_2=='0':
        box4pha2text.set('                                ')
        
        box4pha2text.set(year4_2+'/'+month4_2+'/'+date4_2+' '+hourFrom4_2+':'+minuteFrom4_2+' | '+'LL'+ ' (' + tcycle_4_2 + 'h)')
        

    if light5_2=='0' and dark5_2=='0':
        box5pha2text.set('                                ')
        
        box5pha2text.set(year5_2+'/'+month5_2+'/'+date5_2+' '+hourFrom5_2+':'+minuteFrom5_2+' | '+hourOn5_2+':'+minOn5_2+' on>'+hourOff5_2+':'+minOff5_2+' off'+ ' (' + tcycle_5_2 + 'h)')
        
    if light5_2=='0' and dark5_2=='1':
        box5pha2text.set('                                ')
        
        box5pha2text.set(year5_2+'/'+month5_2+'/'+date5_2+' '+hourFrom5_2+':'+minuteFrom5_2+' | '+'DD'+ ' (' + tcycle_5_2 + 'h)')
        
    if light5_2=='1' and dark5_2=='0':
        box5pha2text.set('                                ')
        
        box5pha2text.set(year5_2+'/'+month5_2+'/'+date5_2+' '+hourFrom5_2+':'+minuteFrom5_2+' | '+'LL'+ ' (' + tcycle_5_2 + 'h)')

    if light6_2=='0' and dark6_2=='0':
        box6pha2text.set('                                ')
        
        box6pha2text.set(year6_2+'/'+month6_2+'/'+date6_2+' '+hourFrom6_2+':'+minuteFrom6_2+' | '+hourOn6_2+':'+minOn6_2+' on>'+hourOff6_2+':'+minOff6_2+' off'+ ' (' + tcycle_6_2 + 'h)')
        
    if light6_2=='0' and dark6_2=='1':
        box6pha2text.set('                                ')
        
        box6pha2text.set(year6_2+'/'+month6_2+'/'+date6_2+' '+hourFrom6_2+':'+minuteFrom6_2+' | '+'DD'+ ' (' + tcycle_6_2 + 'h)')
        
    if light6_2=='1' and dark6_2=='0':
        box6pha2text.set('                                ')
        
        box6pha2text.set(year6_2+'/'+month6_2+'/'+date6_2+' '+hourFrom6_2+':'+minuteFrom6_2+' | '+'LL'+ ' (' + tcycle_6_2 + 'h)')    

    #3 Phase
    if light1_3=='0' and dark1_3=='0':
        box1pha3text.set('                                ')
        
        box1pha3text.set(year1_3+'/'+month1_3+'/'+date1_3+' '+hourFrom2_3+':'+minuteFrom1_3+' | '+hourOn1_3+':'+minOn1_3+' on>'+hourOff1_3+':'+minOff1_3+' off'+ ' (' + tcycle_1_3 + 'h)')
        
    if light1_3=='0' and dark1_3=='1':
        box1pha3text.set('                                ')
        
        box1pha3text.set(year1_3+'/'+month1_3+'/'+date1_3+' '+hourFrom2_3+':'+minuteFrom1_3+' | '+'DD'+ ' (' + tcycle_1_3 + 'h)')
        
    if light1_3=='1' and dark1_3=='0':
        box1pha3text.set('                                 ')
        
        box1pha3text.set(year1_3+'/'+month1_3+'/'+date1_3+' '+hourFrom2_3+':'+minuteFrom1_3+' | '+'LL'+ ' (' + tcycle_1_3 + 'h)')
        
    
    if light2_3=='0' and dark2_3=='0':
        box2pha3text.set('                                ')
        
        box2pha3text.set(year2_3+'/'+month2_3+'/'+date2_3+' '+hourFrom2_3+':'+minuteFrom2_3+' | '+hourOn2_3+':'+minOn2_3+' on>'+hourOff2_3+':'+minOff2_3+' off'+ ' (' + tcycle_2_3 + 'h)')
        
    if light2_3=='0' and dark2_3=='1':
        box2pha3text.set('                                ')
        
        box2pha3text.set(year2_3+'/'+month2_3+'/'+date2_3+' '+hourFrom2_3+':'+minuteFrom2_3+' | '+'DD'+ ' (' + tcycle_2_3 + 'h)')
        
    if light2_3=='1' and dark2_3=='0':
        box2pha3text.set('                                 ')
        
        box2pha3text.set(year2_3+'/'+month2_3+'/'+date2_3+' '+hourFrom2_3+':'+minuteFrom2_3+' | '+'LL'+ ' (' + tcycle_2_3 + 'h)')
        

    if light3_3=='0' and dark3_3=='0':
        box3pha3text.set('                                ')
        
        box3pha3text.set(year3_3+'/'+month3_3+'/'+date3_3+' '+hourFrom3_3+':'+minuteFrom3_3+' | '+hourOn3_3+':'+minOn3_3+' on>'+hourOff3_3+':'+minOff3_3+' off'+ ' (' + tcycle_3_3 + 'h)')
        
    if light3_3=='0' and dark3_3=='1':
        box3pha3text.set('                                ')
        
        box3pha3text.set(year3_3+'/'+month3_3+'/'+date3_3+' '+hourFrom3_3+':'+minuteFrom3_3+' | '+'DD'+ ' (' + tcycle_3_3 + 'h)')
        
    if light3_3=='1' and dark3_3=='0':
        box3pha3text.set('                                 ')
        
        box3pha3text.set(year3_3+'/'+month3_3+'/'+date3_3+' '+hourFrom3_3+':'+minuteFrom3_3+' | '+'LL'+ ' (' + tcycle_3_3 + 'h)')
        

    if light4_3=='0' and dark4_3=='0':
        box4pha3text.set('                                ')
        
        box4pha3text.set(year4_3+'/'+month4_3+'/'+date4_3+' '+hourFrom4_3+':'+minuteFrom4_3+' | '+hourOn4_3+':'+minOn4_3+' on>'+hourOff4_3+':'+minOff4_3+' off'+ ' (' + tcycle_4_3 + 'h)')
        
    if light4_3=='0' and dark4_3=='1':
        box4pha3text.set('                                ')
        
        box4pha3text.set(year4_3+'/'+month4_3+'/'+date4_3+' '+hourFrom4_3+':'+minuteFrom4_3+' | '+'DD'+ ' (' + tcycle_4_3 + 'h)')
        
    if light4_3=='1' and dark4_3=='0':
        box4pha3text.set('                                 ')
        
        box4pha3text.set(year4_3+'/'+month4_3+'/'+date4_3+' '+hourFrom4_3+':'+minuteFrom4_3+' | '+'LL'+ ' (' + tcycle_4_3 + 'h)')
        

    if light5_3=='0' and dark5_3=='0':
        box5pha3text.set('                                ')
        
        box5pha3text.set(year5_3+'/'+month5_3+'/'+date5_3+' '+hourFrom5_3+':'+minuteFrom5_3+' | '+hourOn5_3+':'+minOn5_3+' on>'+hourOff5_3+':'+minOff5_3+' off'+ ' (' + tcycle_5_3 + 'h)')
        
    if light5_3=='0' and dark5_3=='1':
        box5pha3text.set('                                ')
        
        box5pha3text.set(year5_3+'/'+month5_3+'/'+date5_3+' '+hourFrom5_3+':'+minuteFrom5_3+' | '+'DD'+ ' (' + tcycle_5_3 + 'h)')
        
    if light5_3=='1' and dark5_3=='0':
        box5pha3text.set('                                 ')
        
        box5pha3text.set(year5_3+'/'+month5_3+'/'+date5_3+' '+hourFrom5_3+':'+minuteFrom5_3+' | '+'LL'+ ' (' + tcycle_5_3 + 'h)')
        
    if light6_3=='0' and dark6_3=='0':
        box6pha3text.set('                                ')
        
        box6pha3text.set(year6_3+'/'+month6_3+'/'+date6_3+' '+hourFrom6_3+':'+minuteFrom6_3+' | '+hourOn6_3+':'+minOn6_3+' on>'+hourOff6_3+':'+minOff6_3+' off'+ ' (' + tcycle_6_3 + 'h)')
        
    if light6_3=='0' and dark6_3=='1':
        box6pha3text.set('                                ')
        
        box6pha3text.set(year6_3+'/'+month6_3+'/'+date6_3+' '+hourFrom6_3+':'+minuteFrom6_3+' | '+'DD'+ ' (' + tcycle_6_3 + 'h)')
        
    if light6_3=='1' and dark6_3=='0':
        box6pha3text.set('                                 ')
        
        box6pha3text.set(year6_3+'/'+month6_3+'/'+date6_3+' '+hourFrom6_3+':'+minuteFrom6_3+' | '+'LL'+ ' (' + tcycle_6_3 + 'h)')

    # 4 Phase
    if light1_4=='0' and dark1_4=='0':
        box1pha4text.set('                                ')
        
        box1pha4text.set(year1_4+'/'+month1_4+'/'+date1_4+' '+hourFrom2_4+':'+minuteFrom1_4+' | '+hourOn1_4+':'+minOn1_4+' on>'+hourOff1_4+':'+minOff1_4+' off'+ ' (' + tcycle_1_4 + 'h)')
        
    if light1_4=='0' and dark1_4=='1':
        box1pha4text.set('                                ')
        
        box1pha4text.set(year1_4+'/'+month1_4+'/'+date1_4+' '+hourFrom2_4+':'+minuteFrom1_4+' | '+'DD'+ ' (' + tcycle_1_4 + 'h)')
        
    if light1_4=='1' and dark1_4=='0':
        box1pha4text.set('                                 ')
        
        box1pha4text.set(year1_4+'/'+month1_4+'/'+date1_4+' '+hourFrom2_4+':'+minuteFrom1_4+' | '+'LL'+ ' (' + tcycle_1_4 + 'h)')
        

    if light2_4=='0' and dark2_4=='0':
        box2pha4text.set('                                ')
        
        box2pha4text.set(year2_4+'/'+month2_4+'/'+date2_4+' '+hourFrom2_4+':'+minuteFrom2_4+' | '+hourOn2_4+':'+minOn2_4+' on>'+hourOff2_4+':'+minOff2_4+' off'+ ' (' + tcycle_2_4 + 'h)')
        
    if light2_4=='0' and dark2_4=='1':
        box2pha4text.set('                                ')
        
        box2pha4text.set(year2_4+'/'+month2_4+'/'+date2_4+' '+hourFrom2_4+':'+minuteFrom2_4+' | '+'DD'+ ' (' + tcycle_2_4 + 'h)')
        
    if light2_4=='1' and dark2_4=='0':
        box2pha4text.set('                                 ')
        
        box2pha4text.set(year2_4+'/'+month2_4+'/'+date2_4+' '+hourFrom2_4+':'+minuteFrom2_4+' | '+'LL'+ ' (' + tcycle_2_4 + 'h)')
        

    if light3_4=='0' and dark3_4=='0':
        box3pha4text.set('                                ')
        
        box3pha4text.set(year3_4+'/'+month3_4+'/'+date3_4+' '+hourFrom3_4+':'+minuteFrom3_4+' | '+hourOn3_4+':'+minOn3_4+' on>'+hourOff3_4+':'+minOff3_4+' off'+ ' (' + tcycle_3_4 + 'h)')
        
    if light3_4=='0' and dark3_4=='1':
        box3pha4text.set('                                ')
        
        box3pha4text.set(year3_4+'/'+month3_4+'/'+date3_4+' '+hourFrom3_4+':'+minuteFrom3_4+' | '+'DD'+ ' (' + tcycle_3_4 + 'h)')
        
    if light3_4=='1' and dark3_4=='0':
        box3pha4text.set('                                 ')
        
        box3pha4text.set(year3_4+'/'+month3_4+'/'+date3_4+' '+hourFrom3_4+':'+minuteFrom3_4+' | '+'LL'+ ' (' + tcycle_3_4 + 'h)')
        

    if light4_4=='0' and dark4_4=='0':
        box4pha4text.set('                                ')
        
        box4pha4text.set(year4_4+'/'+month4_4+'/'+date4_4+' '+hourFrom4_4+':'+minuteFrom4_4+' | '+hourOn4_4+':'+minOn4_4+' on>'+hourOff4_4+':'+minOff4_4+' off'+ ' (' + tcycle_4_4 + 'h)')
        
    if light4_4=='0' and dark4_4=='1':
        box4pha4text.set('                                ')
        
        box4pha4text.set(year4_4+'/'+month4_4+'/'+date4_4+' '+hourFrom4_4+':'+minuteFrom4_4+' | '+'DD'+ ' (' + tcycle_4_4 + 'h)')
        
    if light4_4=='1' and dark4_4=='0':
        box4pha4text.set('                                 ')
        
        box4pha4text.set(year4_4+'/'+month4_4+'/'+date4_4+' '+hourFrom4_4+':'+minuteFrom4_4+' | '+'LL'+ ' (' + tcycle_4_4 + 'h)')
        

    if light5_4=='0' and dark5_4=='0':
        box5pha4text.set('                                ')
        
        box5pha4text.set(year5_4+'/'+month5_4+'/'+date5_4+' '+hourFrom5_4+':'+minuteFrom5_4+' | '+hourOn5_4+':'+minOn5_4+' on>'+hourOff5_4+':'+minOff5_4+' off'+ ' (' + tcycle_5_4 + 'h)')
        
    if light5_4=='0' and dark5_4=='1':
        box5pha4text.set('                                ')
        
        box5pha4text.set(year5_4+'/'+month5_4+'/'+date5_4+' '+hourFrom5_4+':'+minuteFrom5_4+' | '+'DD'+ ' (' + tcycle_5_4 + 'h)')
        
    if light5_4=='1' and dark5_4=='0':
        box5pha4text.set('                                 ')
        
        box5pha4text.set(year5_4+'/'+month5_4+'/'+date5_4+' '+hourFrom5_4+':'+minuteFrom5_4+' | '+'LL'+ ' (' + tcycle_5_4 + 'h)')
        
    if light6_4=='0' and dark6_4=='0':
        box6pha4text.set('                                ')
        
        box6pha4text.set(year6_4+'/'+month6_4+'/'+date6_4+' '+hourFrom6_4+':'+minuteFrom6_4+' | '+hourOn6_4+':'+minOn6_4+' on>'+hourOff6_4+':'+minOff6_4+' off'+ ' (' + tcycle_6_4 + 'h)')
        
    if light6_4=='0' and dark6_4=='1':
        box6pha4text.set('                                ')
        
        box6pha4text.set(year6_4+'/'+month6_4+'/'+date6_4+' '+hourFrom6_4+':'+minuteFrom6_4+' | '+'DD'+ ' (' + tcycle_6_4 + 'h)')
        
    if light6_4=='1' and dark6_4=='0':
        box6pha4text.set('                                 ')
        
        box6pha4text.set(year6_4+'/'+month6_4+'/'+date6_4+' '+hourFrom6_4+':'+minuteFrom6_4+' | '+'LL'+ ' (' + tcycle_6_4 + 'h)')
    

    # 5 Phase
    
    if light1_5=='0' and dark1_5=='0':
        box1pha5text.set('                                ')
        
        box1pha5text.set(year1_5+'/'+month1_5+'/'+date1_5+' '+hourFrom2_5+':'+minuteFrom1_5+' | '+hourOn1_5+':'+minOn1_5+' on>'+hourOff1_5+':'+minOff1_5+' off'+ ' (' + tcycle_1_5 + 'h)')
        
    if light1_5=='0' and dark1_5=='1':
        box1pha5text.set('                                ')
        
        box1pha5text.set(year1_5+'/'+month1_5+'/'+date1_5+' '+hourFrom2_5+':'+minuteFrom1_5+' | '+'DD'+ ' (' + tcycle_1_5 + 'h)')
        
    if light1_5=='1' and dark1_5=='0':
        box1pha5text.set('                                 ')
        
        box1pha5text.set(year1_5+'/'+month1_5+'/'+date1_5+' '+hourFrom2_5+':'+minuteFrom1_5+' | '+'LL'+ ' (' + tcycle_1_5 + 'h)')
        

    if light2_5=='0' and dark2_5=='0':
        box2pha5text.set('                                ')
        
        box2pha5text.set(year2_5+'/'+month2_5+'/'+date2_5+' '+hourFrom2_5+':'+minuteFrom2_5+' | '+hourOn2_5+':'+minOn2_5+' on>'+hourOff2_5+':'+minOff2_5+' off'+ ' (' + tcycle_2_5 + 'h)')
        
    if light2_5=='0' and dark2_5=='1':
        box2pha5text.set('                                ')
        
        box2pha5text.set(year2_5+'/'+month2_5+'/'+date2_5+' '+hourFrom2_5+':'+minuteFrom2_5+' | '+'DD'+ ' (' + tcycle_2_5 + 'h)')
        
    if light2_5=='1' and dark2_5=='0':
        box2pha5text.set('                                 ')
        
        box2pha5text.set(year2_5+'/'+month2_5+'/'+date2_5+' '+hourFrom2_5+':'+minuteFrom2_5+' | '+'LL'+ ' (' + tcycle_2_5 + 'h)')
        

    if light3_5=='0' and dark3_5=='0':
        box3pha5text.set('                                ')
        
        box3pha5text.set(year3_5+'/'+month3_5+'/'+date3_5+' '+hourFrom3_5+':'+minuteFrom3_5+' | '+hourOn3_5+':'+minOn3_5+' on>'+hourOff3_5+':'+minOff3_5+' off'+ ' (' + tcycle_3_5 + 'h)')
        
    if light3_5=='0' and dark3_5=='1':
        box3pha5text.set('                                ')
        
        box3pha5text.set(year3_5+'/'+month3_5+'/'+date3_5+' '+hourFrom3_5+':'+minuteFrom3_5+' | '+'DD'+ ' (' + tcycle_3_5 + 'h)')
        
    if light3_5=='1' and dark3_5=='0':
        box3pha5text.set('                                 ')
        
        box3pha5text.set(year3_5+'/'+month3_5+'/'+date3_5+' '+hourFrom3_5+':'+minuteFrom3_5+' | '+'LL'+ ' (' + tcycle_3_5 + 'h)')
        

    if light4_5=='0' and dark4_5=='0':
        box4pha5text.set('                                ')
        
        box4pha5text.set(year4_5+'/'+month4_5+'/'+date4_5+' '+hourFrom4_5+':'+minuteFrom4_5+' | '+hourOn4_5+':'+minOn4_5+' on>'+hourOff4_5+':'+minOff4_5+' off'+ ' (' + tcycle_4_5 + 'h)')
        
    if light4_5=='0' and dark4_5=='1':
        box4pha5text.set('                                ')
        
        box4pha5text.set(year4_5+'/'+month4_5+'/'+date4_5+' '+hourFrom4_5+':'+minuteFrom4_5+' | '+'DD'+ ' (' + tcycle_4_5 + 'h)')
        
    if light4_5=='1' and dark4_5=='0':
        box4pha5text.set('                                 ')
        
        box4pha5text.set(year4_5+'/'+month4_5+'/'+date4_5+' '+hourFrom4_5+':'+minuteFrom4_5+' | '+'LL'+ ' (' + tcycle_4_5 + 'h)')
        

    if light5_5=='0' and dark5_5=='0':
        box5pha5text.set('                                ')
        
        box5pha5text.set(year5_5+'/'+month5_5+'/'+date5_5+' '+hourFrom5_5+':'+minuteFrom5_5+' | '+hourOn5_5+':'+minOn5_5+' on>'+hourOff5_5+':'+minOff5_5+' off'+ ' (' + tcycle_5_5 + 'h)')
        
    if light5_5=='0' and dark5_5=='1':
        box5pha5text.set('                                ')
        
        box5pha5text.set(year5_5+'/'+month5_5+'/'+date5_5+' '+hourFrom5_5+':'+minuteFrom5_5+' | '+'DD'+ ' (' + tcycle_5_5 + 'h)')
        
    if light5_5=='1' and dark5_5=='0':
        box5pha5text.set('                                 ')
        
        box5pha5text.set(year5_5+'/'+month5_5+'/'+date5_5+' '+hourFrom5_5+':'+minuteFrom5_5+' | '+'LL'+ ' (' + tcycle_5_5 + 'h)')

    if light6_5=='0' and dark6_5=='0':
        box6pha5text.set('                                ')
        
        box6pha5text.set(year6_5+'/'+month6_5+'/'+date6_5+' '+hourFrom6_5+':'+minuteFrom6_5+' | '+hourOn6_5+':'+minOn6_5+' on>'+hourOff6_5+':'+minOff6_5+' off'+ ' (' + tcycle_6_5 + 'h)')
        
    if light6_5=='0' and dark6_5=='1':
        box6pha5text.set('                                ')
        
        box6pha5text.set(year6_5+'/'+month6_5+'/'+date6_5+' '+hourFrom6_5+':'+minuteFrom6_5+' | '+'DD'+ ' (' + tcycle_6_5 + 'h)')
        
    if light6_5=='1' and dark6_5=='0':
        box6pha5text.set('                                 ')
        
        box6pha5text.set(year6_5+'/'+month6_5+'/'+date6_5+' '+hourFrom6_5+':'+minuteFrom6_5+' | '+'LL'+ ' (' + tcycle_6_5 + 'h)')
        

    #6 Phase
    if light1_6=='0' and dark1_6=='0':
        box1pha6text.set('                                ')
        
        box1pha6text.set(year1_6+'/'+month1_6+'/'+date1_6+' '+hourFrom2_6+':'+minuteFrom1_6+' | '+hourOn1_6+':'+minOn1_6+' on>'+hourOff1_6+':'+minOff1_6+' off'+ ' (' + tcycle_1_6 + 'h)')
        
    if light1_6=='0' and dark1_6=='1':
        box1pha6text.set('                                ')
        
        box1pha6text.set(year1_6+'/'+month1_6+'/'+date1_6+' '+hourFrom2_6+':'+minuteFrom1_6+' | '+'DD'+ ' (' + tcycle_1_6 + 'h)')
        
    if light1_6=='1' and dark1_6=='0':
        box1pha6text.set('                                 ')
        
        box1pha6text.set(year1_6+'/'+month1_6+'/'+date1_6+' '+hourFrom2_6+':'+minuteFrom1_6+' | '+'LL'+ ' (' + tcycle_1_6 + 'h)')
        

    if light2_6=='0' and dark2_6=='0':
        box2pha6text.set('                                ')
        
        box2pha6text.set(year2_6+'/'+month2_6+'/'+date2_6+' '+hourFrom2_6+':'+minuteFrom2_6+' | '+hourOn2_6+':'+minOn2_6+' on>'+hourOff2_6+':'+minOff2_6+' off'+ ' (' + tcycle_2_6 + 'h)')
        
    if light2_6=='0' and dark2_6=='1':
        box2pha6text.set('                                ')
        
        box2pha6text.set(year2_6+'/'+month2_6+'/'+date2_6+' '+hourFrom2_6+':'+minuteFrom2_6+' | '+'DD'+ ' (' + tcycle_2_6 + 'h)')
        
    if light2_6=='1' and dark2_6=='0':
        box2pha6text.set('                                 ')
        
        box2pha6text.set(year2_6+'/'+month2_6+'/'+date2_6+' '+hourFrom2_6+':'+minuteFrom2_6+' | '+'LL'+ ' (' + tcycle_2_6 + 'h)')
        

    if light3_6=='0' and dark3_6=='0':
        box3pha6text.set('                                ')
        
        box3pha6text.set(year3_6+'/'+month3_6+'/'+date3_6+' '+hourFrom3_6+':'+minuteFrom3_6+' | '+hourOn3_6+':'+minOn3_6+' on>'+hourOff3_6+':'+minOff3_6+' off'+ ' (' + tcycle_3_6 + 'h)')
        
    if light3_6=='0' and dark3_6=='1':
        box3pha6text.set('                                ')
        
        box3pha6text.set(year3_6+'/'+month3_6+'/'+date3_6+' '+hourFrom3_6+':'+minuteFrom3_6+' | '+'DD'+ ' (' + tcycle_3_6 + 'h)')
        
    if light3_6=='1' and dark3_6=='0':
        box3pha6text.set('                                 ')
        
        box3pha6text.set(year3_6+'/'+month3_6+'/'+date3_6+' '+hourFrom3_6+':'+minuteFrom3_6+' | '+'LL'+ ' (' + tcycle_3_6 + 'h)')
        

    if light4_6=='0' and dark4_6=='0':
        box4pha6text.set('                                ')
        
        box4pha6text.set(year4_6+'/'+month4_6+'/'+date4_6+' '+hourFrom4_6+':'+minuteFrom4_6+' | '+hourOn4_6+':'+minOn4_6+' on>'+hourOff4_6+':'+minOff4_6+' off'+ ' (' + tcycle_4_6 + 'h)')
        
    if light4_6=='0' and dark4_6=='1':
        box4pha6text.set('                                ')
        
        box4pha6text.set(year4_6+'/'+month4_6+'/'+date4_6+' '+hourFrom4_6+':'+minuteFrom4_6+' | '+'DD'+ ' (' + tcycle_4_6 + 'h)')
        
    if light4_6=='1' and dark4_6=='0':
        box4pha6text.set('                                 ')
        
        box4pha6text.set(year4_6+'/'+month4_6+'/'+date4_6+' '+hourFrom4_6+':'+minuteFrom4_6+' | '+'LL'+ ' (' + tcycle_4_6 + 'h)')
        

    if light5_6=='0' and dark5_6=='0':
        box5pha6text.set('                                ')
        
        box5pha6text.set(year5_6+'/'+month5_6+'/'+date5_6+' '+hourFrom5_6+':'+minuteFrom5_6+' | '+hourOn5_6+':'+minOn5_6+' on>'+hourOff5_6+':'+minOff5_6+' off'+ ' (' + tcycle_5_6 + 'h)')
        
    if light5_6=='0' and dark5_6=='1':
        box5pha6text.set('                                ')
        
        box5pha6text.set(year5_6+'/'+month5_6+'/'+date5_6+' '+hourFrom5_6+':'+minuteFrom5_6+' | '+'DD'+ ' (' + tcycle_5_6 + 'h)')
        
    if light5_6=='1' and dark5_6=='0':
        box5pha6text.set('                                 ')
        
        box5pha6text.set(year5_6+'/'+month5_6+'/'+date5_6+' '+hourFrom5_6+':'+minuteFrom5_6+' | '+'LL'+ ' (' + tcycle_5_6 + 'h)')
        
    if light6_6=='0' and dark6_6=='0':
        box6pha6text.set('                                ')
        
        box6pha6text.set(year6_6+'/'+month6_6+'/'+date6_6+' '+hourFrom6_6+':'+minuteFrom6_6+' | '+hourOn6_6+':'+minOn6_6+' on>'+hourOff6_6+':'+minOff6_6+' off'+ ' (' + tcycle_6_6 + 'h)')
        
    if light6_6=='0' and dark6_6=='1':
        box6pha6text.set('                                ')
        
        box6pha6text.set(year6_6+'/'+month6_6+'/'+date6_6+' '+hourFrom6_6+':'+minuteFrom6_6+' | '+'DD'+ ' (' + tcycle_6_6 + 'h)')
        
    if light6_6=='1' and dark6_6=='0':
        box6pha6text.set('                                 ')
        
        box6pha6text.set(year6_6+'/'+month6_6+'/'+date6_6+' '+hourFrom6_6+':'+minuteFrom6_6+' | '+'LL'+ ' (' + tcycle_6_6 + 'h)')

    #7 Phase
    if light1_7=='0' and dark1_7=='0':
        box1pha7text.set('                                ')
        
        box1pha7text.set(year1_7+'/'+month1_7+'/'+date1_7+' '+hourFrom2_7+':'+minuteFrom1_7+' | '+hourOn1_7+':'+minOn1_7+' on>'+hourOff1_7+':'+minOff1_7+' off'+ ' (' + tcycle_1_7 + 'h)')
        
    if light1_7=='0' and dark1_7=='1':
        box1pha7text.set('                                ')
        
        box1pha7text.set(year1_7+'/'+month1_7+'/'+date1_7+' '+hourFrom2_7+':'+minuteFrom1_7+' | '+'DD'+ ' (' + tcycle_1_7 + 'h)')
        
    if light1_7=='1' and dark1_7=='0':
        box1pha7text.set('                                 ')
        
        box1pha7text.set(year1_7+'/'+month1_7+'/'+date1_7+' '+hourFrom2_7+':'+minuteFrom1_7+' | '+'LL'+ ' (' + tcycle_1_7 + 'h)')
        
    
    if light2_7=='0' and dark2_7=='0':
        box2pha7text.set('                                ')
        
        box2pha7text.set(year2_7+'/'+month2_7+'/'+date2_7+' '+hourFrom2_7+':'+minuteFrom2_7+' | '+hourOn2_7+':'+minOn2_7+' on>'+hourOff2_7+':'+minOff2_7+' off'+ ' (' + tcycle_2_7 + 'h)')
        
    if light2_7=='0' and dark2_7=='1':
        box2pha7text.set('                                ')
        
        box2pha7text.set(year2_7+'/'+month2_7+'/'+date2_7+' '+hourFrom2_7+':'+minuteFrom2_7+' | '+'DD'+ ' (' + tcycle_2_7 + 'h)')
        
    if light2_7=='1' and dark2_7=='0':
        box2pha7text.set('                                 ')
        
        box2pha7text.set(year2_7+'/'+month2_7+'/'+date2_7+' '+hourFrom2_7+':'+minuteFrom2_7+' | '+'LL'+ ' (' + tcycle_2_7 + 'h)')
        
    
    if light3_7=='0' and dark3_7=='0':
        box3pha7text.set('                                ')
        
        box3pha7text.set(year3_7+'/'+month3_7+'/'+date3_7+' '+hourFrom3_7+':'+minuteFrom3_7+' | '+hourOn3_7+':'+minOn3_6+' on>'+hourOff3_7+':'+minOff3_7+' off'+ ' (' + tcycle_3_7 + 'h)')
         
    if light3_7=='0' and dark3_7=='1':
        box3pha7text.set('                                ')
        
        box3pha7text.set(year3_7+'/'+month3_7+'/'+date3_7+' '+hourFrom3_7+':'+minuteFrom3_7+' | '+'DD'+ ' (' + tcycle_3_7 + 'h)')
        
    if light3_7=='1' and dark3_7=='0':
        box3pha7text.set('                                 ')
        
        box3pha7text.set(year3_7+'/'+month3_7+'/'+date3_7+' '+hourFrom3_7+':'+minuteFrom3_7+' | '+'LL'+ ' (' + tcycle_3_7 + 'h)')
        
    
    if light4_7=='0' and dark4_7=='0':
        box4pha7text.set('                                ')
        
        box4pha7text.set(year4_7+'/'+month4_7+'/'+date4_7+' '+hourFrom4_7+':'+minuteFrom4_7+' | '+hourOn4_7+':'+minOn4_7+' on>'+hourOff4_7+':'+minOff4_7+' off'+ ' (' + tcycle_4_7 + 'h)')
        
    if light4_7=='0' and dark4_7=='1':
        box4pha7text.set('                                ')
        
        box4pha7text.set(year4_7+'/'+month4_7+'/'+date4_7+' '+hourFrom4_7+':'+minuteFrom4_7+' | '+'DD'+ ' (' + tcycle_4_7 + 'h)')
        
    if light4_7=='1' and dark4_7=='0':
        box4pha7text.set('                                 ')
        
        box4pha7text.set(year4_7+'/'+month4_7+'/'+date4_7+' '+hourFrom4_7+':'+minuteFrom4_7+' | '+'LL'+ ' (' + tcycle_4_7 + 'h)')
        
    
    if light5_7=='0' and dark5_7=='0':
        box5pha7text.set('                                ')
        
        box5pha7text.set(year5_7+'/'+month5_7+'/'+date5_7+' '+hourFrom5_7+':'+minuteFrom5_7+' | '+hourOn5_7+':'+minOn5_7+' on>'+hourOff5_7+':'+minOff5_7+' off'+ ' (' + tcycle_5_7 + 'h)')
        
    if light5_7=='0' and dark5_7=='1':
        box5pha7text.set('                                ')
        
        box5pha7text.set(year5_7+'/'+month5_7+'/'+date5_7+' '+hourFrom5_7+':'+minuteFrom5_7+' | '+'DD'+ ' (' + tcycle_5_7 + 'h)')
        
    if light5_7=='1' and dark5_7=='0':
        box5pha7text.set('                                 ')
        
        box5pha7text.set(year5_7+'/'+month5_7+'/'+date5_7+' '+hourFrom5_7+':'+minuteFrom5_7+' | '+'LL'+ ' (' + tcycle_5_7 + 'h)')
           
    if light6_7=='0' and dark6_7=='0':
        box6pha7text.set('                                ')
        
        box6pha7text.set(year6_7+'/'+month6_7+'/'+date6_7+' '+hourFrom6_7+':'+minuteFrom6_7+' | '+hourOn6_7+':'+minOn6_7+' on>'+hourOff6_7+':'+minOff6_7+' off'+ ' (' + tcycle_6_7 + 'h)')
        
    if light6_7=='0' and dark6_7=='1':
        box6pha7text.set('                                ')
        
        box6pha7text.set(year6_7+'/'+month6_7+'/'+date6_7+' '+hourFrom6_7+':'+minuteFrom6_7+' | '+'DD'+ ' (' + tcycle_6_7 + 'h)')
        
    if light6_7=='1' and dark6_7=='0':
        box6pha7text.set('                                 ')
        
        box6pha7text.set(year6_7+'/'+month6_7+'/'+date6_7+' '+hourFrom6_7+':'+minuteFrom6_7+' | '+'LL'+ ' (' + tcycle_6_7 + 'h)')

    #8 Phase
    if light1_8=='0' and dark1_8=='0':
        box1pha8text.set('                                ')
        
        box1pha8text.set(year1_8+'/'+month1_8+'/'+date1_8+' '+hourFrom2_8+':'+minuteFrom1_8+' | '+hourOn1_8+':'+minOn1_8+' on>'+hourOff1_8+':'+minOff1_8+' off'+ ' (' + tcycle_1_8 + 'h)')
        
    if light1_8=='0' and dark1_8=='1':
        box1pha8text.set('                                ')
        
        box1pha8text.set(year1_8+'/'+month1_8+'/'+date1_8+' '+hourFrom2_8+':'+minuteFrom1_8+' | '+'DD'+ ' (' + tcycle_1_8 + 'h)')
        
    if light1_8=='1' and dark1_8=='0':
        box1pha8text.set('                                 ')
        
        box1pha8text.set(year1_8+'/'+month1_8+'/'+date1_8+' '+hourFrom2_8+':'+minuteFrom1_8+' | '+'LL'+ ' (' + tcycle_1_8 + 'h)')
        
    
    if light2_8=='0' and dark2_8=='0':
        box2pha8text.set('                                ')
        
        box2pha8text.set(year2_8+'/'+month2_8+'/'+date2_8+' '+hourFrom2_8+':'+minuteFrom2_8+' | '+hourOn2_8+':'+minOn2_8+' on>'+hourOff2_8+':'+minOff2_8+' off'+ ' (' + tcycle_2_8 + 'h)')
        
    if light2_8=='0' and dark2_8=='1':
        box2pha8text.set('                                ')
        
        box2pha8text.set(year2_8+'/'+month2_8+'/'+date2_8+' '+hourFrom2_8+':'+minuteFrom2_8+' | '+'DD'+ ' (' + tcycle_2_8 + 'h)')
        
    if light2_8=='1' and dark2_8=='0':
        box2pha8text.set('                                 ')
        
        box2pha8text.set(year2_8+'/'+month2_8+'/'+date2_8+' '+hourFrom2_8+':'+minuteFrom2_8+' | '+'LL'+ ' (' + tcycle_2_8 + 'h)')
        
    
    if light3_8=='0' and dark3_8=='0':
        box3pha8text.set('                                ')
        
        box3pha8text.set(year3_8+'/'+month3_8+'/'+date3_8+' '+hourFrom3_8+':'+minuteFrom3_8+' | '+hourOn3_8+':'+minOn3_6+' on>'+hourOff3_8+':'+minOff3_8+' off'+ ' (' + tcycle_3_8 + 'h)')
         
    if light3_8=='0' and dark3_8=='1':
        box3pha8text.set('                                ')
        
        box3pha8text.set(year3_8+'/'+month3_8+'/'+date3_8+' '+hourFrom3_8+':'+minuteFrom3_8+' | '+'DD'+ ' (' + tcycle_3_8 + 'h)')
        
    if light3_8=='1' and dark3_8=='0':
        box3pha8text.set('                                 ')
        
        box3pha8text.set(year3_8+'/'+month3_8+'/'+date3_8+' '+hourFrom3_8+':'+minuteFrom3_8+' | '+'LL'+ ' (' + tcycle_3_8 + 'h)')
        
    
    if light4_8=='0' and dark4_8=='0':
        box4pha8text.set('                                ')
        
        box4pha8text.set(year4_8+'/'+month4_8+'/'+date4_8+' '+hourFrom4_8+':'+minuteFrom4_8+' | '+hourOn4_8+':'+minOn4_8+' on>'+hourOff4_8+':'+minOff4_8+' off'+ ' (' + tcycle_4_8 + 'h)')
        
    if light4_8=='0' and dark4_8=='1':
        box4pha8text.set('                                ')
        
        box4pha8text.set(year4_8+'/'+month4_8+'/'+date4_8+' '+hourFrom4_8+':'+minuteFrom4_8+' | '+'DD'+ ' (' + tcycle_4_8 + 'h)')
        
    if light4_8=='1' and dark4_8=='0':
        box4pha8text.set('                                 ')
        
        box4pha8text.set(year4_8+'/'+month4_8+'/'+date4_8+' '+hourFrom4_8+':'+minuteFrom4_8+' | '+'LL'+ ' (' + tcycle_4_8 + 'h)')
        
    
    if light5_8=='0' and dark5_8=='0':
        box5pha8text.set('                                ')
        
        box5pha8text.set(year5_8+'/'+month5_8+'/'+date5_8+' '+hourFrom5_8+':'+minuteFrom5_8+' | '+hourOn5_8+':'+minOn5_8+' on>'+hourOff5_8+':'+minOff5_8+' off'+ ' (' + tcycle_5_8 + 'h)')
        
    if light5_8=='0' and dark5_8=='1':
        box5pha8text.set('                                ')
        
        box5pha8text.set(year5_8+'/'+month5_8+'/'+date5_8+' '+hourFrom5_8+':'+minuteFrom5_8+' | '+'DD'+ ' (' + tcycle_5_8 + 'h)')
        
    if light5_8=='1' and dark5_8=='0':
        box5pha8text.set('                                 ')
        
        box5pha8text.set(year5_8+'/'+month5_8+'/'+date5_8+' '+hourFrom5_8+':'+minuteFrom5_8+' | '+'LL'+ ' (' + tcycle_5_8 + 'h)')

    if light6_8=='0' and dark6_8=='0':
        box6pha8text.set('                                ')
        
        box6pha8text.set(year6_8+'/'+month6_8+'/'+date6_8+' '+hourFrom6_8+':'+minuteFrom6_8+' | '+hourOn6_8+':'+minOn6_8+' on>'+hourOff6_8+':'+minOff6_8+' off'+ ' (' + tcycle_6_8 + 'h)')
        
    if light6_8=='0' and dark6_8=='1':
        box6pha8text.set('                                ')
        
        box6pha8text.set(year6_8+'/'+month6_8+'/'+date6_8+' '+hourFrom6_8+':'+minuteFrom6_8+' | '+'DD'+ ' (' + tcycle_6_8 + 'h)')
        
    if light6_8=='1' and dark6_8=='0':
        box6pha8text.set('                                 ')
        
        box6pha8text.set(year6_8+'/'+month6_8+'/'+date6_8+' '+hourFrom6_8+':'+minuteFrom6_8+' | '+'LL'+ ' (' + tcycle_6_8 + 'h)')        
      
    #9 Phase
    if light1_9=='0' and dark1_9=='0':
        box1pha9text.set('                                ')
        
        box1pha9text.set(year1_9+'/'+month1_9+'/'+date1_9+' '+hourFrom2_9+':'+minuteFrom1_9+' | '+hourOn1_9+':'+minOn1_9+' on>'+hourOff1_9+':'+minOff1_9+' off'+ ' (' + tcycle_1_9 + 'h)')
        
    if light1_9=='0' and dark1_9=='1':
        box1pha9text.set('                                ')
        
        box1pha9text.set(year1_9+'/'+month1_9+'/'+date1_9+' '+hourFrom2_9+':'+minuteFrom1_9+' | '+'DD'+ ' (' + tcycle_1_9 + 'h)')
        
    if light1_9=='1' and dark1_9=='0':
        box1pha9text.set('                                 ')
        
        box1pha9text.set(year1_9+'/'+month1_9+'/'+date1_9+' '+hourFrom2_9+':'+minuteFrom1_9+' | '+'LL'+ ' (' + tcycle_1_9 + 'h)')
        
    
    if light2_9=='0' and dark2_9=='0':
        box2pha9text.set('                                ')
        
        box2pha9text.set(year2_9+'/'+month2_9+'/'+date2_9+' '+hourFrom2_9+':'+minuteFrom2_9+' | '+hourOn2_9+':'+minOn2_9+' on>'+hourOff2_9+':'+minOff2_9+' off'+ ' (' + tcycle_2_9 + 'h)')
        
    if light2_9=='0' and dark2_9=='1':
        box2pha9text.set('                                ')
        
        box2pha9text.set(year2_9+'/'+month2_9+'/'+date2_9+' '+hourFrom2_9+':'+minuteFrom2_9+' | '+'DD'+ ' (' + tcycle_2_9 + 'h)')
        
    if light2_9=='1' and dark2_9=='0':
        box2pha9text.set('                                 ')
        
        box2pha9text.set(year2_9+'/'+month2_9+'/'+date2_9+' '+hourFrom2_9+':'+minuteFrom2_9+' | '+'LL'+ ' (' + tcycle_2_9 + 'h)')
        
    
    if light3_9=='0' and dark3_9=='0':
        box3pha9text.set('                                ')
        
        box3pha9text.set(year3_9+'/'+month3_9+'/'+date3_9+' '+hourFrom3_9+':'+minuteFrom3_9+' | '+hourOn3_9+':'+minOn3_6+' on>'+hourOff3_9+':'+minOff3_9+' off'+ ' (' + tcycle_3_9 + 'h)')
         
    if light3_9=='0' and dark3_9=='1':
        box3pha9text.set('                                ')
        
        box3pha9text.set(year3_9+'/'+month3_9+'/'+date3_9+' '+hourFrom3_9+':'+minuteFrom3_9+' | '+'DD'+ ' (' + tcycle_3_9 + 'h)')
        
    if light3_9=='1' and dark3_9=='0':
        box3pha9text.set('                                 ')
        
        box3pha9text.set(year3_9+'/'+month3_9+'/'+date3_9+' '+hourFrom3_9+':'+minuteFrom3_9+' | '+'LL'+ ' (' + tcycle_3_9 + 'h)')
        
    
    if light4_9=='0' and dark4_9=='0':
        box4pha9text.set('                                ')
        
        box4pha9text.set(year4_9+'/'+month4_9+'/'+date4_9+' '+hourFrom4_9+':'+minuteFrom4_9+' | '+hourOn4_9+':'+minOn4_9+' on>'+hourOff4_9+':'+minOff4_9+' off'+ ' (' + tcycle_4_9 + 'h)')
        
    if light4_9=='0' and dark4_9=='1':
        box4pha9text.set('                                ')
        
        box4pha9text.set(year4_9+'/'+month4_9+'/'+date4_9+' '+hourFrom4_9+':'+minuteFrom4_9+' | '+'DD'+ ' (' + tcycle_4_9 + 'h)')
        
    if light4_9=='1' and dark4_9=='0':
        box4pha9text.set('                                 ')
        
        box4pha9text.set(year4_9+'/'+month4_9+'/'+date4_9+' '+hourFrom4_9+':'+minuteFrom4_9+' | '+'LL'+ ' (' + tcycle_4_9 + 'h)')
        
    
    if light5_9=='0' and dark5_9=='0':
        box5pha9text.set('                                ')
        
        box5pha9text.set(year5_9+'/'+month5_9+'/'+date5_9+' '+hourFrom5_9+':'+minuteFrom5_9+' | '+hourOn5_9+':'+minOn5_9+' on>'+hourOff5_9+':'+minOff5_9+' off'+ ' (' + tcycle_5_9 + 'h)')
        
    if light5_9=='0' and dark5_9=='1':
        box5pha9text.set('                                ')
        
        box5pha9text.set(year5_9+'/'+month5_9+'/'+date5_9+' '+hourFrom5_9+':'+minuteFrom5_9+' | '+'DD'+ ' (' + tcycle_5_9 + 'h)')
        
    if light5_9=='1' and dark5_9=='0':
        box5pha9text.set('                                 ')
        
        box5pha9text.set(year5_9+'/'+month5_9+'/'+date5_9+' '+hourFrom5_9+':'+minuteFrom5_9+' | '+'LL'+ ' (' + tcycle_5_9 + 'h)')
           
    if light6_9=='0' and dark6_9=='0':
        box6pha9text.set('                                ')
        
        box6pha9text.set(year6_9+'/'+month6_9+'/'+date6_9+' '+hourFrom6_9+':'+minuteFrom6_9+' | '+hourOn6_9+':'+minOn6_9+' on>'+hourOff6_9+':'+minOff6_9+' off'+ ' (' + tcycle_6_9 + 'h)')
        
    if light6_9=='0' and dark6_9=='1':
        box6pha9text.set('                                ')
        
        box6pha9text.set(year6_9+'/'+month6_9+'/'+date6_9+' '+hourFrom6_9+':'+minuteFrom6_9+' | '+'DD'+ ' (' + tcycle_6_9 + 'h)')
        
    if light6_9=='1' and dark6_9=='0':
        box6pha9text.set('                                 ')
        
        box6pha9text.set(year6_9+'/'+month6_9+'/'+date6_9+' '+hourFrom6_9+':'+minuteFrom6_9+' | '+'LL'+ ' (' + tcycle_6_9 + 'h)')

    #10 Phase
    if light1_10=='0' and dark1_10=='0':
        box1pha10text.set('                                ')
        
        box1pha10text.set(year1_10+'/'+month1_10+'/'+date1_10+' '+hourFrom2_10+':'+minuteFrom1_10+' | '+hourOn1_10+':'+minOn1_10+' on>'+hourOff1_10+':'+minOff1_10+' off'+ ' (' + tcycle_1_10 + 'h)')
        
    if light1_10=='0' and dark1_10=='1':
        box1pha10text.set('                                ')
        
        box1pha10text.set(year1_10+'/'+month1_10+'/'+date1_10+' '+hourFrom2_10+':'+minuteFrom1_10+' | '+'DD'+ ' (' + tcycle_1_10 + 'h)')
        
    if light1_10=='1' and dark1_10=='0':
        box1pha10text.set('                                 ')
        
        box1pha10text.set(year1_10+'/'+month1_10+'/'+date1_10+' '+hourFrom2_10+':'+minuteFrom1_10+' | '+'LL'+ ' (' + tcycle_1_10 + 'h)')
        
    
    if light2_10=='0' and dark2_10=='0':
        box2pha10text.set('                                ')
        
        box2pha10text.set(year2_10+'/'+month2_10+'/'+date2_10+' '+hourFrom2_10+':'+minuteFrom2_10+' | '+hourOn2_10+':'+minOn2_10+' on>'+hourOff2_10+':'+minOff2_10+' off'+ ' (' + tcycle_2_10 + 'h)')
        
    if light2_10=='0' and dark2_10=='1':
        box2pha10text.set('                                ')
        
        box2pha10text.set(year2_10+'/'+month2_10+'/'+date2_10+' '+hourFrom2_10+':'+minuteFrom2_10+' | '+'DD'+ ' (' + tcycle_2_10 + 'h)')
        
    if light2_10=='1' and dark2_10=='0':
        box2pha10text.set('                                 ')
        
        box2pha10text.set(year2_10+'/'+month2_10+'/'+date2_10+' '+hourFrom2_10+':'+minuteFrom2_10+' | '+'LL'+ ' (' + tcycle_2_10 + 'h)')
        
    
    if light3_10=='0' and dark3_10=='0':
        box3pha10text.set('                                ')
        
        box3pha10text.set(year3_10+'/'+month3_10+'/'+date3_10+' '+hourFrom3_10+':'+minuteFrom3_10+' | '+hourOn3_10+':'+minOn3_6+' on>'+hourOff3_10+':'+minOff3_10+' off'+ ' (' + tcycle_3_10 + 'h)')
         
    if light3_10=='0' and dark3_10=='1':
        box3pha10text.set('                                ')
        
        box3pha10text.set(year3_10+'/'+month3_10+'/'+date3_10+' '+hourFrom3_10+':'+minuteFrom3_10+' | '+'DD'+ ' (' + tcycle_3_10 + 'h)')
        
    if light3_10=='1' and dark3_10=='0':
        box3pha10text.set('                                 ')
        
        box3pha10text.set(year3_10+'/'+month3_10+'/'+date3_10+' '+hourFrom3_10+':'+minuteFrom3_10+' | '+'LL'+ ' (' + tcycle_3_10 + 'h)')
        
    
    if light4_10=='0' and dark4_10=='0':
        box4pha10text.set('                                ')
        
        box4pha10text.set(year4_10+'/'+month4_10+'/'+date4_10+' '+hourFrom4_10+':'+minuteFrom4_10+' | '+hourOn4_10+':'+minOn4_10+' on>'+hourOff4_10+':'+minOff4_10+' off'+ ' (' + tcycle_4_10 + 'h)')
        
    if light4_10=='0' and dark4_10=='1':
        box4pha10text.set('                                ')
        
        box4pha10text.set(year4_10+'/'+month4_10+'/'+date4_10+' '+hourFrom4_10+':'+minuteFrom4_10+' | '+'DD'+ ' (' + tcycle_4_10 + 'h)')
        
    if light4_10=='1' and dark4_10=='0':
        box4pha10text.set('                                 ')
        
        box4pha10text.set(year4_10+'/'+month4_10+'/'+date4_10+' '+hourFrom4_10+':'+minuteFrom4_10+' | '+'LL'+ ' (' + tcycle_4_10 + 'h)')
        
    
    if light5_10=='0' and dark5_10=='0':
        box5pha10text.set('                                ')
        
        box5pha10text.set(year5_10+'/'+month5_10+'/'+date5_10+' '+hourFrom5_10+':'+minuteFrom5_10+' | '+hourOn5_10+':'+minOn5_10+' on>'+hourOff5_10+':'+minOff5_10+' off'+ ' (' + tcycle_5_10 + 'h)')
        
    if light5_10=='0' and dark5_10=='1':
        box5pha10text.set('                                ')
        
        box5pha10text.set(year5_10+'/'+month5_10+'/'+date5_10+' '+hourFrom5_10+':'+minuteFrom5_10+' | '+'DD'+ ' (' + tcycle_5_10 + 'h)')
        
    if light5_10=='1' and dark5_10=='0':
        box5pha10text.set('                                 ')
        
        box5pha10text.set(year5_10+'/'+month5_10+'/'+date5_10+' '+hourFrom5_10+':'+minuteFrom5_10+' | '+'LL'+ ' (' + tcycle_5_10 + 'h)')

    if light6_10=='0' and dark6_10=='0':
        box6pha10text.set('                                ')
        
        box6pha10text.set(year6_10+'/'+month6_10+'/'+date6_10+' '+hourFrom6_10+':'+minuteFrom6_10+' | '+hourOn6_10+':'+minOn6_10+' on>'+hourOff6_10+':'+minOff6_10+' off'+ ' (' + tcycle_6_10 + 'h)')
        
    if light6_10=='0' and dark6_10=='1':
        box6pha10text.set('                                ')
        
        box6pha10text.set(year6_10+'/'+month6_10+'/'+date6_10+' '+hourFrom6_10+':'+minuteFrom6_10+' | '+'DD'+ ' (' + tcycle_6_10 + 'h)')
        
    if light6_10=='1' and dark6_10=='0':
        box6pha10text.set('                                 ')
        
        box6pha10text.set(year6_10+'/'+month6_10+'/'+date6_10+' '+hourFrom6_10+':'+minuteFrom6_10+' | '+'LL'+ ' (' + tcycle_6_10 + 'h)')
          

    #11 Phase
    if light1_11=='0' and dark1_11=='0':
        box1pha11text.set('                                ')
        
        box1pha11text.set(year1_11+'/'+month1_11+'/'+date1_11+' '+hourFrom2_11+':'+minuteFrom1_11+' | '+hourOn1_11+':'+minOn1_11+' on>'+hourOff1_11+':'+minOff1_11+' off'+ ' (' + tcycle_1_11 + 'h)')
        
    if light1_11=='0' and dark1_11=='1':
        box1pha11text.set('                                ')
        
        box1pha11text.set(year1_11+'/'+month1_11+'/'+date1_11+' '+hourFrom2_11+':'+minuteFrom1_11+' | '+'DD'+ ' (' + tcycle_1_11 + 'h)')
        
    if light1_11=='1' and dark1_11=='0':
        box1pha11text.set('                                 ')
        
        box1pha11text.set(year1_11+'/'+month1_11+'/'+date1_11+' '+hourFrom2_11+':'+minuteFrom1_11+' | '+'LL'+ ' (' + tcycle_1_11 + 'h)')
        
    
    if light2_11=='0' and dark2_11=='0':
        box2pha11text.set('                                ')
        
        box2pha11text.set(year2_11+'/'+month2_11+'/'+date2_11+' '+hourFrom2_11+':'+minuteFrom2_11+' | '+hourOn2_11+':'+minOn2_11+' on>'+hourOff2_11+':'+minOff2_11+' off'+ ' (' + tcycle_2_11 + 'h)')
        
    if light2_11=='0' and dark2_11=='1':
        box2pha11text.set('                                ')
        
        box2pha11text.set(year2_11+'/'+month2_11+'/'+date2_11+' '+hourFrom2_11+':'+minuteFrom2_11+' | '+'DD'+ ' (' + tcycle_2_11 + 'h)'+ ' (' + tcycle_2_11 + 'h)')
        
    if light2_11=='1' and dark2_11=='0':
        box2pha11text.set('                                 ')
        
        box2pha11text.set(year2_11+'/'+month2_11+'/'+date2_11+' '+hourFrom2_11+':'+minuteFrom2_11+' | '+'LL'+ ' (' + tcycle_2_11 + 'h)'+ ' (' + tcycle_2_11 + 'h)')
        
    
    if light3_11=='0' and dark3_11=='0':
        box3pha11text.set('                                ')
        
        box3pha11text.set(year3_11+'/'+month3_11+'/'+date3_11+' '+hourFrom3_11+':'+minuteFrom3_11+' | '+hourOn3_11+':'+minOn3_6+' on>'+hourOff3_11+':'+minOff3_11+' off'+ ' (' + tcycle_3_11 + 'h)')
         
    if light3_11=='0' and dark3_11=='1':
        box3pha11text.set('                                ')
        
        box3pha11text.set(year3_11+'/'+month3_11+'/'+date3_11+' '+hourFrom3_11+':'+minuteFrom3_11+' | '+'DD'+ ' (' + tcycle_3_11 + 'h)'+ ' (' + tcycle_3_11 + 'h)')
        
    if light3_11=='1' and dark3_11=='0':
        box3pha11text.set('                                 ')
        
        box3pha11text.set(year3_11+'/'+month3_11+'/'+date3_11+' '+hourFrom3_11+':'+minuteFrom3_11+' | '+'LL'+ ' (' + tcycle_3_11 + 'h)'+ ' (' + tcycle_3_11 + 'h)')
        
    
    if light4_11=='0' and dark4_11=='0':
        box4pha11text.set('                                ')
        
        box4pha11text.set(year4_11+'/'+month4_11+'/'+date4_11+' '+hourFrom4_11+':'+minuteFrom4_11+' | '+hourOn4_11+':'+minOn4_11+' on>'+hourOff4_11+':'+minOff4_11+' off'+ ' (' + tcycle_4_11 + 'h)')
        
    if light4_11=='0' and dark4_11=='1':
        box4pha11text.set('                                ')
        
        box4pha11text.set(year4_11+'/'+month4_11+'/'+date4_11+' '+hourFrom4_11+':'+minuteFrom4_11+' | '+'DD'+ ' (' + tcycle_4_11 + 'h)')
        
    if light4_11=='1' and dark4_11=='0':
        box4pha11text.set('                                 ')
        
        box4pha11text.set(year4_11+'/'+month4_11+'/'+date4_11+' '+hourFrom4_11+':'+minuteFrom4_11+' | '+'LL'+ ' (' + tcycle_4_11 + 'h)')
        
    
    if light5_11=='0' and dark5_11=='0':
        box5pha11text.set('                                ')
        
        box5pha11text.set(year5_11+'/'+month5_11+'/'+date5_11+' '+hourFrom5_11+':'+minuteFrom5_11+' | '+hourOn5_11+':'+minOn5_11+' on>'+hourOff5_11+':'+minOff5_11+' off'+ ' (' + tcycle_5_11 + 'h)')
        
    if light5_11=='0' and dark5_11=='1':
        box5pha11text.set('                                ')
        
        box5pha11text.set(year5_11+'/'+month5_11+'/'+date5_11+' '+hourFrom5_11+':'+minuteFrom5_11+' | '+'DD'+ ' (' + tcycle_5_11 + 'h)')
        
    if light5_11=='1' and dark5_11=='0':
        box5pha11text.set('                                 ')
        
        box5pha11text.set(year5_11+'/'+month5_11+'/'+date5_11+' '+hourFrom5_11+':'+minuteFrom5_11+' | '+'LL'+ ' (' + tcycle_5_11 + 'h)')
          
    if light6_11=='0' and dark6_11=='0':
        box6pha11text.set('                                ')
        
        box6pha11text.set(year6_11+'/'+month6_11+'/'+date6_11+' '+hourFrom6_11+':'+minuteFrom6_11+' | '+hourOn6_11+':'+minOn6_11+' on>'+hourOff6_11+':'+minOff6_11+' off'+ ' (' + tcycle_6_11 + 'h)')
        
    if light6_11=='0' and dark6_11=='1':
        box6pha11text.set('                                ')
        
        box6pha11text.set(year6_11+'/'+month6_11+'/'+date6_11+' '+hourFrom6_11+':'+minuteFrom6_11+' | '+'DD'+ ' (' + tcycle_6_11 + 'h)')
        
    if light6_11=='1' and dark6_11=='0':
        box6pha11text.set('                                 ')
        
        box6pha11text.set(year6_11+'/'+month6_11+'/'+date6_11+' '+hourFrom6_11+':'+minuteFrom6_11+' | '+'LL'+ ' (' + tcycle_6_11 + 'h)')

    #12 Phase
    if light1_12=='0' and dark1_12=='0':
        box1pha12text.set('                                ')
        
        box1pha12text.set(year1_12+'/'+month1_12+'/'+date1_12+' '+hourFrom2_12+':'+minuteFrom1_12+' | '+hourOn1_12+':'+minOn1_12+' on>'+hourOff1_12+':'+minOff1_12+' off'+ ' (' + tcycle_1_12 + 'h)')
        
    if light1_12=='0' and dark1_12=='1':
        box1pha12text.set('                                ')
        
        box1pha12text.set(year1_12+'/'+month1_12+'/'+date1_12+' '+hourFrom2_12+':'+minuteFrom1_12+' | '+'DD'+ ' (' + tcycle_1_12 + 'h)')
        
    if light1_12=='1' and dark1_12=='0':
        box1pha12text.set('                                 ')
        
        box1pha12text.set(year1_12+'/'+month1_12+'/'+date1_12+' '+hourFrom2_12+':'+minuteFrom1_12+' | '+'LL'+ ' (' + tcycle_1_12 + 'h)')
        
    
    if light2_12=='0' and dark2_12=='0':
        box2pha12text.set('                                ')
        
        box2pha12text.set(year2_12+'/'+month2_12+'/'+date2_12+' '+hourFrom2_12+':'+minuteFrom2_12+' | '+hourOn2_12+':'+minOn2_12+' on>'+hourOff2_12+':'+minOff2_12+' off'+ ' (' + tcycle_2_12 + 'h)')
        
    if light2_12=='0' and dark2_12=='1':
        box2pha12text.set('                                ')
        
        box2pha12text.set(year2_12+'/'+month2_12+'/'+date2_12+' '+hourFrom2_12+':'+minuteFrom2_12+' | '+'DD'+ ' (' + tcycle_2_12 + 'h)')
        
    if light2_12=='1' and dark2_12=='0':
        box2pha12text.set('                                 ')
        
        box2pha12text.set(year2_12+'/'+month2_12+'/'+date2_12+' '+hourFrom2_12+':'+minuteFrom2_12+' | '+'LL'+ ' (' + tcycle_2_12 + 'h)')
        
    
    if light3_12=='0' and dark3_12=='0':
        box3pha12text.set('                                ')
        
        box3pha12text.set(year3_12+'/'+month3_12+'/'+date3_12+' '+hourFrom3_12+':'+minuteFrom3_12+' | '+hourOn3_12+':'+minOn3_6+' on>'+hourOff3_12+':'+minOff3_12+' off'+ ' (' + tcycle_3_12 + 'h)')
         
    if light3_12=='0' and dark3_12=='1':
        box3pha12text.set('                                ')
        
        box3pha12text.set(year3_12+'/'+month3_12+'/'+date3_12+' '+hourFrom3_12+':'+minuteFrom3_12+' | '+'DD'+ ' (' + tcycle_3_12 + 'h)')
        
    if light3_12=='1' and dark3_12=='0':
        box3pha12text.set('                                 ')
        
        box3pha12text.set(year3_12+'/'+month3_12+'/'+date3_12+' '+hourFrom3_12+':'+minuteFrom3_12+' | '+'LL'+ ' (' + tcycle_3_12 + 'h)')
        
    
    if light4_12=='0' and dark4_12=='0':
        box4pha12text.set('                                ')
        
        box4pha12text.set(year4_12+'/'+month4_12+'/'+date4_12+' '+hourFrom4_12+':'+minuteFrom4_12+' | '+hourOn4_12+':'+minOn4_12+' on>'+hourOff4_12+':'+minOff4_12+' off'+ ' (' + tcycle_4_12 + 'h)')
        
    if light4_12=='0' and dark4_12=='1':
        box4pha12text.set('                                ')
        
        box4pha12text.set(year4_12+'/'+month4_12+'/'+date4_12+' '+hourFrom4_12+':'+minuteFrom4_12+' | '+'DD'+ ' (' + tcycle_4_12 + 'h)')
        
    if light4_12=='1' and dark4_12=='0':
        box4pha12text.set('                                 ')
        
        box4pha12text.set(year4_12+'/'+month4_12+'/'+date4_12+' '+hourFrom4_12+':'+minuteFrom4_12+' | '+'LL'+ ' (' + tcycle_4_12 + 'h)')
        
    
    if light5_12=='0' and dark5_12=='0':
        box5pha12text.set('                                ')
        
        box5pha12text.set(year5_12+'/'+month5_12+'/'+date5_12+' '+hourFrom5_12+':'+minuteFrom5_12+' | '+hourOn5_12+':'+minOn5_12+' on>'+hourOff5_12+':'+minOff5_12+' off'+ ' (' + tcycle_5_12 + 'h)')
        
    if light5_12=='0' and dark5_12=='1':
        box5pha12text.set('                                ')
        
        box5pha12text.set(year5_12+'/'+month5_12+'/'+date5_12+' '+hourFrom5_12+':'+minuteFrom5_12+' | '+'DD'+ ' (' + tcycle_5_12 + 'h)')
        
    if light5_12=='1' and dark5_12=='0':
        box5pha12text.set('                                 ')
        
        box5pha12text.set(year5_12+'/'+month5_12+'/'+date5_12+' '+hourFrom5_12+':'+minuteFrom5_12+' | '+'LL'+ ' (' + tcycle_5_12 + 'h)')
        
    if light6_12=='0' and dark6_12=='0':
        box6pha12text.set('                                ')
        
        box6pha12text.set(year6_12+'/'+month6_12+'/'+date6_12+' '+hourFrom6_12+':'+minuteFrom6_12+' | '+hourOn6_12+':'+minOn6_12+' on>'+hourOff6_12+':'+minOff6_12+' off'+ ' (' + tcycle_6_12 + 'h)')
        
    if light6_12=='0' and dark6_12=='1':
        box6pha12text.set('                                ')
        
        box6pha12text.set(year6_12+'/'+month6_12+'/'+date6_12+' '+hourFrom6_12+':'+minuteFrom6_12+' | '+'DD'+ ' (' + tcycle_6_12 + 'h)')
        
    if light6_12=='1' and dark6_12=='0':
        box6pha12text.set('                                 ')
        
        box6pha12text.set(year6_12+'/'+month6_12+'/'+date6_12+' '+hourFrom6_12+':'+minuteFrom6_12+' | '+'LL'+ ' (' + tcycle_6_12 + 'h)')

    window.update_idletasks()   

    

def connect():  # Start to connect and call get_data - Link to Start in Recording menu
    port = port_entry.get()
    baud = baud_entry.get()
    timeout = int(timeout_entry.get())
    global serial_obj   
    global dead
    dead = False
    try:
        serial_obj = create_serial_obj(port, baud, timeout=timeout)
    except NameError:
        status.pack(side='bottom', fill='x')
        status.set('Missing baud rate and port number.')
        return
    t1 = threading.Thread(target=lambda:get_data(0))
    t1.daemon = True
    # inactivate Recording Start button
    btnRun['state']='disabled'
    recordingmenu.entryconfig('Start new', state='disabled')
    show_conf()
    window.update_idletasks()
    t1.start()

def disconnect():  # close the serial_obj thread
    status.pack(side='bottom', fill='x')
    status.set('Attempting to close serial port...')
    global dead
    global serial_obj
    dead = True
    serial_obj.close()
    print(threading.active_count())
    print(threading.enumerate())
    status.pack(side='bottom', fill='x')
    status.set('Stopped recording and disconnected from the boxes.')
    window.update_idletasks()

def OnButtonClick(button_id):
    global setBox1, setBox2, setBox3, setBox4, setBox5
    if button_id == 1:
        getBox1Schedule()
        setBox1=1
    elif button_id == 2:
        getBox2Schedule()
        setBox2=1
    elif button_id == 3:
        getBox3Schedule()
        setBox3=1
    elif button_id == 4:
        getBox4Schedule()
        setBox4=1
    elif button_id == 5:
        getBox5Schedule()
        setBox5=1
    elif button_id == 6:
        getBox5Schedule()
        setBox5=1

def time_to_str(time_int):
    time_int = str(time_int)
    if len(time_int) == 1:
        return '0'+ time_int
    else:
        return time_int
                
def getBox1Schedule(): 
    global setBox1, tcyclespinbox_arr
    setBox1=1
    
    global hourOn1_1, minOn1_1, hourOff1_1, minOff1_1, dark1_1, light1_1, tcycle_1_1
    hourOn1_1=spin1_A_1.get()
    minOn1_1=spin1_B_1.get()
    hourOff1_1=spin1_C_1.get()
    minOff1_1=spin1_D_1.get()        
    tcycle_1_1 = int(tcyclespinbox_arr[0,0].get())
    
    hourOn1_1 = time_to_str(hourOn1_1)
    minOn1_1 = time_to_str(minOn1_1)
    hourOff1_1=time_to_str(hourOff1_1)
    minOff1_1=time_to_str(minOff1_1)
    
    tcycle_1_1=time_to_str(tcycle_1_1)

    if var1_1.get()==1:
        dark1_1='0'
        light1_1='0'
    if var1_1.get()==2:
        dark1_1='1'
        light1_1='0'
    if var1_1.get()==3:
        dark1_1='0'
        light1_1='1'

    #Phase2
    global date1_2, month1_2, year1_2, hourFrom1_2, minuteFrom1_2, hourOn1_2, minOn1_2, hourOff1_2, minOff1_2, dark1_2, light1_2, tcycle_1_2
    date1_2 = date1_2_entry.get()
    month1_2 = month1_2_entry.get()
    year1_2 = year1_2_entry.get()
    
    hourOn1_2=spin1_A_2.get()
    minOn1_2=spin1_B_2.get()
    hourOff1_2=spin1_C_2.get()
    minOff1_2=spin1_D_2.get()     
    hourFrom1_2= spin1_E_2.get()
    minuteFrom1_2= spin1_F_2.get()

    tcycle_1_2 = int(tcyclespinbox_arr[0,1].get())
  
    hourOn1_2 = time_to_str(hourOn1_2)    
    minOn1_2 = time_to_str(minOn1_2)
    hourOff1_2=time_to_str(hourOff1_2)
    minOff1_2=time_to_str(minOff1_2)
    
    tcycle_1_2 = time_to_str(tcycle_1_2)

    date1_2 = time_to_str(date1_2)
    month1_2 = time_to_str(month1_2)
    year1_2 = time_to_str(year1_2)

    if var1_2.get()==1:
        dark1_2='0'
        light1_2='0'
    if var1_2.get()==2:
        dark1_2='1'
        light1_2='0'
    if var1_2.get()==3:
        dark1_2='0'
        light1_2='1'

    #phase3
    
    global date1_3, month1_3, year1_3, hourFrom1_3, minuteFrom1_3, hourOn1_3, minOn1_3, hourOff1_3, minOff1_3, dark1_3, light1_3, tcycle_1_3
    date1_3 = date1_3_entry.get()
    month1_3 = month1_3_entry.get()
    year1_3 = year1_3_entry.get()
    hourFrom1_3= spin1_E_3.get()
    minuteFrom1_3= spin1_F_3.get()
    hourOn1_3=spin1_A_3.get()
    minOn1_3=spin1_B_3.get()
    hourOff1_3=spin1_C_3.get()
    minOff1_3=spin1_D_3.get()   

    tcycle_1_3 = int(tcyclespinbox_arr[0,2].get())
  
    hourOn1_3 = time_to_str(hourOn1_3)    
    minOn1_3 = time_to_str(minOn1_3)
    hourOff1_3=time_to_str(hourOff1_3)
    minOff1_3=time_to_str(minOff1_3)
    
    tcycle_1_3 = time_to_str(tcycle_1_3)
    
    date1_3 = time_to_str(date1_3)
    month1_3 = time_to_str(month1_3)
    year1_3 = time_to_str(year1_3)


    if var1_3.get()==1:
        dark1_3='0'
        light1_3='0'
    if var1_3.get()==2:
        dark1_3='1'
        light1_3='0'
    if var1_3.get()==3:
        dark1_3='0'
        light1_3='1'
    
    #phase4

    global date1_4, month1_4, year1_4, hourFrom1_4, minuteFrom1_4, hourOn1_4, minOn1_4, hourOff1_4, minOff1_4, dark1_4, light1_4, tcycle_1_4
    date1_4 = date1_4_entry.get()
    month1_4 = month1_4_entry.get()
    year1_4 = year1_4_entry.get()
    hourFrom1_4= spin1_E_4.get()
    minuteFrom1_4= spin1_F_4.get()
    hourOn1_4=spin1_A_4.get()
    minOn1_4=spin1_B_4.get()
    hourOff1_4=spin1_C_4.get()
    minOff1_4=spin1_D_4.get() 

    tcycle_1_4 = int(tcyclespinbox_arr[0,3].get())
  
    hourOn1_4 = time_to_str(hourOn1_4)    
    minOn1_4 = time_to_str(minOn1_4)
    hourOff1_4=time_to_str(hourOff1_4)
    minOff1_4=time_to_str(minOff1_4)
    
    tcycle_1_4=time_to_str(tcycle_1_4)

    date1_4 = time_to_str(date1_4)
    month1_4 = time_to_str(month1_4)
    year1_4 = time_to_str(year1_4)

    if var1_4.get()==1:
        dark1_4='0'
        light1_4='0'
    if var1_4.get()==2:
        dark1_4='1'
        light1_4='0'
    if var1_4.get()==3:
        dark1_4='0'
        light1_4='1'
    
    #phase 5
    
    global date1_5, month1_5, year1_5, hourFrom1_5, minuteFrom1_5, hourOn1_5, minOn1_5, hourOff1_5, minOff1_5, dark1_5, light1_5, tcycle_1_5
    date1_5 = date1_5_entry.get()
    month1_5 = month1_5_entry.get()
    year1_5 = year1_5_entry.get()
    hourFrom1_5= spin1_E_5.get()
    minuteFrom1_5= spin1_F_5.get()
    hourOn1_5=spin1_A_5.get()
    minOn1_5=spin1_B_5.get()
    hourOff1_5=spin1_C_5.get()
    minOff1_5=spin1_D_5.get()  

    tcycle_1_5 = int(tcyclespinbox_arr[0,4].get())
   
    hourOn1_5 = time_to_str(hourOn1_5)    
    minOn1_5 = time_to_str(minOn1_5)
    hourOff1_5 = time_to_str(hourOff1_5)
    minOff1_5 = time_to_str(minOff1_5)
    
    tcycle_1_5 =time_to_str(tcycle_1_5)

    date1_5 = time_to_str(date1_5)
    month1_5 = time_to_str(month1_5)
    year1_5 = time_to_str(year1_5)


    if var1_5.get()==1:
        dark1_5='0'
        light1_5='0'
    if var1_5.get()==2:
        dark1_5='1'
        light1_5='0'
    if var1_5.get()==3:
        dark1_5='0'
        light1_5='1'

    # phase 6
    global date1_6, month1_6, year1_6, hourFrom1_6, minuteFrom1_6, hourOn1_6, minOn1_6, hourOff1_6, minOff1_6, dark1_6, light1_6, tcycle_1_6
    date1_6 = date1_6_entry.get()
    month1_6 = month1_6_entry.get()
    year1_6 = year1_6_entry.get()
    hourFrom1_6= spin1_E_6.get()
    minuteFrom1_6= spin1_F_6.get()
    hourOn1_6=spin1_A_6.get()
    minOn1_6=spin1_B_6.get()
    hourOff1_6=spin1_C_6.get()
    minOff1_6=spin1_D_6.get()  

    tcycle_1_6 = int(tcyclespinbox_arr[0,5].get())
   
    hourOn1_6 = time_to_str(hourOn1_6)    
    minOn1_6 = time_to_str(minOn1_6)
    hourOff1_6=time_to_str(hourOff1_6)
    minOff1_6=time_to_str(minOff1_6)
    
    tcycle_1_6=time_to_str(tcycle_1_6)

    date1_6 = time_to_str(date1_6)
    month1_6 = time_to_str(month1_6)
    year1_6 = time_to_str(year1_6)

    if var1_6.get()==1:
        dark1_6='0'
        light1_6='0'
    if var1_6.get()==2:
        dark1_6='1'
        light1_6='0'
    if var1_6.get()==3:
        dark1_6='0'
        light1_6='1'
  
    #phase 7
    global date1_7, month1_7, year1_7, hourFrom1_7, minuteFrom1_7, hourOn1_7, minOn1_7, hourOff1_7, minOff1_7, dark1_7, light1_7, tcycle_1_7
    date1_7 = date1_7_entry.get()
    month1_7 = month1_7_entry.get()
    year1_7 = year1_7_entry.get()
    hourFrom1_7= spin1_E_7.get()
    minuteFrom1_7= spin1_F_7.get()
    hourOn1_7=spin1_A_7.get()
    minOn1_7=spin1_B_7.get()
    hourOff1_7=spin1_C_7.get()
    minOff1_7=spin1_D_7.get()

    tcycle_1_7 = int(tcyclespinbox_arr[0,6].get())
 
    hourOn1_7 = time_to_str(hourOn1_7)    
    minOn1_7 = time_to_str(minOn1_7)
    hourOff1_7=time_to_str(hourOff1_7)
    minOff1_7=time_to_str(minOff1_7)
    
    tcycle_1_7=time_to_str(tcycle_1_7)

    date1_7 = time_to_str(date1_7)
    month1_7 = time_to_str(month1_7)
    year1_7 = time_to_str(year1_7)

    if var1_7.get()==1:
        dark1_7='0'
        light1_7='0'
    if var1_7.get()==2:
        dark1_7='1'
        light1_7='0'
    if var1_7.get()==3:
        dark1_7='0'
        light1_7='1'

    #phase 8
    global date1_8, month1_8, year1_8, hourFrom1_8, minuteFrom1_8, hourOn1_8, minOn1_8, hourOff1_8, minOff1_8, dark1_8, light1_8, tcycle_1_8
    date1_8 = date1_8_entry.get()
    month1_8 = month1_8_entry.get()
    year1_8 = year1_8_entry.get()
    hourFrom1_8= spin1_E_8.get()
    minuteFrom1_8= spin1_F_8.get()
    hourOn1_8=spin1_A_8.get()
    minOn1_8=spin1_B_8.get()
    hourOff1_8=spin1_C_8.get()
    minOff1_8=spin1_D_8.get()  

    tcycle_1_8 = int(tcyclespinbox_arr[0,7].get())
  
    hourOn1_8 = time_to_str(hourOn1_8)    
    minOn1_8 = time_to_str(minOn1_8)
    hourOff1_8=time_to_str(hourOff1_8)
    minOff1_8=time_to_str(minOff1_8)
    
    tcycle_1_8=time_to_str(tcycle_1_8)

    date1_8 = time_to_str(date1_8)
    month1_8 = time_to_str(month1_8)
    year1_8 = time_to_str(year1_8)


    if var1_8.get()==1:
        dark1_8='0'
        light1_8='0'
    if var1_8.get()==2:
        dark1_8='1'
        light1_8='0'
    if var1_8.get()==3:
        dark1_8='0'
        light1_8='1'
    
    #phase 9
    global date1_9, month1_9, year1_9, hourFrom1_9, minuteFrom1_9, hourOn1_9, minOn1_9, hourOff1_9, minOff1_9, dark1_9, light1_9, tcycle_1_9
    date1_9 = date1_9_entry.get()
    month1_9 = month1_9_entry.get()
    year1_9 = year1_9_entry.get()
    hourFrom1_9= spin1_E_9.get()
    minuteFrom1_9= spin1_F_9.get()
    hourOn1_9=spin1_A_9.get()
    minOn1_9=spin1_B_9.get()
    hourOff1_9=spin1_C_9.get()
    minOff1_9=spin1_D_9.get()    

    tcycle_1_9 = int(tcyclespinbox_arr[0,8].get())
  
    hourOn1_9 = time_to_str(hourOn1_9)    
    minOn1_9 = time_to_str(minOn1_9)
    hourOff1_9=time_to_str(hourOff1_9)
    minOff1_9=time_to_str(minOff1_9)
    
    tcycle_1_9=time_to_str(tcycle_1_9)

    date1_9 = time_to_str(date1_9)
    month1_9 = time_to_str(month1_9)
    year1_9 = time_to_str(year1_9)


    if var1_9.get()==1:
        dark1_9='0'
        light1_9='0'
    if var1_9.get()==2:
        dark1_9='1'
        light1_9='0'
    if var1_9.get()==3:
        dark1_9='0'
        light1_9='1'

    #phase 10
    global date1_10, month1_10, year1_10, hourFrom1_10, minuteFrom1_10, hourOn1_10, minOn1_10, hourOff1_10, minOff1_10, dark1_10, light1_10, tcycle_1_10
    date1_10 = date1_10_entry.get()
    month1_10 = month1_10_entry.get()
    year1_10 = year1_10_entry.get()
    hourFrom1_10= spin1_E_10.get()
    minuteFrom1_10= spin1_F_10.get()
    hourOn1_10=spin1_A_10.get()
    minOn1_10=spin1_B_10.get()
    hourOff1_10=spin1_C_10.get()
    minOff1_10=spin1_D_10.get()   

    tcycle_1_10 = int(tcyclespinbox_arr[0,9].get())
  
    hourOn1_10 = time_to_str(hourOn1_10)    
    minOn1_10 = time_to_str(minOn1_10)
    hourOff1_10=time_to_str(hourOff1_10)
    minOff1_10=time_to_str(minOff1_10)
    
    tcycle_1_10 = time_to_str(tcycle_1_10)

    date1_10 = time_to_str(date1_10)
    month1_10 = time_to_str(month1_10)
    year1_10 = time_to_str(year1_10)


    if var1_10.get()==1:
        dark1_10='0'
        light1_10='0'
    if var1_10.get()==2:
        dark1_10='1'
        light1_10='0'
    if var1_10.get()==3:
        dark1_10='0'
        light1_10='1'

    #phase 11
    global date1_11, month1_11, year1_11, hourFrom1_11, minuteFrom1_11, hourOn1_11, minOn1_11, hourOff1_11, minOff1_11, dark1_11, light1_11, tcycle_1_11
    
    date1_11 = date1_11_entry.get()
    month1_11 = month1_11_entry.get()
    year1_11 = year1_11_entry.get()
    hourFrom1_11= spin1_E_11.get()
    minuteFrom1_11= spin1_F_11.get()
    hourOn1_11=spin1_A_11.get()
    minOn1_11=spin1_B_11.get()
    hourOff1_11=spin1_C_11.get()
    minOff1_11=spin1_D_11.get() 

    tcycle_1_11 = int(tcyclespinbox_arr[0,10].get())
  
    hourOn1_11 = time_to_str(hourOn1_11)    
    minOn1_11 = time_to_str(minOn1_11)
    hourOff1_11=time_to_str(hourOff1_11)
    minOff1_11=time_to_str(minOff1_11)
    
    tcycle_1_11=time_to_str(tcycle_1_11)

    date1_11 = time_to_str(date1_11)
    month1_11 = time_to_str(month1_11)
    year1_11 = time_to_str(year1_11)

    if var1_11.get()==1:
        dark1_11='0'
        light1_11='0'
    if var1_11.get()==2:
        dark1_11='1'
        light1_11='0'
    if var1_11.get()==3:
        dark1_11='0'
        light1_11='1'

    #phase 12
    global date1_12, month1_12, year1_12, hourFrom1_12, minuteFrom1_12, hourOn1_12, minOn1_12, hourOff1_12, minOff1_12, dark1_12, light1_12, tcycle_1_12
    date1_12 = date1_12_entry.get()
    month1_12 = month1_12_entry.get()
    year1_12 = year1_12_entry.get()
    hourFrom1_12= spin1_E_12.get()
    minuteFrom1_12= spin1_F_12.get()
    hourOn1_12=spin1_A_12.get()
    minOn1_12=spin1_B_12.get()
    hourOff1_12=spin1_C_12.get()
    minOff1_12=spin1_D_12.get()

    tcycle_1_12 = int(tcyclespinbox_arr[0,11].get())
 
    hourOn1_12 = time_to_str(hourOn1_12)    
    minOn1_12 = time_to_str(minOn1_12)
    hourOff1_12=time_to_str(hourOff1_12)
    minOff1_12=time_to_str(minOff1_12)
    
    tcycle_1_12=time_to_str(tcycle_1_12)

    date1_12 = time_to_str(date1_12)
    month1_12 = time_to_str(month1_12)
    year1_12 = time_to_str(year1_12)

    if var1_12.get()==1:
        dark1_12='0'
        light1_12='0'
    if var1_12.get()==2:
        dark1_12='1'
        light1_12='0'
    if var1_12.get()==3:
        dark1_12='0'
        light1_12='1'

    status.pack(side='bottom', fill='x')
    status.set('Box1 schedule is set.')
    
    if setBox1+setBox2+setBox3+setBox4+setBox5 == 5:
        btnSave['state']='normal'
        btnRun['state']='normal'  
        recordingmenu.entryconfig('Start new', state='normal')
        show_conf()
    window.update_idletasks()

def getBox2Schedule(): 
    global setBox2, tcyclespinbox_arr
    setBox2=1
    
    global hourOn2_1, minOn2_1, hourOff2_1, minOff2_1, dark2_1, light2_1, tcycle_2_1
    hourOn2_1=spin2_A_1.get()
    minOn2_1=spin2_B_1.get()
    hourOff2_1=spin2_C_1.get()
    minOff2_1=spin2_D_1.get()        
    tcycle_2_1 = int(tcyclespinbox_arr[1,0].get())
    
    hourOn2_1 = time_to_str(hourOn2_1)
    minOn2_1 = time_to_str(minOn2_1)
    hourOff2_1=time_to_str(hourOff2_1)
    minOff2_1=time_to_str(minOff2_1)
    
    tcycle_2_1=time_to_str(tcycle_2_1)

    if var2_1.get()==1:
        dark2_1='0'
        light2_1='0'
    if var2_1.get()==2:
        dark2_1='1'
        light2_1='0'
    if var2_1.get()==3:
        dark2_1='0'
        light2_1='1'

    #Phase2
    global date2_2, month2_2, year2_2, hourFrom2_2, minuteFrom2_2, hourOn2_2, minOn2_2, hourOff2_2, minOff2_2, dark2_2, light2_2, tcycle_2_2
    date2_2 = date2_2_entry.get()
    month2_2 = month2_2_entry.get()
    year2_2 = year2_2_entry.get()
    
    hourOn2_2=spin2_A_2.get()
    minOn2_2=spin2_B_2.get()
    hourOff2_2=spin2_C_2.get()
    minOff2_2=spin2_D_2.get()     
    hourFrom2_2= spin2_E_2.get()
    minuteFrom2_2= spin2_F_2.get()

    tcycle_2_2 = int(tcyclespinbox_arr[1,1].get())
  
    hourOn2_2 = time_to_str(hourOn2_2)    
    minOn2_2 = time_to_str(minOn2_2)
    hourOff2_2=time_to_str(hourOff2_2)
    minOff2_2=time_to_str(minOff2_2)
    
    tcycle_2_2 = time_to_str(tcycle_2_2)

    date2_2 = time_to_str(date2_2)
    month2_2 = time_to_str(month2_2)
    year2_2 = time_to_str(year2_2)

    if var2_2.get()==1:
        dark2_2='0'
        light2_2='0'
    if var2_2.get()==2:
        dark2_2='1'
        light2_2='0'
    if var2_2.get()==3:
        dark2_2='0'
        light2_2='1'

    #phase3
    
    global date2_3, month2_3, year2_3, hourFrom2_3, minuteFrom2_3, hourOn2_3, minOn2_3, hourOff2_3, minOff2_3, dark2_3, light2_3, tcycle_2_3
    date2_3 = date2_3_entry.get()
    month2_3 = month2_3_entry.get()
    year2_3 = year2_3_entry.get()
    hourFrom2_3= spin2_E_3.get()
    minuteFrom2_3= spin2_F_3.get()
    hourOn2_3=spin2_A_3.get()
    minOn2_3=spin2_B_3.get()
    hourOff2_3=spin2_C_3.get()
    minOff2_3=spin2_D_3.get()   

    tcycle_2_3 = int(tcyclespinbox_arr[1,2].get())
  
    hourOn2_3 = time_to_str(hourOn2_3)    
    minOn2_3 = time_to_str(minOn2_3)
    hourOff2_3=time_to_str(hourOff2_3)
    minOff2_3=time_to_str(minOff2_3)
    
    tcycle_2_3 = time_to_str(tcycle_2_3)
    
    date2_3 = time_to_str(date2_3)
    month2_3 = time_to_str(month2_3)
    year2_3 = time_to_str(year2_3)


    if var2_3.get()==1:
        dark2_3='0'
        light2_3='0'
    if var2_3.get()==2:
        dark2_3='1'
        light2_3='0'
    if var2_3.get()==3:
        dark2_3='0'
        light2_3='1'
    
    #phase4

    global date2_4, month2_4, year2_4, hourFrom2_4, minuteFrom2_4, hourOn2_4, minOn2_4, hourOff2_4, minOff2_4, dark2_4, light2_4, tcycle_2_4
    date2_4 = date2_4_entry.get()
    month2_4 = month2_4_entry.get()
    year2_4 = year2_4_entry.get()
    hourFrom2_4= spin2_E_4.get()
    minuteFrom2_4= spin2_F_4.get()
    hourOn2_4=spin2_A_4.get()
    minOn2_4=spin2_B_4.get()
    hourOff2_4=spin2_C_4.get()
    minOff2_4=spin2_D_4.get() 

    tcycle_2_4 = int(tcyclespinbox_arr[1,3].get())
  
    hourOn2_4 = time_to_str(hourOn2_4)    
    minOn2_4 = time_to_str(minOn2_4)
    hourOff2_4=time_to_str(hourOff2_4)
    minOff2_4=time_to_str(minOff2_4)
    
    tcycle_2_4=time_to_str(tcycle_2_4)

    date2_4 = time_to_str(date2_4)
    month2_4 = time_to_str(month2_4)
    year2_4 = time_to_str(year2_4)

    if var2_4.get()==1:
        dark2_4='0'
        light2_4='0'
    if var2_4.get()==2:
        dark2_4='1'
        light2_4='0'
    if var2_4.get()==3:
        dark2_4='0'
        light2_4='1'
    
    #phase 5
    
    global date2_5, month2_5, year2_5, hourFrom2_5, minuteFrom2_5, hourOn2_5, minOn2_5, hourOff2_5, minOff2_5, dark2_5, light2_5, tcycle_2_5
    date2_5 = date2_5_entry.get()
    month2_5 = month2_5_entry.get()
    year2_5 = year2_5_entry.get()
    hourFrom2_5= spin2_E_5.get()
    minuteFrom2_5= spin2_F_5.get()
    hourOn2_5=spin2_A_5.get()
    minOn2_5=spin2_B_5.get()
    hourOff2_5=spin2_C_5.get()
    minOff2_5=spin2_D_5.get()  

    tcycle_2_5 = int(tcyclespinbox_arr[1,4].get())
   
    hourOn2_5 = time_to_str(hourOn2_5)    
    minOn2_5 = time_to_str(minOn2_5)
    hourOff2_5 = time_to_str(hourOff2_5)
    minOff2_5 = time_to_str(minOff2_5)
    
    tcycle_2_5 =time_to_str(tcycle_2_5)

    date2_5 = time_to_str(date2_5)
    month2_5 = time_to_str(month2_5)
    year2_5 = time_to_str(year2_5)


    if var2_5.get()==1:
        dark2_5='0'
        light2_5='0'
    if var2_5.get()==2:
        dark2_5='1'
        light2_5='0'
    if var2_5.get()==3:
        dark2_5='0'
        light2_5='1'

    # phase 6
    global date2_6, month2_6, year2_6, hourFrom2_6, minuteFrom2_6, hourOn2_6, minOn2_6, hourOff2_6, minOff2_6, dark2_6, light2_6, tcycle_2_6
    date2_6 = date2_6_entry.get()
    month2_6 = month2_6_entry.get()
    year2_6 = year2_6_entry.get()
    hourFrom2_6= spin2_E_6.get()
    minuteFrom2_6= spin2_F_6.get()
    hourOn2_6=spin2_A_6.get()
    minOn2_6=spin2_B_6.get()
    hourOff2_6=spin2_C_6.get()
    minOff2_6=spin2_D_6.get()  

    tcycle_2_6 = int(tcyclespinbox_arr[1,5].get())
   
    hourOn2_6 = time_to_str(hourOn2_6)    
    minOn2_6 = time_to_str(minOn2_6)
    hourOff2_6=time_to_str(hourOff2_6)
    minOff2_6=time_to_str(minOff2_6)
    
    tcycle_2_6=time_to_str(tcycle_2_6)

    date2_6 = time_to_str(date2_6)
    month2_6 = time_to_str(month2_6)
    year2_6 = time_to_str(year2_6)

    if var2_6.get()==1:
        dark2_6='0'
        light2_6='0'
    if var2_6.get()==2:
        dark2_6='1'
        light2_6='0'
    if var2_6.get()==3:
        dark2_6='0'
        light2_6='1'
  
    #phase 7
    global date2_7, month2_7, year2_7, hourFrom2_7, minuteFrom2_7, hourOn2_7, minOn2_7, hourOff2_7, minOff2_7, dark2_7, light2_7, tcycle_2_7
    date2_7 = date2_7_entry.get()
    month2_7 = month2_7_entry.get()
    year2_7 = year2_7_entry.get()
    hourFrom2_7= spin2_E_7.get()
    minuteFrom2_7= spin2_F_7.get()
    hourOn2_7=spin2_A_7.get()
    minOn2_7=spin2_B_7.get()
    hourOff2_7=spin2_C_7.get()
    minOff2_7=spin2_D_7.get()

    tcycle_2_7 = int(tcyclespinbox_arr[1,6].get())
 
    hourOn2_7 = time_to_str(hourOn2_7)    
    minOn2_7 = time_to_str(minOn2_7)
    hourOff2_7=time_to_str(hourOff2_7)
    minOff2_7=time_to_str(minOff2_7)
    
    tcycle_2_7=time_to_str(tcycle_2_7)

    date2_7 = time_to_str(date2_7)
    month2_7 = time_to_str(month2_7)
    year2_7 = time_to_str(year2_7)

    if var2_7.get()==1:
        dark2_7='0'
        light2_7='0'
    if var2_7.get()==2:
        dark2_7='1'
        light2_7='0'
    if var2_7.get()==3:
        dark2_7='0'
        light2_7='1'

    #phase 8
    global date2_8, month2_8, year2_8, hourFrom2_8, minuteFrom2_8, hourOn2_8, minOn2_8, hourOff2_8, minOff2_8, dark2_8, light2_8, tcycle_2_8
    date2_8 = date2_8_entry.get()
    month2_8 = month2_8_entry.get()
    year2_8 = year2_8_entry.get()
    hourFrom2_8= spin2_E_8.get()
    minuteFrom2_8= spin2_F_8.get()
    hourOn2_8=spin2_A_8.get()
    minOn2_8=spin2_B_8.get()
    hourOff2_8=spin2_C_8.get()
    minOff2_8=spin2_D_8.get()  

    tcycle_2_8 = int(tcyclespinbox_arr[1,7].get())
  
    hourOn2_8 = time_to_str(hourOn2_8)    
    minOn2_8 = time_to_str(minOn2_8)
    hourOff2_8=time_to_str(hourOff2_8)
    minOff2_8=time_to_str(minOff2_8)
    
    tcycle_2_8=time_to_str(tcycle_2_8)

    date2_8 = time_to_str(date2_8)
    month2_8 = time_to_str(month2_8)
    year2_8 = time_to_str(year2_8)


    if var2_8.get()==1:
        dark2_8='0'
        light2_8='0'
    if var2_8.get()==2:
        dark2_8='1'
        light2_8='0'
    if var2_8.get()==3:
        dark2_8='0'
        light2_8='1'
    
    #phase 9
    global date2_9, month2_9, year2_9, hourFrom2_9, minuteFrom2_9, hourOn2_9, minOn2_9, hourOff2_9, minOff2_9, dark2_9, light2_9, tcycle_2_9
    date2_9 = date2_9_entry.get()
    month2_9 = month2_9_entry.get()
    year2_9 = year2_9_entry.get()
    hourFrom2_9= spin2_E_9.get()
    minuteFrom2_9= spin2_F_9.get()
    hourOn2_9=spin2_A_9.get()
    minOn2_9=spin2_B_9.get()
    hourOff2_9=spin2_C_9.get()
    minOff2_9=spin2_D_9.get()    

    tcycle_2_9 = int(tcyclespinbox_arr[1,8].get())
  
    hourOn2_9 = time_to_str(hourOn2_9)    
    minOn2_9 = time_to_str(minOn2_9)
    hourOff2_9=time_to_str(hourOff2_9)
    minOff2_9=time_to_str(minOff2_9)
    
    tcycle_2_9=time_to_str(tcycle_2_9)

    date2_9 = time_to_str(date2_9)
    month2_9 = time_to_str(month2_9)
    year2_9 = time_to_str(year2_9)


    if var2_9.get()==1:
        dark2_9='0'
        light2_9='0'
    if var2_9.get()==2:
        dark2_9='1'
        light2_9='0'
    if var2_9.get()==3:
        dark2_9='0'
        light2_9='1'

    #phase 10
    global date2_10, month2_10, year2_10, hourFrom2_10, minuteFrom2_10, hourOn2_10, minOn2_10, hourOff2_10, minOff2_10, dark2_10, light2_10, tcycle_2_10
    date2_10 = date2_10_entry.get()
    month2_10 = month2_10_entry.get()
    year2_10 = year2_10_entry.get()
    hourFrom2_10= spin2_E_10.get()
    minuteFrom2_10= spin2_F_10.get()
    hourOn2_10=spin2_A_10.get()
    minOn2_10=spin2_B_10.get()
    hourOff2_10=spin2_C_10.get()
    minOff2_10=spin2_D_10.get()   

    tcycle_2_10 = int(tcyclespinbox_arr[1,9].get())
  
    hourOn2_10 = time_to_str(hourOn2_10)    
    minOn2_10 = time_to_str(minOn2_10)
    hourOff2_10=time_to_str(hourOff2_10)
    minOff2_10=time_to_str(minOff2_10)
    
    tcycle_2_10 = time_to_str(tcycle_2_10)

    date2_10 = time_to_str(date2_10)
    month2_10 = time_to_str(month2_10)
    year2_10 = time_to_str(year2_10)


    if var2_10.get()==1:
        dark2_10='0'
        light2_10='0'
    if var2_10.get()==2:
        dark2_10='1'
        light2_10='0'
    if var2_10.get()==3:
        dark2_10='0'
        light2_10='1'

    #phase 11
    global date2_11, month2_11, year2_11, hourFrom2_11, minuteFrom2_11, hourOn2_11, minOn2_11, hourOff2_11, minOff2_11, dark2_11, light2_11, tcycle_2_11
    
    date2_11 = date2_11_entry.get()
    month2_11 = month2_11_entry.get()
    year2_11 = year2_11_entry.get()
    hourFrom2_11= spin2_E_11.get()
    minuteFrom2_11= spin2_F_11.get()
    hourOn2_11=spin2_A_11.get()
    minOn2_11=spin2_B_11.get()
    hourOff2_11=spin2_C_11.get()
    minOff2_11=spin2_D_11.get() 

    tcycle_2_11 = int(tcyclespinbox_arr[1,10].get())
  
    hourOn2_11 = time_to_str(hourOn2_11)    
    minOn2_11 = time_to_str(minOn2_11)
    hourOff2_11=time_to_str(hourOff2_11)
    minOff2_11=time_to_str(minOff2_11)
    
    tcycle_2_11=time_to_str(tcycle_2_11)

    date2_11 = time_to_str(date2_11)
    month2_11 = time_to_str(month2_11)
    year2_11 = time_to_str(year2_11)

    if var2_11.get()==1:
        dark2_11='0'
        light2_11='0'
    if var2_11.get()==2:
        dark2_11='1'
        light2_11='0'
    if var2_11.get()==3:
        dark2_11='0'
        light2_11='1'

    #phase 12
    global date2_12, month2_12, year2_12, hourFrom2_12, minuteFrom2_12, hourOn2_12, minOn2_12, hourOff2_12, minOff2_12, dark2_12, light2_12, tcycle_2_12
    date2_12 = date2_12_entry.get()
    month2_12 = month2_12_entry.get()
    year2_12 = year2_12_entry.get()
    hourFrom2_12= spin2_E_12.get()
    minuteFrom2_12= spin2_F_12.get()
    hourOn2_12=spin2_A_12.get()
    minOn2_12=spin2_B_12.get()
    hourOff2_12=spin2_C_12.get()
    minOff2_12=spin2_D_12.get()

    tcycle_2_12 = int(tcyclespinbox_arr[1,11].get())
 
    hourOn2_12 = time_to_str(hourOn2_12)    
    minOn2_12 = time_to_str(minOn2_12)
    hourOff2_12=time_to_str(hourOff2_12)
    minOff2_12=time_to_str(minOff2_12)
    
    tcycle_2_12=time_to_str(tcycle_2_12)

    date2_12 = time_to_str(date2_12)
    month2_12 = time_to_str(month2_12)
    year2_12 = time_to_str(year2_12)

    if var2_12.get()==1:
        dark2_12='0'
        light2_12='0'
    if var2_12.get()==2:
        dark2_12='1'
        light2_12='0'
    if var2_12.get()==3:
        dark2_12='0'
        light2_12='1'

    status.pack(side='bottom', fill='x')
    status.set('Box2 schedule is set.')
    
    if setBox1+setBox2+setBox3+setBox4+setBox5 == 5:
        btnSave['state']='normal'
        btnRun['state']='normal'  
        recordingmenu.entryconfig('Start new', state='normal')
        show_conf()
    window.update_idletasks()

def getBox3Schedule(): 
    global setBox3, tcyclespinbox_arr
    setBox3=1
    
    global hourOn3_1, minOn3_1, hourOff3_1, minOff3_1, dark3_1, light3_1, tcycle_3_1
    hourOn3_1=spin3_A_1.get()
    minOn3_1=spin3_B_1.get()
    hourOff3_1=spin3_C_1.get()
    minOff3_1=spin3_D_1.get()        
    tcycle_3_1 = int(tcyclespinbox_arr[2,0].get())
    
    hourOn3_1 = time_to_str(hourOn3_1)
    minOn3_1 = time_to_str(minOn3_1)
    hourOff3_1=time_to_str(hourOff3_1)
    minOff3_1=time_to_str(minOff3_1)
    
    tcycle_3_1=time_to_str(tcycle_3_1)

    if var3_1.get()==1:
        dark3_1='0'
        light3_1='0'
    if var3_1.get()==2:
        dark3_1='1'
        light3_1='0'
    if var3_1.get()==3:
        dark3_1='0'
        light3_1='1'

    #Phase2
    global date3_2, month3_2, year3_2, hourFrom3_2, minuteFrom3_2, hourOn3_2, minOn3_2, hourOff3_2, minOff3_2, dark3_2, light3_2, tcycle_3_2

    date3_2 = date3_2_entry.get()
    month3_2 = month3_2_entry.get()
    year3_2 = year3_2_entry.get()
    
    hourOn3_2=spin3_A_2.get()
    minOn3_2=spin3_B_2.get()
    hourOff3_2=spin3_C_2.get()
    minOff3_2=spin3_D_2.get()     
    hourFrom3_2= spin3_E_2.get()
    minuteFrom3_2= spin3_F_2.get()

    tcycle_3_2 = int(tcyclespinbox_arr[2,1].get())
  
    hourOn3_2 = time_to_str(hourOn3_2)    
    minOn3_2 = time_to_str(minOn3_2)
    hourOff3_2=time_to_str(hourOff3_2)
    minOff3_2=time_to_str(minOff3_2)
    
    tcycle_3_2 = time_to_str(tcycle_3_2)

    date3_2 = time_to_str(date3_2)
    month3_2 = time_to_str(month3_2)
    year3_2 = time_to_str(year3_2)

    if var3_2.get()==1:
        dark3_2='0'
        light3_2='0'
    if var3_2.get()==2:
        dark3_2='1'
        light3_2='0'
    if var3_2.get()==3:
        dark3_2='0'
        light3_2='1'

    #phase3
    
    global date3_3, month3_3, year3_3, hourFrom3_3, minuteFrom3_3, hourOn3_3, minOn3_3, hourOff3_3, minOff3_3, dark3_3, light3_3, tcycle_3_3
    date3_3 = date3_3_entry.get()
    month3_3 = month3_3_entry.get()
    year3_3 = year3_3_entry.get()
    hourFrom3_3= spin3_E_3.get()
    minuteFrom3_3= spin3_F_3.get()
    hourOn3_3=spin3_A_3.get()
    minOn3_3=spin3_B_3.get()
    hourOff3_3=spin3_C_3.get()
    minOff3_3=spin3_D_3.get()   

    tcycle_3_3 = int(tcyclespinbox_arr[2,2].get())
  
    hourOn3_3 = time_to_str(hourOn3_3)    
    minOn3_3 = time_to_str(minOn3_3)
    hourOff3_3=time_to_str(hourOff3_3)
    minOff3_3=time_to_str(minOff3_3)
    
    tcycle_3_3 = time_to_str(tcycle_3_3)
    
    date3_3 = time_to_str(date3_3)
    month3_3 = time_to_str(month3_3)
    year3_3 = time_to_str(year3_3)


    if var3_3.get()==1:
        dark3_3='0'
        light3_3='0'
    if var3_3.get()==2:
        dark3_3='1'
        light3_3='0'
    if var3_3.get()==3:
        dark3_3='0'
        light3_3='1'
    
    #phase4

    global date3_4, month3_4, year3_4, hourFrom3_4, minuteFrom3_4, hourOn3_4, minOn3_4, hourOff3_4, minOff3_4, dark3_4, light3_4, tcycle_3_4
    date3_4 = date3_4_entry.get()
    month3_4 = month3_4_entry.get()
    year3_4 = year3_4_entry.get()
    hourFrom3_4= spin3_E_4.get()
    minuteFrom3_4= spin3_F_4.get()
    hourOn3_4=spin3_A_4.get()
    minOn3_4=spin3_B_4.get()
    hourOff3_4=spin3_C_4.get()
    minOff3_4=spin3_D_4.get() 

    tcycle_3_4 = int(tcyclespinbox_arr[2,3].get())
  
    hourOn3_4 = time_to_str(hourOn3_4)    
    minOn3_4 = time_to_str(minOn3_4)
    hourOff3_4=time_to_str(hourOff3_4)
    minOff3_4=time_to_str(minOff3_4)
    
    tcycle_3_4=time_to_str(tcycle_3_4)

    date3_4 = time_to_str(date3_4)
    month3_4 = time_to_str(month3_4)
    year3_4 = time_to_str(year3_4)

    if var3_4.get()==1:
        dark3_4='0'
        light3_4='0'
    if var3_4.get()==2:
        dark3_4='1'
        light3_4='0'
    if var3_4.get()==3:
        dark3_4='0'
        light3_4='1'
    
    #phase 5
    
    global date3_5, month3_5, year3_5, hourFrom3_5, minuteFrom3_5, hourOn3_5, minOn3_5, hourOff3_5, minOff3_5, dark3_5, light3_5, tcycle_3_5
    date3_5 = date3_5_entry.get()
    month3_5 = month3_5_entry.get()
    year3_5 = year3_5_entry.get()
    hourFrom3_5= spin3_E_5.get()
    minuteFrom3_5= spin3_F_5.get()
    hourOn3_5=spin3_A_5.get()
    minOn3_5=spin3_B_5.get()
    hourOff3_5=spin3_C_5.get()
    minOff3_5=spin3_D_5.get()  

    tcycle_3_5 = int(tcyclespinbox_arr[2,4].get())
   
    hourOn3_5 = time_to_str(hourOn3_5)    
    minOn3_5 = time_to_str(minOn3_5)
    hourOff3_5 = time_to_str(hourOff3_5)
    minOff3_5 = time_to_str(minOff3_5)
    
    tcycle_3_5 =time_to_str(tcycle_3_5)

    date3_5 = time_to_str(date3_5)
    month3_5 = time_to_str(month3_5)
    year3_5 = time_to_str(year3_5)


    if var3_5.get()==1:
        dark3_5='0'
        light3_5='0'
    if var3_5.get()==2:
        dark3_5='1'
        light3_5='0'
    if var3_5.get()==3:
        dark3_5='0'
        light3_5='1'

    # phase 6
    global date3_6, month3_6, year3_6, hourFrom3_6, minuteFrom3_6, hourOn3_6, minOn3_6, hourOff3_6, minOff3_6, dark3_6, light3_6, tcycle_3_6
    date3_6 = date3_6_entry.get()
    month3_6 = month3_6_entry.get()
    year3_6 = year3_6_entry.get()
    hourFrom3_6= spin3_E_6.get()
    minuteFrom3_6= spin3_F_6.get()
    hourOn3_6=spin3_A_6.get()
    minOn3_6=spin3_B_6.get()
    hourOff3_6=spin3_C_6.get()
    minOff3_6=spin3_D_6.get()  

    tcycle_3_6 = int(tcyclespinbox_arr[2,5].get())
   
    hourOn3_6 = time_to_str(hourOn3_6)    
    minOn3_6 = time_to_str(minOn3_6)
    hourOff3_6=time_to_str(hourOff3_6)
    minOff3_6=time_to_str(minOff3_6)
    
    tcycle_3_6=time_to_str(tcycle_3_6)

    date3_6 = time_to_str(date3_6)
    month3_6 = time_to_str(month3_6)
    year3_6 = time_to_str(year3_6)

    if var3_6.get()==1:
        dark3_6='0'
        light3_6='0'
    if var3_6.get()==2:
        dark3_6='1'
        light3_6='0'
    if var3_6.get()==3:
        dark3_6='0'
        light3_6='1'
  
    #phase 7
    global date3_7, month3_7, year3_7, hourFrom3_7, minuteFrom3_7, hourOn3_7, minOn3_7, hourOff3_7, minOff3_7, dark3_7, light3_7, tcycle_3_7
    date3_7 = date3_7_entry.get()
    month3_7 = month3_7_entry.get()
    year3_7 = year3_7_entry.get()
    hourFrom3_7= spin3_E_7.get()
    minuteFrom3_7= spin3_F_7.get()
    hourOn3_7=spin3_A_7.get()
    minOn3_7=spin3_B_7.get()
    hourOff3_7=spin3_C_7.get()
    minOff3_7=spin3_D_7.get()

    tcycle_3_7 = int(tcyclespinbox_arr[2,6].get())
 
    hourOn3_7 = time_to_str(hourOn3_7)    
    minOn3_7 = time_to_str(minOn3_7)
    hourOff3_7=time_to_str(hourOff3_7)
    minOff3_7=time_to_str(minOff3_7)
    
    tcycle_3_7=time_to_str(tcycle_3_7)

    date3_7 = time_to_str(date3_7)
    month3_7 = time_to_str(month3_7)
    year3_7 = time_to_str(year3_7)

    if var3_7.get()==1:
        dark3_7='0'
        light3_7='0'
    if var3_7.get()==2:
        dark3_7='1'
        light3_7='0'
    if var3_7.get()==3:
        dark3_7='0'
        light3_7='1'

    #phase 8
    global date3_8, month3_8, year3_8, hourFrom3_8, minuteFrom3_8, hourOn3_8, minOn3_8, hourOff3_8, minOff3_8, dark3_8, light3_8, tcycle_3_8
    date3_8 = date3_8_entry.get()
    month3_8 = month3_8_entry.get()
    year3_8 = year3_8_entry.get()
    hourFrom3_8= spin3_E_8.get()
    minuteFrom3_8= spin3_F_8.get()
    hourOn3_8=spin3_A_8.get()
    minOn3_8=spin3_B_8.get()
    hourOff3_8=spin3_C_8.get()
    minOff3_8=spin3_D_8.get()  

    tcycle_3_8 = int(tcyclespinbox_arr[2,7].get())
  
    hourOn3_8 = time_to_str(hourOn3_8)    
    minOn3_8 = time_to_str(minOn3_8)
    hourOff3_8=time_to_str(hourOff3_8)
    minOff3_8=time_to_str(minOff3_8)
    
    tcycle_3_8=time_to_str(tcycle_3_8)

    date3_8 = time_to_str(date3_8)
    month3_8 = time_to_str(month3_8)
    year3_8 = time_to_str(year3_8)


    if var3_8.get()==1:
        dark3_8='0'
        light3_8='0'
    if var3_8.get()==2:
        dark3_8='1'
        light3_8='0'
    if var3_8.get()==3:
        dark3_8='0'
        light3_8='1'
    
    #phase 9
    global date3_9, month3_9, year3_9, hourFrom3_9, minuteFrom3_9, hourOn3_9, minOn3_9, hourOff3_9, minOff3_9, dark3_9, light3_9, tcycle_3_9
    date3_9 = date3_9_entry.get()
    month3_9 = month3_9_entry.get()
    year3_9 = year3_9_entry.get()
    hourFrom3_9= spin3_E_9.get()
    minuteFrom3_9= spin3_F_9.get()
    hourOn3_9=spin3_A_9.get()
    minOn3_9=spin3_B_9.get()
    hourOff3_9=spin3_C_9.get()
    minOff3_9=spin3_D_9.get()    

    tcycle_3_9 = int(tcyclespinbox_arr[2,8].get())
  
    hourOn3_9 = time_to_str(hourOn3_9)    
    minOn3_9 = time_to_str(minOn3_9)
    hourOff3_9=time_to_str(hourOff3_9)
    minOff3_9=time_to_str(minOff3_9)
    
    tcycle_3_9=time_to_str(tcycle_3_9)

    date3_9 = time_to_str(date3_9)
    month3_9 = time_to_str(month3_9)
    year3_9 = time_to_str(year3_9)


    if var3_9.get()==1:
        dark3_9='0'
        light3_9='0'
    if var3_9.get()==2:
        dark3_9='1'
        light3_9='0'
    if var3_9.get()==3:
        dark3_9='0'
        light3_9='1'

    #phase 10
    global date3_10, month3_10, year3_10, hourFrom3_10, minuteFrom3_10, hourOn3_10, minOn3_10, hourOff3_10, minOff3_10, dark3_10, light3_10, tcycle_3_10
    date3_10 = date3_10_entry.get()
    month3_10 = month3_10_entry.get()
    year3_10 = year3_10_entry.get()
    hourFrom3_10= spin3_E_10.get()
    minuteFrom3_10= spin3_F_10.get()
    hourOn3_10=spin3_A_10.get()
    minOn3_10=spin3_B_10.get()
    hourOff3_10=spin3_C_10.get()
    minOff3_10=spin3_D_10.get()   

    tcycle_3_10 = int(tcyclespinbox_arr[2,9].get())
  
    hourOn3_10 = time_to_str(hourOn3_10)    
    minOn3_10 = time_to_str(minOn3_10)
    hourOff3_10=time_to_str(hourOff3_10)
    minOff3_10=time_to_str(minOff3_10)
    
    tcycle_3_10 = time_to_str(tcycle_3_10)

    date3_10 = time_to_str(date3_10)
    month3_10 = time_to_str(month3_10)
    year3_10 = time_to_str(year3_10)


    if var3_10.get()==1:
        dark3_10='0'
        light3_10='0'
    if var3_10.get()==2:
        dark3_10='1'
        light3_10='0'
    if var3_10.get()==3:
        dark3_10='0'
        light3_10='1'

    #phase 11
    global date3_11, month3_11, year3_11, hourFrom3_11, minuteFrom3_11, hourOn3_11, minOn3_11, hourOff3_11, minOff3_11, dark3_11, light3_11, tcycle_3_11
    
    date3_11 = date3_11_entry.get()
    month3_11 = month3_11_entry.get()
    year3_11 = year3_11_entry.get()
    hourFrom3_11= spin3_E_11.get()
    minuteFrom3_11= spin3_F_11.get()
    hourOn3_11=spin3_A_11.get()
    minOn3_11=spin3_B_11.get()
    hourOff3_11=spin3_C_11.get()
    minOff3_11=spin3_D_11.get() 

    tcycle_3_11 = int(tcyclespinbox_arr[2,10].get())
  
    hourOn3_11 = time_to_str(hourOn3_11)    
    minOn3_11 = time_to_str(minOn3_11)
    hourOff3_11=time_to_str(hourOff3_11)
    minOff3_11=time_to_str(minOff3_11)
    
    tcycle_3_11=time_to_str(tcycle_3_11)

    date3_11 = time_to_str(date3_11)
    month3_11 = time_to_str(month3_11)
    year3_11 = time_to_str(year3_11)

    if var3_11.get()==1:
        dark3_11='0'
        light3_11='0'
    if var3_11.get()==2:
        dark3_11='1'
        light3_11='0'
    if var3_11.get()==3:
        dark3_11='0'
        light3_11='1'

    #phase 12
    global date3_12, month3_12, year3_12, hourFrom3_12, minuteFrom3_12, hourOn3_12, minOn3_12, hourOff3_12, minOff3_12, dark3_12, light3_12, tcycle_3_12
    date3_12 = date3_12_entry.get()
    month3_12 = month3_12_entry.get()
    year3_12 = year3_12_entry.get()
    hourFrom3_12= spin3_E_12.get()
    minuteFrom3_12= spin3_F_12.get()
    hourOn3_12=spin3_A_12.get()
    minOn3_12=spin3_B_12.get()
    hourOff3_12=spin3_C_12.get()
    minOff3_12=spin3_D_12.get()

    tcycle_3_12 = int(tcyclespinbox_arr[2,11].get())
 
    hourOn3_12 = time_to_str(hourOn3_12)    
    minOn3_12 = time_to_str(minOn3_12)
    hourOff3_12=time_to_str(hourOff3_12)
    minOff3_12=time_to_str(minOff3_12)
    
    tcycle_3_12=time_to_str(tcycle_3_12)

    date3_12 = time_to_str(date3_12)
    month3_12 = time_to_str(month3_12)
    year3_12 = time_to_str(year3_12)

    if var3_12.get()==1:
        dark3_12='0'
        light3_12='0'
    if var3_12.get()==2:
        dark3_12='1'
        light3_12='0'
    if var3_12.get()==3:
        dark3_12='0'
        light3_12='1'

    status.pack(side='bottom', fill='x')
    status.set('Box3 schedule is set.')
    
    if setBox1+setBox2+setBox3+setBox4+setBox5 == 5:
        btnSave['state']='normal'
        btnRun['state']='normal'  
        recordingmenu.entryconfig('Start new', state='normal')
        show_conf()
    window.update_idletasks()
    
def getBox4Schedule(): 
    global setBox4, tcyclespinbox_arr
    setBox4=1
    
    global hourOn4_1, minOn4_1, hourOff4_1, minOff4_1, dark4_1, light4_1, tcycle_4_1
    hourOn4_1=spin4_A_1.get()
    minOn4_1=spin4_B_1.get()
    hourOff4_1=spin4_C_1.get()
    minOff4_1=spin4_D_1.get()        
    tcycle_4_1 = int(tcyclespinbox_arr[3,0].get())
    
    hourOn4_1 = time_to_str(hourOn4_1)
    minOn4_1 = time_to_str(minOn4_1)
    hourOff4_1=time_to_str(hourOff4_1)
    minOff4_1=time_to_str(minOff4_1)
    
    tcycle_4_1=time_to_str(tcycle_4_1)

    if var4_1.get()==1:
        dark4_1='0'
        light4_1='0'
    if var4_1.get()==2:
        dark4_1='1'
        light4_1='0'
    if var4_1.get()==3:
        dark4_1='0'
        light4_1='1'

    #Phase2
    global date4_2, month4_2, year4_2, hourFrom4_2, minuteFrom4_2, hourOn4_2, minOn4_2, hourOff4_2, minOff4_2, dark4_2, light4_2, tcycle_4_2

    date4_2 = date4_2_entry.get()
    month4_2 = month4_2_entry.get()
    year4_2 = year4_2_entry.get()

    date4_2 = date4_2_entry.get()
    month4_2 = month4_2_entry.get()
    year4_2 = year4_2_entry.get()
    
    hourOn4_2=spin4_A_2.get()
    minOn4_2=spin4_B_2.get()
    hourOff4_2=spin4_C_2.get()
    minOff4_2=spin4_D_2.get()     
    hourFrom4_2= spin4_E_2.get()
    minuteFrom4_2= spin4_F_2.get()

    tcycle_4_2 = int(tcyclespinbox_arr[3,1].get())
  
    hourOn4_2 = time_to_str(hourOn4_2)    
    minOn4_2 = time_to_str(minOn4_2)
    hourOff4_2=time_to_str(hourOff4_2)
    minOff4_2=time_to_str(minOff4_2)
    
    tcycle_4_2 = time_to_str(tcycle_4_2)

    date4_2 = time_to_str(date4_2)
    month4_2 = time_to_str(month4_2)
    year4_2 = time_to_str(year4_2)

    if var4_2.get()==1:
        dark4_2='0'
        light4_2='0'
    if var4_2.get()==2:
        dark4_2='1'
        light4_2='0'
    if var4_2.get()==3:
        dark4_2='0'
        light4_2='1'

    #phase3
    
    global date4_3, month4_3, year4_3, hourFrom4_3, minuteFrom4_3, hourOn4_3, minOn4_3, hourOff4_3, minOff4_3, dark4_3, light4_3, tcycle_4_3

    date4_3 = date4_3_entry.get()
    month4_3 = month4_3_entry.get()
    year4_3 = year4_3_entry.get()

    hourFrom4_3= spin4_E_3.get()
    minuteFrom4_3= spin4_F_3.get()
    hourOn4_3=spin4_A_3.get()
    minOn4_3=spin4_B_3.get()
    hourOff4_3=spin4_C_3.get()
    minOff4_3=spin4_D_3.get()   

    tcycle_4_3 = int(tcyclespinbox_arr[3,2].get())
  
    hourOn4_3 = time_to_str(hourOn4_3)    
    minOn4_3 = time_to_str(minOn4_3)
    hourOff4_3=time_to_str(hourOff4_3)
    minOff4_3=time_to_str(minOff4_3)
    
    tcycle_4_3 = time_to_str(tcycle_4_3)
    
    date4_3 = time_to_str(date4_3)
    month4_3 = time_to_str(month4_3)
    year4_3 = time_to_str(year4_3)


    if var4_3.get()==1:
        dark4_3='0'
        light4_3='0'
    if var4_3.get()==2:
        dark4_3='1'
        light4_3='0'
    if var4_3.get()==3:
        dark4_3='0'
        light4_3='1'
    
    #phase4

    global date4_4, month4_4, year4_4, hourFrom4_4, minuteFrom4_4, hourOn4_4, minOn4_4, hourOff4_4, minOff4_4, dark4_4, light4_4, tcycle_4_4
    date4_4 = date4_4_entry.get()
    month4_4 = month4_4_entry.get()
    year4_4 = year4_4_entry.get()
    hourFrom4_4= spin4_E_4.get()
    minuteFrom4_4= spin4_F_4.get()
    hourOn4_4=spin4_A_4.get()
    minOn4_4=spin4_B_4.get()
    hourOff4_4=spin4_C_4.get()
    minOff4_4=spin4_D_4.get() 

    tcycle_4_4 = int(tcyclespinbox_arr[3,3].get())
  
    hourOn4_4 = time_to_str(hourOn4_4)    
    minOn4_4 = time_to_str(minOn4_4)
    hourOff4_4=time_to_str(hourOff4_4)
    minOff4_4=time_to_str(minOff4_4)
    
    tcycle_4_4=time_to_str(tcycle_4_4)

    date4_4 = time_to_str(date4_4)
    month4_4 = time_to_str(month4_4)
    year4_4 = time_to_str(year4_4)

    if var4_4.get()==1:
        dark4_4='0'
        light4_4='0'
    if var4_4.get()==2:
        dark4_4='1'
        light4_4='0'
    if var4_4.get()==3:
        dark4_4='0'
        light4_4='1'
    
    #phase 5
    
    global date4_5, month4_5, year4_5, hourFrom4_5, minuteFrom4_5, hourOn4_5, minOn4_5, hourOff4_5, minOff4_5, dark4_5, light4_5, tcycle_4_5
    date4_5 = date4_5_entry.get()
    month4_5 = month4_5_entry.get()
    year4_5 = year4_5_entry.get()
    hourFrom4_5= spin4_E_5.get()
    minuteFrom4_5= spin4_F_5.get()
    hourOn4_5=spin4_A_5.get()
    minOn4_5=spin4_B_5.get()
    hourOff4_5=spin4_C_5.get()
    minOff4_5=spin4_D_5.get()  

    tcycle_4_5 = int(tcyclespinbox_arr[3,4].get())
   
    hourOn4_5 = time_to_str(hourOn4_5)    
    minOn4_5 = time_to_str(minOn4_5)
    hourOff4_5 = time_to_str(hourOff4_5)
    minOff4_5 = time_to_str(minOff4_5)
    
    tcycle_4_5 =time_to_str(tcycle_4_5)

    date4_5 = time_to_str(date4_5)
    month4_5 = time_to_str(month4_5)
    year4_5 = time_to_str(year4_5)


    if var4_5.get()==1:
        dark4_5='0'
        light4_5='0'
    if var4_5.get()==2:
        dark4_5='1'
        light4_5='0'
    if var4_5.get()==3:
        dark4_5='0'
        light4_5='1'

    # phase 6
    global date4_6, month4_6, year4_6, hourFrom4_6, minuteFrom4_6, hourOn4_6, minOn4_6, hourOff4_6, minOff4_6, dark4_6, light4_6, tcycle_4_6
    date4_6 = date4_6_entry.get()
    month4_6 = month4_6_entry.get()
    year4_6 = year4_6_entry.get()
    hourFrom4_6= spin4_E_6.get()
    minuteFrom4_6= spin4_F_6.get()
    hourOn4_6=spin4_A_6.get()
    minOn4_6=spin4_B_6.get()
    hourOff4_6=spin4_C_6.get()
    minOff4_6=spin4_D_6.get()  

    tcycle_4_6 = int(tcyclespinbox_arr[3,5].get())
   
    hourOn4_6 = time_to_str(hourOn4_6)    
    minOn4_6 = time_to_str(minOn4_6)
    hourOff4_6=time_to_str(hourOff4_6)
    minOff4_6=time_to_str(minOff4_6)
    
    tcycle_4_6=time_to_str(tcycle_4_6)

    date4_6 = time_to_str(date4_6)
    month4_6 = time_to_str(month4_6)
    year4_6 = time_to_str(year4_6)

    if var4_6.get()==1:
        dark4_6='0'
        light4_6='0'
    if var4_6.get()==2:
        dark4_6='1'
        light4_6='0'
    if var4_6.get()==3:
        dark4_6='0'
        light4_6='1'
  
    #phase 7
    global date4_7, month4_7, year4_7, hourFrom4_7, minuteFrom4_7, hourOn4_7, minOn4_7, hourOff4_7, minOff4_7, dark4_7, light4_7, tcycle_4_7
    date4_7 = date4_7_entry.get()
    month4_7 = month4_7_entry.get()
    year4_7 = year4_7_entry.get()
    hourFrom4_7= spin4_E_7.get()
    minuteFrom4_7= spin4_F_7.get()
    hourOn4_7=spin4_A_7.get()
    minOn4_7=spin4_B_7.get()
    hourOff4_7=spin4_C_7.get()
    minOff4_7=spin4_D_7.get()

    tcycle_4_7 = int(tcyclespinbox_arr[3,6].get())
 
    hourOn4_7 = time_to_str(hourOn4_7)    
    minOn4_7 = time_to_str(minOn4_7)
    hourOff4_7=time_to_str(hourOff4_7)
    minOff4_7=time_to_str(minOff4_7)
    
    tcycle_4_7=time_to_str(tcycle_4_7)

    date4_7 = time_to_str(date4_7)
    month4_7 = time_to_str(month4_7)
    year4_7 = time_to_str(year4_7)

    if var4_7.get()==1:
        dark4_7='0'
        light4_7='0'
    if var4_7.get()==2:
        dark4_7='1'
        light4_7='0'
    if var4_7.get()==3:
        dark4_7='0'
        light4_7='1'

    #phase 8
    global date4_8, month4_8, year4_8, hourFrom4_8, minuteFrom4_8, hourOn4_8, minOn4_8, hourOff4_8, minOff4_8, dark4_8, light4_8, tcycle_4_8
    date4_8 = date4_8_entry.get()
    month4_8 = month4_8_entry.get()
    year4_8 = year4_8_entry.get()
    hourFrom4_8= spin4_E_8.get()
    minuteFrom4_8= spin4_F_8.get()
    hourOn4_8=spin4_A_8.get()
    minOn4_8=spin4_B_8.get()
    hourOff4_8=spin4_C_8.get()
    minOff4_8=spin4_D_8.get()  

    tcycle_4_8 = int(tcyclespinbox_arr[3,7].get())
  
    hourOn4_8 = time_to_str(hourOn4_8)    
    minOn4_8 = time_to_str(minOn4_8)
    hourOff4_8=time_to_str(hourOff4_8)
    minOff4_8=time_to_str(minOff4_8)
    
    tcycle_4_8=time_to_str(tcycle_4_8)

    date4_8 = time_to_str(date4_8)
    month4_8 = time_to_str(month4_8)
    year4_8 = time_to_str(year4_8)


    if var4_8.get()==1:
        dark4_8='0'
        light4_8='0'
    if var4_8.get()==2:
        dark4_8='1'
        light4_8='0'
    if var4_8.get()==3:
        dark4_8='0'
        light4_8='1'
    
    #phase 9
    global date4_9, month4_9, year4_9, hourFrom4_9, minuteFrom4_9, hourOn4_9, minOn4_9, hourOff4_9, minOff4_9, dark4_9, light4_9, tcycle_4_9
    date4_9 = date4_9_entry.get()
    month4_9 = month4_9_entry.get()
    year4_9 = year4_9_entry.get()
    hourFrom4_9= spin4_E_9.get()
    minuteFrom4_9= spin4_F_9.get()
    hourOn4_9=spin4_A_9.get()
    minOn4_9=spin4_B_9.get()
    hourOff4_9=spin4_C_9.get()
    minOff4_9=spin4_D_9.get()    

    tcycle_4_9 = int(tcyclespinbox_arr[3,8].get())
  
    hourOn4_9 = time_to_str(hourOn4_9)    
    minOn4_9 = time_to_str(minOn4_9)
    hourOff4_9=time_to_str(hourOff4_9)
    minOff4_9=time_to_str(minOff4_9)
    
    tcycle_4_9=time_to_str(tcycle_4_9)

    date4_9 = time_to_str(date4_9)
    month4_9 = time_to_str(month4_9)
    year4_9 = time_to_str(year4_9)


    if var4_9.get()==1:
        dark4_9='0'
        light4_9='0'
    if var4_9.get()==2:
        dark4_9='1'
        light4_9='0'
    if var4_9.get()==3:
        dark4_9='0'
        light4_9='1'

    #phase 10
    global date4_10, month4_10, year4_10, hourFrom4_10, minuteFrom4_10, hourOn4_10, minOn4_10, hourOff4_10, minOff4_10, dark4_10, light4_10, tcycle_4_10
    date4_10 = date4_10_entry.get()
    month4_10 = month4_10_entry.get()
    year4_10 = year4_10_entry.get()
    hourFrom4_10= spin4_E_10.get()
    minuteFrom4_10= spin4_F_10.get()
    hourOn4_10=spin4_A_10.get()
    minOn4_10=spin4_B_10.get()
    hourOff4_10=spin4_C_10.get()
    minOff4_10=spin4_D_10.get()   

    tcycle_4_10 = int(tcyclespinbox_arr[3,9].get())
  
    hourOn4_10 = time_to_str(hourOn4_10)    
    minOn4_10 = time_to_str(minOn4_10)
    hourOff4_10=time_to_str(hourOff4_10)
    minOff4_10=time_to_str(minOff4_10)
    
    tcycle_4_10 = time_to_str(tcycle_4_10)

    date4_10 = time_to_str(date4_10)
    month4_10 = time_to_str(month4_10)
    year4_10 = time_to_str(year4_10)


    if var4_10.get()==1:
        dark4_10='0'
        light4_10='0'
    if var4_10.get()==2:
        dark4_10='1'
        light4_10='0'
    if var4_10.get()==3:
        dark4_10='0'
        light4_10='1'

    #phase 11
    global date4_11, month4_11, year4_11, hourFrom4_11, minuteFrom4_11, hourOn4_11, minOn4_11, hourOff4_11, minOff4_11, dark4_11, light4_11, tcycle_4_11
    
    date4_11 = date4_11_entry.get()
    month4_11 = month4_11_entry.get()
    year4_11 = year4_11_entry.get()
    hourFrom4_11= spin4_E_11.get()
    minuteFrom4_11= spin4_F_11.get()
    hourOn4_11=spin4_A_11.get()
    minOn4_11=spin4_B_11.get()
    hourOff4_11=spin4_C_11.get()
    minOff4_11=spin4_D_11.get() 

    tcycle_4_11 = int(tcyclespinbox_arr[3,10].get())
  
    hourOn4_11 = time_to_str(hourOn4_11)    
    minOn4_11 = time_to_str(minOn4_11)
    hourOff4_11=time_to_str(hourOff4_11)
    minOff4_11=time_to_str(minOff4_11)
    
    tcycle_4_11=time_to_str(tcycle_4_11)

    date4_11 = time_to_str(date4_11)
    month4_11 = time_to_str(month4_11)
    year4_11 = time_to_str(year4_11)

    if var4_11.get()==1:
        dark4_11='0'
        light4_11='0'
    if var4_11.get()==2:
        dark4_11='1'
        light4_11='0'
    if var4_11.get()==3:
        dark4_11='0'
        light4_11='1'

    #phase 12
    global date4_12, month4_12, year4_12, hourFrom4_12, minuteFrom4_12, hourOn4_12, minOn4_12, hourOff4_12, minOff4_12, dark4_12, light4_12, tcycle_4_12
    date4_12 = date4_12_entry.get()
    month4_12 = month4_12_entry.get()
    year4_12 = year4_12_entry.get()
    hourFrom4_12= spin4_E_12.get()
    minuteFrom4_12= spin4_F_12.get()
    hourOn4_12=spin4_A_12.get()
    minOn4_12=spin4_B_12.get()
    hourOff4_12=spin4_C_12.get()
    minOff4_12=spin4_D_12.get()

    tcycle_4_12 = int(tcyclespinbox_arr[3,11].get())
 
    hourOn4_12 = time_to_str(hourOn4_12)    
    minOn4_12 = time_to_str(minOn4_12)
    hourOff4_12=time_to_str(hourOff4_12)
    minOff4_12=time_to_str(minOff4_12)
    
    tcycle_4_12=time_to_str(tcycle_4_12)

    date4_12 = time_to_str(date4_12)
    month4_12 = time_to_str(month4_12)
    year4_12 = time_to_str(year4_12)

    if var4_12.get()==1:
        dark4_12='0'
        light4_12='0'
    if var4_12.get()==2:
        dark4_12='1'
        light4_12='0'
    if var4_12.get()==3:
        dark4_12='0'
        light4_12='1'

    status.pack(side='bottom', fill='x')
    status.set('Box4 schedule is set.')
    
    if setBox1+setBox2+setBox3+setBox4+setBox5 == 5:
        btnSave['state']='normal'
        btnRun['state']='normal'  
        recordingmenu.entryconfig('Start new', state='normal')
        show_conf()
    window.update_idletasks()
    
def getBox5Schedule(): 
    global setBox5, tcyclespinbox_arr
    setBox5=1
    
    global hourOn5_1, minOn5_1, hourOff5_1, minOff5_1, dark5_1, light5_1, tcycle_5_1
    hourOn5_1=spin5_A_1.get()
    minOn5_1=spin5_B_1.get()
    hourOff5_1=spin5_C_1.get()
    minOff5_1=spin5_D_1.get()        
    tcycle_5_1 = int(tcyclespinbox_arr[4,0].get())
    
    hourOn5_1 = time_to_str(hourOn5_1)
    minOn5_1 = time_to_str(minOn5_1)
    hourOff5_1=time_to_str(hourOff5_1)
    minOff5_1=time_to_str(minOff5_1)
    
    tcycle_5_1=time_to_str(tcycle_5_1)

    if var5_1.get()==1:
        dark5_1='0'
        light5_1='0'
    if var5_1.get()==2:
        dark5_1='1'
        light5_1='0'
    if var5_1.get()==3:
        dark5_1='0'
        light5_1='1'

    #Phase2
    global date5_2, month5_2, year5_2, hourFrom5_2, minuteFrom5_2, hourOn5_2, minOn5_2, hourOff5_2, minOff5_2, dark5_2, light5_2, tcycle_5_2

    date5_2 = date5_2_entry.get()
    month5_2 = month5_2_entry.get()
    year5_2 = year5_2_entry.get()
    
    hourOn5_2=spin5_A_2.get()
    minOn5_2=spin5_B_2.get()
    hourOff5_2=spin5_C_2.get()
    minOff5_2=spin5_D_2.get()     
    hourFrom5_2= spin5_E_2.get()
    minuteFrom5_2= spin5_F_2.get()

    tcycle_5_2 = int(tcyclespinbox_arr[4,1].get())
  
    hourOn5_2 = time_to_str(hourOn5_2)    
    minOn5_2 = time_to_str(minOn5_2)
    hourOff5_2=time_to_str(hourOff5_2)
    minOff5_2=time_to_str(minOff5_2)
    
    tcycle_5_2 = time_to_str(tcycle_5_2)

    date5_2 = time_to_str(date5_2)
    month5_2 = time_to_str(month5_2)
    year5_2 = time_to_str(year5_2)

    if var5_2.get()==1:
        dark5_2='0'
        light5_2='0'
    if var5_2.get()==2:
        dark5_2='1'
        light5_2='0'
    if var5_2.get()==3:
        dark5_2='0'
        light5_2='1'

    #phase3
    
    global date5_3, month5_3, year5_3, hourFrom5_3, minuteFrom5_3, hourOn5_3, minOn5_3, hourOff5_3, minOff5_3, dark5_3, light5_3, tcycle_5_3

    date5_3 = date5_3_entry.get()
    month5_3 = month5_3_entry.get()
    year5_3 = year5_3_entry.get()

    hourFrom5_3= spin5_E_3.get()
    minuteFrom5_3= spin5_F_3.get()
    hourOn5_3=spin5_A_3.get()
    minOn5_3=spin5_B_3.get()
    hourOff5_3=spin5_C_3.get()
    minOff5_3=spin5_D_3.get()   

    tcycle_5_3 = int(tcyclespinbox_arr[4,2].get())
  
    hourOn5_3 = time_to_str(hourOn5_3)    
    minOn5_3 = time_to_str(minOn5_3)
    hourOff5_3=time_to_str(hourOff5_3)
    minOff5_3=time_to_str(minOff5_3)
    
    tcycle_5_3 = time_to_str(tcycle_5_3)
    
    date5_3 = time_to_str(date5_3)
    month5_3 = time_to_str(month5_3)
    year5_3 = time_to_str(year5_3)


    if var5_3.get()==1:
        dark5_3='0'
        light5_3='0'
    if var5_3.get()==2:
        dark5_3='1'
        light5_3='0'
    if var5_3.get()==3:
        dark5_3='0'
        light5_3='1'
    
    #phase4

    global date5_4, month5_4, year5_4, hourFrom5_4, minuteFrom5_4, hourOn5_4, minOn5_4, hourOff5_4, minOff5_4, dark5_4, light5_4, tcycle_5_4
    
    date5_4 = date5_4_entry.get()
    month5_4 = month5_4_entry.get()
    year5_4 = year5_4_entry.get()

    hourFrom5_4= spin5_E_4.get()
    minuteFrom5_4= spin5_F_4.get()
    hourOn5_4=spin5_A_4.get()
    minOn5_4=spin5_B_4.get()
    hourOff5_4=spin5_C_4.get()
    minOff5_4=spin5_D_4.get() 

    tcycle_5_4 = int(tcyclespinbox_arr[4,3].get())
  
    hourOn5_4 = time_to_str(hourOn5_4)    
    minOn5_4 = time_to_str(minOn5_4)
    hourOff5_4=time_to_str(hourOff5_4)
    minOff5_4=time_to_str(minOff5_4)
    
    tcycle_5_4=time_to_str(tcycle_5_4)

    date5_4 = time_to_str(date5_4)
    month5_4 = time_to_str(month5_4)
    year5_4 = time_to_str(year5_4)

    if var5_4.get()==1:
        dark5_4='0'
        light5_4='0'
    if var5_4.get()==2:
        dark5_4='1'
        light5_4='0'
    if var5_4.get()==3:
        dark5_4='0'
        light5_4='1'
    
    #phase 5
    
    global date5_5, month5_5, year5_5, hourFrom5_5, minuteFrom5_5, hourOn5_5, minOn5_5, hourOff5_5, minOff5_5, dark5_5, light5_5, tcycle_5_5
    date5_5 = date5_5_entry.get()
    month5_5 = month5_5_entry.get()
    year5_5 = year5_5_entry.get()
    hourFrom5_5= spin5_E_5.get()
    minuteFrom5_5= spin5_F_5.get()
    hourOn5_5=spin5_A_5.get()
    minOn5_5=spin5_B_5.get()
    hourOff5_5=spin5_C_5.get()
    minOff5_5=spin5_D_5.get()  

    tcycle_5_5 = int(tcyclespinbox_arr[4,4].get())
   
    hourOn5_5 = time_to_str(hourOn5_5)    
    minOn5_5 = time_to_str(minOn5_5)
    hourOff5_5 = time_to_str(hourOff5_5)
    minOff5_5 = time_to_str(minOff5_5)
    
    tcycle_5_5 =time_to_str(tcycle_5_5)

    date5_5 = time_to_str(date5_5)
    month5_5 = time_to_str(month5_5)
    year5_5 = time_to_str(year5_5)


    if var5_5.get()==1:
        dark5_5='0'
        light5_5='0'
    if var5_5.get()==2:
        dark5_5='1'
        light5_5='0'
    if var5_5.get()==3:
        dark5_5='0'
        light5_5='1'

    # phase 6
    global date5_6, month5_6, year5_6, hourFrom5_6, minuteFrom5_6, hourOn5_6, minOn5_6, hourOff5_6, minOff5_6, dark5_6, light5_6, tcycle_5_6
    date5_6 = date5_6_entry.get()
    month5_6 = month5_6_entry.get()
    year5_6 = year5_6_entry.get()
    hourFrom5_6= spin5_E_6.get()
    minuteFrom5_6= spin5_F_6.get()
    hourOn5_6=spin5_A_6.get()
    minOn5_6=spin5_B_6.get()
    hourOff5_6=spin5_C_6.get()
    minOff5_6=spin5_D_6.get()  

    tcycle_5_6 = int(tcyclespinbox_arr[4,5].get())
   
    hourOn5_6 = time_to_str(hourOn5_6)    
    minOn5_6 = time_to_str(minOn5_6)
    hourOff5_6=time_to_str(hourOff5_6)
    minOff5_6=time_to_str(minOff5_6)
    
    tcycle_5_6=time_to_str(tcycle_5_6)

    date5_6 = time_to_str(date5_6)
    month5_6 = time_to_str(month5_6)
    year5_6 = time_to_str(year5_6)

    if var5_6.get()==1:
        dark5_6='0'
        light5_6='0'
    if var5_6.get()==2:
        dark5_6='1'
        light5_6='0'
    if var5_6.get()==3:
        dark5_6='0'
        light5_6='1'
  
    #phase 7
    global date5_7, month5_7, year5_7, hourFrom5_7, minuteFrom5_7, hourOn5_7, minOn5_7, hourOff5_7, minOff5_7, dark5_7, light5_7, tcycle_5_7
    date5_7 = date5_7_entry.get()
    month5_7 = month5_7_entry.get()
    year5_7 = year5_7_entry.get()
    hourFrom5_7= spin5_E_7.get()
    minuteFrom5_7= spin5_F_7.get()
    hourOn5_7=spin5_A_7.get()
    minOn5_7=spin5_B_7.get()
    hourOff5_7=spin5_C_7.get()
    minOff5_7=spin5_D_7.get()

    tcycle_5_7 = int(tcyclespinbox_arr[4,6].get())
 
    hourOn5_7 = time_to_str(hourOn5_7)    
    minOn5_7 = time_to_str(minOn5_7)
    hourOff5_7=time_to_str(hourOff5_7)
    minOff5_7=time_to_str(minOff5_7)
    
    tcycle_5_7=time_to_str(tcycle_5_7)

    date5_7 = time_to_str(date5_7)
    month5_7 = time_to_str(month5_7)
    year5_7 = time_to_str(year5_7)

    if var5_7.get()==1:
        dark5_7='0'
        light5_7='0'
    if var5_7.get()==2:
        dark5_7='1'
        light5_7='0'
    if var5_7.get()==3:
        dark5_7='0'
        light5_7='1'

    #phase 8
    global date5_8, month5_8, year5_8, hourFrom5_8, minuteFrom5_8, hourOn5_8, minOn5_8, hourOff5_8, minOff5_8, dark5_8, light5_8, tcycle_5_8
    date5_8 = date5_8_entry.get()
    month5_8 = month5_8_entry.get()
    year5_8 = year5_8_entry.get()
    hourFrom5_8= spin5_E_8.get()
    minuteFrom5_8= spin5_F_8.get()
    hourOn5_8=spin5_A_8.get()
    minOn5_8=spin5_B_8.get()
    hourOff5_8=spin5_C_8.get()
    minOff5_8=spin5_D_8.get()  

    tcycle_5_8 = int(tcyclespinbox_arr[4,7].get())
  
    hourOn5_8 = time_to_str(hourOn5_8)    
    minOn5_8 = time_to_str(minOn5_8)
    hourOff5_8=time_to_str(hourOff5_8)
    minOff5_8=time_to_str(minOff5_8)
    
    tcycle_5_8=time_to_str(tcycle_5_8)

    date5_8 = time_to_str(date5_8)
    month5_8 = time_to_str(month5_8)
    year5_8 = time_to_str(year5_8)


    if var5_8.get()==1:
        dark5_8='0'
        light5_8='0'
    if var5_8.get()==2:
        dark5_8='1'
        light5_8='0'
    if var5_8.get()==3:
        dark5_8='0'
        light5_8='1'
    
    #phase 9
    global date5_9, month5_9, year5_9, hourFrom5_9, minuteFrom5_9, hourOn5_9, minOn5_9, hourOff5_9, minOff5_9, dark5_9, light5_9, tcycle_5_9
    date5_9 = date5_9_entry.get()
    month5_9 = month5_9_entry.get()
    year5_9 = year5_9_entry.get()
    hourFrom5_9= spin5_E_9.get()
    minuteFrom5_9= spin5_F_9.get()
    hourOn5_9=spin5_A_9.get()
    minOn5_9=spin5_B_9.get()
    hourOff5_9=spin5_C_9.get()
    minOff5_9=spin5_D_9.get()    

    tcycle_5_9 = int(tcyclespinbox_arr[4,8].get())
  
    hourOn5_9 = time_to_str(hourOn5_9)    
    minOn5_9 = time_to_str(minOn5_9)
    hourOff5_9=time_to_str(hourOff5_9)
    minOff5_9=time_to_str(minOff5_9)
    
    tcycle_5_9=time_to_str(tcycle_5_9)

    date5_9 = time_to_str(date5_9)
    month5_9 = time_to_str(month5_9)
    year5_9 = time_to_str(year5_9)


    if var5_9.get()==1:
        dark5_9='0'
        light5_9='0'
    if var5_9.get()==2:
        dark5_9='1'
        light5_9='0'
    if var5_9.get()==3:
        dark5_9='0'
        light5_9='1'

    #phase 10
    global date5_10, month5_10, year5_10, hourFrom5_10, minuteFrom5_10, hourOn5_10, minOn5_10, hourOff5_10, minOff5_10, dark5_10, light5_10, tcycle_5_10
    date5_10 = date5_10_entry.get()
    month5_10 = month5_10_entry.get()
    year5_10 = year5_10_entry.get()
    hourFrom5_10= spin5_E_10.get()
    minuteFrom5_10= spin5_F_10.get()
    hourOn5_10=spin5_A_10.get()
    minOn5_10=spin5_B_10.get()
    hourOff5_10=spin5_C_10.get()
    minOff5_10=spin5_D_10.get()   

    tcycle_5_10 = int(tcyclespinbox_arr[4,9].get())
  
    hourOn5_10 = time_to_str(hourOn5_10)    
    minOn5_10 = time_to_str(minOn5_10)
    hourOff5_10=time_to_str(hourOff5_10)
    minOff5_10=time_to_str(minOff5_10)
    
    tcycle_5_10 = time_to_str(tcycle_5_10)

    date5_10 = time_to_str(date5_10)
    month5_10 = time_to_str(month5_10)
    year5_10 = time_to_str(year5_10)


    if var5_10.get()==1:
        dark5_10='0'
        light5_10='0'
    if var5_10.get()==2:
        dark5_10='1'
        light5_10='0'
    if var5_10.get()==3:
        dark5_10='0'
        light5_10='1'

    #phase 11
    global date5_11, month5_11, year5_11, hourFrom5_11, minuteFrom5_11, hourOn5_11, minOn5_11, hourOff5_11, minOff5_11, dark5_11, light5_11, tcycle_5_11
    
    date5_11 = date5_11_entry.get()
    month5_11 = month5_11_entry.get()
    year5_11 = year5_11_entry.get()
    hourFrom5_11= spin5_E_11.get()
    minuteFrom5_11= spin5_F_11.get()
    hourOn5_11=spin5_A_11.get()
    minOn5_11=spin5_B_11.get()
    hourOff5_11=spin5_C_11.get()
    minOff5_11=spin5_D_11.get() 

    tcycle_5_11 = int(tcyclespinbox_arr[4,10].get())
  
    hourOn5_11 = time_to_str(hourOn5_11)    
    minOn5_11 = time_to_str(minOn5_11)
    hourOff5_11=time_to_str(hourOff5_11)
    minOff5_11=time_to_str(minOff5_11)
    
    tcycle_5_11=time_to_str(tcycle_5_11)

    date5_11 = time_to_str(date5_11)
    month5_11 = time_to_str(month5_11)
    year5_11 = time_to_str(year5_11)

    if var5_11.get()==1:
        dark5_11='0'
        light5_11='0'
    if var5_11.get()==2:
        dark5_11='1'
        light5_11='0'
    if var5_11.get()==3:
        dark5_11='0'
        light5_11='1'

    #phase 12
    global date5_12, month5_12, year5_12, hourFrom5_12, minuteFrom5_12, hourOn5_12, minOn5_12, hourOff5_12, minOff5_12, dark5_12, light5_12, tcycle_5_12
    date5_12 = date5_12_entry.get()
    month5_12 = month5_12_entry.get()
    year5_12 = year5_12_entry.get()
    hourFrom5_12= spin5_E_12.get()
    minuteFrom5_12= spin5_F_12.get()
    hourOn5_12=spin5_A_12.get()
    minOn5_12=spin5_B_12.get()
    hourOff5_12=spin5_C_12.get()
    minOff5_12=spin5_D_12.get()

    tcycle_5_12 = int(tcyclespinbox_arr[4,11].get())
 
    hourOn5_12 = time_to_str(hourOn5_12)    
    minOn5_12 = time_to_str(minOn5_12)
    hourOff5_12=time_to_str(hourOff5_12)
    minOff5_12=time_to_str(minOff5_12)
    
    tcycle_5_12=time_to_str(tcycle_5_12)

    date5_12 = time_to_str(date5_12)
    month5_12 = time_to_str(month5_12)
    year5_12 = time_to_str(year5_12)

    if var5_12.get()==1:
        dark5_12='0'
        light5_12='0'
    if var5_12.get()==2:
        dark5_12='1'
        light5_12='0'
    if var5_12.get()==3:
        dark5_12='0'
        light5_12='1'

    status.pack(side='bottom', fill='x')
    status.set('Box5 schedule is set.')


def getBox6Schedule(): 
    global setBox6, tcyclespinbox_arr
    setBox6=1
    
    global hourOn6_1, minOn6_1, hourOff6_1, minOff6_1, dark6_1, light6_1, tcycle_6_1
    hourOn6_1=spin6_A_1.get()
    minOn6_1=spin6_B_1.get()
    hourOff6_1=spin6_C_1.get()
    minOff6_1=spin6_D_1.get()        
    tcycle_6_1 = int(tcyclespinbox_arr[5,0].get())
    
    hourOn6_1 = time_to_str(hourOn6_1)
    minOn6_1 = time_to_str(minOn6_1)
    hourOff6_1=time_to_str(hourOff6_1)
    minOff6_1=time_to_str(minOff6_1)
    
    tcycle_6_1=time_to_str(tcycle_6_1)

    if var6_1.get()==1:
        dark6_1='0'
        light6_1='0'
    if var6_1.get()==2:
        dark6_1='1'
        light6_1='0'
    if var6_1.get()==3:
        dark6_1='0'
        light6_1='1'

    #Phase2
    global date6_2, month6_2, year6_2, hourFrom6_2, minuteFrom6_2, hourOn6_2, minOn6_2, hourOff6_2, minOff6_2, dark6_2, light6_2, tcycle_6_2

    date6_2 = date6_2_entry.get()
    month6_2 = month6_2_entry.get()
    year6_2 = year6_2_entry.get()
    
    hourOn6_2=spin6_A_2.get()
    minOn6_2=spin6_B_2.get()
    hourOff6_2=spin6_C_2.get()
    minOff6_2=spin6_D_2.get()     
    hourFrom6_2= spin6_E_2.get()
    minuteFrom6_2= spin6_F_2.get()

    tcycle_6_2 = int(tcyclespinbox_arr[5,1].get())
  
    hourOn6_2 = time_to_str(hourOn6_2)    
    minOn6_2 = time_to_str(minOn6_2)
    hourOff6_2=time_to_str(hourOff6_2)
    minOff6_2=time_to_str(minOff6_2)
    
    tcycle_6_2 = time_to_str(tcycle_6_2)

    date6_2 = time_to_str(date6_2)
    month6_2 = time_to_str(month6_2)
    year6_2 = time_to_str(year6_2)

    if var6_2.get()==1:
        dark6_2='0'
        light6_2='0'
    if var6_2.get()==2:
        dark6_2='1'
        light6_2='0'
    if var6_2.get()==3:
        dark6_2='0'
        light6_2='1'

    #phase3
    
    global date6_3, month6_3, year6_3, hourFrom6_3, minuteFrom6_3, hourOn6_3, minOn6_3, hourOff6_3, minOff6_3, dark6_3, light6_3, tcycle_6_3

    date6_3 = date6_3_entry.get()
    month6_3 = month6_3_entry.get()
    year6_3 = year6_3_entry.get()

    hourFrom6_3= spin6_E_3.get()
    minuteFrom6_3= spin6_F_3.get()
    hourOn6_3=spin6_A_3.get()
    minOn6_3=spin6_B_3.get()
    hourOff6_3=spin6_C_3.get()
    minOff6_3=spin6_D_3.get()   

    tcycle_6_3 = int(tcyclespinbox_arr[5,2].get())
  
    hourOn6_3 = time_to_str(hourOn6_3)    
    minOn6_3 = time_to_str(minOn6_3)
    hourOff6_3=time_to_str(hourOff6_3)
    minOff6_3=time_to_str(minOff6_3)
    
    tcycle_6_3 = time_to_str(tcycle_6_3)
    
    date6_3 = time_to_str(date6_3)
    month6_3 = time_to_str(month6_3)
    year6_3 = time_to_str(year6_3)


    if var6_3.get()==1:
        dark6_3='0'
        light6_3='0'
    if var6_3.get()==2:
        dark6_3='1'
        light6_3='0'
    if var6_3.get()==3:
        dark6_3='0'
        light6_3='1'
    
    #phase4

    global date6_4, month6_4, year6_4, hourFrom6_4, minuteFrom6_4, hourOn6_4, minOn6_4, hourOff6_4, minOff6_4, dark6_4, light6_4, tcycle_6_4
    
    date6_4 = date6_4_entry.get()
    month6_4 = month6_4_entry.get()
    year6_4 = year6_4_entry.get()

    hourFrom6_4= spin6_E_4.get()
    minuteFrom6_4= spin6_F_4.get()
    hourOn6_4=spin6_A_4.get()
    minOn6_4=spin6_B_4.get()
    hourOff6_4=spin6_C_4.get()
    minOff6_4=spin6_D_4.get() 

    tcycle_6_4 = int(tcyclespinbox_arr[5,3].get())
  
    hourOn6_4 = time_to_str(hourOn6_4)    
    minOn6_4 = time_to_str(minOn6_4)
    hourOff6_4=time_to_str(hourOff6_4)
    minOff6_4=time_to_str(minOff6_4)
    
    tcycle_6_4=time_to_str(tcycle_6_4)

    date6_4 = time_to_str(date6_4)
    month6_4 = time_to_str(month6_4)
    year6_4 = time_to_str(year6_4)

    if var6_4.get()==1:
        dark6_4='0'
        light6_4='0'
    if var6_4.get()==2:
        dark6_4='1'
        light6_4='0'
    if var6_4.get()==3:
        dark6_4='0'
        light6_4='1'
    
    #phase 5
    
    global date6_5, month6_5, year6_5, hourFrom6_5, minuteFrom6_5, hourOn6_5, minOn6_5, hourOff6_5, minOff6_5, dark6_5, light6_5, tcycle_6_5
    date6_5 = date6_5_entry.get()
    month6_5 = month6_5_entry.get()
    year6_5 = year6_5_entry.get()
    hourFrom6_5= spin6_E_5.get()
    minuteFrom6_5= spin6_F_5.get()
    hourOn6_5=spin6_A_5.get()
    minOn6_5=spin6_B_5.get()
    hourOff6_5=spin6_C_5.get()
    minOff6_5=spin6_D_5.get()  

    tcycle_6_5 = int(tcyclespinbox_arr[5,4].get())
   
    hourOn6_5 = time_to_str(hourOn6_5)    
    minOn6_5 = time_to_str(minOn6_5)
    hourOff6_5 = time_to_str(hourOff6_5)
    minOff6_5 = time_to_str(minOff6_5)
    
    tcycle_6_5 =time_to_str(tcycle_6_5)

    date6_5 = time_to_str(date6_5)
    month6_5 = time_to_str(month6_5)
    year6_5 = time_to_str(year6_5)


    if var6_5.get()==1:
        dark6_5='0'
        light6_5='0'
    if var6_5.get()==2:
        dark6_5='1'
        light6_5='0'
    if var6_5.get()==3:
        dark6_5='0'
        light6_5='1'

    # phase 6
    global date6_6, month6_6, year6_6, hourFrom6_6, minuteFrom6_6, hourOn6_6, minOn6_6, hourOff6_6, minOff6_6, dark6_6, light6_6, tcycle_6_6
    date6_6 = date6_6_entry.get()
    month6_6 = month6_6_entry.get()
    year6_6 = year6_6_entry.get()
    hourFrom6_6= spin6_E_6.get()
    minuteFrom6_6= spin6_F_6.get()
    hourOn6_6=spin6_A_6.get()
    minOn6_6=spin6_B_6.get()
    hourOff6_6=spin6_C_6.get()
    minOff6_6=spin6_D_6.get()  

    tcycle_6_6 = int(tcyclespinbox_arr[5,5].get())
   
    hourOn6_6 = time_to_str(hourOn6_6)    
    minOn6_6 = time_to_str(minOn6_6)
    hourOff6_6=time_to_str(hourOff6_6)
    minOff6_6=time_to_str(minOff6_6)
    
    tcycle_6_6=time_to_str(tcycle_6_6)

    date6_6 = time_to_str(date6_6)
    month6_6 = time_to_str(month6_6)
    year6_6 = time_to_str(year6_6)

    if var6_6.get()==1:
        dark6_6='0'
        light6_6='0'
    if var6_6.get()==2:
        dark6_6='1'
        light6_6='0'
    if var6_6.get()==3:
        dark6_6='0'
        light6_6='1'
  
    #phase 7
    global date6_7, month6_7, year6_7, hourFrom6_7, minuteFrom6_7, hourOn6_7, minOn6_7, hourOff6_7, minOff6_7, dark6_7, light6_7, tcycle_6_7
    date6_7 = date6_7_entry.get()
    month6_7 = month6_7_entry.get()
    year6_7 = year6_7_entry.get()
    hourFrom6_7= spin6_E_7.get()
    minuteFrom6_7= spin6_F_7.get()
    hourOn6_7=spin6_A_7.get()
    minOn6_7=spin6_B_7.get()
    hourOff6_7=spin6_C_7.get()
    minOff6_7=spin6_D_7.get()

    tcycle_6_7 = int(tcyclespinbox_arr[5,6].get())
 
    hourOn6_7 = time_to_str(hourOn6_7)    
    minOn6_7 = time_to_str(minOn6_7)
    hourOff6_7=time_to_str(hourOff6_7)
    minOff6_7=time_to_str(minOff6_7)
    
    tcycle_6_7=time_to_str(tcycle_6_7)

    date6_7 = time_to_str(date6_7)
    month6_7 = time_to_str(month6_7)
    year6_7 = time_to_str(year6_7)

    if var6_7.get()==1:
        dark6_7='0'
        light6_7='0'
    if var6_7.get()==2:
        dark6_7='1'
        light6_7='0'
    if var6_7.get()==3:
        dark6_7='0'
        light6_7='1'

    #phase 8
    global date6_8, month6_8, year6_8, hourFrom6_8, minuteFrom6_8, hourOn6_8, minOn6_8, hourOff6_8, minOff6_8, dark6_8, light6_8, tcycle_6_8
    date6_8 = date6_8_entry.get()
    month6_8 = month6_8_entry.get()
    year6_8 = year6_8_entry.get()
    hourFrom6_8= spin6_E_8.get()
    minuteFrom6_8= spin6_F_8.get()
    hourOn6_8=spin6_A_8.get()
    minOn6_8=spin6_B_8.get()
    hourOff6_8=spin6_C_8.get()
    minOff6_8=spin6_D_8.get()  

    tcycle_6_8 = int(tcyclespinbox_arr[5,7].get())
  
    hourOn6_8 = time_to_str(hourOn6_8)    
    minOn6_8 = time_to_str(minOn6_8)
    hourOff6_8=time_to_str(hourOff6_8)
    minOff6_8=time_to_str(minOff6_8)
    
    tcycle_6_8=time_to_str(tcycle_6_8)

    date6_8 = time_to_str(date6_8)
    month6_8 = time_to_str(month6_8)
    year6_8 = time_to_str(year6_8)


    if var6_8.get()==1:
        dark6_8='0'
        light6_8='0'
    if var6_8.get()==2:
        dark6_8='1'
        light6_8='0'
    if var6_8.get()==3:
        dark6_8='0'
        light6_8='1'
    
    #phase 9
    global date6_9, month6_9, year6_9, hourFrom6_9, minuteFrom6_9, hourOn6_9, minOn6_9, hourOff6_9, minOff6_9, dark6_9, light6_9, tcycle_6_9
    date6_9 = date6_9_entry.get()
    month6_9 = month6_9_entry.get()
    year6_9 = year6_9_entry.get()
    hourFrom6_9= spin6_E_9.get()
    minuteFrom6_9= spin6_F_9.get()
    hourOn6_9=spin6_A_9.get()
    minOn6_9=spin6_B_9.get()
    hourOff6_9=spin6_C_9.get()
    minOff6_9=spin6_D_9.get()    

    tcycle_6_9 = int(tcyclespinbox_arr[5,8].get())
  
    hourOn6_9 = time_to_str(hourOn6_9)    
    minOn6_9 = time_to_str(minOn6_9)
    hourOff6_9=time_to_str(hourOff6_9)
    minOff6_9=time_to_str(minOff6_9)
    
    tcycle_6_9=time_to_str(tcycle_6_9)

    date6_9 = time_to_str(date6_9)
    month6_9 = time_to_str(month6_9)
    year6_9 = time_to_str(year6_9)


    if var6_9.get()==1:
        dark6_9='0'
        light6_9='0'
    if var6_9.get()==2:
        dark6_9='1'
        light6_9='0'
    if var6_9.get()==3:
        dark6_9='0'
        light6_9='1'

    #phase 10
    global date6_10, month6_10, year6_10, hourFrom6_10, minuteFrom6_10, hourOn6_10, minOn6_10, hourOff6_10, minOff6_10, dark6_10, light6_10, tcycle_6_10
    date6_10 = date6_10_entry.get()
    month6_10 = month6_10_entry.get()
    year6_10 = year6_10_entry.get()
    hourFrom6_10= spin6_E_10.get()
    minuteFrom6_10= spin6_F_10.get()
    hourOn6_10=spin6_A_10.get()
    minOn6_10=spin6_B_10.get()
    hourOff6_10=spin6_C_10.get()
    minOff6_10=spin6_D_10.get()   

    tcycle_6_10 = int(tcyclespinbox_arr[5,9].get())
  
    hourOn6_10 = time_to_str(hourOn6_10)    
    minOn6_10 = time_to_str(minOn6_10)
    hourOff6_10=time_to_str(hourOff6_10)
    minOff6_10=time_to_str(minOff6_10)
    
    tcycle_6_10 = time_to_str(tcycle_6_10)

    date6_10 = time_to_str(date6_10)
    month6_10 = time_to_str(month6_10)
    year6_10 = time_to_str(year6_10)


    if var6_10.get()==1:
        dark6_10='0'
        light6_10='0'
    if var6_10.get()==2:
        dark6_10='1'
        light6_10='0'
    if var6_10.get()==3:
        dark6_10='0'
        light6_10='1'

    #phase 11
    global date6_11, month6_11, year6_11, hourFrom6_11, minuteFrom6_11, hourOn6_11, minOn6_11, hourOff6_11, minOff6_11, dark6_11, light6_11, tcycle_6_11
    
    date6_11 = date6_11_entry.get()
    month6_11 = month6_11_entry.get()
    year6_11 = year6_11_entry.get()
    hourFrom6_11= spin6_E_11.get()
    minuteFrom6_11= spin6_F_11.get()
    hourOn6_11=spin6_A_11.get()
    minOn6_11=spin6_B_11.get()
    hourOff6_11=spin6_C_11.get()
    minOff6_11=spin6_D_11.get() 

    tcycle_6_11 = int(tcyclespinbox_arr[5,10].get())
  
    hourOn6_11 = time_to_str(hourOn6_11)    
    minOn6_11 = time_to_str(minOn6_11)
    hourOff6_11=time_to_str(hourOff6_11)
    minOff6_11=time_to_str(minOff6_11)
    
    tcycle_6_11=time_to_str(tcycle_6_11)

    date6_11 = time_to_str(date6_11)
    month6_11 = time_to_str(month6_11)
    year6_11 = time_to_str(year6_11)

    if var6_11.get()==1:
        dark6_11='0'
        light6_11='0'
    if var6_11.get()==2:
        dark6_11='1'
        light6_11='0'
    if var6_11.get()==3:
        dark6_11='0'
        light6_11='1'

    #phase 12
    global date6_12, month6_12, year6_12, hourFrom6_12, minuteFrom6_12, hourOn6_12, minOn6_12, hourOff6_12, minOff6_12, dark6_12, light6_12, tcycle_6_12
    date6_12 = date6_12_entry.get()
    month6_12 = month6_12_entry.get()
    year6_12 = year6_12_entry.get()
    hourFrom6_12= spin6_E_12.get()
    minuteFrom6_12= spin6_F_12.get()
    hourOn6_12=spin6_A_12.get()
    minOn6_12=spin6_B_12.get()
    hourOff6_12=spin6_C_12.get()
    minOff6_12=spin6_D_12.get()

    tcycle_6_12 = int(tcyclespinbox_arr[5,11].get())
 
    hourOn6_12 = time_to_str(hourOn6_12)    
    minOn6_12 = time_to_str(minOn6_12)
    hourOff6_12=time_to_str(hourOff6_12)
    minOff6_12=time_to_str(minOff6_12)
    
    tcycle_6_12=time_to_str(tcycle_6_12)

    date6_12 = time_to_str(date6_12)
    month6_12 = time_to_str(month6_12)
    year6_12 = time_to_str(year6_12)

    if var6_12.get()==1:
        dark6_12='0'
        light6_12='0'
    if var6_12.get()==2:
        dark6_12='1'
        light6_12='0'
    if var6_12.get()==3:
        dark6_12='0'
        light6_12='1'

    status.pack(side='bottom', fill='x')
    status.set('Box6 schedule is set.')
    
    if setBox1+setBox2+setBox3+setBox4+setBox5+setBox6 == 6:
        btnSave['state']='normal'
        btnRun['state']='normal'  
        recordingmenu.entryconfig('Start new', state='normal')
        show_conf()
    window.update_idletasks()



def getAllBoxSchedule(): 

    global value_mat, phase_delimiters
    global initLED1_str, initLED2_str, initLED3_str, initLED4_str , initLED5_str, initLED6_str
    global initLED1, initLED2, initLED3, initLED4 , initLED5, initLED6

    getBox1Schedule()
    getBox2Schedule()
    getBox3Schedule()
    getBox4Schedule()
    getBox5Schedule()
    getBox6Schedule()

    initLED1_str = initLED1.get()
    initLED2_str = initLED2.get()
    initLED3_str = initLED3.get()
    initLED4_str = initLED4.get()
    initLED5_str = initLED5.get()
    initLED6_str = initLED6.get()

    today=datetime.date.today()
    day = today.day
    thismonth = today.month
    thisyear = today.year
    thishour = datetime.datetime.now().hour
    thismin = datetime.datetime.now().minute
    date_p2 = datetime.datetime(int(year1_2), int(month1_2), int(date1_2), int(hourFrom1_2), int(minuteFrom1_2))
    date_p3 = datetime.datetime(int(year1_3), int(month1_3), int(date1_3), int(hourFrom1_3), int(minuteFrom1_3))
    date_p4 = datetime.datetime(int(year1_4), int(month1_4), int(date1_4), int(hourFrom1_4), int(minuteFrom1_4))
    date_p5 = datetime.datetime(int(year1_5), int(month1_5), int(date1_5), int(hourFrom1_5), int(minuteFrom1_5))
    date_p6 = datetime.datetime(int(year1_6), int(month1_6), int(date1_6), int(hourFrom1_6), int(minuteFrom1_6))
    date_p7 = datetime.datetime(int(year1_7), int(month1_7), int(date1_7), int(hourFrom1_7), int(minuteFrom1_7))
    date_p8 = datetime.datetime(int(year1_8), int(month1_8), int(date1_8), int(hourFrom1_8), int(minuteFrom1_8))
    date_p9 = datetime.datetime(int(year1_9), int(month1_9), int(date1_9), int(hourFrom1_9), int(minuteFrom1_9))
    date_p10 = datetime.datetime(int(year1_10), int(month1_10), int(date1_10), int(hourFrom1_10), int(minuteFrom1_10))
    date_p11 = datetime.datetime(int(year1_11), int(month1_11), int(date1_11), int(hourFrom1_11), int(minuteFrom1_11))
    date_p12 = datetime.datetime(int(year1_12), int(month1_12), int(date1_12), int(hourFrom1_12), int(minuteFrom1_12))
    phase_delimiters = [datetime.datetime.now(), date_p2, date_p3, date_p4, date_p5, date_p6, date_p7, date_p8, date_p9, date_p10, date_p11, date_p12 ]

    value_mat = [hourOn1_1, minOn1_1, hourOff1_1, minOff1_1, dark1_1, light1_1, day,thismonth, thisyear, thishour, thismin,
    hourOn2_1, minOn2_1, hourOff2_1, minOff2_1, dark2_1, light2_1, day,thismonth, thisyear, thishour, thismin,
    hourOn3_1, minOn3_1, hourOff3_1, minOff3_1, dark3_1, light3_1,day,thismonth, thisyear, thishour, thismin,
    hourOn4_1, minOn4_1, hourOff4_1, minOff4_1, dark4_1, light4_1,day,thismonth, thisyear, thishour, thismin,
    hourOn5_1, minOn5_1, hourOff5_1, minOff5_1, dark5_1, light5_1, day,thismonth, thisyear, thishour, thismin,
    hourOn6_1, minOn6_1, hourOff6_1, minOff6_1, dark6_1, light6_1, day,thismonth, thisyear, thishour, thismin,

    hourOn1_2, minOn1_2, hourOff1_2, minOff1_2, dark1_2, light1_2, date1_2, month1_2, year1_2, hourFrom1_2, minuteFrom1_2,
    hourOn2_2, minOn2_2, hourOff2_2, minOff2_2, dark2_2, light2_2, date2_2, month2_2, year2_2, hourFrom2_2, minuteFrom2_2,
    hourOn3_2, minOn3_2, hourOff3_2, minOff3_2, dark3_2, light3_2, date3_2, month3_2, year3_2, hourFrom3_2, minuteFrom3_2,
    hourOn4_2, minOn4_2, hourOff4_2, minOff4_2, dark4_2, light4_2, date4_2, month4_2, year4_2, hourFrom4_2, minuteFrom4_2,
    hourOn5_2, minOn5_2, hourOff5_2, minOff5_2, dark5_2, light5_2, date5_2, month5_2, year5_2, hourFrom5_2, minuteFrom5_2,
    hourOn6_2, minOn6_2, hourOff6_2, minOff6_2, dark6_2, light6_2, date6_2, month6_2, year6_2, hourFrom6_2, minuteFrom6_2,

    hourOn1_3, minOn1_3, hourOff1_3, minOff1_3, dark1_3, light1_3, date1_3, month1_3, year1_3, hourFrom1_3, minuteFrom1_3,
    hourOn2_3, minOn2_3, hourOff2_3, minOff2_3, dark2_3, light2_3, date2_3, month2_3, year2_3, hourFrom2_3, minuteFrom2_3,
    hourOn3_3, minOn3_3, hourOff3_3, minOff3_3, dark3_3, light3_3, date3_3, month3_3, year3_3, hourFrom3_3, minuteFrom3_3,
    hourOn4_3, minOn4_3, hourOff4_3, minOff4_3, dark4_3, light4_3, date4_3, month4_3, year4_3, hourFrom4_3, minuteFrom4_3,
    hourOn5_3, minOn5_3, hourOff5_3, minOff5_3, dark5_3, light5_3, date5_3, month5_3, year5_3, hourFrom5_3, minuteFrom5_3,
    hourOn6_3, minOn6_3, hourOff6_3, minOff6_3, dark6_3, light6_3, date6_3, month6_3, year6_3, hourFrom6_3, minuteFrom6_3,

    hourOn1_4, minOn1_4, hourOff1_4, minOff1_4, dark1_4, light1_4, date1_4, month1_4, year1_4, hourFrom1_4, minuteFrom1_4,
    hourOn2_4, minOn2_4, hourOff2_4, minOff2_4, dark2_4, light2_4, date2_4, month2_4, year2_4, hourFrom2_4, minuteFrom2_4,
    hourOn3_4, minOn3_4, hourOff3_4, minOff3_4, dark3_4, light3_4, date3_4, month3_4, year3_4, hourFrom3_4, minuteFrom3_4,
    hourOn4_4, minOn4_4, hourOff4_4, minOff4_4, dark4_4, light4_4, date4_4, month4_4, year4_4, hourFrom4_4, minuteFrom4_4,
    hourOn5_4, minOn5_4, hourOff5_4, minOff5_4, dark5_4, light5_4, date5_4, month5_4, year5_4, hourFrom5_4, minuteFrom5_4,
    hourOn6_4, minOn6_4, hourOff6_4, minOff6_4, dark6_4, light6_4, date6_4, month6_4, year6_4, hourFrom6_4, minuteFrom6_4,

    hourOn1_5, minOn1_5, hourOff1_5, minOff1_5, dark1_5, light1_5, date1_5, month1_5, year1_5, hourFrom1_5, minuteFrom1_5,
    hourOn2_5, minOn2_5, hourOff2_5, minOff2_5, dark2_5, light2_5, date2_5, month2_5, year2_5, hourFrom2_5, minuteFrom2_5,
    hourOn3_5, minOn3_5, hourOff3_5, minOff3_5, dark3_5, light3_5, date3_5, month3_5, year3_5, hourFrom3_5, minuteFrom3_5,
    hourOn4_5, minOn4_5, hourOff4_5, minOff4_5, dark4_5, light4_5, date4_5, month4_5, year4_5, hourFrom4_5, minuteFrom4_5,
    hourOn5_5, minOn5_5, hourOff5_5, minOff5_5, dark5_5, light5_5, date5_5, month5_5, year5_5, hourFrom5_5, minuteFrom5_5,
    hourOn6_5, minOn6_5, hourOff6_5, minOff6_5, dark6_5, light6_5, date6_5, month6_5, year6_5, hourFrom6_5, minuteFrom6_5,

    hourOn1_6, minOn1_6, hourOff1_6, minOff1_6, dark1_6, light1_6, date1_6, month1_6, year1_6, hourFrom1_6, minuteFrom1_6,
    hourOn2_6, minOn2_6, hourOff2_6, minOff2_6, dark2_6, light2_6, date2_6, month2_6, year2_6, hourFrom2_6, minuteFrom2_6,
    hourOn3_6, minOn3_6, hourOff3_6, minOff3_6, dark3_6, light3_6, date3_6, month3_6, year3_6, hourFrom3_6, minuteFrom3_6,
    hourOn4_6, minOn4_6, hourOff4_6, minOff4_6, dark4_6, light4_6, date4_6, month4_6, year4_6, hourFrom4_6, minuteFrom4_6,
    hourOn5_6, minOn5_6, hourOff5_6, minOff5_6, dark5_6, light5_6, date5_6, month5_6, year5_6, hourFrom5_6, minuteFrom5_6,
    hourOn6_6, minOn6_6, hourOff6_6, minOff6_6, dark6_6, light6_6, date6_6, month6_6, year6_6, hourFrom6_6, minuteFrom6_6,

    hourOn1_7, minOn1_7, hourOff1_7, minOff1_7, dark1_7, light1_7, date1_7, month1_7, year1_7, hourFrom1_7, minuteFrom1_7,
    hourOn2_7, minOn2_7, hourOff2_7, minOff2_7, dark2_7, light2_7, date2_7, month2_7, year2_7, hourFrom2_7, minuteFrom2_7,
    hourOn3_7, minOn3_7, hourOff3_7, minOff3_7, dark3_7, light3_7, date3_7, month3_7, year3_7, hourFrom3_7, minuteFrom3_7,
    hourOn4_7, minOn4_7, hourOff4_7, minOff4_7, dark4_7, light4_7, date4_7, month4_7, year4_7, hourFrom4_7, minuteFrom4_7,
    hourOn5_7, minOn5_7, hourOff5_7, minOff5_7, dark5_7, light5_7, date5_7, month5_7, year5_7, hourFrom5_7, minuteFrom5_7,
    hourOn6_7, minOn6_7, hourOff6_7, minOff6_7, dark6_7, light6_7, date6_7, month6_7, year6_7, hourFrom6_7, minuteFrom6_7,

    hourOn1_8, minOn1_8, hourOff1_8, minOff1_8, dark1_8, light1_8, date1_8, month1_8, year1_8, hourFrom1_8, minuteFrom1_8,
    hourOn2_8, minOn2_8, hourOff2_8, minOff2_8, dark2_8, light2_8, date2_8, month2_8, year2_8, hourFrom2_8, minuteFrom2_8,
    hourOn3_8, minOn3_8, hourOff3_8, minOff3_8, dark3_8, light3_8, date3_8, month3_8, year3_8, hourFrom3_8, minuteFrom3_8,
    hourOn4_8, minOn4_8, hourOff4_8, minOff4_8, dark4_8, light4_8, date4_8, month4_8, year4_8, hourFrom4_8, minuteFrom4_8,
    hourOn5_8, minOn5_8, hourOff5_8, minOff5_8, dark5_8, light5_8, date5_8, month5_8, year5_8, hourFrom5_8, minuteFrom5_8,
    hourOn6_8, minOn6_8, hourOff6_8, minOff6_8, dark6_8, light6_8, date6_8, month6_8, year6_8, hourFrom6_8, minuteFrom6_8,

    hourOn1_9, minOn1_9, hourOff1_9, minOff1_9, dark1_9, light1_9, date1_9, month1_9, year1_9, hourFrom1_9, minuteFrom1_9,
    hourOn2_9, minOn2_9, hourOff2_9, minOff2_9, dark2_9, light2_9, date2_9, month2_9, year2_9, hourFrom2_9, minuteFrom2_9,
    hourOn3_9, minOn3_9, hourOff3_9, minOff3_9, dark3_9, light3_9, date3_9, month3_9, year3_9, hourFrom3_9, minuteFrom3_9,
    hourOn4_9, minOn4_9, hourOff4_9, minOff4_9, dark4_9, light4_9, date4_9, month4_9, year4_9, hourFrom4_9, minuteFrom4_9,
    hourOn5_9, minOn5_9, hourOff5_9, minOff5_9, dark5_9, light5_9, date5_9, month5_9, year5_9, hourFrom5_9, minuteFrom5_9,
    hourOn6_9, minOn6_9, hourOff6_9, minOff6_9, dark6_9, light6_9, date6_9, month6_9, year6_9, hourFrom6_9, minuteFrom6_9,

    hourOn1_10, minOn1_10, hourOff1_10, minOff1_10, dark1_10, light1_10, date1_10, month1_10, year1_10, hourFrom1_10, minuteFrom1_10,
    hourOn2_10, minOn2_10, hourOff2_10, minOff2_10, dark2_10, light2_10, date2_10, month2_10, year2_10, hourFrom2_10, minuteFrom2_10,
    hourOn3_10, minOn3_10, hourOff3_10, minOff3_10, dark3_10, light3_10, date3_10, month3_10, year3_10, hourFrom3_10, minuteFrom3_10,
    hourOn4_10, minOn4_10, hourOff4_10, minOff4_10, dark4_10, light4_10, date4_10, month4_10, year4_10, hourFrom4_10, minuteFrom4_10,
    hourOn5_10, minOn5_10, hourOff5_10, minOff5_10, dark5_10, light5_10, date5_10, month5_10, year5_10, hourFrom5_10, minuteFrom5_10,
    hourOn6_10, minOn6_10, hourOff6_10, minOff6_10, dark6_10, light6_10, date6_10, month6_10, year6_10, hourFrom6_10, minuteFrom6_10,

    hourOn1_11, minOn1_11, hourOff1_11, minOff1_11, dark1_11, light1_11, date1_11, month1_11, year1_11, hourFrom1_11, minuteFrom1_11,
    hourOn2_11, minOn2_11, hourOff2_11, minOff2_11, dark2_11, light2_11, date2_11, month2_11, year2_11, hourFrom2_11, minuteFrom2_11,
    hourOn3_11, minOn3_11, hourOff3_11, minOff3_11, dark3_11, light3_11, date3_11, month3_11, year3_11, hourFrom3_11, minuteFrom3_11,
    hourOn4_11, minOn4_11, hourOff4_11, minOff4_11, dark4_11, light4_11, date4_11, month4_11, year4_11, hourFrom4_11, minuteFrom4_11,
    hourOn5_11, minOn5_11, hourOff5_11, minOff5_11, dark5_11, light5_11, date5_11, month5_11, year5_11, hourFrom5_11, minuteFrom5_11,
    hourOn6_11, minOn6_11, hourOff6_11, minOff6_11, dark6_11, light6_11, date6_11, month6_11, year6_11, hourFrom6_11, minuteFrom6_11,

    hourOn1_12, minOn1_12, hourOff1_12, minOff1_12, dark1_12, light1_12, date1_12, month1_12, year1_12, hourFrom1_12, minuteFrom1_12,
    hourOn2_12, minOn2_12, hourOff2_12, minOff2_12, dark2_12, light2_12, date2_12, month2_12, year2_12, hourFrom2_12, minuteFrom2_12,
    hourOn3_12, minOn3_12, hourOff3_12, minOff3_12, dark3_12, light3_12, date3_12, month3_12, year3_12, hourFrom3_12, minuteFrom3_12,
    hourOn4_12, minOn4_12, hourOff4_12, minOff4_12, dark4_12, light4_12, date4_12, month4_12, year4_12, hourFrom4_12, minuteFrom4_12,
    hourOn5_12, minOn5_12, hourOff5_12, minOff5_12, dark5_12, light5_12, date5_12, month5_12, year5_12, hourFrom5_12, minuteFrom5_12,
    hourOn6_12, minOn6_12, hourOff6_12, minOff6_12, dark6_12, light6_12, date6_12, month6_12, year6_12, hourFrom6_12, minuteFrom6_12]

    
    value_mat = np.asarray(value_mat)
    
    value_mat = value_mat.reshape(6,12,11)

    #np.save("value_mat.npy", value_mat)

    status.pack(side='bottom', fill='x')
    status.set('Schedules for all boxes are set.')
    show_conf()
    btnSave['state']='normal'
    btnRun['state']='normal'
    recordingmenu.entryconfig('Start new', state='normal')
    window.update_idletasks()



def copyScheduletoAll(tab_index):
    global value_mat, input_mat

    current_frame = tab_index
    
    if current_frame == 1:
        temp_savedBoxSchedule = copyBox1()
    elif current_frame == 2:
        temp_savedBoxSchedule = copyBox2()
    elif current_frame == 3:
        temp_savedBoxSchedule = copyBox3()
    elif current_frame == 4:
        temp_savedBoxSchedule = copyBox4()
    elif current_frame == 5:
        temp_savedBoxSchedule = copyBox5()
    elif current_frame == 6:
        temp_savedBoxSchedule = copyBox6()
    elif current_frame == 7:
        pass
    
    
    for ind in range(1,7):
        temp_savedBoxSchedule.pasteSchedule(ind, input_mat) #box_index_to be pasted, global_mat
   

def copyBox1():
    temp_savedBoxSchedule = BoxSchedule()
    #fix minute columns
    #PhaseSchedule(hourOn, minOn, hourOff, minOff, dark, light, date, month, year, hourFrom, minuteFrom #add 12 phases
    # global array: hourOn1_2, minOn1_2, hourOff1_2, minOff1_2, dark1_2, light1_2, date1_2, month1_2, year1_2, hourFrom1_2, minuteFrom1_2,
    temp_savedBoxSchedule.addPhase1(spin1_A_1.get(),spin1_B_1.get(),spin1_C_1.get(),spin1_D_1.get(), var1_1) #Phase 1 has less vars
    temp_savedBoxSchedule.addPhase(hourOn = spin1_A_2.get(), minOn= spin1_B_2.get(), hourOff = spin1_C_2.get(), minOff = spin1_D_2.get(), var=var1_2, date = date1_2_entry.get(), month =  month1_2_entry.get(),year =year1_2_entry.get(), hourFrom= spin1_E_2.get(),  minuteFrom = spin1_F_2.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin1_A_3.get(), minOn= spin1_B_3.get(), hourOff = spin1_C_3.get(), minOff = spin1_D_3.get(), var=var1_3, date = date1_3_entry.get(), month =  month1_3_entry.get(),year =year1_3_entry.get(), hourFrom= spin1_E_3.get(),  minuteFrom = spin1_F_3.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin1_A_4.get(), minOn= spin1_B_4.get(), hourOff = spin1_C_4.get(), minOff = spin1_D_4.get(), var=var1_4, date = date1_4_entry.get(), month =  month1_4_entry.get(),year =year1_4_entry.get(), hourFrom= spin1_E_4.get(),  minuteFrom = spin1_F_4.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin1_A_5.get(), minOn= spin1_B_5.get(), hourOff = spin1_C_5.get(), minOff = spin1_D_5.get(), var=var1_5, date = date1_5_entry.get(), month =  month1_5_entry.get(),year =year1_5_entry.get(), hourFrom= spin1_E_5.get(),  minuteFrom = spin1_F_5.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin1_A_6.get(), minOn= spin1_B_6.get(), hourOff = spin1_C_6.get(), minOff = spin1_D_6.get(), var=var1_6, date = date1_6_entry.get(), month =  month1_6_entry.get(),year =year1_6_entry.get(), hourFrom= spin1_E_6.get(),  minuteFrom = spin1_F_6.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin1_A_7.get(), minOn= spin1_B_7.get(), hourOff = spin1_C_7.get(), minOff = spin1_D_7.get(), var=var1_7, date = date1_7_entry.get(), month =  month1_7_entry.get(),year =year1_7_entry.get(), hourFrom= spin1_E_7.get(),  minuteFrom = spin1_F_7.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin1_A_8.get(), minOn= spin1_B_8.get(), hourOff = spin1_C_8.get(), minOff = spin1_D_8.get(), var=var1_8, date = date1_8_entry.get(), month =  month1_8_entry.get(),year =year1_8_entry.get(), hourFrom= spin1_E_8.get(),  minuteFrom = spin1_F_8.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin1_A_9.get(), minOn= spin1_B_9.get(), hourOff = spin1_C_9.get(), minOff = spin1_D_9.get(), var=var1_9, date = date1_9_entry.get(), month =  month1_9_entry.get(),year =year1_9_entry.get(), hourFrom= spin1_E_9.get(),  minuteFrom = spin1_F_9.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin1_A_10.get(), minOn= spin1_B_10.get(), hourOff = spin1_C_10.get(), minOff = spin1_D_10.get(), var=var1_10, date = date1_10_entry.get(), month =  month1_10_entry.get(),year =year1_10_entry.get(), hourFrom= spin1_E_10.get(),  minuteFrom = spin1_F_10.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin1_A_11.get(), minOn= spin1_B_11.get(), hourOff = spin1_C_11.get(), minOff = spin1_D_11.get(), var=var1_11, date = date1_11_entry.get(), month =  month1_11_entry.get(),year =year1_11_entry.get(), hourFrom= spin1_E_11.get(),  minuteFrom = spin1_F_11.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin1_A_12.get(), minOn= spin1_B_12.get(), hourOff = spin1_C_12.get(), minOff = spin1_D_12.get(), var=var1_12, date = date1_12_entry.get(), month =  month1_12_entry.get(),year =year1_12_entry.get(), hourFrom= spin1_E_12.get(),  minuteFrom = spin1_F_12.get())
    return temp_savedBoxSchedule

def copyBox2():
    temp_savedBoxSchedule = BoxSchedule()
    #PhaseSchedule(hourOn, minOn, hourOff, minOff, dark, light, date, month, year, hourFrom, minuteFrom #add 12 phases
    temp_savedBoxSchedule.addPhase1(spin2_A_1.get(),spin2_B_1.get(),spin2_C_1.get(),spin2_D_1.get(), var2_1) #Phase 1 has less vars
    temp_savedBoxSchedule.addPhase(hourOn = spin2_A_2.get(), minOn= spin2_B_2.get(), hourOff = spin2_C_2.get(), minOff = spin2_D_2.get(), var=var2_2, date = date2_2_entry.get(), month =  month2_2_entry.get(),year =year2_2_entry.get(), hourFrom= spin2_E_2.get(),  minuteFrom = spin2_F_2.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin2_A_3.get(), minOn= spin2_B_3.get(), hourOff = spin2_C_3.get(), minOff = spin2_D_3.get(), var=var2_3, date = date2_3_entry.get(), month =  month2_3_entry.get(),year =year2_3_entry.get(), hourFrom= spin2_E_3.get(),  minuteFrom = spin2_F_3.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin2_A_4.get(), minOn= spin2_B_4.get(), hourOff = spin2_C_4.get(), minOff = spin2_D_4.get(), var=var2_4, date = date2_4_entry.get(), month =  month2_4_entry.get(),year =year2_4_entry.get(), hourFrom= spin2_E_4.get(),  minuteFrom = spin2_F_4.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin2_A_5.get(), minOn= spin2_B_5.get(), hourOff = spin2_C_5.get(), minOff = spin2_D_5.get(), var=var2_5, date = date2_5_entry.get(), month =  month2_5_entry.get(),year =year2_5_entry.get(), hourFrom= spin2_E_5.get(),  minuteFrom = spin2_F_5.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin2_A_6.get(), minOn= spin2_B_6.get(), hourOff = spin2_C_6.get(), minOff = spin2_D_6.get(), var=var2_6, date = date2_6_entry.get(), month =  month2_6_entry.get(),year =year2_6_entry.get(), hourFrom= spin2_E_6.get(),  minuteFrom = spin2_F_6.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin2_A_7.get(), minOn= spin2_B_7.get(), hourOff = spin2_C_7.get(), minOff = spin2_D_7.get(), var=var2_7, date = date2_7_entry.get(), month =  month2_7_entry.get(),year =year2_7_entry.get(), hourFrom= spin2_E_7.get(),  minuteFrom = spin2_F_7.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin2_A_8.get(), minOn= spin2_B_8.get(), hourOff = spin2_C_8.get(), minOff = spin2_D_8.get(), var=var2_8, date = date2_8_entry.get(), month =  month2_8_entry.get(),year =year2_8_entry.get(), hourFrom= spin2_E_8.get(),  minuteFrom = spin2_F_8.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin2_A_9.get(), minOn= spin2_B_9.get(), hourOff = spin2_C_9.get(), minOff = spin2_D_9.get(), var=var2_9, date = date2_9_entry.get(), month =  month2_9_entry.get(),year =year2_9_entry.get(), hourFrom= spin2_E_9.get(),  minuteFrom = spin2_F_9.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin2_A_10.get(), minOn= spin2_B_10.get(), hourOff = spin2_C_10.get(), minOff = spin2_D_10.get(), var=var2_10, date = date2_10_entry.get(), month =  month2_10_entry.get(),year =year2_10_entry.get(), hourFrom= spin2_E_10.get(),  minuteFrom = spin2_F_10.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin2_A_11.get(), minOn= spin2_B_11.get(), hourOff = spin2_C_11.get(), minOff = spin2_D_11.get(), var=var2_11, date = date2_11_entry.get(), month =  month2_11_entry.get(),year =year2_11_entry.get(), hourFrom= spin2_E_11.get(),  minuteFrom = spin2_F_11.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin2_A_12.get(), minOn= spin2_B_12.get(), hourOff = spin2_C_12.get(), minOff = spin2_D_12.get(), var=var2_12, date = date2_12_entry.get(), month =  month2_12_entry.get(),year =year2_12_entry.get(), hourFrom= spin2_E_12.get(),  minuteFrom = spin2_F_12.get())
    return temp_savedBoxSchedule

def copyBox3():
    temp_savedBoxSchedule = BoxSchedule()
    #PhaseSchedule(hourOn, minOn, hourOff, minOff, dark, light, date, month, year, hourFrom, minuteFrom #add 12 phases
    temp_savedBoxSchedule.addPhase1(spin3_A_1.get(),spin3_B_1.get(),spin3_C_1.get(),spin3_D_1.get(), var3_1) #Phase 1 has less vars
    temp_savedBoxSchedule.addPhase(hourOn = spin3_A_2.get(), minOn= spin3_B_2.get(), hourOff = spin3_C_2.get(), minOff = spin3_D_2.get(), var=var3_2, date = date3_2_entry.get(), month =  month3_2_entry.get(),year =year3_2_entry.get(), hourFrom= spin3_E_2.get(),  minuteFrom = spin3_F_2.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin3_A_3.get(), minOn= spin3_B_3.get(), hourOff = spin3_C_3.get(), minOff = spin3_D_3.get(), var=var3_3, date = date3_3_entry.get(), month =  month3_3_entry.get(),year =year3_3_entry.get(), hourFrom= spin3_E_3.get(),  minuteFrom = spin3_F_3.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin3_A_4.get(), minOn= spin3_B_4.get(), hourOff = spin3_C_4.get(), minOff = spin3_D_4.get(), var=var3_4, date = date3_4_entry.get(), month =  month3_4_entry.get(),year =year3_4_entry.get(), hourFrom= spin3_E_4.get(),  minuteFrom = spin3_F_4.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin3_A_5.get(), minOn= spin3_B_5.get(), hourOff = spin3_C_5.get(), minOff = spin3_D_5.get(), var=var3_5, date = date3_5_entry.get(), month =  month3_5_entry.get(),year =year3_5_entry.get(), hourFrom= spin3_E_5.get(),  minuteFrom = spin3_F_5.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin3_A_6.get(), minOn= spin3_B_6.get(), hourOff = spin3_C_6.get(), minOff = spin3_D_6.get(), var=var3_6, date = date3_6_entry.get(), month =  month3_6_entry.get(),year =year3_6_entry.get(), hourFrom= spin3_E_6.get(),  minuteFrom = spin3_F_6.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin3_A_7.get(), minOn= spin3_B_7.get(), hourOff = spin3_C_7.get(), minOff = spin3_D_7.get(), var=var3_7, date = date3_7_entry.get(), month =  month3_7_entry.get(),year =year3_7_entry.get(), hourFrom= spin3_E_7.get(),  minuteFrom = spin3_F_7.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin3_A_8.get(), minOn= spin3_B_8.get(), hourOff = spin3_C_8.get(), minOff = spin3_D_8.get(), var=var3_8, date = date3_8_entry.get(), month =  month3_8_entry.get(),year =year3_8_entry.get(), hourFrom= spin3_E_8.get(),  minuteFrom = spin3_F_8.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin3_A_9.get(), minOn= spin3_B_9.get(), hourOff = spin3_C_9.get(), minOff = spin3_D_9.get(), var=var3_9, date = date3_9_entry.get(), month =  month3_9_entry.get(),year =year3_9_entry.get(), hourFrom= spin3_E_9.get(),  minuteFrom = spin3_F_9.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin3_A_10.get(), minOn= spin3_B_10.get(), hourOff = spin3_C_10.get(), minOff = spin3_D_10.get(), var=var3_10, date = date3_10_entry.get(), month =  month3_10_entry.get(),year =year3_10_entry.get(), hourFrom= spin3_E_10.get(),  minuteFrom = spin3_F_10.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin3_A_11.get(), minOn= spin3_B_11.get(), hourOff = spin3_C_11.get(), minOff = spin3_D_11.get(), var=var3_11, date = date3_11_entry.get(), month =  month3_11_entry.get(),year =year3_11_entry.get(), hourFrom= spin3_E_11.get(),  minuteFrom = spin3_F_11.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin3_A_12.get(), minOn= spin3_B_12.get(), hourOff = spin3_C_12.get(), minOff = spin3_D_12.get(), var=var3_12, date = date3_12_entry.get(), month =  month3_12_entry.get(),year =year3_12_entry.get(), hourFrom= spin3_E_12.get(),  minuteFrom = spin3_F_12.get())
    return temp_savedBoxSchedule
    

def copyBox4():
    temp_savedBoxSchedule = BoxSchedule()
    #PhaseSchedule(hourOn, minOn, hourOff, minOff, dark, light, date, month, year, hourFrom, minuteFrom #add 12 phases
    temp_savedBoxSchedule.addPhase1(spin4_A_1.get(),spin4_B_1.get(),spin4_C_1.get(),spin4_D_1.get(), var4_1) #Phase 1 has less vars
    temp_savedBoxSchedule.addPhase(hourOn = spin4_A_2.get(), minOn= spin4_B_2.get(), hourOff = spin4_C_2.get(), minOff = spin4_D_2.get(), var=var4_2, date = date4_2_entry.get(), month =  month4_2_entry.get(),year =year4_2_entry.get(), hourFrom= spin4_E_2.get(),  minuteFrom = spin4_F_2.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin4_A_3.get(), minOn= spin4_B_3.get(), hourOff = spin4_C_3.get(), minOff = spin4_D_3.get(), var=var4_3, date = date4_3_entry.get(), month =  month4_3_entry.get(),year =year4_3_entry.get(), hourFrom= spin4_E_3.get(),  minuteFrom = spin4_F_3.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin4_A_4.get(), minOn= spin4_B_4.get(), hourOff = spin4_C_4.get(), minOff = spin4_D_4.get(), var=var4_4, date = date4_4_entry.get(), month =  month4_4_entry.get(),year =year4_4_entry.get(), hourFrom= spin4_E_4.get(),  minuteFrom = spin4_F_4.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin4_A_5.get(), minOn= spin4_B_5.get(), hourOff = spin4_C_5.get(), minOff = spin4_D_5.get(), var=var4_5, date = date4_5_entry.get(), month =  month4_5_entry.get(),year =year4_5_entry.get(), hourFrom= spin4_E_5.get(),  minuteFrom = spin4_F_5.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin4_A_6.get(), minOn= spin4_B_6.get(), hourOff = spin4_C_6.get(), minOff = spin4_D_6.get(), var=var4_6, date = date4_6_entry.get(), month =  month4_6_entry.get(),year =year4_6_entry.get(), hourFrom= spin4_E_6.get(),  minuteFrom = spin4_F_6.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin4_A_7.get(), minOn= spin4_B_7.get(), hourOff = spin4_C_7.get(), minOff = spin4_D_7.get(), var=var4_7, date = date4_7_entry.get(), month =  month4_7_entry.get(),year =year4_7_entry.get(), hourFrom= spin4_E_7.get(),  minuteFrom = spin4_F_7.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin4_A_8.get(), minOn= spin4_B_8.get(), hourOff = spin4_C_8.get(), minOff = spin4_D_8.get(), var=var4_8, date = date4_8_entry.get(), month =  month4_8_entry.get(),year =year4_8_entry.get(), hourFrom= spin4_E_8.get(),  minuteFrom = spin4_F_8.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin4_A_9.get(), minOn= spin4_B_9.get(), hourOff = spin4_C_9.get(), minOff = spin4_D_9.get(), var=var4_9, date = date4_9_entry.get(), month =  month4_9_entry.get(),year =year4_9_entry.get(), hourFrom= spin4_E_9.get(),  minuteFrom = spin4_F_9.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin4_A_10.get(), minOn= spin4_B_10.get(), hourOff = spin4_C_10.get(), minOff = spin4_D_10.get(), var=var4_10, date = date4_10_entry.get(), month =  month4_10_entry.get(),year =year4_10_entry.get(), hourFrom= spin4_E_10.get(),  minuteFrom = spin4_F_10.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin4_A_11.get(), minOn= spin4_B_11.get(), hourOff = spin4_C_11.get(), minOff = spin4_D_11.get(), var=var4_11, date = date4_11_entry.get(), month =  month4_11_entry.get(),year =year4_11_entry.get(), hourFrom= spin4_E_11.get(),  minuteFrom = spin4_F_11.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin4_A_12.get(), minOn= spin4_B_12.get(), hourOff = spin4_C_12.get(), minOff = spin4_D_12.get(), var=var4_12, date = date4_12_entry.get(), month =  month4_12_entry.get(),year =year4_12_entry.get(), hourFrom= spin4_E_12.get(),  minuteFrom = spin4_F_12.get())
    return temp_savedBoxSchedule


def copyBox5():
    temp_savedBoxSchedule = BoxSchedule()
    #PhaseSchedule(hourOn, minOn, hourOff, minOff, dark, light, date, month, year, hourFrom, minuteFrom #add 12 phases
    temp_savedBoxSchedule.addPhase1(spin5_A_1.get(),spin5_B_1.get(),spin5_C_1.get(),spin5_D_1.get(), var5_1) #Phase 1 has less vars
    temp_savedBoxSchedule.addPhase(hourOn = spin5_A_2.get(), minOn= spin5_B_2.get(), hourOff = spin5_C_2.get(), minOff = spin5_D_2.get(), var=var5_2, date = date5_2_entry.get(), month =  month5_2_entry.get(),year =year5_2_entry.get(), hourFrom= spin5_E_2.get(),  minuteFrom = spin5_F_2.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin5_A_3.get(), minOn= spin5_B_3.get(), hourOff = spin5_C_3.get(), minOff = spin5_D_3.get(), var=var5_3, date = date5_3_entry.get(), month =  month5_3_entry.get(),year =year5_3_entry.get(), hourFrom= spin5_E_3.get(),  minuteFrom = spin5_F_3.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin5_A_4.get(), minOn= spin5_B_4.get(), hourOff = spin5_C_4.get(), minOff = spin5_D_4.get(), var=var5_4, date = date5_4_entry.get(), month =  month5_4_entry.get(),year =year5_4_entry.get(), hourFrom= spin5_E_4.get(),  minuteFrom = spin5_F_4.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin5_A_5.get(), minOn= spin5_B_5.get(), hourOff = spin5_C_5.get(), minOff = spin5_D_5.get(), var=var5_5, date = date5_5_entry.get(), month =  month5_5_entry.get(),year =year5_5_entry.get(), hourFrom= spin5_E_5.get(),  minuteFrom = spin5_F_5.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin5_A_6.get(), minOn= spin5_B_6.get(), hourOff = spin5_C_6.get(), minOff = spin5_D_6.get(), var=var5_6, date = date5_6_entry.get(), month =  month5_6_entry.get(),year =year5_6_entry.get(), hourFrom= spin5_E_6.get(),  minuteFrom = spin5_F_6.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin5_A_7.get(), minOn= spin5_B_7.get(), hourOff = spin5_C_7.get(), minOff = spin5_D_7.get(), var=var5_7, date = date5_7_entry.get(), month =  month5_7_entry.get(),year =year5_7_entry.get(), hourFrom= spin5_E_7.get(),  minuteFrom = spin5_F_7.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin5_A_8.get(), minOn= spin5_B_8.get(), hourOff = spin5_C_8.get(), minOff = spin5_D_8.get(), var=var5_8, date = date5_8_entry.get(), month =  month5_8_entry.get(),year =year5_8_entry.get(), hourFrom= spin5_E_8.get(),  minuteFrom = spin5_F_8.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin5_A_9.get(), minOn= spin5_B_9.get(), hourOff = spin5_C_9.get(), minOff = spin5_D_9.get(), var=var5_9, date = date5_9_entry.get(), month =  month5_9_entry.get(),year =year5_9_entry.get(), hourFrom= spin5_E_9.get(),  minuteFrom = spin5_F_9.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin5_A_10.get(), minOn= spin5_B_10.get(), hourOff = spin5_C_10.get(), minOff = spin5_D_10.get(), var=var5_10, date = date5_10_entry.get(), month =  month5_10_entry.get(),year =year5_10_entry.get(), hourFrom= spin5_E_10.get(),  minuteFrom = spin5_F_10.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin5_A_11.get(), minOn= spin5_B_11.get(), hourOff = spin5_C_11.get(), minOff = spin5_D_11.get(), var=var5_11, date = date5_11_entry.get(), month =  month5_11_entry.get(),year =year5_11_entry.get(), hourFrom= spin5_E_11.get(),  minuteFrom = spin5_F_11.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin5_A_12.get(), minOn= spin5_B_12.get(), hourOff = spin5_C_12.get(), minOff = spin5_D_12.get(), var=var5_12, date = date5_12_entry.get(), month =  month5_12_entry.get(),year =year5_12_entry.get(), hourFrom= spin5_E_12.get(),  minuteFrom = spin5_F_12.get())
    return temp_savedBoxSchedule
    
def copyBox6():
    temp_savedBoxSchedule = BoxSchedule()
    #PhaseSchedule(hourOn, minOn, hourOff, minOff, dark, light, date, month, year, hourFrom, minuteFrom #add 12 phases
    temp_savedBoxSchedule.addPhase1(spin6_A_1.get(),spin6_B_1.get(),spin6_C_1.get(),spin6_D_1.get(), var6_1) #Phase 1 has less vars
    temp_savedBoxSchedule.addPhase(hourOn = spin6_A_2.get(), minOn= spin6_B_2.get(), hourOff = spin6_C_2.get(), minOff = spin6_D_2.get(), var=var6_2, date = date6_2_entry.get(), month =  month6_2_entry.get(),year =year6_2_entry.get(), hourFrom= spin6_E_2.get(),  minuteFrom = spin6_F_2.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin6_A_3.get(), minOn= spin6_B_3.get(), hourOff = spin6_C_3.get(), minOff = spin6_D_3.get(), var=var6_3, date = date6_3_entry.get(), month =  month6_3_entry.get(),year =year6_3_entry.get(), hourFrom= spin6_E_3.get(),  minuteFrom = spin6_F_3.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin6_A_4.get(), minOn= spin6_B_4.get(), hourOff = spin6_C_4.get(), minOff = spin6_D_4.get(), var=var6_4, date = date6_4_entry.get(), month =  month6_4_entry.get(),year =year6_4_entry.get(), hourFrom= spin6_E_4.get(),  minuteFrom = spin6_F_4.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin6_A_5.get(), minOn= spin6_B_5.get(), hourOff = spin6_C_5.get(), minOff = spin6_D_5.get(), var=var6_5, date = date6_5_entry.get(), month =  month6_5_entry.get(),year =year6_5_entry.get(), hourFrom= spin6_E_5.get(),  minuteFrom = spin6_F_5.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin6_A_6.get(), minOn= spin6_B_6.get(), hourOff = spin6_C_6.get(), minOff = spin6_D_6.get(), var=var6_6, date = date6_6_entry.get(), month =  month6_6_entry.get(),year =year6_6_entry.get(), hourFrom= spin6_E_6.get(),  minuteFrom = spin6_F_6.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin6_A_7.get(), minOn= spin6_B_7.get(), hourOff = spin6_C_7.get(), minOff = spin6_D_7.get(), var=var6_7, date = date6_7_entry.get(), month =  month6_7_entry.get(),year =year6_7_entry.get(), hourFrom= spin6_E_7.get(),  minuteFrom = spin6_F_7.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin6_A_8.get(), minOn= spin6_B_8.get(), hourOff = spin6_C_8.get(), minOff = spin6_D_8.get(), var=var6_8, date = date6_8_entry.get(), month =  month6_8_entry.get(),year =year6_8_entry.get(), hourFrom= spin6_E_8.get(),  minuteFrom = spin6_F_8.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin6_A_9.get(), minOn= spin6_B_9.get(), hourOff = spin6_C_9.get(), minOff = spin6_D_9.get(), var=var6_9, date = date6_9_entry.get(), month =  month6_9_entry.get(),year =year6_9_entry.get(), hourFrom= spin6_E_9.get(),  minuteFrom = spin6_F_9.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin6_A_10.get(), minOn= spin6_B_10.get(), hourOff = spin6_C_10.get(), minOff = spin6_D_10.get(), var=var6_10, date = date6_10_entry.get(), month =  month6_10_entry.get(),year =year6_10_entry.get(), hourFrom= spin6_E_10.get(),  minuteFrom = spin6_F_10.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin6_A_11.get(), minOn= spin6_B_11.get(), hourOff = spin6_C_11.get(), minOff = spin6_D_11.get(), var=var6_11, date = date6_11_entry.get(), month =  month6_11_entry.get(),year =year6_11_entry.get(), hourFrom= spin6_E_11.get(),  minuteFrom = spin6_F_11.get())
    temp_savedBoxSchedule.addPhase(hourOn = spin6_A_12.get(), minOn= spin6_B_12.get(), hourOff = spin6_C_12.get(), minOff = spin6_D_12.get(), var=var6_12, date = date6_12_entry.get(), month =  month6_12_entry.get(),year =year6_12_entry.get(), hourFrom= spin6_E_12.get(),  minuteFrom = spin6_F_12.get())
    return temp_savedBoxSchedule

def copyBoxn(n, input_mat):
    temp_savedBoxSchedule = BoxSchedule()
    
    temp_savedBoxSchedule.addPhase1(input_mat[n, 0,0],input_mat[n, 0,1], input_mat[n, 0,2], input_mat[n, 0,3], input_mat[n, 0,4],input_mat[n, 0,5])
    for phase_ind in range(1,12):
        temp_savedBoxSchedule.addPhase(*input_mat[n, phase_ind])



#START MAIN


if __name__ == '__main__':
    
    init_plot()
    #### All of the components and their positions in the GUI ####
    # You can change the design from here # 
    #, input_mat, log_mat      
    menu = Menu(window) #define menu    
    # tcyclefactor =24
  

    # Define Var to keep track of the schedule
                                    #1 for LD
                                    #2 for DD
                                    #3 for LL     
    # 1_1 = Box_Phases
      
    var1_1 = IntVar(value=1) 
    var2_1 = IntVar(value=1)
    var3_1 = IntVar(value=1)
    var4_1 = IntVar(value=1)
    var5_1 = IntVar(value=1)
    var6_1 = IntVar(value=1)

    var1_2 = IntVar(value=1)
    var2_2 = IntVar(value=1)
    var3_2 = IntVar(value=1)
    var4_2 = IntVar(value=1)
    var5_2 = IntVar(value=1)
    var6_2 = IntVar(value=1)

    var1_3 = IntVar(value=1)
    var2_3 = IntVar(value=1)
    var3_3 = IntVar(value=1)
    var4_3 = IntVar(value=1)
    var5_3 = IntVar(value=1)
    var6_3 = IntVar(value=1)

    var1_4 = IntVar(value=1)
    var2_4 = IntVar(value=1)
    var3_4 = IntVar(value=1)
    var4_4 = IntVar(value=1)
    var5_4 = IntVar(value=1)
    var6_4 = IntVar(value=1)

    var1_5 = IntVar(value=1)
    var2_5 = IntVar(value=1)
    var3_5 = IntVar(value=1)
    var4_5 = IntVar(value=1)
    var5_5 = IntVar(value=1)
    var6_5 = IntVar(value=1)
    
    var1_6 = IntVar(value=1)
    var2_6 = IntVar(value=1)
    var3_6 = IntVar(value=1)
    var4_6 = IntVar(value=1)
    var5_6 = IntVar(value=1)  
    var6_6 = IntVar(value=1)  

    var1_7 = IntVar(value=1)
    var2_7 = IntVar(value=1)
    var3_7 = IntVar(value=1)
    var4_7 = IntVar(value=1)
    var5_7 = IntVar(value=1)
    var6_7 = IntVar(value=1)

    var1_8 = IntVar(value=1)
    var2_8 = IntVar(value=1)
    var3_8 = IntVar(value=1)
    var4_8 = IntVar(value=1)
    var5_8 = IntVar(value=1)  
    var6_8 = IntVar(value=1)  

    var1_9 = IntVar(value=1)
    var2_9 = IntVar(value=1)
    var3_9 = IntVar(value=1)
    var4_9 = IntVar(value=1)
    var5_9 = IntVar(value=1)
    var6_9 = IntVar(value=1)

    var1_10 = IntVar(value=1)
    var2_10 = IntVar(value=1)
    var3_10 = IntVar(value=1)
    var4_10 = IntVar(value=1)
    var5_10 = IntVar(value=1)
    var6_10 = IntVar(value=1)

    var1_11 = IntVar(value=1)
    var2_11 = IntVar(value=1)
    var3_11 = IntVar(value=1)
    var4_11 = IntVar(value=1)
    var5_11 = IntVar(value=1)
    var6_11 = IntVar(value=1)

    var1_12 = IntVar(value=1)
    var2_12 = IntVar(value=1)
    var3_12 = IntVar(value=1)
    var4_12 = IntVar(value=1)
    var5_12 = IntVar(value=1)
    var6_12 = IntVar(value=1)

    log_mat =np.empty((120,12), dtype="<U10")
    tcyclespinbox_arr =  np.empty((6,12), dtype= object)
    
    #Create file menu
    filemenu = Menu(menu)
    filemenu.add_command(label='Load schedules', command=read_conf)
    filemenu.add_command(label='Save schedules', command=save_conf)
    filemenu.add_separator()
    filemenu.add_command(label='Quit', command=destruct)
    menu.add_cascade(label='File', menu=filemenu)
    #create setting menu
    settingmenu = Menu(menu)
    settingmenu.add_command(label='Set all boxes', command=getAllBoxSchedule)
    settingmenu.add_command(label='Show schedule', command=show_conf)
    menu.add_cascade(label='Setting', menu=settingmenu)
    #create recording menu
    recordingmenu = Menu(menu)
    recordingmenu.add_command(label='Start new', command=connect)
    recordingmenu.entryconfig('Start new', state='disabled')
    #recordingmenu.add_command(label='Start revised', command=lambda:get_data(1))
    recordingmenu.add_separator()
    recordingmenu.add_command(label='Stop', command=disconnect)
    menu.add_cascade(label='Recording', menu=recordingmenu)
    #create About menu
    aboutmenu = Menu(menu)
    aboutmenu.add_command(label='About LocoBox', command=about)
    menu.add_cascade(label='Help', menu=aboutmenu)
    window.config(menu=menu)
    #Window 900x550
    f1 = tk.Frame(window,  width=900,height=160)
    f2 = tk.Frame(window,  width=900, height=250)
    f3 = tk.Frame(window, width=900, height=70)
    canvas_status = Canvas(f2, width=900, height=250)

    def do_layout():
        f1.pack(side="top", fill="both", expand=True)
        f2.pack(side="top", fill="both", expand=True)
        f3.pack(side="top", fill="both", expand=True)


    do_layout()


    tab_control = ttk.Notebook(f1)

    tab_control.bind('<<NotebookTabChanged>>', on_tab_change_trigger)

    
    ParentFrame1 = ttk.Frame(tab_control,width=850, height=200, relief=tk.FLAT)
    ParentFrame1.pack()
    ParentFrame2 = ttk.Frame(tab_control)
    ParentFrame3 = ttk.Frame(tab_control)
    ParentFrame4 = ttk.Frame(tab_control)
    ParentFrame5 = ttk.Frame(tab_control)
    ParentFrame6 = ttk.Frame(tab_control)
    ParentFrame11 = ttk.Frame(tab_control)


    tab_control.add(ParentFrame1, text='Box1')
    tab_control.add(ParentFrame2, text='Box2')
    tab_control.add(ParentFrame3, text='Box3')
    tab_control.add(ParentFrame4, text='Box4')
    tab_control.add(ParentFrame5, text='Box5')
    tab_control.add(ParentFrame6, text='Box6')
    tab_control.add(ParentFrame11, text='Schedules')
    

    #tab1

    canvas1 = Canvas(ParentFrame1, width=900, height=220) #, highlightbackground="red", highlightthickness=2
    scroll1 = Scrollbar(ParentFrame1, orient=VERTICAL, command=canvas1.yview)
    scrollx1 = Scrollbar(ParentFrame1, orient=HORIZONTAL, command=canvas1.xview)
   
    scrollx1.grid(row=1, column=0, sticky=tk.EW)    
    canvas1.grid(row=0, column=0)
    scroll1.grid(row=0, column=1, sticky='ns')

    # scrollx1.pack(expand=1, fill=X, side=BOTTOM)window
    # scroll1.pack(side = RIGHT, fill = Y, expand=1)
    # canvas1.pack(side=LEFT,expand=True,fill=BOTH)
    canvas1.config(yscrollcommand=scroll1.set, xscrollcommand=scrollx1.set)
    
    tab1 = Frame(canvas1, width=200, height=150)#, highlightbackground="black", highlightthickness=1
    tab1.bind(
    "<Configure>",
    lambda e: canvas1.configure(
        scrollregion=canvas1.bbox("all")
        )
    )
    canvas1.create_window(400, 175, window=tab1)

#tab2
    canvas2 = Canvas(ParentFrame2, width=900, height=220, scrollregion=(0,0,900,300))
    canvas2.grid(row=0, column=0)
    scroll2 = Scrollbar(ParentFrame2, orient=VERTICAL, command=canvas2.yview)
    
    scroll2.grid(row=0, column=1, sticky='ns')
    scrollx2 = Scrollbar(ParentFrame2, orient=HORIZONTAL, command=canvas2.xview)
    scrollx2.grid(row=1, column=0, sticky=tk.EW)
    canvas2.config(yscrollcommand=scroll2.set, xscrollcommand=scrollx2.set)
    # scrollx2.pack(expand=1, fill=X, side=BOTTOM)
    # scroll2.pack(side = RIGHT, fill = Y, expand=1)
    # canvas2.pack(side=LEFT,expand=True,fill=BOTH)
    tab2 = Frame(canvas2, width=200, height=150)
    tab2.bind(
    "<Configure>",
    lambda e: canvas2.configure(
        scrollregion=canvas2.bbox("all")
        )
    )

    canvas2.create_window(400, 175, window=tab2)

#tab3
    canvas3 = Canvas(ParentFrame3, width=900, height=220, scrollregion=(0,0,900,300))
    scroll3 = Scrollbar(ParentFrame3, orient=VERTICAL, command=canvas3.yview)
    canvas3.grid(row=0, column=0)
    scroll3.grid(row=0, column=1, sticky='ns')
    scrollx3 = Scrollbar(ParentFrame3, orient=HORIZONTAL, command=canvas3.xview)
    # scrollx3.pack(expand=1, fill=X, side=BOTTOM)
    # scroll3.pack(side = RIGHT, fill = Y, expand=1)
    # canvas3.pack(side=LEFT,expand=True,fill=BOTH)
    scrollx3.grid(row=1, column=0, sticky='ew')
    canvas3.config(yscrollcommand=scroll3.set, xscrollcommand=scrollx3.set)
    tab3 = Frame(canvas3, width=200, height=150)
    tab3.bind(
    "<Configure>",
    lambda e: canvas3.configure(
        scrollregion=canvas3.bbox("all")
        )
    )
    canvas3.create_window(400, 175, window=tab3)   


#tab 4 
    canvas4 = Canvas(ParentFrame4, width=900, height=220, scrollregion=(0,0,900,300))
    scroll4 = Scrollbar(ParentFrame4, orient=VERTICAL, command=canvas4.yview)
    canvas4.grid(row=0, column=0)
    scroll4.grid(row=0, column=1, sticky='ns')
    scrollx4 = Scrollbar(ParentFrame4, orient=HORIZONTAL, command=canvas4.xview)
    scrollx4.grid(row=1, column=0, sticky='ew')
    canvas4.config(yscrollcommand=scroll4.set, xscrollcommand=scrollx4.set)
    #scrollx4.pack(expand=1, fill=X, side=BOTTOM)
    #scroll4.pack(side = RIGHT, fill = Y, expand=1)
    #canvas4.pack(side=LEFT,expand=True,fill=BOTH)
    tab4 = Frame(canvas4, width=200, height=150)
    tab4.bind(
    "<Configure>",
    lambda e: canvas4.configure(
        scrollregion=canvas4.bbox("all")
        )
    )
    canvas4.create_window(400, 175, window=tab4)


#tab 5
    canvas5 = Canvas(ParentFrame5, width=900, height=220, scrollregion=(0,0,900,300))
    scroll5 = Scrollbar(ParentFrame5, orient=VERTICAL, command=canvas5.yview)
    canvas5.grid(row=0, column=0)
    scroll5.grid(row=0, column=1, sticky='ns')
    scrollx5 = Scrollbar(ParentFrame5, orient=HORIZONTAL, command=canvas5.xview)
    scrollx5.grid(row=1, column=0, sticky='ew')
    # scrollx5.pack(expand=1, fill=X, side=BOTTOM)
    # scroll5.pack(side = RIGHT, fill = Y, expand=1)
    # canvas5.pack(side=LEFT,expand=True,fill=BOTH)
    canvas5.config(yscrollcommand=scroll5.set, xscrollcommand=scrollx5.set)
    tab5 = Frame(canvas5, width=200, height=150)
    tab5.bind(
    "<Configure>",
    lambda e: canvas5.configure(
        scrollregion=canvas5.bbox("all")
        )
    )
    canvas5.create_window(400, 175, window=tab5)
    

#tab 6
    canvas6 = Canvas(ParentFrame6, width=900, height=220, scrollregion=(0,0,900,300))
    scroll6 = Scrollbar(ParentFrame6, orient=VERTICAL, command=canvas6.yview)
    canvas6.grid(row=0, column=0)
    scroll6.grid(row=0, column=1, sticky='ns')
    scrollx6 = Scrollbar(ParentFrame6, orient=HORIZONTAL, command=canvas6.xview)
    scrollx6.grid(row=1, column=0, sticky='ew')
    # scrollx5.pack(expand=1, fill=X, side=BOTTOM)
    # scroll5.pack(side = RIGHT, fill = Y, expand=1)
    # canvas5.pack(side=LEFT,expand=True,fill=BOTH)
    canvas6.config(yscrollcommand=scroll6.set, xscrollcommand=scrollx6.set)
    tab6 = Frame(canvas6, width=200, height=150)
    tab6.bind(
    "<Configure>",
    lambda e: canvas6.configure(
        scrollregion=canvas6.bbox("all")
        )
    )
    canvas6.create_window(400, 175, window=tab6)

#schedule tab

    canvas11 = Canvas(ParentFrame11, width=900, height=220, scrollregion=(0,0,900,300)) #, highlightbackground="red", highlightthickness=2
    scroll11 = Scrollbar(ParentFrame11, orient=VERTICAL, command=canvas11.yview)
    canvas11.grid(row=0, column=0)
    scroll11.grid(row=0, column=1, sticky='ns')
    scrollx11 = Scrollbar(ParentFrame11, orient=HORIZONTAL, command=canvas11.xview)
    scrollx11.grid(row=1, column=0, sticky='ew')
   
    canvas11.config(yscrollcommand=scroll11.set, xscrollcommand=scrollx11.set)
    tab11 = Frame(canvas11, width=200, height=150)#, highlightbackground="black", highlightthickness=1
    tab11.bind(
    "<Configure>",
    lambda e: canvas11.configure(
        scrollregion=canvas11.bbox("all")
        )
    )
    canvas11.create_window(400, 175, window=tab11)
   

    #Display all available serial ports
    ports = list(serial.tools.list_ports.comports())
    openPorts = []
    for p in ports:
        print(p)
        openPorts.append(p.device)
    if len(openPorts) == 0:
        openPorts=[openPorts]
    status.pack(side='bottom', fill='x')
    status.set('Available ports: '+', '.join(map(str,openPorts)))

    yupperbtns = 2
    ymidbtns = 30
    ylowerbtns = 60

    #tcycle
    # Label(f3,text =  'T-cycle length').place(x = 40, y = 0)
    # tcyclelength = Spinbox(f3, width=5)
    # tcyclelength.place(x = 150, y = 0)
    # tcyclelength.delete(0,'end')
    # tcyclelength.insert(0,24)

    #Entry for Port, Baud, timeout, filename to save
    Label(f3,text =  'Schedule').place(x = 363, y = yupperbtns)
    Label(f3,text = 'Port').place(x = 40, y = ylowerbtns)
    Label(f3,text =  'Baud rate').place(x = 363, y = ylowerbtns)
    Label(f3,text = 'Time out').place(x= 575, y=ylowerbtns)
    Label(f3,text= 'Data').place(x=40, y=ymidbtns)
    Label(f3,text= 'Schedule file').place(x=363, y=ymidbtns)

    port_entry = Spinbox(f3,values=openPorts, width=25)
    port_entry.delete(0,'end')
    port_entry.insert(0,openPorts[0]) #first port is the default 
    port_entry.place(x = 80, y = ylowerbtns)
    baud_entry = Spinbox(f3,values=(300, 600, 1200, 2400, 4800, 9600, 14400, 19200, 28800, 38400, 57600, 115200), width=7)
    baud_entry.delete(0,'end')
    baud_entry.insert(0,'9600')    
    baud_entry.place(x = 440, y = ylowerbtns)
    timeout_entry = Entry(f3,width = 4)
    timeout_entry.place(x=635,y=ylowerbtns)
    timeout_entry.insert(0,'10')

    filename_entry = Entry(f3, width = 25)
    filename_entry.place(x=80, y=ymidbtns)
    date_string = time.strftime('%Y%m%d') # predefine a default filename with ISO date    
    filename_entry.insert(0,'BOX1-6-'+date_string+'.txt')
    configfilename_entry = Entry(f3,width = 30)
    configfilename_entry.place(x=470, y=ymidbtns)
    configfilename_entry.insert(0,'BOX1-6-sched-'+date_string+'.json')

    #SHOW STATUS
    
    
    #boxsched_stat=Label(f2, textvariable=boxsched_text, anchor=W, justify=LEFT)    
    
   

    log_text = StringVar()
    first_log = ''
    log_text.set(first_log)
    
    #log_display=Label(f2, textvariable=log_text, anchor='center', justify=LEFT)
    log_display = tkscrolled.ScrolledText(f2, height=20, width=70, bg = 'grey')
    log_display.config(state="normal")
    log_display.insert(tk.END, first_log)
    log_display.config(state="disabled")

    # Packing the actogram
    frame_acto = Frame(f2, width=300, height=500)
    frame_acto.pack()
    frame_acto.place(anchor='center', relx=0.78, rely=0.4)

    # Create an object of tkinter ImageTk
    img_acto = ImageTk.PhotoImage(Image.open("./init.png"))

    # Create a Label Widget to display the text or Image
    label_acto = Label(frame_acto, image = img_acto)
    label_acto.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)
    log_display.pack(side = LEFT)
    window.update_idletasks()


    btnSave = Button(f3, text=' Save ', command=save_conf, state='disabled')
    btnRun = Button(f3, text= ' Recording Start ', command=connect, state='disabled')
    btnSetCurrent = Button(f3,text=' Set current box ', command=lambda: OnButtonClick(int(tab_control.index('current'))+1))
    btnSetAll = Button(f3, text='Set All', command=getAllBoxSchedule)    
    btnReplicateToAll = Button(f3, text=' Replicate to All ', command= lambda: copyScheduletoAll(int(tab_control.index('current'))+1))
    btnRefresh = Button(f2, text=' Refresh actogram', command= refresh_plot)
    
  
    # if box settings of all 6 boxes are done, activate save and run buttons
    if setBox1+setBox2+setBox3+setBox4+setBox5+setBox6 == 6:
        btnSave['state']='normal'
        btnRun['state']='normal'
        
        recordingmenu.entryconfig('Start new', state='normal')
        show_conf()
        window.update_idletasks()

    if "Schedules" in tab_control.select():
        btnSetCurrent['state']='disabled'
        window.update_idletasks()
    else:
        btnSetCurrent['state']='normal'
        window.update_idletasks()

    # button positions change depending on OS


    btnRefresh.place(anchor='se', relx=0.835, rely=0.85)
    window.update_idletasks()


    if sys.platform.startswith('win'):
        btnSave.place(x=730, y= ymidbtns)
        btnRun.place(x=730, y=ylowerbtns)
        btnSetCurrent.place(x=430, y=yupperbtns)       
        btnSetAll.place(x=730, y=yupperbtns)
        btnReplicateToAll.place(x=577, y=yupperbtns)
        #btnRefresh.place(x =730, y=yupperbtns+500)

        window.update_idletasks()

    elif sys.platform.startswith('darwin'):
        btnSave.place(x=730, y= ymidbtns)
        btnRun.place(x=730, y=ylowerbtns)
        btnSetCurrent.place(x=430, y=yupperbtns)       
        btnSetAll.place(x=730, y=yupperbtns)
        btnReplicateToAll.place(x=577, y=yupperbtns)
        btnRefresh.place(x =730, y=ylowerbtns +30)
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        btnSave.place(x=730, y= ymidbtns)
        btnRun.place(x=730, y=ylowerbtns)
        btnSetCurrent.place(x=430, y=yupperbtns)       
        btnSetAll.place(x=730, y=yupperbtns)
        btnReplicateToAll.place(x=577, y=yupperbtns)
        btnRefresh.place(x =730, y=ylowerbtns +30)    
    else:
        btnSave.place(x=730, y= ymidbtns)
        btnRun.place(x=730, y=ylowerbtns)
        btnSetCurrent.place(x=430, y=yupperbtns)       
        btnSetAll.place(x=730, y=yupperbtns)
        btnReplicateToAll.place(x=577, y=yupperbtns)
        btnRefresh.place(x =730, y=ylowerbtns +30)

    row_adj = 3  # useful when a new row is added above
    boxstatusSeparator = ttk.Separator(f2, orient='horizontal').place(x=0, y=0, relwidth=1)
    runSeparator = ttk.Separator(f3, orient='horizontal').place(x=0, y=0, relwidth=1)#ttk.Separator(window, orient='horizontal') #.place(x = 363, y = ylowerbtns + 30)
    
    #runSeparator.pack(fill='x')


    # PIN LOCATION

    pinlabel1 = Label(tab1, text='PIR-LED-LUM pins')
    pinlabel1.grid(column=2, row=3, padx=1, pady=5)

    pinsep1_1 = Label(tab1, text='-')
    pinsep1_1.grid(column=8, row=3, padx=3, pady=5)

    pinsep1_2 = Label(tab1, text='-')
    pinsep1_2.grid(column=10, row=3, padx=3, pady=5)


    DIn_box1 = Spinbox(tab1,from_=00, to=99, width=3, format='%02.0f')
    DIn_box1.delete(0,'end')
    DIn_box1.insert(0,'02')
    DIn_box1.grid(column=7, row=3, pady=5)

    DOut_box1 = Spinbox(tab1,from_=00, to=99, width=3, format='%02.0f')
    DOut_box1.delete(0,'end')
    DOut_box1.insert(0,'03')
    DOut_box1.grid(column=9, row=3, pady=5)

    anIn_box1 = Spinbox(tab1,from_=0, to=9, width=2, format='%01.0f')
    anIn_box1.delete(0,'end')
    anIn_box1.insert(0,1)
    anIn_box1.grid(column=11, row=3, pady=5)


    #INIT LED
    initLED1 = IntVar(value=0)
    rad_ON1 = Radiobutton(tab1, text='ON', variable=initLED1, value=1)
    rad_OFF1 = Radiobutton(tab1, text='OFF', variable=initLED1, value=0)
    rad_ON1.grid(column=9, row=1+row_adj, padx=15, pady=5)
    rad_OFF1.grid(column=11, row=1+row_adj, pady=5)

    initLED2 = IntVar(value=0)
    rad_ON2 = Radiobutton(tab2, text='ON', variable=initLED2, value=1)
    rad_OFF2 = Radiobutton(tab2, text='OFF', variable=initLED2, value=0)
    rad_ON2.grid(column=9, row=1+row_adj, padx=15, pady=5)
    rad_OFF2.grid(column=11, row=1+row_adj, pady=5)

    initLED3 = IntVar(value=0)
    rad_ON3 = Radiobutton(tab3, text='ON', variable=initLED3, value=1)
    rad_OFF3 = Radiobutton(tab3, text='OFF', variable=initLED3, value=0)
    rad_ON3.grid(column=9, row=1+row_adj, padx=15, pady=5)
    rad_OFF3.grid(column=11, row=1+row_adj, pady=5)

    initLED4 = IntVar(value=0)
    rad_ON4 = Radiobutton(tab4, text='ON', variable=initLED4, value=1)
    rad_OFF4 = Radiobutton(tab4, text='OFF', variable=initLED4, value=0)
    rad_ON4.grid(column=9, row=1+row_adj, padx=15, pady=5)
    rad_OFF4.grid(column=11, row=1+row_adj, pady=5)

    initLED5 = IntVar(value=0)
    rad_ON5 = Radiobutton(tab5, text='ON', variable=initLED5, value=1)
    rad_OFF5 = Radiobutton(tab5, text='OFF', variable=initLED5, value=0)
    rad_ON5.grid(column=9, row=1+row_adj, padx=15, pady=5)
    rad_OFF5.grid(column=11, row=1+row_adj, pady=5)

    initLED6 = IntVar(value=0)
    rad_ON6 = Radiobutton(tab6, text='ON', variable=initLED6, value=1)
    rad_OFF6 = Radiobutton(tab6, text='OFF', variable=initLED6, value=0)
    rad_ON6.grid(column=9, row=1+row_adj, padx=15, pady=5)
    rad_OFF6.grid(column=11, row=1+row_adj, pady=5)

    initLEDlabel1 = Label(tab1, text='Initial LED')
    initLEDlabel1.grid(column=7, row=1+row_adj, padx=13, pady=5)

    initLEDlabel2 = Label(tab2, text='Initial LED')
    initLEDlabel2.grid(column=7, row=1+row_adj, padx=13, pady=5)

    initLEDlabel3 = Label(tab3, text='Initial LED')
    initLEDlabel3.grid(column=7, row=1+row_adj, padx=13, pady=5)

    initLEDlabel4 = Label(tab4, text='Initial LED')
    initLEDlabel4.grid(column=7, row=1+row_adj, padx=13, pady=5)

    initLEDlabel5 = Label(tab5, text='Initial LED')
    initLEDlabel5.grid(column=7, row=1+row_adj, padx=13, pady=5)

    initLEDlabel6 = Label(tab6, text='Initial LED')
    initLEDlabel6.grid(column=7, row=1+row_adj, padx=13, pady=5)

 # Box1 main

    for i in range(0,12):
        tcyclelength = Spinbox(tab1,from_=12, to=48, width=3)

        tcyclelength.grid(column=26, row=2+i+row_adj, pady=5)
        tcyclelength.delete(0,'end')
        tcyclelength.insert(0,24)
        tcyclespinbox_arr[0,i] = tcyclelength
    
    tcyclespinbox_arr[0,0].grid(column=26, row=1+row_adj, pady=5)

    tcyclelabel = Label(tab1, text='T-cycle length')
    tcyclelabel.grid(column=26, row=1, padx=3, pady=5)
    
    tab1_title = Label(tab1, text= 'LED schedule', anchor='center')
    tab1_title.grid(column=12, row= 1, columnspan='27', sticky='we')
    #capSep1 = ttk.Separator(tab1, orient=HORIZONTAL)
    #capSep1.grid(column=0, row = row_adj+5, columnspan='27', sticky='we')
    box1sched_text=StringVar()
    box1sched_text.set('Schedule not set.')
    box1sched_stat=Label(tab1, textvariable=box1sched_text, anchor=W, justify=LEFT)
        # phase 1
    phaseLabel1_1 = Label(tab1, text='Phase 1')
    dateLabel = time.strftime('%H:%M   %Y/%m/%d') # reads time for Phase 1 start-time
    fromLabel1_1 = Label(tab1, text='From:')
    date_label1 = Label(tab1, text=dateLabel)
    rad1_A_1 = Radiobutton(tab1, text='LD', variable=var1_1, value=1)
    lbl1_A_1 = Label(tab1, text= 'On:')
    spin1_A_1 = Spinbox(tab1, from_=00, to=24, width=3, format='%02.0f')
    spin1_B_1 = Spinbox(tab1, from_=00, to=59, width=3, format='%02.0f')
    spin1_A_1.delete(0,'end')
    spin1_A_1.insert(0,'07')
    spin1_B_1.delete(0,'end')
    spin1_B_1.insert(0,'00')
    label1_h1_1 = Label(tab1, text=':')
    label1_m1_1 = Label(tab1, text='')
    lbl1_B_1 = Label(tab1, text= 'Off:')
    spin1_C_1 = Spinbox(tab1, from_=00, to=24, width=3, format='%02.0f')
    spin1_D_1 = Spinbox(tab1, from_=00, to=59, width=3, format='%02.0f')
    spin1_C_1.delete(0,'end')
    spin1_C_1.insert(0,'19')
    spin1_D_1.delete(0,'end')
    spin1_D_1.insert(0,'00')
    label1_h2_1 = Label(tab1, text=':')
    label1_m2_1 = Label(tab1, text='')
    rad1_B_1 = Radiobutton(tab1, text='DD', variable=var1_1, value=2)
    rad1_C_1 = Radiobutton(tab1, text='LL', variable=var1_1, value=3)
    phaseLabel1_1.grid(column=0, row=1+row_adj, padx=15, pady=5)
    fromLabel1_1.grid(column=1,row=1+row_adj)
    date_label1.grid(column=2, row=1+row_adj, columnspan='10', sticky='w')
    rad1_A_1.grid(column=13, row=1+row_adj, pady=5)
    lbl1_A_1.grid(column=14, row=1+row_adj, pady=5)
    spin1_A_1.grid(column=15, row=1+row_adj, pady=5)
    label1_h1_1.grid(column=16, row=1+row_adj, pady=5, sticky='w')
    spin1_B_1.grid(column=17, row=1+row_adj, pady=5)
    label1_m1_1.grid(column=18, row=1+row_adj, pady=5, sticky='w')
    lbl1_B_1.grid(column=19, row=1+row_adj, pady=5)
    spin1_C_1.grid(column=20, row=1+row_adj, pady=5)
    label1_h2_1.grid(column=21, row=1+row_adj, pady=5, sticky='w')
    spin1_D_1.grid(column=22, row=1+row_adj, pady=5)
    label1_m2_1.grid(column=23, row=1+row_adj, pady=5, sticky='w')
    rad1_B_1.grid(column=24, row=1+row_adj, padx=15, pady=5)
    rad1_C_1.grid(column=25, row=1+row_adj, pady=5)



        # phase 2
    phaseLabel1_2 = Label(tab1, text='Phase 2')
    fromLabel1_2 = Label(tab1, text='From:')
    space1_2 = Label(tab1, text=' ')
    space1_2_2 = Label(tab1, text=' ')
    spin1_E_2 = Spinbox(tab1, from_=00, to=24, width=3, format='%02.0f')
    spin1_F_2 = Spinbox(tab1, from_=00, to=59, width=3, format='%02.0f')
    spin1_E_2.delete(0,'end')
    spin1_E_2.insert(0,'07')
    spin1_F_2.delete(0,'end')
    spin1_F_2.insert(0,'00')
    label1_h0_2 = Label(tab1, text=':')
    label1_m0_2 = Label(tab1, text='')
    
    date1_2_entry = Spinbox(tab1, from_=00, to=31, width=3, format='%02.0f') #, textvariable=defaultVarDate1_2
    month1_2_entry = Spinbox(tab1, from_=00, to=12, width=3, format='%02.0f')
    year1_2_entry = Spinbox(tab1, from_=2018, to=2030, width=5)
    date1_2_entry.delete(0,'end')
    today=datetime.date.today() # today
    day_phase2 = today + datetime.timedelta(days=7) # calculate dates for 7 days after recording initiation
    date1_2_entry.insert(0,'{:02d}'.format(day_phase2.day))
    month1_2_entry.delete(0,'end')
    month1_2_entry.insert(0,'{:02d}'.format(day_phase2.month))
    year1_2_entry.delete(0,'end')
    year1_2_entry.insert(0,day_phase2.year) # ISO format is YYYY/MM/DD

    label1_d_0 = Label(tab1, text= 'Month')
    label1_m_0 = Label(tab1, text= 'Date')
    label1_m_0.grid(column=11,row=2+row_adj)
    label1_d_0.grid(column=9,row=2+row_adj)
    label1_d_1 = Label(tab1, text= '/')
    label1_m_1 = Label(tab1, text= '/')
    label1_d_1.grid(column=8,row=2+row_adj)
    label1_m_1.grid(column=10,row=2+row_adj)


    label1_d_2 = Label(tab1, text= '/')
    label1_m_2 = Label(tab1, text= '/')
    rad1_A_2 = Radiobutton(tab1, text='LD', variable=var1_2, value=1)
    lbl1_A_2 = Label(tab1, text= 'On:')
    spin1_A_2 = Spinbox(tab1, from_=00, to=24, width=3, format='%02.0f')
    spin1_B_2 = Spinbox(tab1, from_=00, to=59, width=3, format='%02.0f')
    spin1_A_2.delete(0,'end')
    spin1_A_2.insert(0,'07')
    spin1_B_2.delete(0,'end')
    spin1_B_2.insert(0,'00')
    label1_h1_2 = Label(tab1, text=':')
    label1_m1_2 = Label(tab1, text='')
    lbl1_B_2 = Label(tab1, text= 'Off:')
    spin1_C_2 = Spinbox(tab1, from_=00, to=24, width=3, format='%02.0f')
    spin1_D_2 = Spinbox(tab1, from_=00, to=59, width=3, format='%02.0f')
    spin1_C_2.delete(0,'end')
    spin1_C_2.insert(0,'19')
    spin1_D_2.delete(0,'end')
    spin1_D_2.insert(0,'00')
    label1_h2_2 = Label(tab1, text=':')
    label1_m2_2 = Label(tab1, text='')
    rad1_B_2 = Radiobutton(tab1, text='DD', variable=var1_2, value=2)
    rad1_C_2 = Radiobutton(tab1, text='LL', variable=var1_2, value=3)
    phaseLabel1_2.grid(column=0, row=3+row_adj, padx=15, pady=5)
    fromLabel1_2.grid(column=1,row=3+row_adj)
    spin1_E_2.grid(column=2,row=3+row_adj)
    label1_h0_2.grid(column=3,row=3+row_adj)
    spin1_F_2.grid(column=4,row=3+row_adj)
    label1_m0_2.grid(column=5,row=3+row_adj)
    space1_2.grid(column=6,row=3+row_adj)
    year1_2_entry.grid(column=7, row=3+row_adj)
    label1_m_2.grid(column=8,row=3+row_adj)
    month1_2_entry.grid(column=9, row=3+row_adj)
    label1_d_2.grid(column=10,row=3+row_adj)
    date1_2_entry.grid(column=11, row=3+row_adj) # ISO format
    space1_2_2.grid(column=12,row=3+row_adj,padx=5)
    rad1_A_2.grid(column=13, row=3+row_adj, pady=5)
    lbl1_A_2.grid(column=14, row=3+row_adj, pady=5)
    spin1_A_2.grid(column=15,row=3+row_adj, pady=5)
    label1_h1_2.grid(column=16,row=3+row_adj, pady=5)
    spin1_B_2.grid(column=17,row=3+row_adj, pady=5)
    label1_m1_2.grid(column=18,row=3+row_adj, pady=5)
    lbl1_B_2.grid(column=19, row=3+row_adj, pady=5)
    spin1_C_2.grid(column=20,row=3+row_adj, pady=5)
    label1_h2_2.grid(column=21,row=3+row_adj, pady=5)
    spin1_D_2.grid(column=22,row=3+row_adj, pady=5)
    label1_m2_2.grid(column=23,row=3+row_adj, pady=5)
    rad1_B_2.grid(column=24, row=3+row_adj, padx=15, pady=5)
    rad1_C_2.grid(column=25, row=3+row_adj, pady=5)

    
        # phase 3
    phaseLabel1_3 = Label(tab1, text='Phase 3')
    fromLabel1_3 = Label(tab1, text='From:')
    fromLabel1_3.grid(column=1,row=4+row_adj)
    space1_3 = Label(tab1, text=' ')
    space1_3_2 = Label(tab1, text=' ')
    spin1_E_3 = Spinbox(tab1, from_=00, to=24, width=3, format='%02.0f')
    spin1_F_3 = Spinbox(tab1, from_=00, to=59, width=3, format='%02.0f')
    spin1_E_3.delete(0,'end')
    spin1_E_3.insert(0,'07')
    spin1_F_3.delete(0,'end')
    spin1_F_3.insert(0,'00')
    label1_h0_3 = Label(tab1, text=':')
    label1_m0_3 = Label(tab1, text='')
    date1_3_entry = Spinbox(tab1, from_=00, to=31, width=3, format='%02.0f')
    month1_3_entry = Spinbox(tab1, from_=00, to=12, width=3, format='%02.0f')
    year1_3_entry = Spinbox(tab1, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase3 = day_phase2 + datetime.timedelta(days=7) # calculate dates for 14 days after recording initiation
    date1_3_entry.delete(0,'end')
    date1_3_entry.insert(0,'{:02d}'.format(day_phase3.day))
    month1_3_entry.delete(0,'end')
    month1_3_entry.insert(0,'{:02d}'.format(day_phase3.month))
    year1_3_entry.delete(0,'end')
    year1_3_entry.insert(0,day_phase3.year)
    label1_d_3 = Label(tab1, text= '/')
    label1_m_3 = Label(tab1, text= '/')
    rad1_A_3 = Radiobutton(tab1, text='LD', variable=var1_3, value=1)
    lbl1_A_3 = Label(tab1, text= 'On:')
    spin1_A_3 = Spinbox(tab1, from_=00, to=24, width=3, format='%02.0f')
    spin1_B_3 = Spinbox(tab1, from_=00, to=59, width=3, format='%02.0f')
    spin1_A_3.delete(0,'end')
    spin1_A_3.insert(0,'07')
    spin1_B_3.delete(0,'end')
    spin1_B_3.insert(0,'00')
    label1_h1_3 = Label(tab1, text=':')
    label1_m1_3 = Label(tab1, text='')
    lbl1_B_3 = Label(tab1, text= 'Off:')
    spin1_C_3 = Spinbox(tab1, from_=00, to=24, width=3, format='%02.0f')
    spin1_D_3 = Spinbox(tab1, from_=00, to=59, width=3, format='%02.0f')
    spin1_C_3.delete(0,'end')
    spin1_C_3.insert(0,'19')
    spin1_D_3.delete(0,'end')
    spin1_D_3.insert(0,'00')
    label1_h2_3 = Label(tab1, text=':')
    label1_m2_3 = Label(tab1, text='')
    rad1_B_3 = Radiobutton(tab1, text='DD', variable=var1_3, value=2)
    rad1_C_3 = Radiobutton(tab1, text='LL', variable=var1_3, value=3)
    phaseLabel1_3.grid(column=0, row=4+row_adj, padx=15, pady=5)
    spin1_E_3.grid(column=2,row=4+row_adj)
    label1_h0_3.grid(column=3,row=4+row_adj)
    spin1_F_3.grid(column=4,row=4+row_adj)
    label1_m0_3.grid(column=5,row=4+row_adj)
    space1_3.grid(column=6,row=4+row_adj)
    date1_3_entry.grid(column=11, row=4+row_adj)
    label1_d_3.grid(column=8,row=4+row_adj)
    month1_3_entry.grid(column=9, row=4+row_adj)
    label1_m_3.grid(column=10,row=4+row_adj)
    year1_3_entry.grid(column=7, row=4+row_adj) # ISO format
    space1_3_2.grid(column=12,row=4+row_adj,padx=5)
    rad1_A_3.grid(column=13, row=4+row_adj, pady=5)
    lbl1_A_3.grid(column=14, row=4+row_adj, pady=5)
    spin1_A_3.grid(column=15,row=4+row_adj, pady=5)
    label1_h1_3.grid(column=16,row=4+row_adj, pady=5)
    spin1_B_3.grid(column=17,row=4+row_adj, pady=5)
    label1_m1_3.grid(column=18,row=4+row_adj, pady=5)
    lbl1_B_3.grid(column=19, row=4+row_adj, pady=5)
    spin1_C_3.grid(column=20,row=4+row_adj, pady=5)
    label1_h2_3.grid(column=21,row=4+row_adj, pady=5)
    spin1_D_3.grid(column=22,row=4+row_adj, pady=5)
    label1_m2_3.grid(column=23,row=4+row_adj, pady=5)
    rad1_B_3.grid(column=24, row=4+row_adj, padx=15, pady=5)
    rad1_C_3.grid(column=25, row=4+row_adj, pady=5)


   


        # phase 4
    phaseLabel1_4 = Label(tab1, text='Phase 4')
    fromLabel1_4 = Label(tab1, text='From:')
    space1_4 = Label(tab1, text=' ')
    space1_4_2 = Label(tab1, text=' ')
    spin1_E_4 = Spinbox(tab1, from_=00, to=24, width=3, format='%02.0f')
    spin1_F_4 = Spinbox(tab1, from_=00, to=59, width=3, format='%02.0f')
    spin1_E_4.delete(0,'end')
    spin1_E_4.insert(0,'07')
    spin1_F_4.delete(0,'end')
    spin1_F_4.insert(0,'00')
    label1_h0_4 = Label(tab1, text=':')
    label1_m0_4 = Label(tab1, text='')
    date1_4_entry = Spinbox(tab1, from_=00, to=31, width=3, format='%02.0f')
    month1_4_entry = Spinbox(tab1, from_=00, to=12, width=3, format='%02.0f')
    year1_4_entry = Spinbox(tab1, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase4 = day_phase3 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date1_4_entry.delete(0,'end')
    date1_4_entry.insert(0,'{:02d}'.format(day_phase4.day))
    month1_4_entry.delete(0,'end')
    month1_4_entry.insert(0,'{:02d}'.format(day_phase4.month))
    year1_4_entry.delete(0,'end')
    year1_4_entry.insert(0,day_phase4.year)
    label1_d_4 = Label(tab1, text= '/')
    label1_m_4 = Label(tab1, text= '/')
    rad1_A_4 = Radiobutton(tab1, text='LD', variable=var1_4, value=1)
    lbl1_A_4 = Label(tab1, text= 'On:')
    spin1_A_4 = Spinbox(tab1, from_=00, to=24, width=3, format='%02.0f')
    spin1_B_4 = Spinbox(tab1, from_=00, to=59, width=3, format='%02.0f')
    spin1_A_4.delete(0,'end')
    spin1_A_4.insert(0,'07')
    spin1_B_4.delete(0,'end')
    spin1_B_4.insert(0,'00')
    label1_h1_4 = Label(tab1, text=':')
    label1_m1_4 = Label(tab1, text='')
    lbl1_B_4 = Label(tab1, text= 'Off:')
    spin1_C_4 = Spinbox(tab1, from_=00, to=24, width=3, format='%02.0f')
    spin1_D_4 = Spinbox(tab1, from_=00, to=59, width=3, format='%02.0f')
    spin1_C_4.delete(0,'end')
    spin1_C_4.insert(0,'19')
    spin1_D_4.delete(0,'end')
    spin1_D_4.insert(0,'00')
    label1_h2_4 = Label(tab1, text=':')
    label1_m2_4 = Label(tab1, text='')
    rad1_B_4 = Radiobutton(tab1, text='DD', variable=var1_4, value=2)
    rad1_C_4 = Radiobutton(tab1, text='LL', variable=var1_4, value=3)
    phaseLabel1_4.grid(column=0, row=5+row_adj, padx=15, pady=5)
    fromLabel1_4.grid(column=1,row=5+row_adj)
    spin1_E_4.grid(column=2,row=5+row_adj)
    label1_h0_4.grid(column=3,row=5+row_adj)
    spin1_F_4.grid(column=4,row=5+row_adj)
    label1_m0_4.grid(column=5,row=5+row_adj)
    space1_4.grid(column=6,row=5+row_adj)
    date1_4_entry.grid(column=11, row=5+row_adj)
    label1_d_4.grid(column=8,row=5+row_adj)
    month1_4_entry.grid(column=9, row=5+row_adj)
    label1_m_4.grid(column=10,row=5+row_adj)
    year1_4_entry.grid(column=7, row=5+row_adj) # ISO format
    space1_4_2.grid(column=12,row=5+row_adj,padx=5)
    rad1_A_4.grid(column=13, row=5+row_adj, pady=5)
    lbl1_A_4.grid(column=14, row=5+row_adj, pady=5)
    spin1_A_4.grid(column=15,row=5+row_adj, pady=5)
    label1_h1_4.grid(column=16,row=5+row_adj, pady=5)
    spin1_B_4.grid(column=17,row=5+row_adj, pady=5)
    label1_m1_4.grid(column=18,row=5+row_adj, pady=5)
    lbl1_B_4.grid(column=19, row=5+row_adj, pady=5)
    spin1_C_4.grid(column=20,row=5+row_adj, pady=5)
    label1_h2_4.grid(column=21,row=5+row_adj, pady=5)
    spin1_D_4.grid(column=22,row=5+row_adj, pady=5)
    label1_m2_4.grid(column=23,row=5+row_adj, pady=5)
    rad1_B_4.grid(column=24, row=5+row_adj, padx=15, pady=5)
    rad1_C_4.grid(column=25, row=5+row_adj, pady=5)

   




        # Phase 5
    phaseLabel1_5 = Label(tab1, text='Phase 5')
    fromLabel1_5 = Label(tab1, text='From:')
    space1_5 = Label(tab1, text=' ')
    space1_5_2 = Label(tab1, text=' ')
    spin1_E_5 = Spinbox(tab1, from_=00, to=24, width=3, format='%02.0f')
    spin1_F_5 = Spinbox(tab1, from_=00, to=59, width=3, format='%02.0f')
    spin1_E_5.delete(0,'end')
    spin1_E_5.insert(0,'07')
    spin1_F_5.delete(0,'end')
    spin1_F_5.insert(0,'00')
    label1_h0_5 = Label(tab1, text=':')
    label1_m0_5 = Label(tab1, text='')
    date1_5_entry = Spinbox(tab1, from_=00, to=31, width=3, format='%02.0f')
    month1_5_entry = Spinbox(tab1, from_=00, to=12, width=3, format='%02.0f')
    year1_5_entry = Spinbox(tab1, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase5 = day_phase4 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date1_5_entry.delete(0,'end')
    date1_5_entry.insert(0,'{:02d}'.format(day_phase5.day))
    month1_5_entry.delete(0,'end')
    month1_5_entry.insert(0,'{:02d}'.format(day_phase5.month))
    year1_5_entry.delete(0,'end')
    year1_5_entry.insert(0,day_phase5.year)
    label1_d_5 = Label(tab1, text= '/')
    label1_m_5 = Label(tab1, text= '/')
    rad1_A_5 = Radiobutton(tab1, text='LD', variable=var1_5, value=1)
    lbl1_A_5 = Label(tab1, text= 'On:')
    spin1_A_5 = Spinbox(tab1, from_=00, to=24, width=3, format='%02.0f')
    spin1_B_5 = Spinbox(tab1, from_=00, to=59, width=3, format='%02.0f')
    spin1_A_5.delete(0,'end')
    spin1_A_5.insert(0,'07')
    spin1_B_5.delete(0,'end')
    spin1_B_5.insert(0,'00')
    label1_h1_5 = Label(tab1, text=':')
    label1_m1_5 = Label(tab1, text='')
    lbl1_B_5 = Label(tab1, text= 'Off:')
    spin1_C_5 = Spinbox(tab1, from_=00, to=24, width=3, format='%02.0f')
    spin1_D_5 = Spinbox(tab1, from_=00, to=59, width=3, format='%02.0f')
    spin1_C_5.delete(0,'end')
    spin1_C_5.insert(0,'19')
    spin1_D_5.delete(0,'end')
    spin1_D_5.insert(0,'00')
    label1_h2_5 = Label(tab1, text=':')
    label1_m2_5 = Label(tab1, text='')
    rad1_B_5 = Radiobutton(tab1, text='DD', variable=var1_5, value=2)
    rad1_C_5 = Radiobutton(tab1, text='LL', variable=var1_5, value=3)
    phaseLabel1_5.grid(column=0, row=6+row_adj, padx=15, pady=5)
    fromLabel1_5.grid(column=1,row=6+row_adj)
    spin1_E_5.grid(column=2,row=6+row_adj)
    label1_h0_5.grid(column=3,row=6+row_adj)
    spin1_F_5.grid(column=4,row=6+row_adj)
    label1_m0_5.grid(column=5,row=6+row_adj)
    space1_5.grid(column=6,row=6+row_adj)
    date1_5_entry.grid(column=11, row=6+row_adj)
    label1_d_5.grid(column=8,row=6+row_adj)
    month1_5_entry.grid(column=9, row=6+row_adj)
    label1_m_5.grid(column=10,row=6+row_adj)
    year1_5_entry.grid(column=7, row=6+row_adj) # ISO format
    space1_5_2.grid(column=12,row=6+row_adj,padx=5)
    rad1_A_5.grid(column=13, row=6+row_adj, pady=5)
    lbl1_A_5.grid(column=14, row=6+row_adj, pady=5)
    spin1_A_5.grid(column=15,row=6+row_adj, pady=5)
    label1_h1_5.grid(column=16,row=6+row_adj, pady=5)
    spin1_B_5.grid(column=17,row=6+row_adj, pady=5)
    label1_m1_5.grid(column=18,row=6+row_adj, pady=5)
    lbl1_B_5.grid(column=19, row=6+row_adj, pady=5)
    spin1_C_5.grid(column=20,row=6+row_adj, pady=5)
    label1_h2_5.grid(column=21,row=6+row_adj, pady=5)
    spin1_D_5.grid(column=22,row=6+row_adj, pady=5)
    label1_m2_5.grid(column=23,row=6+row_adj, pady=5)
    rad1_B_5.grid(column=24, row=6+row_adj, padx=15, pady=5)
    rad1_C_5.grid(column=25, row=6+row_adj, pady=5)

        # Phase 6
    phaseLabel1_6 = Label(tab1, text='Phase 6')
    fromLabel1_6 = Label(tab1, text='From:')
    space1_6 = Label(tab1, text=' ')
    space1_6_2 = Label(tab1, text=' ')
    spin1_E_6 = Spinbox(tab1, from_=00, to=24, width=3, format='%02.0f')
    spin1_F_6 = Spinbox(tab1, from_=00, to=59, width=3, format='%02.0f')
    spin1_E_6.delete(0,'end')
    spin1_E_6.insert(0,'07')
    spin1_F_6.delete(0,'end')
    spin1_F_6.insert(0,'00')
    label1_h0_6 = Label(tab1, text=':')
    label1_m0_6 = Label(tab1, text='')
    date1_6_entry = Spinbox(tab1, from_=00, to=31, width=3, format='%02.0f')
    month1_6_entry = Spinbox(tab1, from_=00, to=12, width=3, format='%02.0f')
    year1_6_entry = Spinbox(tab1, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase6 = day_phase5 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date1_6_entry.delete(0,'end')
    date1_6_entry.insert(0,'{:02d}'.format(day_phase6.day))
    month1_6_entry.delete(0,'end')
    month1_6_entry.insert(0,'{:02d}'.format(day_phase6.month))
    year1_6_entry.delete(0,'end')
    year1_6_entry.insert(0,day_phase6.year)
    label1_d_6 = Label(tab1, text= '/')
    label1_m_6 = Label(tab1, text= '/')
    rad1_A_6 = Radiobutton(tab1, text='LD', variable=var1_6, value=1)
    lbl1_A_6 = Label(tab1, text= 'On:')
    spin1_A_6 = Spinbox(tab1, from_=00, to=24, width=3, format='%02.0f')
    spin1_B_6 = Spinbox(tab1, from_=00, to=59, width=3, format='%02.0f')
    spin1_A_6.delete(0,'end')
    spin1_A_6.insert(0,'07')
    spin1_B_6.delete(0,'end')
    spin1_B_6.insert(0,'00')
    label1_h1_6 = Label(tab1, text=':')
    label1_m1_6 = Label(tab1, text='')
    lbl1_B_6 = Label(tab1, text= 'Off:')
    spin1_C_6 = Spinbox(tab1, from_=00, to=24, width=3, format='%02.0f')
    spin1_D_6 = Spinbox(tab1, from_=00, to=59, width=3, format='%02.0f')
    spin1_C_6.delete(0,'end')
    spin1_C_6.insert(0,'19')
    spin1_D_6.delete(0,'end')
    spin1_D_6.insert(0,'00')
    label1_h2_6 = Label(tab1, text=':')
    label1_m2_6 = Label(tab1, text='')
    rad1_B_6 = Radiobutton(tab1, text='DD', variable=var1_6, value=2)
    rad1_C_6 = Radiobutton(tab1, text='LL', variable=var1_6, value=3)

    rowPhase6 = 7
    phaseLabel1_6.grid(column=0, row=rowPhase6+row_adj, padx=15, pady=5)
    fromLabel1_6.grid(column=1,row=rowPhase6+row_adj)
    spin1_E_6.grid(column=2,row=rowPhase6+row_adj)
    label1_h0_6.grid(column=3,row=rowPhase6+row_adj)
    spin1_F_6.grid(column=4,row=rowPhase6+row_adj)
    label1_m0_6.grid(column=5,row=rowPhase6+row_adj)
    space1_6.grid(column=6,row=rowPhase6+row_adj)
    date1_6_entry.grid(column=11, row=rowPhase6+row_adj)
    label1_d_6.grid(column=8,row=rowPhase6+row_adj)
    month1_6_entry.grid(column=9, row=rowPhase6+row_adj)
    label1_m_6.grid(column=10,row=rowPhase6+row_adj)
    year1_6_entry.grid(column=7, row=rowPhase6+row_adj) # ISO format
    space1_6_2.grid(column=12,row=rowPhase6+row_adj,padx=5)
    rad1_A_6.grid(column=13, row=rowPhase6+row_adj, pady=5)
    lbl1_A_6.grid(column=14, row=rowPhase6+row_adj, pady=5)
    spin1_A_6.grid(column=15,row=rowPhase6+row_adj, pady=5)
    label1_h1_6.grid(column=16,row=rowPhase6+row_adj, pady=5)
    spin1_B_6.grid(column=17,row=rowPhase6+row_adj, pady=5)
    label1_m1_6.grid(column=18,row=rowPhase6+row_adj, pady=5)
    lbl1_B_6.grid(column=19, row=rowPhase6+row_adj, pady=5)
    spin1_C_6.grid(column=20,row=rowPhase6+row_adj, pady=5)
    label1_h2_6.grid(column=21,row=rowPhase6+row_adj, pady=5)
    spin1_D_6.grid(column=22,row=rowPhase6+row_adj, pady=5)
    label1_m2_6.grid(column=23,row=rowPhase6+row_adj, pady=5)
    rad1_B_6.grid(column=24, row=rowPhase6+row_adj, padx=15, pady=5)
    rad1_C_6.grid(column=25, row=rowPhase6+row_adj, pady=5)

  



        # Phase 7
    phaseLabel1_7 = Label(tab1, text='Phase 7')
    fromLabel1_7 = Label(tab1, text='From:')
    space1_7 = Label(tab1, text=' ')
    space1_7_2 = Label(tab1, text=' ')
    spin1_E_7 = Spinbox(tab1, from_=00, to=24, width=3, format='%02.0f')
    spin1_F_7 = Spinbox(tab1, from_=00, to=59, width=3, format='%02.0f')
    spin1_E_7.delete(0,'end')
    spin1_E_7.insert(0,'07')
    spin1_F_7.delete(0,'end')
    spin1_F_7.insert(0,'00')
    label1_h0_7 = Label(tab1, text=':')
    label1_m0_7 = Label(tab1, text='')
    date1_7_entry = Spinbox(tab1, from_=00, to=31, width=3, format='%02.0f')
    month1_7_entry = Spinbox(tab1, from_=00, to=12, width=3, format='%02.0f')
    year1_7_entry = Spinbox(tab1, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase7 = day_phase6 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date1_7_entry.delete(0,'end')
    date1_7_entry.insert(0,'{:02d}'.format(day_phase7.day))
    month1_7_entry.delete(0,'end')
    month1_7_entry.insert(0,'{:02d}'.format(day_phase7.month))
    year1_7_entry.delete(0,'end')
    year1_7_entry.insert(0,day_phase7.year)
    label1_d_7 = Label(tab1, text= '/')
    label1_m_7 = Label(tab1, text= '/')
    rad1_A_7 = Radiobutton(tab1, text='LD', variable=var1_7, value=1)
    lbl1_A_7 = Label(tab1, text= 'On:')
    spin1_A_7 = Spinbox(tab1, from_=00, to=24, width=3, format='%02.0f')
    spin1_B_7 = Spinbox(tab1, from_=00, to=59, width=3, format='%02.0f')
    spin1_A_7.delete(0,'end')
    spin1_A_7.insert(0,'07')
    spin1_B_7.delete(0,'end')
    spin1_B_7.insert(0,'00')
    label1_h1_7 = Label(tab1, text=':')
    label1_m1_7 = Label(tab1, text='')
    lbl1_B_7 = Label(tab1, text= 'Off:')
    spin1_C_7 = Spinbox(tab1, from_=00, to=24, width=3, format='%02.0f')
    spin1_D_7 = Spinbox(tab1, from_=00, to=59, width=3, format='%02.0f')
    spin1_C_7.delete(0,'end')
    spin1_C_7.insert(0,'19')
    spin1_D_7.delete(0,'end')
    spin1_D_7.insert(0,'00')
    label1_h2_7 = Label(tab1, text=':')
    label1_m2_7 = Label(tab1, text='')
    rad1_B_7 = Radiobutton(tab1, text='DD', variable=var1_7, value=2)
    rad1_C_7 = Radiobutton(tab1, text='LL', variable=var1_7, value=3)

    rowPhase7 = 8
    phaseLabel1_7.grid(column=0, row=rowPhase7+row_adj, padx=15, pady=5)
    fromLabel1_7.grid(column=1,row=rowPhase7+row_adj)
    spin1_E_7.grid(column=2,row=rowPhase7+row_adj)
    label1_h0_7.grid(column=3,row=rowPhase7+row_adj)
    spin1_F_7.grid(column=4,row=rowPhase7+row_adj)
    label1_m0_7.grid(column=5,row=rowPhase7+row_adj)
    space1_7.grid(column=6,row=rowPhase7+row_adj)
    date1_7_entry.grid(column=11, row=rowPhase7+row_adj)
    label1_d_7.grid(column=8,row=rowPhase7+row_adj)
    month1_7_entry.grid(column=9, row=rowPhase7+row_adj)
    label1_m_7.grid(column=10,row=rowPhase7+row_adj)
    year1_7_entry.grid(column=7, row=rowPhase7+row_adj) # ISO format
    space1_7_2.grid(column=12,row=rowPhase7+row_adj,padx=5)
    rad1_A_7.grid(column=13, row=rowPhase7+row_adj, pady=5)
    lbl1_A_7.grid(column=14, row=rowPhase7+row_adj, pady=5)
    spin1_A_7.grid(column=15,row=rowPhase7+row_adj, pady=5)
    label1_h1_7.grid(column=16,row=rowPhase7+row_adj, pady=5)
    spin1_B_7.grid(column=17,row=rowPhase7+row_adj, pady=5)
    label1_m1_7.grid(column=18,row=rowPhase7+row_adj, pady=5)
    lbl1_B_7.grid(column=19, row=rowPhase7+row_adj, pady=5)
    spin1_C_7.grid(column=20,row=rowPhase7+row_adj, pady=5)
    label1_h2_7.grid(column=21,row=rowPhase7+row_adj, pady=5)
    spin1_D_7.grid(column=22,row=rowPhase7+row_adj, pady=5)
    label1_m2_7.grid(column=23,row=rowPhase7+row_adj, pady=5)
    rad1_B_7.grid(column=24, row=rowPhase7+row_adj, padx=15, pady=5)
    rad1_C_7.grid(column=25, row=rowPhase7+row_adj, pady=5)


   


    # Phase 8
    phaseLabel1_8 = Label(tab1, text='Phase 8')
    fromLabel1_8 = Label(tab1, text='From:')
    space1_8 = Label(tab1, text=' ')
    space1_8_2 = Label(tab1, text=' ')
    spin1_E_8 = Spinbox(tab1, from_=00, to=24, width=3, format='%02.0f')
    spin1_F_8 = Spinbox(tab1, from_=00, to=59, width=3, format='%02.0f')
    spin1_E_8.delete(0,'end')
    spin1_E_8.insert(0,'07')
    spin1_F_8.delete(0,'end')
    spin1_F_8.insert(0,'00')
    label1_h0_8 = Label(tab1, text=':')
    label1_m0_8 = Label(tab1, text='')
    date1_8_entry = Spinbox(tab1, from_=00, to=31, width=3, format='%02.0f')
    month1_8_entry = Spinbox(tab1, from_=00, to=12, width=3, format='%02.0f')
    year1_8_entry = Spinbox(tab1, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase8 = day_phase7 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date1_8_entry.delete(0,'end')
    date1_8_entry.insert(0,'{:02d}'.format(day_phase8.day))
    month1_8_entry.delete(0,'end')
    month1_8_entry.insert(0,'{:02d}'.format(day_phase8.month))
    year1_8_entry.delete(0,'end')
    year1_8_entry.insert(0,day_phase8.year)
    label1_d_8 = Label(tab1, text= '/')
    label1_m_8 = Label(tab1, text= '/')
    rad1_A_8 = Radiobutton(tab1, text='LD', variable=var1_8, value=1)
    lbl1_A_8 = Label(tab1, text= 'On:')
    spin1_A_8 = Spinbox(tab1, from_=00, to=24, width=3, format='%02.0f')
    spin1_B_8 = Spinbox(tab1, from_=00, to=59, width=3, format='%02.0f')
    spin1_A_8.delete(0,'end')
    spin1_A_8.insert(0,'07')
    spin1_B_8.delete(0,'end')
    spin1_B_8.insert(0,'00')
    label1_h1_8 = Label(tab1, text=':')
    label1_m1_8 = Label(tab1, text='')
    lbl1_B_8 = Label(tab1, text= 'Off:')
    spin1_C_8 = Spinbox(tab1, from_=00, to=24, width=3, format='%02.0f')
    spin1_D_8 = Spinbox(tab1, from_=00, to=59, width=3, format='%02.0f')
    spin1_C_8.delete(0,'end')
    spin1_C_8.insert(0,'19')
    spin1_D_8.delete(0,'end')
    spin1_D_8.insert(0,'00')
    label1_h2_8 = Label(tab1, text=':')
    label1_m2_8 = Label(tab1, text='')
    rad1_B_8 = Radiobutton(tab1, text='DD', variable=var1_8, value=2)
    rad1_C_8 = Radiobutton(tab1, text='LL', variable=var1_8, value=3)

    rowPhase8 = 9
    phaseLabel1_8.grid(column=0, row=rowPhase8+row_adj, padx=15, pady=5)
    fromLabel1_8.grid(column=1,row=rowPhase8+row_adj)
    spin1_E_8.grid(column=2,row=rowPhase8+row_adj)
    label1_h0_8.grid(column=3,row=rowPhase8+row_adj)
    spin1_F_8.grid(column=4,row=rowPhase8+row_adj)
    label1_m0_8.grid(column=5,row=rowPhase8+row_adj)
    space1_8.grid(column=6,row=rowPhase8+row_adj)
    date1_8_entry.grid(column=11, row=rowPhase8+row_adj)
    label1_d_8.grid(column=8,row=rowPhase8+row_adj)
    month1_8_entry.grid(column=9, row=rowPhase8+row_adj)
    label1_m_8.grid(column=10,row=rowPhase8+row_adj)
    year1_8_entry.grid(column=7, row=rowPhase8+row_adj) # ISO format
    space1_8_2.grid(column=12,row=rowPhase8+row_adj,padx=5)
    rad1_A_8.grid(column=13, row=rowPhase8+row_adj, pady=5)
    lbl1_A_8.grid(column=14, row=rowPhase8+row_adj, pady=5)
    spin1_A_8.grid(column=15,row=rowPhase8+row_adj, pady=5)
    label1_h1_8.grid(column=16,row=rowPhase8+row_adj, pady=5)
    spin1_B_8.grid(column=17,row=rowPhase8+row_adj, pady=5)
    label1_m1_8.grid(column=18,row=rowPhase8+row_adj, pady=5)
    lbl1_B_8.grid(column=19, row=rowPhase8+row_adj, pady=5)
    spin1_C_8.grid(column=20,row=rowPhase8+row_adj, pady=5)
    label1_h2_8.grid(column=21,row=rowPhase8+row_adj, pady=5)
    spin1_D_8.grid(column=22,row=rowPhase8+row_adj, pady=5)
    label1_m2_8.grid(column=23,row=rowPhase8+row_adj, pady=5)
    rad1_B_8.grid(column=24, row=rowPhase8+row_adj, padx=15, pady=5)
    rad1_C_8.grid(column=25, row=rowPhase8+row_adj, pady=5)

   

    # Phase 9
    phaseLabel1_9 = Label(tab1, text='Phase 9')
    fromLabel1_9 = Label(tab1, text='From:')
    space1_9 = Label(tab1, text=' ')
    space1_9_2 = Label(tab1, text=' ')
    spin1_E_9 = Spinbox(tab1, from_=00, to=24, width=3, format='%02.0f')
    spin1_F_9 = Spinbox(tab1, from_=00, to=59, width=3, format='%02.0f')
    spin1_E_9.delete(0,'end')
    spin1_E_9.insert(0,'07')
    spin1_F_9.delete(0,'end')
    spin1_F_9.insert(0,'00')
    label1_h0_9 = Label(tab1, text=':')
    label1_m0_9 = Label(tab1, text='')
    date1_9_entry = Spinbox(tab1, from_=00, to=31, width=3, format='%02.0f')
    month1_9_entry = Spinbox(tab1, from_=00, to=12, width=3, format='%02.0f')
    year1_9_entry = Spinbox(tab1, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase9 = day_phase8 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date1_9_entry.delete(0,'end')
    date1_9_entry.insert(0,'{:02d}'.format(day_phase9.day))
    month1_9_entry.delete(0,'end')
    month1_9_entry.insert(0,'{:02d}'.format(day_phase9.month))
    year1_9_entry.delete(0,'end')
    year1_9_entry.insert(0,day_phase9.year)
    label1_d_9 = Label(tab1, text= '/')
    label1_m_9 = Label(tab1, text= '/')
    rad1_A_9 = Radiobutton(tab1, text='LD', variable=var1_9, value=1)
    lbl1_A_9 = Label(tab1, text= 'On:')
    spin1_A_9 = Spinbox(tab1, from_=00, to=24, width=3, format='%02.0f')
    spin1_B_9 = Spinbox(tab1, from_=00, to=59, width=3, format='%02.0f')
    spin1_A_9.delete(0,'end')
    spin1_A_9.insert(0,'07')
    spin1_B_9.delete(0,'end')
    spin1_B_9.insert(0,'00')
    label1_h1_9 = Label(tab1, text=':')
    label1_m1_9 = Label(tab1, text='')
    lbl1_B_9 = Label(tab1, text= 'Off:')
    spin1_C_9 = Spinbox(tab1, from_=00, to=24, width=3, format='%02.0f')
    spin1_D_9 = Spinbox(tab1, from_=00, to=59, width=3, format='%02.0f')
    spin1_C_9.delete(0,'end')
    spin1_C_9.insert(0,'19')
    spin1_D_9.delete(0,'end')
    spin1_D_9.insert(0,'00')
    label1_h2_9 = Label(tab1, text=':')
    label1_m2_9 = Label(tab1, text='')
    rad1_B_9 = Radiobutton(tab1, text='DD', variable=var1_9, value=2)
    rad1_C_9 = Radiobutton(tab1, text='LL', variable=var1_9, value=3)

    rowPhase9 = 10
    phaseLabel1_9.grid(column=0, row=rowPhase9+row_adj, padx=15, pady=5)
    fromLabel1_9.grid(column=1,row=rowPhase9+row_adj)
    spin1_E_9.grid(column=2,row=rowPhase9+row_adj)
    label1_h0_9.grid(column=3,row=rowPhase9+row_adj)
    spin1_F_9.grid(column=4,row=rowPhase9+row_adj)
    label1_m0_9.grid(column=5,row=rowPhase9+row_adj)
    space1_9.grid(column=6,row=rowPhase9+row_adj)
    date1_9_entry.grid(column=11, row=rowPhase9+row_adj)
    label1_d_9.grid(column=8,row=rowPhase9+row_adj)
    month1_9_entry.grid(column=9, row=rowPhase9+row_adj)
    label1_m_9.grid(column=10,row=rowPhase9+row_adj)
    year1_9_entry.grid(column=7, row=rowPhase9+row_adj) # ISO format
    space1_9_2.grid(column=12,row=rowPhase9+row_adj,padx=5)
    rad1_A_9.grid(column=13, row=rowPhase9+row_adj, pady=5)
    lbl1_A_9.grid(column=14, row=rowPhase9+row_adj, pady=5)
    spin1_A_9.grid(column=15,row=rowPhase9+row_adj, pady=5)
    label1_h1_9.grid(column=16,row=rowPhase9+row_adj, pady=5)
    spin1_B_9.grid(column=17,row=rowPhase9+row_adj, pady=5)
    label1_m1_9.grid(column=18,row=rowPhase9+row_adj, pady=5)
    lbl1_B_9.grid(column=19, row=rowPhase9+row_adj, pady=5)
    spin1_C_9.grid(column=20,row=rowPhase9+row_adj, pady=5)
    label1_h2_9.grid(column=21,row=rowPhase9+row_adj, pady=5)
    spin1_D_9.grid(column=22,row=rowPhase9+row_adj, pady=5)
    label1_m2_9.grid(column=23,row=rowPhase9+row_adj, pady=5)
    rad1_B_9.grid(column=24, row=rowPhase9+row_adj, padx=15, pady=5)
    rad1_C_9.grid(column=25, row=rowPhase9+row_adj, pady=5)
   


    # Phase 10
    phaseLabel1_10 = Label(tab1, text='Phase 10')
    fromLabel1_10 = Label(tab1, text='From:')
    space1_10 = Label(tab1, text=' ')
    space1_10_2 = Label(tab1, text=' ')
    spin1_E_10 = Spinbox(tab1, from_=00, to=24, width=3, format='%02.0f')
    spin1_F_10 = Spinbox(tab1, from_=00, to=59, width=3, format='%02.0f')
    spin1_E_10.delete(0,'end')
    spin1_E_10.insert(0,'07')
    spin1_F_10.delete(0,'end')
    spin1_F_10.insert(0,'00')
    label1_h0_10 = Label(tab1, text=':')
    label1_m0_10 = Label(tab1, text='')
    date1_10_entry = Spinbox(tab1, from_=00, to=31, width=3, format='%02.0f')
    month1_10_entry = Spinbox(tab1, from_=00, to=12, width=3, format='%02.0f')
    year1_10_entry = Spinbox(tab1, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase10 = day_phase9 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date1_10_entry.delete(0,'end')
    date1_10_entry.insert(0,'{:02d}'.format(day_phase10.day))
    month1_10_entry.delete(0,'end')
    month1_10_entry.insert(0,'{:02d}'.format(day_phase10.month))
    year1_10_entry.delete(0,'end')
    year1_10_entry.insert(0,day_phase10.year)
    label1_d_10 = Label(tab1, text= '/')
    label1_m_10 = Label(tab1, text= '/')
    rad1_A_10 = Radiobutton(tab1, text='LD', variable=var1_10, value=1)
    lbl1_A_10 = Label(tab1, text= 'On:')
    spin1_A_10 = Spinbox(tab1, from_=00, to=24, width=3, format='%02.0f')
    spin1_B_10 = Spinbox(tab1, from_=00, to=59, width=3, format='%02.0f')
    spin1_A_10.delete(0,'end')
    spin1_A_10.insert(0,'07')
    spin1_B_10.delete(0,'end')
    spin1_B_10.insert(0,'00')
    label1_h1_10 = Label(tab1, text=':')
    label1_m1_10 = Label(tab1, text='')
    lbl1_B_10 = Label(tab1, text= 'Off:')
    spin1_C_10 = Spinbox(tab1, from_=00, to=24, width=3, format='%02.0f')
    spin1_D_10 = Spinbox(tab1, from_=00, to=59, width=3, format='%02.0f')
    spin1_C_10.delete(0,'end')
    spin1_C_10.insert(0,'19')
    spin1_D_10.delete(0,'end')
    spin1_D_10.insert(0,'00')
    label1_h2_10 = Label(tab1, text=':')
    label1_m2_10 = Label(tab1, text='')
    rad1_B_10 = Radiobutton(tab1, text='DD', variable=var1_10, value=2)
    rad1_C_10 = Radiobutton(tab1, text='LL', variable=var1_10, value=3)

    rowPhase10 = 11
    phaseLabel1_10.grid(column=0, row=rowPhase10+row_adj, padx=15, pady=5)
    fromLabel1_10.grid(column=1,row=rowPhase10+row_adj)
    spin1_E_10.grid(column=2,row=rowPhase10+row_adj)
    label1_h0_10.grid(column=3,row=rowPhase10+row_adj)
    spin1_F_10.grid(column=4,row=rowPhase10+row_adj)
    label1_m0_10.grid(column=5,row=rowPhase10+row_adj)
    space1_10.grid(column=6,row=rowPhase10+row_adj)
    date1_10_entry.grid(column=11, row=rowPhase10+row_adj)
    label1_d_10.grid(column=8,row=rowPhase10+row_adj)
    month1_10_entry.grid(column=9, row=rowPhase10+row_adj)
    label1_m_10.grid(column=10,row=rowPhase10+row_adj)
    year1_10_entry.grid(column=7, row=rowPhase10+row_adj) # ISO format
    space1_10_2.grid(column=12,row=rowPhase10+row_adj,padx=5)
    rad1_A_10.grid(column=13, row=rowPhase10+row_adj, pady=5)
    lbl1_A_10.grid(column=14, row=rowPhase10+row_adj, pady=5)
    spin1_A_10.grid(column=15,row=rowPhase10+row_adj, pady=5)
    label1_h1_10.grid(column=16,row=rowPhase10+row_adj, pady=5)
    spin1_B_10.grid(column=17,row=rowPhase10+row_adj, pady=5)
    label1_m1_10.grid(column=18,row=rowPhase10+row_adj, pady=5)
    lbl1_B_10.grid(column=19, row=rowPhase10+row_adj, pady=5)
    spin1_C_10.grid(column=20,row=rowPhase10+row_adj, pady=5)
    label1_h2_10.grid(column=21,row=rowPhase10+row_adj, pady=5)
    spin1_D_10.grid(column=22,row=rowPhase10+row_adj, pady=5)
    label1_m2_10.grid(column=23,row=rowPhase10+row_adj, pady=5)
    rad1_B_10.grid(column=24, row=rowPhase10+row_adj, padx=15, pady=5)
    rad1_C_10.grid(column=25, row=rowPhase10+row_adj, pady=5)

   


    # Phase 11
    phaseLabel1_11 = Label(tab1, text='Phase 11')
    fromLabel1_11 = Label(tab1, text='From:')
    space1_11 = Label(tab1, text=' ')
    space1_11_2 = Label(tab1, text=' ')
    spin1_E_11 = Spinbox(tab1, from_=00, to=24, width=3, format='%02.0f')
    spin1_F_11 = Spinbox(tab1, from_=00, to=59, width=3, format='%02.0f')
    spin1_E_11.delete(0,'end')
    spin1_E_11.insert(0,'07')
    spin1_F_11.delete(0,'end')
    spin1_F_11.insert(0,'00')
    label1_h0_11 = Label(tab1, text=':')
    label1_m0_11 = Label(tab1, text='')
    date1_11_entry = Spinbox(tab1, from_=00, to=31, width=3, format='%02.0f')
    month1_11_entry = Spinbox(tab1, from_=00, to=12, width=3, format='%02.0f')
    year1_11_entry = Spinbox(tab1, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase11 = day_phase10 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date1_11_entry.delete(0,'end')
    date1_11_entry.insert(0,'{:02d}'.format(day_phase11.day))
    month1_11_entry.delete(0,'end')
    month1_11_entry.insert(0,'{:02d}'.format(day_phase11.month))
    year1_11_entry.delete(0,'end')
    year1_11_entry.insert(0,day_phase11.year)
    label1_d_11 = Label(tab1, text= '/')
    label1_m_11 = Label(tab1, text= '/')
    rad1_A_11 = Radiobutton(tab1, text='LD', variable=var1_11, value=1)
    lbl1_A_11 = Label(tab1, text= 'On:')
    spin1_A_11 = Spinbox(tab1, from_=00, to=24, width=3, format='%02.0f')
    spin1_B_11 = Spinbox(tab1, from_=00, to=59, width=3, format='%02.0f')
    spin1_A_11.delete(0,'end')
    spin1_A_11.insert(0,'07')
    spin1_B_11.delete(0,'end')
    spin1_B_11.insert(0,'00')
    label1_h1_11 = Label(tab1, text=':')
    label1_m1_11 = Label(tab1, text='')
    lbl1_B_11 = Label(tab1, text= 'Off:')
    spin1_C_11 = Spinbox(tab1, from_=00, to=24, width=3, format='%02.0f')
    spin1_D_11 = Spinbox(tab1, from_=00, to=59, width=3, format='%02.0f')
    spin1_C_11.delete(0,'end')
    spin1_C_11.insert(0,'19')
    spin1_D_11.delete(0,'end')
    spin1_D_11.insert(0,'00')
    label1_h2_11 = Label(tab1, text=':')
    label1_m2_11 = Label(tab1, text='')
    rad1_B_11 = Radiobutton(tab1, text='DD', variable=var1_11, value=2)
    rad1_C_11 = Radiobutton(tab1, text='LL', variable=var1_11, value=3)

    rowPhase11 = 12
    phaseLabel1_11.grid(column=0, row=rowPhase11+row_adj, padx=15, pady=5)
    fromLabel1_11.grid(column=1,row=rowPhase11+row_adj)
    spin1_E_11.grid(column=2,row=rowPhase11+row_adj)
    label1_h0_11.grid(column=3,row=rowPhase11+row_adj)
    spin1_F_11.grid(column=4,row=rowPhase11+row_adj)
    label1_m0_11.grid(column=5,row=rowPhase11+row_adj)
    space1_11.grid(column=6,row=rowPhase11+row_adj)
    date1_11_entry.grid(column=11, row=rowPhase11+row_adj)
    label1_d_11.grid(column=8,row=rowPhase11+row_adj)
    month1_11_entry.grid(column=9, row=rowPhase11+row_adj)
    label1_m_11.grid(column=10,row=rowPhase11+row_adj)
    year1_11_entry.grid(column=7, row=rowPhase11+row_adj) # ISO format
    space1_11_2.grid(column=12,row=rowPhase11+row_adj,padx=5)
    rad1_A_11.grid(column=13, row=rowPhase11+row_adj, pady=5)
    lbl1_A_11.grid(column=14, row=rowPhase11+row_adj, pady=5)
    spin1_A_11.grid(column=15,row=rowPhase11+row_adj, pady=5)
    label1_h1_11.grid(column=16,row=rowPhase11+row_adj, pady=5)
    spin1_B_11.grid(column=17,row=rowPhase11+row_adj, pady=5)
    label1_m1_11.grid(column=18,row=rowPhase11+row_adj, pady=5)
    lbl1_B_11.grid(column=19, row=rowPhase11+row_adj, pady=5)
    spin1_C_11.grid(column=20,row=rowPhase11+row_adj, pady=5)
    label1_h2_11.grid(column=21,row=rowPhase11+row_adj, pady=5)
    spin1_D_11.grid(column=22,row=rowPhase11+row_adj, pady=5)
    label1_m2_11.grid(column=23,row=rowPhase11+row_adj, pady=5)
    rad1_B_11.grid(column=24, row=rowPhase11+row_adj, padx=15, pady=5)
    rad1_C_11.grid(column=25, row=rowPhase11+row_adj, pady=5)

   


    # Phase 12
    phaseLabel1_12 = Label(tab1, text='Phase 12')
    fromLabel1_12 = Label(tab1, text='From:')
    space1_12 = Label(tab1, text=' ')
    space1_12_2 = Label(tab1, text=' ')
    spin1_E_12 = Spinbox(tab1, from_=00, to=24, width=3, format='%02.0f')
    spin1_F_12 = Spinbox(tab1, from_=00, to=59, width=3, format='%02.0f')
    spin1_E_12.delete(0,'end')
    spin1_E_12.insert(0,'07')
    spin1_F_12.delete(0,'end')
    spin1_F_12.insert(0,'00')
    label1_h0_12 = Label(tab1, text=':')
    label1_m0_12 = Label(tab1, text='')
    date1_12_entry = Spinbox(tab1, from_=00, to=31, width=3, format='%02.0f')
    month1_12_entry = Spinbox(tab1, from_=00, to=12, width=3, format='%02.0f')
    year1_12_entry = Spinbox(tab1, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase12 = day_phase11 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date1_12_entry.delete(0,'end')
    date1_12_entry.insert(0,'{:02d}'.format(day_phase12.day))
    month1_12_entry.delete(0,'end')
    month1_12_entry.insert(0,'{:02d}'.format(day_phase12.month))
    year1_12_entry.delete(0,'end')
    year1_12_entry.insert(0,day_phase12.year)
    label1_d_12 = Label(tab1, text= '/')
    label1_m_12 = Label(tab1, text= '/')
    rad1_A_12 = Radiobutton(tab1, text='LD', variable=var1_12, value=1)
    lbl1_A_12 = Label(tab1, text= 'On:')
    spin1_A_12 = Spinbox(tab1, from_=00, to=24, width=3, format='%02.0f')
    spin1_B_12 = Spinbox(tab1, from_=00, to=59, width=3, format='%02.0f')
    spin1_A_12.delete(0,'end')
    spin1_A_12.insert(0,'07')
    spin1_B_12.delete(0,'end')
    spin1_B_12.insert(0,'00')
    label1_h1_12 = Label(tab1, text=':')
    label1_m1_12 = Label(tab1, text='')
    lbl1_B_12 = Label(tab1, text= 'Off:')
    spin1_C_12 = Spinbox(tab1, from_=00, to=24, width=3, format='%02.0f')
    spin1_D_12 = Spinbox(tab1, from_=00, to=59, width=3, format='%02.0f')
    spin1_C_12.delete(0,'end')
    spin1_C_12.insert(0,'19')
    spin1_D_12.delete(0,'end')
    spin1_D_12.insert(0,'00')
    label1_h2_12 = Label(tab1, text=':')
    label1_m2_12 = Label(tab1, text='')
    rad1_B_12 = Radiobutton(tab1, text='DD', variable=var1_12, value=2)
    rad1_C_12 = Radiobutton(tab1, text='LL', variable=var1_12, value=3)

    rowPhase12 = 13
    phaseLabel1_12.grid(column=0, row=rowPhase12+row_adj, padx=15, pady=5)
    fromLabel1_12.grid(column=1,row=rowPhase12+row_adj)
    spin1_E_12.grid(column=2,row=rowPhase12+row_adj)
    label1_h0_12.grid(column=3,row=rowPhase12+row_adj)
    spin1_F_12.grid(column=4,row=rowPhase12+row_adj)
    label1_m0_12.grid(column=5,row=rowPhase12+row_adj)
    space1_12.grid(column=7,row=rowPhase12+row_adj)
    date1_12_entry.grid(column=11, row=rowPhase12+row_adj)
    label1_d_12.grid(column=8,row=rowPhase12+row_adj)
    month1_12_entry.grid(column=9, row=rowPhase12+row_adj)
    label1_m_12.grid(column=10,row=rowPhase12+row_adj)
    year1_12_entry.grid(column=7, row=rowPhase12+row_adj) # ISO format
    space1_12_2.grid(column=12,row=rowPhase12+row_adj,padx=5)
    rad1_A_12.grid(column=13, row=rowPhase12+row_adj, pady=5)
    lbl1_A_12.grid(column=14, row=rowPhase12+row_adj, pady=5)
    spin1_A_12.grid(column=15,row=rowPhase12+row_adj, pady=5)
    label1_h1_12.grid(column=16,row=rowPhase12+row_adj, pady=5)
    spin1_B_12.grid(column=17,row=rowPhase12+row_adj, pady=5)
    label1_m1_12.grid(column=18,row=rowPhase12+row_adj, pady=5)
    lbl1_B_12.grid(column=19, row=rowPhase12+row_adj, pady=5)
    spin1_C_12.grid(column=20,row=rowPhase12+row_adj, pady=5)
    label1_h2_12.grid(column=21,row=rowPhase12+row_adj, pady=5)
    spin1_D_12.grid(column=22,row=rowPhase12+row_adj, pady=5)
    label1_m2_12.grid(column=23,row=rowPhase12+row_adj, pady=5)
    rad1_B_12.grid(column=24, row=rowPhase12+row_adj, padx=15, pady=5)
    rad1_C_12.grid(column=25, row=rowPhase12+row_adj, pady=5)

    rowsButton = 13
    

    # Box2 main
    tcyclelabel2 = Label(tab2, text='T-cycle length')
    tcyclelabel2.grid(column=26, row=1, padx=3, pady=5)

    for i in range(0,12): 
        tcyclelength = Spinbox(tab2, from_=12, to=48, width=3)
        tcyclelength.grid(column=26, row=2+i+row_adj, padx=3,pady=5)
        tcyclelength.delete(0,'end')
        tcyclelength.insert(0,24)
        tcyclespinbox_arr[1,i] = tcyclelength
        
    tcyclespinbox_arr[1,0].grid(column=26, row=1+row_adj, pady=5)
    
   
    tab2_title = Label(tab2, text= 'LED schedule', anchor='center')
    tab2_title.grid(column=12, row= 1, columnspan='27', sticky='we')
    # capSep2 = ttk.Separator(tab2, orient=HORIZONTAL)
    # capSep2.grid(column=0, row = row_adj+5, columnspan='27', sticky='we')
    box2sched_text=StringVar()
    box2sched_text.set('Schedule not set.')
    box2sched_stat=Label(tab2, textvariable=box2sched_text, anchor=W, justify=LEFT)
        # phase 1
    phaseLabel2_1 = Label(tab2, text='Phase 1')
    dateLabel = time.strftime('%H:%M   %Y/%m/%d') # reads time for Phase 1 start-time
    fromLabel2_1 = Label(tab2, text='From:')
    date_label2 = Label(tab2, text=dateLabel)
    rad2_A_1 = Radiobutton(tab2, text='LD', variable=var2_1, value=1)
    lbl2_A_1 = Label(tab2, text= 'On:')
    spin2_A_1 = Spinbox(tab2, from_=00, to=24, width=3, format='%02.0f')
    spin2_B_1 = Spinbox(tab2, from_=00, to=59, width=3, format='%02.0f')
    spin2_A_1.delete(0,'end')
    spin2_A_1.insert(0,'07')
    spin2_B_1.delete(0,'end')
    spin2_B_1.insert(0,'00')
    label2_h1_1 = Label(tab2, text=':')
    label2_m1_1 = Label(tab2, text='')
    lbl2_B_1 = Label(tab2, text= 'Off:')
    spin2_C_1 = Spinbox(tab2, from_=00, to=24, width=3, format='%02.0f')
    spin2_D_1 = Spinbox(tab2, from_=00, to=59, width=3, format='%02.0f')
    spin2_C_1.delete(0,'end')
    spin2_C_1.insert(0,'19')
    spin2_D_1.delete(0,'end')
    spin2_D_1.insert(0,'00')
    label2_h2_1 = Label(tab2, text=':')
    label2_m2_1 = Label(tab2, text='')
    rad2_B_1 = Radiobutton(tab2, text='DD', variable=var2_1, value=2)
    rad2_C_1 = Radiobutton(tab2, text='LL', variable=var2_1, value=3)
    phaseLabel2_1.grid(column=0, row=1+row_adj, padx=15, pady=5)
    fromLabel2_1.grid(column=1,row=1+row_adj)
    date_label2.grid(column=2, row=1+row_adj, columnspan='10', sticky='w')
    rad2_A_1.grid(column=13, row=1+row_adj, pady=5)
    lbl2_A_1.grid(column=14, row=1+row_adj, pady=5)
    spin2_A_1.grid(column=15,row=1+row_adj, pady=5)
    label2_h1_1.grid(column=16,row=1+row_adj, pady=5, sticky='w')
    spin2_B_1.grid(column=17,row=1+row_adj, pady=5)
    label2_m1_1.grid(column=18,row=1+row_adj, pady=5, sticky='w')
    lbl2_B_1.grid(column=19, row=1+row_adj, pady=5)
    spin2_C_1.grid(column=20,row=1+row_adj, pady=5)
    label2_h2_1.grid(column=21,row=1+row_adj, pady=5, sticky='w')
    spin2_D_1.grid(column=22,row=1+row_adj, pady=5)
    label2_m2_1.grid(column=23,row=1+row_adj, pady=5, sticky='w')
    rad2_B_1.grid(column=24, row=1+row_adj, padx=15, pady=5)
    rad2_C_1.grid(column=25, row=1+row_adj, pady=5)
    
        # phase 2
    phaseLabel2_2 = Label(tab2, text='Phase 2')
    fromLabel2_2 = Label(tab2, text='From:')
    space2_2 = Label(tab2, text=' ')
    space2_2_2 = Label(tab2, text=' ')
    spin2_E_2 = Spinbox(tab2, from_=00, to=24, width=3, format='%02.0f')
    spin2_F_2 = Spinbox(tab2, from_=00, to=59, width=3, format='%02.0f')
    spin2_E_2.delete(0,'end')
    spin2_E_2.insert(0,'07')
    spin2_F_2.delete(0,'end')
    spin2_F_2.insert(0,'00')
    label2_h0_2 = Label(tab2, text=':')
    label2_m0_2 = Label(tab2, text='')
    date2_2_entry = Spinbox(tab2, from_=00, to=31, width=3, format='%02.0f')
    month2_2_entry = Spinbox(tab2, from_=00, to=12, width=3, format='%02.0f')
    year2_2_entry = Spinbox(tab2, from_=2018, to=2030, width=5)
    date2_2_entry.delete(0,'end')
    today=datetime.date.today() # today
    day_phase2 = today + datetime.timedelta(days=7) # calculate dates for 7 days after recording initiation
    date2_2_entry.insert(0,'{:02d}'.format(day_phase2.day))
    month2_2_entry.delete(0,'end')
    month2_2_entry.insert(0,'{:02d}'.format(day_phase2.month))
    year2_2_entry.delete(0,'end')
    year2_2_entry.insert(0,day_phase2.year) # ISO format is YYYY/MM/DD
    
    label2_d_0 = Label(tab2, text= 'Month')
    label2_m_0 = Label(tab2, text= 'Date')
    label2_m_0.grid(column=11,row=2+row_adj)
    label2_d_0.grid(column=9,row=2+row_adj)
    label1_d_1 = Label(tab2, text= '/')
    label1_m_1 = Label(tab2, text= '/')
    label1_d_1.grid(column=8,row=2+row_adj)
    label1_m_1.grid(column=10,row=2+row_adj)
    
    label2_d_2 = Label(tab2, text= '/')
    label2_m_2 = Label(tab2, text= '/')
    rad2_A_2 = Radiobutton(tab2, text='LD', variable=var2_2, value=1)
    lbl2_A_2 = Label(tab2, text= 'On:')
    spin2_A_2 = Spinbox(tab2, from_=00, to=24, width=3, format='%02.0f')
    spin2_B_2 = Spinbox(tab2, from_=00, to=59, width=3, format='%02.0f')
    spin2_A_2.delete(0,'end')
    spin2_A_2.insert(0,'07')
    spin2_B_2.delete(0,'end')
    spin2_B_2.insert(0,'00')
    label2_h1_2 = Label(tab2, text=':')
    label2_m1_2 = Label(tab2, text='')
    lbl2_B_2 = Label(tab2, text= 'Off:')
    spin2_C_2 = Spinbox(tab2, from_=00, to=24, width=3, format='%02.0f')
    spin2_D_2 = Spinbox(tab2, from_=00, to=59, width=3, format='%02.0f')
    spin2_C_2.delete(0,'end')
    spin2_C_2.insert(0,'19')
    spin2_D_2.delete(0,'end')
    spin2_D_2.insert(0,'00')
    label2_h2_2 = Label(tab2, text=':')
    label2_m2_2 = Label(tab2, text='')
    rad2_B_2 = Radiobutton(tab2, text='DD', variable=var2_2, value=2)
    rad2_C_2 = Radiobutton(tab2, text='LL', variable=var2_2, value=3)
    phaseLabel2_2.grid(column=0, row=3+row_adj, padx=15, pady=5)
    fromLabel2_2.grid(column=1,row=3+row_adj)
    spin2_E_2.grid(column=2,row=3+row_adj)
    label2_h0_2.grid(column=3,row=3+row_adj)
    spin2_F_2.grid(column=4,row=3+row_adj)
    label2_m0_2.grid(column=5,row=3+row_adj)
    space2_2.grid(column=6,row=3+row_adj)
    date2_2_entry.grid(column=11, row=3+row_adj)
    label2_d_2.grid(column=8,row=3+row_adj)
    month2_2_entry.grid(column=9, row=3+row_adj)
    label2_m_2.grid(column=10,row=3+row_adj)
    year2_2_entry.grid(column=7, row=3+row_adj) # ISO format
    space2_2_2.grid(column=12,row=3+row_adj,padx=5)
    rad2_A_2.grid(column=13, row=3+row_adj, pady=5)
    lbl2_A_2.grid(column=14, row=3+row_adj, pady=5)
    spin2_A_2.grid(column=15,row=3+row_adj, pady=5)
    label2_h1_2.grid(column=16,row=3+row_adj, pady=5)
    spin2_B_2.grid(column=17,row=3+row_adj, pady=5)
    label2_m1_2.grid(column=18,row=3+row_adj, pady=5)
    lbl2_B_2.grid(column=19, row=3+row_adj, pady=5)
    spin2_C_2.grid(column=20,row=3+row_adj, pady=5)
    label2_h2_2.grid(column=21,row=3+row_adj, pady=5)
    spin2_D_2.grid(column=22,row=3+row_adj, pady=5)
    label2_m2_2.grid(column=23,row=3+row_adj, pady=5)
    rad2_B_2.grid(column=24, row=3+row_adj, padx=15, pady=5)
    rad2_C_2.grid(column=25, row=3+row_adj, pady=5)
        # phase 3
    phaseLabel2_3 = Label(tab2, text='Phase 3')
    fromLabel2_3 = Label(tab2, text='From:')
    space2_3 = Label(tab2, text=' ')
    spin2_E_3 = Spinbox(tab2, from_=00, to=24, width=3, format='%02.0f')
    spin2_F_3 = Spinbox(tab2, from_=00, to=59, width=3, format='%02.0f')
    spin2_E_3.delete(0,'end')
    spin2_E_3.insert(0,'07')
    spin2_F_3.delete(0,'end')
    spin2_F_3.insert(0,'00')
    label2_h0_3 = Label(tab2, text=':')
    label2_m0_3 = Label(tab2, text='')
    date2_3_entry = Spinbox(tab2, from_=00, to=31, width=3, format='%02.0f')
    month2_3_entry = Spinbox(tab2, from_=00, to=12, width=3, format='%02.0f')
    year2_3_entry = Spinbox(tab2, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase3 = day_phase2 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date2_3_entry.delete(0,'end')
    date2_3_entry.insert(0,'{:02d}'.format(day_phase3.day))
    month2_3_entry.delete(0,'end')
    month2_3_entry.insert(0,'{:02d}'.format(day_phase3.month))
    year2_3_entry.delete(0,'end')
    year2_3_entry.insert(0,day_phase3.year)
    label2_d_3 = Label(tab2, text= '/')
    label2_m_3 = Label(tab2, text= '/')
    rad2_A_3 = Radiobutton(tab2, text='LD', variable=var2_3, value=1)
    lbl2_A_3 = Label(tab2, text= 'On:')
    spin2_A_3 = Spinbox(tab2, from_=00, to=24, width=3, format='%02.0f')
    spin2_B_3 = Spinbox(tab2, from_=00, to=59, width=3, format='%02.0f')
    spin2_A_3.delete(0,'end')
    spin2_A_3.insert(0,'07')
    spin2_B_3.delete(0,'end')
    spin2_B_3.insert(0,'00')
    label2_h1_3 = Label(tab2, text=':')
    label2_m1_3 = Label(tab2, text='')
    lbl2_B_3 = Label(tab2, text= 'Off:')
    spin2_C_3 = Spinbox(tab2, from_=00, to=24, width=3, format='%02.0f')
    spin2_D_3 = Spinbox(tab2, from_=00, to=59, width=3, format='%02.0f')
    spin2_C_3.delete(0,'end')
    spin2_C_3.insert(0,'19')
    spin2_D_3.delete(0,'end')
    spin2_D_3.insert(0,'00')
    label2_h2_3 = Label(tab2, text=':')
    label2_m2_3 = Label(tab2, text='')
    rad2_B_3 = Radiobutton(tab2, text='DD', variable=var2_3, value=2)
    rad2_C_3 = Radiobutton(tab2, text='LL', variable=var2_3, value=3)
    phaseLabel2_3.grid(column=0, row=4+row_adj, padx=15, pady=5)
    fromLabel2_3.grid(column=1,row=4+row_adj)
    spin2_E_3.grid(column=2,row=4+row_adj)
    label2_h0_3.grid(column=3,row=4+row_adj)
    spin2_F_3.grid(column=4,row=4+row_adj)
    label2_m0_3.grid(column=5,row=4+row_adj)
    space2_3.grid(column=6,row=4+row_adj)
    date2_3_entry.grid(column=11, row=4+row_adj)
    label2_d_3.grid(column=8,row=4+row_adj)
    month2_3_entry.grid(column=9, row=4+row_adj)
    label2_m_3.grid(column=10,row=4+row_adj)
    year2_3_entry.grid(column=7, row=4+row_adj) # ISO format
    rad2_A_3.grid(column=13, row=4+row_adj, pady=5)
    lbl2_A_3.grid(column=14, row=4+row_adj, pady=5)
    spin2_A_3.grid(column=15,row=4+row_adj, pady=5)
    label2_h1_3.grid(column=16,row=4+row_adj, pady=5)
    spin2_B_3.grid(column=17,row=4+row_adj, pady=5)
    label2_m1_3.grid(column=18,row=4+row_adj, pady=5)
    lbl2_B_3.grid(column=19, row=4+row_adj, pady=5)
    spin2_C_3.grid(column=20,row=4+row_adj, pady=5)
    label2_h2_3.grid(column=21,row=4+row_adj, pady=5)
    spin2_D_3.grid(column=22,row=4+row_adj, pady=5)
    label2_m2_3.grid(column=23,row=4+row_adj, pady=5)
    rad2_B_3.grid(column=24, row=4+row_adj, padx=15, pady=5)
    rad2_C_3.grid(column=25, row=4+row_adj, pady=5)

        # phase 4
    phaseLabel2_4 = Label(tab2, text='Phase 4')
    fromLabel2_4 = Label(tab2, text='From:')
    space2_4 = Label(tab2, text=' ')
    spin2_E_4 = Spinbox(tab2, from_=00, to=24, width=3, format='%02.0f')
    spin2_F_4 = Spinbox(tab2, from_=00, to=59, width=3, format='%02.0f')
    spin2_E_4.delete(0,'end')
    spin2_E_4.insert(0,'07')
    spin2_F_4.delete(0,'end')
    spin2_F_4.insert(0,'00')
    label2_h0_4 = Label(tab2, text=':')
    label2_m0_4 = Label(tab2, text='')
    date2_4_entry = Spinbox(tab2, from_=00, to=31, width=3, format='%02.0f')
    month2_4_entry = Spinbox(tab2, from_=00, to=12, width=3, format='%02.0f')
    year2_4_entry = Spinbox(tab2, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase4 = day_phase3 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date2_4_entry.delete(0,'end')
    date2_4_entry.insert(0,'{:02d}'.format(day_phase4.day))
    month2_4_entry.delete(0,'end')
    month2_4_entry.insert(0,'{:02d}'.format(day_phase4.month))
    year2_4_entry.delete(0,'end')
    year2_4_entry.insert(0,day_phase4.year)
    label2_d_4 = Label(tab2, text= '/')
    label2_m_4 = Label(tab2, text= '/')
    rad2_A_4 = Radiobutton(tab2, text='LD', variable=var2_4, value=1)
    lbl2_A_4 = Label(tab2, text= 'On:')
    spin2_A_4 = Spinbox(tab2, from_=00, to=24, width=3, format='%02.0f')
    spin2_B_4 = Spinbox(tab2, from_=00, to=59, width=3, format='%02.0f')
    spin2_A_4.delete(0,'end')
    spin2_A_4.insert(0,'07')
    spin2_B_4.delete(0,'end')
    spin2_B_4.insert(0,'00')
    label2_h1_4 = Label(tab2, text=':')
    label2_m1_4 = Label(tab2, text='')
    lbl2_B_4 = Label(tab2, text= 'Off:')
    spin2_C_4 = Spinbox(tab2, from_=00, to=24, width=3, format='%02.0f')
    spin2_D_4 = Spinbox(tab2, from_=00, to=59, width=3, format='%02.0f')
    spin2_C_4.delete(0,'end')
    spin2_C_4.insert(0,'19')
    spin2_D_4.delete(0,'end')
    spin2_D_4.insert(0,'00')
    label2_h2_4 = Label(tab2, text=':')
    label2_m2_4 = Label(tab2, text='')
    rad2_B_4 = Radiobutton(tab2, text='DD', variable=var2_4, value=2)
    rad2_C_4 = Radiobutton(tab2, text='LL', variable=var2_4, value=3)
    phaseLabel2_4.grid(column=0, row=5+row_adj, padx=15, pady=5)
    fromLabel2_4.grid(column=1,row=5+row_adj)
    spin2_E_4.grid(column=2,row=5+row_adj)
    label2_h0_4.grid(column=3,row=5+row_adj)
    spin2_F_4.grid(column=4,row=5+row_adj)
    label2_m0_4.grid(column=5,row=5+row_adj)
    space2_4.grid(column=6,row=5+row_adj)
    date2_4_entry.grid(column=11, row=5+row_adj)
    label2_d_4.grid(column=8,row=5+row_adj)
    month2_4_entry.grid(column=9, row=5+row_adj)
    label2_m_4.grid(column=10,row=5+row_adj)
    year2_4_entry.grid(column=7, row=5+row_adj) # ISO format
    rad2_A_4.grid(column=13, row=5+row_adj, pady=5)
    lbl2_A_4.grid(column=14, row=5+row_adj, pady=5)
    spin2_A_4.grid(column=15,row=5+row_adj, pady=5)
    label2_h1_4.grid(column=16,row=5+row_adj, pady=5)
    spin2_B_4.grid(column=17,row=5+row_adj, pady=5)
    label2_m1_4.grid(column=18,row=5+row_adj, pady=5)
    lbl2_B_4.grid(column=19, row=5+row_adj, pady=5)
    spin2_C_4.grid(column=20,row=5+row_adj, pady=5)
    label2_h2_4.grid(column=21,row=5+row_adj, pady=5)
    spin2_D_4.grid(column=22,row=5+row_adj, pady=5)
    label2_m2_4.grid(column=23,row=5+row_adj, pady=5)
    rad2_B_4.grid(column=24, row=5+row_adj, padx=15, pady=5)
    rad2_C_4.grid(column=25, row=5+row_adj, pady=5)
    
    # Phase 5
    phaseLabel2_5 = Label(tab2, text='Phase 5')
    fromLabel2_5 = Label(tab2, text='From:')
    space2_5 = Label(tab2, text=' ')
    space2_5_2 = Label(tab2, text=' ')
    spin2_E_5 = Spinbox(tab2, from_=00, to=24, width=3, format='%02.0f')
    spin2_F_5 = Spinbox(tab2, from_=00, to=59, width=3, format='%02.0f')
    spin2_E_5.delete(0,'end')
    spin2_E_5.insert(0,'07')
    spin2_F_5.delete(0,'end')
    spin2_F_5.insert(0,'00')
    label2_h0_5 = Label(tab2, text=':')
    label2_m0_5 = Label(tab2, text='')
    date2_5_entry = Spinbox(tab2, from_=00, to=31, width=3, format='%02.0f')
    month2_5_entry = Spinbox(tab2, from_=00, to=12, width=3, format='%02.0f')
    year2_5_entry = Spinbox(tab2, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase5 = day_phase4 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date2_5_entry.delete(0,'end')
    date2_5_entry.insert(0,'{:02d}'.format(day_phase5.day))
    month2_5_entry.delete(0,'end')
    month2_5_entry.insert(0,'{:02d}'.format(day_phase5.month))
    year2_5_entry.delete(0,'end')
    year2_5_entry.insert(0,day_phase5.year)
    label2_d_5 = Label(tab2, text= '/')
    label2_m_5 = Label(tab2, text= '/')
    rad2_A_5 = Radiobutton(tab2, text='LD', variable=var2_5, value=1)
    lbl2_A_5 = Label(tab2, text= 'On:')
    spin2_A_5 = Spinbox(tab2, from_=00, to=24, width=3, format='%02.0f')
    spin2_B_5 = Spinbox(tab2, from_=00, to=59, width=3, format='%02.0f')
    spin2_A_5.delete(0,'end')
    spin2_A_5.insert(0,'07')
    spin2_B_5.delete(0,'end')
    spin2_B_5.insert(0,'00')
    label2_h1_5 = Label(tab2, text=':')
    label2_m1_5 = Label(tab2, text='')
    lbl2_B_5 = Label(tab2, text= 'Off:')
    spin2_C_5 = Spinbox(tab2, from_=00, to=24, width=3, format='%02.0f')
    spin2_D_5 = Spinbox(tab2, from_=00, to=59, width=3, format='%02.0f')
    spin2_C_5.delete(0,'end')
    spin2_C_5.insert(0,'19')
    spin2_D_5.delete(0,'end')
    spin2_D_5.insert(0,'00')
    label2_h2_5 = Label(tab2, text=':')
    label2_m2_5 = Label(tab2, text='')
    rad2_B_5 = Radiobutton(tab2, text='DD', variable=var2_5, value=2)
    rad2_C_5 = Radiobutton(tab2, text='LL', variable=var2_5, value=3)
    phaseLabel2_5.grid(column=0, row=6+row_adj, padx=15, pady=5)
    fromLabel2_5.grid(column=1,row=6+row_adj)
    spin2_E_5.grid(column=2,row=6+row_adj)
    label2_h0_5.grid(column=3,row=6+row_adj)
    spin2_F_5.grid(column=4,row=6+row_adj)
    label2_m0_5.grid(column=5,row=6+row_adj)
    space2_5.grid(column=6,row=6+row_adj)
    date2_5_entry.grid(column=11, row=6+row_adj)
    label2_d_5.grid(column=8,row=6+row_adj)
    month2_5_entry.grid(column=9, row=6+row_adj)
    label2_m_5.grid(column=10,row=6+row_adj)
    year2_5_entry.grid(column=7, row=6+row_adj) # ISO format
    space2_5_2.grid(column=12,row=6+row_adj,padx=5)
    rad2_A_5.grid(column=13, row=6+row_adj, pady=5)
    lbl2_A_5.grid(column=14, row=6+row_adj, pady=5)
    spin2_A_5.grid(column=15,row=6+row_adj, pady=5)
    label2_h1_5.grid(column=16,row=6+row_adj, pady=5)
    spin2_B_5.grid(column=17,row=6+row_adj, pady=5)
    label2_m1_5.grid(column=18,row=6+row_adj, pady=5)
    lbl2_B_5.grid(column=19, row=6+row_adj, pady=5)
    spin2_C_5.grid(column=20,row=6+row_adj, pady=5)
    label2_h2_5.grid(column=21,row=6+row_adj, pady=5)
    spin2_D_5.grid(column=22,row=6+row_adj, pady=5)
    label2_m2_5.grid(column=23,row=6+row_adj, pady=5)
    rad2_B_5.grid(column=24, row=6+row_adj, padx=15, pady=5)
    rad2_C_5.grid(column=25, row=6+row_adj, pady=5)

    # Phase 6
    phaseLabel2_6 = Label(tab2, text='Phase 6')
    fromLabel2_6 = Label(tab2, text='From:')
    space2_6 = Label(tab2, text=' ')
    space2_6_2 = Label(tab2, text=' ')
    spin2_E_6 = Spinbox(tab2, from_=00, to=24, width=3, format='%02.0f')
    spin2_F_6 = Spinbox(tab2, from_=00, to=59, width=3, format='%02.0f')
    spin2_E_6.delete(0,'end')
    spin2_E_6.insert(0,'07')
    spin2_F_6.delete(0,'end')
    spin2_F_6.insert(0,'00')
    label2_h0_6 = Label(tab2, text=':')
    label2_m0_6 = Label(tab2, text='')
    date2_6_entry = Spinbox(tab2, from_=00, to=31, width=3, format='%02.0f')
    month2_6_entry = Spinbox(tab2, from_=00, to=12, width=3, format='%02.0f')
    year2_6_entry = Spinbox(tab2, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase6 = day_phase5 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date2_6_entry.delete(0,'end')
    date2_6_entry.insert(0,'{:02d}'.format(day_phase6.day))
    month2_6_entry.delete(0,'end')
    month2_6_entry.insert(0,'{:02d}'.format(day_phase6.month))
    year2_6_entry.delete(0,'end')
    year2_6_entry.insert(0,day_phase6.year)
    label2_d_6 = Label(tab2, text= '/')
    label2_m_6 = Label(tab2, text= '/')
    rad2_A_6 = Radiobutton(tab2, text='LD', variable=var2_6, value=1)
    lbl2_A_6 = Label(tab2, text= 'On:')
    spin2_A_6 = Spinbox(tab2, from_=00, to=24, width=3, format='%02.0f')
    spin2_B_6 = Spinbox(tab2, from_=00, to=59, width=3, format='%02.0f')
    spin2_A_6.delete(0,'end')
    spin2_A_6.insert(0,'07')
    spin2_B_6.delete(0,'end')
    spin2_B_6.insert(0,'00')
    label2_h1_6 = Label(tab2, text=':')
    label2_m1_6 = Label(tab2, text='')
    lbl2_B_6 = Label(tab2, text= 'Off:')
    spin2_C_6 = Spinbox(tab2, from_=00, to=24, width=3, format='%02.0f')
    spin2_D_6 = Spinbox(tab2, from_=00, to=59, width=3, format='%02.0f')
    spin2_C_6.delete(0,'end')
    spin2_C_6.insert(0,'19')
    spin2_D_6.delete(0,'end')
    spin2_D_6.insert(0,'00')
    label2_h2_6 = Label(tab2, text=':')
    label2_m2_6 = Label(tab2, text='')
    rad2_B_6 = Radiobutton(tab2, text='DD', variable=var2_6, value=2)
    rad2_C_6 = Radiobutton(tab2, text='LL', variable=var2_6, value=3)

    phaseLabel2_6.grid(column=0, row=rowPhase6+row_adj, padx=15, pady=5)
    fromLabel2_6.grid(column=1,row=rowPhase6+row_adj)
    spin2_E_6.grid(column=2,row=rowPhase6+row_adj)
    label2_h0_6.grid(column=3,row=rowPhase6+row_adj)
    spin2_F_6.grid(column=4,row=rowPhase6+row_adj)
    label2_m0_6.grid(column=5,row=rowPhase6+row_adj)
    space2_6.grid(column=6,row=rowPhase6+row_adj)
    date2_6_entry.grid(column=11, row=rowPhase6+row_adj)
    label2_d_6.grid(column=8,row=rowPhase6+row_adj)
    month2_6_entry.grid(column=9, row=rowPhase6+row_adj)
    label2_m_6.grid(column=10,row=rowPhase6+row_adj)
    year2_6_entry.grid(column=7, row=rowPhase6+row_adj) # ISO format
    space2_6_2.grid(column=12,row=rowPhase6+row_adj,padx=5)
    rad2_A_6.grid(column=13, row=rowPhase6+row_adj, pady=5)
    lbl2_A_6.grid(column=14, row=rowPhase6+row_adj, pady=5)
    spin2_A_6.grid(column=15,row=rowPhase6+row_adj, pady=5)
    label2_h1_6.grid(column=16,row=rowPhase6+row_adj, pady=5)
    spin2_B_6.grid(column=17,row=rowPhase6+row_adj, pady=5)
    label2_m1_6.grid(column=18,row=rowPhase6+row_adj, pady=5)
    lbl2_B_6.grid(column=19, row=rowPhase6+row_adj, pady=5)
    spin2_C_6.grid(column=20,row=rowPhase6+row_adj, pady=5)
    label2_h2_6.grid(column=21,row=rowPhase6+row_adj, pady=5)
    spin2_D_6.grid(column=22,row=rowPhase6+row_adj, pady=5)
    label2_m2_6.grid(column=23,row=rowPhase6+row_adj, pady=5)
    rad2_B_6.grid(column=24, row=rowPhase6+row_adj, padx=15, pady=5)
    rad2_C_6.grid(column=25, row=rowPhase6+row_adj, pady=5)

        # Phase 7
    phaseLabel2_7 = Label(tab2, text='Phase 7')
    fromLabel2_7 = Label(tab2, text='From:')
    space2_7 = Label(tab2, text=' ')
    space2_7_2 = Label(tab2, text=' ')
    spin2_E_7 = Spinbox(tab2, from_=00, to=24, width=3, format='%02.0f')
    spin2_F_7 = Spinbox(tab2, from_=00, to=59, width=3, format='%02.0f')
    spin2_E_7.delete(0,'end')
    spin2_E_7.insert(0,'07')
    spin2_F_7.delete(0,'end')
    spin2_F_7.insert(0,'00')
    label2_h0_7 = Label(tab2, text=':')
    label2_m0_7 = Label(tab2, text='')
    date2_7_entry = Spinbox(tab2, from_=00, to=31, width=3, format='%02.0f')
    month2_7_entry = Spinbox(tab2, from_=00, to=12, width=3, format='%02.0f')
    year2_7_entry = Spinbox(tab2, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase7 = day_phase6 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date2_7_entry.delete(0,'end')
    date2_7_entry.insert(0,'{:02d}'.format(day_phase7.day))
    month2_7_entry.delete(0,'end')
    month2_7_entry.insert(0,'{:02d}'.format(day_phase7.month))
    year2_7_entry.delete(0,'end')
    year2_7_entry.insert(0,day_phase7.year)
    label2_d_7 = Label(tab2, text= '/')
    label2_m_7 = Label(tab2, text= '/')
    rad2_A_7 = Radiobutton(tab2, text='LD', variable=var2_7, value=1)
    lbl2_A_7 = Label(tab2, text= 'On:')
    spin2_A_7 = Spinbox(tab2, from_=00, to=24, width=3, format='%02.0f')
    spin2_B_7 = Spinbox(tab2, from_=00, to=59, width=3, format='%02.0f')
    spin2_A_7.delete(0,'end')
    spin2_A_7.insert(0,'07')
    spin2_B_7.delete(0,'end')
    spin2_B_7.insert(0,'00')
    label2_h1_7 = Label(tab2, text=':')
    label2_m1_7 = Label(tab2, text='')
    lbl2_B_7 = Label(tab2, text= 'Off:')
    spin2_C_7 = Spinbox(tab2, from_=00, to=24, width=3, format='%02.0f')
    spin2_D_7 = Spinbox(tab2, from_=00, to=59, width=3, format='%02.0f')
    spin2_C_7.delete(0,'end')
    spin2_C_7.insert(0,'19')
    spin2_D_7.delete(0,'end')
    spin2_D_7.insert(0,'00')
    label2_h2_7 = Label(tab2, text=':')
    label2_m2_7 = Label(tab2, text='')
    rad2_B_7 = Radiobutton(tab2, text='DD', variable=var2_7, value=2)
    rad2_C_7 = Radiobutton(tab2, text='LL', variable=var2_7, value=3)

    phaseLabel2_7.grid(column=0, row=rowPhase7+row_adj, padx=15, pady=5)
    fromLabel2_7.grid(column=1,row=rowPhase7+row_adj)
    spin2_E_7.grid(column=2,row=rowPhase7+row_adj)
    label2_h0_7.grid(column=3,row=rowPhase7+row_adj)
    spin2_F_7.grid(column=4,row=rowPhase7+row_adj)
    label2_m0_7.grid(column=5,row=rowPhase7+row_adj)
    space2_7.grid(column=6,row=rowPhase7+row_adj)
    date2_7_entry.grid(column=11, row=rowPhase7+row_adj)
    label2_d_7.grid(column=8,row=rowPhase7+row_adj)
    month2_7_entry.grid(column=9, row=rowPhase7+row_adj)
    label2_m_7.grid(column=10,row=rowPhase7+row_adj)
    year2_7_entry.grid(column=7, row=rowPhase7+row_adj) # ISO format
    space2_7_2.grid(column=12,row=rowPhase7+row_adj,padx=5)
    rad2_A_7.grid(column=13, row=rowPhase7+row_adj, pady=5)
    lbl2_A_7.grid(column=14, row=rowPhase7+row_adj, pady=5)
    spin2_A_7.grid(column=15,row=rowPhase7+row_adj, pady=5)
    label2_h1_7.grid(column=16,row=rowPhase7+row_adj, pady=5)
    spin2_B_7.grid(column=17,row=rowPhase7+row_adj, pady=5)
    label2_m1_7.grid(column=18,row=rowPhase7+row_adj, pady=5)
    lbl2_B_7.grid(column=19, row=rowPhase7+row_adj, pady=5)
    spin2_C_7.grid(column=20,row=rowPhase7+row_adj, pady=5)
    label2_h2_7.grid(column=21,row=rowPhase7+row_adj, pady=5)
    spin2_D_7.grid(column=22,row=rowPhase7+row_adj, pady=5)
    label2_m2_7.grid(column=23,row=rowPhase7+row_adj, pady=5)
    rad2_B_7.grid(column=24, row=rowPhase7+row_adj, padx=15, pady=5)
    rad2_C_7.grid(column=25, row=rowPhase7+row_adj, pady=5)

        # Phase 8
    phaseLabel2_8 = Label(tab2, text='Phase 8')
    fromLabel2_8 = Label(tab2, text='From:')
    space2_8 = Label(tab2, text=' ')
    space2_8_2 = Label(tab2, text=' ')
    spin2_E_8 = Spinbox(tab2, from_=00, to=24, width=3, format='%02.0f')
    spin2_F_8 = Spinbox(tab2, from_=00, to=59, width=3, format='%02.0f')
    spin2_E_8.delete(0,'end')
    spin2_E_8.insert(0,'07')
    spin2_F_8.delete(0,'end')
    spin2_F_8.insert(0,'00')
    label2_h0_8 = Label(tab2, text=':')
    label2_m0_8 = Label(tab2, text='')
    date2_8_entry = Spinbox(tab2, from_=00, to=31, width=3, format='%02.0f')
    month2_8_entry = Spinbox(tab2, from_=00, to=12, width=3, format='%02.0f')
    year2_8_entry = Spinbox(tab2, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase8 = day_phase7 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date2_8_entry.delete(0,'end')
    date2_8_entry.insert(0,'{:02d}'.format(day_phase8.day))
    month2_8_entry.delete(0,'end')
    month2_8_entry.insert(0,'{:02d}'.format(day_phase8.month))
    year2_8_entry.delete(0,'end')
    year2_8_entry.insert(0,day_phase8.year)
    label2_d_8 = Label(tab2, text= '/')
    label2_m_8 = Label(tab2, text= '/')
    rad2_A_8 = Radiobutton(tab2, text='LD', variable=var2_8, value=1)
    lbl2_A_8 = Label(tab2, text= 'On:')
    spin2_A_8 = Spinbox(tab2, from_=00, to=24, width=3, format='%02.0f')
    spin2_B_8 = Spinbox(tab2, from_=00, to=59, width=3, format='%02.0f')
    spin2_A_8.delete(0,'end')
    spin2_A_8.insert(0,'07')
    spin2_B_8.delete(0,'end')
    spin2_B_8.insert(0,'00')
    label2_h1_8 = Label(tab2, text=':')
    label2_m1_8 = Label(tab2, text='')
    lbl2_B_8 = Label(tab2, text= 'Off:')
    spin2_C_8 = Spinbox(tab2, from_=00, to=24, width=3, format='%02.0f')
    spin2_D_8 = Spinbox(tab2, from_=00, to=59, width=3, format='%02.0f')
    spin2_C_8.delete(0,'end')
    spin2_C_8.insert(0,'19')
    spin2_D_8.delete(0,'end')
    spin2_D_8.insert(0,'00')
    label2_h2_8 = Label(tab2, text=':')
    label2_m2_8 = Label(tab2, text='')
    rad2_B_8 = Radiobutton(tab2, text='DD', variable=var2_8, value=2)
    rad2_C_8 = Radiobutton(tab2, text='LL', variable=var2_8, value=3)

    phaseLabel2_8.grid(column=0, row=rowPhase8+row_adj, padx=15, pady=5)
    fromLabel2_8.grid(column=1,row=rowPhase8+row_adj)
    spin2_E_8.grid(column=2,row=rowPhase8+row_adj)
    label2_h0_8.grid(column=3,row=rowPhase8+row_adj)
    spin2_F_8.grid(column=4,row=rowPhase8+row_adj)
    label2_m0_8.grid(column=5,row=rowPhase8+row_adj)
    space2_8.grid(column=6,row=rowPhase8+row_adj)
    date2_8_entry.grid(column=11, row=rowPhase8+row_adj)
    label2_d_8.grid(column=8,row=rowPhase8+row_adj)
    month2_8_entry.grid(column=9, row=rowPhase8+row_adj)
    label2_m_8.grid(column=10,row=rowPhase8+row_adj)
    year2_8_entry.grid(column=7, row=rowPhase8+row_adj) # ISO format
    space2_8_2.grid(column=12,row=rowPhase8+row_adj,padx=5)
    rad2_A_8.grid(column=13, row=rowPhase8+row_adj, pady=5)
    lbl2_A_8.grid(column=14, row=rowPhase8+row_adj, pady=5)
    spin2_A_8.grid(column=15,row=rowPhase8+row_adj, pady=5)
    label2_h1_8.grid(column=16,row=rowPhase8+row_adj, pady=5)
    spin2_B_8.grid(column=17,row=rowPhase8+row_adj, pady=5)
    label2_m1_8.grid(column=18,row=rowPhase8+row_adj, pady=5)
    lbl2_B_8.grid(column=19, row=rowPhase8+row_adj, pady=5)
    spin2_C_8.grid(column=20,row=rowPhase8+row_adj, pady=5)
    label2_h2_8.grid(column=21,row=rowPhase8+row_adj, pady=5)
    spin2_D_8.grid(column=22,row=rowPhase8+row_adj, pady=5)
    label2_m2_8.grid(column=23,row=rowPhase8+row_adj, pady=5)
    rad2_B_8.grid(column=24, row=rowPhase8+row_adj, padx=15, pady=5)
    rad2_C_8.grid(column=25, row=rowPhase8+row_adj, pady=5)
    
    # Phase 9
    phaseLabel2_9 = Label(tab2, text='Phase 9')
    fromLabel2_9 = Label(tab2, text='From:')
    space2_9 = Label(tab2, text=' ')
    space2_9_2 = Label(tab2, text=' ')
    spin2_E_9 = Spinbox(tab2, from_=00, to=24, width=3, format='%02.0f')
    spin2_F_9 = Spinbox(tab2, from_=00, to=59, width=3, format='%02.0f')
    spin2_E_9.delete(0,'end')
    spin2_E_9.insert(0,'07')
    spin2_F_9.delete(0,'end')
    spin2_F_9.insert(0,'00')
    label2_h0_9 = Label(tab2, text=':')
    label2_m0_9 = Label(tab2, text='')
    date2_9_entry = Spinbox(tab2, from_=00, to=31, width=3, format='%02.0f')
    month2_9_entry = Spinbox(tab2, from_=00, to=12, width=3, format='%02.0f')
    year2_9_entry = Spinbox(tab2, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase9 = day_phase8 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date2_9_entry.delete(0,'end')
    date2_9_entry.insert(0,'{:02d}'.format(day_phase9.day))
    month2_9_entry.delete(0,'end')
    month2_9_entry.insert(0,'{:02d}'.format(day_phase9.month))
    year2_9_entry.delete(0,'end')
    year2_9_entry.insert(0,day_phase9.year)
    label2_d_9 = Label(tab2, text= '/')
    label2_m_9 = Label(tab2, text= '/')
    rad2_A_9 = Radiobutton(tab2, text='LD', variable=var2_9, value=1)
    lbl2_A_9 = Label(tab2, text= 'On:')
    spin2_A_9 = Spinbox(tab2, from_=00, to=24, width=3, format='%02.0f')
    spin2_B_9 = Spinbox(tab2, from_=00, to=59, width=3, format='%02.0f')
    spin2_A_9.delete(0,'end')
    spin2_A_9.insert(0,'07')
    spin2_B_9.delete(0,'end')
    spin2_B_9.insert(0,'00')
    label2_h1_9 = Label(tab2, text=':')
    label2_m1_9 = Label(tab2, text='')
    lbl2_B_9 = Label(tab2, text= 'Off:')
    spin2_C_9 = Spinbox(tab2, from_=00, to=24, width=3, format='%02.0f')
    spin2_D_9 = Spinbox(tab2, from_=00, to=59, width=3, format='%02.0f')
    spin2_C_9.delete(0,'end')
    spin2_C_9.insert(0,'19')
    spin2_D_9.delete(0,'end')
    spin2_D_9.insert(0,'00')
    label2_h2_9 = Label(tab2, text=':')
    label2_m2_9 = Label(tab2, text='')
    rad2_B_9 = Radiobutton(tab2, text='DD', variable=var2_9, value=2)
    rad2_C_9 = Radiobutton(tab2, text='LL', variable=var2_9, value=3)

    phaseLabel2_9.grid(column=0, row=rowPhase9+row_adj, padx=15, pady=5)
    fromLabel2_9.grid(column=1,row=rowPhase9+row_adj)
    spin2_E_9.grid(column=2,row=rowPhase9+row_adj)
    label2_h0_9.grid(column=3,row=rowPhase9+row_adj)
    spin2_F_9.grid(column=4,row=rowPhase9+row_adj)
    label2_m0_9.grid(column=5,row=rowPhase9+row_adj)
    space2_9.grid(column=7,row=rowPhase9+row_adj)
    date2_9_entry.grid(column=11, row=rowPhase9+row_adj)
    label2_d_9.grid(column=8,row=rowPhase9+row_adj)
    month2_9_entry.grid(column=9, row=rowPhase9+row_adj)
    label2_m_9.grid(column=10,row=rowPhase9+row_adj)
    year2_9_entry.grid(column=7, row=rowPhase9+row_adj) # ISO format
    space2_9_2.grid(column=12,row=rowPhase9+row_adj,padx=5)
    rad2_A_9.grid(column=13, row=rowPhase9+row_adj, pady=5)
    lbl2_A_9.grid(column=14, row=rowPhase9+row_adj, pady=5)
    spin2_A_9.grid(column=15,row=rowPhase9+row_adj, pady=5)
    label2_h1_9.grid(column=16,row=rowPhase9+row_adj, pady=5)
    spin2_B_9.grid(column=17,row=rowPhase9+row_adj, pady=5)
    label2_m1_9.grid(column=18,row=rowPhase9+row_adj, pady=5)
    lbl2_B_9.grid(column=19, row=rowPhase9+row_adj, pady=5)
    spin2_C_9.grid(column=20,row=rowPhase9+row_adj, pady=5)
    label2_h2_9.grid(column=21,row=rowPhase9+row_adj, pady=5)
    spin2_D_9.grid(column=22,row=rowPhase9+row_adj, pady=5)
    label2_m2_9.grid(column=23,row=rowPhase9+row_adj, pady=5)
    rad2_B_9.grid(column=24, row=rowPhase9+row_adj, padx=15, pady=5)
    rad2_C_9.grid(column=25, row=rowPhase9+row_adj, pady=5)

    # Phase 10
    phaseLabel2_10 = Label(tab2, text='Phase 10')
    fromLabel2_10 = Label(tab2, text='From:')
    space2_10 = Label(tab2, text=' ')
    space2_10_2 = Label(tab2, text=' ')
    spin2_E_10 = Spinbox(tab2, from_=00, to=24, width=3, format='%02.0f')
    spin2_F_10 = Spinbox(tab2, from_=00, to=59, width=3, format='%02.0f')
    spin2_E_10.delete(0,'end')
    spin2_E_10.insert(0,'07')
    spin2_F_10.delete(0,'end')
    spin2_F_10.insert(0,'00')
    label2_h0_10 = Label(tab2, text=':')
    label2_m0_10 = Label(tab2, text='')
    date2_10_entry = Spinbox(tab2, from_=00, to=31, width=3, format='%02.0f')
    month2_10_entry = Spinbox(tab2, from_=00, to=12, width=3, format='%02.0f')
    year2_10_entry = Spinbox(tab2, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase10 = day_phase9 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date2_10_entry.delete(0,'end')
    date2_10_entry.insert(0,'{:02d}'.format(day_phase10.day))
    month2_10_entry.delete(0,'end')
    month2_10_entry.insert(0,'{:02d}'.format(day_phase10.month))
    year2_10_entry.delete(0,'end')
    year2_10_entry.insert(0,day_phase10.year)
    label2_d_10 = Label(tab2, text= '/')
    label2_m_10 = Label(tab2, text= '/')
    rad2_A_10 = Radiobutton(tab2, text='LD', variable=var2_10, value=1)
    lbl2_A_10 = Label(tab2, text= 'On:')
    spin2_A_10 = Spinbox(tab2, from_=00, to=24, width=3, format='%02.0f')
    spin2_B_10 = Spinbox(tab2, from_=00, to=59, width=3, format='%02.0f')
    spin2_A_10.delete(0,'end')
    spin2_A_10.insert(0,'07')
    spin2_B_10.delete(0,'end')
    spin2_B_10.insert(0,'00')
    label2_h1_10 = Label(tab2, text=':')
    label2_m1_10 = Label(tab2, text='')
    lbl2_B_10 = Label(tab2, text= 'Off:')
    spin2_C_10 = Spinbox(tab2, from_=00, to=24, width=3, format='%02.0f')
    spin2_D_10 = Spinbox(tab2, from_=00, to=59, width=3, format='%02.0f')
    spin2_C_10.delete(0,'end')
    spin2_C_10.insert(0,'19')
    spin2_D_10.delete(0,'end')
    spin2_D_10.insert(0,'00')
    label2_h2_10 = Label(tab2, text=':')
    label2_m2_10 = Label(tab2, text='')
    rad2_B_10 = Radiobutton(tab2, text='DD', variable=var2_10, value=2)
    rad2_C_10 = Radiobutton(tab2, text='LL', variable=var2_10, value=3)

    phaseLabel2_10.grid(column=0, row=rowPhase10+row_adj, padx=15, pady=5)
    fromLabel2_10.grid(column=1,row=rowPhase10+row_adj)
    spin2_E_10.grid(column=2,row=rowPhase10+row_adj)
    label2_h0_10.grid(column=3,row=rowPhase10+row_adj)
    spin2_F_10.grid(column=4,row=rowPhase10+row_adj)
    label2_m0_10.grid(column=5,row=rowPhase10+row_adj)
    space2_10.grid(column=7,row=rowPhase10+row_adj)
    date2_10_entry.grid(column=11, row=rowPhase10+row_adj)
    label2_d_10.grid(column=8,row=rowPhase10+row_adj)
    month2_10_entry.grid(column=9, row=rowPhase10+row_adj)
    label2_m_10.grid(column=10,row=rowPhase10+row_adj)
    year2_10_entry.grid(column=7, row=rowPhase10+row_adj) # ISO format
    space2_10_2.grid(column=12,row=rowPhase10+row_adj,padx=5)
    rad2_A_10.grid(column=13, row=rowPhase10+row_adj, pady=5)
    lbl2_A_10.grid(column=14, row=rowPhase10+row_adj, pady=5)
    spin2_A_10.grid(column=15,row=rowPhase10+row_adj, pady=5)
    label2_h1_10.grid(column=16,row=rowPhase10+row_adj, pady=5)
    spin2_B_10.grid(column=17,row=rowPhase10+row_adj, pady=5)
    label2_m1_10.grid(column=18,row=rowPhase10+row_adj, pady=5)
    lbl2_B_10.grid(column=19, row=rowPhase10+row_adj, pady=5)
    spin2_C_10.grid(column=20,row=rowPhase10+row_adj, pady=5)
    label2_h2_10.grid(column=21,row=rowPhase10+row_adj, pady=5)
    spin2_D_10.grid(column=22,row=rowPhase10+row_adj, pady=5)
    label2_m2_10.grid(column=23,row=rowPhase10+row_adj, pady=5)
    rad2_B_10.grid(column=24, row=rowPhase10+row_adj, padx=15, pady=5)
    rad2_C_10.grid(column=25, row=rowPhase10+row_adj, pady=5)

    # Phase 11
    phaseLabel2_11 = Label(tab2, text='Phase 11')
    fromLabel2_11 = Label(tab2, text='From:')
    space2_11 = Label(tab2, text=' ')
    space2_11_2 = Label(tab2, text=' ')
    spin2_E_11 = Spinbox(tab2, from_=00, to=24, width=3, format='%02.0f')
    spin2_F_11 = Spinbox(tab2, from_=00, to=59, width=3, format='%02.0f')
    spin2_E_11.delete(0,'end')
    spin2_E_11.insert(0,'07')
    spin2_F_11.delete(0,'end')
    spin2_F_11.insert(0,'00')
    label2_h0_11 = Label(tab2, text=':')
    label2_m0_11 = Label(tab2, text='')
    date2_11_entry = Spinbox(tab2, from_=00, to=31, width=3, format='%02.0f')
    month2_11_entry = Spinbox(tab2, from_=00, to=12, width=3, format='%02.0f')
    year2_11_entry = Spinbox(tab2, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase11 = day_phase10 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date2_11_entry.delete(0,'end')
    date2_11_entry.insert(0,'{:02d}'.format(day_phase11.day))
    month2_11_entry.delete(0,'end')
    month2_11_entry.insert(0,'{:02d}'.format(day_phase11.month))
    year2_11_entry.delete(0,'end')
    year2_11_entry.insert(0,day_phase11.year)
    label2_d_11 = Label(tab2, text= '/')
    label2_m_11 = Label(tab2, text= '/')
    rad2_A_11 = Radiobutton(tab2, text='LD', variable=var2_11, value=1)
    lbl2_A_11 = Label(tab2, text= 'On:')
    spin2_A_11 = Spinbox(tab2, from_=00, to=24, width=3, format='%02.0f')
    spin2_B_11 = Spinbox(tab2, from_=00, to=59, width=3, format='%02.0f')
    spin2_A_11.delete(0,'end')
    spin2_A_11.insert(0,'07')
    spin2_B_11.delete(0,'end')
    spin2_B_11.insert(0,'00')
    label2_h1_11 = Label(tab2, text=':')
    label2_m1_11 = Label(tab2, text='')
    lbl2_B_11 = Label(tab2, text= 'Off:')
    spin2_C_11 = Spinbox(tab2, from_=00, to=24, width=3, format='%02.0f')
    spin2_D_11 = Spinbox(tab2, from_=00, to=59, width=3, format='%02.0f')
    spin2_C_11.delete(0,'end')
    spin2_C_11.insert(0,'19')
    spin2_D_11.delete(0,'end')
    spin2_D_11.insert(0,'00')
    label2_h2_11 = Label(tab2, text=':')
    label2_m2_11 = Label(tab2, text='')
    rad2_B_11 = Radiobutton(tab2, text='DD', variable=var2_11, value=2)
    rad2_C_11 = Radiobutton(tab2, text='LL', variable=var2_11, value=3)

    phaseLabel2_11.grid(column=0, row=rowPhase11+row_adj, padx=15, pady=5)
    fromLabel2_11.grid(column=1,row=rowPhase11+row_adj)
    spin2_E_11.grid(column=2,row=rowPhase11+row_adj)
    label2_h0_11.grid(column=3,row=rowPhase11+row_adj)
    spin2_F_11.grid(column=4,row=rowPhase11+row_adj)
    label2_m0_11.grid(column=5,row=rowPhase11+row_adj)
    space2_11.grid(column=7,row=rowPhase11+row_adj)
    date2_11_entry.grid(column=11, row=rowPhase11+row_adj)
    label2_d_11.grid(column=8,row=rowPhase11+row_adj)
    month2_11_entry.grid(column=9, row=rowPhase11+row_adj)
    label2_m_11.grid(column=10,row=rowPhase11+row_adj)
    year2_11_entry.grid(column=7, row=rowPhase11+row_adj) # ISO format
    space2_11_2.grid(column=12,row=rowPhase11+row_adj,padx=5)
    rad2_A_11.grid(column=13, row=rowPhase11+row_adj, pady=5)
    lbl2_A_11.grid(column=14, row=rowPhase11+row_adj, pady=5)
    spin2_A_11.grid(column=15,row=rowPhase11+row_adj, pady=5)
    label2_h1_11.grid(column=16,row=rowPhase11+row_adj, pady=5)
    spin2_B_11.grid(column=17,row=rowPhase11+row_adj, pady=5)
    label2_m1_11.grid(column=18,row=rowPhase11+row_adj, pady=5)
    lbl2_B_11.grid(column=19, row=rowPhase11+row_adj, pady=5)
    spin2_C_11.grid(column=20,row=rowPhase11+row_adj, pady=5)
    label2_h2_11.grid(column=21,row=rowPhase11+row_adj, pady=5)
    spin2_D_11.grid(column=22,row=rowPhase11+row_adj, pady=5)
    label2_m2_11.grid(column=23,row=rowPhase11+row_adj, pady=5)
    rad2_B_11.grid(column=24, row=rowPhase11+row_adj, padx=15, pady=5)
    rad2_C_11.grid(column=25, row=rowPhase11+row_adj, pady=5)

    # Phase 12
    phaseLabel2_12 = Label(tab2, text='Phase 12')
    fromLabel2_12 = Label(tab2, text='From:')
    space2_12 = Label(tab2, text=' ')
    space2_12_2 = Label(tab2, text=' ')
    spin2_E_12 = Spinbox(tab2, from_=00, to=24, width=3, format='%02.0f')
    spin2_F_12 = Spinbox(tab2, from_=00, to=59, width=3, format='%02.0f')
    spin2_E_12.delete(0,'end')
    spin2_E_12.insert(0,'07')
    spin2_F_12.delete(0,'end')
    spin2_F_12.insert(0,'00')
    label2_h0_12 = Label(tab2, text=':')
    label2_m0_12 = Label(tab2, text='')
    date2_12_entry = Spinbox(tab2, from_=00, to=31, width=3, format='%02.0f')
    month2_12_entry = Spinbox(tab2, from_=00, to=12, width=3, format='%02.0f')
    year2_12_entry = Spinbox(tab2, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase12 = day_phase11 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date2_12_entry.delete(0,'end')
    date2_12_entry.insert(0,'{:02d}'.format(day_phase12.day))
    month2_12_entry.delete(0,'end')
    month2_12_entry.insert(0,'{:02d}'.format(day_phase12.month))
    year2_12_entry.delete(0,'end')
    year2_12_entry.insert(0,day_phase12.year)
    label2_d_12 = Label(tab2, text= '/')
    label2_m_12 = Label(tab2, text= '/')
    rad2_A_12 = Radiobutton(tab2, text='LD', variable=var2_12, value=1)
    lbl2_A_12 = Label(tab2, text= 'On:')
    spin2_A_12 = Spinbox(tab2, from_=00, to=24, width=3, format='%02.0f')
    spin2_B_12 = Spinbox(tab2, from_=00, to=59, width=3, format='%02.0f')
    spin2_A_12.delete(0,'end')
    spin2_A_12.insert(0,'07')
    spin2_B_12.delete(0,'end')
    spin2_B_12.insert(0,'00')
    label2_h1_12 = Label(tab2, text=':')
    label2_m1_12 = Label(tab2, text='')
    lbl2_B_12 = Label(tab2, text= 'Off:')
    spin2_C_12 = Spinbox(tab2, from_=00, to=24, width=3, format='%02.0f')
    spin2_D_12 = Spinbox(tab2, from_=00, to=59, width=3, format='%02.0f')
    spin2_C_12.delete(0,'end')
    spin2_C_12.insert(0,'19')
    spin2_D_12.delete(0,'end')
    spin2_D_12.insert(0,'00')
    label2_h2_12 = Label(tab2, text=':')
    label2_m2_12 = Label(tab2, text='')
    rad2_B_12 = Radiobutton(tab2, text='DD', variable=var2_12, value=2)
    rad2_C_12 = Radiobutton(tab2, text='LL', variable=var2_12, value=3)

    phaseLabel2_12.grid(column=0, row=rowPhase12+row_adj, padx=15, pady=5)
    fromLabel2_12.grid(column=1,row=rowPhase12+row_adj)
    spin2_E_12.grid(column=2,row=rowPhase12+row_adj)
    label2_h0_12.grid(column=3,row=rowPhase12+row_adj)
    spin2_F_12.grid(column=4,row=rowPhase12+row_adj)
    label2_m0_12.grid(column=5,row=rowPhase12+row_adj)
    space2_12.grid(column=7,row=rowPhase12+row_adj)
    date2_12_entry.grid(column=11, row=rowPhase12+row_adj)
    label2_d_12.grid(column=8,row=rowPhase12+row_adj)
    month2_12_entry.grid(column=9, row=rowPhase12+row_adj)
    label2_m_12.grid(column=10,row=rowPhase12+row_adj)
    year2_12_entry.grid(column=7, row=rowPhase12+row_adj) # ISO format
    space2_12_2.grid(column=12,row=rowPhase12+row_adj,padx=5)
    rad2_A_12.grid(column=13, row=rowPhase12+row_adj, pady=5)
    lbl2_A_12.grid(column=14, row=rowPhase12+row_adj, pady=5)
    spin2_A_12.grid(column=15,row=rowPhase12+row_adj, pady=5)
    label2_h1_12.grid(column=17,row=rowPhase12+row_adj, pady=5)
    spin2_B_12.grid(column=17,row=rowPhase12+row_adj, pady=5)
    label2_m1_12.grid(column=18,row=rowPhase12+row_adj, pady=5)
    lbl2_B_12.grid(column=19, row=rowPhase12+row_adj, pady=5)
    spin2_C_12.grid(column=20,row=rowPhase12+row_adj, pady=5)
    label2_h2_12.grid(column=21,row=rowPhase12+row_adj, pady=5)
    spin2_D_12.grid(column=22,row=rowPhase12+row_adj, pady=5)
    label2_m2_12.grid(column=23,row=rowPhase12+row_adj, pady=5)
    rad2_B_12.grid(column=24, row=rowPhase12+row_adj, padx=15, pady=5)
    rad2_C_12.grid(column=25, row=rowPhase12+row_adj, pady=5)

    
   
   

    # Box3 main

    tcyclelabel3 = Label(tab3, text='T-cycle length')
    tcyclelabel3.grid(column=26, row=1, padx=3, pady=5)

    for i in range(0,12): 
        tcyclelength = Spinbox(tab3, from_=12, to=48, width=3)
        tcyclelength.grid(column=26, row=2+i+row_adj, padx=3,pady=5)
        tcyclelength.delete(0,'end')
        tcyclelength.insert(0,24)
        tcyclespinbox_arr[2,i] = tcyclelength
        
    tcyclespinbox_arr[2,0].grid(column=26, row=1+row_adj, pady=5)
        
  
    tab3_title = Label(tab3, text= 'LED schedule', anchor='center')
    tab3_title.grid(column=12, row= 1, columnspan='27', sticky='we')
    # capSep3 = ttk.Separator(tab3, orient=HORIZONTAL)
    # capSep3.grid(column=0, row = row_adj+5, columnspan='27', sticky='we')
    box3sched_text=StringVar()
    box3sched_text.set('Schedule not set.')
    box3sched_stat=Label(tab3, textvariable=box3sched_text, anchor=W, justify=LEFT)
        # phase 1
    phaseLabel3_1 = Label(tab3, text='Phase 1')
    dateLabel = time.strftime('%H:%M   %Y/%m/%d') # reads time for Phase 1 start-time
    fromLabel3_1 = Label(tab3, text='From:')
    date_label3 = Label(tab3, text=dateLabel)
    rad3_A_1 = Radiobutton(tab3, text='LD', variable=var3_1, value=1)
    lbl3_A_1 = Label(tab3, text= 'On:')
    spin3_A_1 = Spinbox(tab3, from_=00, to=24, width=3, format='%02.0f')
    spin3_B_1 = Spinbox(tab3, from_=00, to=59, width=3, format='%02.0f')
    spin3_A_1.delete(0,'end')
    spin3_A_1.insert(0,'07')
    spin3_B_1.delete(0,'end')
    spin3_B_1.insert(0,'00')
    label3_h1_1 = Label(tab3, text=':')
    label3_m1_1 = Label(tab3, text='')
    lbl3_B_1 = Label(tab3, text= 'Off:')
    spin3_C_1 = Spinbox(tab3, from_=00, to=24, width=3, format='%02.0f')
    spin3_D_1 = Spinbox(tab3, from_=00, to=59, width=3, format='%02.0f')
    spin3_C_1.delete(0,'end')
    spin3_C_1.insert(0,'19')
    spin3_D_1.delete(0,'end')
    spin3_D_1.insert(0,'00')
    label3_h2_1 = Label(tab3, text=':')
    label3_m2_1 = Label(tab3, text='')
    rad3_B_1 = Radiobutton(tab3, text='DD', variable=var3_1, value=2)
    rad3_C_1 = Radiobutton(tab3, text='LL', variable=var3_1, value=3)
    phaseLabel3_1.grid(column=0, row=1+row_adj, padx=15, pady=5)
    fromLabel3_1.grid(column=1,row=1+row_adj)
    date_label3.grid(column=2, row=1+row_adj, columnspan='10', sticky='w')
    rad3_A_1.grid(column=13, row=1+row_adj, pady=5)
    lbl3_A_1.grid(column=14, row=1+row_adj, pady=5)
    spin3_A_1.grid(column=15,row=1+row_adj, pady=5)
    label3_h1_1.grid(column=16,row=1+row_adj, pady=5, sticky='w')
    spin3_B_1.grid(column=17,row=1+row_adj, pady=5)
    label3_m1_1.grid(column=18,row=1+row_adj, pady=5, sticky='w')
    lbl3_B_1.grid(column=19, row=1+row_adj, pady=5)
    spin3_C_1.grid(column=20,row=1+row_adj, pady=5)
    label3_h2_1.grid(column=21,row=1+row_adj, pady=5, sticky='w')
    spin3_D_1.grid(column=22,row=1+row_adj, pady=5)
    label3_m2_1.grid(column=23,row=1+row_adj, pady=5, sticky='w')
    rad3_B_1.grid(column=24, row=1+row_adj, padx=15, pady=5)
    rad3_C_1.grid(column=25, row=1+row_adj, pady=5)

        # phase 2
    phaseLabel3_2 = Label(tab3, text='Phase 2')
    fromLabel3_2 = Label(tab3, text='From:')
    space3_2 = Label(tab3, text=' ')
    space3_2_2 = Label(tab3, text=' ')
    spin3_E_2 = Spinbox(tab3, from_=00, to=24, width=3, format='%02.0f')
    spin3_F_2 = Spinbox(tab3, from_=00, to=59, width=3, format='%02.0f')
    spin3_E_2.delete(0,'end')
    spin3_E_2.insert(0,'07')
    spin3_F_2.delete(0,'end')
    spin3_F_2.insert(0,'00')
    label3_h0_2 = Label(tab3, text=':')
    label3_m0_2 = Label(tab3, text='')
    date3_2_entry = Spinbox(tab3, from_=00, to=31, width=3, format='%02.0f')
    month3_2_entry = Spinbox(tab3, from_=00, to=12, width=3, format='%02.0f')
    year3_2_entry = Spinbox(tab3, from_=2018, to=2030, width=5)
    date3_2_entry.delete(0,'end')
    today=datetime.date.today() # today
    day_phase2 = today + datetime.timedelta(days=7) # calculate dates for 7 days after recording initiation
    date3_2_entry.insert(0,'{:02d}'.format(day_phase2.day))
    month3_2_entry.delete(0,'end')
    month3_2_entry.insert(0,'{:02d}'.format(day_phase2.month))
    year3_2_entry.delete(0,'end')
    year3_2_entry.insert(0,day_phase2.year) # ISO format is YYYY/MM/DD    

    label3_d_0 = Label(tab3, text= 'Month')
    label3_m_0 = Label(tab3, text= 'Date')
    label3_m_0.grid(column=11,row=2+row_adj)
    label3_d_0.grid(column=9,row=2+row_adj)
    label3_d_1 = Label(tab3, text= '/')
    label3_m_1 = Label(tab3, text= '/')
    label3_d_1.grid(column=8,row=2+row_adj)
    label3_m_1.grid(column=10,row=2+row_adj)

    label3_d_2 = Label(tab3, text= '/')
    label3_m_2 = Label(tab3, text= '/')
    rad3_A_2 = Radiobutton(tab3, text='LD', variable=var3_2, value=1)
    lbl3_A_2 = Label(tab3, text= 'On:')
    spin3_A_2 = Spinbox(tab3, from_=00, to=24, width=3, format='%02.0f')
    spin3_B_2 = Spinbox(tab3, from_=00, to=59, width=3, format='%02.0f')
    spin3_A_2.delete(0,'end')
    spin3_A_2.insert(0,'07')
    spin3_B_2.delete(0,'end')
    spin3_B_2.insert(0,'00')
    label3_h1_2 = Label(tab3, text=':')
    label3_m1_2 = Label(tab3, text='')
    lbl3_B_2 = Label(tab3, text= 'Off:')
    spin3_C_2 = Spinbox(tab3, from_=00, to=24, width=3, format='%02.0f')
    spin3_D_2 = Spinbox(tab3, from_=00, to=59, width=3, format='%02.0f')
    spin3_C_2.delete(0,'end')
    spin3_C_2.insert(0,'19')
    spin3_D_2.delete(0,'end')
    spin3_D_2.insert(0,'00')
    label3_h2_2 = Label(tab3, text=':')
    label3_m2_2 = Label(tab3, text='')
    rad3_B_2 = Radiobutton(tab3, text='DD', variable=var3_2, value=2)
    rad3_C_2 = Radiobutton(tab3, text='LL', variable=var3_2, value=3)
    phaseLabel3_2.grid(column=0, row=3+row_adj, padx=15, pady=5)
    fromLabel3_2.grid(column=1,row=3+row_adj)
    spin3_E_2.grid(column=2,row=3+row_adj)
    label3_h0_2.grid(column=3,row=3+row_adj)
    spin3_F_2.grid(column=4,row=3+row_adj)
    label3_m0_2.grid(column=5,row=3+row_adj)
    space3_2.grid(column=6,row=3+row_adj)
    date3_2_entry.grid(column=11, row=3+row_adj)
    label3_d_2.grid(column=8,row=3+row_adj)
    month3_2_entry.grid(column=9, row=3+row_adj)
    label3_m_2.grid(column=10,row=3+row_adj)
    year3_2_entry.grid(column=7, row=3+row_adj) # ISO format
    space3_2_2.grid(column=12,row=3+row_adj,padx=5)
    rad3_A_2.grid(column=13, row=3+row_adj, pady=5)
    lbl3_A_2.grid(column=14, row=3+row_adj, pady=5)
    spin3_A_2.grid(column=15,row=3+row_adj, pady=5)
    label3_h1_2.grid(column=16,row=3+row_adj, pady=5)
    spin3_B_2.grid(column=17,row=3+row_adj, pady=5)
    label3_m1_2.grid(column=18,row=3+row_adj, pady=5)
    lbl3_B_2.grid(column=19, row=3+row_adj, pady=5)
    spin3_C_2.grid(column=20,row=3+row_adj, pady=5)
    label3_h2_2.grid(column=21,row=3+row_adj, pady=5)
    spin3_D_2.grid(column=22,row=3+row_adj, pady=5)
    label3_m2_2.grid(column=23,row=3+row_adj, pady=5)
    rad3_B_2.grid(column=24, row=3+row_adj, padx=15, pady=5)
    rad3_C_2.grid(column=25, row=3+row_adj, pady=5)

        # phase 3
    phaseLabel3_3 = Label(tab3, text='Phase 3')
    fromLabel3_3 = Label(tab3, text='From:')
    space3_3 = Label(tab3, text=' ')
    spin3_E_3 = Spinbox(tab3, from_=00, to=24, width=3, format='%02.0f')
    spin3_F_3 = Spinbox(tab3, from_=00, to=59, width=3, format='%02.0f')
    spin3_E_3.delete(0,'end')
    spin3_E_3.insert(0,'07')
    spin3_F_3.delete(0,'end')
    spin3_F_3.insert(0,'00')
    label3_h0_3 = Label(tab3, text=':')
    label3_m0_3 = Label(tab3, text='')
    date3_3_entry = Spinbox(tab3, from_=00, to=31, width=3, format='%02.0f')
    month3_3_entry = Spinbox(tab3, from_=00, to=12, width=3, format='%02.0f')
    year3_3_entry = Spinbox(tab3, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase3 = day_phase2 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date3_3_entry.delete(0,'end')
    date3_3_entry.insert(0,'{:02d}'.format(day_phase3.day))
    month3_3_entry.delete(0,'end')
    month3_3_entry.insert(0,'{:02d}'.format(day_phase3.month))
    year3_3_entry.delete(0,'end')
    year3_3_entry.insert(0,day_phase3.year)
    label3_d_3 = Label(tab3, text= '/')
    label3_m_3 = Label(tab3, text= '/')
    rad3_A_3 = Radiobutton(tab3, text='LD', variable=var3_3, value=1)
    lbl3_A_3 = Label(tab3, text= 'On:')
    spin3_A_3 = Spinbox(tab3, from_=00, to=24, width=3, format='%02.0f')
    spin3_B_3 = Spinbox(tab3, from_=00, to=59, width=3, format='%02.0f')
    spin3_A_3.delete(0,'end')
    spin3_A_3.insert(0,'07')
    spin3_B_3.delete(0,'end')
    spin3_B_3.insert(0,'00')
    label3_h1_3 = Label(tab3, text=':')
    label3_m1_3 = Label(tab3, text='')
    lbl3_B_3 = Label(tab3, text= 'Off:')
    spin3_C_3 = Spinbox(tab3, from_=00, to=24, width=3, format='%02.0f')
    spin3_D_3 = Spinbox(tab3, from_=00, to=59, width=3, format='%02.0f')
    spin3_C_3.delete(0,'end')
    spin3_C_3.insert(0,'19')
    spin3_D_3.delete(0,'end')
    spin3_D_3.insert(0,'00')
    label3_h2_3 = Label(tab3, text=':')
    label3_m2_3 = Label(tab3, text='')
    rad3_B_3 = Radiobutton(tab3, text='DD', variable=var3_3, value=2)
    rad3_C_3 = Radiobutton(tab3, text='LL', variable=var3_3, value=3)
    phaseLabel3_3.grid(column=0, row=4+row_adj, padx=15, pady=5)
    fromLabel3_3.grid(column=1,row=4+row_adj)
    spin3_E_3.grid(column=2,row=4+row_adj)
    label3_h0_3.grid(column=3,row=4+row_adj)
    spin3_F_3.grid(column=4,row=4+row_adj)
    label3_m0_3.grid(column=5,row=4+row_adj)
    space3_3.grid(column=6,row=4+row_adj)
    date3_3_entry.grid(column=11, row=4+row_adj)
    label3_d_3.grid(column=8,row=4+row_adj)
    month3_3_entry.grid(column=9, row=4+row_adj)
    label3_m_3.grid(column=10,row=4+row_adj)
    year3_3_entry.grid(column=7, row=4+row_adj) # ISO format
    rad3_A_3.grid(column=13, row=4+row_adj, pady=5)
    lbl3_A_3.grid(column=14, row=4+row_adj, pady=5)
    spin3_A_3.grid(column=15,row=4+row_adj, pady=5)
    label3_h1_3.grid(column=16,row=4+row_adj, pady=5)
    spin3_B_3.grid(column=17,row=4+row_adj, pady=5)
    label3_m1_3.grid(column=18,row=4+row_adj, pady=5)
    lbl3_B_3.grid(column=19, row=4+row_adj, pady=5)
    spin3_C_3.grid(column=20,row=4+row_adj, pady=5)
    label3_h2_3.grid(column=21,row=4+row_adj, pady=5)
    spin3_D_3.grid(column=22,row=4+row_adj, pady=5)
    label3_m2_3.grid(column=23,row=4+row_adj, pady=5)
    rad3_B_3.grid(column=24, row=4+row_adj, padx=15, pady=5)
    rad3_C_3.grid(column=25, row=4+row_adj, pady=5)

        # phase 4
    phaseLabel3_4 = Label(tab3, text='Phase 4')
    fromLabel3_4 = Label(tab3, text='From:')
    space3_4 = Label(tab3, text=' ')
    space3_4_2 = Label(tab3, text=' ')
    spin3_E_4 = Spinbox(tab3, from_=00, to=24, width=3, format='%02.0f')
    spin3_F_4 = Spinbox(tab3, from_=00, to=59, width=3, format='%02.0f')
    spin3_E_4.delete(0,'end')
    spin3_E_4.insert(0,'07')
    spin3_F_4.delete(0,'end')
    spin3_F_4.insert(0,'00')
    label3_h0_4 = Label(tab3, text=':')
    label3_m0_4 = Label(tab3, text='')
    date3_4_entry = Spinbox(tab3, from_=00, to=31, width=3, format='%02.0f')
    month3_4_entry = Spinbox(tab3, from_=00, to=12, width=3, format='%02.0f')
    year3_4_entry = Spinbox(tab3, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase4 = day_phase3 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date3_4_entry.delete(0,'end')
    date3_4_entry.insert(0,'{:02d}'.format(day_phase4.day))
    month3_4_entry.delete(0,'end')
    month3_4_entry.insert(0,'{:02d}'.format(day_phase4.month))
    year3_4_entry.delete(0,'end')
    year3_4_entry.insert(0,day_phase4.year)
    label3_d_4 = Label(tab3, text= '/')
    label3_m_4 = Label(tab3, text= '/')
    rad3_A_4 = Radiobutton(tab3, text='LD', variable=var3_4, value=1)
    lbl3_A_4 = Label(tab3, text= 'On:')
    spin3_A_4 = Spinbox(tab3, from_=00, to=24, width=3, format='%02.0f')
    spin3_B_4 = Spinbox(tab3, from_=00, to=59, width=3, format='%02.0f')
    spin3_A_4.delete(0,'end')
    spin3_A_4.insert(0,'07')
    spin3_B_4.delete(0,'end')
    spin3_B_4.insert(0,'00')
    label3_h1_4 = Label(tab3, text=':')
    label3_m1_4 = Label(tab3, text='')
    lbl3_B_4 = Label(tab3, text= 'Off:')
    spin3_C_4 = Spinbox(tab3, from_=00, to=24, width=3, format='%02.0f')
    spin3_D_4 = Spinbox(tab3, from_=00, to=59, width=3, format='%02.0f')
    spin3_C_4.delete(0,'end')
    spin3_C_4.insert(0,'19')
    spin3_D_4.delete(0,'end')
    spin3_D_4.insert(0,'00')
    label3_h2_4 = Label(tab3, text=':')
    label3_m2_4 = Label(tab3, text='')
    rad3_B_4 = Radiobutton(tab3, text='DD', variable=var3_4, value=2)
    rad3_C_4 = Radiobutton(tab3, text='LL', variable=var3_4, value=3)
    phaseLabel3_4.grid(column=0, row=5+row_adj, padx=15, pady=5)
    fromLabel3_4.grid(column=1,row=5+row_adj)
    spin3_E_4.grid(column=2,row=5+row_adj)
    label3_h0_4.grid(column=3,row=5+row_adj)
    spin3_F_4.grid(column=4,row=5+row_adj)
    label3_m0_4.grid(column=5,row=5+row_adj)
    space3_4.grid(column=6,row=5+row_adj)
    date3_4_entry.grid(column=11, row=5+row_adj)
    label3_d_4.grid(column=8,row=5+row_adj)
    month3_4_entry.grid(column=9, row=5+row_adj)
    label3_m_4.grid(column=10,row=5+row_adj)
    year3_4_entry.grid(column=7, row=5+row_adj) # ISO format
    space3_4_2.grid(column=12,row=5+row_adj,padx=5)
    rad3_A_4.grid(column=13, row=5+row_adj, pady=5)
    lbl3_A_4.grid(column=14, row=5+row_adj, pady=5)
    spin3_A_4.grid(column=15,row=5+row_adj, pady=5)
    label3_h1_4.grid(column=16,row=5+row_adj, pady=5)
    spin3_B_4.grid(column=17,row=5+row_adj, pady=5)
    label3_m1_4.grid(column=18,row=5+row_adj, pady=5)
    lbl3_B_4.grid(column=19, row=5+row_adj, pady=5)
    spin3_C_4.grid(column=20,row=5+row_adj, pady=5)
    label3_h2_4.grid(column=21,row=5+row_adj, pady=5)
    spin3_D_4.grid(column=22,row=5+row_adj, pady=5)
    label3_m2_4.grid(column=23,row=5+row_adj, pady=5)
    rad3_B_4.grid(column=24, row=5+row_adj, padx=15, pady=5)
    rad3_C_4.grid(column=25, row=5+row_adj, pady=5)

    # phase 5
    phaseLabel3_5 = Label(tab3, text='Phase 5')
    fromLabel3_5 = Label(tab3, text='From:')
    space3_5 = Label(tab3, text=' ')
    space3_5_2 = Label(tab3, text=' ')
    spin3_E_5 = Spinbox(tab3, from_=00, to=24, width=3, format='%02.0f')
    spin3_F_5 = Spinbox(tab3, from_=00, to=59, width=3, format='%02.0f')
    spin3_E_5.delete(0,'end')
    spin3_E_5.insert(0,'07')
    spin3_F_5.delete(0,'end')
    spin3_F_5.insert(0,'00')
    label3_h0_5 = Label(tab3, text=':')
    label3_m0_5 = Label(tab3, text='')
    date3_5_entry = Spinbox(tab3, from_=00, to=31, width=3, format='%02.0f')
    month3_5_entry = Spinbox(tab3, from_=00, to=12, width=3, format='%02.0f')
    year3_5_entry = Spinbox(tab3, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase5 = day_phase4 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date3_5_entry.delete(0,'end')
    date3_5_entry.insert(0,'{:02d}'.format(day_phase5.day))
    month3_5_entry.delete(0,'end')
    month3_5_entry.insert(0,'{:02d}'.format(day_phase5.month))
    year3_5_entry.delete(0,'end')
    year3_5_entry.insert(0,day_phase5.year)
    label3_d_5 = Label(tab3, text= '/')
    label3_m_5 = Label(tab3, text= '/')
    rad3_A_5 = Radiobutton(tab3, text='LD', variable=var3_5, value=1)
    lbl3_A_5 = Label(tab3, text= 'On:')
    spin3_A_5 = Spinbox(tab3, from_=00, to=24, width=3, format='%02.0f')
    spin3_B_5 = Spinbox(tab3, from_=00, to=59, width=3, format='%02.0f')
    spin3_A_5.delete(0,'end')
    spin3_A_5.insert(0,'07')
    spin3_B_5.delete(0,'end')
    spin3_B_5.insert(0,'00')
    label3_h1_5 = Label(tab3, text=':')
    label3_m1_5 = Label(tab3, text='')
    lbl3_B_5 = Label(tab3, text= 'Off:')
    spin3_C_5 = Spinbox(tab3, from_=00, to=24, width=3, format='%02.0f')
    spin3_D_5 = Spinbox(tab3, from_=00, to=59, width=3, format='%02.0f')
    spin3_C_5.delete(0,'end')
    spin3_C_5.insert(0,'19')
    spin3_D_5.delete(0,'end')
    spin3_D_5.insert(0,'00')
    label3_h2_5 = Label(tab3, text=':')
    label3_m2_5 = Label(tab3, text='')
    rad3_B_5 = Radiobutton(tab3, text='DD', variable=var3_5, value=2)
    rad3_C_5 = Radiobutton(tab3, text='LL', variable=var3_5, value=3)
    phaseLabel3_5.grid(column=0, row=6+row_adj, padx=15, pady=5)
    fromLabel3_5.grid(column=1,row=6+row_adj)
    spin3_E_5.grid(column=2,row=6+row_adj)
    label3_h0_5.grid(column=3,row=6+row_adj)
    spin3_F_5.grid(column=4,row=6+row_adj)
    label3_m0_5.grid(column=5,row=6+row_adj)
    space3_5.grid(column=6,row=6+row_adj)
    date3_5_entry.grid(column=11, row=6+row_adj)
    label3_d_5.grid(column=8,row=6+row_adj)
    month3_5_entry.grid(column=9, row=6+row_adj)
    label3_m_5.grid(column=10,row=6+row_adj)
    year3_5_entry.grid(column=7, row=6+row_adj) # ISO format
    space3_5_2.grid(column=12,row=6+row_adj,padx=5)
    rad3_A_5.grid(column=13, row=6+row_adj, pady=5)
    lbl3_A_5.grid(column=14, row=6+row_adj, pady=5)
    spin3_A_5.grid(column=15,row=6+row_adj, pady=5)
    label3_h1_5.grid(column=16,row=6+row_adj, pady=5)
    spin3_B_5.grid(column=17,row=6+row_adj, pady=5)
    label3_m1_5.grid(column=18,row=6+row_adj, pady=5)
    lbl3_B_5.grid(column=19, row=6+row_adj, pady=5)
    spin3_C_5.grid(column=20,row=6+row_adj, pady=5)
    label3_h2_5.grid(column=21,row=6+row_adj, pady=5)
    spin3_D_5.grid(column=22,row=6+row_adj, pady=5)
    label3_m2_5.grid(column=23,row=6+row_adj, pady=5)
    rad3_B_5.grid(column=24, row=6+row_adj, padx=15, pady=5)
    rad3_C_5.grid(column=25, row=6+row_adj, pady=5)
    
        # phase 6 
    phaseLabel3_6 = Label(tab3, text='Phase 6')
    fromLabel3_6 = Label(tab3, text='From:')
    space3_6 = Label(tab3, text=' ')
    space3_6_2 = Label(tab3, text=' ')
    spin3_E_6 = Spinbox(tab3, from_=00, to=24, width=3, format='%02.0f')
    spin3_F_6 = Spinbox(tab3, from_=00, to=59, width=3, format='%02.0f')
    spin3_E_6.delete(0,'end')
    spin3_E_6.insert(0,'07')
    spin3_F_6.delete(0,'end')
    spin3_F_6.insert(0,'00')
    label3_h0_6 = Label(tab3, text=':')
    label3_m0_6 = Label(tab3, text='')
    date3_6_entry = Spinbox(tab3, from_=00, to=31, width=3, format='%02.0f')
    month3_6_entry = Spinbox(tab3, from_=00, to=12, width=3, format='%02.0f')
    year3_6_entry = Spinbox(tab3, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase6 = day_phase5 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date3_6_entry.delete(0,'end')
    date3_6_entry.insert(0,'{:02d}'.format(day_phase6.day))
    month3_6_entry.delete(0,'end')
    month3_6_entry.insert(0,'{:02d}'.format(day_phase6.month))
    year3_6_entry.delete(0,'end')
    year3_6_entry.insert(0,day_phase6.year)
    label3_d_6 = Label(tab3, text= '/')
    label3_m_6 = Label(tab3, text= '/')
    rad3_A_6 = Radiobutton(tab3, text='LD', variable=var3_6, value=1)
    lbl3_A_6 = Label(tab3, text= 'On:')
    spin3_A_6 = Spinbox(tab3, from_=00, to=24, width=3, format='%02.0f')
    spin3_B_6 = Spinbox(tab3, from_=00, to=59, width=3, format='%02.0f')
    spin3_A_6.delete(0,'end')
    spin3_A_6.insert(0,'07')
    spin3_B_6.delete(0,'end')
    spin3_B_6.insert(0,'00')
    label3_h1_6 = Label(tab3, text=':')
    label3_m1_6 = Label(tab3, text='')
    lbl3_B_6 = Label(tab3, text= 'Off:')
    spin3_C_6 = Spinbox(tab3, from_=00, to=24, width=3, format='%02.0f')
    spin3_D_6 = Spinbox(tab3, from_=00, to=59, width=3, format='%02.0f')
    spin3_C_6.delete(0,'end')
    spin3_C_6.insert(0,'19')
    spin3_D_6.delete(0,'end')
    spin3_D_6.insert(0,'00')
    label3_h2_6 = Label(tab3, text=':')
    label3_m2_6 = Label(tab3, text='')
    rad3_B_6 = Radiobutton(tab3, text='DD', variable=var3_6, value=2)
    rad3_C_6 = Radiobutton(tab3, text='LL', variable=var3_6, value=3)

    phaseLabel3_6.grid(column=0, row=rowPhase6+row_adj, padx=15, pady=5)
    fromLabel3_6.grid(column=1,row=rowPhase6+row_adj)
    spin3_E_6.grid(column=2,row=rowPhase6+row_adj)
    label3_h0_6.grid(column=3,row=rowPhase6+row_adj)
    spin3_F_6.grid(column=4,row=rowPhase6+row_adj)
    label3_m0_6.grid(column=5,row=rowPhase6+row_adj)
    space3_6.grid(column=6,row=rowPhase6+row_adj)
    date3_6_entry.grid(column=11, row=rowPhase6+row_adj)
    label3_d_6.grid(column=8,row=rowPhase6+row_adj)
    month3_6_entry.grid(column=9, row=rowPhase6+row_adj)
    label3_m_6.grid(column=10,row=rowPhase6+row_adj)
    year3_6_entry.grid(column=7, row=rowPhase6+row_adj) # ISO format
    space3_6_2.grid(column=12,row=rowPhase6+row_adj,padx=5)
    rad3_A_6.grid(column=13, row=rowPhase6+row_adj, pady=5)
    lbl3_A_6.grid(column=14, row=rowPhase6+row_adj, pady=5)
    spin3_A_6.grid(column=15,row=rowPhase6+row_adj, pady=5)
    label3_h1_6.grid(column=16,row=rowPhase6+row_adj, pady=5)
    spin3_B_6.grid(column=17,row=rowPhase6+row_adj, pady=5)
    label3_m1_6.grid(column=18,row=rowPhase6+row_adj, pady=5)
    lbl3_B_6.grid(column=19, row=rowPhase6+row_adj, pady=5)
    spin3_C_6.grid(column=20,row=rowPhase6+row_adj, pady=5)
    label3_h2_6.grid(column=21,row=rowPhase6+row_adj, pady=5)
    spin3_D_6.grid(column=22,row=rowPhase6+row_adj, pady=5)
    label3_m2_6.grid(column=23,row=rowPhase6+row_adj, pady=5)
    rad3_B_6.grid(column=24, row=rowPhase6+row_adj, padx=15, pady=5)
    rad3_C_6.grid(column=25, row=rowPhase6+row_adj, pady=5)
    
    # phase 7
    phaseLabel3_7 = Label(tab3, text='Phase 7')
    fromLabel3_7 = Label(tab3, text='From:')
    space3_7 = Label(tab3, text=' ')
    space3_7_2 = Label(tab3, text=' ')
    spin3_E_7 = Spinbox(tab3, from_=00, to=24, width=3, format='%02.0f')
    spin3_F_7 = Spinbox(tab3, from_=00, to=59, width=3, format='%02.0f')
    spin3_E_7.delete(0,'end')
    spin3_E_7.insert(0,'07')
    spin3_F_7.delete(0,'end')
    spin3_F_7.insert(0,'00')
    label3_h0_7 = Label(tab3, text=':')
    label3_m0_7 = Label(tab3, text='')
    date3_7_entry = Spinbox(tab3, from_=00, to=31, width=3, format='%02.0f')
    month3_7_entry = Spinbox(tab3, from_=00, to=12, width=3, format='%02.0f')
    year3_7_entry = Spinbox(tab3, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase7 = day_phase6 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date3_7_entry.delete(0,'end')
    date3_7_entry.insert(0,'{:02d}'.format(day_phase7.day))
    month3_7_entry.delete(0,'end')
    month3_7_entry.insert(0,'{:02d}'.format(day_phase7.month))
    year3_7_entry.delete(0,'end')
    year3_7_entry.insert(0,day_phase7.year)
    label3_d_7 = Label(tab3, text= '/')
    label3_m_7 = Label(tab3, text= '/')
    rad3_A_7 = Radiobutton(tab3, text='LD', variable=var3_7, value=1)
    lbl3_A_7 = Label(tab3, text= 'On:')
    spin3_A_7 = Spinbox(tab3, from_=00, to=24, width=3, format='%02.0f')
    spin3_B_7 = Spinbox(tab3, from_=00, to=59, width=3, format='%02.0f')
    spin3_A_7.delete(0,'end')
    spin3_A_7.insert(0,'07')
    spin3_B_7.delete(0,'end')
    spin3_B_7.insert(0,'00')
    label3_h1_7 = Label(tab3, text=':')
    label3_m1_7 = Label(tab3, text='')
    lbl3_B_7 = Label(tab3, text= 'Off:')
    spin3_C_7 = Spinbox(tab3, from_=00, to=24, width=3, format='%02.0f')
    spin3_D_7 = Spinbox(tab3, from_=00, to=59, width=3, format='%02.0f')
    spin3_C_7.delete(0,'end')
    spin3_C_7.insert(0,'19')
    spin3_D_7.delete(0,'end')
    spin3_D_7.insert(0,'00')
    label3_h2_7 = Label(tab3, text=':')
    label3_m2_7 = Label(tab3, text='')
    rad3_B_7 = Radiobutton(tab3, text='DD', variable=var3_7, value=2)
    rad3_C_7 = Radiobutton(tab3, text='LL', variable=var3_7, value=3)

    phaseLabel3_7.grid(column=0, row=rowPhase7+row_adj, padx=15, pady=5)
    fromLabel3_7.grid(column=1,row=rowPhase7+row_adj)
    spin3_E_7.grid(column=2,row=rowPhase7+row_adj)
    label3_h0_7.grid(column=3,row=rowPhase7+row_adj)
    spin3_F_7.grid(column=4,row=rowPhase7+row_adj)
    label3_m0_7.grid(column=5,row=rowPhase7+row_adj)
    space3_7.grid(column=6,row=rowPhase7+row_adj)
    date3_7_entry.grid(column=11, row=rowPhase7+row_adj)
    label3_d_7.grid(column=8,row=rowPhase7+row_adj)
    month3_7_entry.grid(column=9, row=rowPhase7+row_adj)
    label3_m_7.grid(column=10,row=rowPhase7+row_adj)
    year3_7_entry.grid(column=7, row=rowPhase7+row_adj) # ISO format
    space3_7_2.grid(column=12,row=rowPhase7+row_adj,padx=5)
    rad3_A_7.grid(column=13, row=rowPhase7+row_adj, pady=5)
    lbl3_A_7.grid(column=14, row=rowPhase7+row_adj, pady=5)
    spin3_A_7.grid(column=15,row=rowPhase7+row_adj, pady=5)
    label3_h1_7.grid(column=16,row=rowPhase7+row_adj, pady=5)
    spin3_B_7.grid(column=17,row=rowPhase7+row_adj, pady=5)
    label3_m1_7.grid(column=18,row=rowPhase7+row_adj, pady=5)
    lbl3_B_7.grid(column=19, row=rowPhase7+row_adj, pady=5)
    spin3_C_7.grid(column=20,row=rowPhase7+row_adj, pady=5)
    label3_h2_7.grid(column=21,row=rowPhase7+row_adj, pady=5)
    spin3_D_7.grid(column=22,row=rowPhase7+row_adj, pady=5)
    label3_m2_7.grid(column=23,row=rowPhase7+row_adj, pady=5)
    rad3_B_7.grid(column=24, row=rowPhase7+row_adj, padx=15, pady=5)
    rad3_C_7.grid(column=25, row=rowPhase7+row_adj, pady=5)

     # phase 8 
    phaseLabel3_8 = Label(tab3, text='Phase 8')
    fromLabel3_8 = Label(tab3, text='From:')
    space3_8 = Label(tab3, text=' ')
    space3_8_2 = Label(tab3, text=' ')
    spin3_E_8 = Spinbox(tab3, from_=00, to=24, width=3, format='%02.0f')
    spin3_F_8 = Spinbox(tab3, from_=00, to=59, width=3, format='%02.0f')
    spin3_E_8.delete(0,'end')
    spin3_E_8.insert(0,'07')
    spin3_F_8.delete(0,'end')
    spin3_F_8.insert(0,'00')
    label3_h0_8 = Label(tab3, text=':')
    label3_m0_8 = Label(tab3, text='')
    date3_8_entry = Spinbox(tab3, from_=00, to=31, width=3, format='%02.0f')
    month3_8_entry = Spinbox(tab3, from_=00, to=12, width=3, format='%02.0f')
    year3_8_entry = Spinbox(tab3, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase8 = day_phase7 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date3_8_entry.delete(0,'end')
    date3_8_entry.insert(0,'{:02d}'.format(day_phase8.day))
    month3_8_entry.delete(0,'end')
    month3_8_entry.insert(0,'{:02d}'.format(day_phase8.month))
    year3_8_entry.delete(0,'end')
    year3_8_entry.insert(0,day_phase8.year)
    label3_d_8 = Label(tab1, text= '/')
    label3_m_8 = Label(tab1, text= '/')
    rad3_A_8 = Radiobutton(tab3, text='LD', variable=var3_8, value=1)
    lbl3_A_8 = Label(tab3, text= 'On:')
    spin3_A_8 = Spinbox(tab3, from_=00, to=24, width=3, format='%02.0f')
    spin3_B_8 = Spinbox(tab3, from_=00, to=59, width=3, format='%02.0f')
    spin3_A_8.delete(0,'end')
    spin3_A_8.insert(0,'07')
    spin3_B_8.delete(0,'end')
    spin3_B_8.insert(0,'00')
    label3_h1_8 = Label(tab3, text=':')
    label3_m1_8 = Label(tab3, text='')
    lbl3_B_8 = Label(tab3, text= 'Off:')
    spin3_C_8 = Spinbox(tab3, from_=00, to=24, width=3, format='%02.0f')
    spin3_D_8 = Spinbox(tab3, from_=00, to=59, width=3, format='%02.0f')
    spin3_C_8.delete(0,'end')
    spin3_C_8.insert(0,'19')
    spin3_D_8.delete(0,'end')
    spin3_D_8.insert(0,'00')
    label3_h2_8 = Label(tab3, text=':')
    label3_m2_8 = Label(tab3, text='')
    rad3_B_8 = Radiobutton(tab3, text='DD', variable=var3_8, value=2)
    rad3_C_8 = Radiobutton(tab3, text='LL', variable=var3_8, value=3)

    phaseLabel3_8.grid(column=0, row=rowPhase8+row_adj, padx=15, pady=5)
    fromLabel3_8.grid(column=1,row=rowPhase8+row_adj)
    spin3_E_8.grid(column=2,row=rowPhase8+row_adj)
    label3_h0_8.grid(column=3,row=rowPhase8+row_adj)
    spin3_F_8.grid(column=4,row=rowPhase8+row_adj)
    label3_m0_8.grid(column=5,row=rowPhase8+row_adj)
    space3_8.grid(column=7,row=rowPhase8+row_adj)
    date3_8_entry.grid(column=11, row=rowPhase8+row_adj)
    label3_d_8.grid(column=8,row=rowPhase8+row_adj)
    month3_8_entry.grid(column=9, row=rowPhase8+row_adj)
    label3_m_8.grid(column=10,row=rowPhase8+row_adj)
    year3_8_entry.grid(column=7, row=rowPhase8+row_adj) # ISO format
    space3_8_2.grid(column=12,row=rowPhase8+row_adj,padx=5)
    rad3_A_8.grid(column=13, row=rowPhase8+row_adj, pady=5)
    lbl3_A_8.grid(column=14, row=rowPhase8+row_adj, pady=5)
    spin3_A_8.grid(column=15,row=rowPhase8+row_adj, pady=5)
    label3_h1_8.grid(column=16,row=rowPhase8+row_adj, pady=5)
    spin3_B_8.grid(column=17,row=rowPhase8+row_adj, pady=5)
    label3_m1_8.grid(column=18,row=rowPhase8+row_adj, pady=5)
    lbl3_B_8.grid(column=19, row=rowPhase8+row_adj, pady=5)
    spin3_C_8.grid(column=20,row=rowPhase8+row_adj, pady=5)
    label3_h2_8.grid(column=21,row=rowPhase8+row_adj, pady=5)
    spin3_D_8.grid(column=22,row=rowPhase8+row_adj, pady=5)
    label3_m2_8.grid(column=23,row=rowPhase8+row_adj, pady=5)
    rad3_B_8.grid(column=24, row=rowPhase8+row_adj, padx=15, pady=5)
    rad3_C_8.grid(column=25, row=rowPhase8+row_adj, pady=5)

    # phase 9 
    phaseLabel3_9 = Label(tab3, text='Phase 9')
    fromLabel3_9 = Label(tab3, text='From:')
    space3_9 = Label(tab3, text=' ')
    space3_9_2 = Label(tab3, text=' ')
    spin3_E_9 = Spinbox(tab3, from_=00, to=24, width=3, format='%02.0f')
    spin3_F_9 = Spinbox(tab3, from_=00, to=59, width=3, format='%02.0f')
    spin3_E_9.delete(0,'end')
    spin3_E_9.insert(0,'07')
    spin3_F_9.delete(0,'end')
    spin3_F_9.insert(0,'00')
    label3_h0_9 = Label(tab3, text=':')
    label3_m0_9 = Label(tab3, text='')
    date3_9_entry = Spinbox(tab3, from_=00, to=31, width=3, format='%02.0f')
    month3_9_entry = Spinbox(tab3, from_=00, to=12, width=3, format='%02.0f')
    year3_9_entry = Spinbox(tab3, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase9 = day_phase8 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date3_9_entry.delete(0,'end')
    date3_9_entry.insert(0,'{:02d}'.format(day_phase9.day))
    month3_9_entry.delete(0,'end')
    month3_9_entry.insert(0,'{:02d}'.format(day_phase9.month))
    year3_9_entry.delete(0,'end')
    year3_9_entry.insert(0,day_phase9.year)
    label3_d_9 = Label(tab3, text= '/')
    label3_m_9 = Label(tab3, text= '/')
    rad3_A_9 = Radiobutton(tab3, text='LD', variable=var3_9, value=1)
    lbl3_A_9 = Label(tab3, text= 'On:')
    spin3_A_9 = Spinbox(tab3, from_=00, to=24, width=3, format='%02.0f')
    spin3_B_9 = Spinbox(tab3, from_=00, to=59, width=3, format='%02.0f')
    spin3_A_9.delete(0,'end')
    spin3_A_9.insert(0,'07')
    spin3_B_9.delete(0,'end')
    spin3_B_9.insert(0,'00')
    label3_h1_9 = Label(tab3, text=':')
    label3_m1_9 = Label(tab3, text='')
    lbl3_B_9 = Label(tab3, text= 'Off:')
    spin3_C_9 = Spinbox(tab3, from_=00, to=24, width=3, format='%02.0f')
    spin3_D_9 = Spinbox(tab3, from_=00, to=59, width=3, format='%02.0f')
    spin3_C_9.delete(0,'end')
    spin3_C_9.insert(0,'19')
    spin3_D_9.delete(0,'end')
    spin3_D_9.insert(0,'00')
    label3_h2_9 = Label(tab3, text=':')
    label3_m2_9 = Label(tab3, text='')
    rad3_B_9 = Radiobutton(tab3, text='DD', variable=var3_9, value=2)
    rad3_C_9 = Radiobutton(tab3, text='LL', variable=var3_9, value=3)

    phaseLabel3_9.grid(column=0, row=rowPhase9+row_adj, padx=15, pady=5)
    fromLabel3_9.grid(column=1,row=rowPhase9+row_adj)
    spin3_E_9.grid(column=2,row=rowPhase9+row_adj)
    label3_h0_9.grid(column=3,row=rowPhase9+row_adj)
    spin3_F_9.grid(column=4,row=rowPhase9+row_adj)
    label3_m0_9.grid(column=5,row=rowPhase9+row_adj)
    space3_9.grid(column=7,row=rowPhase9+row_adj)
    date3_9_entry.grid(column=11, row=rowPhase9+row_adj)
    label3_d_9.grid(column=8,row=rowPhase9+row_adj)
    month3_9_entry.grid(column=9, row=rowPhase9+row_adj)
    label3_m_9.grid(column=10,row=rowPhase9+row_adj)
    year3_9_entry.grid(column=7, row=rowPhase9+row_adj) # ISO format
    space3_9_2.grid(column=12,row=rowPhase9+row_adj,padx=5)
    rad3_A_9.grid(column=13, row=rowPhase9+row_adj, pady=5)
    lbl3_A_9.grid(column=14, row=rowPhase9+row_adj, pady=5)
    spin3_A_9.grid(column=15,row=rowPhase9+row_adj, pady=5)
    label3_h1_9.grid(column=16,row=rowPhase9+row_adj, pady=5)
    spin3_B_9.grid(column=17,row=rowPhase9+row_adj, pady=5)
    label3_m1_9.grid(column=18,row=rowPhase9+row_adj, pady=5)
    lbl3_B_9.grid(column=19, row=rowPhase9+row_adj, pady=5)
    spin3_C_9.grid(column=20,row=rowPhase9+row_adj, pady=5)
    label3_h2_9.grid(column=21,row=rowPhase9+row_adj, pady=5)
    spin3_D_9.grid(column=22,row=rowPhase9+row_adj, pady=5)
    label3_m2_9.grid(column=23,row=rowPhase9+row_adj, pady=5)
    rad3_B_9.grid(column=24, row=rowPhase9+row_adj, padx=15, pady=5)
    rad3_C_9.grid(column=25, row=rowPhase9+row_adj, pady=5)

    # phase 10
    phaseLabel3_10 = Label(tab3, text='Phase 10')
    fromLabel3_10 = Label(tab3, text='From:')
    space3_10 = Label(tab3, text=' ')
    space3_10_2 = Label(tab3, text=' ')
    spin3_E_10 = Spinbox(tab3, from_=00, to=24, width=3, format='%02.0f')
    spin3_F_10 = Spinbox(tab3, from_=00, to=59, width=3, format='%02.0f')
    spin3_E_10.delete(0,'end')
    spin3_E_10.insert(0,'07')
    spin3_F_10.delete(0,'end')
    spin3_F_10.insert(0,'00')
    label3_h0_10 = Label(tab3, text=':')
    label3_m0_10 = Label(tab3, text='')
    date3_10_entry = Spinbox(tab3, from_=00, to=31, width=3, format='%02.0f')
    month3_10_entry = Spinbox(tab3, from_=00, to=12, width=3, format='%02.0f')
    year3_10_entry = Spinbox(tab3, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase10 = day_phase9 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date3_10_entry.delete(0,'end')
    date3_10_entry.insert(0,'{:02d}'.format(day_phase10.day))
    month3_10_entry.delete(0,'end')
    month3_10_entry.insert(0,'{:02d}'.format(day_phase10.month))
    year3_10_entry.delete(0,'end')
    year3_10_entry.insert(0,day_phase10.year)
    label3_d_10 = Label(tab3, text= '/')
    label3_m_10 = Label(tab3, text= '/')
    rad3_A_10 = Radiobutton(tab3, text='LD', variable=var3_10, value=1)
    lbl3_A_10 = Label(tab3, text= 'On:')
    spin3_A_10 = Spinbox(tab3, from_=00, to=24, width=3, format='%02.0f')
    spin3_B_10 = Spinbox(tab3, from_=00, to=59, width=3, format='%02.0f')
    spin3_A_10.delete(0,'end')
    spin3_A_10.insert(0,'07')
    spin3_B_10.delete(0,'end')
    spin3_B_10.insert(0,'00')
    label3_h1_10 = Label(tab3, text=':')
    label3_m1_10 = Label(tab3, text='')
    lbl3_B_10 = Label(tab3, text= 'Off:')
    spin3_C_10 = Spinbox(tab3, from_=00, to=24, width=3, format='%02.0f')
    spin3_D_10 = Spinbox(tab3, from_=00, to=59, width=3, format='%02.0f')
    spin3_C_10.delete(0,'end')
    spin3_C_10.insert(0,'19')
    spin3_D_10.delete(0,'end')
    spin3_D_10.insert(0,'00')
    label3_h2_10 = Label(tab3, text=':')
    label3_m2_10 = Label(tab3, text='')
    rad3_B_10 = Radiobutton(tab3, text='DD', variable=var3_10, value=2)
    rad3_C_10 = Radiobutton(tab3, text='LL', variable=var3_10, value=3)

    phaseLabel3_10.grid(column=0, row=rowPhase10+row_adj, padx=15, pady=5)
    fromLabel3_10.grid(column=1,row=rowPhase10+row_adj)
    spin3_E_10.grid(column=2,row=rowPhase10+row_adj)
    label3_h0_10.grid(column=3,row=rowPhase10+row_adj)
    spin3_F_10.grid(column=4,row=rowPhase10+row_adj)
    label3_m0_10.grid(column=5,row=rowPhase10+row_adj)
    space3_10.grid(column=7,row=rowPhase10+row_adj)
    date3_10_entry.grid(column=11, row=rowPhase10+row_adj)
    label3_d_10.grid(column=8,row=rowPhase10+row_adj)
    month3_10_entry.grid(column=9, row=rowPhase10+row_adj)
    label3_m_10.grid(column=10,row=rowPhase10+row_adj)
    year3_10_entry.grid(column=7, row=rowPhase10+row_adj) # ISO format
    space3_10_2.grid(column=12,row=rowPhase10+row_adj,padx=5)
    rad3_A_10.grid(column=13, row=rowPhase10+row_adj, pady=5)
    lbl3_A_10.grid(column=14, row=rowPhase10+row_adj, pady=5)
    spin3_A_10.grid(column=15,row=rowPhase10+row_adj, pady=5)
    label3_h1_10.grid(column=16,row=rowPhase10+row_adj, pady=5)
    spin3_B_10.grid(column=17,row=rowPhase10+row_adj, pady=5)
    label3_m1_10.grid(column=18,row=rowPhase10+row_adj, pady=5)
    lbl3_B_10.grid(column=19, row=rowPhase10+row_adj, pady=5)
    spin3_C_10.grid(column=20,row=rowPhase10+row_adj, pady=5)
    label3_h2_10.grid(column=21,row=rowPhase10+row_adj, pady=5)
    spin3_D_10.grid(column=22,row=rowPhase10+row_adj, pady=5)
    label3_m2_10.grid(column=23,row=rowPhase10+row_adj, pady=5)
    rad3_B_10.grid(column=24, row=rowPhase10+row_adj, padx=15, pady=5)
    rad3_C_10.grid(column=25, row=rowPhase10+row_adj, pady=5)

    # phase 11
    phaseLabel3_11 = Label(tab3, text='Phase 11')
    fromLabel3_11 = Label(tab3, text='From:')
    space3_11 = Label(tab3, text=' ')
    space3_11_2 = Label(tab3, text=' ')
    spin3_E_11 = Spinbox(tab3, from_=00, to=24, width=3, format='%02.0f')
    spin3_F_11 = Spinbox(tab3, from_=00, to=59, width=3, format='%02.0f')
    spin3_E_11.delete(0,'end')
    spin3_E_11.insert(0,'07')
    spin3_F_11.delete(0,'end')
    spin3_F_11.insert(0,'00')
    label3_h0_11 = Label(tab3, text=':')
    label3_m0_11 = Label(tab3, text='')
    date3_11_entry = Spinbox(tab3, from_=00, to=31, width=3, format='%02.0f')
    month3_11_entry = Spinbox(tab3, from_=00, to=12, width=3, format='%02.0f')
    year3_11_entry = Spinbox(tab3, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase11 = day_phase10 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date3_11_entry.delete(0,'end')
    date3_11_entry.insert(0,'{:02d}'.format(day_phase11.day))
    month3_11_entry.delete(0,'end')
    month3_11_entry.insert(0,'{:02d}'.format(day_phase11.month))
    year3_11_entry.delete(0,'end')
    year3_11_entry.insert(0,day_phase11.year)
    label3_d_11 = Label(tab3, text= '/')
    label3_m_11 = Label(tab3, text= '/')
    rad3_A_11 = Radiobutton(tab3, text='LD', variable=var3_11, value=1)
    lbl3_A_11 = Label(tab3, text= 'On:')
    spin3_A_11 = Spinbox(tab3, from_=00, to=24, width=3, format='%02.0f')
    spin3_B_11 = Spinbox(tab3, from_=00, to=59, width=3, format='%02.0f')
    spin3_A_11.delete(0,'end')
    spin3_A_11.insert(0,'07')
    spin3_B_11.delete(0,'end')
    spin3_B_11.insert(0,'00')
    label3_h1_11 = Label(tab3, text=':')
    label3_m1_11 = Label(tab3, text='')
    lbl3_B_11 = Label(tab3, text= 'Off:')
    spin3_C_11 = Spinbox(tab3, from_=00, to=24, width=3, format='%02.0f')
    spin3_D_11 = Spinbox(tab3, from_=00, to=59, width=3, format='%02.0f')
    spin3_C_11.delete(0,'end')
    spin3_C_11.insert(0,'19')
    spin3_D_11.delete(0,'end')
    spin3_D_11.insert(0,'00')
    label3_h2_11 = Label(tab3, text=':')
    label3_m2_11 = Label(tab3, text='')
    rad3_B_11 = Radiobutton(tab3, text='DD', variable=var3_11, value=2)
    rad3_C_11 = Radiobutton(tab3, text='LL', variable=var3_11, value=3)

    phaseLabel3_11.grid(column=0, row=rowPhase11+row_adj, padx=15, pady=5)
    fromLabel3_11.grid(column=1,row=rowPhase11+row_adj)
    spin3_E_11.grid(column=2,row=rowPhase11+row_adj)
    label3_h0_11.grid(column=3,row=rowPhase11+row_adj)
    spin3_F_11.grid(column=4,row=rowPhase11+row_adj)
    label3_m0_11.grid(column=5,row=rowPhase11+row_adj)
    space3_11.grid(column=7,row=rowPhase11+row_adj)
    date3_11_entry.grid(column=11, row=rowPhase11+row_adj)
    label3_d_11.grid(column=8,row=rowPhase11+row_adj)
    month3_11_entry.grid(column=9, row=rowPhase11+row_adj)
    label3_m_11.grid(column=10,row=rowPhase11+row_adj)
    year3_11_entry.grid(column=7, row=rowPhase11+row_adj) # ISO format
    space3_11_2.grid(column=12,row=rowPhase11+row_adj,padx=5)
    rad3_A_11.grid(column=13, row=rowPhase11+row_adj, pady=5)
    lbl3_A_11.grid(column=14, row=rowPhase11+row_adj, pady=5)
    spin3_A_11.grid(column=15,row=rowPhase11+row_adj, pady=5)
    label3_h1_11.grid(column=16,row=rowPhase11+row_adj, pady=5)
    spin3_B_11.grid(column=17,row=rowPhase11+row_adj, pady=5)
    label3_m1_11.grid(column=18,row=rowPhase11+row_adj, pady=5)
    lbl3_B_11.grid(column=19, row=rowPhase11+row_adj, pady=5)
    spin3_C_11.grid(column=20,row=rowPhase11+row_adj, pady=5)
    label3_h2_11.grid(column=21,row=rowPhase11+row_adj, pady=5)
    spin3_D_11.grid(column=22,row=rowPhase11+row_adj, pady=5)
    label3_m2_11.grid(column=23,row=rowPhase11+row_adj, pady=5)
    rad3_B_11.grid(column=24, row=rowPhase11+row_adj, padx=15, pady=5)
    rad3_C_11.grid(column=25, row=rowPhase11+row_adj, pady=5)

    # phase 12
    phaseLabel3_12 = Label(tab3, text='Phase 12')
    fromLabel3_12 = Label(tab3, text='From:')
    space3_12 = Label(tab3, text=' ')
    space3_12_2 = Label(tab3, text=' ')
    spin3_E_12 = Spinbox(tab3, from_=00, to=24, width=3, format='%02.0f')
    spin3_F_12 = Spinbox(tab3, from_=00, to=59, width=3, format='%02.0f')
    spin3_E_12.delete(0,'end')
    spin3_E_12.insert(0,'07')
    spin3_F_12.delete(0,'end')
    spin3_F_12.insert(0,'00')
    label3_h0_12 = Label(tab3, text=':')
    label3_m0_12 = Label(tab3, text='')
    date3_12_entry = Spinbox(tab3, from_=00, to=31, width=3, format='%02.0f')
    month3_12_entry = Spinbox(tab3, from_=00, to=12, width=3, format='%02.0f')
    year3_12_entry = Spinbox(tab3, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase12 = day_phase11 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date3_12_entry.delete(0,'end')
    date3_12_entry.insert(0,'{:02d}'.format(day_phase12.day))
    month3_12_entry.delete(0,'end')
    month3_12_entry.insert(0,'{:02d}'.format(day_phase12.month))
    year3_12_entry.delete(0,'end')
    year3_12_entry.insert(0,day_phase12.year)
    label3_d_12 = Label(tab3, text= '/')
    label3_m_12 = Label(tab3, text= '/')
    rad3_A_12 = Radiobutton(tab3, text='LD', variable=var3_12, value=1)
    lbl3_A_12 = Label(tab3, text= 'On:')
    spin3_A_12 = Spinbox(tab3, from_=00, to=24, width=3, format='%02.0f')
    spin3_B_12 = Spinbox(tab3, from_=00, to=59, width=3, format='%02.0f')
    spin3_A_12.delete(0,'end')
    spin3_A_12.insert(0,'07')
    spin3_B_12.delete(0,'end')
    spin3_B_12.insert(0,'00')
    label3_h1_12 = Label(tab3, text=':')
    label3_m1_12 = Label(tab3, text='')
    lbl3_B_12 = Label(tab3, text= 'Off:')
    spin3_C_12 = Spinbox(tab3, from_=00, to=24, width=3, format='%02.0f')
    spin3_D_12 = Spinbox(tab3, from_=00, to=59, width=3, format='%02.0f')
    spin3_C_12.delete(0,'end')
    spin3_C_12.insert(0,'19')
    spin3_D_12.delete(0,'end')
    spin3_D_12.insert(0,'00')
    label3_h2_12 = Label(tab3, text=':')
    label3_m2_12 = Label(tab3, text='')
    rad3_B_12 = Radiobutton(tab3, text='DD', variable=var3_12, value=2)
    rad3_C_12 = Radiobutton(tab3, text='LL', variable=var3_12, value=3)

    phaseLabel3_12.grid(column=0, row=rowPhase12+row_adj, padx=15, pady=5)
    fromLabel3_12.grid(column=1,row=rowPhase12+row_adj)
    spin3_E_12.grid(column=2,row=rowPhase12+row_adj)
    label3_h0_12.grid(column=3,row=rowPhase12+row_adj)
    spin3_F_12.grid(column=4,row=rowPhase12+row_adj)
    label3_m0_12.grid(column=5,row=rowPhase12+row_adj)
    space3_12.grid(column=7,row=rowPhase12+row_adj)
    date3_12_entry.grid(column=11, row=rowPhase12+row_adj)
    label3_d_12.grid(column=8,row=rowPhase12+row_adj)
    month3_12_entry.grid(column=9, row=rowPhase12+row_adj)
    label3_m_12.grid(column=10,row=rowPhase12+row_adj)
    year3_12_entry.grid(column=7, row=rowPhase12+row_adj) # ISO format
    space3_12_2.grid(column=12,row=rowPhase12+row_adj,padx=5)
    rad3_A_12.grid(column=13, row=rowPhase12+row_adj, pady=5)
    lbl3_A_12.grid(column=14, row=rowPhase12+row_adj, pady=5)
    spin3_A_12.grid(column=15,row=rowPhase12+row_adj, pady=5)
    label3_h1_12.grid(column=16,row=rowPhase12+row_adj, pady=5)
    spin3_B_12.grid(column=17,row=rowPhase12+row_adj, pady=5)
    label3_m1_12.grid(column=18,row=rowPhase12+row_adj, pady=5)
    lbl3_B_12.grid(column=19, row=rowPhase12+row_adj, pady=5)
    spin3_C_12.grid(column=20,row=rowPhase12+row_adj, pady=5)
    label3_h2_12.grid(column=21,row=rowPhase12+row_adj, pady=5)
    spin3_D_12.grid(column=22,row=rowPhase12+row_adj, pady=5)
    label3_m2_12.grid(column=23,row=rowPhase12+row_adj, pady=5)
    rad3_B_12.grid(column=24, row=rowPhase12+row_adj, padx=15, pady=5)
    rad3_C_12.grid(column=25, row=rowPhase12+row_adj, pady=5)
    
    
   

    
    
    # Box4 main


    tcyclelabel4 = Label(tab4, text='T-cycle length')
    tcyclelabel4.grid(column=26, row=1, padx=3, pady=5)

    for i in range(0,12): 
        tcyclelength = Spinbox(tab4, from_=12, to=48, width=3) 
        tcyclelength.grid(column=26, row=2+i+row_adj, padx=3,pady=5)
        tcyclelength.delete(0,'end')
        tcyclelength.insert(0,24)
        tcyclespinbox_arr[3,i] = tcyclelength
        
    tcyclespinbox_arr[3,0].grid(column=26, row=1+row_adj, pady=5)
        
    
    tab4_title = Label(tab4, text= 'LED schedule', anchor='center')
    tab4_title.grid(column=12, row= 1, columnspan='27', sticky='we')
    # capSep4 = ttk.Separator(tab4, orient=HORIZONTAL)
    # capSep4.grid(column=0, row = row_adj+5, columnspan='27', sticky='we')
    box4sched_text=StringVar()
    box4sched_text.set('Schedule not set.')
    box4sched_stat=Label(tab4, textvariable=box4sched_text, anchor=W, justify=LEFT)
        # phase 1
    phaseLabel4_1 = Label(tab4, text='Phase 1')
    dateLabel = time.strftime('%H:%M   %Y/%m/%d') # reads time for Phase 1 start-time
    fromLabel4_1 = Label(tab4, text='From:')
    date_label4 = Label(tab4, text=dateLabel)
    rad4_A_1 = Radiobutton(tab4, text='LD', variable=var4_1, value=1)
    lbl4_A_1 = Label(tab4, text= 'On:')
    spin4_A_1 = Spinbox(tab4, from_=00, to=24, width=3, format='%02.0f')
    spin4_B_1 = Spinbox(tab4, from_=00, to=59, width=3, format='%02.0f')
    spin4_A_1.delete(0,'end')
    spin4_A_1.insert(0,'07')
    spin4_B_1.delete(0,'end')
    spin4_B_1.insert(0,'00')
    label4_h1_1 = Label(tab4, text=':')
    label4_m1_1 = Label(tab4, text='')
    lbl4_B_1 = Label(tab4, text= 'Off:')
    spin4_C_1 = Spinbox(tab4, from_=00, to=24, width=3, format='%02.0f')
    spin4_D_1 = Spinbox(tab4, from_=00, to=59, width=3, format='%02.0f')
    spin4_C_1.delete(0,'end')
    spin4_C_1.insert(0,'19')
    spin4_D_1.delete(0,'end')
    spin4_D_1.insert(0,'00')
    label4_h2_1 = Label(tab4, text=':')
    label4_m2_1 = Label(tab4, text='')
    rad4_B_1 = Radiobutton(tab4, text='DD', variable=var4_1, value=2)
    rad4_C_1 = Radiobutton(tab4, text='LL', variable=var4_1, value=3)
    phaseLabel4_1.grid(column=0, row=1+row_adj, padx=15, pady=5)
    fromLabel4_1.grid(column=1,row=1+row_adj)
    date_label4.grid(column=2, row=1+row_adj, columnspan='10', sticky='w')
    rad4_A_1.grid(column=13, row=1+row_adj, pady=5)
    lbl4_A_1.grid(column=14, row=1+row_adj, pady=5)
    spin4_A_1.grid(column=15,row=1+row_adj, pady=5)
    label4_h1_1.grid(column=16,row=1+row_adj, pady=5, sticky='w')
    spin4_B_1.grid(column=17,row=1+row_adj, pady=5)
    label4_m1_1.grid(column=18,row=1+row_adj, pady=5, sticky='w')
    lbl4_B_1.grid(column=19, row=1+row_adj, pady=5)
    spin4_C_1.grid(column=20,row=1+row_adj, pady=5)
    label4_h2_1.grid(column=21,row=1+row_adj, pady=5, sticky='w')
    spin4_D_1.grid(column=22,row=1+row_adj, pady=5)
    label4_m2_1.grid(column=23,row=1+row_adj, pady=5, sticky='w')
    rad4_B_1.grid(column=24, row=1+row_adj, padx=15, pady=5)
    rad4_C_1.grid(column=25, row=1+row_adj, pady=5)
        # phase 2
    phaseLabel4_2 = Label(tab4, text='Phase 2')
    fromLabel4_2 = Label(tab4, text='From:')
    space4_2 = Label(tab4, text=' ')
    space4_2_2 = Label(tab4, text=' ')
    spin4_E_2 = Spinbox(tab4, from_=00, to=24, width=3, format='%02.0f')
    spin4_F_2 = Spinbox(tab4, from_=00, to=59, width=3, format='%02.0f')
    spin4_E_2.delete(0,'end')
    spin4_E_2.insert(0,'07')
    spin4_F_2.delete(0,'end')
    spin4_F_2.insert(0,'00')
    label4_h0_2 = Label(tab4, text=':')
    label4_m0_2 = Label(tab4, text='')
    date4_2_entry = Spinbox(tab4, from_=00, to=31, width=3, format='%02.0f')
    month4_2_entry = Spinbox(tab4, from_=00, to=12, width=3, format='%02.0f')
    year4_2_entry = Spinbox(tab4, from_=2018, to=2030, width=5)
    date4_2_entry.delete(0,'end')
    today=datetime.date.today() # today
    day_phase2 = today + datetime.timedelta(days=7) # calculate dates for 7 days after recording initiation
    date4_2_entry.insert(0,'{:02d}'.format(day_phase2.day))
    month4_2_entry.delete(0,'end')
    month4_2_entry.insert(0,'{:02d}'.format(day_phase2.month))
    year4_2_entry.delete(0,'end')
    year4_2_entry.insert(0,day_phase2.year) # ISO format is YYYY/MM/DD

    label3_d_0 = Label(tab4, text= 'Month')
    label3_m_0 = Label(tab4, text= 'Date')
    label3_m_0.grid(column=11,row=2+row_adj)
    label3_d_0.grid(column=9,row=2+row_adj)
    label3_d_1 = Label(tab4, text= '/')
    label3_m_1 = Label(tab4, text= '/')
    label3_d_1.grid(column=8,row=2+row_adj)
    label3_m_1.grid(column=10,row=2+row_adj)

    label4_d_2 = Label(tab4, text= '/')
    label4_m_2 = Label(tab4, text= '/')
    rad4_A_2 = Radiobutton(tab4, text='LD', variable=var4_2, value=1)
    lbl4_A_2 = Label(tab4, text= 'On:')
    spin4_A_2 = Spinbox(tab4, from_=00, to=24, width=3, format='%02.0f')
    spin4_B_2 = Spinbox(tab4, from_=00, to=59, width=3, format='%02.0f')
    spin4_A_2.delete(0,'end')
    spin4_A_2.insert(0,'07')
    spin4_B_2.delete(0,'end')
    spin4_B_2.insert(0,'00')
    label4_h1_2 = Label(tab4, text=':')
    label4_m1_2 = Label(tab4, text='')
    lbl4_B_2 = Label(tab4, text= 'Off:')
    spin4_C_2 = Spinbox(tab4, from_=00, to=24, width=3, format='%02.0f')
    spin4_D_2 = Spinbox(tab4, from_=00, to=59, width=3, format='%02.0f')
    spin4_C_2.delete(0,'end')
    spin4_C_2.insert(0,'19')
    spin4_D_2.delete(0,'end')
    spin4_D_2.insert(0,'00')
    label4_h2_2 = Label(tab4, text=':')
    label4_m2_2 = Label(tab4, text='')
    rad4_B_2 = Radiobutton(tab4, text='DD', variable=var4_2, value=2)
    rad4_C_2 = Radiobutton(tab4, text='LL', variable=var4_2, value=3)
    phaseLabel4_2.grid(column=0, row=3+row_adj, padx=15, pady=5)
    fromLabel4_2.grid(column=1,row=3+row_adj)
    spin4_E_2.grid(column=2,row=3+row_adj)
    label4_h0_2.grid(column=3,row=3+row_adj)
    spin4_F_2.grid(column=4,row=3+row_adj)
    label4_m0_2.grid(column=5,row=3+row_adj)
    space4_2.grid(column=6,row=3+row_adj)
    date4_2_entry.grid(column=11, row=3+row_adj)
    label4_d_2.grid(column=8,row=3+row_adj)
    month4_2_entry.grid(column=9, row=3+row_adj)
    label4_m_2.grid(column=10,row=3+row_adj)
    year4_2_entry.grid(column=7, row=3+row_adj) # ISO format
    space4_2_2.grid(column=12,row=3+row_adj,padx=5)
    rad4_A_2.grid(column=13, row=3+row_adj, pady=5)
    lbl4_A_2.grid(column=14, row=3+row_adj, pady=5)
    spin4_A_2.grid(column=15,row=3+row_adj, pady=5)
    label4_h1_2.grid(column=16,row=3+row_adj, pady=5)
    spin4_B_2.grid(column=17,row=3+row_adj, pady=5)
    label4_m1_2.grid(column=18,row=3+row_adj, pady=5)
    lbl4_B_2.grid(column=19, row=3+row_adj, pady=5)
    spin4_C_2.grid(column=20,row=3+row_adj, pady=5)
    label4_h2_2.grid(column=21,row=3+row_adj, pady=5)
    spin4_D_2.grid(column=22,row=3+row_adj, pady=5)
    label4_m2_2.grid(column=23,row=3+row_adj, pady=5)
    rad4_B_2.grid(column=24, row=3+row_adj, padx=15, pady=5)
    rad4_C_2.grid(column=25, row=3+row_adj, pady=5)

        # phase 3
    phaseLabel4_3 = Label(tab4, text='Phase 3')
    fromLabel4_3 = Label(tab4, text='From:')
    space4_3 = Label(tab4, text=' ')
    spin4_E_3 = Spinbox(tab4, from_=00, to=24, width=3, format='%02.0f')
    spin4_F_3 = Spinbox(tab4, from_=00, to=59, width=3, format='%02.0f')
    spin4_E_3.delete(0,'end')
    spin4_E_3.insert(0,'07')
    spin4_F_3.delete(0,'end')
    spin4_F_3.insert(0,'00')
    label4_h0_3 = Label(tab4, text=':')
    label4_m0_3 = Label(tab4, text='')
    date4_3_entry = Spinbox(tab4, from_=00, to=31, width=3, format='%02.0f')
    month4_3_entry = Spinbox(tab4, from_=00, to=12, width=3, format='%02.0f')
    year4_3_entry = Spinbox(tab4, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase3 = day_phase2 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date4_3_entry.delete(0,'end')
    date4_3_entry.insert(0,'{:02d}'.format(day_phase3.day))
    month4_3_entry.delete(0,'end')
    month4_3_entry.insert(0,'{:02d}'.format(day_phase3.month))
    year4_3_entry.delete(0,'end')
    year4_3_entry.insert(0,day_phase3.year)
    label4_d_3 = Label(tab4, text= '/')
    label4_m_3 = Label(tab4, text= '/')
    rad4_A_3 = Radiobutton(tab4, text='LD', variable=var4_3, value=1)
    lbl4_A_3 = Label(tab4, text= 'On:')
    spin4_A_3 = Spinbox(tab4, from_=00, to=24, width=3, format='%02.0f')
    spin4_B_3 = Spinbox(tab4, from_=00, to=59, width=3, format='%02.0f')
    spin4_A_3.delete(0,'end')
    spin4_A_3.insert(0,'07')
    spin4_B_3.delete(0,'end')
    spin4_B_3.insert(0,'00')
    label4_h1_3 = Label(tab4, text=':')
    label4_m1_3 = Label(tab4, text='')
    lbl4_B_3 = Label(tab4, text= 'Off:')
    spin4_C_3 = Spinbox(tab4, from_=00, to=24, width=3, format='%02.0f')
    spin4_D_3 = Spinbox(tab4, from_=00, to=59, width=3, format='%02.0f')
    spin4_C_3.delete(0,'end')
    spin4_C_3.insert(0,'19')
    spin4_D_3.delete(0,'end')
    spin4_D_3.insert(0,'00')
    label4_h2_3 = Label(tab4, text=':')
    label4_m2_3 = Label(tab4, text='')
    rad4_B_3 = Radiobutton(tab4, text='DD', variable=var4_3, value=2)
    rad4_C_3 = Radiobutton(tab4, text='LL', variable=var4_3, value=3)
    phaseLabel4_3.grid(column=0, row=4+row_adj, padx=15, pady=5)
    fromLabel4_3.grid(column=1,row=4+row_adj)
    spin4_E_3.grid(column=2,row=4+row_adj)
    label4_h0_3.grid(column=3,row=4+row_adj)
    spin4_F_3.grid(column=4,row=4+row_adj)
    label4_m0_3.grid(column=5,row=4+row_adj)
    space4_3.grid(column=6,row=4+row_adj)
    date4_3_entry.grid(column=11, row=4+row_adj)
    label4_d_3.grid(column=8,row=4+row_adj)
    month4_3_entry.grid(column=9, row=4+row_adj)
    label4_m_3.grid(column=10,row=4+row_adj)
    year4_3_entry.grid(column=7, row=4+row_adj)
    rad4_A_3.grid(column=13, row=4+row_adj, pady=5)
    lbl4_A_3.grid(column=14, row=4+row_adj, pady=5)
    spin4_A_3.grid(column=15,row=4+row_adj, pady=5)
    label4_h1_3.grid(column=16,row=4+row_adj, pady=5)
    spin4_B_3.grid(column=17,row=4+row_adj, pady=5)
    label4_m1_3.grid(column=18,row=4+row_adj, pady=5)
    lbl4_B_3.grid(column=19, row=4+row_adj, pady=5)
    spin4_C_3.grid(column=20,row=4+row_adj, pady=5)
    label4_h2_3.grid(column=21,row=4+row_adj, pady=5)
    spin4_D_3.grid(column=22,row=4+row_adj, pady=5)
    label4_m2_3.grid(column=23,row=4+row_adj, pady=5)
    rad4_B_3.grid(column=24, row=4+row_adj, padx=15, pady=5)
    rad4_C_3.grid(column=25, row=4+row_adj, pady=5)

        # phase 4
    phaseLabel4_4 = Label(tab4, text='Phase 4')
    fromLabel4_4 = Label(tab4, text='From:')
    space4_4 = Label(tab4, text=' ')
    space4_4_2 = Label(tab4, text=' ')
    spin4_E_4 = Spinbox(tab4, from_=00, to=24, width=3, format='%02.0f')
    spin4_F_4 = Spinbox(tab4, from_=00, to=59, width=3, format='%02.0f')
    spin4_E_4.delete(0,'end')
    spin4_E_4.insert(0,'07')
    spin4_F_4.delete(0,'end')
    spin4_F_4.insert(0,'00')
    label4_h0_4 = Label(tab4, text=':')
    label4_m0_4 = Label(tab4, text='')
    date4_4_entry = Spinbox(tab4, from_=00, to=31, width=3, format='%02.0f')
    month4_4_entry = Spinbox(tab4, from_=00, to=12, width=3, format='%02.0f')
    year4_4_entry = Spinbox(tab4, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase4 = day_phase3 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date4_4_entry.delete(0,'end')
    date4_4_entry.insert(0,'{:02d}'.format(day_phase4.day))
    month4_4_entry.delete(0,'end')
    month4_4_entry.insert(0,'{:02d}'.format(day_phase4.month))
    year4_4_entry.delete(0,'end')
    year4_4_entry.insert(0,day_phase4.year)
    label4_d_4 = Label(tab4, text= '/')
    label4_m_4 = Label(tab4, text= '/')
    rad4_A_4 = Radiobutton(tab4, text='LD', variable=var4_4, value=1)
    lbl4_A_4 = Label(tab4, text= 'On:')
    spin4_A_4 = Spinbox(tab4, from_=00, to=24, width=3, format='%02.0f')
    spin4_B_4 = Spinbox(tab4, from_=00, to=59, width=3, format='%02.0f')
    spin4_A_4.delete(0,'end')
    spin4_A_4.insert(0,'07')
    spin4_B_4.delete(0,'end')
    spin4_B_4.insert(0,'00')
    label4_h1_4 = Label(tab4, text=':')
    label4_m1_4 = Label(tab4, text='')
    lbl4_B_4 = Label(tab4, text= 'Off:')
    spin4_C_4 = Spinbox(tab4, from_=00, to=24, width=3, format='%02.0f')
    spin4_D_4 = Spinbox(tab4, from_=00, to=59, width=3, format='%02.0f')
    spin4_C_4.delete(0,'end')
    spin4_C_4.insert(0,'19')
    spin4_D_4.delete(0,'end')
    spin4_D_4.insert(0,'00')
    label4_h2_4 = Label(tab4, text=':')
    label4_m2_4 = Label(tab4, text='')
    rad4_B_4 = Radiobutton(tab4, text='DD', variable=var4_4, value=2)
    rad4_C_4 = Radiobutton(tab4, text='LL', variable=var4_4, value=3)
    phaseLabel4_4.grid(column=0, row=5+row_adj, padx=15, pady=5)
    fromLabel4_4.grid(column=1,row=5+row_adj)
    spin4_E_4.grid(column=2,row=5+row_adj)
    label4_h0_4.grid(column=3,row=5+row_adj)
    spin4_F_4.grid(column=4,row=5+row_adj)
    label4_m0_4.grid(column=5,row=5+row_adj)
    space4_4.grid(column=6,row=5+row_adj)
    date4_4_entry.grid(column=11, row=5+row_adj)
    label4_d_4.grid(column=8,row=5+row_adj)
    month4_4_entry.grid(column=9, row=5+row_adj)
    label4_m_4.grid(column=10,row=5+row_adj)
    year4_4_entry.grid(column=7, row=5+row_adj) # ISO format
    space4_4_2.grid(column=12,row=5+row_adj,padx=5)
    rad4_A_4.grid(column=13, row=5+row_adj, pady=5)
    lbl4_A_4.grid(column=14, row=5+row_adj, pady=5)
    spin4_A_4.grid(column=15,row=5+row_adj, pady=5)
    label4_h1_4.grid(column=16,row=5+row_adj, pady=5)
    spin4_B_4.grid(column=17,row=5+row_adj, pady=5)
    label4_m1_4.grid(column=18,row=5+row_adj, pady=5)
    lbl4_B_4.grid(column=19, row=5+row_adj, pady=5)
    spin4_C_4.grid(column=20,row=5+row_adj, pady=5)
    label4_h2_4.grid(column=21,row=5+row_adj, pady=5)
    spin4_D_4.grid(column=22,row=5+row_adj, pady=5)
    label4_m2_4.grid(column=23,row=5+row_adj, pady=5)
    rad4_B_4.grid(column=24, row=5+row_adj, padx=15, pady=5)
    rad4_C_4.grid(column=25, row=5+row_adj, pady=5)

    # phase 5
    phaseLabel4_5 = Label(tab4, text='Phase 5')
    fromLabel4_5 = Label(tab4, text='From:')
    space4_5 = Label(tab4, text=' ')
    space4_5_2 = Label(tab4, text=' ')
    spin4_E_5 = Spinbox(tab4, from_=00, to=24, width=3, format='%02.0f')
    spin4_F_5 = Spinbox(tab4, from_=00, to=59, width=3, format='%02.0f')
    spin4_E_5.delete(0,'end')
    spin4_E_5.insert(0,'07')
    spin4_F_5.delete(0,'end')
    spin4_F_5.insert(0,'00')
    label4_h0_5 = Label(tab4, text=':')
    label4_m0_5 = Label(tab4, text='')
    date4_5_entry = Spinbox(tab4, from_=00, to=31, width=3, format='%02.0f')
    month4_5_entry = Spinbox(tab4, from_=00, to=12, width=3, format='%02.0f')
    year4_5_entry = Spinbox(tab4, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase5 = day_phase4 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date4_5_entry.delete(0,'end')
    date4_5_entry.insert(0,'{:02d}'.format(day_phase5.day))
    month4_5_entry.delete(0,'end')
    month4_5_entry.insert(0,'{:02d}'.format(day_phase5.month))
    year4_5_entry.delete(0,'end')
    year4_5_entry.insert(0,day_phase4.year)
    label4_d_5 = Label(tab4, text= '/')
    label4_m_5 = Label(tab4, text= '/')
    rad4_A_5 = Radiobutton(tab4, text='LD', variable=var4_5, value=1)
    lbl4_A_5 = Label(tab4, text= 'On:')
    spin4_A_5 = Spinbox(tab4, from_=00, to=24, width=3, format='%02.0f')
    spin4_B_5 = Spinbox(tab4, from_=00, to=59, width=3, format='%02.0f')
    spin4_A_5.delete(0,'end')
    spin4_A_5.insert(0,'07')
    spin4_B_5.delete(0,'end')
    spin4_B_5.insert(0,'00')
    label4_h1_5 = Label(tab4, text=':')
    label4_m1_5 = Label(tab4, text='')
    lbl4_B_5 = Label(tab4, text= 'Off:')
    spin4_C_5 = Spinbox(tab4, from_=00, to=24, width=3, format='%02.0f')
    spin4_D_5 = Spinbox(tab4, from_=00, to=59, width=3, format='%02.0f')
    spin4_C_5.delete(0,'end')
    spin4_C_5.insert(0,'19')
    spin4_D_5.delete(0,'end')
    spin4_D_5.insert(0,'00')
    label4_h2_5 = Label(tab4, text=':')
    label4_m2_5 = Label(tab4, text='')
    rad4_B_5 = Radiobutton(tab4, text='DD', variable=var4_5, value=2)
    rad4_C_5 = Radiobutton(tab4, text='LL', variable=var4_5, value=3)
    phaseLabel4_5.grid(column=0, row=6+row_adj, padx=15, pady=5)
    fromLabel4_5.grid(column=1,row=6+row_adj)
    spin4_E_5.grid(column=2,row=6+row_adj)
    label4_h0_5.grid(column=3,row=6+row_adj)
    spin4_F_5.grid(column=4,row=6+row_adj)
    label4_m0_5.grid(column=5,row=6+row_adj)
    space4_5.grid(column=6,row=6+row_adj)
    date4_5_entry.grid(column=11, row=6+row_adj)
    label4_d_5.grid(column=8,row=6+row_adj)
    month4_5_entry.grid(column=9, row=6+row_adj)
    label4_m_5.grid(column=10,row=6+row_adj)
    year4_5_entry.grid(column=7, row=6+row_adj) # ISO format
    space4_5_2.grid(column=12,row=6+row_adj,padx=5)
    rad4_A_5.grid(column=13, row=6+row_adj, pady=5)
    lbl4_A_5.grid(column=14, row=6+row_adj, pady=5)
    spin4_A_5.grid(column=15,row=6+row_adj, pady=5)
    label4_h1_5.grid(column=16,row=6+row_adj, pady=5)
    spin4_B_5.grid(column=17,row=6+row_adj, pady=5)
    label4_m1_5.grid(column=18,row=6+row_adj, pady=5)
    lbl4_B_5.grid(column=19, row=6+row_adj, pady=5)
    spin4_C_5.grid(column=20,row=6+row_adj, pady=5)
    label4_h2_5.grid(column=21,row=6+row_adj, pady=5)
    spin4_D_5.grid(column=22,row=6+row_adj, pady=5)
    label4_m2_5.grid(column=23,row=6+row_adj, pady=5)
    rad4_B_5.grid(column=24, row=6+row_adj, padx=15, pady=5)
    rad4_C_5.grid(column=25, row=6+row_adj, pady=5)

        # phase 6
    phaseLabel4_6 = Label(tab4, text='Phase 6')
    fromLabel4_6 = Label(tab4, text='From:')
    space4_6 = Label(tab4, text=' ')
    space4_6_2 = Label(tab4, text=' ')
    spin4_E_6 = Spinbox(tab4, from_=00, to=24, width=3, format='%02.0f')
    spin4_F_6 = Spinbox(tab4, from_=00, to=59, width=3, format='%02.0f')
    spin4_E_6.delete(0,'end')
    spin4_E_6.insert(0,'07')
    spin4_F_6.delete(0,'end')
    spin4_F_6.insert(0,'00')
    label4_h0_6 = Label(tab4, text=':')
    label4_m0_6 = Label(tab4, text='')
    date4_6_entry = Spinbox(tab4, from_=00, to=31, width=3, format='%02.0f')
    month4_6_entry = Spinbox(tab4, from_=00, to=12, width=3, format='%02.0f')
    year4_6_entry = Spinbox(tab4, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase6 = day_phase5 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date4_6_entry.delete(0,'end')
    date4_6_entry.insert(0,'{:02d}'.format(day_phase6.day))
    month4_6_entry.delete(0,'end')
    month4_6_entry.insert(0,'{:02d}'.format(day_phase6.month))
    year4_6_entry.delete(0,'end')
    year4_6_entry.insert(0,day_phase6.year)
    label4_d_6 = Label(tab4, text= '/')
    label4_m_6 = Label(tab4, text= '/')
    rad4_A_6 = Radiobutton(tab4, text='LD', variable=var4_6, value=1)
    lbl4_A_6 = Label(tab4, text= 'On:')
    spin4_A_6 = Spinbox(tab4, from_=00, to=24, width=3, format='%02.0f')
    spin4_B_6 = Spinbox(tab4, from_=00, to=59, width=3, format='%02.0f')
    spin4_A_6.delete(0,'end')
    spin4_A_6.insert(0,'07')
    spin4_B_6.delete(0,'end')
    spin4_B_6.insert(0,'00')
    label4_h1_6 = Label(tab4, text=':')
    label4_m1_6 = Label(tab4, text='')
    lbl4_B_6 = Label(tab4, text= 'Off:')
    spin4_C_6 = Spinbox(tab4, from_=00, to=24, width=3, format='%02.0f')
    spin4_D_6 = Spinbox(tab4, from_=00, to=59, width=3, format='%02.0f')
    spin4_C_6.delete(0,'end')
    spin4_C_6.insert(0,'19')
    spin4_D_6.delete(0,'end')
    spin4_D_6.insert(0,'00')
    label4_h2_6 = Label(tab4, text=':')
    label4_m2_6 = Label(tab4, text='')
    rad4_B_6 = Radiobutton(tab4, text='DD', variable=var4_6, value=2)
    rad4_C_6 = Radiobutton(tab4, text='LL', variable=var4_6, value=3)
    
    
    phaseLabel4_6.grid(column=0, row=rowPhase6+row_adj, padx=15, pady=5)
    fromLabel4_6.grid(column=1,row=rowPhase6+row_adj)
    spin4_E_6.grid(column=2,row=rowPhase6+row_adj)
    label4_h0_6.grid(column=3,row=rowPhase6+row_adj)
    spin4_F_6.grid(column=4,row=rowPhase6+row_adj)
    label4_m0_6.grid(column=5,row=rowPhase6+row_adj)
    space4_6.grid(column=6,row=rowPhase6+row_adj)
    date4_6_entry.grid(column=11, row=rowPhase6+row_adj)
    label4_d_6.grid(column=8,row=rowPhase6+row_adj)
    month4_6_entry.grid(column=9, row=rowPhase6+row_adj)
    label4_m_6.grid(column=10,row=rowPhase6+row_adj)
    year4_6_entry.grid(column=7, row=rowPhase6+row_adj) # ISO format
    space4_6_2.grid(column=12,row=rowPhase6+row_adj,padx=5)
    rad4_A_6.grid(column=13, row=rowPhase6+row_adj, pady=5)
    lbl4_A_6.grid(column=14, row=rowPhase6+row_adj, pady=5)
    spin4_A_6.grid(column=15,row=rowPhase6+row_adj, pady=5)
    label4_h1_6.grid(column=16,row=rowPhase6+row_adj, pady=5)
    spin4_B_6.grid(column=17,row=rowPhase6+row_adj, pady=5)
    label4_m1_6.grid(column=18,row=rowPhase6+row_adj, pady=5)
    lbl4_B_6.grid(column=19, row=rowPhase6+row_adj, pady=5)
    spin4_C_6.grid(column=20,row=rowPhase6+row_adj, pady=5)
    label4_h2_6.grid(column=21,row=rowPhase6+row_adj, pady=5)
    spin4_D_6.grid(column=22,row=rowPhase6+row_adj, pady=5)
    label4_m2_6.grid(column=23,row=rowPhase6+row_adj, pady=5)
    rad4_B_6.grid(column=24, row=rowPhase6+row_adj, padx=15, pady=5)
    rad4_C_6.grid(column=25, row=rowPhase6+row_adj, pady=5)

        # phase 7
    phaseLabel4_7 = Label(tab4, text='Phase 7')
    fromLabel4_7 = Label(tab4, text='From:')
    space4_7 = Label(tab4, text=' ')
    space4_7_2 = Label(tab4, text=' ')
    spin4_E_7 = Spinbox(tab4, from_=00, to=24, width=3, format='%02.0f')
    spin4_F_7 = Spinbox(tab4, from_=00, to=59, width=3, format='%02.0f')
    spin4_E_7.delete(0,'end')
    spin4_E_7.insert(0,'07')
    spin4_F_7.delete(0,'end')
    spin4_F_7.insert(0,'00')
    label4_h0_7 = Label(tab4, text=':')
    label4_m0_7 = Label(tab4, text='')
    date4_7_entry = Spinbox(tab4, from_=00, to=31, width=3, format='%02.0f')
    month4_7_entry = Spinbox(tab4, from_=00, to=12, width=3, format='%02.0f')
    year4_7_entry = Spinbox(tab4, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase7 = day_phase6 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date4_7_entry.delete(0,'end')
    date4_7_entry.insert(0,'{:02d}'.format(day_phase7.day))
    month4_7_entry.delete(0,'end')
    month4_7_entry.insert(0,'{:02d}'.format(day_phase7.month))
    year4_7_entry.delete(0,'end')
    year4_7_entry.insert(0,day_phase7.year)
    label4_d_7 = Label(tab4, text= '/')
    label4_m_7 = Label(tab4, text= '/')
    rad4_A_7 = Radiobutton(tab4, text='LD', variable=var4_7, value=1)
    lbl4_A_7 = Label(tab4, text= 'On:')
    spin4_A_7 = Spinbox(tab4, from_=00, to=24, width=3, format='%02.0f')
    spin4_B_7 = Spinbox(tab4, from_=00, to=59, width=3, format='%02.0f')
    spin4_A_7.delete(0,'end')
    spin4_A_7.insert(0,'07')
    spin4_B_7.delete(0,'end')
    spin4_B_7.insert(0,'00')
    label4_h1_7 = Label(tab4, text=':')
    label4_m1_7 = Label(tab4, text='')
    lbl4_B_7 = Label(tab4, text= 'Off:')
    spin4_C_7 = Spinbox(tab4, from_=00, to=24, width=3, format='%02.0f')
    spin4_D_7 = Spinbox(tab4, from_=00, to=59, width=3, format='%02.0f')
    spin4_C_7.delete(0,'end')
    spin4_C_7.insert(0,'19')
    spin4_D_7.delete(0,'end')
    spin4_D_7.insert(0,'00')
    label4_h2_7 = Label(tab4, text=':')
    label4_m2_7 = Label(tab4, text='')
    rad4_B_7 = Radiobutton(tab4, text='DD', variable=var4_7, value=2)
    rad4_C_7 = Radiobutton(tab4, text='LL', variable=var4_7, value=3)
    
    
    phaseLabel4_7.grid(column=0, row=rowPhase7+row_adj, padx=15, pady=5)
    fromLabel4_7.grid(column=1,row=rowPhase7+row_adj)
    spin4_E_7.grid(column=2,row=rowPhase7+row_adj)
    label4_h0_7.grid(column=3,row=rowPhase7+row_adj)
    spin4_F_7.grid(column=4,row=rowPhase7+row_adj)
    label4_m0_7.grid(column=5,row=rowPhase7+row_adj)
    space4_7.grid(column=7,row=rowPhase7+row_adj)
    date4_7_entry.grid(column=11, row=rowPhase7+row_adj)
    label4_d_7.grid(column=8,row=rowPhase7+row_adj)
    month4_7_entry.grid(column=9, row=rowPhase7+row_adj)
    label4_m_7.grid(column=10,row=rowPhase7+row_adj)
    year4_7_entry.grid(column=7, row=rowPhase7+row_adj) # ISO format
    space4_7_2.grid(column=12,row=rowPhase7+row_adj,padx=5)
    rad4_A_7.grid(column=13, row=rowPhase7+row_adj, pady=5)
    lbl4_A_7.grid(column=14, row=rowPhase7+row_adj, pady=5)
    spin4_A_7.grid(column=15,row=rowPhase7+row_adj, pady=5)
    label4_h1_7.grid(column=16,row=rowPhase7+row_adj, pady=5)
    spin4_B_7.grid(column=17,row=rowPhase7+row_adj, pady=5)
    label4_m1_7.grid(column=18,row=rowPhase7+row_adj, pady=5)
    lbl4_B_7.grid(column=19, row=rowPhase7+row_adj, pady=5)
    spin4_C_7.grid(column=20,row=rowPhase7+row_adj, pady=5)
    label4_h2_7.grid(column=21,row=rowPhase7+row_adj, pady=5)
    spin4_D_7.grid(column=22,row=rowPhase7+row_adj, pady=5)
    label4_m2_7.grid(column=23,row=rowPhase7+row_adj, pady=5)
    rad4_B_7.grid(column=24, row=rowPhase7+row_adj, padx=15, pady=5)
    rad4_C_7.grid(column=25, row=rowPhase7+row_adj, pady=5)

        # phase 8
    phaseLabel4_8 = Label(tab4, text='Phase 8')
    fromLabel4_8 = Label(tab4, text='From:')
    space4_8 = Label(tab4, text=' ')
    space4_8_2 = Label(tab4, text=' ')
    spin4_E_8 = Spinbox(tab4, from_=00, to=24, width=3, format='%02.0f')
    spin4_F_8 = Spinbox(tab4, from_=00, to=59, width=3, format='%02.0f')
    spin4_E_8.delete(0,'end')
    spin4_E_8.insert(0,'07')
    spin4_F_8.delete(0,'end')
    spin4_F_8.insert(0,'00')
    label4_h0_8 = Label(tab4, text=':')
    label4_m0_8 = Label(tab4, text='')
    date4_8_entry = Spinbox(tab4, from_=00, to=31, width=3, format='%02.0f')
    month4_8_entry = Spinbox(tab4, from_=00, to=12, width=3, format='%02.0f')
    year4_8_entry = Spinbox(tab4, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase8 = day_phase7 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date4_8_entry.delete(0,'end')
    date4_8_entry.insert(0,'{:02d}'.format(day_phase8.day))
    month4_8_entry.delete(0,'end')
    month4_8_entry.insert(0,'{:02d}'.format(day_phase8.month))
    year4_8_entry.delete(0,'end')
    year4_8_entry.insert(0,day_phase8.year)
    label4_d_8 = Label(tab4, text= '/')
    label4_m_8 = Label(tab4, text= '/')
    rad4_A_8 = Radiobutton(tab4, text='LD', variable=var4_8, value=1)
    lbl4_A_8 = Label(tab4, text= 'On:')
    spin4_A_8 = Spinbox(tab4, from_=00, to=24, width=3, format='%02.0f')
    spin4_B_8 = Spinbox(tab4, from_=00, to=59, width=3, format='%02.0f')
    spin4_A_8.delete(0,'end')
    spin4_A_8.insert(0,'07')
    spin4_B_8.delete(0,'end')
    spin4_B_8.insert(0,'00')
    label4_h1_8 = Label(tab4, text=':')
    label4_m1_8 = Label(tab4, text='')
    lbl4_B_8 = Label(tab4, text= 'Off:')
    spin4_C_8 = Spinbox(tab4, from_=00, to=24, width=3, format='%02.0f')
    spin4_D_8 = Spinbox(tab4, from_=00, to=59, width=3, format='%02.0f')
    spin4_C_8.delete(0,'end')
    spin4_C_8.insert(0,'19')
    spin4_D_8.delete(0,'end')
    spin4_D_8.insert(0,'00')
    label4_h2_8 = Label(tab4, text=':')
    label4_m2_8 = Label(tab4, text='')
    rad4_B_8 = Radiobutton(tab4, text='DD', variable=var4_8, value=2)
    rad4_C_8 = Radiobutton(tab4, text='LL', variable=var4_8, value=3)
    
    
    phaseLabel4_8.grid(column=0, row=rowPhase8+row_adj, padx=15, pady=5)
    fromLabel4_8.grid(column=1,row=rowPhase8+row_adj)
    spin4_E_8.grid(column=2,row=rowPhase8+row_adj)
    label4_h0_8.grid(column=3,row=rowPhase8+row_adj)
    spin4_F_8.grid(column=4,row=rowPhase8+row_adj)
    label4_m0_8.grid(column=5,row=rowPhase8+row_adj)
    space4_8.grid(column=7,row=rowPhase8+row_adj)
    date4_8_entry.grid(column=11, row=rowPhase8+row_adj)
    label4_d_8.grid(column=8,row=rowPhase8+row_adj)
    month4_8_entry.grid(column=9, row=rowPhase8+row_adj)
    label4_m_8.grid(column=10,row=rowPhase8+row_adj)
    year4_8_entry.grid(column=7, row=rowPhase8+row_adj) # ISO format
    space4_8_2.grid(column=12,row=rowPhase8+row_adj,padx=5)
    rad4_A_8.grid(column=13, row=rowPhase8+row_adj, pady=5)
    lbl4_A_8.grid(column=14, row=rowPhase8+row_adj, pady=5)
    spin4_A_8.grid(column=15,row=rowPhase8+row_adj, pady=5)
    label4_h1_8.grid(column=16,row=rowPhase8+row_adj, pady=5)
    spin4_B_8.grid(column=17,row=rowPhase8+row_adj, pady=5)
    label4_m1_8.grid(column=18,row=rowPhase8+row_adj, pady=5)
    lbl4_B_8.grid(column=19, row=rowPhase8+row_adj, pady=5)
    spin4_C_8.grid(column=20,row=rowPhase8+row_adj, pady=5)
    label4_h2_8.grid(column=21,row=rowPhase8+row_adj, pady=5)
    spin4_D_8.grid(column=22,row=rowPhase8+row_adj, pady=5)
    label4_m2_8.grid(column=23,row=rowPhase8+row_adj, pady=5)
    rad4_B_8.grid(column=24, row=rowPhase8+row_adj, padx=15, pady=5)
    rad4_C_8.grid(column=25, row=rowPhase8+row_adj, pady=5)

    # phase 9
    phaseLabel4_9 = Label(tab4, text='Phase 9')
    fromLabel4_9 = Label(tab4, text='From:')
    space4_9 = Label(tab4, text=' ')
    space4_9_2 = Label(tab4, text=' ')
    spin4_E_9 = Spinbox(tab4, from_=00, to=24, width=3, format='%02.0f')
    spin4_F_9 = Spinbox(tab4, from_=00, to=59, width=3, format='%02.0f')
    spin4_E_9.delete(0,'end')
    spin4_E_9.insert(0,'07')
    spin4_F_9.delete(0,'end')
    spin4_F_9.insert(0,'00')
    label4_h0_9 = Label(tab4, text=':')
    label4_m0_9 = Label(tab4, text='')
    date4_9_entry = Spinbox(tab4, from_=00, to=31, width=3, format='%02.0f')
    month4_9_entry = Spinbox(tab4, from_=00, to=12, width=3, format='%02.0f')
    year4_9_entry = Spinbox(tab4, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase9 = day_phase8 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date4_9_entry.delete(0,'end')
    date4_9_entry.insert(0,'{:02d}'.format(day_phase9.day))
    month4_9_entry.delete(0,'end')
    month4_9_entry.insert(0,'{:02d}'.format(day_phase9.month))
    year4_9_entry.delete(0,'end')
    year4_9_entry.insert(0,day_phase9.year)
    label4_d_9 = Label(tab4, text= '/')
    label4_m_9 = Label(tab4, text= '/')
    rad4_A_9 = Radiobutton(tab4, text='LD', variable=var4_9, value=1)
    lbl4_A_9 = Label(tab4, text= 'On:')
    spin4_A_9 = Spinbox(tab4, from_=00, to=24, width=3, format='%02.0f')
    spin4_B_9 = Spinbox(tab4, from_=00, to=59, width=3, format='%02.0f')
    spin4_A_9.delete(0,'end')
    spin4_A_9.insert(0,'07')
    spin4_B_9.delete(0,'end')
    spin4_B_9.insert(0,'00')
    label4_h1_9 = Label(tab4, text=':')
    label4_m1_9 = Label(tab4, text='')
    lbl4_B_9 = Label(tab4, text= 'Off:')
    spin4_C_9 = Spinbox(tab4, from_=00, to=24, width=3, format='%02.0f')
    spin4_D_9 = Spinbox(tab4, from_=00, to=59, width=3, format='%02.0f')
    spin4_C_9.delete(0,'end')
    spin4_C_9.insert(0,'19')
    spin4_D_9.delete(0,'end')
    spin4_D_9.insert(0,'00')
    label4_h2_9 = Label(tab4, text=':')
    label4_m2_9 = Label(tab4, text='')
    rad4_B_9 = Radiobutton(tab4, text='DD', variable=var4_9, value=2)
    rad4_C_9 = Radiobutton(tab4, text='LL', variable=var4_9, value=3)
    
    
    phaseLabel4_9.grid(column=0, row=rowPhase9+row_adj, padx=15, pady=5)
    fromLabel4_9.grid(column=1,row=rowPhase9+row_adj)
    spin4_E_9.grid(column=2,row=rowPhase9+row_adj)
    label4_h0_9.grid(column=3,row=rowPhase9+row_adj)
    spin4_F_9.grid(column=4,row=rowPhase9+row_adj)
    label4_m0_9.grid(column=5,row=rowPhase9+row_adj)
    space4_9.grid(column=7,row=rowPhase9+row_adj)
    date4_9_entry.grid(column=11, row=rowPhase9+row_adj)
    label4_d_9.grid(column=8,row=rowPhase9+row_adj)
    month4_9_entry.grid(column=9, row=rowPhase9+row_adj)
    label4_m_9.grid(column=10,row=rowPhase9+row_adj)
    year4_9_entry.grid(column=7, row=rowPhase9+row_adj) # ISO format
    space4_9_2.grid(column=12,row=rowPhase9+row_adj,padx=5)
    rad4_A_9.grid(column=13, row=rowPhase9+row_adj, pady=5)
    lbl4_A_9.grid(column=14, row=rowPhase9+row_adj, pady=5)
    spin4_A_9.grid(column=15,row=rowPhase9+row_adj, pady=5)
    label4_h1_9.grid(column=16,row=rowPhase9+row_adj, pady=5)
    spin4_B_9.grid(column=17,row=rowPhase9+row_adj, pady=5)
    label4_m1_9.grid(column=18,row=rowPhase9+row_adj, pady=5)
    lbl4_B_9.grid(column=19, row=rowPhase9+row_adj, pady=5)
    spin4_C_9.grid(column=20,row=rowPhase9+row_adj, pady=5)
    label4_h2_9.grid(column=21,row=rowPhase9+row_adj, pady=5)
    spin4_D_9.grid(column=22,row=rowPhase9+row_adj, pady=5)
    label4_m2_9.grid(column=23,row=rowPhase9+row_adj, pady=5)
    rad4_B_9.grid(column=24, row=rowPhase9+row_adj, padx=15, pady=5)
    rad4_C_9.grid(column=25, row=rowPhase9+row_adj, pady=5)

    # phase 10
    phaseLabel4_10 = Label(tab4, text='Phase 10')
    fromLabel4_10 = Label(tab4, text='From:')
    space4_10 = Label(tab4, text=' ')
    space4_10_2 = Label(tab4, text=' ')
    spin4_E_10 = Spinbox(tab4, from_=00, to=24, width=3, format='%02.0f')
    spin4_F_10 = Spinbox(tab4, from_=00, to=59, width=3, format='%02.0f')
    spin4_E_10.delete(0,'end')
    spin4_E_10.insert(0,'07')
    spin4_F_10.delete(0,'end')
    spin4_F_10.insert(0,'00')
    label4_h0_10 = Label(tab4, text=':')
    label4_m0_10 = Label(tab4, text='')
    date4_10_entry = Spinbox(tab4, from_=00, to=31, width=3, format='%02.0f')
    month4_10_entry = Spinbox(tab4, from_=00, to=12, width=3, format='%02.0f')
    year4_10_entry = Spinbox(tab4, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase10 = day_phase9 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date4_10_entry.delete(0,'end')
    date4_10_entry.insert(0,'{:02d}'.format(day_phase10.day))
    month4_10_entry.delete(0,'end')
    month4_10_entry.insert(0,'{:02d}'.format(day_phase10.month))
    year4_10_entry.delete(0,'end')
    year4_10_entry.insert(0,day_phase10.year)
    label4_d_10 = Label(tab4, text= '/')
    label4_m_10 = Label(tab4, text= '/')
    rad4_A_10 = Radiobutton(tab4, text='LD', variable=var4_10, value=1)
    lbl4_A_10 = Label(tab4, text= 'On:')
    spin4_A_10 = Spinbox(tab4, from_=00, to=24, width=3, format='%02.0f')
    spin4_B_10 = Spinbox(tab4, from_=00, to=59, width=3, format='%02.0f')
    spin4_A_10.delete(0,'end')
    spin4_A_10.insert(0,'07')
    spin4_B_10.delete(0,'end')
    spin4_B_10.insert(0,'00')
    label4_h1_10 = Label(tab4, text=':')
    label4_m1_10 = Label(tab4, text='')
    lbl4_B_10 = Label(tab4, text= 'Off:')
    spin4_C_10 = Spinbox(tab4, from_=00, to=24, width=3, format='%02.0f')
    spin4_D_10 = Spinbox(tab4, from_=00, to=59, width=3, format='%02.0f')
    spin4_C_10.delete(0,'end')
    spin4_C_10.insert(0,'19')
    spin4_D_10.delete(0,'end')
    spin4_D_10.insert(0,'00')
    label4_h2_10 = Label(tab4, text=':')
    label4_m2_10 = Label(tab4, text='')
    rad4_B_10 = Radiobutton(tab4, text='DD', variable=var4_10, value=2)
    rad4_C_10 = Radiobutton(tab4, text='LL', variable=var4_10, value=3)
    
    
    phaseLabel4_10.grid(column=0, row=rowPhase10+row_adj, padx=15, pady=5)
    fromLabel4_10.grid(column=1,row=rowPhase10+row_adj)
    spin4_E_10.grid(column=2,row=rowPhase10+row_adj)
    label4_h0_10.grid(column=3,row=rowPhase10+row_adj)
    spin4_F_10.grid(column=4,row=rowPhase10+row_adj)
    label4_m0_10.grid(column=5,row=rowPhase10+row_adj)
    space4_10.grid(column=7,row=rowPhase10+row_adj)
    date4_10_entry.grid(column=11, row=rowPhase10+row_adj)
    label4_d_10.grid(column=8,row=rowPhase10+row_adj)
    month4_10_entry.grid(column=9, row=rowPhase10+row_adj)
    label4_m_10.grid(column=10,row=rowPhase10+row_adj)
    year4_10_entry.grid(column=7, row=rowPhase10+row_adj) # ISO format
    space4_10_2.grid(column=12,row=rowPhase10+row_adj,padx=5)
    rad4_A_10.grid(column=13, row=rowPhase10+row_adj, pady=5)
    lbl4_A_10.grid(column=14, row=rowPhase10+row_adj, pady=5)
    spin4_A_10.grid(column=15,row=rowPhase10+row_adj, pady=5)
    label4_h1_10.grid(column=16,row=rowPhase10+row_adj, pady=5)
    spin4_B_10.grid(column=17,row=rowPhase10+row_adj, pady=5)
    label4_m1_10.grid(column=18,row=rowPhase10+row_adj, pady=5)
    lbl4_B_10.grid(column=19, row=rowPhase10+row_adj, pady=5)
    spin4_C_10.grid(column=20,row=rowPhase10+row_adj, pady=5)
    label4_h2_10.grid(column=21,row=rowPhase10+row_adj, pady=5)
    spin4_D_10.grid(column=22,row=rowPhase10+row_adj, pady=5)
    label4_m2_10.grid(column=23,row=rowPhase10+row_adj, pady=5)
    rad4_B_10.grid(column=24, row=rowPhase10+row_adj, padx=15, pady=5)
    rad4_C_10.grid(column=25, row=rowPhase10+row_adj, pady=5)

    # phase 11
    phaseLabel4_11 = Label(tab4, text='Phase 11')
    fromLabel4_11 = Label(tab4, text='From:')
    space4_11 = Label(tab4, text=' ')
    space4_11_2 = Label(tab4, text=' ')
    spin4_E_11 = Spinbox(tab4, from_=00, to=24, width=3, format='%02.0f')
    spin4_F_11 = Spinbox(tab4, from_=00, to=59, width=3, format='%02.0f')
    spin4_E_11.delete(0,'end')
    spin4_E_11.insert(0,'07')
    spin4_F_11.delete(0,'end')
    spin4_F_11.insert(0,'00')
    label4_h0_11 = Label(tab4, text=':')
    label4_m0_11 = Label(tab4, text='')
    date4_11_entry = Spinbox(tab4, from_=00, to=31, width=3, format='%02.0f')
    month4_11_entry = Spinbox(tab4, from_=00, to=12, width=3, format='%02.0f')
    year4_11_entry = Spinbox(tab4, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase11 = day_phase10 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date4_11_entry.delete(0,'end')
    date4_11_entry.insert(0,'{:02d}'.format(day_phase11.day))
    month4_11_entry.delete(0,'end')
    month4_11_entry.insert(0,'{:02d}'.format(day_phase11.month))
    year4_11_entry.delete(0,'end')
    year4_11_entry.insert(0,day_phase11.year)
    label4_d_11 = Label(tab4, text= '/')
    label4_m_11 = Label(tab4, text= '/')
    rad4_A_11 = Radiobutton(tab4, text='LD', variable=var4_11, value=1)
    lbl4_A_11 = Label(tab4, text= 'On:')
    spin4_A_11 = Spinbox(tab4, from_=00, to=24, width=3, format='%02.0f')
    spin4_B_11 = Spinbox(tab4, from_=00, to=59, width=3, format='%02.0f')
    spin4_A_11.delete(0,'end')
    spin4_A_11.insert(0,'07')
    spin4_B_11.delete(0,'end')
    spin4_B_11.insert(0,'00')
    label4_h1_11 = Label(tab4, text=':')
    label4_m1_11 = Label(tab4, text='')
    lbl4_B_11 = Label(tab4, text= 'Off:')
    spin4_C_11 = Spinbox(tab4, from_=00, to=24, width=3, format='%02.0f')
    spin4_D_11 = Spinbox(tab4, from_=00, to=59, width=3, format='%02.0f')
    spin4_C_11.delete(0,'end')
    spin4_C_11.insert(0,'19')
    spin4_D_11.delete(0,'end')
    spin4_D_11.insert(0,'00')
    label4_h2_11 = Label(tab4, text=':')
    label4_m2_11 = Label(tab4, text='')
    rad4_B_11 = Radiobutton(tab4, text='DD', variable=var4_11, value=2)
    rad4_C_11 = Radiobutton(tab4, text='LL', variable=var4_11, value=3)
    
    
    phaseLabel4_11.grid(column=0, row=rowPhase11+row_adj, padx=15, pady=5)
    fromLabel4_11.grid(column=1,row=rowPhase11+row_adj)
    spin4_E_11.grid(column=2,row=rowPhase11+row_adj)
    label4_h0_11.grid(column=3,row=rowPhase11+row_adj)
    spin4_F_11.grid(column=4,row=rowPhase11+row_adj)
    label4_m0_11.grid(column=5,row=rowPhase11+row_adj)
    space4_11.grid(column=7,row=rowPhase11+row_adj)
    date4_11_entry.grid(column=11, row=rowPhase11+row_adj)
    label4_d_11.grid(column=8,row=rowPhase11+row_adj)
    month4_11_entry.grid(column=9, row=rowPhase11+row_adj)
    label4_m_11.grid(column=10,row=rowPhase11+row_adj)
    year4_11_entry.grid(column=7, row=rowPhase11+row_adj) # ISO format
    space4_11_2.grid(column=12,row=rowPhase11+row_adj,padx=5)
    rad4_A_11.grid(column=13, row=rowPhase11+row_adj, pady=5)
    lbl4_A_11.grid(column=14, row=rowPhase11+row_adj, pady=5)
    spin4_A_11.grid(column=15,row=rowPhase11+row_adj, pady=5)
    label4_h1_11.grid(column=16,row=rowPhase11+row_adj, pady=5)
    spin4_B_11.grid(column=17,row=rowPhase11+row_adj, pady=5)
    label4_m1_11.grid(column=18,row=rowPhase11+row_adj, pady=5)
    lbl4_B_11.grid(column=19, row=rowPhase11+row_adj, pady=5)
    spin4_C_11.grid(column=20,row=rowPhase11+row_adj, pady=5)
    label4_h2_11.grid(column=21,row=rowPhase11+row_adj, pady=5)
    spin4_D_11.grid(column=22,row=rowPhase11+row_adj, pady=5)
    label4_m2_11.grid(column=23,row=rowPhase11+row_adj, pady=5)
    rad4_B_11.grid(column=24, row=rowPhase11+row_adj, padx=15, pady=5)
    rad4_C_11.grid(column=25, row=rowPhase11+row_adj, pady=5)

    # phase 12
    phaseLabel4_12 = Label(tab4, text='Phase 12')
    fromLabel4_12 = Label(tab4, text='From:')
    space4_12 = Label(tab4, text=' ')
    space4_12_2 = Label(tab4, text=' ')
    spin4_E_12 = Spinbox(tab4, from_=00, to=24, width=3, format='%02.0f')
    spin4_F_12 = Spinbox(tab4, from_=00, to=59, width=3, format='%02.0f')
    spin4_E_12.delete(0,'end')
    spin4_E_12.insert(0,'07')
    spin4_F_12.delete(0,'end')
    spin4_F_12.insert(0,'00')
    label4_h0_12 = Label(tab4, text=':')
    label4_m0_12 = Label(tab4, text='')
    date4_12_entry = Spinbox(tab4, from_=00, to=31, width=3, format='%02.0f')
    month4_12_entry = Spinbox(tab4, from_=00, to=12, width=3, format='%02.0f')
    year4_12_entry = Spinbox(tab4, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase12 = day_phase11 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date4_12_entry.delete(0,'end')
    date4_12_entry.insert(0,'{:02d}'.format(day_phase12.day))
    month4_12_entry.delete(0,'end')
    month4_12_entry.insert(0,'{:02d}'.format(day_phase12.month))
    year4_12_entry.delete(0,'end')
    year4_12_entry.insert(0,day_phase12.year)
    label4_d_12 = Label(tab4, text= '/')
    label4_m_12 = Label(tab4, text= '/')
    rad4_A_12 = Radiobutton(tab4, text='LD', variable=var4_12, value=1)
    lbl4_A_12 = Label(tab4, text= 'On:')
    spin4_A_12 = Spinbox(tab4, from_=00, to=24, width=3, format='%02.0f')
    spin4_B_12 = Spinbox(tab4, from_=00, to=59, width=3, format='%02.0f')
    spin4_A_12.delete(0,'end')
    spin4_A_12.insert(0,'07')
    spin4_B_12.delete(0,'end')
    spin4_B_12.insert(0,'00')
    label4_h1_12 = Label(tab4, text=':')
    label4_m1_12 = Label(tab4, text='')
    lbl4_B_12 = Label(tab4, text= 'Off:')
    spin4_C_12 = Spinbox(tab4, from_=00, to=24, width=3, format='%02.0f')
    spin4_D_12 = Spinbox(tab4, from_=00, to=59, width=3, format='%02.0f')
    spin4_C_12.delete(0,'end')
    spin4_C_12.insert(0,'19')
    spin4_D_12.delete(0,'end')
    spin4_D_12.insert(0,'00')
    label4_h2_12 = Label(tab4, text=':')
    label4_m2_12 = Label(tab4, text='')
    rad4_B_12 = Radiobutton(tab4, text='DD', variable=var4_12, value=2)
    rad4_C_12 = Radiobutton(tab4, text='LL', variable=var4_12, value=3)
    
    
    phaseLabel4_12.grid(column=0, row=rowPhase12+row_adj, padx=15, pady=5)
    fromLabel4_12.grid(column=1,row=rowPhase12+row_adj)
    spin4_E_12.grid(column=2,row=rowPhase12+row_adj)
    label4_h0_12.grid(column=3,row=rowPhase12+row_adj)
    spin4_F_12.grid(column=4,row=rowPhase12+row_adj)
    label4_m0_12.grid(column=5,row=rowPhase12+row_adj)
    space4_12.grid(column=7,row=rowPhase12+row_adj)
    date4_12_entry.grid(column=11, row=rowPhase12+row_adj)
    label4_d_12.grid(column=8,row=rowPhase12+row_adj)
    month4_12_entry.grid(column=9, row=rowPhase12+row_adj)
    label4_m_12.grid(column=10,row=rowPhase12+row_adj)
    year4_12_entry.grid(column=7, row=rowPhase12+row_adj) # ISO format
    space4_12_2.grid(column=12,row=rowPhase12+row_adj,padx=5)
    rad4_A_12.grid(column=13, row=rowPhase12+row_adj, pady=5)
    lbl4_A_12.grid(column=14, row=rowPhase12+row_adj, pady=5)
    spin4_A_12.grid(column=15,row=rowPhase12+row_adj, pady=5)
    label4_h1_12.grid(column=16,row=rowPhase12+row_adj, pady=5)
    spin4_B_12.grid(column=17,row=rowPhase12+row_adj, pady=5)
    label4_m1_12.grid(column=18,row=rowPhase12+row_adj, pady=5)
    lbl4_B_12.grid(column=19, row=rowPhase12+row_adj, pady=5)
    spin4_C_12.grid(column=20,row=rowPhase12+row_adj, pady=5)
    label4_h2_12.grid(column=21,row=rowPhase12+row_adj, pady=5)
    spin4_D_12.grid(column=22,row=rowPhase12+row_adj, pady=5)
    label4_m2_12.grid(column=23,row=rowPhase12+row_adj, pady=5)
    rad4_B_12.grid(column=24, row=rowPhase12+row_adj, padx=15, pady=5)
    rad4_C_12.grid(column=25, row=rowPhase12+row_adj, pady=5)

    
    

    # Box5 main

    tcyclelabel5 = Label(tab5, text='T-cycle length')
    tcyclelabel5.grid(column=26, row=1, padx=3, pady=5)

    for i in range(0,12): 
        tcyclelength = Spinbox(tab5, from_=12, to=48, width=3)
        tcyclelength.grid(column=26, row=2+i+row_adj, padx=3,pady=5)
        tcyclelength.delete(0,'end')
        tcyclelength.insert(0,24)
        tcyclespinbox_arr[4,i] = tcyclelength
        
    tcyclespinbox_arr[4,0].grid(column=26, row=1+row_adj, pady=5)
        
    
    tab5_title = Label(tab5, text= 'LED schedule', anchor='center')
    tab5_title.grid(column=12, row= 1, columnspan='27', sticky='we')
    # capSep5 = ttk.Separator(tab5, orient=HORIZONTAL)
    # capSep5.grid(column=0, row = row_adj+5, columnspan='27', sticky='we')
    box5sched_text=StringVar()
    box5sched_text.set('Schedule not set.')
    box5sched_stat=Label(tab5, textvariable=box5sched_text, anchor=W, justify=LEFT)
        # phase 1
    phaseLabel5_1 = Label(tab5, text='Phase 1')
    dateLabel = time.strftime('%H:%M   %Y/%m/%d') # reads time for Phase 1 start-time
    fromLabel5_1 = Label(tab5, text='From:')
    date_label5 = Label(tab5, text=dateLabel)
    rad5_A_1 = Radiobutton(tab5, text='LD', variable=var5_1, value=1)
    lbl5_A_1 = Label(tab5, text= 'On:')
    spin5_A_1 = Spinbox(tab5, from_=00, to=24, width=3, format='%02.0f')
    spin5_B_1 = Spinbox(tab5, from_=00, to=59, width=3, format='%02.0f')
    spin5_A_1.delete(0,'end')
    spin5_A_1.insert(0,'07')
    spin5_B_1.delete(0,'end')
    spin5_B_1.insert(0,'00')
    label5_h1_1 = Label(tab5, text=':')
    label5_m1_1 = Label(tab5, text='')
    lbl5_B_1 = Label(tab5, text= 'Off:')
    spin5_C_1 = Spinbox(tab5, from_=00, to=24, width=3, format='%02.0f')
    spin5_D_1 = Spinbox(tab5, from_=00, to=59, width=3, format='%02.0f')
    spin5_C_1.delete(0,'end')
    spin5_C_1.insert(0,'19')
    spin5_D_1.delete(0,'end')
    spin5_D_1.insert(0,'00')
    label5_h2_1 = Label(tab5, text=':')
    label5_m2_1 = Label(tab5, text='')
    rad5_B_1 = Radiobutton(tab5, text='DD', variable=var5_1, value=2)
    rad5_C_1 = Radiobutton(tab5, text='LL', variable=var5_1, value=3)
    phaseLabel5_1.grid(column=0, row=1+row_adj, padx=15, pady=5)
    fromLabel5_1.grid(column=1,row=1+row_adj)
    date_label5.grid(column=2, row=1+row_adj, columnspan='10', sticky='w')
    rad5_A_1.grid(column=13, row=1+row_adj, pady=5)
    lbl5_A_1.grid(column=14, row=1+row_adj, pady=5)
    spin5_A_1.grid(column=15,row=1+row_adj, pady=5)
    label5_h1_1.grid(column=16,row=1+row_adj, pady=5, sticky='w')
    spin5_B_1.grid(column=17,row=1+row_adj, pady=5)
    label5_m1_1.grid(column=18,row=1+row_adj, pady=5, sticky='w')
    lbl5_B_1.grid(column=19, row=1+row_adj, pady=5)
    spin5_C_1.grid(column=20,row=1+row_adj, pady=5)
    label5_h2_1.grid(column=21,row=1+row_adj, pady=5, sticky='w')
    spin5_D_1.grid(column=22,row=1+row_adj, pady=5)
    label5_m2_1.grid(column=23,row=1+row_adj, pady=5, sticky='w')
    rad5_B_1.grid(column=24, row=1+row_adj, padx=15, pady=5)
    rad5_C_1.grid(column=25, row=1+row_adj, pady=5)
        # phase 2
    phaseLabel5_2 = Label(tab5, text='Phase 2')
    fromLabel5_2 = Label(tab5, text='From:')
    space5_2 = Label(tab5, text=' ')
    space5_2_2 = Label(tab5, text=' ')
    spin5_E_2 = Spinbox(tab5, from_=00, to=24, width=3, format='%02.0f')
    spin5_F_2 = Spinbox(tab5, from_=00, to=59, width=3, format='%02.0f')
    spin5_E_2.delete(0,'end')
    spin5_E_2.insert(0,'07')
    spin5_F_2.delete(0,'end')
    spin5_F_2.insert(0,'00')
    label5_h0_2 = Label(tab5, text=':')
    label5_m0_2 = Label(tab5, text='')
    date5_2_entry = Spinbox(tab5, from_=00, to=31, width=3, format='%02.0f')
    month5_2_entry = Spinbox(tab5, from_=00, to=12, width=3, format='%02.0f')
    year5_2_entry = Spinbox(tab5, from_=2018, to=2030, width=5)
    date5_2_entry.delete(0,'end')
    today=datetime.date.today() # today
    day_phase2 = today + datetime.timedelta(days=7) # calculate dates for 7 days after recording initiation
    date5_2_entry.insert(0,'{:02d}'.format(day_phase2.day))
    month5_2_entry.delete(0,'end')
    month5_2_entry.insert(0,'{:02d}'.format(day_phase2.month))
    year5_2_entry.delete(0,'end')
    year5_2_entry.insert(0,day_phase2.year) # ISO format is YYYY/MM/DD

    label3_d_0 = Label(tab5, text= 'Month')
    label3_m_0 = Label(tab5, text= 'Date')
    label3_m_0.grid(column=11,row=2+row_adj)
    label3_d_0.grid(column=9,row=2+row_adj)
    label3_d_1 = Label(tab5, text= '/')
    label3_m_1 = Label(tab5, text= '/')
    label3_d_1.grid(column=8,row=2+row_adj)
    label3_m_1.grid(column=10,row=2+row_adj)

    label5_d_2 = Label(tab5, text= '/')
    label5_m_2 = Label(tab5, text= '/')
    rad5_A_2 = Radiobutton(tab5, text='LD', variable=var5_2, value=1)
    lbl5_A_2 = Label(tab5, text= 'On:')
    spin5_A_2 = Spinbox(tab5, from_=00, to=24, width=3, format='%02.0f')
    spin5_B_2 = Spinbox(tab5, from_=00, to=59, width=3, format='%02.0f')
    spin5_A_2.delete(0,'end')
    spin5_A_2.insert(0,'07')
    spin5_B_2.delete(0,'end')
    spin5_B_2.insert(0,'00')
    label5_h1_2 = Label(tab5, text=':')
    label5_m1_2 = Label(tab5, text='')
    lbl5_B_2 = Label(tab5, text= 'Off:')
    spin5_C_2 = Spinbox(tab5, from_=00, to=24, width=3, format='%02.0f')
    spin5_D_2 = Spinbox(tab5, from_=00, to=59, width=3, format='%02.0f')
    spin5_C_2.delete(0,'end')
    spin5_C_2.insert(0,'19')
    spin5_D_2.delete(0,'end')
    spin5_D_2.insert(0,'00')
    label5_h2_2 = Label(tab5, text=':')
    label5_m2_2 = Label(tab5, text='')
    rad5_B_2 = Radiobutton(tab5, text='DD', variable=var5_2, value=2)
    rad5_C_2 = Radiobutton(tab5, text='LL', variable=var5_2, value=3)
    phaseLabel5_2.grid(column=0, row=3+row_adj, padx=15, pady=5)
    fromLabel5_2.grid(column=1,row=3+row_adj)
    spin5_E_2.grid(column=2,row=3+row_adj)
    label5_h0_2.grid(column=3,row=3+row_adj)
    spin5_F_2.grid(column=4,row=3+row_adj)
    label5_m0_2.grid(column=5,row=3+row_adj)
    space5_2.grid(column=6,row=3+row_adj)
    date5_2_entry.grid(column=11, row=3+row_adj)
    label5_d_2.grid(column=8,row=3+row_adj)
    month5_2_entry.grid(column=9, row=3+row_adj)
    label5_m_2.grid(column=10,row=3+row_adj)
    year5_2_entry.grid(column=7, row=3+row_adj) # ISO format
    space5_2_2.grid(column=12,row=3+row_adj,padx=5)
    rad5_A_2.grid(column=13, row=3+row_adj, pady=5)
    lbl5_A_2.grid(column=14, row=3+row_adj, pady=5)
    spin5_A_2.grid(column=15,row=3+row_adj, pady=5)
    label5_h1_2.grid(column=16,row=3+row_adj, pady=5)
    spin5_B_2.grid(column=17,row=3+row_adj, pady=5)
    label5_m1_2.grid(column=18,row=3+row_adj, pady=5)
    lbl5_B_2.grid(column=19, row=3+row_adj, pady=5)
    spin5_C_2.grid(column=20,row=3+row_adj, pady=5)
    label5_h2_2.grid(column=21,row=3+row_adj, pady=5)
    spin5_D_2.grid(column=22,row=3+row_adj, pady=5)
    label5_m2_2.grid(column=23,row=3+row_adj, pady=5)
    rad5_B_2.grid(column=24, row=3+row_adj, padx=15, pady=5)
    rad5_C_2.grid(column=25, row=3+row_adj, pady=5)

        # phase 3
    phaseLabel5_3 = Label(tab5, text='Phase 3')
    fromLabel5_3 = Label(tab5, text='From:')
    space5_3 = Label(tab5, text=' ')
    spin5_E_3 = Spinbox(tab5, from_=00, to=24, width=3, format='%02.0f')
    spin5_F_3 = Spinbox(tab5, from_=00, to=59, width=3, format='%02.0f')
    spin5_E_3.delete(0,'end')
    spin5_E_3.insert(0,'07')
    spin5_F_3.delete(0,'end')
    spin5_F_3.insert(0,'00')
    label5_h0_3 = Label(tab5, text=':')
    label5_m0_3 = Label(tab5, text='')
    date5_3_entry = Spinbox(tab5, from_=00, to=31, width=3, format='%02.0f')
    month5_3_entry = Spinbox(tab5, from_=00, to=12, width=3, format='%02.0f')
    year5_3_entry = Spinbox(tab5, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase3 = day_phase2 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date5_3_entry.delete(0,'end')
    date5_3_entry.insert(0,'{:02d}'.format(day_phase3.day))
    month5_3_entry.delete(0,'end')
    month5_3_entry.insert(0,'{:02d}'.format(day_phase3.month))
    year5_3_entry.delete(0,'end')
    year5_3_entry.insert(0,day_phase3.year)
    label5_d_3 = Label(tab5, text= '/')
    label5_m_3 = Label(tab5, text= '/')
    rad5_A_3 = Radiobutton(tab5, text='LD', variable=var5_3, value=1)
    lbl5_A_3 = Label(tab5, text= 'On:')
    spin5_A_3 = Spinbox(tab5, from_=00, to=24, width=3, format='%02.0f')
    spin5_B_3 = Spinbox(tab5, from_=00, to=59, width=3, format='%02.0f')
    spin5_A_3.delete(0,'end')
    spin5_A_3.insert(0,'07')
    spin5_B_3.delete(0,'end')
    spin5_B_3.insert(0,'00')
    label5_h1_3 = Label(tab5, text=':')
    label5_m1_3 = Label(tab5, text='')
    lbl5_B_3 = Label(tab5, text= 'Off:')
    spin5_C_3 = Spinbox(tab5, from_=00, to=24, width=3, format='%02.0f')
    spin5_D_3 = Spinbox(tab5, from_=00, to=59, width=3, format='%02.0f')
    spin5_C_3.delete(0,'end')
    spin5_C_3.insert(0,'19')
    spin5_D_3.delete(0,'end')
    spin5_D_3.insert(0,'00')
    label5_h2_3 = Label(tab5, text=':')
    label5_m2_3 = Label(tab5, text='')
    rad5_B_3 = Radiobutton(tab5, text='DD', variable=var5_3, value=2)
    rad5_C_3 = Radiobutton(tab5, text='LL', variable=var5_3, value=3)
    phaseLabel5_3.grid(column=0, row=4+row_adj, padx=15, pady=5)
    fromLabel5_3.grid(column=1,row=4+row_adj)
    spin5_E_3.grid(column=2,row=4+row_adj)
    label5_h0_3.grid(column=3,row=4+row_adj)
    spin5_F_3.grid(column=4,row=4+row_adj)
    label5_m0_3.grid(column=5,row=4+row_adj)
    space5_3.grid(column=6,row=4+row_adj)
    date5_3_entry.grid(column=11, row=4+row_adj)
    label5_d_3.grid(column=8,row=4+row_adj)
    month5_3_entry.grid(column=9, row=4+row_adj)
    label5_m_3.grid(column=10,row=4+row_adj)
    year5_3_entry.grid(column=7, row=4+row_adj) # ISO format
    rad5_A_3.grid(column=13, row=4+row_adj, pady=5)
    lbl5_A_3.grid(column=14, row=4+row_adj, pady=5)
    spin5_A_3.grid(column=15,row=4+row_adj, pady=5)
    label5_h1_3.grid(column=16,row=4+row_adj, pady=5)
    spin5_B_3.grid(column=17,row=4+row_adj, pady=5)
    label5_m1_3.grid(column=18,row=4+row_adj, pady=5)
    lbl5_B_3.grid(column=19, row=4+row_adj, pady=5)
    spin5_C_3.grid(column=20,row=4+row_adj, pady=5)
    label5_h2_3.grid(column=21,row=4+row_adj, pady=5)
    spin5_D_3.grid(column=22,row=4+row_adj, pady=5)
    label5_m2_3.grid(column=23,row=4+row_adj, pady=5)
    rad5_B_3.grid(column=24, row=4+row_adj, padx=15, pady=5)
    rad5_C_3.grid(column=25, row=4+row_adj, pady=5)

        # phase 4
    phaseLabel5_4 = Label(tab5, text='Phase 4')
    fromLabel5_4 = Label(tab5, text='From:')
    space5_4 = Label(tab5, text=' ')
    space5_4_2 = Label(tab5, text=' ')
    spin5_E_4 = Spinbox(tab5, from_=00, to=24, width=3, format='%02.0f')
    spin5_F_4 = Spinbox(tab5, from_=00, to=59, width=3, format='%02.0f')
    spin5_E_4.delete(0,'end')
    spin5_E_4.insert(0,'07')
    spin5_F_4.delete(0,'end')
    spin5_F_4.insert(0,'00')
    label5_h0_4 = Label(tab5, text=':')
    label5_m0_4 = Label(tab5, text='')
    date5_4_entry = Spinbox(tab5, from_=00, to=31, width=3, format='%02.0f')
    month5_4_entry = Spinbox(tab5, from_=00, to=12, width=3, format='%02.0f')
    year5_4_entry = Spinbox(tab5, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase4 = day_phase3 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date5_4_entry.delete(0,'end')
    date5_4_entry.insert(0,'{:02d}'.format(day_phase4.day))
    month5_4_entry.delete(0,'end')
    month5_4_entry.insert(0,'{:02d}'.format(day_phase4.month))
    year5_4_entry.delete(0,'end')
    year5_4_entry.insert(0,day_phase4.year)
    label5_d_4 = Label(tab5, text= '/')
    label5_m_4 = Label(tab5, text= '/')
    rad5_A_4 = Radiobutton(tab5, text='LD', variable=var5_4, value=1)
    lbl5_A_4 = Label(tab5, text= 'On:')
    spin5_A_4 = Spinbox(tab5, from_=00, to=24, width=3, format='%02.0f')
    spin5_B_4 = Spinbox(tab5, from_=00, to=59, width=3, format='%02.0f')
    spin5_A_4.delete(0,'end')
    spin5_A_4.insert(0,'07')
    spin5_B_4.delete(0,'end')
    spin5_B_4.insert(0,'00')
    label5_h1_4 = Label(tab5, text=':')
    label5_m1_4 = Label(tab5, text='')
    lbl5_B_4 = Label(tab5, text= 'Off:')
    spin5_C_4 = Spinbox(tab5, from_=00, to=24, width=3, format='%02.0f')
    spin5_D_4 = Spinbox(tab5, from_=00, to=59, width=3, format='%02.0f')
    spin5_C_4.delete(0,'end')
    spin5_C_4.insert(0,'19')
    spin5_D_4.delete(0,'end')
    spin5_D_4.insert(0,'00')
    label5_h2_4 = Label(tab5, text=':')
    label5_m2_4 = Label(tab5, text='')
    rad5_B_4 = Radiobutton(tab5, text='DD', variable=var5_4, value=2)
    rad5_C_4 = Radiobutton(tab5, text='LL', variable=var5_4, value=3)
    phaseLabel5_4.grid(column=0, row=5+row_adj, padx=15, pady=5)
    fromLabel5_4.grid(column=1,row=5+row_adj)
    spin5_E_4.grid(column=2,row=5+row_adj)
    label5_h0_4.grid(column=3,row=5+row_adj)
    spin5_F_4.grid(column=4,row=5+row_adj)
    label5_m0_4.grid(column=5,row=5+row_adj)
    space5_4.grid(column=6,row=5+row_adj)
    date5_4_entry.grid(column=11, row=5+row_adj)
    label5_d_4.grid(column=8,row=5+row_adj)
    month5_4_entry.grid(column=9, row=5+row_adj)
    label5_m_4.grid(column=10,row=5+row_adj)
    year5_4_entry.grid(column=7, row=5+row_adj) # ISO format
    space5_4_2.grid(column=12,row=5+row_adj,padx=5)
    rad5_A_4.grid(column=13, row=5+row_adj, pady=5)
    lbl5_A_4.grid(column=14, row=5+row_adj, pady=5)
    spin5_A_4.grid(column=15,row=5+row_adj, pady=5)
    label5_h1_4.grid(column=16,row=5+row_adj, pady=5)
    spin5_B_4.grid(column=17,row=5+row_adj, pady=5)
    label5_m1_4.grid(column=18,row=5+row_adj, pady=5)
    lbl5_B_4.grid(column=19, row=5+row_adj, pady=5)
    spin5_C_4.grid(column=20,row=5+row_adj, pady=5)
    label5_h2_4.grid(column=21,row=5+row_adj, pady=5)
    spin5_D_4.grid(column=22,row=5+row_adj, pady=5)
    label5_m2_4.grid(column=23,row=5+row_adj, pady=5)
    rad5_B_4.grid(column=24, row=5+row_adj, padx=15, pady=5)
    rad5_C_4.grid(column=25, row=5+row_adj, pady=5)

    # phase 5
    phaseLabel5_5 = Label(tab5, text='Phase 5')
    fromLabel5_5 = Label(tab5, text='From:')
    space5_5 = Label(tab5, text=' ')
    space5_5_2 = Label(tab5, text=' ')
    spin5_E_5 = Spinbox(tab5, from_=00, to=24, width=3, format='%02.0f')
    spin5_F_5 = Spinbox(tab5, from_=00, to=59, width=3, format='%02.0f')
    spin5_E_5.delete(0,'end')
    spin5_E_5.insert(0,'07')
    spin5_F_5.delete(0,'end')
    spin5_F_5.insert(0,'00')
    label5_h0_5 = Label(tab5, text=':')
    label5_m0_5 = Label(tab5, text='')
    date5_5_entry = Spinbox(tab5, from_=00, to=31, width=3, format='%02.0f')
    month5_5_entry = Spinbox(tab5, from_=00, to=12, width=3, format='%02.0f')
    year5_5_entry = Spinbox(tab5, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase5 = day_phase4 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date5_5_entry.delete(0,'end')
    date5_5_entry.insert(0,'{:02d}'.format(day_phase5.day))
    month5_5_entry.delete(0,'end')
    month5_5_entry.insert(0,'{:02d}'.format(day_phase5.month))
    year5_5_entry.delete(0,'end')
    year5_5_entry.insert(0,day_phase5.year)
    label5_d_5 = Label(tab5, text= '/')
    label5_m_5 = Label(tab5, text= '/')
    rad5_A_5 = Radiobutton(tab5, text='LD', variable=var5_5, value=1)
    lbl5_A_5 = Label(tab5, text= 'On:')
    spin5_A_5 = Spinbox(tab5, from_=00, to=24, width=3, format='%02.0f')
    spin5_B_5 = Spinbox(tab5, from_=00, to=59, width=3, format='%02.0f')
    spin5_A_5.delete(0,'end')
    spin5_A_5.insert(0,'07')
    spin5_B_5.delete(0,'end')
    spin5_B_5.insert(0,'00')
    label5_h1_5 = Label(tab5, text=':')
    label5_m1_5 = Label(tab5, text='')
    lbl5_B_5 = Label(tab5, text= 'Off:')
    spin5_C_5 = Spinbox(tab5, from_=00, to=24, width=3, format='%02.0f')
    spin5_D_5 = Spinbox(tab5, from_=00, to=59, width=3, format='%02.0f')
    spin5_C_5.delete(0,'end')
    spin5_C_5.insert(0,'19')
    spin5_D_5.delete(0,'end')
    spin5_D_5.insert(0,'00')
    label5_h2_5 = Label(tab5, text=':')
    label5_m2_5 = Label(tab5, text='')
    rad5_B_5 = Radiobutton(tab5, text='DD', variable=var5_5, value=2)
    rad5_C_5 = Radiobutton(tab5, text='LL', variable=var5_5, value=3)
    phaseLabel5_5.grid(column=0, row=6+row_adj, padx=15, pady=5)
    fromLabel5_5.grid(column=1,row=6+row_adj)
    spin5_E_5.grid(column=2,row=6+row_adj)
    label5_h0_5.grid(column=3,row=6+row_adj)
    spin5_F_5.grid(column=4,row=6+row_adj)
    label5_m0_5.grid(column=5,row=6+row_adj)
    space5_5.grid(column=6,row=6+row_adj)
    date5_5_entry.grid(column=11, row=6+row_adj)
    label5_d_5.grid(column=8,row=6+row_adj)
    month5_5_entry.grid(column=9, row=6+row_adj)
    label5_m_5.grid(column=10,row=6+row_adj)
    year5_5_entry.grid(column=7, row=6+row_adj) # ISO format
    space5_5_2.grid(column=12,row=6+row_adj,padx=5)
    rad5_A_5.grid(column=13, row=6+row_adj, pady=5)
    lbl5_A_5.grid(column=14, row=6+row_adj, pady=5)
    spin5_A_5.grid(column=15,row=6+row_adj, pady=5)
    label5_h1_5.grid(column=16,row=6+row_adj, pady=5)
    spin5_B_5.grid(column=17,row=6+row_adj, pady=5)
    label5_m1_5.grid(column=18,row=6+row_adj, pady=5)
    lbl5_B_5.grid(column=19, row=6+row_adj, pady=5)
    spin5_C_5.grid(column=20,row=6+row_adj, pady=5)
    label5_h2_5.grid(column=21,row=6+row_adj, pady=5)
    spin5_D_5.grid(column=22,row=6+row_adj, pady=5)
    label5_m2_5.grid(column=23,row=6+row_adj, pady=5)
    rad5_B_5.grid(column=24, row=6+row_adj, padx=15, pady=5)
    rad5_C_5.grid(column=25, row=6+row_adj, pady=5)

        # phase 6
    phaseLabel5_6 = Label(tab5, text='Phase 6')
    fromLabel5_6 = Label(tab5, text='From:')
    space5_6 = Label(tab5, text=' ')
    space5_6_2 = Label(tab5, text=' ')
    spin5_E_6 = Spinbox(tab5, from_=00, to=24, width=3, format='%02.0f')
    spin5_F_6 = Spinbox(tab5, from_=00, to=59, width=3, format='%02.0f')
    spin5_E_6.delete(0,'end')
    spin5_E_6.insert(0,'07')
    spin5_F_6.delete(0,'end')
    spin5_F_6.insert(0,'00')
    label5_h0_6 = Label(tab5, text=':')
    label5_m0_6 = Label(tab5, text='')
    date5_6_entry = Spinbox(tab5, from_=00, to=31, width=3, format='%02.0f')
    month5_6_entry = Spinbox(tab5, from_=00, to=12, width=3, format='%02.0f')
    year5_6_entry = Spinbox(tab5, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase6 = day_phase5 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date5_6_entry.delete(0,'end')
    date5_6_entry.insert(0,'{:02d}'.format(day_phase6.day))
    month5_6_entry.delete(0,'end')
    month5_6_entry.insert(0,'{:02d}'.format(day_phase6.month))
    year5_6_entry.delete(0,'end')
    year5_6_entry.insert(0,day_phase6.year)
    label5_d_6 = Label(tab5, text= '/')
    label5_m_6 = Label(tab5, text= '/')
    rad5_A_6 = Radiobutton(tab5, text='LD', variable=var5_6, value=1)
    lbl5_A_6 = Label(tab5, text= 'On:')
    spin5_A_6 = Spinbox(tab5, from_=00, to=24, width=3, format='%02.0f')
    spin5_B_6 = Spinbox(tab5, from_=00, to=59, width=3, format='%02.0f')
    spin5_A_6.delete(0,'end')
    spin5_A_6.insert(0,'07')
    spin5_B_6.delete(0,'end')
    spin5_B_6.insert(0,'00')
    label5_h1_6 = Label(tab5, text=':')
    label5_m1_6 = Label(tab5, text='')
    lbl5_B_6 = Label(tab5, text= 'Off:')
    spin5_C_6 = Spinbox(tab5, from_=00, to=24, width=3, format='%02.0f')
    spin5_D_6 = Spinbox(tab5, from_=00, to=59, width=3, format='%02.0f')
    spin5_C_6.delete(0,'end')
    spin5_C_6.insert(0,'19')
    spin5_D_6.delete(0,'end')
    spin5_D_6.insert(0,'00')
    label5_h2_6 = Label(tab5, text=':')
    label5_m2_6 = Label(tab5, text='')
    rad5_B_6 = Radiobutton(tab5, text='DD', variable=var5_6, value=2)
    rad5_C_6 = Radiobutton(tab5, text='LL', variable=var5_6, value=3)
    
    
    phaseLabel5_6.grid(column=0, row=rowPhase6+row_adj, padx=15, pady=5)
    fromLabel5_6.grid(column=1,row=rowPhase6+row_adj)
    spin5_E_6.grid(column=2,row=rowPhase6+row_adj)
    label5_h0_6.grid(column=3,row=rowPhase6+row_adj)
    spin5_F_6.grid(column=4,row=rowPhase6+row_adj)
    label5_m0_6.grid(column=5,row=rowPhase6+row_adj)
    space5_6.grid(column=6,row=rowPhase6+row_adj)
    date5_6_entry.grid(column=11, row=rowPhase6+row_adj)
    label5_d_6.grid(column=8,row=rowPhase6+row_adj)
    month5_6_entry.grid(column=9, row=rowPhase6+row_adj)
    label5_m_6.grid(column=10,row=rowPhase6+row_adj)
    year5_6_entry.grid(column=7, row=rowPhase6+row_adj) # ISO format
    space5_6_2.grid(column=12,row=rowPhase6+row_adj,padx=5)
    rad5_A_6.grid(column=13, row=rowPhase6+row_adj, pady=5)
    lbl5_A_6.grid(column=14, row=rowPhase6+row_adj, pady=5)
    spin5_A_6.grid(column=15,row=rowPhase6+row_adj, pady=5)
    label5_h1_6.grid(column=16,row=rowPhase6+row_adj, pady=5)
    spin5_B_6.grid(column=17,row=rowPhase6+row_adj, pady=5)
    label5_m1_6.grid(column=18,row=rowPhase6+row_adj, pady=5)
    lbl5_B_6.grid(column=19, row=rowPhase6+row_adj, pady=5)
    spin5_C_6.grid(column=20,row=rowPhase6+row_adj, pady=5)
    label5_h2_6.grid(column=21,row=rowPhase6+row_adj, pady=5)
    spin5_D_6.grid(column=22,row=rowPhase6+row_adj, pady=5)
    label5_m2_6.grid(column=23,row=rowPhase6+row_adj, pady=5)
    rad5_B_6.grid(column=24, row=rowPhase6+row_adj, padx=15, pady=5)
    rad5_C_6.grid(column=25, row=rowPhase6+row_adj, pady=5)

        # phase 7
    phaseLabel5_7 = Label(tab5, text='Phase 7')
    fromLabel5_7 = Label(tab5, text='From:')
    space5_7 = Label(tab5, text=' ')
    space5_7_2 = Label(tab5, text=' ')
    spin5_E_7 = Spinbox(tab5, from_=00, to=24, width=3, format='%02.0f')
    spin5_F_7 = Spinbox(tab5, from_=00, to=59, width=3, format='%02.0f')
    spin5_E_7.delete(0,'end')
    spin5_E_7.insert(0,'07')
    spin5_F_7.delete(0,'end')
    spin5_F_7.insert(0,'00')
    label5_h0_7 = Label(tab5, text=':')
    label5_m0_7 = Label(tab5, text='')
    date5_7_entry = Spinbox(tab5, from_=00, to=31, width=3, format='%02.0f')
    month5_7_entry = Spinbox(tab5, from_=00, to=12, width=3, format='%02.0f')
    year5_7_entry = Spinbox(tab5, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase7 = day_phase6 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date5_7_entry.delete(0,'end')
    date5_7_entry.insert(0,'{:02d}'.format(day_phase7.day))
    month5_7_entry.delete(0,'end')
    month5_7_entry.insert(0,'{:02d}'.format(day_phase7.month))
    year5_7_entry.delete(0,'end')
    year5_7_entry.insert(0,day_phase7.year)
    label5_d_7 = Label(tab5, text= '/')
    label5_m_7 = Label(tab5, text= '/')
    rad5_A_7 = Radiobutton(tab5, text='LD', variable=var5_7, value=1)
    lbl5_A_7 = Label(tab5, text= 'On:')
    spin5_A_7 = Spinbox(tab5, from_=00, to=24, width=3, format='%02.0f')
    spin5_B_7 = Spinbox(tab5, from_=00, to=59, width=3, format='%02.0f')
    spin5_A_7.delete(0,'end')
    spin5_A_7.insert(0,'07')
    spin5_B_7.delete(0,'end')
    spin5_B_7.insert(0,'00')
    label5_h1_7 = Label(tab5, text=':')
    label5_m1_7 = Label(tab5, text='')
    lbl5_B_7 = Label(tab5, text= 'Off:')
    spin5_C_7 = Spinbox(tab5, from_=00, to=24, width=3, format='%02.0f')
    spin5_D_7 = Spinbox(tab5, from_=00, to=59, width=3, format='%02.0f')
    spin5_C_7.delete(0,'end')
    spin5_C_7.insert(0,'19')
    spin5_D_7.delete(0,'end')
    spin5_D_7.insert(0,'00')
    label5_h2_7 = Label(tab5, text=':')
    label5_m2_7 = Label(tab5, text='')
    rad5_B_7 = Radiobutton(tab5, text='DD', variable=var5_7, value=2)
    rad5_C_7 = Radiobutton(tab5, text='LL', variable=var5_7, value=3)
    
    
    phaseLabel5_7.grid(column=0, row=rowPhase7+row_adj, padx=15, pady=5)
    fromLabel5_7.grid(column=1,row=rowPhase7+row_adj)
    spin5_E_7.grid(column=2,row=rowPhase7+row_adj)
    label5_h0_7.grid(column=3,row=rowPhase7+row_adj)
    spin5_F_7.grid(column=4,row=rowPhase7+row_adj)
    label5_m0_7.grid(column=5,row=rowPhase7+row_adj)
    space5_7.grid(column=7,row=rowPhase7+row_adj)
    date5_7_entry.grid(column=11, row=rowPhase7+row_adj)
    label5_d_7.grid(column=8,row=rowPhase7+row_adj)
    month5_7_entry.grid(column=9, row=rowPhase7+row_adj)
    label5_m_7.grid(column=10,row=rowPhase7+row_adj)
    year5_7_entry.grid(column=7, row=rowPhase7+row_adj) # ISO format
    space5_7_2.grid(column=12,row=rowPhase7+row_adj,padx=5)
    rad5_A_7.grid(column=13, row=rowPhase7+row_adj, pady=5)
    lbl5_A_7.grid(column=14, row=rowPhase7+row_adj, pady=5)
    spin5_A_7.grid(column=15,row=rowPhase7+row_adj, pady=5)
    label5_h1_7.grid(column=16,row=rowPhase7+row_adj, pady=5)
    spin5_B_7.grid(column=17,row=rowPhase7+row_adj, pady=5)
    label5_m1_7.grid(column=18,row=rowPhase7+row_adj, pady=5)
    lbl5_B_7.grid(column=19, row=rowPhase7+row_adj, pady=5)
    spin5_C_7.grid(column=20,row=rowPhase7+row_adj, pady=5)
    label5_h2_7.grid(column=21,row=rowPhase7+row_adj, pady=5)
    spin5_D_7.grid(column=22,row=rowPhase7+row_adj, pady=5)
    label5_m2_7.grid(column=23,row=rowPhase7+row_adj, pady=5)
    rad5_B_7.grid(column=24, row=rowPhase7+row_adj, padx=15, pady=5)
    rad5_C_7.grid(column=25, row=rowPhase7+row_adj, pady=5)

    # phase 8
    phaseLabel5_8 = Label(tab5, text='Phase 8')
    fromLabel5_8 = Label(tab5, text='From:')
    space5_8 = Label(tab5, text=' ')
    space5_8_2 = Label(tab5, text=' ')
    spin5_E_8 = Spinbox(tab5, from_=00, to=24, width=3, format='%02.0f')
    spin5_F_8 = Spinbox(tab5, from_=00, to=59, width=3, format='%02.0f')
    spin5_E_8.delete(0,'end')
    spin5_E_8.insert(0,'07')
    spin5_F_8.delete(0,'end')
    spin5_F_8.insert(0,'00')
    label5_h0_8 = Label(tab5, text=':')
    label5_m0_8 = Label(tab5, text='')
    date5_8_entry = Spinbox(tab5, from_=00, to=31, width=3, format='%02.0f')
    month5_8_entry = Spinbox(tab5, from_=00, to=12, width=3, format='%02.0f')
    year5_8_entry = Spinbox(tab5, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase8 = day_phase7 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date5_8_entry.delete(0,'end')
    date5_8_entry.insert(0,'{:02d}'.format(day_phase8.day))
    month5_8_entry.delete(0,'end')
    month5_8_entry.insert(0,'{:02d}'.format(day_phase8.month))
    year5_8_entry.delete(0,'end')
    year5_8_entry.insert(0,day_phase8.year)
    label5_d_8 = Label(tab5, text= '/')
    label5_m_8 = Label(tab5, text= '/')
    rad5_A_8 = Radiobutton(tab5, text='LD', variable=var5_8, value=1)
    lbl5_A_8 = Label(tab5, text= 'On:')
    spin5_A_8 = Spinbox(tab5, from_=00, to=24, width=3, format='%02.0f')
    spin5_B_8 = Spinbox(tab5, from_=00, to=59, width=3, format='%02.0f')
    spin5_A_8.delete(0,'end')
    spin5_A_8.insert(0,'07')
    spin5_B_8.delete(0,'end')
    spin5_B_8.insert(0,'00')
    label5_h1_8 = Label(tab5, text=':')
    label5_m1_8 = Label(tab5, text='')
    lbl5_B_8 = Label(tab5, text= 'Off:')
    spin5_C_8 = Spinbox(tab5, from_=00, to=24, width=3, format='%02.0f')
    spin5_D_8 = Spinbox(tab5, from_=00, to=59, width=3, format='%02.0f')
    spin5_C_8.delete(0,'end')
    spin5_C_8.insert(0,'19')
    spin5_D_8.delete(0,'end')
    spin5_D_8.insert(0,'00')
    label5_h2_8 = Label(tab5, text=':')
    label5_m2_8 = Label(tab5, text='')
    rad5_B_8 = Radiobutton(tab5, text='DD', variable=var5_8, value=2)
    rad5_C_8 = Radiobutton(tab5, text='LL', variable=var5_8, value=3)
    
    
    phaseLabel5_8.grid(column=0, row=rowPhase8+row_adj, padx=15, pady=5)
    fromLabel5_8.grid(column=1,row=rowPhase8+row_adj)
    spin5_E_8.grid(column=2,row=rowPhase8+row_adj)
    label5_h0_8.grid(column=3,row=rowPhase8+row_adj)
    spin5_F_8.grid(column=4,row=rowPhase8+row_adj)
    label5_m0_8.grid(column=5,row=rowPhase8+row_adj)
    space5_8.grid(column=7,row=rowPhase8+row_adj)
    date5_8_entry.grid(column=11, row=rowPhase8+row_adj)
    label5_d_8.grid(column=8,row=rowPhase8+row_adj)
    month5_8_entry.grid(column=9, row=rowPhase8+row_adj)
    label5_m_8.grid(column=10,row=rowPhase8+row_adj)
    year5_8_entry.grid(column=7, row=rowPhase8+row_adj) # ISO format
    space5_8_2.grid(column=12,row=rowPhase8+row_adj,padx=5)
    rad5_A_8.grid(column=13, row=rowPhase8+row_adj, pady=5)
    lbl5_A_8.grid(column=14, row=rowPhase8+row_adj, pady=5)
    spin5_A_8.grid(column=15,row=rowPhase8+row_adj, pady=5)
    label5_h1_8.grid(column=16,row=rowPhase8+row_adj, pady=5)
    spin5_B_8.grid(column=17,row=rowPhase8+row_adj, pady=5)
    label5_m1_8.grid(column=18,row=rowPhase8+row_adj, pady=5)
    lbl5_B_8.grid(column=19, row=rowPhase8+row_adj, pady=5)
    spin5_C_8.grid(column=20,row=rowPhase8+row_adj, pady=5)
    label5_h2_8.grid(column=21,row=rowPhase8+row_adj, pady=5)
    spin5_D_8.grid(column=22,row=rowPhase8+row_adj, pady=5)
    label5_m2_8.grid(column=23,row=rowPhase8+row_adj, pady=5)
    rad5_B_8.grid(column=24, row=rowPhase8+row_adj, padx=15, pady=5)
    rad5_C_8.grid(column=25, row=rowPhase8+row_adj, pady=5)

    # phase 9
    phaseLabel5_9 = Label(tab5, text='Phase 9')
    fromLabel5_9 = Label(tab5, text='From:')
    space5_9 = Label(tab5, text=' ')
    space5_9_2 = Label(tab5, text=' ')
    spin5_E_9 = Spinbox(tab5, from_=00, to=24, width=3, format='%02.0f')
    spin5_F_9 = Spinbox(tab5, from_=00, to=59, width=3, format='%02.0f')
    spin5_E_9.delete(0,'end')
    spin5_E_9.insert(0,'07')
    spin5_F_9.delete(0,'end')
    spin5_F_9.insert(0,'00')
    label5_h0_9 = Label(tab5, text=':')
    label5_m0_9 = Label(tab5, text='')
    date5_9_entry = Spinbox(tab5, from_=00, to=31, width=3, format='%02.0f')
    month5_9_entry = Spinbox(tab5, from_=00, to=12, width=3, format='%02.0f')
    year5_9_entry = Spinbox(tab5, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase9 = day_phase8 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date5_9_entry.delete(0,'end')
    date5_9_entry.insert(0,'{:02d}'.format(day_phase9.day))
    month5_9_entry.delete(0,'end')
    month5_9_entry.insert(0,'{:02d}'.format(day_phase9.month))
    year5_9_entry.delete(0,'end')
    year5_9_entry.insert(0,day_phase9.year)
    label5_d_9 = Label(tab5, text= '/')
    label5_m_9 = Label(tab5, text= '/')
    rad5_A_9 = Radiobutton(tab5, text='LD', variable=var5_9, value=1)
    lbl5_A_9 = Label(tab5, text= 'On:')
    spin5_A_9 = Spinbox(tab5, from_=00, to=24, width=3, format='%02.0f')
    spin5_B_9 = Spinbox(tab5, from_=00, to=59, width=3, format='%02.0f')
    spin5_A_9.delete(0,'end')
    spin5_A_9.insert(0,'07')
    spin5_B_9.delete(0,'end')
    spin5_B_9.insert(0,'00')
    label5_h1_9 = Label(tab5, text=':')
    label5_m1_9 = Label(tab5, text='')
    lbl5_B_9 = Label(tab5, text= 'Off:')
    spin5_C_9 = Spinbox(tab5, from_=00, to=24, width=3, format='%02.0f')
    spin5_D_9 = Spinbox(tab5, from_=00, to=59, width=3, format='%02.0f')
    spin5_C_9.delete(0,'end')
    spin5_C_9.insert(0,'19')
    spin5_D_9.delete(0,'end')
    spin5_D_9.insert(0,'00')
    label5_h2_9 = Label(tab5, text=':')
    label5_m2_9 = Label(tab5, text='')
    rad5_B_9 = Radiobutton(tab5, text='DD', variable=var5_9, value=2)
    rad5_C_9 = Radiobutton(tab5, text='LL', variable=var5_9, value=3)
    
    
    phaseLabel5_9.grid(column=0, row=rowPhase9+row_adj, padx=15, pady=5)
    fromLabel5_9.grid(column=1,row=rowPhase9+row_adj)
    spin5_E_9.grid(column=2,row=rowPhase9+row_adj)
    label5_h0_9.grid(column=3,row=rowPhase9+row_adj)
    spin5_F_9.grid(column=4,row=rowPhase9+row_adj)
    label5_m0_9.grid(column=5,row=rowPhase9+row_adj)
    space5_9.grid(column=7,row=rowPhase9+row_adj)
    date5_9_entry.grid(column=11, row=rowPhase9+row_adj)
    label5_d_9.grid(column=8,row=rowPhase9+row_adj)
    month5_9_entry.grid(column=9, row=rowPhase9+row_adj)
    label5_m_9.grid(column=10,row=rowPhase9+row_adj)
    year5_9_entry.grid(column=7, row=rowPhase9+row_adj) # ISO format
    space5_9_2.grid(column=12,row=rowPhase9+row_adj,padx=5)
    rad5_A_9.grid(column=13, row=rowPhase9+row_adj, pady=5)
    lbl5_A_9.grid(column=14, row=rowPhase9+row_adj, pady=5)
    spin5_A_9.grid(column=15,row=rowPhase9+row_adj, pady=5)
    label5_h1_9.grid(column=16,row=rowPhase9+row_adj, pady=5)
    spin5_B_9.grid(column=17,row=rowPhase9+row_adj, pady=5)
    label5_m1_9.grid(column=18,row=rowPhase9+row_adj, pady=5)
    lbl5_B_9.grid(column=19, row=rowPhase9+row_adj, pady=5)
    spin5_C_9.grid(column=20,row=rowPhase9+row_adj, pady=5)
    label5_h2_9.grid(column=21,row=rowPhase9+row_adj, pady=5)
    spin5_D_9.grid(column=22,row=rowPhase9+row_adj, pady=5)
    label5_m2_9.grid(column=23,row=rowPhase9+row_adj, pady=5)
    rad5_B_9.grid(column=24, row=rowPhase9+row_adj, padx=15, pady=5)
    rad5_C_9.grid(column=25, row=rowPhase9+row_adj, pady=5)

    # phase 10
    phaseLabel5_10 = Label(tab5, text='Phase 10')
    fromLabel5_10 = Label(tab5, text='From:')
    space5_10 = Label(tab5, text=' ')
    space5_10_2 = Label(tab5, text=' ')
    spin5_E_10 = Spinbox(tab5, from_=00, to=24, width=3, format='%02.0f')
    spin5_F_10 = Spinbox(tab5, from_=00, to=59, width=3, format='%02.0f')
    spin5_E_10.delete(0,'end')
    spin5_E_10.insert(0,'07')
    spin5_F_10.delete(0,'end')
    spin5_F_10.insert(0,'00')
    label5_h0_10 = Label(tab5, text=':')
    label5_m0_10 = Label(tab5, text='')
    date5_10_entry = Spinbox(tab5, from_=00, to=31, width=3, format='%02.0f')
    month5_10_entry = Spinbox(tab5, from_=00, to=12, width=3, format='%02.0f')
    year5_10_entry = Spinbox(tab5, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase10 = day_phase9 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date5_10_entry.delete(0,'end')
    date5_10_entry.insert(0,'{:02d}'.format(day_phase10.day))
    month5_10_entry.delete(0,'end')
    month5_10_entry.insert(0,'{:02d}'.format(day_phase10.month))
    year5_10_entry.delete(0,'end')
    year5_10_entry.insert(0,day_phase10.year)
    label5_d_10 = Label(tab5, text= '/')
    label5_m_10 = Label(tab5, text= '/')
    rad5_A_10 = Radiobutton(tab5, text='LD', variable=var5_10, value=1)
    lbl5_A_10 = Label(tab5, text= 'On:')
    spin5_A_10 = Spinbox(tab5, from_=00, to=24, width=3, format='%02.0f')
    spin5_B_10 = Spinbox(tab5, from_=00, to=59, width=3, format='%02.0f')
    spin5_A_10.delete(0,'end')
    spin5_A_10.insert(0,'07')
    spin5_B_10.delete(0,'end')
    spin5_B_10.insert(0,'00')
    label5_h1_10 = Label(tab5, text=':')
    label5_m1_10 = Label(tab5, text='')
    lbl5_B_10 = Label(tab5, text= 'Off:')
    spin5_C_10 = Spinbox(tab5, from_=00, to=24, width=3, format='%02.0f')
    spin5_D_10 = Spinbox(tab5, from_=00, to=59, width=3, format='%02.0f')
    spin5_C_10.delete(0,'end')
    spin5_C_10.insert(0,'19')
    spin5_D_10.delete(0,'end')
    spin5_D_10.insert(0,'00')
    label5_h2_10 = Label(tab5, text=':')
    label5_m2_10 = Label(tab5, text='')
    rad5_B_10 = Radiobutton(tab5, text='DD', variable=var5_10, value=2)
    rad5_C_10 = Radiobutton(tab5, text='LL', variable=var5_10, value=3)
    
    
    phaseLabel5_10.grid(column=0, row=rowPhase10+row_adj, padx=15, pady=5)
    fromLabel5_10.grid(column=1,row=rowPhase10+row_adj)
    spin5_E_10.grid(column=2,row=rowPhase10+row_adj)
    label5_h0_10.grid(column=3,row=rowPhase10+row_adj)
    spin5_F_10.grid(column=4,row=rowPhase10+row_adj)
    label5_m0_10.grid(column=5,row=rowPhase10+row_adj)
    space5_10.grid(column=7,row=rowPhase10+row_adj)
    date5_10_entry.grid(column=11, row=rowPhase10+row_adj)
    label5_d_10.grid(column=8,row=rowPhase10+row_adj)
    month5_10_entry.grid(column=9, row=rowPhase10+row_adj)
    label5_m_10.grid(column=10,row=rowPhase10+row_adj)
    year5_10_entry.grid(column=7, row=rowPhase10+row_adj) # ISO format
    space5_10_2.grid(column=12,row=rowPhase10+row_adj,padx=5)
    rad5_A_10.grid(column=13, row=rowPhase10+row_adj, pady=5)
    lbl5_A_10.grid(column=14, row=rowPhase10+row_adj, pady=5)
    spin5_A_10.grid(column=15,row=rowPhase10+row_adj, pady=5)
    label5_h1_10.grid(column=16,row=rowPhase10+row_adj, pady=5)
    spin5_B_10.grid(column=17,row=rowPhase10+row_adj, pady=5)
    label5_m1_10.grid(column=18,row=rowPhase10+row_adj, pady=5)
    lbl5_B_10.grid(column=19, row=rowPhase10+row_adj, pady=5)
    spin5_C_10.grid(column=20,row=rowPhase10+row_adj, pady=5)
    label5_h2_10.grid(column=21,row=rowPhase10+row_adj, pady=5)
    spin5_D_10.grid(column=22,row=rowPhase10+row_adj, pady=5)
    label5_m2_10.grid(column=23,row=rowPhase10+row_adj, pady=5)
    rad5_B_10.grid(column=24, row=rowPhase10+row_adj, padx=15, pady=5)
    rad5_C_10.grid(column=25, row=rowPhase10+row_adj, pady=5)

    # phase 11
    phaseLabel5_11 = Label(tab5, text='Phase 11')
    fromLabel5_11 = Label(tab5, text='From:')
    space5_11 = Label(tab5, text=' ')
    space5_11_2 = Label(tab5, text=' ')
    spin5_E_11 = Spinbox(tab5, from_=00, to=24, width=3, format='%02.0f')
    spin5_F_11 = Spinbox(tab5, from_=00, to=59, width=3, format='%02.0f')
    spin5_E_11.delete(0,'end')
    spin5_E_11.insert(0,'07')
    spin5_F_11.delete(0,'end')
    spin5_F_11.insert(0,'00')
    label5_h0_11 = Label(tab5, text=':')
    label5_m0_11 = Label(tab5, text='')
    date5_11_entry = Spinbox(tab5, from_=00, to=31, width=3, format='%02.0f')
    month5_11_entry = Spinbox(tab5, from_=00, to=12, width=3, format='%02.0f')
    year5_11_entry = Spinbox(tab5, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase11 = day_phase10 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date5_11_entry.delete(0,'end')
    date5_11_entry.insert(0,'{:02d}'.format(day_phase11.day))
    month5_11_entry.delete(0,'end')
    month5_11_entry.insert(0,'{:02d}'.format(day_phase11.month))
    year5_11_entry.delete(0,'end')
    year5_11_entry.insert(0,day_phase11.year)
    label5_d_11 = Label(tab5, text= '/')
    label5_m_11 = Label(tab5, text= '/')
    rad5_A_11 = Radiobutton(tab5, text='LD', variable=var5_11, value=1)
    lbl5_A_11 = Label(tab5, text= 'On:')
    spin5_A_11 = Spinbox(tab5, from_=00, to=24, width=3, format='%02.0f')
    spin5_B_11 = Spinbox(tab5, from_=00, to=59, width=3, format='%02.0f')
    spin5_A_11.delete(0,'end')
    spin5_A_11.insert(0,'07')
    spin5_B_11.delete(0,'end')
    spin5_B_11.insert(0,'00')
    label5_h1_11 = Label(tab5, text=':')
    label5_m1_11 = Label(tab5, text='')
    lbl5_B_11 = Label(tab5, text= 'Off:')
    spin5_C_11 = Spinbox(tab5, from_=00, to=24, width=3, format='%02.0f')
    spin5_D_11 = Spinbox(tab5, from_=00, to=59, width=3, format='%02.0f')
    spin5_C_11.delete(0,'end')
    spin5_C_11.insert(0,'19')
    spin5_D_11.delete(0,'end')
    spin5_D_11.insert(0,'00')
    label5_h2_11 = Label(tab5, text=':')
    label5_m2_11 = Label(tab5, text='')
    rad5_B_11 = Radiobutton(tab5, text='DD', variable=var5_11, value=2)
    rad5_C_11 = Radiobutton(tab5, text='LL', variable=var5_11, value=3)
    
    
    phaseLabel5_11.grid(column=0, row=rowPhase11+row_adj, padx=15, pady=5)
    fromLabel5_11.grid(column=1,row=rowPhase11+row_adj)
    spin5_E_11.grid(column=2,row=rowPhase11+row_adj)
    label5_h0_11.grid(column=3,row=rowPhase11+row_adj)
    spin5_F_11.grid(column=4,row=rowPhase11+row_adj)
    label5_m0_11.grid(column=5,row=rowPhase11+row_adj)
    space5_11.grid(column=7,row=rowPhase11+row_adj)
    date5_11_entry.grid(column=11, row=rowPhase11+row_adj)
    label5_d_11.grid(column=8,row=rowPhase11+row_adj)
    month5_11_entry.grid(column=9, row=rowPhase11+row_adj)
    label5_m_11.grid(column=10,row=rowPhase11+row_adj)
    year5_11_entry.grid(column=7, row=rowPhase11+row_adj) # ISO format
    space5_11_2.grid(column=12,row=rowPhase11+row_adj,padx=5)
    rad5_A_11.grid(column=13, row=rowPhase11+row_adj, pady=5)
    lbl5_A_11.grid(column=14, row=rowPhase11+row_adj, pady=5)
    spin5_A_11.grid(column=15,row=rowPhase11+row_adj, pady=5)
    label5_h1_11.grid(column=16,row=rowPhase11+row_adj, pady=5)
    spin5_B_11.grid(column=17,row=rowPhase11+row_adj, pady=5)
    label5_m1_11.grid(column=18,row=rowPhase11+row_adj, pady=5)
    lbl5_B_11.grid(column=19, row=rowPhase11+row_adj, pady=5)
    spin5_C_11.grid(column=20,row=rowPhase11+row_adj, pady=5)
    label5_h2_11.grid(column=21,row=rowPhase11+row_adj, pady=5)
    spin5_D_11.grid(column=22,row=rowPhase11+row_adj, pady=5)
    label5_m2_11.grid(column=23,row=rowPhase11+row_adj, pady=5)
    rad5_B_11.grid(column=24, row=rowPhase11+row_adj, padx=15, pady=5)
    rad5_C_11.grid(column=25, row=rowPhase11+row_adj, pady=5)

    # phase 12
    phaseLabel5_12 = Label(tab5, text='Phase 12')
    fromLabel5_12 = Label(tab5, text='From:')
    space5_12 = Label(tab5, text=' ')
    space5_12_2 = Label(tab5, text=' ')
    spin5_E_12 = Spinbox(tab5, from_=00, to=24, width=3, format='%02.0f')
    spin5_F_12 = Spinbox(tab5, from_=00, to=59, width=3, format='%02.0f')
    spin5_E_12.delete(0,'end')
    spin5_E_12.insert(0,'07')
    spin5_F_12.delete(0,'end')
    spin5_F_12.insert(0,'00')
    label5_h0_12 = Label(tab5, text=':')
    label5_m0_12 = Label(tab5, text='')
    date5_12_entry = Spinbox(tab5, from_=00, to=31, width=3, format='%02.0f')
    month5_12_entry = Spinbox(tab5, from_=00, to=12, width=3, format='%02.0f')
    year5_12_entry = Spinbox(tab5, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase12 = day_phase11 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date5_12_entry.delete(0,'end')
    date5_12_entry.insert(0,'{:02d}'.format(day_phase12.day))
    month5_12_entry.delete(0,'end')
    month5_12_entry.insert(0,'{:02d}'.format(day_phase12.month))
    year5_12_entry.delete(0,'end')
    year5_12_entry.insert(0,day_phase12.year)
    label5_d_12 = Label(tab5, text= '/')
    label5_m_12 = Label(tab5, text= '/')
    rad5_A_12 = Radiobutton(tab5, text='LD', variable=var5_12, value=1)
    lbl5_A_12 = Label(tab5, text= 'On:')
    spin5_A_12 = Spinbox(tab5, from_=00, to=24, width=3, format='%02.0f')
    spin5_B_12 = Spinbox(tab5, from_=00, to=59, width=3, format='%02.0f')
    spin5_A_12.delete(0,'end')
    spin5_A_12.insert(0,'07')
    spin5_B_12.delete(0,'end')
    spin5_B_12.insert(0,'00')
    label5_h1_12 = Label(tab5, text=':')
    label5_m1_12 = Label(tab5, text='')
    lbl5_B_12 = Label(tab5, text= 'Off:')
    spin5_C_12 = Spinbox(tab5, from_=00, to=24, width=3, format='%02.0f')
    spin5_D_12 = Spinbox(tab5, from_=00, to=59, width=3, format='%02.0f')
    spin5_C_12.delete(0,'end')
    spin5_C_12.insert(0,'19')
    spin5_D_12.delete(0,'end')
    spin5_D_12.insert(0,'00')
    label5_h2_12 = Label(tab5, text=':')
    label5_m2_12 = Label(tab5, text='')
    rad5_B_12 = Radiobutton(tab5, text='DD', variable=var5_12, value=2)
    rad5_C_12 = Radiobutton(tab5, text='LL', variable=var5_12, value=3)
    
    
    phaseLabel5_12.grid(column=0, row=rowPhase12+row_adj, padx=15, pady=5)
    fromLabel5_12.grid(column=1,row=rowPhase12+row_adj)
    spin5_E_12.grid(column=2,row=rowPhase12+row_adj)
    label5_h0_12.grid(column=3,row=rowPhase12+row_adj)
    spin5_F_12.grid(column=4,row=rowPhase12+row_adj)
    label5_m0_12.grid(column=5,row=rowPhase12+row_adj)
    space5_12.grid(column=7,row=rowPhase12+row_adj)
    date5_12_entry.grid(column=11, row=rowPhase12+row_adj)
    label5_d_12.grid(column=8,row=rowPhase12+row_adj)
    month5_12_entry.grid(column=9, row=rowPhase12+row_adj)
    label5_m_12.grid(column=10,row=rowPhase12+row_adj)
    year5_12_entry.grid(column=7, row=rowPhase12+row_adj) # ISO format
    space5_12_2.grid(column=12,row=rowPhase12+row_adj,padx=5)
    rad5_A_12.grid(column=13, row=rowPhase12+row_adj, pady=5)
    lbl5_A_12.grid(column=14, row=rowPhase12+row_adj, pady=5)
    spin5_A_12.grid(column=15,row=rowPhase12+row_adj, pady=5)
    label5_h1_12.grid(column=16,row=rowPhase12+row_adj, pady=5)
    spin5_B_12.grid(column=17,row=rowPhase12+row_adj, pady=5)
    label5_m1_12.grid(column=18,row=rowPhase12+row_adj, pady=5)
    lbl5_B_12.grid(column=19, row=rowPhase12+row_adj, pady=5)
    spin5_C_12.grid(column=20,row=rowPhase12+row_adj, pady=5)
    label5_h2_12.grid(column=21,row=rowPhase12+row_adj, pady=5)
    spin5_D_12.grid(column=22,row=rowPhase12+row_adj, pady=5)
    label5_m2_12.grid(column=23,row=rowPhase12+row_adj, pady=5)
    rad5_B_12.grid(column=24, row=rowPhase12+row_adj, padx=15, pady=5)
    rad5_C_12.grid(column=25, row=rowPhase12+row_adj, pady=5)

    # box6 main

    tcyclelabel6 = Label(tab6, text='T-cycle length')
    tcyclelabel6.grid(column=26, row=1, padx=3, pady=5)

    for i in range(0,12): 
        tcyclelength = Spinbox(tab6, from_=12, to=48, width=3)
        tcyclelength.grid(column=26, row=2+i+row_adj, padx=3,pady=5)
        tcyclelength.delete(0,'end')
        tcyclelength.insert(0,24)
        tcyclespinbox_arr[5,i] = tcyclelength
        
    tcyclespinbox_arr[5,0].grid(column=26, row=1+row_adj, pady=5)
        
    
    tab6_title = Label(tab6, text= 'LED schedule', anchor='center')
    tab6_title.grid(column=12, row= 1, columnspan='27', sticky='we')
    # capSep5 = ttk.Separator(tab6, orient=HORIZONTAL)
    # capSep5.grid(column=0, row = row_adj+5, columnspan='27', sticky='we')
    box6sched_text=StringVar()
    box6sched_text.set('Schedule not set.')
    box6sched_stat=Label(tab6, textvariable=box6sched_text, anchor=W, justify=LEFT)
        # phase 1
    phaseLabel6_1 = Label(tab6, text='Phase 1')
    dateLabel = time.strftime('%H:%M   %Y/%m/%d') # reads time for Phase 1 start-time
    fromLabel6_1 = Label(tab6, text='From:')
    date_label6 = Label(tab6, text=dateLabel)
    rad6_A_1 = Radiobutton(tab6, text='LD', variable=var6_1, value=1)
    lbl6_A_1 = Label(tab6, text= 'On:')
    spin6_A_1 = Spinbox(tab6, from_=00, to=24, width=3, format='%02.0f')
    spin6_B_1 = Spinbox(tab6, from_=00, to=59, width=3, format='%02.0f')
    spin6_A_1.delete(0,'end')
    spin6_A_1.insert(0,'07')
    spin6_B_1.delete(0,'end')
    spin6_B_1.insert(0,'00')
    label6_h1_1 = Label(tab6, text=':')
    label6_m1_1 = Label(tab6, text='')
    lbl6_B_1 = Label(tab6, text= 'Off:')
    spin6_C_1 = Spinbox(tab6, from_=00, to=24, width=3, format='%02.0f')
    spin6_D_1 = Spinbox(tab6, from_=00, to=59, width=3, format='%02.0f')
    spin6_C_1.delete(0,'end')
    spin6_C_1.insert(0,'19')
    spin6_D_1.delete(0,'end')
    spin6_D_1.insert(0,'00')
    label6_h2_1 = Label(tab6, text=':')
    label6_m2_1 = Label(tab6, text='')
    rad6_B_1 = Radiobutton(tab6, text='DD', variable=var6_1, value=2)
    rad6_C_1 = Radiobutton(tab6, text='LL', variable=var6_1, value=3)
    phaseLabel6_1.grid(column=0, row=1+row_adj, padx=15, pady=5)
    fromLabel6_1.grid(column=1,row=1+row_adj)
    date_label6.grid(column=2, row=1+row_adj, columnspan='10', sticky='w')
    rad6_A_1.grid(column=13, row=1+row_adj, pady=5)
    lbl6_A_1.grid(column=14, row=1+row_adj, pady=5)
    spin6_A_1.grid(column=15,row=1+row_adj, pady=5)
    label6_h1_1.grid(column=16,row=1+row_adj, pady=5, sticky='w')
    spin6_B_1.grid(column=17,row=1+row_adj, pady=5)
    label6_m1_1.grid(column=18,row=1+row_adj, pady=5, sticky='w')
    lbl6_B_1.grid(column=19, row=1+row_adj, pady=5)
    spin6_C_1.grid(column=20,row=1+row_adj, pady=5)
    label6_h2_1.grid(column=21,row=1+row_adj, pady=5, sticky='w')
    spin6_D_1.grid(column=22,row=1+row_adj, pady=5)
    label6_m2_1.grid(column=23,row=1+row_adj, pady=5, sticky='w')
    rad6_B_1.grid(column=24, row=1+row_adj, padx=15, pady=5)
    rad6_C_1.grid(column=25, row=1+row_adj, pady=5)
        # phase 2
    phaseLabel6_2 = Label(tab6, text='Phase 2')
    fromLabel6_2 = Label(tab6, text='From:')
    space6_2 = Label(tab6, text=' ')
    space6_2_2 = Label(tab6, text=' ')
    spin6_E_2 = Spinbox(tab6, from_=00, to=24, width=3, format='%02.0f')
    spin6_F_2 = Spinbox(tab6, from_=00, to=59, width=3, format='%02.0f')
    spin6_E_2.delete(0,'end')
    spin6_E_2.insert(0,'07')
    spin6_F_2.delete(0,'end')
    spin6_F_2.insert(0,'00')
    label6_h0_2 = Label(tab6, text=':')
    label6_m0_2 = Label(tab6, text='')
    date6_2_entry = Spinbox(tab6, from_=00, to=31, width=3, format='%02.0f')
    month6_2_entry = Spinbox(tab6, from_=00, to=12, width=3, format='%02.0f')
    year6_2_entry = Spinbox(tab6, from_=2018, to=2030, width=5)
    date6_2_entry.delete(0,'end')
    today=datetime.date.today() # today
    day_phase2 = today + datetime.timedelta(days=7) # calculate dates for 7 days after recording initiation
    date6_2_entry.insert(0,'{:02d}'.format(day_phase2.day))
    month6_2_entry.delete(0,'end')
    month6_2_entry.insert(0,'{:02d}'.format(day_phase2.month))
    year6_2_entry.delete(0,'end')
    year6_2_entry.insert(0,day_phase2.year) # ISO format is YYYY/MM/DD

    label3_d_0 = Label(tab6, text= 'Month')
    label3_m_0 = Label(tab6, text= 'Date')
    label3_m_0.grid(column=11,row=2+row_adj)
    label3_d_0.grid(column=9,row=2+row_adj)
    label3_d_1 = Label(tab6, text= '/')
    label3_m_1 = Label(tab6, text= '/')
    label3_d_1.grid(column=8,row=2+row_adj)
    label3_m_1.grid(column=10,row=2+row_adj)

    label6_d_2 = Label(tab6, text= '/')
    label6_m_2 = Label(tab6, text= '/')
    rad6_A_2 = Radiobutton(tab6, text='LD', variable=var6_2, value=1)
    lbl6_A_2 = Label(tab6, text= 'On:')
    spin6_A_2 = Spinbox(tab6, from_=00, to=24, width=3, format='%02.0f')
    spin6_B_2 = Spinbox(tab6, from_=00, to=59, width=3, format='%02.0f')
    spin6_A_2.delete(0,'end')
    spin6_A_2.insert(0,'07')
    spin6_B_2.delete(0,'end')
    spin6_B_2.insert(0,'00')
    label6_h1_2 = Label(tab6, text=':')
    label6_m1_2 = Label(tab6, text='')
    lbl6_B_2 = Label(tab6, text= 'Off:')
    spin6_C_2 = Spinbox(tab6, from_=00, to=24, width=3, format='%02.0f')
    spin6_D_2 = Spinbox(tab6, from_=00, to=59, width=3, format='%02.0f')
    spin6_C_2.delete(0,'end')
    spin6_C_2.insert(0,'19')
    spin6_D_2.delete(0,'end')
    spin6_D_2.insert(0,'00')
    label6_h2_2 = Label(tab6, text=':')
    label6_m2_2 = Label(tab6, text='')
    rad6_B_2 = Radiobutton(tab6, text='DD', variable=var6_2, value=2)
    rad6_C_2 = Radiobutton(tab6, text='LL', variable=var6_2, value=3)
    phaseLabel6_2.grid(column=0, row=3+row_adj, padx=15, pady=5)
    fromLabel6_2.grid(column=1,row=3+row_adj)
    spin6_E_2.grid(column=2,row=3+row_adj)
    label6_h0_2.grid(column=3,row=3+row_adj)
    spin6_F_2.grid(column=4,row=3+row_adj)
    label6_m0_2.grid(column=5,row=3+row_adj)
    space6_2.grid(column=6,row=3+row_adj)
    date6_2_entry.grid(column=11, row=3+row_adj)
    label6_d_2.grid(column=8,row=3+row_adj)
    month6_2_entry.grid(column=9, row=3+row_adj)
    label6_m_2.grid(column=10,row=3+row_adj)
    year6_2_entry.grid(column=7, row=3+row_adj) # ISO format
    space6_2_2.grid(column=12,row=3+row_adj,padx=5)
    rad6_A_2.grid(column=13, row=3+row_adj, pady=5)
    lbl6_A_2.grid(column=14, row=3+row_adj, pady=5)
    spin6_A_2.grid(column=15,row=3+row_adj, pady=5)
    label6_h1_2.grid(column=16,row=3+row_adj, pady=5)
    spin6_B_2.grid(column=17,row=3+row_adj, pady=5)
    label6_m1_2.grid(column=18,row=3+row_adj, pady=5)
    lbl6_B_2.grid(column=19, row=3+row_adj, pady=5)
    spin6_C_2.grid(column=20,row=3+row_adj, pady=5)
    label6_h2_2.grid(column=21,row=3+row_adj, pady=5)
    spin6_D_2.grid(column=22,row=3+row_adj, pady=5)
    label6_m2_2.grid(column=23,row=3+row_adj, pady=5)
    rad6_B_2.grid(column=24, row=3+row_adj, padx=15, pady=5)
    rad6_C_2.grid(column=25, row=3+row_adj, pady=5)

        # phase 3
    phaseLabel6_3 = Label(tab6, text='Phase 3')
    fromLabel6_3 = Label(tab6, text='From:')
    space6_3 = Label(tab6, text=' ')
    spin6_E_3 = Spinbox(tab6, from_=00, to=24, width=3, format='%02.0f')
    spin6_F_3 = Spinbox(tab6, from_=00, to=59, width=3, format='%02.0f')
    spin6_E_3.delete(0,'end')
    spin6_E_3.insert(0,'07')
    spin6_F_3.delete(0,'end')
    spin6_F_3.insert(0,'00')
    label6_h0_3 = Label(tab6, text=':')
    label6_m0_3 = Label(tab6, text='')
    date6_3_entry = Spinbox(tab6, from_=00, to=31, width=3, format='%02.0f')
    month6_3_entry = Spinbox(tab6, from_=00, to=12, width=3, format='%02.0f')
    year6_3_entry = Spinbox(tab6, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase3 = day_phase2 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date6_3_entry.delete(0,'end')
    date6_3_entry.insert(0,'{:02d}'.format(day_phase3.day))
    month6_3_entry.delete(0,'end')
    month6_3_entry.insert(0,'{:02d}'.format(day_phase3.month))
    year6_3_entry.delete(0,'end')
    year6_3_entry.insert(0,day_phase3.year)
    label6_d_3 = Label(tab6, text= '/')
    label6_m_3 = Label(tab6, text= '/')
    rad6_A_3 = Radiobutton(tab6, text='LD', variable=var6_3, value=1)
    lbl6_A_3 = Label(tab6, text= 'On:')
    spin6_A_3 = Spinbox(tab6, from_=00, to=24, width=3, format='%02.0f')
    spin6_B_3 = Spinbox(tab6, from_=00, to=59, width=3, format='%02.0f')
    spin6_A_3.delete(0,'end')
    spin6_A_3.insert(0,'07')
    spin6_B_3.delete(0,'end')
    spin6_B_3.insert(0,'00')
    label6_h1_3 = Label(tab6, text=':')
    label6_m1_3 = Label(tab6, text='')
    lbl6_B_3 = Label(tab6, text= 'Off:')
    spin6_C_3 = Spinbox(tab6, from_=00, to=24, width=3, format='%02.0f')
    spin6_D_3 = Spinbox(tab6, from_=00, to=59, width=3, format='%02.0f')
    spin6_C_3.delete(0,'end')
    spin6_C_3.insert(0,'19')
    spin6_D_3.delete(0,'end')
    spin6_D_3.insert(0,'00')
    label6_h2_3 = Label(tab6, text=':')
    label6_m2_3 = Label(tab6, text='')
    rad6_B_3 = Radiobutton(tab6, text='DD', variable=var6_3, value=2)
    rad6_C_3 = Radiobutton(tab6, text='LL', variable=var6_3, value=3)
    phaseLabel6_3.grid(column=0, row=4+row_adj, padx=15, pady=5)
    fromLabel6_3.grid(column=1,row=4+row_adj)
    spin6_E_3.grid(column=2,row=4+row_adj)
    label6_h0_3.grid(column=3,row=4+row_adj)
    spin6_F_3.grid(column=4,row=4+row_adj)
    label6_m0_3.grid(column=5,row=4+row_adj)
    space6_3.grid(column=6,row=4+row_adj)
    date6_3_entry.grid(column=11, row=4+row_adj)
    label6_d_3.grid(column=8,row=4+row_adj)
    month6_3_entry.grid(column=9, row=4+row_adj)
    label6_m_3.grid(column=10,row=4+row_adj)
    year6_3_entry.grid(column=7, row=4+row_adj) # ISO format
    rad6_A_3.grid(column=13, row=4+row_adj, pady=5)
    lbl6_A_3.grid(column=14, row=4+row_adj, pady=5)
    spin6_A_3.grid(column=15,row=4+row_adj, pady=5)
    label6_h1_3.grid(column=16,row=4+row_adj, pady=5)
    spin6_B_3.grid(column=17,row=4+row_adj, pady=5)
    label6_m1_3.grid(column=18,row=4+row_adj, pady=5)
    lbl6_B_3.grid(column=19, row=4+row_adj, pady=5)
    spin6_C_3.grid(column=20,row=4+row_adj, pady=5)
    label6_h2_3.grid(column=21,row=4+row_adj, pady=5)
    spin6_D_3.grid(column=22,row=4+row_adj, pady=5)
    label6_m2_3.grid(column=23,row=4+row_adj, pady=5)
    rad6_B_3.grid(column=24, row=4+row_adj, padx=15, pady=5)
    rad6_C_3.grid(column=25, row=4+row_adj, pady=5)

        # phase 4
    phaseLabel6_4 = Label(tab6, text='Phase 4')
    fromLabel6_4 = Label(tab6, text='From:')
    space6_4 = Label(tab6, text=' ')
    space6_4_2 = Label(tab6, text=' ')
    spin6_E_4 = Spinbox(tab6, from_=00, to=24, width=3, format='%02.0f')
    spin6_F_4 = Spinbox(tab6, from_=00, to=59, width=3, format='%02.0f')
    spin6_E_4.delete(0,'end')
    spin6_E_4.insert(0,'07')
    spin6_F_4.delete(0,'end')
    spin6_F_4.insert(0,'00')
    label6_h0_4 = Label(tab6, text=':')
    label6_m0_4 = Label(tab6, text='')
    date6_4_entry = Spinbox(tab6, from_=00, to=31, width=3, format='%02.0f')
    month6_4_entry = Spinbox(tab6, from_=00, to=12, width=3, format='%02.0f')
    year6_4_entry = Spinbox(tab6, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase4 = day_phase3 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date6_4_entry.delete(0,'end')
    date6_4_entry.insert(0,'{:02d}'.format(day_phase4.day))
    month6_4_entry.delete(0,'end')
    month6_4_entry.insert(0,'{:02d}'.format(day_phase4.month))
    year6_4_entry.delete(0,'end')
    year6_4_entry.insert(0,day_phase4.year)
    label6_d_4 = Label(tab6, text= '/')
    label6_m_4 = Label(tab6, text= '/')
    rad6_A_4 = Radiobutton(tab6, text='LD', variable=var6_4, value=1)
    lbl6_A_4 = Label(tab6, text= 'On:')
    spin6_A_4 = Spinbox(tab6, from_=00, to=24, width=3, format='%02.0f')
    spin6_B_4 = Spinbox(tab6, from_=00, to=59, width=3, format='%02.0f')
    spin6_A_4.delete(0,'end')
    spin6_A_4.insert(0,'07')
    spin6_B_4.delete(0,'end')
    spin6_B_4.insert(0,'00')
    label6_h1_4 = Label(tab6, text=':')
    label6_m1_4 = Label(tab6, text='')
    lbl6_B_4 = Label(tab6, text= 'Off:')
    spin6_C_4 = Spinbox(tab6, from_=00, to=24, width=3, format='%02.0f')
    spin6_D_4 = Spinbox(tab6, from_=00, to=59, width=3, format='%02.0f')
    spin6_C_4.delete(0,'end')
    spin6_C_4.insert(0,'19')
    spin6_D_4.delete(0,'end')
    spin6_D_4.insert(0,'00')
    label6_h2_4 = Label(tab6, text=':')
    label6_m2_4 = Label(tab6, text='')
    rad6_B_4 = Radiobutton(tab6, text='DD', variable=var6_4, value=2)
    rad6_C_4 = Radiobutton(tab6, text='LL', variable=var6_4, value=3)
    phaseLabel6_4.grid(column=0, row=5+row_adj, padx=15, pady=5)
    fromLabel6_4.grid(column=1,row=5+row_adj)
    spin6_E_4.grid(column=2,row=5+row_adj)
    label6_h0_4.grid(column=3,row=5+row_adj)
    spin6_F_4.grid(column=4,row=5+row_adj)
    label6_m0_4.grid(column=5,row=5+row_adj)
    space6_4.grid(column=6,row=5+row_adj)
    date6_4_entry.grid(column=11, row=5+row_adj)
    label6_d_4.grid(column=8,row=5+row_adj)
    month6_4_entry.grid(column=9, row=5+row_adj)
    label6_m_4.grid(column=10,row=5+row_adj)
    year6_4_entry.grid(column=7, row=5+row_adj) # ISO format
    space6_4_2.grid(column=12,row=5+row_adj,padx=5)
    rad6_A_4.grid(column=13, row=5+row_adj, pady=5)
    lbl6_A_4.grid(column=14, row=5+row_adj, pady=5)
    spin6_A_4.grid(column=15,row=5+row_adj, pady=5)
    label6_h1_4.grid(column=16,row=5+row_adj, pady=5)
    spin6_B_4.grid(column=17,row=5+row_adj, pady=5)
    label6_m1_4.grid(column=18,row=5+row_adj, pady=5)
    lbl6_B_4.grid(column=19, row=5+row_adj, pady=5)
    spin6_C_4.grid(column=20,row=5+row_adj, pady=5)
    label6_h2_4.grid(column=21,row=5+row_adj, pady=5)
    spin6_D_4.grid(column=22,row=5+row_adj, pady=5)
    label6_m2_4.grid(column=23,row=5+row_adj, pady=5)
    rad6_B_4.grid(column=24, row=5+row_adj, padx=15, pady=5)
    rad6_C_4.grid(column=25, row=5+row_adj, pady=5)

    # phase 5
    phaseLabel6_5 = Label(tab6, text='Phase 5')
    fromLabel6_5 = Label(tab6, text='From:')
    space6_5 = Label(tab6, text=' ')
    space6_5_2 = Label(tab6, text=' ')
    spin6_E_5 = Spinbox(tab6, from_=00, to=24, width=3, format='%02.0f')
    spin6_F_5 = Spinbox(tab6, from_=00, to=59, width=3, format='%02.0f')
    spin6_E_5.delete(0,'end')
    spin6_E_5.insert(0,'07')
    spin6_F_5.delete(0,'end')
    spin6_F_5.insert(0,'00')
    label6_h0_5 = Label(tab6, text=':')
    label6_m0_5 = Label(tab6, text='')
    date6_5_entry = Spinbox(tab6, from_=00, to=31, width=3, format='%02.0f')
    month6_5_entry = Spinbox(tab6, from_=00, to=12, width=3, format='%02.0f')
    year6_5_entry = Spinbox(tab6, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase5 = day_phase4 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date6_5_entry.delete(0,'end')
    date6_5_entry.insert(0,'{:02d}'.format(day_phase5.day))
    month6_5_entry.delete(0,'end')
    month6_5_entry.insert(0,'{:02d}'.format(day_phase5.month))
    year6_5_entry.delete(0,'end')
    year6_5_entry.insert(0,day_phase5.year)
    label6_d_5 = Label(tab6, text= '/')
    label6_m_5 = Label(tab6, text= '/')
    rad6_A_5 = Radiobutton(tab6, text='LD', variable=var6_5, value=1)
    lbl6_A_5 = Label(tab6, text= 'On:')
    spin6_A_5 = Spinbox(tab6, from_=00, to=24, width=3, format='%02.0f')
    spin6_B_5 = Spinbox(tab6, from_=00, to=59, width=3, format='%02.0f')
    spin6_A_5.delete(0,'end')
    spin6_A_5.insert(0,'07')
    spin6_B_5.delete(0,'end')
    spin6_B_5.insert(0,'00')
    label6_h1_5 = Label(tab6, text=':')
    label6_m1_5 = Label(tab6, text='')
    lbl6_B_5 = Label(tab6, text= 'Off:')
    spin6_C_5 = Spinbox(tab6, from_=00, to=24, width=3, format='%02.0f')
    spin6_D_5 = Spinbox(tab6, from_=00, to=59, width=3, format='%02.0f')
    spin6_C_5.delete(0,'end')
    spin6_C_5.insert(0,'19')
    spin6_D_5.delete(0,'end')
    spin6_D_5.insert(0,'00')
    label6_h2_5 = Label(tab6, text=':')
    label6_m2_5 = Label(tab6, text='')
    rad6_B_5 = Radiobutton(tab6, text='DD', variable=var6_5, value=2)
    rad6_C_5 = Radiobutton(tab6, text='LL', variable=var6_5, value=3)
    phaseLabel6_5.grid(column=0, row=6+row_adj, padx=15, pady=5)
    fromLabel6_5.grid(column=1,row=6+row_adj)
    spin6_E_5.grid(column=2,row=6+row_adj)
    label6_h0_5.grid(column=3,row=6+row_adj)
    spin6_F_5.grid(column=4,row=6+row_adj)
    label6_m0_5.grid(column=5,row=6+row_adj)
    space6_5.grid(column=6,row=6+row_adj)
    date6_5_entry.grid(column=11, row=6+row_adj)
    label6_d_5.grid(column=8,row=6+row_adj)
    month6_5_entry.grid(column=9, row=6+row_adj)
    label6_m_5.grid(column=10,row=6+row_adj)
    year6_5_entry.grid(column=7, row=6+row_adj) # ISO format
    space6_5_2.grid(column=12,row=6+row_adj,padx=5)
    rad6_A_5.grid(column=13, row=6+row_adj, pady=5)
    lbl6_A_5.grid(column=14, row=6+row_adj, pady=5)
    spin6_A_5.grid(column=15,row=6+row_adj, pady=5)
    label6_h1_5.grid(column=16,row=6+row_adj, pady=5)
    spin6_B_5.grid(column=17,row=6+row_adj, pady=5)
    label6_m1_5.grid(column=18,row=6+row_adj, pady=5)
    lbl6_B_5.grid(column=19, row=6+row_adj, pady=5)
    spin6_C_5.grid(column=20,row=6+row_adj, pady=5)
    label6_h2_5.grid(column=21,row=6+row_adj, pady=5)
    spin6_D_5.grid(column=22,row=6+row_adj, pady=5)
    label6_m2_5.grid(column=23,row=6+row_adj, pady=5)
    rad6_B_5.grid(column=24, row=6+row_adj, padx=15, pady=5)
    rad6_C_5.grid(column=25, row=6+row_adj, pady=5)

        # phase 6
    phaseLabel6_6 = Label(tab6, text='Phase 6')
    fromLabel6_6 = Label(tab6, text='From:')
    space6_6 = Label(tab6, text=' ')
    space6_6_2 = Label(tab6, text=' ')
    spin6_E_6 = Spinbox(tab6, from_=00, to=24, width=3, format='%02.0f')
    spin6_F_6 = Spinbox(tab6, from_=00, to=59, width=3, format='%02.0f')
    spin6_E_6.delete(0,'end')
    spin6_E_6.insert(0,'07')
    spin6_F_6.delete(0,'end')
    spin6_F_6.insert(0,'00')
    label6_h0_6 = Label(tab6, text=':')
    label6_m0_6 = Label(tab6, text='')
    date6_6_entry = Spinbox(tab6, from_=00, to=31, width=3, format='%02.0f')
    month6_6_entry = Spinbox(tab6, from_=00, to=12, width=3, format='%02.0f')
    year6_6_entry = Spinbox(tab6, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase6 = day_phase5 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date6_6_entry.delete(0,'end')
    date6_6_entry.insert(0,'{:02d}'.format(day_phase6.day))
    month6_6_entry.delete(0,'end')
    month6_6_entry.insert(0,'{:02d}'.format(day_phase6.month))
    year6_6_entry.delete(0,'end')
    year6_6_entry.insert(0,day_phase6.year)
    label6_d_6 = Label(tab6, text= '/')
    label6_m_6 = Label(tab6, text= '/')
    rad6_A_6 = Radiobutton(tab6, text='LD', variable=var6_6, value=1)
    lbl6_A_6 = Label(tab6, text= 'On:')
    spin6_A_6 = Spinbox(tab6, from_=00, to=24, width=3, format='%02.0f')
    spin6_B_6 = Spinbox(tab6, from_=00, to=59, width=3, format='%02.0f')
    spin6_A_6.delete(0,'end')
    spin6_A_6.insert(0,'07')
    spin6_B_6.delete(0,'end')
    spin6_B_6.insert(0,'00')
    label6_h1_6 = Label(tab6, text=':')
    label6_m1_6 = Label(tab6, text='')
    lbl6_B_6 = Label(tab6, text= 'Off:')
    spin6_C_6 = Spinbox(tab6, from_=00, to=24, width=3, format='%02.0f')
    spin6_D_6 = Spinbox(tab6, from_=00, to=59, width=3, format='%02.0f')
    spin6_C_6.delete(0,'end')
    spin6_C_6.insert(0,'19')
    spin6_D_6.delete(0,'end')
    spin6_D_6.insert(0,'00')
    label6_h2_6 = Label(tab6, text=':')
    label6_m2_6 = Label(tab6, text='')
    rad6_B_6 = Radiobutton(tab6, text='DD', variable=var6_6, value=2)
    rad6_C_6 = Radiobutton(tab6, text='LL', variable=var6_6, value=3)
    
    
    phaseLabel6_6.grid(column=0, row=rowPhase6+row_adj, padx=15, pady=5)
    fromLabel6_6.grid(column=1,row=rowPhase6+row_adj)
    spin6_E_6.grid(column=2,row=rowPhase6+row_adj)
    label6_h0_6.grid(column=3,row=rowPhase6+row_adj)
    spin6_F_6.grid(column=4,row=rowPhase6+row_adj)
    label6_m0_6.grid(column=5,row=rowPhase6+row_adj)
    space6_6.grid(column=6,row=rowPhase6+row_adj)
    date6_6_entry.grid(column=11, row=rowPhase6+row_adj)
    label6_d_6.grid(column=8,row=rowPhase6+row_adj)
    month6_6_entry.grid(column=9, row=rowPhase6+row_adj)
    label6_m_6.grid(column=10,row=rowPhase6+row_adj)
    year6_6_entry.grid(column=7, row=rowPhase6+row_adj) # ISO format
    space6_6_2.grid(column=12,row=rowPhase6+row_adj,padx=5)
    rad6_A_6.grid(column=13, row=rowPhase6+row_adj, pady=5)
    lbl6_A_6.grid(column=14, row=rowPhase6+row_adj, pady=5)
    spin6_A_6.grid(column=15,row=rowPhase6+row_adj, pady=5)
    label6_h1_6.grid(column=16,row=rowPhase6+row_adj, pady=5)
    spin6_B_6.grid(column=17,row=rowPhase6+row_adj, pady=5)
    label6_m1_6.grid(column=18,row=rowPhase6+row_adj, pady=5)
    lbl6_B_6.grid(column=19, row=rowPhase6+row_adj, pady=5)
    spin6_C_6.grid(column=20,row=rowPhase6+row_adj, pady=5)
    label6_h2_6.grid(column=21,row=rowPhase6+row_adj, pady=5)
    spin6_D_6.grid(column=22,row=rowPhase6+row_adj, pady=5)
    label6_m2_6.grid(column=23,row=rowPhase6+row_adj, pady=5)
    rad6_B_6.grid(column=24, row=rowPhase6+row_adj, padx=15, pady=5)
    rad6_C_6.grid(column=25, row=rowPhase6+row_adj, pady=5)

        # phase 7
    phaseLabel6_7 = Label(tab6, text='Phase 7')
    fromLabel6_7 = Label(tab6, text='From:')
    space6_7 = Label(tab6, text=' ')
    space6_7_2 = Label(tab6, text=' ')
    spin6_E_7 = Spinbox(tab6, from_=00, to=24, width=3, format='%02.0f')
    spin6_F_7 = Spinbox(tab6, from_=00, to=59, width=3, format='%02.0f')
    spin6_E_7.delete(0,'end')
    spin6_E_7.insert(0,'07')
    spin6_F_7.delete(0,'end')
    spin6_F_7.insert(0,'00')
    label6_h0_7 = Label(tab6, text=':')
    label6_m0_7 = Label(tab6, text='')
    date6_7_entry = Spinbox(tab6, from_=00, to=31, width=3, format='%02.0f')
    month6_7_entry = Spinbox(tab6, from_=00, to=12, width=3, format='%02.0f')
    year6_7_entry = Spinbox(tab6, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase7 = day_phase6 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date6_7_entry.delete(0,'end')
    date6_7_entry.insert(0,'{:02d}'.format(day_phase7.day))
    month6_7_entry.delete(0,'end')
    month6_7_entry.insert(0,'{:02d}'.format(day_phase7.month))
    year6_7_entry.delete(0,'end')
    year6_7_entry.insert(0,day_phase7.year)
    label6_d_7 = Label(tab6, text= '/')
    label6_m_7 = Label(tab6, text= '/')
    rad6_A_7 = Radiobutton(tab6, text='LD', variable=var6_7, value=1)
    lbl6_A_7 = Label(tab6, text= 'On:')
    spin6_A_7 = Spinbox(tab6, from_=00, to=24, width=3, format='%02.0f')
    spin6_B_7 = Spinbox(tab6, from_=00, to=59, width=3, format='%02.0f')
    spin6_A_7.delete(0,'end')
    spin6_A_7.insert(0,'07')
    spin6_B_7.delete(0,'end')
    spin6_B_7.insert(0,'00')
    label6_h1_7 = Label(tab6, text=':')
    label6_m1_7 = Label(tab6, text='')
    lbl6_B_7 = Label(tab6, text= 'Off:')
    spin6_C_7 = Spinbox(tab6, from_=00, to=24, width=3, format='%02.0f')
    spin6_D_7 = Spinbox(tab6, from_=00, to=59, width=3, format='%02.0f')
    spin6_C_7.delete(0,'end')
    spin6_C_7.insert(0,'19')
    spin6_D_7.delete(0,'end')
    spin6_D_7.insert(0,'00')
    label6_h2_7 = Label(tab6, text=':')
    label6_m2_7 = Label(tab6, text='')
    rad6_B_7 = Radiobutton(tab6, text='DD', variable=var6_7, value=2)
    rad6_C_7 = Radiobutton(tab6, text='LL', variable=var6_7, value=3)
    
    
    phaseLabel6_7.grid(column=0, row=rowPhase7+row_adj, padx=15, pady=5)
    fromLabel6_7.grid(column=1,row=rowPhase7+row_adj)
    spin6_E_7.grid(column=2,row=rowPhase7+row_adj)
    label6_h0_7.grid(column=3,row=rowPhase7+row_adj)
    spin6_F_7.grid(column=4,row=rowPhase7+row_adj)
    label6_m0_7.grid(column=5,row=rowPhase7+row_adj)
    space6_7.grid(column=7,row=rowPhase7+row_adj)
    date6_7_entry.grid(column=11, row=rowPhase7+row_adj)
    label6_d_7.grid(column=8,row=rowPhase7+row_adj)
    month6_7_entry.grid(column=9, row=rowPhase7+row_adj)
    label6_m_7.grid(column=10,row=rowPhase7+row_adj)
    year6_7_entry.grid(column=7, row=rowPhase7+row_adj) # ISO format
    space6_7_2.grid(column=12,row=rowPhase7+row_adj,padx=5)
    rad6_A_7.grid(column=13, row=rowPhase7+row_adj, pady=5)
    lbl6_A_7.grid(column=14, row=rowPhase7+row_adj, pady=5)
    spin6_A_7.grid(column=15,row=rowPhase7+row_adj, pady=5)
    label6_h1_7.grid(column=16,row=rowPhase7+row_adj, pady=5)
    spin6_B_7.grid(column=17,row=rowPhase7+row_adj, pady=5)
    label6_m1_7.grid(column=18,row=rowPhase7+row_adj, pady=5)
    lbl6_B_7.grid(column=19, row=rowPhase7+row_adj, pady=5)
    spin6_C_7.grid(column=20,row=rowPhase7+row_adj, pady=5)
    label6_h2_7.grid(column=21,row=rowPhase7+row_adj, pady=5)
    spin6_D_7.grid(column=22,row=rowPhase7+row_adj, pady=5)
    label6_m2_7.grid(column=23,row=rowPhase7+row_adj, pady=5)
    rad6_B_7.grid(column=24, row=rowPhase7+row_adj, padx=15, pady=5)
    rad6_C_7.grid(column=25, row=rowPhase7+row_adj, pady=5)

    # phase 8
    phaseLabel6_8 = Label(tab6, text='Phase 8')
    fromLabel6_8 = Label(tab6, text='From:')
    space6_8 = Label(tab6, text=' ')
    space6_8_2 = Label(tab6, text=' ')
    spin6_E_8 = Spinbox(tab6, from_=00, to=24, width=3, format='%02.0f')
    spin6_F_8 = Spinbox(tab6, from_=00, to=59, width=3, format='%02.0f')
    spin6_E_8.delete(0,'end')
    spin6_E_8.insert(0,'07')
    spin6_F_8.delete(0,'end')
    spin6_F_8.insert(0,'00')
    label6_h0_8 = Label(tab6, text=':')
    label6_m0_8 = Label(tab6, text='')
    date6_8_entry = Spinbox(tab6, from_=00, to=31, width=3, format='%02.0f')
    month6_8_entry = Spinbox(tab6, from_=00, to=12, width=3, format='%02.0f')
    year6_8_entry = Spinbox(tab6, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase8 = day_phase7 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date6_8_entry.delete(0,'end')
    date6_8_entry.insert(0,'{:02d}'.format(day_phase8.day))
    month6_8_entry.delete(0,'end')
    month6_8_entry.insert(0,'{:02d}'.format(day_phase8.month))
    year6_8_entry.delete(0,'end')
    year6_8_entry.insert(0,day_phase8.year)
    label6_d_8 = Label(tab6, text= '/')
    label6_m_8 = Label(tab6, text= '/')
    rad6_A_8 = Radiobutton(tab6, text='LD', variable=var6_8, value=1)
    lbl6_A_8 = Label(tab6, text= 'On:')
    spin6_A_8 = Spinbox(tab6, from_=00, to=24, width=3, format='%02.0f')
    spin6_B_8 = Spinbox(tab6, from_=00, to=59, width=3, format='%02.0f')
    spin6_A_8.delete(0,'end')
    spin6_A_8.insert(0,'07')
    spin6_B_8.delete(0,'end')
    spin6_B_8.insert(0,'00')
    label6_h1_8 = Label(tab6, text=':')
    label6_m1_8 = Label(tab6, text='')
    lbl6_B_8 = Label(tab6, text= 'Off:')
    spin6_C_8 = Spinbox(tab6, from_=00, to=24, width=3, format='%02.0f')
    spin6_D_8 = Spinbox(tab6, from_=00, to=59, width=3, format='%02.0f')
    spin6_C_8.delete(0,'end')
    spin6_C_8.insert(0,'19')
    spin6_D_8.delete(0,'end')
    spin6_D_8.insert(0,'00')
    label6_h2_8 = Label(tab6, text=':')
    label6_m2_8 = Label(tab6, text='')
    rad6_B_8 = Radiobutton(tab6, text='DD', variable=var6_8, value=2)
    rad6_C_8 = Radiobutton(tab6, text='LL', variable=var6_8, value=3)
    
    
    phaseLabel6_8.grid(column=0, row=rowPhase8+row_adj, padx=15, pady=5)
    fromLabel6_8.grid(column=1,row=rowPhase8+row_adj)
    spin6_E_8.grid(column=2,row=rowPhase8+row_adj)
    label6_h0_8.grid(column=3,row=rowPhase8+row_adj)
    spin6_F_8.grid(column=4,row=rowPhase8+row_adj)
    label6_m0_8.grid(column=5,row=rowPhase8+row_adj)
    space6_8.grid(column=7,row=rowPhase8+row_adj)
    date6_8_entry.grid(column=11, row=rowPhase8+row_adj)
    label6_d_8.grid(column=8,row=rowPhase8+row_adj)
    month6_8_entry.grid(column=9, row=rowPhase8+row_adj)
    label6_m_8.grid(column=10,row=rowPhase8+row_adj)
    year6_8_entry.grid(column=7, row=rowPhase8+row_adj) # ISO format
    space6_8_2.grid(column=12,row=rowPhase8+row_adj,padx=5)
    rad6_A_8.grid(column=13, row=rowPhase8+row_adj, pady=5)
    lbl6_A_8.grid(column=14, row=rowPhase8+row_adj, pady=5)
    spin6_A_8.grid(column=15,row=rowPhase8+row_adj, pady=5)
    label6_h1_8.grid(column=16,row=rowPhase8+row_adj, pady=5)
    spin6_B_8.grid(column=17,row=rowPhase8+row_adj, pady=5)
    label6_m1_8.grid(column=18,row=rowPhase8+row_adj, pady=5)
    lbl6_B_8.grid(column=19, row=rowPhase8+row_adj, pady=5)
    spin6_C_8.grid(column=20,row=rowPhase8+row_adj, pady=5)
    label6_h2_8.grid(column=21,row=rowPhase8+row_adj, pady=5)
    spin6_D_8.grid(column=22,row=rowPhase8+row_adj, pady=5)
    label6_m2_8.grid(column=23,row=rowPhase8+row_adj, pady=5)
    rad6_B_8.grid(column=24, row=rowPhase8+row_adj, padx=15, pady=5)
    rad6_C_8.grid(column=25, row=rowPhase8+row_adj, pady=5)

    # phase 9
    phaseLabel6_9 = Label(tab6, text='Phase 9')
    fromLabel6_9 = Label(tab6, text='From:')
    space6_9 = Label(tab6, text=' ')
    space6_9_2 = Label(tab6, text=' ')
    spin6_E_9 = Spinbox(tab6, from_=00, to=24, width=3, format='%02.0f')
    spin6_F_9 = Spinbox(tab6, from_=00, to=59, width=3, format='%02.0f')
    spin6_E_9.delete(0,'end')
    spin6_E_9.insert(0,'07')
    spin6_F_9.delete(0,'end')
    spin6_F_9.insert(0,'00')
    label6_h0_9 = Label(tab6, text=':')
    label6_m0_9 = Label(tab6, text='')
    date6_9_entry = Spinbox(tab6, from_=00, to=31, width=3, format='%02.0f')
    month6_9_entry = Spinbox(tab6, from_=00, to=12, width=3, format='%02.0f')
    year6_9_entry = Spinbox(tab6, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase9 = day_phase8 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date6_9_entry.delete(0,'end')
    date6_9_entry.insert(0,'{:02d}'.format(day_phase9.day))
    month6_9_entry.delete(0,'end')
    month6_9_entry.insert(0,'{:02d}'.format(day_phase9.month))
    year6_9_entry.delete(0,'end')
    year6_9_entry.insert(0,day_phase9.year)
    label6_d_9 = Label(tab6, text= '/')
    label6_m_9 = Label(tab6, text= '/')
    rad6_A_9 = Radiobutton(tab6, text='LD', variable=var6_9, value=1)
    lbl6_A_9 = Label(tab6, text= 'On:')
    spin6_A_9 = Spinbox(tab6, from_=00, to=24, width=3, format='%02.0f')
    spin6_B_9 = Spinbox(tab6, from_=00, to=59, width=3, format='%02.0f')
    spin6_A_9.delete(0,'end')
    spin6_A_9.insert(0,'07')
    spin6_B_9.delete(0,'end')
    spin6_B_9.insert(0,'00')
    label6_h1_9 = Label(tab6, text=':')
    label6_m1_9 = Label(tab6, text='')
    lbl6_B_9 = Label(tab6, text= 'Off:')
    spin6_C_9 = Spinbox(tab6, from_=00, to=24, width=3, format='%02.0f')
    spin6_D_9 = Spinbox(tab6, from_=00, to=59, width=3, format='%02.0f')
    spin6_C_9.delete(0,'end')
    spin6_C_9.insert(0,'19')
    spin6_D_9.delete(0,'end')
    spin6_D_9.insert(0,'00')
    label6_h2_9 = Label(tab6, text=':')
    label6_m2_9 = Label(tab6, text='')
    rad6_B_9 = Radiobutton(tab6, text='DD', variable=var6_9, value=2)
    rad6_C_9 = Radiobutton(tab6, text='LL', variable=var6_9, value=3)
    
    
    phaseLabel6_9.grid(column=0, row=rowPhase9+row_adj, padx=15, pady=5)
    fromLabel6_9.grid(column=1,row=rowPhase9+row_adj)
    spin6_E_9.grid(column=2,row=rowPhase9+row_adj)
    label6_h0_9.grid(column=3,row=rowPhase9+row_adj)
    spin6_F_9.grid(column=4,row=rowPhase9+row_adj)
    label6_m0_9.grid(column=5,row=rowPhase9+row_adj)
    space6_9.grid(column=7,row=rowPhase9+row_adj)
    date6_9_entry.grid(column=11, row=rowPhase9+row_adj)
    label6_d_9.grid(column=8,row=rowPhase9+row_adj)
    month6_9_entry.grid(column=9, row=rowPhase9+row_adj)
    label6_m_9.grid(column=10,row=rowPhase9+row_adj)
    year6_9_entry.grid(column=7, row=rowPhase9+row_adj) # ISO format
    space6_9_2.grid(column=12,row=rowPhase9+row_adj,padx=5)
    rad6_A_9.grid(column=13, row=rowPhase9+row_adj, pady=5)
    lbl6_A_9.grid(column=14, row=rowPhase9+row_adj, pady=5)
    spin6_A_9.grid(column=15,row=rowPhase9+row_adj, pady=5)
    label6_h1_9.grid(column=16,row=rowPhase9+row_adj, pady=5)
    spin6_B_9.grid(column=17,row=rowPhase9+row_adj, pady=5)
    label6_m1_9.grid(column=18,row=rowPhase9+row_adj, pady=5)
    lbl6_B_9.grid(column=19, row=rowPhase9+row_adj, pady=5)
    spin6_C_9.grid(column=20,row=rowPhase9+row_adj, pady=5)
    label6_h2_9.grid(column=21,row=rowPhase9+row_adj, pady=5)
    spin6_D_9.grid(column=22,row=rowPhase9+row_adj, pady=5)
    label6_m2_9.grid(column=23,row=rowPhase9+row_adj, pady=5)
    rad6_B_9.grid(column=24, row=rowPhase9+row_adj, padx=15, pady=5)
    rad6_C_9.grid(column=25, row=rowPhase9+row_adj, pady=5)

    # phase 10
    phaseLabel6_10 = Label(tab6, text='Phase 10')
    fromLabel6_10 = Label(tab6, text='From:')
    space6_10 = Label(tab6, text=' ')
    space6_10_2 = Label(tab6, text=' ')
    spin6_E_10 = Spinbox(tab6, from_=00, to=24, width=3, format='%02.0f')
    spin6_F_10 = Spinbox(tab6, from_=00, to=59, width=3, format='%02.0f')
    spin6_E_10.delete(0,'end')
    spin6_E_10.insert(0,'07')
    spin6_F_10.delete(0,'end')
    spin6_F_10.insert(0,'00')
    label6_h0_10 = Label(tab6, text=':')
    label6_m0_10 = Label(tab6, text='')
    date6_10_entry = Spinbox(tab6, from_=00, to=31, width=3, format='%02.0f')
    month6_10_entry = Spinbox(tab6, from_=00, to=12, width=3, format='%02.0f')
    year6_10_entry = Spinbox(tab6, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase10 = day_phase9 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date6_10_entry.delete(0,'end')
    date6_10_entry.insert(0,'{:02d}'.format(day_phase10.day))
    month6_10_entry.delete(0,'end')
    month6_10_entry.insert(0,'{:02d}'.format(day_phase10.month))
    year6_10_entry.delete(0,'end')
    year6_10_entry.insert(0,day_phase10.year)
    label6_d_10 = Label(tab6, text= '/')
    label6_m_10 = Label(tab6, text= '/')
    rad6_A_10 = Radiobutton(tab6, text='LD', variable=var6_10, value=1)
    lbl6_A_10 = Label(tab6, text= 'On:')
    spin6_A_10 = Spinbox(tab6, from_=00, to=24, width=3, format='%02.0f')
    spin6_B_10 = Spinbox(tab6, from_=00, to=59, width=3, format='%02.0f')
    spin6_A_10.delete(0,'end')
    spin6_A_10.insert(0,'07')
    spin6_B_10.delete(0,'end')
    spin6_B_10.insert(0,'00')
    label6_h1_10 = Label(tab6, text=':')
    label6_m1_10 = Label(tab6, text='')
    lbl6_B_10 = Label(tab6, text= 'Off:')
    spin6_C_10 = Spinbox(tab6, from_=00, to=24, width=3, format='%02.0f')
    spin6_D_10 = Spinbox(tab6, from_=00, to=59, width=3, format='%02.0f')
    spin6_C_10.delete(0,'end')
    spin6_C_10.insert(0,'19')
    spin6_D_10.delete(0,'end')
    spin6_D_10.insert(0,'00')
    label6_h2_10 = Label(tab6, text=':')
    label6_m2_10 = Label(tab6, text='')
    rad6_B_10 = Radiobutton(tab6, text='DD', variable=var6_10, value=2)
    rad6_C_10 = Radiobutton(tab6, text='LL', variable=var6_10, value=3)
    
    
    phaseLabel6_10.grid(column=0, row=rowPhase10+row_adj, padx=15, pady=5)
    fromLabel6_10.grid(column=1,row=rowPhase10+row_adj)
    spin6_E_10.grid(column=2,row=rowPhase10+row_adj)
    label6_h0_10.grid(column=3,row=rowPhase10+row_adj)
    spin6_F_10.grid(column=4,row=rowPhase10+row_adj)
    label6_m0_10.grid(column=5,row=rowPhase10+row_adj)
    space6_10.grid(column=7,row=rowPhase10+row_adj)
    date6_10_entry.grid(column=11, row=rowPhase10+row_adj)
    label6_d_10.grid(column=8,row=rowPhase10+row_adj)
    month6_10_entry.grid(column=9, row=rowPhase10+row_adj)
    label6_m_10.grid(column=10,row=rowPhase10+row_adj)
    year6_10_entry.grid(column=7, row=rowPhase10+row_adj) # ISO format
    space6_10_2.grid(column=12,row=rowPhase10+row_adj,padx=5)
    rad6_A_10.grid(column=13, row=rowPhase10+row_adj, pady=5)
    lbl6_A_10.grid(column=14, row=rowPhase10+row_adj, pady=5)
    spin6_A_10.grid(column=15,row=rowPhase10+row_adj, pady=5)
    label6_h1_10.grid(column=16,row=rowPhase10+row_adj, pady=5)
    spin6_B_10.grid(column=17,row=rowPhase10+row_adj, pady=5)
    label6_m1_10.grid(column=18,row=rowPhase10+row_adj, pady=5)
    lbl6_B_10.grid(column=19, row=rowPhase10+row_adj, pady=5)
    spin6_C_10.grid(column=20,row=rowPhase10+row_adj, pady=5)
    label6_h2_10.grid(column=21,row=rowPhase10+row_adj, pady=5)
    spin6_D_10.grid(column=22,row=rowPhase10+row_adj, pady=5)
    label6_m2_10.grid(column=23,row=rowPhase10+row_adj, pady=5)
    rad6_B_10.grid(column=24, row=rowPhase10+row_adj, padx=15, pady=5)
    rad6_C_10.grid(column=25, row=rowPhase10+row_adj, pady=5)

    # phase 11
    phaseLabel6_11 = Label(tab6, text='Phase 11')
    fromLabel6_11 = Label(tab6, text='From:')
    space6_11 = Label(tab6, text=' ')
    space6_11_2 = Label(tab6, text=' ')
    spin6_E_11 = Spinbox(tab6, from_=00, to=24, width=3, format='%02.0f')
    spin6_F_11 = Spinbox(tab6, from_=00, to=59, width=3, format='%02.0f')
    spin6_E_11.delete(0,'end')
    spin6_E_11.insert(0,'07')
    spin6_F_11.delete(0,'end')
    spin6_F_11.insert(0,'00')
    label6_h0_11 = Label(tab6, text=':')
    label6_m0_11 = Label(tab6, text='')
    date6_11_entry = Spinbox(tab6, from_=00, to=31, width=3, format='%02.0f')
    month6_11_entry = Spinbox(tab6, from_=00, to=12, width=3, format='%02.0f')
    year6_11_entry = Spinbox(tab6, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase11 = day_phase10 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date6_11_entry.delete(0,'end')
    date6_11_entry.insert(0,'{:02d}'.format(day_phase11.day))
    month6_11_entry.delete(0,'end')
    month6_11_entry.insert(0,'{:02d}'.format(day_phase11.month))
    year6_11_entry.delete(0,'end')
    year6_11_entry.insert(0,day_phase11.year)
    label6_d_11 = Label(tab6, text= '/')
    label6_m_11 = Label(tab6, text= '/')
    rad6_A_11 = Radiobutton(tab6, text='LD', variable=var6_11, value=1)
    lbl6_A_11 = Label(tab6, text= 'On:')
    spin6_A_11 = Spinbox(tab6, from_=00, to=24, width=3, format='%02.0f')
    spin6_B_11 = Spinbox(tab6, from_=00, to=59, width=3, format='%02.0f')
    spin6_A_11.delete(0,'end')
    spin6_A_11.insert(0,'07')
    spin6_B_11.delete(0,'end')
    spin6_B_11.insert(0,'00')
    label6_h1_11 = Label(tab6, text=':')
    label6_m1_11 = Label(tab6, text='')
    lbl6_B_11 = Label(tab6, text= 'Off:')
    spin6_C_11 = Spinbox(tab6, from_=00, to=24, width=3, format='%02.0f')
    spin6_D_11 = Spinbox(tab6, from_=00, to=59, width=3, format='%02.0f')
    spin6_C_11.delete(0,'end')
    spin6_C_11.insert(0,'19')
    spin6_D_11.delete(0,'end')
    spin6_D_11.insert(0,'00')
    label6_h2_11 = Label(tab6, text=':')
    label6_m2_11 = Label(tab6, text='')
    rad6_B_11 = Radiobutton(tab6, text='DD', variable=var6_11, value=2)
    rad6_C_11 = Radiobutton(tab6, text='LL', variable=var6_11, value=3)
    
    
    phaseLabel6_11.grid(column=0, row=rowPhase11+row_adj, padx=15, pady=5)
    fromLabel6_11.grid(column=1,row=rowPhase11+row_adj)
    spin6_E_11.grid(column=2,row=rowPhase11+row_adj)
    label6_h0_11.grid(column=3,row=rowPhase11+row_adj)
    spin6_F_11.grid(column=4,row=rowPhase11+row_adj)
    label6_m0_11.grid(column=5,row=rowPhase11+row_adj)
    space6_11.grid(column=7,row=rowPhase11+row_adj)
    date6_11_entry.grid(column=11, row=rowPhase11+row_adj)
    label6_d_11.grid(column=8,row=rowPhase11+row_adj)
    month6_11_entry.grid(column=9, row=rowPhase11+row_adj)
    label6_m_11.grid(column=10,row=rowPhase11+row_adj)
    year6_11_entry.grid(column=7, row=rowPhase11+row_adj) # ISO format
    space6_11_2.grid(column=12,row=rowPhase11+row_adj,padx=5)
    rad6_A_11.grid(column=13, row=rowPhase11+row_adj, pady=5)
    lbl6_A_11.grid(column=14, row=rowPhase11+row_adj, pady=5)
    spin6_A_11.grid(column=15,row=rowPhase11+row_adj, pady=5)
    label6_h1_11.grid(column=16,row=rowPhase11+row_adj, pady=5)
    spin6_B_11.grid(column=17,row=rowPhase11+row_adj, pady=5)
    label6_m1_11.grid(column=18,row=rowPhase11+row_adj, pady=5)
    lbl6_B_11.grid(column=19, row=rowPhase11+row_adj, pady=5)
    spin6_C_11.grid(column=20,row=rowPhase11+row_adj, pady=5)
    label6_h2_11.grid(column=21,row=rowPhase11+row_adj, pady=5)
    spin6_D_11.grid(column=22,row=rowPhase11+row_adj, pady=5)
    label6_m2_11.grid(column=23,row=rowPhase11+row_adj, pady=5)
    rad6_B_11.grid(column=24, row=rowPhase11+row_adj, padx=15, pady=5)
    rad6_C_11.grid(column=25, row=rowPhase11+row_adj, pady=5)

    # phase 12
    phaseLabel6_12 = Label(tab6, text='Phase 12')
    fromLabel6_12 = Label(tab6, text='From:')
    space6_12 = Label(tab6, text=' ')
    space6_12_2 = Label(tab6, text=' ')
    spin6_E_12 = Spinbox(tab6, from_=00, to=24, width=3, format='%02.0f')
    spin6_F_12 = Spinbox(tab6, from_=00, to=59, width=3, format='%02.0f')
    spin6_E_12.delete(0,'end')
    spin6_E_12.insert(0,'07')
    spin6_F_12.delete(0,'end')
    spin6_F_12.insert(0,'00')
    label6_h0_12 = Label(tab6, text=':')
    label6_m0_12 = Label(tab6, text='')
    date6_12_entry = Spinbox(tab6, from_=00, to=31, width=3, format='%02.0f')
    month6_12_entry = Spinbox(tab6, from_=00, to=12, width=3, format='%02.0f')
    year6_12_entry = Spinbox(tab6, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase12 = day_phase11 + datetime.timedelta(days=7) # calculate dates for 21 days after recording initiation
    date6_12_entry.delete(0,'end')
    date6_12_entry.insert(0,'{:02d}'.format(day_phase12.day))
    month6_12_entry.delete(0,'end')
    month6_12_entry.insert(0,'{:02d}'.format(day_phase12.month))
    year6_12_entry.delete(0,'end')
    year6_12_entry.insert(0,day_phase12.year)
    label6_d_12 = Label(tab6, text= '/')
    label6_m_12 = Label(tab6, text= '/')
    rad6_A_12 = Radiobutton(tab6, text='LD', variable=var6_12, value=1)
    lbl6_A_12 = Label(tab6, text= 'On:')
    spin6_A_12 = Spinbox(tab6, from_=00, to=24, width=3, format='%02.0f')
    spin6_B_12 = Spinbox(tab6, from_=00, to=59, width=3, format='%02.0f')
    spin6_A_12.delete(0,'end')
    spin6_A_12.insert(0,'07')
    spin6_B_12.delete(0,'end')
    spin6_B_12.insert(0,'00')
    label6_h1_12 = Label(tab6, text=':')
    label6_m1_12 = Label(tab6, text='')
    lbl6_B_12 = Label(tab6, text= 'Off:')
    spin6_C_12 = Spinbox(tab6, from_=00, to=24, width=3, format='%02.0f')
    spin6_D_12 = Spinbox(tab6, from_=00, to=59, width=3, format='%02.0f')
    spin6_C_12.delete(0,'end')
    spin6_C_12.insert(0,'19')
    spin6_D_12.delete(0,'end')
    spin6_D_12.insert(0,'00')
    label6_h2_12 = Label(tab6, text=':')
    label6_m2_12 = Label(tab6, text='')
    rad6_B_12 = Radiobutton(tab6, text='DD', variable=var6_12, value=2)
    rad6_C_12 = Radiobutton(tab6, text='LL', variable=var6_12, value=3)
    
    
    phaseLabel6_12.grid(column=0, row=rowPhase12+row_adj, padx=15, pady=5)
    fromLabel6_12.grid(column=1,row=rowPhase12+row_adj)
    spin6_E_12.grid(column=2,row=rowPhase12+row_adj)
    label6_h0_12.grid(column=3,row=rowPhase12+row_adj)
    spin6_F_12.grid(column=4,row=rowPhase12+row_adj)
    label6_m0_12.grid(column=5,row=rowPhase12+row_adj)
    space6_12.grid(column=7,row=rowPhase12+row_adj)
    date6_12_entry.grid(column=11, row=rowPhase12+row_adj)
    label6_d_12.grid(column=8,row=rowPhase12+row_adj)
    month6_12_entry.grid(column=9, row=rowPhase12+row_adj)
    label6_m_12.grid(column=10,row=rowPhase12+row_adj)
    year6_12_entry.grid(column=7, row=rowPhase12+row_adj) # ISO format
    space6_12_2.grid(column=12,row=rowPhase12+row_adj,padx=5)
    rad6_A_12.grid(column=13, row=rowPhase12+row_adj, pady=5)
    lbl6_A_12.grid(column=14, row=rowPhase12+row_adj, pady=5)
    spin6_A_12.grid(column=15,row=rowPhase12+row_adj, pady=5)
    label6_h1_12.grid(column=16,row=rowPhase12+row_adj, pady=5)
    spin6_B_12.grid(column=17,row=rowPhase12+row_adj, pady=5)
    label6_m1_12.grid(column=18,row=rowPhase12+row_adj, pady=5)
    lbl6_B_12.grid(column=19, row=rowPhase12+row_adj, pady=5)
    spin6_C_12.grid(column=20,row=rowPhase12+row_adj, pady=5)
    label6_h2_12.grid(column=21,row=rowPhase12+row_adj, pady=5)
    spin6_D_12.grid(column=22,row=rowPhase12+row_adj, pady=5)
    label6_m2_12.grid(column=23,row=rowPhase12+row_adj, pady=5)
    rad6_B_12.grid(column=24, row=rowPhase12+row_adj, padx=15, pady=5)
    rad6_C_12.grid(column=25, row=rowPhase12+row_adj, pady=5)

    #hourOn1_2, minOn1_2, hourOff1_2, minOff1_2, dark1_2, light1_2, date1_2, month1_2, year1_2, hourFrom1_2, minuteFrom1_2,
    
    input_mat = [spin1_A_1, spin1_B_1, spin1_C_1, spin1_D_1, var1_1, 0, 0,0, 0, 0,
    spin1_A_2, spin1_B_2, spin1_C_2, spin1_D_2, var1_2, date1_2_entry, month1_2_entry,year1_2_entry, spin1_E_2, spin1_F_2,
    spin1_A_3, spin1_B_3, spin1_C_3, spin1_D_3, var1_3, date1_3_entry, month1_3_entry,year1_3_entry, spin1_E_3, spin1_F_3,
    spin1_A_4, spin1_B_4, spin1_C_4, spin1_D_4, var1_4, date1_4_entry, month1_4_entry,year1_4_entry, spin1_E_4, spin1_F_4,
    spin1_A_5, spin1_B_5, spin1_C_5, spin1_D_5, var1_5, date1_5_entry, month1_5_entry,year1_5_entry, spin1_E_5, spin1_F_5,
    spin1_A_6, spin1_B_6, spin1_C_6, spin1_D_6, var1_6, date1_6_entry, month1_6_entry,year1_6_entry, spin1_E_6, spin1_F_6,
    spin1_A_7, spin1_B_7, spin1_C_7, spin1_D_7, var1_7, date1_7_entry, month1_7_entry,year1_7_entry, spin1_E_7, spin1_F_7,
    spin1_A_8, spin1_B_8, spin1_C_8, spin1_D_8, var1_8, date1_8_entry, month1_8_entry,year1_8_entry, spin1_E_8, spin1_F_8,
    spin1_A_9, spin1_B_9, spin1_C_9, spin1_D_9, var1_9, date1_9_entry, month1_9_entry,year1_9_entry, spin1_E_9, spin1_F_9,
    spin1_A_10, spin1_B_10, spin1_C_10, spin1_D_10, var1_10, date1_10_entry, month1_10_entry,year1_10_entry, spin1_E_10, spin1_F_10,
    spin1_A_11, spin1_B_11, spin1_C_11, spin1_D_11, var1_11, date1_11_entry, month1_11_entry,year1_11_entry, spin1_E_11, spin1_F_11,
    spin1_A_12, spin1_B_12, spin1_C_12, spin1_D_12, var1_12, date1_12_entry, month1_12_entry,year1_12_entry, spin1_E_12, spin1_F_12,
    spin2_A_1, spin2_B_1, spin2_C_1, spin2_D_1, var2_1, 0, 0,0, 0, 0,
    spin2_A_2, spin2_B_2, spin2_C_2, spin2_D_2, var2_2, date2_2_entry, month2_2_entry,year2_2_entry, spin2_E_2, spin2_F_2,
    spin2_A_3, spin2_B_3, spin2_C_3, spin2_D_3, var2_3, date2_3_entry, month2_3_entry,year2_3_entry, spin2_E_3, spin2_F_3,
    spin2_A_4, spin2_B_4, spin2_C_4, spin2_D_4, var2_4, date2_4_entry, month2_4_entry,year2_4_entry, spin2_E_4, spin2_F_4,
    spin2_A_5, spin2_B_5, spin2_C_5, spin2_D_5, var2_5, date2_5_entry, month2_5_entry,year2_5_entry, spin2_E_5, spin2_F_5,
    spin2_A_6, spin2_B_6, spin2_C_6, spin2_D_6, var2_6, date2_6_entry, month2_6_entry,year2_6_entry, spin2_E_6, spin2_F_6,
    spin2_A_7, spin2_B_7, spin2_C_7, spin2_D_7, var2_7, date2_7_entry, month2_7_entry,year2_7_entry, spin2_E_7, spin2_F_7,
    spin2_A_8, spin2_B_8, spin2_C_8, spin2_D_8, var2_8, date2_8_entry, month2_8_entry,year2_8_entry, spin2_E_8, spin2_F_8,
    spin2_A_9, spin2_B_9, spin2_C_9, spin2_D_9, var2_9, date2_9_entry, month2_9_entry,year2_9_entry, spin2_E_9, spin2_F_9,
    spin2_A_10, spin2_B_10, spin2_C_10, spin2_D_10, var2_10, date2_10_entry, month2_10_entry,year2_10_entry, spin2_E_10, spin2_F_10,
    spin2_A_11, spin2_B_11, spin2_C_11, spin2_D_11, var2_11, date2_11_entry, month2_11_entry,year2_11_entry, spin2_E_11, spin2_F_11,
    spin2_A_12, spin2_B_12, spin2_C_12, spin2_D_12, var2_12, date2_12_entry, month2_12_entry,year2_12_entry, spin2_E_12, spin2_F_12,
    spin3_A_1, spin3_B_1, spin3_C_1, spin3_D_1, var3_1, 0, 0,0, 0, 0,
    spin3_A_2, spin3_B_2, spin3_C_2, spin3_D_2, var3_2, date3_2_entry, month3_2_entry,year3_2_entry, spin3_E_2, spin3_F_2,
    spin3_A_3, spin3_B_3, spin3_C_3, spin3_D_3, var3_3, date3_3_entry, month3_3_entry,year3_3_entry, spin3_E_3, spin3_F_3,
    spin3_A_4, spin3_B_4, spin3_C_4, spin3_D_4, var3_4, date3_4_entry, month3_4_entry,year3_4_entry, spin3_E_4, spin3_F_4,
    spin3_A_5, spin3_B_5, spin3_C_5, spin3_D_5, var3_5, date3_5_entry, month3_5_entry,year3_5_entry, spin3_E_5, spin3_F_5,
    spin3_A_6, spin3_B_6, spin3_C_6, spin3_D_6, var3_6, date3_6_entry, month3_6_entry,year3_6_entry, spin3_E_6, spin3_F_6,
    spin3_A_7, spin3_B_7, spin3_C_7, spin3_D_7, var3_7, date3_7_entry, month3_7_entry,year3_7_entry, spin3_E_7, spin3_F_7,
    spin3_A_8, spin3_B_8, spin3_C_8, spin3_D_8, var3_8, date3_8_entry, month3_8_entry,year3_8_entry, spin3_E_8, spin3_F_8,
    spin3_A_9, spin3_B_9, spin3_C_9, spin3_D_9, var3_9, date3_9_entry, month3_9_entry,year3_9_entry, spin3_E_9, spin3_F_9,
    spin3_A_10, spin3_B_10, spin3_C_10, spin3_D_10, var3_10, date3_10_entry, month3_10_entry,year3_10_entry, spin3_E_10, spin3_F_10,
    spin3_A_11, spin3_B_11, spin3_C_11, spin3_D_11, var3_11, date3_11_entry, month3_11_entry,year3_11_entry, spin3_E_11, spin3_F_11,
    spin3_A_12, spin3_B_12, spin3_C_12, spin3_D_12, var3_12, date3_12_entry, month3_12_entry,year3_12_entry, spin3_E_12, spin3_F_12,
    spin4_A_1, spin4_B_1, spin4_C_1, spin4_D_1, var4_1, 0, 0,0, 0, 0,
    spin4_A_2, spin4_B_2, spin4_C_2, spin4_D_2, var4_2, date4_2_entry, month4_2_entry,year4_2_entry, spin4_E_2, spin4_F_2,
    spin4_A_3, spin4_B_3, spin4_C_3, spin4_D_3, var4_3, date4_3_entry, month4_3_entry,year4_3_entry, spin4_E_3, spin4_F_3,
    spin4_A_4, spin4_B_4, spin4_C_4, spin4_D_4, var4_4, date4_4_entry, month4_4_entry,year4_4_entry, spin4_E_4, spin4_F_4,
    spin4_A_5, spin4_B_5, spin4_C_5, spin4_D_5, var4_5, date4_5_entry, month4_5_entry,year4_5_entry, spin4_E_5, spin4_F_5,
    spin4_A_6, spin4_B_6, spin4_C_6, spin4_D_6, var4_6, date4_6_entry, month4_6_entry,year4_6_entry, spin4_E_6, spin4_F_6,
    spin4_A_7, spin4_B_7, spin4_C_7, spin4_D_7, var4_7, date4_7_entry, month4_7_entry,year4_7_entry, spin4_E_7, spin4_F_7,
    spin4_A_8, spin4_B_8, spin4_C_8, spin4_D_8, var4_8, date4_8_entry, month4_8_entry,year4_8_entry, spin4_E_8, spin4_F_8,
    spin4_A_9, spin4_B_9, spin4_C_9, spin4_D_9, var4_9, date4_9_entry, month4_9_entry,year4_9_entry, spin4_E_9, spin4_F_9,
    spin4_A_10, spin4_B_10, spin4_C_10, spin4_D_10, var4_10, date4_10_entry, month4_10_entry,year4_10_entry, spin4_E_10, spin4_F_10,
    spin4_A_11, spin4_B_11, spin4_C_11, spin4_D_11, var4_11, date4_11_entry, month4_11_entry,year4_11_entry, spin4_E_11, spin4_F_11,
    spin4_A_12, spin4_B_12, spin4_C_12, spin4_D_12, var4_12, date4_12_entry, month4_12_entry,year4_12_entry, spin4_E_12, spin4_F_12,
    spin5_A_1, spin5_B_1, spin5_C_1, spin5_D_1, var5_1, 0, 0,0, 0, 0,
    spin5_A_2, spin5_B_2, spin5_C_2, spin5_D_2, var5_2, date5_2_entry, month5_2_entry,year5_2_entry, spin5_E_2, spin5_F_2,
    spin5_A_3, spin5_B_3, spin5_C_3, spin5_D_3, var5_3, date5_3_entry, month5_3_entry,year5_3_entry, spin5_E_3, spin5_F_3,
    spin5_A_4, spin5_B_4, spin5_C_4, spin5_D_4, var5_4, date5_4_entry, month5_4_entry,year5_4_entry, spin5_E_4, spin5_F_4,
    spin5_A_5, spin5_B_5, spin5_C_5, spin5_D_5, var5_5, date5_5_entry, month5_5_entry,year5_5_entry, spin5_E_5, spin5_F_5,
    spin5_A_6, spin5_B_6, spin5_C_6, spin5_D_6, var5_6, date5_6_entry, month5_6_entry,year5_6_entry, spin5_E_6, spin5_F_6,
    spin5_A_7, spin5_B_7, spin5_C_7, spin5_D_7, var5_7, date5_7_entry, month5_7_entry,year5_7_entry, spin5_E_7, spin5_F_7,
    spin5_A_8, spin5_B_8, spin5_C_8, spin5_D_8, var5_8, date5_8_entry, month5_8_entry,year5_8_entry, spin5_E_8, spin5_F_8,
    spin5_A_9, spin5_B_9, spin5_C_9, spin5_D_9, var5_9, date5_9_entry, month5_9_entry,year5_9_entry, spin5_E_9, spin5_F_9,
    spin5_A_10, spin5_B_10, spin5_C_10, spin5_D_10, var5_10, date5_10_entry, month5_10_entry,year5_10_entry, spin5_E_10, spin5_F_10,
    spin5_A_11, spin5_B_11, spin5_C_11, spin5_D_11, var5_11, date5_11_entry, month5_11_entry,year5_11_entry, spin5_E_11, spin5_F_11,
    spin5_A_12, spin5_B_12, spin5_C_12, spin5_D_12, var5_12, date5_12_entry, month5_12_entry,year5_12_entry, spin5_E_12, spin5_F_12,
    spin6_A_1, spin6_B_1, spin6_C_1, spin6_D_1, var6_1, 0, 0,0, 0, 0,
    spin6_A_2, spin6_B_2, spin6_C_2, spin6_D_2, var6_2, date6_2_entry, month6_2_entry,year6_2_entry, spin6_E_2, spin6_F_2,
    spin6_A_3, spin6_B_3, spin6_C_3, spin6_D_3, var6_3, date6_3_entry, month6_3_entry,year6_3_entry, spin6_E_3, spin6_F_3,
    spin6_A_4, spin6_B_4, spin6_C_4, spin6_D_4, var6_4, date6_4_entry, month6_4_entry,year6_4_entry, spin6_E_4, spin6_F_4,
    spin6_A_5, spin6_B_5, spin6_C_5, spin6_D_5, var6_5, date6_5_entry, month6_5_entry,year6_5_entry, spin6_E_5, spin6_F_5,
    spin6_A_6, spin6_B_6, spin6_C_6, spin6_D_6, var6_6, date6_6_entry, month6_6_entry,year6_6_entry, spin6_E_6, spin6_F_6,
    spin6_A_7, spin6_B_7, spin6_C_7, spin6_D_7, var6_7, date6_7_entry, month6_7_entry,year6_7_entry, spin6_E_7, spin6_F_7,
    spin6_A_8, spin6_B_8, spin6_C_8, spin6_D_8, var6_8, date6_8_entry, month6_8_entry,year6_8_entry, spin6_E_8, spin6_F_8,
    spin6_A_9, spin6_B_9, spin6_C_9, spin6_D_9, var6_9, date6_9_entry, month6_9_entry,year6_9_entry, spin6_E_9, spin6_F_9,
    spin6_A_10, spin6_B_10, spin6_C_10, spin6_D_10, var6_10, date6_10_entry, month6_10_entry,year6_10_entry, spin6_E_10, spin6_F_10,
    spin6_A_11, spin6_B_11, spin6_C_11, spin6_D_11, var6_11, date6_11_entry, month6_11_entry,year6_11_entry, spin6_E_11, spin6_F_11,
    spin6_A_12, spin6_B_12, spin6_C_12, spin6_D_12, var6_12, date6_12_entry, month6_12_entry,year6_12_entry, spin6_E_12, spin6_F_12]

    input_mat = np.asarray(input_mat)

    input_mat = input_mat.reshape(6,12,10)

    #phaseLabels1
    #phaseLabel1_6

    phase_delimiters = [datetime.datetime.now()]

   
    getAllBoxSchedule()

    
    tab_control.pack(expand=1, fill='both')

    ### Main loop

    window.mainloop()