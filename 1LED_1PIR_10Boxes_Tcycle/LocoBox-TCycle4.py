import serial   # For Serial communication

import time     # Required for using delay functions

import datetime  # For date-time setting and timedelta calculations

import platform

import glob

import tkinter as tk

from tkinter import *  # import INIT set of tkinter library for GUI

from tkinter import ttk

from tkinter import messagebox

from tkinter.filedialog import askopenfilename

import json
import sys

try:

    from tkinter import filedialog

except ImportError:

    fileDialog = tk.filedialog

import threading  # To run Arduino loop and tkinter loop alongside

import serial.tools.list_ports  # For identifying Arduino port

#import numpy as np

#import pandas as pd


# Global variables

global starthour, startminute, startYear1_1, startMonth1_1, startdate1_1
global days1, days2, days3, days4, days5,days6, days7, days8, days9, days10,days11, days12, days13, days14, days15,days16, days17, days18, days19, days20
global t_cycle1, t_cycle2, t_cycle3, t_cycle4, t_cycle5,t_cycle6, t_cycle7, t_cycle8, t_cycle9, t_cycle10,t_cycle11, t_cycle12, t_cycle13, t_cycle14, t_cycle15,t_cycle16, t_cycle17, t_cycle18, t_cycle19, t_cycle20

global hourOn_1, minOn_1
global hourOn_2, minOn_2
global hourOn_3, minOn_3
global hourOn_4, minOn_4
global hourOn_5, minOn_5
global hourOn_6, minOn_6
global hourOn_7, minOn_7
global hourOn_8, minOn_8
global hourOn_9, minOn_9
global hourOn_10, minOn_10
global hourOn_11, minOn_11
global hourOn_12, minOn_12
global hourOn_13, minOn_13
global hourOn_14, minOn_14
global hourOn_15, minOn_15
global hourOn_16, minOn_16
global hourOn_17, minOn_17
global hourOn_18, minOn_18
global hourOn_19, minOn_19
global hourOn_20, minOn_20

global ratio_on_1, ratio_off_1
global ratio_on_2, ratio_off_2
global ratio_on_3, ratio_off_3
global ratio_on_4, ratio_off_4
global ratio_on_5, ratio_off_5
global ratio_on_6, ratio_off_6
global ratio_on_7, ratio_off_7
global ratio_on_8, ratio_off_8
global ratio_on_9, ratio_off_9
global ratio_on_10, ratio_off_10
global ratio_on_11, ratio_off_11
global ratio_on_12, ratio_off_12
global ratio_on_13, ratio_off_13
global ratio_on_14, ratio_off_14
global ratio_on_15, ratio_off_15
global ratio_on_16, ratio_off_16
global ratio_on_17, ratio_off_17
global ratio_on_18, ratio_off_18
global ratio_on_19, ratio_off_19
global ratio_on_20, ratio_off_20

global dark_1, light_1
global dark_2, light_2
global dark_3, light_3
global dark_4, light_4
global dark_5, light_5
global dark_6, light_6
global dark_7, light_7
global dark_8, light_8
global dark_9, light_9
global dark_10, light_10
global dark_11, light_11
global dark_12, light_12
global dark_13, light_13
global dark_14, light_14
global dark_15, light_15
global dark_16, light_16
global dark_17, light_17
global dark_18, light_18
global dark_19, light_19
global dark_20, light_20

global setBox


# Preset values

setBox = 0


# Version information


def about():

    return messagebox.showinfo('About',

                               '10-Box Schedule Setter\n' +

                               'LocoBox-TCycle.py\n\n' +

                               'Version 0.1.0\n' +

                               'Nov 19, 2018\n\n' +

                               'Jihwan Myung & Vuong Truong\n' +

                               'Laboratory of Braintime\n\n' +

                               'https://github.com/braintimelab/LocomotorBox')


# Define and create serial object function


def create_serial_obj(portPath, baud_rate, timeout):
    '''

    Given the port path, baud rate, creates

    and returns a pyserial object.

    '''

    return serial.Serial(portPath, baud_rate, timeout=timeout)


# Find open serial ports


def serial_ports():

    arduino_ports = [

        p.device

        for p in serial.tools.list_ports.comports()

        if 'Arduino' or 'Generic CDC' in p.description

    ]

    if sys.platform.startswith('win'):

        arduino_ports = ['COM%s' % (i + 1) for i in range(256)]

    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):

        # this excludes your current terminal '/dev/tty'

        arduino_ports = glob.glob('/dev/tty[A-Za-z]*')

    elif sys.platform.startswith('darwin'):

        arduino_ports = glob.glob('/dev/tty.*')

    else:

        raise EnvironmentError('Unsupported platform')

    result = []

    for port in arduino_ports:

        try:

            s = serial.Serial(port)

            s.close()

            result.append(port)

        except (OSError, serial.SerialException):

            pass

    return result

    # Classes


class StatusBar(Frame):  # scan open serial ports

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


# Initialize the windows size and name
window = Tk()

window.title('LocoBox (10-box)')

if sys.platform.startswith('win'):

    window.geometry('1000x770')

elif sys.platform.startswith('darwin'):

    window.geometry('1000x440')

elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):

    window.geometry('730x420')

else:

    window.geometry('1000x440')

status = StatusBar(window)


# Define functions


def destruct():  # Quit the program

    print('LocoBox ended.')

    window.quit()


def get_data(istate=0):  # Start recording

    status.pack(side='bottom', fill='x')

    status.set('Starting the recording...')

    for i in range(10):

        boxrec_text[i].set('Preparing for recording.')

    window.update_idletasks()

    i = istate

    counti = 0

    # init csv file and write the COM port name

    headers = port_entry.get()

    filename = filename_entry.get()

    with open(filename, 'w', encoding='utf-8') as w:

        w.write(headers+'\n')

    w.close()

    global serial_obj

    global dead

    # try:

    while True:

        string2 = serial_obj.readline().decode('utf-8')

        if string2 != '':

            with open(filename, 'a') as w:

                w.write(string2)

            w.close()

        print(string2)

        if i == 0:

            print('Synching time...')

            status.pack(side='bottom', fill='x')

            status.set('Synching time...')

            t = datetime.datetime.now()

            #serial_obj.write(str.encode(t.strftime('%Y-%m-%d %H:%M:%S')))

            serial_obj.write(str.encode(t.strftime('2018-12-08 23:00:00')))

        if i == 1:

            serial_obj.write(str.encode(starthour+startminute+startYear1_1 + startMonth1_1 + startdate1_1))

        if i == 2:

            serial_obj.write(str.encode(dark_1[0] + light_1[0] + dark_1[1] + light_1[1] + dark_1[2] + light_1[2] + dark_1[3] + light_1[3] + dark_1[4] + light_1[4] + dark_1[5] + light_1[5] +

                                        dark_1[6] + light_1[6] + dark_1[7] + light_1[7] + dark_1[8] + light_1[8] + dark_1[9] + light_1[9] +

                                        dark_2[0] + light_2[0] + dark_2[1] + light_2[1] + dark_2[2] + light_2[2] + dark_2[3] + light_2[3] + dark_2[4] + light_2[4] + dark_2[5] + light_2[5] +

                                        dark_2[6] + light_2[6] + dark_2[7] + light_2[7] + dark_2[8] + light_2[8] + dark_2[9] + light_2[9] +

                                        dark_3[0] + light_3[0] + dark_3[1] + light_3[1] + dark_3[2] + light_3[2] + dark_3[3] + light_3[3] + dark_3[4] + light_3[4] + dark_3[5] + light_3[5] +

                                        dark_3[6] + light_3[6] + dark_3[7] + light_3[7] + dark_3[8] + light_3[8] + dark_3[9] + light_3[9]))

        if i == 3:

            serial_obj.write(str.encode(hourOn_1[0] + minOn_1[0] + hourOn_1[1] + minOn_1[1] + hourOn_1[2] + minOn_1[2] + hourOn_1[3] + minOn_1[3] + hourOn_1[4] + minOn_1[4] +

                                        hourOn_1[5] + minOn_1[5] + hourOn_1[6] + minOn_1[6] + hourOn_1[7] + minOn_1[7] + hourOn_1[8] + minOn_1[8] + hourOn_1[9] + minOn_1[9] +

                                        ratio_on_1[0] + ratio_off_1[0] + ratio_on_1[1] + ratio_off_1[1] + ratio_on_1[2] + ratio_off_1[2] + ratio_on_1[3] + ratio_off_1[3] + ratio_on_1[4] + ratio_off_1[4]))

        if i == 4:

            serial_obj.write(str.encode(ratio_on_1[5]+ratio_off_1[5] + ratio_on_1[6] + ratio_off_1[6] + ratio_on_1[7] + ratio_off_1[7] + ratio_on_1[8] + ratio_off_1[8] + ratio_on_1[9] + ratio_off_1[9] +

                                        hourOn_2[0] + minOn_2[0] + hourOn_2[1] + minOn_2[1] + hourOn_2[2] + minOn_2[2] + hourOn_2[3] + minOn_2[3] + hourOn_2[4] + minOn_2[4] +

                                        hourOn_2[5] + minOn_2[5] + hourOn_2[6] + minOn_2[6] + hourOn_2[7] + minOn_2[7] + hourOn_2[8] + minOn_2[8] + hourOn_2[9] + minOn_2[9]))

        if i == 5:

            serial_obj.write(str.encode(ratio_on_2[0] + ratio_off_2[0] + ratio_on_2[1] + ratio_off_2[1] + ratio_on_2[2] + ratio_off_2[2] + ratio_on_2[3] + ratio_off_2[3] + ratio_on_2[4] + ratio_off_2[4] +

                                        ratio_on_2[5] + ratio_off_2[5] + ratio_on_2[6] + ratio_off_2[6] + ratio_on_2[7] + ratio_off_2[7] + ratio_on_2[8] + ratio_off_2[8] + ratio_on_2[9] + ratio_off_2[9] +

                                        hourOn_3[0] + minOn_3[0] + hourOn_3[1] + minOn_3[1] + hourOn_3[2] + minOn_3[2] + hourOn_3[3] + minOn_3[3] + hourOn_3[4] + minOn_3[4]))

        if i == 6:

            serial_obj.write(str.encode(hourOn_3[5] + minOn_3[5] + hourOn_3[6] + minOn_3[6] + hourOn_3[7] + minOn_3[7] + hourOn_3[8] + minOn_3[8] + hourOn_3[9] + minOn_3[9] +

                                        ratio_on_3[0] + ratio_off_3[0] + ratio_on_3[1] + ratio_off_3[1] + ratio_on_3[2] + ratio_off_3[2] + ratio_on_3[3] + ratio_off_3[3] + ratio_on_3[4] + ratio_off_3[4] +

                                        ratio_on_3[5] + ratio_off_3[5] + ratio_on_3[6] + ratio_off_3[6] + ratio_on_3[7] + ratio_off_3[7] + ratio_on_3[8] + ratio_off_3[8] + ratio_on_3[9] + ratio_off_3[9]))
        if i == 7:

            serial_obj.write(str.encode(dark_4[0] + light_4[0] + dark_4[1] + light_4[1] + dark_4[2] + light_4[2] + dark_4[3] + light_4[3] + dark_4[4] + light_4[4] + dark_4[5] + light_4[5] +

                                        dark_4[6] + light_4[6] + dark_4[7] + light_4[7] + dark_4[8] + light_4[8] + dark_4[9] + light_4[9] +

                                        dark_5[0] + light_5[0] + dark_5[1] + light_5[1] + dark_5[2] + light_5[2] + dark_5[3] + light_5[3] + dark_5[4] + light_5[4] + dark_5[5] + light_5[5] +

                                        dark_5[6] + light_5[6] + dark_5[7] + light_5[7] + dark_5[8] + light_5[8] + dark_5[9] + light_5[9] +

                                        dark_6[0] + light_6[0] + dark_6[1] + light_6[1] + dark_6[2] + light_6[2] + dark_6[3] + light_6[3] + dark_6[4] + light_6[4] + dark_6[5] + light_6[5] +

                                        dark_6[6] + light_6[6] + dark_6[7] + light_6[7] + dark_6[8] + light_6[8] + dark_6[9] + light_6[9]))
        if i == 8:

            serial_obj.write(str.encode(dark_7[0] + light_7[0] + dark_7[1] + light_7[1] + dark_7[2] + light_7[2] + dark_7[3] + light_7[3] + dark_7[4] + light_7[4] + dark_7[5] + light_7[5] +

                                        dark_7[6] + light_7[6] + dark_7[7] + light_7[7] + dark_7[8] + light_7[8] + dark_7[9] + light_7[9] +
                                        dark_8[0] + light_8[0] + dark_8[1] + light_8[1] + dark_8[2] + light_8[2] + dark_8[3] + light_8[3] + dark_8[4] + light_8[4] + dark_8[5] + light_8[5] +

                                        dark_8[6] + light_8[6] + dark_8[7] + light_8[7] + dark_8[8] + light_8[8] + dark_8[9] + light_8[9] +
                                        dark_9[0] + light_9[0] + dark_9[1] + light_9[1] + dark_9[2] + light_9[2] + dark_9[3] + light_9[3] + dark_9[4] + light_9[4] + dark_9[5] + light_9[5] +

                                        dark_9[6] + light_9[6] + dark_9[7] + light_9[7] + dark_9[8] + light_9[8] + dark_9[9] + light_9[9]))
        if i == 9:

            serial_obj.write(str.encode(dark_10[0] + light_10[0] + dark_10[1] + light_10[1] + dark_10[2] + light_10[2] + dark_10[3] + light_10[3] + dark_10[4] + light_10[4] + dark_10[5] + light_10[5] +

                                        dark_10[6] + light_10[6] + dark_10[7] + light_10[7] + dark_10[8] + light_10[8] + dark_10[9] + light_10[9] +
                                        dark_11[0] + light_11[0] + dark_11[1] + light_11[1] + dark_11[2] + light_11[2] + dark_11[3] + light_11[3] + dark_11[4] + light_11[4] + dark_11[5] + light_11[5] +

                                        dark_11[6] + light_11[6] + dark_11[7] + light_11[7] + dark_11[8] + light_11[8] + dark_11[9] + light_11[9] +
                                        dark_12[0] + light_12[0] + dark_12[1] + light_12[1] + dark_12[2] + light_12[2] + dark_12[3] + light_12[3] + dark_12[4] + light_12[4] + dark_12[5] + light_12[5] +

                                        dark_12[6] + light_12[6] + dark_12[7] + light_12[7] + dark_12[8] + light_12[8] + dark_12[9] + light_12[9]))
        if i == 10:

            serial_obj.write(str.encode(dark_13[0] + light_13[0] + dark_13[1] + light_13[1] + dark_13[2] + light_13[2] + dark_13[3] + light_13[3] + dark_13[4] + light_13[4] + dark_13[5] + light_13[5] +

                                        dark_13[6] + light_13[6] + dark_13[7] + light_13[7] + dark_13[8] + light_13[8] + dark_13[9] + light_13[9] +
                                        dark_14[0] + light_14[0] + dark_14[1] + light_14[1] + dark_14[2] + light_14[2] + dark_14[3] + light_14[3] + dark_14[4] + light_14[4] + dark_14[5] + light_14[5] +

                                        dark_14[6] + light_14[6] + dark_14[7] + light_14[7] + dark_14[8] + light_14[8] + dark_14[9] + light_14[9] +
                                        dark_15[0] + light_15[0] + dark_15[1] + light_15[1] + dark_15[2] + light_15[2] + dark_15[3] + light_15[3] + dark_15[4] + light_15[4] + dark_15[5] + light_15[5] +

                                        dark_15[6] + light_15[6] + dark_15[7] + light_15[7] + dark_15[8] + light_15[8] + dark_15[9] + light_15[9]))

        if i == 11:

            serial_obj.write(str.encode(dark_16[0] + light_16[0] + dark_16[1] + light_16[1] + dark_16[2] + light_16[2] + dark_16[3] + light_16[3] + dark_16[4] + light_16[4] + dark_16[5] + light_16[5] +

                                        dark_16[6] + light_16[6] + dark_16[7] + light_16[7] + dark_16[8] + light_16[8] + dark_16[9] + light_16[9] +
                                        dark_17[0] + light_17[0] + dark_17[1] + light_17[1] + dark_17[2] + light_17[2] + dark_17[3] + light_17[3] + dark_17[4] + light_17[4] + dark_17[5] + light_17[5] +

                                        dark_17[6] + light_17[6] + dark_17[7] + light_17[7] + dark_17[8] + light_17[8] + dark_17[9] + light_17[9] +
                                        dark_18[0] + light_18[0] + dark_18[1] + light_18[1] + dark_18[2] + light_18[2] + dark_18[3] + light_18[3] + dark_18[4] + light_18[4] + dark_18[5] + light_18[5] +

                                        dark_18[6] + light_18[6] + dark_18[7] + light_18[7] + dark_18[8] + light_18[8] + dark_18[9] + light_18[9]))

        if i == 12:
            serial_obj.write(str.encode(dark_19[0] + light_19[0] + dark_19[1] + light_19[1] + dark_19[2] + light_19[2] + dark_19[3] + light_19[3] + dark_19[4] + light_19[4] + dark_19[5] + light_19[5] +

                                        dark_19[6] + light_19[6] + dark_19[7] + light_19[7] + dark_19[8] + light_19[8] + dark_19[9] + light_19[9] +
                                        dark_20[0] + light_20[0] + dark_20[1] + light_20[1] + dark_20[2] + light_20[2] + dark_20[3] + light_20[3] + dark_20[4] + light_20[4] + dark_20[5] + light_20[5] +

                                        dark_20[6] + light_20[6] + dark_20[7] + light_20[7] + dark_20[8] + light_20[8] + dark_20[9] + light_20[9]))

        if i == 13:
            serial_obj.write(str.encode(hourOn_4[0] + minOn_4[0] + hourOn_4[1] + minOn_4[1] + hourOn_4[2] + minOn_4[2] + hourOn_4[3] + minOn_4[3] + hourOn_4[4] + minOn_4[4] +

                                        hourOn_4[5] + minOn_4[5] + hourOn_4[6] + minOn_4[6] + hourOn_4[7] + minOn_4[7] + hourOn_4[8] + minOn_4[8] + hourOn_4[9] + minOn_4[9] +

                                        ratio_on_4[0] + ratio_off_4[0] + ratio_on_4[1] + ratio_off_4[1] + ratio_on_4[2] + ratio_off_4[2] + ratio_on_4[3] + ratio_off_4[3] + ratio_on_4[4] + ratio_off_4[4]))

        if i == 14:
            serial_obj.write(str.encode(ratio_on_4[5] + ratio_off_4[5] + ratio_on_4[6] + ratio_off_4[6] + ratio_on_4[7] + ratio_off_4[7] + ratio_on_4[8] + ratio_off_4[8] + ratio_on_4[9] + ratio_off_4[9] +

                                        hourOn_5[0] + minOn_5[0] + hourOn_5[1] + minOn_5[1] + hourOn_5[2] + minOn_5[2] + hourOn_5[3] + minOn_5[3] + hourOn_5[4] + minOn_5[4] +

                                        hourOn_5[5] + minOn_5[5] + hourOn_5[6] + minOn_5[6] + hourOn_5[7] + minOn_5[7] + hourOn_5[8] + minOn_5[8] + hourOn_5[9] + minOn_5[9]))
        if i == 15:
            serial_obj.write(str.encode(ratio_on_5[0] + ratio_off_5[0] + ratio_on_5[1] + ratio_off_5[1] + ratio_on_5[2] + ratio_off_5[2] + ratio_on_5[3] + ratio_off_5[3] + ratio_on_5[4] + ratio_off_5[4] +

                                        ratio_on_5[5] + ratio_off_5[5] + ratio_on_5[6] + ratio_off_5[6] + ratio_on_5[7] + ratio_off_5[7] + ratio_on_5[8] + ratio_off_5[8] + ratio_on_5[9] + ratio_off_5[9] +

                                        hourOn_6[0] + minOn_6[0] + hourOn_6[1] + minOn_6[1] + hourOn_6[2] + minOn_6[2] + hourOn_6[3] + minOn_6[3] + hourOn_6[4] + minOn_6[4]))
        if i == 16:
            serial_obj.write(str.encode(hourOn_6[5] + minOn_6[5] + hourOn_6[6] + minOn_6[6] + hourOn_6[7] + minOn_6[7] + hourOn_6[8] + minOn_6[8] + hourOn_6[9] + minOn_6[9] +

                                        ratio_on_6[0] + ratio_off_6[0] + ratio_on_6[1] + ratio_off_6[1] + ratio_on_6[2] + ratio_off_6[2] + ratio_on_6[3] + ratio_off_6[3] + ratio_on_6[4] + ratio_off_6[4] +

                                        ratio_on_6[5] + ratio_off_6[5] + ratio_on_6[6] + ratio_off_6[6] + ratio_on_6[7] + ratio_off_6[7] + ratio_on_6[8] + ratio_off_6[8] + ratio_on_6[9] + ratio_off_6[9]))
        if i == 17:
            serial_obj.write(str.encode(hourOn_7[0] + minOn_7[0] + hourOn_7[1] + minOn_7[1] + hourOn_7[2] + minOn_7[2] + hourOn_7[3] + minOn_7[3] + hourOn_7[4] + minOn_7[4] +

                                        hourOn_7[5] + minOn_7[5] + hourOn_7[6] + minOn_7[6] + hourOn_7[7] + minOn_7[7] + hourOn_7[8] + minOn_7[8] + hourOn_7[9] + minOn_7[9] +

                                        ratio_on_7[0] + ratio_off_7[0] + ratio_on_7[1] + ratio_off_7[1] + ratio_on_7[2] + ratio_off_7[2] + ratio_on_7[3] + ratio_off_7[3] + ratio_on_7[4] + ratio_off_7[4]))
        if i == 18:
            serial_obj.write(str.encode(ratio_on_7[5] + ratio_off_7[5] + ratio_on_7[6] + ratio_off_7[6] + ratio_on_7[7] + ratio_off_7[7] + ratio_on_7[8] + ratio_off_7[8] + ratio_on_7[9] + ratio_off_7[9] +

                                        hourOn_8[0] + minOn_8[0] + hourOn_8[1] + minOn_8[1] + hourOn_8[2] + minOn_8[2] + hourOn_8[3] + minOn_8[3] + hourOn_8[4] + minOn_8[4] +

                                        hourOn_8[5] + minOn_8[5] + hourOn_8[6] + minOn_8[6] + hourOn_8[7] + minOn_8[7] + hourOn_8[8] + minOn_8[8] + hourOn_8[9] + minOn_8[9]))
        if i == 19:
            serial_obj.write(str.encode(ratio_on_8[0] + ratio_off_8[0] + ratio_on_8[1] + ratio_off_8[1] + ratio_on_8[2] + ratio_off_8[2] + ratio_on_8[3] + ratio_off_8[3] + ratio_on_8[4] + ratio_off_8[4] +

                                        ratio_on_8[5] + ratio_off_8[5] + ratio_on_8[6] + ratio_off_8[6] + ratio_on_8[7] + ratio_off_8[7] + ratio_on_8[8] + ratio_off_8[8] + ratio_on_8[9] + ratio_off_8[9] +

                                        hourOn_9[0] + minOn_9[0] + hourOn_9[1] + minOn_9[1] + hourOn_9[2] + minOn_9[2] + hourOn_9[3] + minOn_9[3] + hourOn_9[4] + minOn_9[4]))
        if i == 20:
            serial_obj.write(str.encode(hourOn_9[5] + minOn_9[5] + hourOn_9[6] + minOn_9[6] + hourOn_9[7] + minOn_9[7] + hourOn_9[8] + minOn_9[8] + hourOn_9[9] + minOn_9[9] +

                                        ratio_on_9[0] + ratio_off_9[0] + ratio_on_9[1] + ratio_off_9[1] + ratio_on_9[2] + ratio_off_9[2] + ratio_on_9[3] + ratio_off_9[3] + ratio_on_9[4] + ratio_off_9[4] +

                                        ratio_on_9[5] + ratio_off_9[5] + ratio_on_9[6] + ratio_off_9[6] + ratio_on_9[7] + ratio_off_9[7] + ratio_on_9[8] + ratio_off_9[8] + ratio_on_9[9] + ratio_off_9[9]))
        if i == 21:
            serial_obj.write(str.encode(hourOn_10[0] + minOn_10[0] + hourOn_10[1] + minOn_10[1] + hourOn_10[2] + minOn_10[2] + hourOn_10[3] + minOn_10[3] + hourOn_10[4] + minOn_10[4] +

                                        hourOn_10[5] + minOn_10[5] + hourOn_10[6] + minOn_10[6] + hourOn_10[7] + minOn_10[7] + hourOn_10[8] + minOn_10[8] + hourOn_10[9] + minOn_10[9] +

                                        ratio_on_10[0] + ratio_off_10[0] + ratio_on_10[1] + ratio_off_10[1] + ratio_on_10[2] + ratio_off_10[2] + ratio_on_10[3] + ratio_off_10[3] + ratio_on_10[4] + ratio_off_10[4]))
        if i == 22:
            serial_obj.write(str.encode(ratio_on_10[5] + ratio_off_10[5] + ratio_on_10[6] + ratio_off_10[6] + ratio_on_10[7] + ratio_off_10[7] + ratio_on_10[8] + ratio_off_10[8] + ratio_on_10[9] + ratio_off_10[9] +

                                        hourOn_11[0] + minOn_11[0] + hourOn_11[1] + minOn_11[1] + hourOn_11[2] + minOn_11[2] + hourOn_11[3] + minOn_11[3] + hourOn_11[4] + minOn_11[4] +

                                        hourOn_11[5] + minOn_11[5] + hourOn_11[6] + minOn_11[6] + hourOn_11[7] + minOn_11[7] + hourOn_11[8] + minOn_11[8] + hourOn_11[9] + minOn_11[9]))
        if i == 23:
            serial_obj.write(str.encode(ratio_on_11[0] + ratio_off_11[0] + ratio_on_11[1] + ratio_off_11[1] + ratio_on_11[2] + ratio_off_11[2] + ratio_on_11[3] + ratio_off_11[3] + ratio_on_11[4] + ratio_off_11[4] +

                                        ratio_on_11[5] + ratio_off_11[5] + ratio_on_11[6] + ratio_off_11[6] + ratio_on_11[7] + ratio_off_11[7] + ratio_on_11[8] + ratio_off_11[8] + ratio_on_11[9] + ratio_off_11[9] +

                                        hourOn_12[0] + minOn_12[0] + hourOn_12[1] + minOn_12[1] + hourOn_12[2] + minOn_12[2] + hourOn_12[3] + minOn_12[3] + hourOn_12[4] + minOn_12[4]))
        if i == 24:
            serial_obj.write(str.encode(hourOn_12[5] + minOn_12[5] + hourOn_12[6] + minOn_12[6] + hourOn_12[7] + minOn_12[7] + hourOn_12[8] + minOn_12[8] + hourOn_12[9] + minOn_12[9] +

                                        ratio_on_12[0] + ratio_off_12[0] + ratio_on_12[1] + ratio_off_12[1] + ratio_on_12[2] + ratio_off_12[2] + ratio_on_12[3] + ratio_off_12[3] + ratio_on_12[4] + ratio_off_12[4] +

                                        ratio_on_12[5] + ratio_off_12[5] + ratio_on_12[6] + ratio_off_12[6] + ratio_on_12[7] + ratio_off_12[7] + ratio_on_12[8] + ratio_off_12[8] + ratio_on_12[9] + ratio_off_12[9]))
        if i == 25:
            serial_obj.write(str.encode(hourOn_13[0] + minOn_13[0] + hourOn_13[1] + minOn_13[1] + hourOn_13[2] + minOn_13[2] + hourOn_13[3] + minOn_13[3] + hourOn_13[4] + minOn_13[4] +

                                        hourOn_13[5] + minOn_13[5] + hourOn_13[6] + minOn_13[6] + hourOn_13[7] + minOn_13[7] + hourOn_13[8] + minOn_13[8] + hourOn_13[9] + minOn_13[9] +

                                        ratio_on_13[0] + ratio_off_13[0] + ratio_on_13[1] + ratio_off_13[1] + ratio_on_13[2] + ratio_off_13[2] + ratio_on_13[3] + ratio_off_13[3] + ratio_on_13[4] + ratio_off_13[4]))
        if i == 26:
            serial_obj.write(str.encode(ratio_on_13[5] + ratio_off_13[5] + ratio_on_13[6] + ratio_off_13[6] + ratio_on_13[7] + ratio_off_13[7] + ratio_on_13[8] + ratio_off_13[8] + ratio_on_13[9] + ratio_off_13[9] +

                                        hourOn_14[0] + minOn_14[0] + hourOn_14[1] + minOn_14[1] + hourOn_14[2] + minOn_14[2] + hourOn_14[3] + minOn_14[3] + hourOn_14[4] + minOn_14[4] +

                                        hourOn_14[5] + minOn_14[5] + hourOn_14[6] + minOn_14[6] + hourOn_14[7] + minOn_14[7] + hourOn_14[8] + minOn_14[8] + hourOn_14[9] + minOn_14[9]))
        if i == 27:
            serial_obj.write(str.encode(ratio_on_14[0] + ratio_off_14[0] + ratio_on_14[1] + ratio_off_14[1] + ratio_on_14[2] + ratio_off_14[2] + ratio_on_14[3] + ratio_off_14[3] + ratio_on_14[4] + ratio_off_14[4] +

                                        ratio_on_14[5] + ratio_off_14[5] + ratio_on_14[6] + ratio_off_14[6] + ratio_on_14[7] + ratio_off_14[7] + ratio_on_14[8] + ratio_off_14[8] + ratio_on_14[9] + ratio_off_14[9] +

                                        hourOn_15[0] + minOn_15[0] + hourOn_15[1] + minOn_15[1] + hourOn_15[2] + minOn_15[2] + hourOn_15[3] + minOn_15[3] + hourOn_15[4] + minOn_15[4]))
        if i == 28:
            serial_obj.write(str.encode(hourOn_15[5] + minOn_15[5] + hourOn_15[6] + minOn_15[6] + hourOn_15[7] + minOn_15[7] + hourOn_15[8] + minOn_15[8] + hourOn_15[9] + minOn_15[9] +

                                        ratio_on_15[0] + ratio_off_15[0] + ratio_on_15[1] + ratio_off_15[1] + ratio_on_15[2] + ratio_off_15[2] + ratio_on_15[3] + ratio_off_15[3] + ratio_on_15[4] + ratio_off_15[4] +

                                        ratio_on_15[5] + ratio_off_15[5] + ratio_on_15[6] + ratio_off_15[6] + ratio_on_15[7] + ratio_off_15[7] + ratio_on_15[8] + ratio_off_15[8] + ratio_on_15[9] + ratio_off_15[9]))
        if i == 29:
            serial_obj.write(str.encode(hourOn_16[0] + minOn_16[0] + hourOn_16[1] + minOn_16[1] + hourOn_16[2] + minOn_16[2] + hourOn_16[3] + minOn_16[3] + hourOn_16[4] + minOn_16[4] +

                                        hourOn_16[5] + minOn_16[5] + hourOn_16[6] + minOn_16[6] + hourOn_16[7] + minOn_16[7] + hourOn_16[8] + minOn_16[8] + hourOn_16[9] + minOn_16[9] +

                                        ratio_on_16[0] + ratio_off_16[0] + ratio_on_16[1] + ratio_off_16[1] + ratio_on_16[2] + ratio_off_16[2] + ratio_on_16[3] + ratio_off_16[3] + ratio_on_16[4] + ratio_off_16[4]))
        if i == 30:
            serial_obj.write(str.encode(ratio_on_16[5] + ratio_off_16[5] + ratio_on_16[6] + ratio_off_16[6] + ratio_on_16[7] + ratio_off_16[7] + ratio_on_16[8] + ratio_off_16[8] + ratio_on_16[9] + ratio_off_16[9] +

                                        hourOn_17[0] + minOn_17[0] + hourOn_17[1] + minOn_17[1] + hourOn_17[2] + minOn_17[2] + hourOn_17[3] + minOn_17[3] + hourOn_17[4] + minOn_17[4] +

                                        hourOn_17[5] + minOn_17[5] + hourOn_17[6] + minOn_17[6] + hourOn_17[7] + minOn_17[7] + hourOn_17[8] + minOn_17[8] + hourOn_17[9] + minOn_17[9]))
        if i == 31:
            serial_obj.write(str.encode(ratio_on_17[0] + ratio_off_17[0] + ratio_on_17[1] + ratio_off_17[1] + ratio_on_17[2] + ratio_off_17[2] + ratio_on_17[3] + ratio_off_17[3] + ratio_on_17[4] + ratio_off_17[4] +

                                        ratio_on_17[5] + ratio_off_17[5] + ratio_on_17[6] + ratio_off_17[6] + ratio_on_17[7] + ratio_off_17[7] + ratio_on_17[8] + ratio_off_17[8] + ratio_on_17[9] + ratio_off_17[9] +

                                        hourOn_18[0] + minOn_18[0] + hourOn_18[1] + minOn_18[1] + hourOn_18[2] + minOn_18[2] + hourOn_18[3] + minOn_18[3] + hourOn_18[4] + minOn_18[4]))
        if i == 32:
            serial_obj.write(str.encode(hourOn_18[5] + minOn_18[5] + hourOn_18[6] + minOn_18[6] + hourOn_18[7] + minOn_18[7] + hourOn_18[8] + minOn_18[8] + hourOn_18[9] + minOn_18[9] +

                                        ratio_on_18[0] + ratio_off_18[0] + ratio_on_18[1] + ratio_off_18[1] + ratio_on_18[2] + ratio_off_18[2] + ratio_on_18[3] + ratio_off_18[3] + ratio_on_18[4] + ratio_off_18[4] +

                                        ratio_on_18[5] + ratio_off_18[5] + ratio_on_18[6] + ratio_off_18[6] + ratio_on_18[7] + ratio_off_18[7] + ratio_on_18[8] + ratio_off_18[8] + ratio_on_18[9] + ratio_off_18[9]))
        if i == 33:
            serial_obj.write(str.encode(hourOn_19[0] + minOn_19[0] + hourOn_19[1] + minOn_19[1] + hourOn_19[2] + minOn_19[2] + hourOn_19[3] + minOn_19[3] + hourOn_19[4] + minOn_19[4] +

                                        hourOn_19[5] + minOn_19[5] + hourOn_19[6] + minOn_19[6] + hourOn_19[7] + minOn_19[7] + hourOn_19[8] + minOn_19[8] + hourOn_19[9] + minOn_19[9] +

                                        ratio_on_19[0] + ratio_off_19[0] + ratio_on_19[1] + ratio_off_19[1] + ratio_on_19[2] + ratio_off_19[2] + ratio_on_19[3] + ratio_off_19[3] + ratio_on_19[4] + ratio_off_19[4]))
        if i == 34:
            serial_obj.write(str.encode(ratio_on_19[5] + ratio_off_19[5] + ratio_on_19[6] + ratio_off_19[6] + ratio_on_19[7] + ratio_off_19[7] + ratio_on_19[8] + ratio_off_19[8] + ratio_on_19[9] + ratio_off_19[9] +

                                        hourOn_20[0] + minOn_20[0] + hourOn_20[1] + minOn_20[1] + hourOn_20[2] + minOn_20[2] + hourOn_20[3] + minOn_20[3] + hourOn_20[4] + minOn_20[4] +

                                        hourOn_20[5] + minOn_20[5] + hourOn_20[6] + minOn_20[6] + hourOn_20[7] + minOn_20[7] + hourOn_20[8] + minOn_20[8] + hourOn_20[9] + minOn_20[9]))
        if i == 35:
            serial_obj.write(str.encode(ratio_on_20[0] + ratio_off_20[0] + ratio_on_20[1] + ratio_off_20[1] + ratio_on_20[2] + ratio_off_20[2] + ratio_on_20[3] + ratio_off_20[3] + ratio_on_20[4] + ratio_off_20[4] +

                                        ratio_on_20[5] + ratio_off_20[5] + ratio_on_20[6] + ratio_off_20[6] + ratio_on_20[7] + ratio_off_20[7] + ratio_on_20[8] + ratio_off_20[8] + ratio_on_20[9] + ratio_off_20[9]))
        if i == 36:
            serial_obj.write(str.encode(days1 + days2 + days3 + days4 + days5 +days6 + days7 + days8 + days9 + days10 +
                                        days11 + days12 + days13 + days14 + days15 +days16 + days17 + days18 + days19 + days20))
        if i == 37:
            serial_obj.write(str.encode(t_cycle1 + t_cycle2 + t_cycle3 + t_cycle4 + t_cycle5 +t_cycle6 +t_cycle7 + t_cycle8 + t_cycle9 +t_cycle10 +
                                        t_cycle11 + t_cycle12 + t_cycle13 + t_cycle14 + t_cycle15 +t_cycle16 +t_cycle17 + t_cycle18 + t_cycle19 +t_cycle20))


            status.pack(side='bottom', fill='x')

            status.set('All schedules transferred. Recording began.')

            for i in range(10):

                boxrec_text[i].set('Recording on-going.')

            window.update_idletasks()

        i = i+1

    # except:

    #     print('Stopped recording and disconnected from the boxes.')

    #     status.pack(side='bottom', fill='x')

    #     status.set('Stopped recording and disconnected from the boxes.')

    #     for i in range(10):

    #         boxrec_text[i].set('Recording stopped.')

    #     window.update_idletasks()


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

    t1 = threading.Thread(target=lambda: get_data(0))

    t1.daemon = True

    # inactivate Recording Start button

    btnRun['state'] = 'disabled'

    recordingmenu.entryconfig('Start new', state='disabled')

    # show_conf()

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

    for i in range(10):

        boxrec_text[i].set('Recording stopped.')

    window.update_idletasks()


def StartFrom():

    window.update_idletasks()


def getAllBoxSchedule():

    global starthour, startminute, startYear1_1, startMonth1_1, startdate1_1
    global days1, days2, days3, days4, days5,days6, days7, days8, days9, days10,days11, days12, days13, days14, days15,days16, days17, days18, days19, days20
    global t_cycle1, t_cycle2, t_cycle3, t_cycle4, t_cycle5,t_cycle6, t_cycle7, t_cycle8, t_cycle9, t_cycle10,t_cycle11, t_cycle12, t_cycle13, t_cycle14, t_cycle15,t_cycle16, t_cycle17, t_cycle18, t_cycle19, t_cycle20


    global hourOn_1, minOn_1
    global hourOn_2, minOn_2
    global hourOn_3, minOn_3
    global hourOn_4, minOn_4
    global hourOn_5, minOn_5
    global hourOn_6, minOn_6
    global hourOn_7, minOn_7
    global hourOn_8, minOn_8
    global hourOn_9, minOn_9
    global hourOn_10, minOn_10
    global hourOn_11, minOn_11
    global hourOn_12, minOn_12
    global hourOn_13, minOn_13
    global hourOn_14, minOn_14
    global hourOn_15, minOn_15
    global hourOn_16, minOn_16
    global hourOn_17, minOn_17
    global hourOn_18, minOn_18
    global hourOn_19, minOn_19
    global hourOn_20, minOn_20

    global ratio_on_1, ratio_off_1
    global ratio_on_2, ratio_off_2
    global ratio_on_3, ratio_off_3
    global ratio_on_4, ratio_off_4
    global ratio_on_5, ratio_off_5
    global ratio_on_6, ratio_off_6
    global ratio_on_7, ratio_off_7
    global ratio_on_8, ratio_off_8
    global ratio_on_9, ratio_off_9
    global ratio_on_10, ratio_off_10
    global ratio_on_11, ratio_off_11
    global ratio_on_12, ratio_off_12
    global ratio_on_13, ratio_off_13
    global ratio_on_14, ratio_off_14
    global ratio_on_15, ratio_off_15
    global ratio_on_16, ratio_off_16
    global ratio_on_17, ratio_off_17
    global ratio_on_18, ratio_off_18
    global ratio_on_19, ratio_off_19
    global ratio_on_20, ratio_off_20

    global dark_1, light_1
    global dark_2, light_2
    global dark_3, light_3
    global dark_4, light_4
    global dark_5, light_5
    global dark_6, light_6
    global dark_7, light_7
    global dark_8, light_8
    global dark_9, light_9
    global dark_10, light_10
    global dark_11, light_11
    global dark_12, light_12
    global dark_13, light_13
    global dark_14, light_14
    global dark_15, light_15
    global dark_16, light_16
    global dark_17, light_17
    global dark_18, light_18
    global dark_19, light_19
    global dark_20, light_20

    hourOn_1 = []
    minOn_1 = []
    hourOn_2 = []
    minOn_2 = []
    hourOn_3 = []
    minOn_3 = []
    hourOn_4 = []
    minOn_4 = []
    hourOn_5 = []
    minOn_5 = []
    hourOn_6 = []
    minOn_6 = []
    hourOn_7 = []
    minOn_7 = []
    hourOn_8 = []
    minOn_8 = []
    hourOn_9 = []
    minOn_9 = []
    hourOn_10 = []
    minOn_10 = []
    hourOn_11 = []
    minOn_11 = []
    hourOn_12 = []
    minOn_12 = []
    hourOn_13 = []
    minOn_13 = []
    hourOn_14 = []
    minOn_14 = []
    hourOn_15 = []
    minOn_15 = []
    hourOn_16 = []
    minOn_16 = []
    hourOn_17 = []
    minOn_17 = []
    hourOn_18 = []
    minOn_18 = []
    hourOn_19 = []
    minOn_19 = []
    hourOn_20 = []
    minOn_20 = []

    ratio_on_1 = []
    ratio_off_1 = []
    ratio_on_2 = []
    ratio_off_2 = []
    ratio_on_3 = []
    ratio_off_3 = []
    ratio_on_4 = []
    ratio_off_4 = []
    ratio_on_5 = []
    ratio_off_5 = []
    ratio_on_6 = []
    ratio_off_6 = []
    ratio_on_7 = []
    ratio_off_7 = []
    ratio_on_8 = []
    ratio_off_8 = []
    ratio_on_9 = []
    ratio_off_9 = []
    ratio_on_10 = []
    ratio_off_10 = []
    ratio_on_11 = []
    ratio_off_11 = []
    ratio_on_12 = []
    ratio_off_12 = []
    ratio_on_13 = []
    ratio_off_13 = []
    ratio_on_14 = []
    ratio_off_14 = []
    ratio_on_15 = []
    ratio_off_15 = []
    ratio_on_16 = []
    ratio_off_16 = []
    ratio_on_17 = []
    ratio_off_17 = []
    ratio_on_18 = []
    ratio_off_18 = []
    ratio_on_19 = []
    ratio_off_19 = []
    ratio_on_20 = []
    ratio_off_20 = []

    dark_1 = []
    light_1 = []
    dark_2 = []
    light_2 = []
    dark_3 = []
    light_3 = []
    dark_4 = []
    light_4 = []
    dark_5 = []
    light_5 = []
    dark_6 = []
    light_6 = []
    dark_7 = []
    light_7 = []
    dark_8 = []
    light_8 = []
    dark_9 = []
    light_9 = []
    dark_10 = []
    light_10 = []
    dark_11 = []
    light_11 = []
    dark_12 = []
    light_12 = []
    dark_13 = []
    light_13 = []
    dark_14 = []
    light_14 = []
    dark_15 = []
    light_15 = []
    dark_16 = []
    light_16 = []
    dark_17 = []
    light_17 = []
    dark_18 = []
    light_18 = []
    dark_19 = []
    light_19 = []
    dark_20 = []
    light_20 = []

    starthour = spin0_1.get()

    startminute = spin0_2.get()

    startYear1_1 = year0_entry.get()

    startMonth1_1 = month0_entry.get()

    startdate1_1 = date0_entry.get()


    days1 = spin1_6.get()
    days2 = spin1_7.get()
    days3 = spin1_8.get()
    days4 = spin1_9.get()
    days5 = spin1_10.get()
    days6 = spin1_11.get()
    days7 = spin1_12.get()
    days8 = spin1_13.get()
    days9 = spin1_14.get()
    days10 = spin1_15.get()
    days11 = spin1_16.get()
    days12 = spin1_17.get()
    days13 = spin1_18.get()
    days14 = spin1_19.get()
    days15 = spin1_20.get()
    days16 = spin1_21.get()
    days17 = spin1_22.get()
    days18 = spin1_23.get()
    days19 = spin1_24.get()
    days20 = spin1_25.get()


    t_cycle1 = spin0_3.get()
    t_cycle2 = spin0_4.get()
    t_cycle3 = spin0_5.get()
    t_cycle4 = spin0_6.get()
    t_cycle5 = spin0_7.get()
    t_cycle6 = spin0_8.get()
    t_cycle7 = spin0_9.get()
    t_cycle8 = spin0_10.get()
    t_cycle9 = spin0_11.get()
    t_cycle10 = spin0_12.get()
    t_cycle11 = spin0_13.get()
    t_cycle12 = spin0_14.get()
    t_cycle13 = spin0_15.get()
    t_cycle14 = spin0_16.get()
    t_cycle15 = spin0_17.get()
    t_cycle16 = spin0_18.get()
    t_cycle17 = spin0_19.get()
    t_cycle18 = spin0_20.get()
    t_cycle19 = spin0_21.get()
    t_cycle20 = spin0_22.get()


    setBox = 0

    for i in range(10):

        hourOn_1.append(spin_A_1[i].get())

        minOn_1.append(spin_B_1[i].get())

        ratio_on_1.append(spin_C_1[i].get())

        ratio_off_1.append(spin_D_1[i].get())

        if var_1[i].get() == 1:

            dark_1.append('0')

            light_1.append('0')

        if var_1[i].get() == 2:

            dark_1.append('1')

            light_1.append('0')

        if var_1[i].get() == 3:

            dark_1.append('0')

            light_1.append('1')

        hourOn_2.append(spin_A_2[i].get())

        minOn_2.append(spin_B_2[i].get())

        ratio_on_2.append(spin_C_2[i].get())

        ratio_off_2.append(spin_D_2[i].get())

        if var_2[i].get() == 1:

            dark_2.append('0')

            light_2.append('0')

        if var_2[i].get() == 2:

            dark_2.append('1')

            light_2.append('0')

        if var_2[i].get() == 3:

            dark_2.append('0')

            light_2.append('1')

        hourOn_3.append(spin_A_3[i].get())

        minOn_3.append(spin_B_3[i].get())

        ratio_on_3.append(spin_C_3[i].get())

        ratio_off_3.append(spin_D_3[i].get())

        if var_3[i].get() == 1:

            dark_3.append('0')

            light_3.append('0')

        if var_3[i].get() == 2:

            dark_3.append('1')

            light_3.append('0')

        if var_3[i].get() == 3:

            dark_3.append('0')

            light_3.append('1')

        hourOn_4.append(spin_A_4[i].get())

        minOn_4.append(spin_B_4[i].get())

        ratio_on_4.append(spin_C_4[i].get())

        ratio_off_4.append(spin_D_4[i].get())

        if var_4[i].get() == 1:

                dark_4.append('0')

                light_4.append('0')

        if var_4[i].get() == 2:

                dark_4.append('1')

                light_4.append('0')

        if var_4[i].get() == 3:

                dark_4.append('0')

                light_4.append('1')

        hourOn_5.append(spin_A_5[i].get())

        minOn_5.append(spin_B_5[i].get())

        ratio_on_5.append(spin_C_5[i].get())

        ratio_off_5.append(spin_D_5[i].get())

        if var_5[i].get() == 1:

                dark_5.append('0')

                light_5.append('0')

        if var_5[i].get() == 2:

                dark_5.append('1')

                light_5.append('0')

        if var_5[i].get() == 3:

                dark_5.append('0')

                light_5.append('1')
        hourOn_6.append(spin_A_6[i].get())

        minOn_6.append(spin_B_6[i].get())

        ratio_on_6.append(spin_C_6[i].get())

        ratio_off_6.append(spin_D_6[i].get())

        if var_6[i].get() == 1:

                dark_6.append('0')

                light_6.append('0')

        if var_6[i].get() == 2:

                dark_6.append('1')

                light_6.append('0')

        if var_6[i].get() == 3:

                dark_6.append('0')

                light_6.append('1')
        hourOn_7.append(spin_A_7[i].get())

        minOn_7.append(spin_B_7[i].get())

        ratio_on_7.append(spin_C_7[i].get())

        ratio_off_7.append(spin_D_7[i].get())

        if var_7[i].get() == 1:

                dark_7.append('0')

                light_7.append('0')

        if var_7[i].get() == 2:

                dark_7.append('1')

                light_7.append('0')

        if var_7[i].get() == 3:

                dark_7.append('0')

                light_7.append('1')
        hourOn_8.append(spin_A_8[i].get())

        minOn_8.append(spin_B_8[i].get())

        ratio_on_8.append(spin_C_8[i].get())

        ratio_off_8.append(spin_D_8[i].get())

        if var_8[i].get() == 1:

                dark_8.append('0')

                light_8.append('0')

        if var_8[i].get() == 2:

                dark_8.append('1')

                light_8.append('0')

        if var_8[i].get() == 3:

                dark_8.append('0')

                light_8.append('1')
        hourOn_9.append(spin_A_9[i].get())

        minOn_9.append(spin_B_9[i].get())

        ratio_on_9.append(spin_C_9[i].get())

        ratio_off_9.append(spin_D_9[i].get())

        if var_9[i].get() == 1:

                dark_9.append('0')

                light_9.append('0')

        if var_9[i].get() == 2:

                dark_9.append('1')

                light_9.append('0')

        if var_9[i].get() == 3:

                dark_9.append('0')

                light_9.append('1')
        hourOn_10.append(spin_A_10[i].get())

        minOn_10.append(spin_B_10[i].get())

        ratio_on_10.append(spin_C_10[i].get())

        ratio_off_10.append(spin_D_10[i].get())

        if var_10[i].get() == 1:

                dark_10.append('0')

                light_10.append('0')

        if var_10[i].get() == 2:

                dark_10.append('1')

                light_10.append('0')

        if var_10[i].get() == 3:

                dark_10.append('0')

                light_10.append('1')
        hourOn_11.append(spin_A_11[i].get())

        minOn_11.append(spin_B_11[i].get())

        ratio_on_11.append(spin_C_11[i].get())

        ratio_off_11.append(spin_D_11[i].get())

        if var_11[i].get() == 1:

                dark_11.append('0')

                light_11.append('0')

        if var_11[i].get() == 2:

                dark_11.append('1')

                light_11.append('0')

        if var_11[i].get() == 3:

                dark_11.append('0')

                light_11.append('1')
        hourOn_12.append(spin_A_12[i].get())

        minOn_12.append(spin_B_12[i].get())

        ratio_on_12.append(spin_C_12[i].get())

        ratio_off_12.append(spin_D_12[i].get())

        if var_12[i].get() == 1:

                dark_12.append('0')

                light_12.append('0')

        if var_12[i].get() == 2:

                dark_12.append('1')

                light_12.append('0')

        if var_12[i].get() == 3:

                dark_12.append('0')

                light_12.append('1')
        hourOn_13.append(spin_A_13[i].get())

        minOn_13.append(spin_B_13[i].get())

        ratio_on_13.append(spin_C_13[i].get())

        ratio_off_13.append(spin_D_13[i].get())

        if var_13[i].get() == 1:

                dark_13.append('0')

                light_13.append('0')

        if var_13[i].get() == 2:

                dark_13.append('1')

                light_13.append('0')

        if var_13[i].get() == 3:

                dark_13.append('0')

                light_13.append('1')
        hourOn_14.append(spin_A_14[i].get())

        minOn_14.append(spin_B_14[i].get())

        ratio_on_14.append(spin_C_14[i].get())

        ratio_off_14.append(spin_D_14[i].get())

        if var_14[i].get() == 1:

                dark_14.append('0')

                light_14.append('0')

        if var_14[i].get() == 2:

                dark_14.append('1')

                light_14.append('0')

        if var_14[i].get() == 3:

                dark_14.append('0')

                light_14.append('1')
        hourOn_15.append(spin_A_15[i].get())

        minOn_15.append(spin_B_15[i].get())

        ratio_on_15.append(spin_C_15[i].get())

        ratio_off_15.append(spin_D_15[i].get())

        if var_15[i].get() == 1:

                dark_15.append('0')

                light_15.append('0')

        if var_15[i].get() == 2:

                dark_15.append('1')

                light_15.append('0')

        if var_15[i].get() == 3:

                dark_15.append('0')

                light_15.append('1')
        hourOn_16.append(spin_A_16[i].get())

        minOn_16.append(spin_B_16[i].get())

        ratio_on_16.append(spin_C_16[i].get())

        ratio_off_16.append(spin_D_16[i].get())

        if var_16[i].get() == 1:

                dark_16.append('0')

                light_16.append('0')

        if var_16[i].get() == 2:

                dark_16.append('1')

                light_16.append('0')

        if var_16[i].get() == 3:

                dark_16.append('0')

                light_16.append('1')
        hourOn_17.append(spin_A_17[i].get())

        minOn_17.append(spin_B_17[i].get())

        ratio_on_17.append(spin_C_17[i].get())

        ratio_off_17.append(spin_D_17[i].get())

        if var_17[i].get() == 1:

                dark_17.append('0')

                light_17.append('0')

        if var_17[i].get() == 2:

                dark_17.append('1')

                light_17.append('0')

        if var_17[i].get() == 3:

                dark_17.append('0')

                light_17.append('1')
        hourOn_18.append(spin_A_18[i].get())

        minOn_18.append(spin_B_18[i].get())

        ratio_on_18.append(spin_C_18[i].get())

        ratio_off_18.append(spin_D_18[i].get())

        if var_18[i].get() == 1:

                dark_18.append('0')

                light_18.append('0')

        if var_18[i].get() == 2:

                dark_18.append('1')

                light_18.append('0')

        if var_18[i].get() == 3:

                dark_18.append('0')

                light_18.append('1')
        hourOn_19.append(spin_A_19[i].get())

        minOn_19.append(spin_B_19[i].get())

        ratio_on_19.append(spin_C_19[i].get())

        ratio_off_19.append(spin_D_19[i].get())

        if var_19[i].get() == 1:

                dark_19.append('0')

                light_19.append('0')

        if var_19[i].get() == 2:

                dark_19.append('1')

                light_19.append('0')

        if var_19[i].get() == 3:

                dark_19.append('0')

                light_19.append('1')
        hourOn_20.append(spin_A_20[i].get())

        minOn_20.append(spin_B_20[i].get())

        ratio_on_20.append(spin_C_20[i].get())

        ratio_off_20.append(spin_D_20[i].get())

        if var_20[i].get() == 1:

                dark_20.append('0')

                light_20.append('0')

        if var_20[i].get() == 2:

                dark_20.append('1')

                light_20.append('0')

        if var_20[i].get() == 3:

                dark_20.append('0')

                light_20.append('1')

        setBox = setBox+1

    status.pack(side='bottom', fill='x')

    status.set('Schedules for all boxes are set.')

    # show_conf()

    btnSave['state'] = 'normal'

    btnRun['state'] = 'normal'

    recordingmenu.entryconfig('Start new', state='normal')

    window.update_idletasks()


if __name__ == '__main__':

    #### All of the components and their positions in the GUI ####

    # You can change the design from here #

    menu = Menu(window)  # define menu

    # Define Var to keep track of the schedule

    # 1 for LD

    # 2 for DD

    # 3 for LL

    var_1 = [IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(
        value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1)]
    var_2 = [IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(
        value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1)]
    var_3 = [IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(
        value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1)]
    var_4 = [IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(
        value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1)]
    var_5 = [IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(
        value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1)]
    var_6 = [IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(
        value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1)]
    var_7 = [IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(
        value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1)]
    var_8 = [IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(
        value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1)]
    var_9 = [IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(
        value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1)]
    var_10 = [IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(
        value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1)]
    var_11 = [IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(
        value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1)]
    var_12 = [IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(
        value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1)]
    var_13 = [IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(
        value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1)]
    var_14 = [IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(
        value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1)]
    var_15 = [IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(
        value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1)]
    var_16 = [IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(
        value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1)]
    var_17 = [IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(
        value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1)]
    var_18 = [IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(
        value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1)]
    var_19 = [IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(
        value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1)]
    var_20 = [IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(
        value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1)]

    # Create file menu

    filemenu = Menu(menu)

    filemenu.add_command(label='Load schedules')

    filemenu.add_command(label='Save schedules')

    filemenu.add_separator()

    filemenu.add_command(label='Quit', command=destruct)

    menu.add_cascade(label='File', menu=filemenu)

    # create setting menu

    settingmenu = Menu(menu)

    settingmenu.add_command(label='Set all boxes', command=getAllBoxSchedule)

    settingmenu.add_command(label='Show schedule')

    menu.add_cascade(label='Setting', menu=settingmenu)

    # create recording menu

    recordingmenu = Menu(menu)

    recordingmenu.add_command(label='Start new', command=connect)

    recordingmenu.entryconfig('Start new', state='disabled')

    #recordingmenu.add_command(label='Start revised', command=lambda:get_data(1))

    recordingmenu.add_separator()

    recordingmenu.add_command(label='Stop', command=disconnect)

    menu.add_cascade(label='Recording', menu=recordingmenu)

    # create About menu

    aboutmenu = Menu(menu)

    aboutmenu.add_command(label='About LocoBox', command=about)

    menu.add_cascade(label='Help', menu=aboutmenu)

    window.config(menu=menu)

    tab_control = ttk.Notebook(window)

    tab0 = ttk.Frame(tab_control)

    tab_control.add(tab0, text='All boxes: cycle lentgh')

    tab = []

    for i in range(10):

        tab1 = ttk.Frame(tab_control)

        tab.append(tab1)

        tab_control.add(tab[i], text='Box%s' % str(i+1))

    tab11 = ttk.Frame(tab_control)

    tab_control.add(tab11, text='Schedules')

    # Display all available serial ports

    # openPorts=serial_ports()

    ports = list(serial.tools.list_ports.comports())

    for p in ports:

        print(p)

    openPorts = p.device

    #if len(np.shape(openPorts)) == 0:

        #openPorts = [openPorts]

    status.pack(side='bottom', fill='x')

    status.set('Available ports: '+', '.join(map(str, openPorts)))

    # Entry for Port, Baud, timeout, filename to save

    port = Label(tab0, text='Port').place(x=40, y=320)
    #port = Label(tab0, text='Port').place(x=565, y=320)

    baud = Label(tab0, text='Baud rate').place(x=363, y=320)
    #baud = Label(text='Baud rate').place(x=888, y=320)

    timeout = Label(tab0, text='Time out').place(x=565, y=320)
    #timeout = Label(text='Time out').place(x=1090, y=320)

    filename = Label(tab0, text='File').place(x=40, y=360)
    #filename = Label(text='File').place(x=565, y=360)

    configfilename = Label(tab0, text='Schedule').place(x=363, y=360)
    #configfilename = Label(text='Schedule').place(x=888, y=360)

    port_entry = Spinbox(tab0, values=openPorts, width=25)

    port_entry.delete(0, 'end')

    port_entry.insert(0, openPorts[0])  # first port is the default

    port_entry.place(x=80, y=320)
    #port_entry.place(x=605, y=320)

    baud_entry = Spinbox(tab0, values=(300, 600, 1200, 2400, 4800,

                                       9600, 14400, 19200, 28800, 38400, 57600, 115200), width=7)

    baud_entry.delete(0, 'end')

    baud_entry.insert(0, '9600')

    baud_entry.place(x=440, y=320)
    #baud_entry.place(x=965, y=320)

    timeout_entry = Entry(tab0, width=4)

    timeout_entry.place(x=635, y=320)
    #timeout_entry.place(x=1160, y=320)

    timeout_entry.insert(0, '10')

    filename_entry = Entry(tab0, width=25)

    filename_entry.place(x=80, y=360)
    #filename_entry.place(x=605, y=360)

    # predefine a default filename with ISO date

    date_string = time.strftime('%Y%m%d')

    filename_entry.insert(0, 'BOX1-Tcycle-'+date_string+'.txt')

    configfilename_entry = Entry(tab0, width=25)

    configfilename_entry.place(x=440, y=360)

    configfilename_entry.insert(0, 'BOX1-sched-Tcycle-'+date_string+'.json')

    btnSave = Button(tab0, text=' Save ', state='disabled')

    btnRun = Button(tab0, text=' Recording Start ',

                    command=connect, state='disabled')

    # if box settings of all 10 boxes are done, activate save and run buttons

    if setBox == 10:

        btnSave['state'] = 'normal'

        btnRun['state'] = 'normal'

        recordingmenu.entryconfig('Start new', state='normal')

        # show_conf()

        window.update_idletasks()

    # button positions change depending on OS

    if sys.platform.startswith('win'):

        btnSave.place(x=610, y=360)

        btnRun.place(x=660, y=360)

    elif sys.platform.startswith('darwin'):

        btnSave.place(x=685, y=360)

        btnRun.place(x=745, y=360)

    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):

        btnSave.place(x=610, y=360)

        btnRun.place(x=660, y=360)

    else:

        btnSave.place(x=685, y=360)

        btnRun.place(x=745, y=360)

    row_adj = 3  # useful when a new row is added above

    # T-cycle for all boxes

    fromLabel0 = Label(tab0, text='Start from')

    space0 = Label(tab0, text='  ')

    spin0_1 = Spinbox(tab0, from_=00, to=24, width=3, format='%02.0f')

    spin0_2 = Spinbox(tab0, from_=00, to=24, width=3, format='%02.0f')

    spin0_1.delete(0, 'end')

    spin0_1.insert(0, '07')

    spin0_2.delete(0, 'end')

    spin0_2.insert(0, '00')

    label0_h0 = Label(tab0, text=':')

    date0_entry = Spinbox(tab0, from_=00, to=31, width=3, format='%02.0f')

    month0_entry = Spinbox(tab0, from_=00, to=12, width=3, format='%02.0f')

    year0_entry = Spinbox(tab0, from_=2018, to=2030, width=5)

    # btnFrom = Button(text=' Set ', command='StartFrom', state='disabled')

    # btnFrom['state'] = 'normal'

    # btnFrom.place(x=470, y=41)

    window.update_idletasks()

    # calculate dates automatically for phase 1

    today = datetime.date.today()

    date0_entry.delete(0, 'end')

    date0_entry.insert(0, '{:02d}'.format(today.day))

    month0_entry.delete(0, 'end')

    month0_entry.insert(0, '{:02d}'.format(today.month))

    year0_entry.delete(0, 'end')

    year0_entry.insert(0, today.year)  # ISO format is YYYY/MM/DD

    label0_d_0 = Label(tab0, text='/')

    label0_m_0 = Label(tab0, text='/')

    spin0_3 = Spinbox(tab0, from_=00, to=24, width=3, format='%02.0f')
    spin0_3.delete(0, 'end')
    spin0_3.insert(0, '24')
    spin0_4 = Spinbox(tab0, from_=00, to=24, width=3, format='%02.0f')
    spin0_4.delete(0, 'end')
    spin0_4.insert(0, '24')
    spin0_5 = Spinbox(tab0, from_=00, to=24, width=3, format='%02.0f')
    spin0_5.delete(0, 'end')
    spin0_5.insert(0, '25')
    spin0_6 = Spinbox(tab0, from_=00, to=24, width=3, format='%02.0f')
    spin0_6.delete(0, 'end')
    spin0_6.insert(0, '26')
    spin0_7 = Spinbox(tab0, from_=00, to=24, width=3, format='%02.0f')
    spin0_7.delete(0, 'end')
    spin0_7.insert(0, '27')
    spin0_8 = Spinbox(tab0, from_=00, to=24, width=3, format='%02.0f')
    spin0_8.delete(0, 'end')
    spin0_8.insert(0, '28')
    spin0_9 = Spinbox(tab0, from_=00, to=24, width=3, format='%02.0f')
    spin0_9.delete(0, 'end')
    spin0_9.insert(0, '29')
    spin0_10 = Spinbox(tab0, from_=00, to=24, width=3, format='%02.0f')
    spin0_10.delete(0, 'end')
    spin0_10.insert(0, '30')
    spin0_11 = Spinbox(tab0, from_=00, to=24, width=3, format='%02.0f')
    spin0_11.delete(0, 'end')
    spin0_11.insert(0, '31')
    spin0_12 = Spinbox(tab0, from_=00, to=24, width=3, format='%02.0f')
    spin0_12.delete(0, 'end')
    spin0_12.insert(0, '32')

    spin0_13 = Spinbox(tab0, from_=00, to=24, width=3, format='%02.0f')
    spin0_13.delete(0, 'end')
    spin0_13.insert(0, '33')
    spin0_14 = Spinbox(tab0, from_=00, to=24, width=3, format='%02.0f')
    spin0_14.delete(0, 'end')
    spin0_14.insert(0, '34')
    spin0_15 = Spinbox(tab0, from_=00, to=24, width=3, format='%02.0f')
    spin0_15.delete(0, 'end')
    spin0_15.insert(0, '35')
    spin0_16 = Spinbox(tab0, from_=00, to=24, width=3, format='%02.0f')
    spin0_16.delete(0, 'end')
    spin0_16.insert(0, '36')
    spin0_17 = Spinbox(tab0, from_=00, to=24, width=3, format='%02.0f')
    spin0_17.delete(0, 'end')
    spin0_17.insert(0, '24')
    spin0_18 = Spinbox(tab0, from_=00, to=24, width=3, format='%02.0f')
    spin0_18.delete(0, 'end')
    spin0_18.insert(0, '24')
    spin0_19 = Spinbox(tab0, from_=00, to=24, width=3, format='%02.0f')
    spin0_19.delete(0, 'end')
    spin0_19.insert(0, '24')
    spin0_20 = Spinbox(tab0, from_=00, to=24, width=3, format='%02.0f')
    spin0_20.delete(0, 'end')
    spin0_20.insert(0, '24')
    spin0_21 = Spinbox(tab0, from_=00, to=24, width=3, format='%02.0f')
    spin0_21.delete(0, 'end')
    spin0_21.insert(0, '24')
    spin0_22 = Spinbox(tab0, from_=00, to=24, width=3, format='%02.0f')
    spin0_22.delete(0, 'end')
    spin0_22.insert(0, '24')


    spin1_6 = Spinbox(tab0, from_=00, to=999, width=4, format='%02.0f')
    spin1_6.delete(0, 'end')
    spin1_6.insert(0, '02')
    spin1_7 = Spinbox(tab0, from_=00, to=999, width=4, format='%02.0f')
    spin1_7.delete(0, 'end')
    spin1_7.insert(0, '14')
    spin1_8 = Spinbox(tab0, from_=00, to=999, width=4, format='%02.0f')
    spin1_8.delete(0, 'end')
    spin1_8.insert(0, '02')
    spin1_9 = Spinbox(tab0, from_=00, to=999, width=4, format='%02.0f')
    spin1_9.delete(0, 'end')
    spin1_9.insert(0, '02')
    spin1_10 = Spinbox(tab0, from_=00, to=999, width=4, format='%02.0f')
    spin1_10.delete(0, 'end')
    spin1_10.insert(0, '02')
    spin1_11 = Spinbox(tab0, from_=00, to=999, width=4, format='%02.0f')
    spin1_11.delete(0, 'end')
    spin1_11.insert(0, '02')
    spin1_12 = Spinbox(tab0, from_=00, to=999, width=4, format='%02.0f')
    spin1_12.delete(0, 'end')
    spin1_12.insert(0, '02')
    spin1_13 = Spinbox(tab0, from_=00, to=999, width=4, format='%02.0f')
    spin1_13.delete(0, 'end')
    spin1_13.insert(0, '02')
    spin1_14 = Spinbox(tab0, from_=00, to=999, width=4, format='%02.0f')
    spin1_14.delete(0, 'end')
    spin1_14.insert(0, '02')
    spin1_15 = Spinbox(tab0, from_=00, to=999, width=4, format='%02.0f')
    spin1_15.delete(0, 'end')
    spin1_15.insert(0, '02')

    spin1_16 = Spinbox(tab0, from_=00, to=999, width=4, format='%02.0f')
    spin1_16.delete(0, 'end')
    spin1_16.insert(0, '02')
    spin1_17 = Spinbox(tab0, from_=00, to=999, width=4, format='%02.0f')
    spin1_17.delete(0, 'end')
    spin1_17.insert(0, '02')
    spin1_18 = Spinbox(tab0, from_=00, to=999, width=4, format='%02.0f')
    spin1_18.delete(0, 'end')
    spin1_18.insert(0, '02')
    spin1_19 = Spinbox(tab0, from_=00, to=999, width=4, format='%02.0f')
    spin1_19.delete(0, 'end')
    spin1_19.insert(0, '02')
    spin1_20 = Spinbox(tab0, from_=00, to=999, width=4, format='%02.0f')
    spin1_20.delete(0, 'end')
    spin1_20.insert(0, '14')
    spin1_21 = Spinbox(tab0, from_=00, to=999, width=4, format='%02.0f')
    spin1_21.delete(0, 'end')
    spin1_21.insert(0, '01')
    spin1_22 = Spinbox(tab0, from_=00, to=999, width=4, format='%02.0f')
    spin1_22.delete(0, 'end')
    spin1_22.insert(0, '01')
    spin1_23 = Spinbox(tab0, from_=00, to=999, width=4, format='%02.0f')
    spin1_23.delete(0, 'end')
    spin1_23.insert(0, '01')
    spin1_24 = Spinbox(tab0, from_=00, to=999, width=4, format='%02.0f')
    spin1_24.delete(0, 'end')
    spin1_24.insert(0, '01')
    spin1_25 = Spinbox(tab0, from_=00, to=999, width=4, format='%02.0f')
    spin1_25.delete(0, 'end')
    spin1_25.insert(0, '01')

    phaseLabel0_1 = Label(tab0, text='Phase 1:  ')
    phaseLabel0_2 = Label(tab0, text='Phase 2:  ')
    phaseLabel0_3 = Label(tab0, text='Phase 3:  ')
    phaseLabel0_4 = Label(tab0, text='Phase 4:  ')
    phaseLabel0_5 = Label(tab0, text='Phase 5:  ')
    phaseLabel0_6 = Label(tab0, text='Phase 6:  ')
    phaseLabel0_7 = Label(tab0, text='Phase 7:  ')
    phaseLabel0_8 = Label(tab0, text='Phase 8:  ')
    phaseLabel0_9 = Label(tab0, text='Phase 9:  ')
    phaseLabel0_10 = Label(tab0, text='Phase 10:  ')
    phaseLabel0_11 = Label(tab0, text='Phase 11:  ')
    phaseLabel0_12 = Label(tab0, text='Phase 12:  ')
    phaseLabel0_13 = Label(tab0, text='Phase 13:  ')
    phaseLabel0_14 = Label(tab0, text='Phase 14:  ')
    phaseLabel0_15 = Label(tab0, text='Phase 15:  ')
    phaseLabel0_16 = Label(tab0, text='Phase 16:  ')
    phaseLabel0_17 = Label(tab0, text='Phase 17:  ')
    phaseLabel0_18 = Label(tab0, text='Phase 18:  ')
    phaseLabel0_19 = Label(tab0, text='Phase 19:  ')
    phaseLabel0_20 = Label(tab0, text='Phase 20:  ')
    

    T_label0_1 = Label(tab0, text='T=')
    T_label0_2 = Label(tab0, text='T=')
    T_label0_3 = Label(tab0, text='T=')
    T_label0_4 = Label(tab0, text='T=')
    T_label0_5 = Label(tab0, text='T=')
    T_label0_6 = Label(tab0, text='T=')
    T_label0_7 = Label(tab0, text='T=')
    T_label0_8 = Label(tab0, text='T=')
    T_label0_9 = Label(tab0, text='T=')
    T_label0_10 = Label(tab0, text='T=')
    T_label0_11 = Label(tab0, text='T=')
    T_label0_12 = Label(tab0, text='T=')
    T_label0_13 = Label(tab0, text='T=')
    T_label0_14 = Label(tab0, text='T=')
    T_label0_15 = Label(tab0, text='T=')
    T_label0_16 = Label(tab0, text='T=')
    T_label0_17 = Label(tab0, text='T=')
    T_label0_18 = Label(tab0, text='T=')
    T_label0_19 = Label(tab0, text='T=')
    T_label0_20 = Label(tab0, text='T=')

    T_labelend1 = Label(tab0, text='h/day  ')
    T_labelend2 = Label(tab0, text='h/day  ')
    T_labelend3 = Label(tab0, text='h/day  ')
    T_labelend4 = Label(tab0, text='h/day  ')
    T_labelend5 = Label(tab0, text='h/day  ')
    T_labelend6 = Label(tab0, text='h/day  ')
    T_labelend7 = Label(tab0, text='h/day  ')
    T_labelend8 = Label(tab0, text='h/day  ')
    T_labelend9 = Label(tab0, text='h/day  ')
    T_labelend10 = Label(tab0, text='h/day  ')
    T_labelend11 = Label(tab0, text='h/day  ')
    T_labelend12 = Label(tab0, text='h/day  ')
    T_labelend13 = Label(tab0, text='h/day  ')
    T_labelend14 = Label(tab0, text='h/day  ')
    T_labelend15 = Label(tab0, text='h/day  ')
    T_labelend16 = Label(tab0, text='h/day  ')
    T_labelend17 = Label(tab0, text='h/day  ')
    T_labelend18 = Label(tab0, text='h/day  ')
    T_labelend19 = Label(tab0, text='h/day  ')
    T_labelend20 = Label(tab0, text='h/day  ')


    DurationLabel1 = Label(tab0, text=' Duration  ')
    DurationLabel2 = Label(tab0, text=' Duration  ')
    DurationLabel3 = Label(tab0, text=' Duration  ')
    DurationLabel4 = Label(tab0, text=' Duration  ')
    DurationLabel5 = Label(tab0, text=' Duration  ')
    DurationLabel6 = Label(tab0, text=' Duration  ')
    DurationLabel7 = Label(tab0, text=' Duration  ')
    DurationLabel8 = Label(tab0, text=' Duration  ')
    DurationLabel9 = Label(tab0, text=' Duration  ')
    DurationLabel10 = Label(tab0, text=' Duration  ')
    DurationLabel11 = Label(tab0, text=' Duration  ')
    DurationLabel12 = Label(tab0, text=' Duration  ')
    DurationLabel13 = Label(tab0, text=' Duration  ')
    DurationLabel14 = Label(tab0, text=' Duration  ')
    DurationLabel15 = Label(tab0, text=' Duration  ')
    DurationLabel16 = Label(tab0, text=' Duration  ')
    DurationLabel17 = Label(tab0, text=' Duration  ')
    DurationLabel18 = Label(tab0, text=' Duration  ')
    DurationLabel19 = Label(tab0, text=' Duration  ')
    DurationLabel20 = Label(tab0, text=' Duration  ')

    DayLabel1 = Label(tab0, text='days      ')
    DayLabel2 = Label(tab0, text='days      ')
    DayLabel3 = Label(tab0, text='days      ')
    DayLabel4 = Label(tab0, text='days      ')
    DayLabel5 = Label(tab0, text='days      ')
    DayLabel6 = Label(tab0, text='days      ')
    DayLabel7 = Label(tab0, text='days      ')
    DayLabel8 = Label(tab0, text='days      ')
    DayLabel9 = Label(tab0, text='days      ')
    DayLabel10 = Label(tab0, text='days      ')
    DayLabel11 = Label(tab0, text='days      ')
    DayLabel12 = Label(tab0, text='days      ')
    DayLabel13 = Label(tab0, text='days      ')
    DayLabel14 = Label(tab0, text='days      ')
    DayLabel15 = Label(tab0, text='days      ')
    DayLabel16 = Label(tab0, text='days      ')
    DayLabel17 = Label(tab0, text='days      ')
    DayLabel18 = Label(tab0, text='days      ')
    DayLabel19 = Label(tab0, text='days      ')
    DayLabel20 = Label(tab0, text='days      ')

    fromLabel0.grid(column=0, row=2+row_adj, padx=15, pady=5)
    spin0_1.grid(column=1, row=2+row_adj)
    label0_h0.grid(column=2, row=2+row_adj)
    spin0_2.grid(column=3, row=2+row_adj)
    space0.grid(column=4, row=2+row_adj)
    year0_entry.grid(column=5, row=2+row_adj)
    label0_d_0.grid(column=6, row=2+row_adj)
    month0_entry.grid(column=7, row=2+row_adj)
    label0_m_0.grid(column=8, row=2+row_adj)
    date0_entry.grid(column=9, row=2+row_adj)


    phaseLabel0_1.grid(column=10, row=3+row_adj)
    T_label0_1.grid(column=11, row=3+row_adj)
    spin0_3.grid(column=12, row=3+row_adj)
    T_labelend1.grid(column=13, row=3+row_adj)
    DurationLabel1.grid(column=14, row=3+row_adj)
    spin1_6.grid(column=15, row=3+row_adj)
    DayLabel1.grid(column=16, row=3+row_adj)


    phaseLabel0_2.grid(column=10, row=4+row_adj)
    T_label0_2.grid(column=11, row=4+row_adj)
    spin0_4.grid(column=12, row=4+row_adj)
    T_labelend2.grid(column=13, row=4+row_adj)
    DurationLabel2.grid(column=14, row=4+row_adj)
    spin1_7.grid(column=15, row=4+row_adj)
    DayLabel2.grid(column=16, row=4+row_adj)

    phaseLabel0_3.grid(column=10, row=5+row_adj)
    T_label0_3.grid(column=11, row=5+row_adj)
    spin0_5.grid(column=12, row=5+row_adj)
    T_labelend3.grid(column=13, row=5+row_adj)
    DurationLabel3.grid(column=14, row=5+row_adj)
    spin1_8.grid(column=15, row=5+row_adj)
    DayLabel3.grid(column=16, row=5+row_adj)

    phaseLabel0_4.grid(column=10, row=6+row_adj)
    T_label0_4.grid(column=11, row=6+row_adj)
    spin0_6.grid(column=12, row=6+row_adj)
    T_labelend4.grid(column=13, row=6+row_adj)
    DurationLabel4.grid(column=14, row=6+row_adj)
    spin1_9.grid(column=15, row=6+row_adj)
    DayLabel4.grid(column=16, row=6+row_adj)

    phaseLabel0_5.grid(column=10, row=7+row_adj)
    T_label0_5.grid(column=11, row=7+row_adj)
    spin0_7.grid(column=12, row=7+row_adj)
    T_labelend5.grid(column=13, row=7+row_adj)
    DurationLabel5.grid(column=14, row=7+row_adj)
    spin1_10.grid(column=15, row=7+row_adj)
    DayLabel5.grid(column=16, row=7+row_adj)

    phaseLabel0_6.grid(column=10, row=8+row_adj)
    T_label0_6.grid(column=11, row=8+row_adj)
    spin0_8.grid(column=12, row=8+row_adj)
    T_labelend6.grid(column=13, row=8+row_adj)
    DurationLabel6.grid(column=14, row=8+row_adj)
    spin1_11.grid(column=15, row=8+row_adj)
    DayLabel6.grid(column=16, row=8+row_adj)

    phaseLabel0_7.grid(column=10, row=9+row_adj)
    T_label0_7.grid(column=11, row=9+row_adj)
    spin0_9.grid(column=12, row=9+row_adj)
    T_labelend7.grid(column=13, row=9+row_adj)
    DurationLabel7.grid(column=14, row=9+row_adj)
    spin1_12.grid(column=15, row=9+row_adj)
    DayLabel7.grid(column=16, row=9+row_adj)

    phaseLabel0_8.grid(column=10, row=10+row_adj)
    T_label0_8.grid(column=11, row=10+row_adj)
    spin0_10.grid(column=12, row=10+row_adj)
    T_labelend8.grid(column=13, row=10+row_adj)
    DurationLabel8.grid(column=14, row=10+row_adj)
    spin1_13.grid(column=15, row=10+row_adj)
    DayLabel8.grid(column=16, row=10+row_adj)

    phaseLabel0_9.grid(column=10, row=11+row_adj)
    T_label0_9.grid(column=11, row=11+row_adj)
    spin0_11.grid(column=12, row=11+row_adj)
    T_labelend9.grid(column=13, row=11+row_adj)
    DurationLabel9.grid(column=14, row=11+row_adj)
    spin1_14.grid(column=15, row=11+row_adj)
    DayLabel9.grid(column=16, row=11+row_adj)

    phaseLabel0_10.grid(column=10, row=12+row_adj)
    T_label0_10.grid(column=11, row=12+row_adj)
    spin0_12.grid(column=12, row=12+row_adj)
    T_labelend10.grid(column=13, row=12+row_adj)
    DurationLabel10.grid(column=14, row=12+row_adj)
    spin1_15.grid(column=15, row=12+row_adj)
    DayLabel10.grid(column=16, row=12+row_adj)

    phaseLabel0_11.grid(column=17, row=3+row_adj)
    T_label0_11.grid(column=18, row=3+row_adj)
    spin0_13.grid(column=19, row=3+row_adj)
    T_labelend11.grid(column=20, row=3+row_adj)
    DurationLabel11.grid(column=21, row=3+row_adj)
    spin1_16.grid(column=22, row=3+row_adj)
    DayLabel11.grid(column=23, row=3+row_adj)

    phaseLabel0_12.grid(column=17, row=4+row_adj)
    T_label0_12.grid(column=18, row=4+row_adj)
    spin0_14.grid(column=19, row=4+row_adj)
    T_labelend12.grid(column=20, row=4+row_adj)
    DurationLabel12.grid(column=21, row=4+row_adj)
    spin1_17.grid(column=22, row=4+row_adj)
    DayLabel12.grid(column=23, row=4+row_adj)

    phaseLabel0_13.grid(column=17, row=5+row_adj)
    T_label0_13.grid(column=18, row=5+row_adj)
    spin0_15.grid(column=19, row=5+row_adj)
    T_labelend13.grid(column=20, row=5+row_adj)
    DurationLabel13.grid(column=21, row=5+row_adj)
    spin1_18.grid(column=22, row=5+row_adj)
    DayLabel13.grid(column=23, row=5+row_adj)

    phaseLabel0_14.grid(column=17, row=6+row_adj)
    T_label0_14.grid(column=18, row=6+row_adj)
    spin0_16.grid(column=19, row=6+row_adj)
    T_labelend14.grid(column=20, row=6+row_adj)
    DurationLabel14.grid(column=21, row=6+row_adj)
    spin1_19.grid(column=22, row=6+row_adj)
    DayLabel14.grid(column=23, row=6+row_adj)

    phaseLabel0_15.grid(column=17, row=7+row_adj)
    T_label0_15.grid(column=18, row=7+row_adj)
    spin0_17.grid(column=19, row=7+row_adj)
    T_labelend15.grid(column=20, row=7+row_adj)
    DurationLabel15.grid(column=21, row=7+row_adj)
    spin1_20.grid(column=22, row=7+row_adj)
    DayLabel15.grid(column=23, row=7+row_adj)

    phaseLabel0_16.grid(column=17, row=8+row_adj)
    T_label0_16.grid(column=18, row=8+row_adj)
    spin0_18.grid(column=19, row=8+row_adj)
    T_labelend16.grid(column=20, row=8+row_adj)
    DurationLabel16.grid(column=21, row=8+row_adj)
    spin1_21.grid(column=22, row=8+row_adj)
    DayLabel16.grid(column=23, row=8+row_adj)

    phaseLabel0_17.grid(column=17, row=9+row_adj)
    T_label0_17.grid(column=18, row=9+row_adj)
    spin0_19.grid(column=19, row=9+row_adj)
    T_labelend17.grid(column=20, row=9+row_adj)
    DurationLabel17.grid(column=21, row=9+row_adj)
    spin1_22.grid(column=22, row=9+row_adj)
    DayLabel17.grid(column=23, row=9+row_adj)

    phaseLabel0_18.grid(column=17, row=10+row_adj)
    T_label0_18.grid(column=18, row=10+row_adj)
    spin0_20.grid(column=19, row=10+row_adj)
    T_labelend18.grid(column=20, row=10+row_adj)
    DurationLabel18.grid(column=21, row=10+row_adj)
    spin1_23.grid(column=22, row=10+row_adj)
    DayLabel18.grid(column=23, row=10+row_adj)

    phaseLabel0_19.grid(column=17, row=11+row_adj)
    T_label0_19.grid(column=18, row=11+row_adj)
    spin0_21.grid(column=19, row=11+row_adj)
    T_labelend19.grid(column=20, row=11+row_adj)
    DurationLabel19.grid(column=21, row=11+row_adj)
    spin1_24.grid(column=22, row=11+row_adj)
    DayLabel19.grid(column=23, row=11+row_adj)

    phaseLabel0_20.grid(column=17, row=12+row_adj)
    T_label0_20.grid(column=18, row=12+row_adj)
    spin0_22.grid(column=19, row=12+row_adj)
    T_labelend20.grid(column=20, row=12+row_adj)
    DurationLabel20.grid(column=21, row=12+row_adj)
    spin1_25.grid(column=22, row=12+row_adj)
    DayLabel20.grid(column=23, row=12+row_adj)

    # Boxes

    boxes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    btn = []

    btnAll = []

    tab_title = []

    capSep = []

    boxsched_text = []

    phaseLabel_1 = []

    rad_A_1 = []

    lbl_A_1 = []

    spin_A_1 = []

    boxsched_stat = []

    spin_B_1 = []

    label_h1_1 = []

    label_m1_1 = []

    lbl_B_1 = []

    spin_C_1 = []

    spin_D_1 = []

    label_h2_1 = []

    label_m2_1 = []

    rad_B_1 = []

    rad_C_1 = []

    phaseLabel_2 = []

    rad_A_2 = []

    lbl_A_2 = []

    spin_A_2 = []

    spin_B_2 = []

    label_h1_2 = []

    label_m1_2 = []

    lbl_B_2 = []

    spin_C_2 = []

    spin_D_2 = []

    label_h2_2 = []

    label_m2_2 = []

    rad_B_2 = []

    rad_C_2 = []

    phaseLabel_3 = []
    rad_A_3 = []
    lbl_A_3 = []
    spin_A_3 = []
    spin_B_3 = []
    label_h1_3 = []
    label_m1_3 = []
    lbl_B_3 = []
    spin_C_3 = []
    spin_D_3 = []
    label_h2_3 = []
    label_m2_3 = []
    rad_B_3 = []
    rad_C_3 = []
    phaseLabel_4 = []
    rad_A_4 = []
    lbl_A_4 = []
    spin_A_4 = []
    spin_B_4 = []
    label_h1_4 = []
    label_m1_4 = []
    lbl_B_4 = []
    spin_C_4 = []
    spin_D_4 = []
    label_h2_4 = []
    label_m2_4 = []
    rad_B_4 = []
    rad_C_4 = []
    phaseLabel_5 = []
    rad_A_5 = []
    lbl_A_5 = []
    spin_A_5 = []
    spin_B_5 = []
    label_h1_5 = []
    label_m1_5 = []
    lbl_B_5 = []
    spin_C_5 = []
    spin_D_5 = []
    label_h2_5 = []
    label_m2_5 = []
    rad_B_5 = []
    rad_C_5 = []
    phaseLabel_6 = []
    rad_A_6 = []
    lbl_A_6 = []
    spin_A_6 = []
    spin_B_6 = []
    label_h1_6 = []
    label_m1_6 = []
    lbl_B_6 = []
    spin_C_6 = []
    spin_D_6 = []
    label_h2_6 = []
    label_m2_6 = []
    rad_B_6 = []
    rad_C_6 = []
    phaseLabel_7 = []
    rad_A_7 = []
    lbl_A_7 = []
    spin_A_7 = []
    spin_B_7 = []
    label_h1_7 = []
    label_m1_7 = []
    lbl_B_7 = []
    spin_C_7 = []
    spin_D_7 = []
    label_h2_7 = []
    label_m2_7 = []
    rad_B_7 = []
    rad_C_7 = []
    phaseLabel_8 = []
    rad_A_8 = []
    lbl_A_8 = []
    spin_A_8 = []
    spin_B_8 = []
    label_h1_8 = []
    label_m1_8 = []
    lbl_B_8 = []
    spin_C_8 = []
    spin_D_8 = []
    label_h2_8 = []
    label_m2_8 = []
    rad_B_8 = []
    rad_C_8 = []
    phaseLabel_9 = []
    rad_A_9 = []
    lbl_A_9 = []
    spin_A_9 = []
    spin_B_9 = []
    label_h1_9 = []
    label_m1_9 = []
    lbl_B_9 = []
    spin_C_9 = []
    spin_D_9 = []
    label_h2_9 = []
    label_m2_9 = []
    rad_B_9 = []
    rad_C_9 = []
    phaseLabel_10 = []
    rad_A_10 = []
    lbl_A_10 = []
    spin_A_10 = []
    spin_B_10 = []
    label_h1_10 = []
    label_m1_10 = []
    lbl_B_10 = []
    spin_C_10 = []
    spin_D_10 = []
    label_h2_10 = []
    label_m2_10 = []
    rad_B_10 = []
    rad_C_10 = []
    phaseLabel_11 = []
    rad_A_11 = []
    lbl_A_11 = []
    spin_A_11 = []
    spin_B_11 = []
    label_h1_11 = []
    label_m1_11 = []
    lbl_B_11 = []
    spin_C_11 = []
    spin_D_11 = []
    label_h2_11 = []
    label_m2_11 = []
    rad_B_11 = []
    rad_C_11 = []
    phaseLabel_12 = []
    rad_A_12 = []
    lbl_A_12 = []
    spin_A_12 = []
    spin_B_12 = []
    label_h1_12 = []
    label_m1_12 = []
    lbl_B_12 = []
    spin_C_12 = []
    spin_D_12 = []
    label_h2_12 = []
    label_m2_12 = []
    rad_B_12 = []
    rad_C_12 = []
    phaseLabel_13 = []
    rad_A_13 = []
    lbl_A_13 = []
    spin_A_13 = []
    spin_B_13 = []
    label_h1_13 = []
    label_m1_13 = []
    lbl_B_13 = []
    spin_C_13 = []
    spin_D_13 = []
    label_h2_13 = []
    label_m2_13 = []
    rad_B_13 = []
    rad_C_13 = []
    phaseLabel_14 = []
    rad_A_14 = []
    lbl_A_14 = []
    spin_A_14 = []
    spin_B_14 = []
    label_h1_14 = []
    label_m1_14 = []
    lbl_B_14 = []
    spin_C_14 = []
    spin_D_14 = []
    label_h2_14 = []
    label_m2_14 = []
    rad_B_14 = []
    rad_C_14 = []
    phaseLabel_15 = []
    rad_A_15 = []
    lbl_A_15 = []
    spin_A_15 = []
    spin_B_15 = []
    label_h1_15 = []
    label_m1_15 = []
    lbl_B_15 = []
    spin_C_15 = []
    spin_D_15 = []
    label_h2_15 = []
    label_m2_15 = []
    rad_B_15 = []
    rad_C_15 = []
    phaseLabel_16 = []
    rad_A_16 = []
    lbl_A_16 = []
    spin_A_16 = []
    spin_B_16 = []
    label_h1_16 = []
    label_m1_16 = []
    lbl_B_16 = []
    spin_C_16 = []
    spin_D_16 = []
    label_h2_16 = []
    label_m2_16 = []
    rad_B_16 = []
    rad_C_16 = []
    phaseLabel_17 = []
    rad_A_17 = []
    lbl_A_17 = []
    spin_A_17 = []
    spin_B_17 = []
    label_h1_17 = []
    label_m1_17 = []
    lbl_B_17 = []
    spin_C_17 = []
    spin_D_17 = []
    label_h2_17 = []
    label_m2_17 = []
    rad_B_17 = []
    rad_C_17 = []
    phaseLabel_18 = []
    rad_A_18 = []
    lbl_A_18 = []
    spin_A_18 = []
    spin_B_18 = []
    label_h1_18 = []
    label_m1_18 = []
    lbl_B_18 = []
    spin_C_18 = []
    spin_D_18 = []
    label_h2_18 = []
    label_m2_18 = []
    rad_B_18 = []
    rad_C_18 = []
    phaseLabel_19 = []
    rad_A_19 = []
    lbl_A_19 = []
    spin_A_19 = []
    spin_B_19 = []
    label_h1_19 = []
    label_m1_19 = []
    lbl_B_19 = []
    spin_C_19 = []
    spin_D_19 = []
    label_h2_19 = []
    label_m2_19 = []
    rad_B_19 = []
    rad_C_19 = []
    phaseLabel_20 = []
    rad_A_20 = []
    lbl_A_20 = []
    spin_A_20 = []
    spin_B_20 = []
    label_h1_20 = []
    label_m1_20 = []
    lbl_B_20 = []
    spin_C_20 = []
    spin_D_20 = []
    label_h2_20 = []
    label_m2_20 = []
    rad_B_20 = []
    rad_C_20 = []

    tab_title2 = []

    boxrec_text = []

    boxrec_stat = []

    for i in range(10):

        btnAll.append(Button(tab[i], text='Set All',
                             command=getAllBoxSchedule))

        tab_title.append(Label(tab[i], text='LED schedule', anchor='center'))

        capSep.append(ttk.Separator(tab[i], orient=HORIZONTAL))

        boxsched_text.append(StringVar())

        phaseLabel_1.append(Label(tab[i], text='Phase 1'))

        rad_A_1.append(Radiobutton(

            tab[i], text='LD', variable=var_1[i], value=1))

        lbl_A_1.append(Label(tab[i], text='On:'))

        spin_A_1.append(
            Spinbox(tab[i], from_=00, to=24, width=3, format='%02.0f'))

        boxsched_stat.append(Label(

            tab[i], textvariable=boxsched_text[i], anchor=W, justify=LEFT))

        spin_B_1.append(
            Spinbox(tab[i], from_=00, to=59, width=3, format='%02.0f'))

        label_h1_1.append(Label(tab[i], text=':'))

        label_m1_1.append(Label(tab[i], text=''))

        lbl_B_1.append(Label(tab[i], text='Ratio:'))

        spin_C_1.append(
            Spinbox(tab[i], from_=00, to=24, width=3, format='%02.0f'))

        spin_D_1.append(
            Spinbox(tab[i], from_=00, to=24, width=3, format='%02.0f'))

        label_h2_1.append(Label(tab[i], text=':'))

        label_m2_1.append(Label(tab[i], text=''))

        rad_B_1.append(Radiobutton(
            tab[i], text='DD', variable=var_1[i], value=2))

        rad_C_1.append(Radiobutton(
            tab[i], text='LL', variable=var_1[i], value=3))

        phaseLabel_2.append(Label(tab[i], text='Phase 2'))

        rad_A_2.append(Radiobutton(
            tab[i], text='LD', variable=var_2[i], value=1))

        lbl_A_2.append(Label(tab[i], text='On:'))

        spin_A_2.append(
            Spinbox(tab[i], from_=00, to=24, width=3, format='%02.0f'))

        spin_B_2.append(
            Spinbox(tab[i], from_=00, to=59, width=3, format='%02.0f'))

        label_h1_2.append(Label(tab[i], text=':'))

        lbl_B_2.append(Label(tab[i], text='Ratio:'))

        spin_C_2.append(
            Spinbox(tab[i], from_=00, to=24, width=3, format='%02.0f'))

        spin_D_2.append(
            Spinbox(tab[i], from_=00, to=24, width=3, format='%02.0f'))

        label_h2_2.append(Label(tab[i], text=':'))

        label_m2_2.append(Label(tab[i], text=''))

        rad_B_2.append(Radiobutton(
            tab[i], text='DD', variable=var_2[i], value=2))

        rad_C_2.append(Radiobutton(

            tab[i], text='LL', variable=var_2[i], value=3))

        phaseLabel_3.append(Label(tab[i], text='Phase 3'))

        rad_A_3.append(Radiobutton(
            tab[i], text='LD', variable=var_3[i], value=1))

        lbl_A_3.append(Label(tab[i], text='On:'))

        spin_A_3.append(
            Spinbox(tab[i], from_=00, to=24, width=3, format='%02.0f'))

        spin_B_3.append(
            Spinbox(tab[i], from_=00, to=59, width=3, format='%02.0f'))

        label_h1_3.append(Label(tab[i], text=':'))

        lbl_B_3.append(Label(tab[i], text='Ratio:'))

        spin_C_3.append(
            Spinbox(tab[i], from_=00, to=24, width=3, format='%02.0f'))

        spin_D_3.append(
            Spinbox(tab[i], from_=00, to=24, width=3, format='%02.0f'))

        label_h2_3.append(Label(tab[i], text=':'))

        rad_B_3.append(Radiobutton(

            tab[i], text='DD', variable=var_3[i], value=2))

        rad_C_3.append(Radiobutton(
            tab[i], text='LL', variable=var_3[i], value=3))

        # phase4
        phaseLabel_4.append(Label(tab[i], text='Phase 4'))

        rad_A_4.append(Radiobutton(
            tab[i], text='LD', variable=var_4[i], value=1))

        lbl_A_4.append(Label(tab[i], text='On:'))

        spin_A_4.append(Spinbox(tab[i], from_=00,
                                to=24, width=3, format='%02.0f'))

        spin_B_4.append(Spinbox(tab[i], from_=00,
                                to=59, width=3, format='%02.0f'))

        label_h1_4.append(Label(tab[i], text=':'))

        lbl_B_4.append(Label(tab[i], text='Ratio:'))

        spin_C_4.append(Spinbox(tab[i], from_=00,
                                to=24, width=3, format='%02.0f'))

        spin_D_4.append(Spinbox(tab[i], from_=00,
                                to=24, width=3, format='%02.0f'))

        label_h2_4.append(Label(tab[i], text=':'))

        rad_B_4.append(Radiobutton(

            tab[i], text='DD', variable=var_4[i], value=2))

        rad_C_4.append(Radiobutton(
            tab[i], text='LL', variable=var_4[i], value=3))

        # phase5
        phaseLabel_5.append(Label(tab[i], text='Phase 5'))

        rad_A_5.append(Radiobutton(
            tab[i], text='LD', variable=var_5[i], value=1))

        lbl_A_5.append(Label(tab[i], text='On:'))

        spin_A_5.append(Spinbox(tab[i], from_=00,
                                to=24, width=3, format='%02.0f'))

        spin_B_5.append(Spinbox(tab[i], from_=00,
                                to=59, width=3, format='%02.0f'))

        label_h1_5.append(Label(tab[i], text=':'))

        lbl_B_5.append(Label(tab[i], text='Ratio:'))

        spin_C_5.append(Spinbox(tab[i], from_=00,
                                to=24, width=3, format='%02.0f'))

        spin_D_5.append(Spinbox(tab[i], from_=00,
                                to=24, width=3, format='%02.0f'))

        label_h2_5.append(Label(tab[i], text=':'))

        rad_B_5.append(Radiobutton(

            tab[i], text='DD', variable=var_5[i], value=2))

        rad_C_5.append(Radiobutton(
            tab[i], text='LL', variable=var_5[i], value=3))

        # phase6
        phaseLabel_6.append(Label(tab[i], text='Phase 6'))

        rad_A_6.append(Radiobutton(
            tab[i], text='LD', variable=var_6[i], value=1))

        lbl_A_6.append(Label(tab[i], text='On:'))

        spin_A_6.append(Spinbox(tab[i], from_=00,
                                to=24, width=3, format='%02.0f'))

        spin_B_6.append(Spinbox(tab[i], from_=00,
                                to=59, width=3, format='%02.0f'))

        label_h1_6.append(Label(tab[i], text=':'))

        lbl_B_6.append(Label(tab[i], text='Ratio:'))

        spin_C_6.append(Spinbox(tab[i], from_=00,
                                to=24, width=3, format='%02.0f'))

        spin_D_6.append(Spinbox(tab[i], from_=00,
                                to=24, width=3, format='%02.0f'))

        label_h2_6.append(Label(tab[i], text=':'))

        rad_B_6.append(Radiobutton(

            tab[i], text='DD', variable=var_6[i], value=2))

        rad_C_6.append(Radiobutton(
            tab[i], text='LL', variable=var_6[i], value=3))

        # phase7
        phaseLabel_7.append(Label(tab[i], text='Phase 7'))

        rad_A_7.append(Radiobutton(
            tab[i], text='LD', variable=var_7[i], value=1))

        lbl_A_7.append(Label(tab[i], text='On:'))

        spin_A_7.append(Spinbox(tab[i], from_=00,
                                to=24, width=3, format='%02.0f'))

        spin_B_7.append(Spinbox(tab[i], from_=00,
                                to=59, width=3, format='%02.0f'))

        label_h1_7.append(Label(tab[i], text=':'))

        lbl_B_7.append(Label(tab[i], text='Ratio:'))

        spin_C_7.append(Spinbox(tab[i], from_=00,
                                to=24, width=3, format='%02.0f'))

        spin_D_7.append(Spinbox(tab[i], from_=00,
                                to=24, width=3, format='%02.0f'))

        label_h2_7.append(Label(tab[i], text=':'))

        rad_B_7.append(Radiobutton(

            tab[i], text='DD', variable=var_7[i], value=2))

        rad_C_7.append(Radiobutton(
            tab[i], text='LL', variable=var_7[i], value=3))

        # phase8
        phaseLabel_8.append(Label(tab[i], text='Phase 8'))

        rad_A_8.append(Radiobutton(
            tab[i], text='LD', variable=var_8[i], value=1))

        lbl_A_8.append(Label(tab[i], text='On:'))

        spin_A_8.append(Spinbox(tab[i], from_=00,
                                to=24, width=3, format='%02.0f'))

        spin_B_8.append(Spinbox(tab[i], from_=00,
                                to=59, width=3, format='%02.0f'))

        label_h1_8.append(Label(tab[i], text=':'))

        lbl_B_8.append(Label(tab[i], text='Ratio:'))

        spin_C_8.append(Spinbox(tab[i], from_=00,
                                to=24, width=3, format='%02.0f'))

        spin_D_8.append(Spinbox(tab[i], from_=00,
                                to=24, width=3, format='%02.0f'))

        label_h2_8.append(Label(tab[i], text=':'))

        rad_B_8.append(Radiobutton(

            tab[i], text='DD', variable=var_8[i], value=2))

        rad_C_8.append(Radiobutton(
            tab[i], text='LL', variable=var_8[i], value=3))

        # phase9
        phaseLabel_9.append(Label(tab[i], text='Phase 9'))

        rad_A_9.append(Radiobutton(
            tab[i], text='LD', variable=var_9[i], value=1))

        lbl_A_9.append(Label(tab[i], text='On:'))

        spin_A_9.append(Spinbox(tab[i], from_=00,
                                to=24, width=3, format='%02.0f'))

        spin_B_9.append(Spinbox(tab[i], from_=00,
                                to=59, width=3, format='%02.0f'))

        label_h1_9.append(Label(tab[i], text=':'))

        lbl_B_9.append(Label(tab[i], text='Ratio:'))

        spin_C_9.append(Spinbox(tab[i], from_=00,
                                to=24, width=3, format='%02.0f'))

        spin_D_9.append(Spinbox(tab[i], from_=00,
                                to=24, width=3, format='%02.0f'))

        label_h2_9.append(Label(tab[i], text=':'))

        rad_B_9.append(Radiobutton(

            tab[i], text='DD', variable=var_9[i], value=2))

        rad_C_9.append(Radiobutton(
            tab[i], text='LL', variable=var_9[i], value=3))

        # phase10
        phaseLabel_10.append(Label(tab[i], text='Phase 10'))

        rad_A_10.append(Radiobutton(
            tab[i], text='LD', variable=var_10[i], value=1))

        lbl_A_10.append(Label(tab[i], text='On:'))

        spin_A_10.append(Spinbox(tab[i], from_=00,
                                 to=24, width=3, format='%02.0f'))

        spin_B_10.append(Spinbox(tab[i], from_=00,
                                 to=59, width=3, format='%02.0f'))

        label_h1_10.append(Label(tab[i], text=':'))

        lbl_B_10.append(Label(tab[i], text='Ratio:'))

        spin_C_10.append(Spinbox(tab[i], from_=00,
                                 to=24, width=3, format='%02.0f'))

        spin_D_10.append(Spinbox(tab[i], from_=00,
                                 to=24, width=3, format='%02.0f'))

        label_h2_10.append(Label(tab[i], text=':'))

        rad_B_10.append(Radiobutton(

            tab[i], text='DD', variable=var_10[i], value=2))

        rad_C_10.append(Radiobutton(
            tab[i], text='LL', variable=var_10[i], value=3))

        # phase11
        phaseLabel_11.append(Label(tab[i], text='Phase 11'))

        rad_A_11.append(Radiobutton(
            tab[i], text='LD', variable=var_11[i], value=1))

        lbl_A_11.append(Label(tab[i], text='On:'))

        spin_A_11.append(Spinbox(tab[i], from_=00,
                                 to=24, width=3, format='%02.0f'))

        spin_B_11.append(Spinbox(tab[i], from_=00,
                                 to=59, width=3, format='%02.0f'))

        label_h1_11.append(Label(tab[i], text=':'))

        lbl_B_11.append(Label(tab[i], text='Ratio:'))

        spin_C_11.append(Spinbox(tab[i], from_=00,
                                 to=24, width=3, format='%02.0f'))

        spin_D_11.append(Spinbox(tab[i], from_=00,
                                 to=24, width=3, format='%02.0f'))

        label_h2_11.append(Label(tab[i], text=':'))

        rad_B_11.append(Radiobutton(

            tab[i], text='DD', variable=var_11[i], value=2))

        rad_C_11.append(Radiobutton(
            tab[i], text='LL', variable=var_11[i], value=3))

        # phase12
        phaseLabel_12.append(Label(tab[i], text='Phase 12'))

        rad_A_12.append(Radiobutton(
            tab[i], text='LD', variable=var_12[i], value=1))

        lbl_A_12.append(Label(tab[i], text='On:'))

        spin_A_12.append(Spinbox(tab[i], from_=00,
                                 to=24, width=3, format='%02.0f'))

        spin_B_12.append(Spinbox(tab[i], from_=00,
                                 to=59, width=3, format='%02.0f'))

        label_h1_12.append(Label(tab[i], text=':'))

        lbl_B_12.append(Label(tab[i], text='Ratio:'))

        spin_C_12.append(Spinbox(tab[i], from_=00,
                                 to=24, width=3, format='%02.0f'))

        spin_D_12.append(Spinbox(tab[i], from_=00,
                                 to=24, width=3, format='%02.0f'))

        label_h2_12.append(Label(tab[i], text=':'))

        rad_B_12.append(Radiobutton(

            tab[i], text='DD', variable=var_12[i], value=2))

        rad_C_12.append(Radiobutton(
            tab[i], text='LL', variable=var_12[i], value=3))

        # phase13
        phaseLabel_13.append(Label(tab[i], text='Phase 13'))

        rad_A_13.append(Radiobutton(
            tab[i], text='LD', variable=var_13[i], value=1))

        lbl_A_13.append(Label(tab[i], text='On:'))

        spin_A_13.append(Spinbox(tab[i], from_=00,
                                 to=24, width=3, format='%02.0f'))

        spin_B_13.append(Spinbox(tab[i], from_=00,
                                 to=59, width=3, format='%02.0f'))

        label_h1_13.append(Label(tab[i], text=':'))

        lbl_B_13.append(Label(tab[i], text='Ratio:'))

        spin_C_13.append(Spinbox(tab[i], from_=00,
                                 to=24, width=3, format='%02.0f'))

        spin_D_13.append(Spinbox(tab[i], from_=00,
                                 to=24, width=3, format='%02.0f'))

        label_h2_13.append(Label(tab[i], text=':'))

        rad_B_13.append(Radiobutton(

            tab[i], text='DD', variable=var_13[i], value=2))

        rad_C_13.append(Radiobutton(
            tab[i], text='LL', variable=var_13[i], value=3))

        # phase14
        phaseLabel_14.append(Label(tab[i], text='Phase 14'))

        rad_A_14.append(Radiobutton(
            tab[i], text='LD', variable=var_14[i], value=1))

        lbl_A_14.append(Label(tab[i], text='On:'))

        spin_A_14.append(Spinbox(tab[i], from_=00,
                                 to=24, width=3, format='%02.0f'))

        spin_B_14.append(Spinbox(tab[i], from_=00,
                                 to=59, width=3, format='%02.0f'))

        label_h1_14.append(Label(tab[i], text=':'))

        lbl_B_14.append(Label(tab[i], text='Ratio:'))

        spin_C_14.append(Spinbox(tab[i], from_=00,
                                 to=24, width=3, format='%02.0f'))

        spin_D_14.append(Spinbox(tab[i], from_=00,
                                 to=24, width=3, format='%02.0f'))

        label_h2_14.append(Label(tab[i], text=':'))

        rad_B_14.append(Radiobutton(

            tab[i], text='DD', variable=var_14[i], value=2))

        rad_C_14.append(Radiobutton(
            tab[i], text='LL', variable=var_14[i], value=3))

        # phase15
        phaseLabel_15.append(Label(tab[i], text='Phase 15'))

        rad_A_15.append(Radiobutton(
            tab[i], text='LD', variable=var_15[i], value=1))

        lbl_A_15.append(Label(tab[i], text='On:'))

        spin_A_15.append(Spinbox(tab[i], from_=00,
                                 to=24, width=3, format='%02.0f'))

        spin_B_15.append(Spinbox(tab[i], from_=00,
                                 to=59, width=3, format='%02.0f'))

        label_h1_15.append(Label(tab[i], text=':'))

        lbl_B_15.append(Label(tab[i], text='Ratio:'))

        spin_C_15.append(Spinbox(tab[i], from_=00,
                                 to=24, width=3, format='%02.0f'))

        spin_D_15.append(Spinbox(tab[i], from_=00,
                                 to=24, width=3, format='%02.0f'))

        label_h2_15.append(Label(tab[i], text=':'))

        rad_B_15.append(Radiobutton(

            tab[i], text='DD', variable=var_15[i], value=2))

        rad_C_15.append(Radiobutton(
            tab[i], text='LL', variable=var_15[i], value=3))

        # phase16
        phaseLabel_16.append(Label(tab[i], text='Phase 16'))

        rad_A_16.append(Radiobutton(
            tab[i], text='LD', variable=var_16[i], value=1))

        lbl_A_16.append(Label(tab[i], text='On:'))

        spin_A_16.append(Spinbox(tab[i], from_=00,
                                 to=24, width=3, format='%02.0f'))

        spin_B_16.append(Spinbox(tab[i], from_=00,
                                 to=59, width=3, format='%02.0f'))

        label_h1_16.append(Label(tab[i], text=':'))

        lbl_B_16.append(Label(tab[i], text='Ratio:'))

        spin_C_16.append(Spinbox(tab[i], from_=00,
                                 to=24, width=3, format='%02.0f'))

        spin_D_16.append(Spinbox(tab[i], from_=00,
                                 to=24, width=3, format='%02.0f'))

        label_h2_16.append(Label(tab[i], text=':'))

        rad_B_16.append(Radiobutton(

            tab[i], text='DD', variable=var_16[i], value=2))

        rad_C_16.append(Radiobutton(
            tab[i], text='LL', variable=var_16[i], value=3))

        # phase17
        phaseLabel_17.append(Label(tab[i], text='Phase 17'))

        rad_A_17.append(Radiobutton(
            tab[i], text='LD', variable=var_17[i], value=1))

        lbl_A_17.append(Label(tab[i], text='On:'))

        spin_A_17.append(Spinbox(tab[i], from_=00,
                                 to=24, width=3, format='%02.0f'))

        spin_B_17.append(Spinbox(tab[i], from_=00,
                                 to=59, width=3, format='%02.0f'))

        label_h1_17.append(Label(tab[i], text=':'))

        lbl_B_17.append(Label(tab[i], text='Ratio:'))

        spin_C_17.append(Spinbox(tab[i], from_=00,
                                 to=24, width=3, format='%02.0f'))

        spin_D_17.append(Spinbox(tab[i], from_=00,
                                 to=24, width=3, format='%02.0f'))

        label_h2_17.append(Label(tab[i], text=':'))

        rad_B_17.append(Radiobutton(

            tab[i], text='DD', variable=var_17[i], value=2))

        rad_C_17.append(Radiobutton(
            tab[i], text='LL', variable=var_17[i], value=3))

        # phase18
        phaseLabel_18.append(Label(tab[i], text='Phase 18'))

        rad_A_18.append(Radiobutton(
            tab[i], text='LD', variable=var_18[i], value=1))

        lbl_A_18.append(Label(tab[i], text='On:'))

        spin_A_18.append(Spinbox(tab[i], from_=00,
                                 to=24, width=3, format='%02.0f'))

        spin_B_18.append(Spinbox(tab[i], from_=00,
                                 to=59, width=3, format='%02.0f'))

        label_h1_18.append(Label(tab[i], text=':'))

        lbl_B_18.append(Label(tab[i], text='Ratio:'))

        spin_C_18.append(Spinbox(tab[i], from_=00,
                                 to=24, width=3, format='%02.0f'))

        spin_D_18.append(Spinbox(tab[i], from_=00,
                                 to=24, width=3, format='%02.0f'))

        label_h2_18.append(Label(tab[i], text=':'))

        rad_B_18.append(Radiobutton(

            tab[i], text='DD', variable=var_18[i], value=2))

        rad_C_18.append(Radiobutton(
            tab[i], text='LL', variable=var_18[i], value=3))

        # phase19
        phaseLabel_19.append(Label(tab[i], text='Phase 19'))

        rad_A_19.append(Radiobutton(
            tab[i], text='LD', variable=var_19[i], value=1))

        lbl_A_19.append(Label(tab[i], text='On:'))

        spin_A_19.append(Spinbox(tab[i], from_=00,
                                 to=24, width=3, format='%02.0f'))

        spin_B_19.append(Spinbox(tab[i], from_=00,
                                 to=59, width=3, format='%02.0f'))

        label_h1_19.append(Label(tab[i], text=':'))

        lbl_B_19.append(Label(tab[i], text='Ratio:'))

        spin_C_19.append(Spinbox(tab[i], from_=00,
                                 to=24, width=3, format='%02.0f'))

        spin_D_19.append(Spinbox(tab[i], from_=00,
                                 to=24, width=3, format='%02.0f'))

        label_h2_19.append(Label(tab[i], text=':'))

        rad_B_19.append(Radiobutton(

            tab[i], text='DD', variable=var_19[i], value=2))

        rad_C_19.append(Radiobutton(
            tab[i], text='LL', variable=var_19[i], value=3))

        # phase20
        phaseLabel_20.append(Label(tab[i], text='Phase 20'))

        rad_A_20.append(Radiobutton(
            tab[i], text='LD', variable=var_20[i], value=1))

        lbl_A_20.append(Label(tab[i], text='On:'))

        spin_A_20.append(Spinbox(tab[i], from_=00,
                                 to=24, width=3, format='%02.0f'))

        spin_B_20.append(Spinbox(tab[i], from_=00,
                                 to=59, width=3, format='%02.0f'))

        label_h1_20.append(Label(tab[i], text=':'))

        lbl_B_20.append(Label(tab[i], text='Ratio:'))

        spin_C_20.append(Spinbox(tab[i], from_=00,
                                 to=24, width=3, format='%02.0f'))

        spin_D_20.append(Spinbox(tab[i], from_=00,
                                 to=24, width=3, format='%02.0f'))

        label_h2_20.append(Label(tab[i], text=':'))

        rad_B_20.append(Radiobutton(

            tab[i], text='DD', variable=var_20[i], value=2))

        rad_C_20.append(Radiobutton(
            tab[i], text='LL', variable=var_20[i], value=3))

        tab_title2.append(

            Label(tab[i], text='Recording status', anchor='center'))

        boxrec_text.append(StringVar())

        boxrec_stat.append(Label(tab[i], textvariable=boxrec_text[i],

                                 anchor='center', justify=LEFT))

    for i in boxes:

        boxsched_text[i].set('Schedule not set.')

        # phase 1

        spin_A_1[i].delete(0, 'end')

        spin_A_1[i].insert(0, '07')

        spin_B_1[i].delete(0, 'end')

        spin_B_1[i].insert(0, '00')

        spin_C_1[i].delete(0, 'end')

        spin_C_1[i].insert(0, '12')

        spin_D_1[i].delete(0, 'end')

        spin_D_1[i].insert(0, '12')

        phaseLabel_1[i].grid(column=0, row=1+row_adj, padx=15, pady=5)

        rad_A_1[i].grid(column=1, row=1+row_adj, pady=5)

        lbl_A_1[i].grid(column=2, row=1+row_adj, pady=5)

        spin_A_1[i].grid(column=3, row=1+row_adj, pady=5)

        label_h1_1[i].grid(column=4, row=1+row_adj, pady=5, sticky='w')

        spin_B_1[i].grid(column=5, row=1+row_adj, pady=5)

        lbl_B_1[i].grid(column=6, row=1+row_adj, pady=5)

        spin_C_1[i].grid(column=7, row=1+row_adj, pady=5)

        label_h2_1[i].grid(column=8, row=1+row_adj, pady=5, sticky='w')

        spin_D_1[i].grid(column=9, row=1+row_adj, pady=5)

        rad_B_1[i].grid(column=10, row=1+row_adj, padx=15, pady=5)

        rad_C_1[i].grid(column=11, row=1+row_adj, pady=5)

        # phase 2

        spin_A_2[i].delete(0, 'end')

        spin_A_2[i].insert(0, '07')

        spin_B_2[i].delete(0, 'end')

        spin_B_2[i].insert(0, '00')

        spin_C_2[i].delete(0, 'end')

        spin_C_2[i].insert(0, '12')

        spin_D_2[i].delete(0, 'end')

        spin_D_2[i].insert(0, '12')

        phaseLabel_2[i].grid(column=0, row=2+row_adj, padx=15, pady=5)

        rad_A_2[i].grid(column=1, row=2+row_adj, pady=5)

        lbl_A_2[i].grid(column=2, row=2+row_adj, pady=5)

        spin_A_2[i].grid(column=3, row=2+row_adj, pady=5)

        label_h1_2[i].grid(column=4, row=2+row_adj, pady=5)

        spin_B_2[i].grid(column=5, row=2+row_adj, pady=5)

        lbl_B_2[i].grid(column=6, row=2+row_adj, pady=5)

        spin_C_2[i].grid(column=7, row=2+row_adj, pady=5)

        label_h2_2[i].grid(column=8, row=2+row_adj, pady=5)

        spin_D_2[i].grid(column=9, row=2+row_adj, pady=5)

        rad_B_2[i].grid(column=10, row=2+row_adj, padx=15, pady=5)

        rad_C_2[i].grid(column=11, row=2+row_adj, pady=5)

        # phase 3

        spin_A_3[i].delete(0, 'end')

        spin_A_3[i].insert(0, '07')

        spin_B_3[i].delete(0, 'end')

        spin_B_3[i].insert(0, '00')

        spin_C_3[i].delete(0, 'end')

        spin_C_3[i].insert(0, '12')

        spin_D_3[i].delete(0, 'end')

        spin_D_3[i].insert(0, '12')

        phaseLabel_3[i].grid(column=0, row=3+row_adj, padx=15, pady=5)

        rad_A_3[i].grid(column=1, row=3+row_adj, pady=5)

        lbl_A_3[i].grid(column=2, row=3+row_adj, pady=5)

        spin_A_3[i].grid(column=3, row=3+row_adj, pady=5)

        label_h1_3[i].grid(column=4, row=3+row_adj, pady=5)

        spin_B_3[i].grid(column=5, row=3+row_adj, pady=5)

        lbl_B_3[i].grid(column=6, row=3+row_adj, pady=5)

        spin_C_3[i].grid(column=7, row=3+row_adj, pady=5)

        label_h2_3[i].grid(column=8, row=3+row_adj, pady=5)

        spin_D_3[i].grid(column=9, row=3+row_adj, pady=5)

        rad_B_3[i].grid(column=10, row=3+row_adj, padx=15, pady=5)

        rad_C_3[i].grid(column=11, row=3+row_adj, pady=5)

        # phase 4

        spin_A_4[i].delete(0, 'end')

        spin_A_4[i].insert(0, '07')

        spin_B_4[i].delete(0, 'end')

        spin_B_4[i].insert(0, '00')

        spin_C_4[i].delete(0, 'end')

        spin_C_4[i].insert(0, '12')

        spin_D_4[i].delete(0, 'end')

        spin_D_4[i].insert(0, '12')

        phaseLabel_4[i].grid(column=0, row=4+row_adj, padx=15, pady=5)

        rad_A_4[i].grid(column=1, row=4+row_adj, pady=5)

        lbl_A_4[i].grid(column=2, row=4+row_adj, pady=5)

        spin_A_4[i].grid(column=3, row=4+row_adj, pady=5)

        label_h1_4[i].grid(column=4, row=4+row_adj, pady=5)

        spin_B_4[i].grid(column=5, row=4+row_adj, pady=5)

        lbl_B_4[i].grid(column=6, row=4+row_adj, pady=5)

        spin_C_4[i].grid(column=7, row=4+row_adj, pady=5)

        label_h2_4[i].grid(column=8, row=4+row_adj, pady=5)

        spin_D_4[i].grid(column=9, row=4+row_adj, pady=5)

        rad_B_4[i].grid(column=10, row=4+row_adj, padx=15, pady=5)

        rad_C_4[i].grid(column=11, row=4+row_adj, pady=5)

        # phase 5

        spin_A_5[i].delete(0, 'end')

        spin_A_5[i].insert(0, '07')

        spin_B_5[i].delete(0, 'end')

        spin_B_5[i].insert(0, '00')

        spin_C_5[i].delete(0, 'end')

        spin_C_5[i].insert(0, '12')

        spin_D_5[i].delete(0, 'end')

        spin_D_5[i].insert(0, '12')

        phaseLabel_5[i].grid(column=0, row=5+row_adj, padx=15, pady=5)

        rad_A_5[i].grid(column=1, row=5+row_adj, pady=5)

        lbl_A_5[i].grid(column=2, row=5+row_adj, pady=5)

        spin_A_5[i].grid(column=3, row=5+row_adj, pady=5)

        label_h1_5[i].grid(column=4, row=5+row_adj, pady=5)

        spin_B_5[i].grid(column=5, row=5+row_adj, pady=5)

        lbl_B_5[i].grid(column=6, row=5+row_adj, pady=5)

        spin_C_5[i].grid(column=7, row=5+row_adj, pady=5)

        label_h2_5[i].grid(column=8, row=5+row_adj, pady=5)

        spin_D_5[i].grid(column=9, row=5+row_adj, pady=5)

        rad_B_5[i].grid(column=10, row=5+row_adj, padx=15, pady=5)

        rad_C_5[i].grid(column=11, row=5+row_adj, pady=5)
        # phase 6

        spin_A_6[i].delete(0, 'end')

        spin_A_6[i].insert(0, '07')

        spin_B_6[i].delete(0, 'end')

        spin_B_6[i].insert(0, '00')

        spin_C_6[i].delete(0, 'end')

        spin_C_6[i].insert(0, '12')

        spin_D_6[i].delete(0, 'end')

        spin_D_6[i].insert(0, '12')

        phaseLabel_6[i].grid(column=0, row=6+row_adj, padx=15, pady=5)

        rad_A_6[i].grid(column=1, row=6+row_adj, pady=5)

        lbl_A_6[i].grid(column=2, row=6+row_adj, pady=5)

        spin_A_6[i].grid(column=3, row=6+row_adj, pady=5)

        label_h1_6[i].grid(column=4, row=6+row_adj, pady=5)

        spin_B_6[i].grid(column=5, row=6+row_adj, pady=5)

        lbl_B_6[i].grid(column=6, row=6+row_adj, pady=5)

        spin_C_6[i].grid(column=7, row=6+row_adj, pady=5)

        label_h2_6[i].grid(column=8, row=6+row_adj, pady=5)

        spin_D_6[i].grid(column=9, row=6+row_adj, pady=5)

        rad_B_6[i].grid(column=10, row=6+row_adj, padx=15, pady=5)

        rad_C_6[i].grid(column=11, row=6+row_adj, pady=5)
        # phase 7

        spin_A_7[i].delete(0, 'end')

        spin_A_7[i].insert(0, '07')

        spin_B_7[i].delete(0, 'end')

        spin_B_7[i].insert(0, '00')

        spin_C_7[i].delete(0, 'end')

        spin_C_7[i].insert(0, '12')

        spin_D_7[i].delete(0, 'end')

        spin_D_7[i].insert(0, '12')

        phaseLabel_7[i].grid(column=0, row=7+row_adj, padx=15, pady=5)

        rad_A_7[i].grid(column=1, row=7+row_adj, pady=5)

        lbl_A_7[i].grid(column=2, row=7+row_adj, pady=5)

        spin_A_7[i].grid(column=3, row=7+row_adj, pady=5)

        label_h1_7[i].grid(column=4, row=7+row_adj, pady=5)

        spin_B_7[i].grid(column=5, row=7+row_adj, pady=5)

        lbl_B_7[i].grid(column=6, row=7+row_adj, pady=5)

        spin_C_7[i].grid(column=7, row=7+row_adj, pady=5)

        label_h2_7[i].grid(column=8, row=7+row_adj, pady=5)

        spin_D_7[i].grid(column=9, row=7+row_adj, pady=5)

        rad_B_7[i].grid(column=10, row=7+row_adj, padx=15, pady=5)

        rad_C_7[i].grid(column=11, row=7+row_adj, pady=5)
        # phase 8

        spin_A_8[i].delete(0, 'end')

        spin_A_8[i].insert(0, '07')

        spin_B_8[i].delete(0, 'end')

        spin_B_8[i].insert(0, '00')

        spin_C_8[i].delete(0, 'end')

        spin_C_8[i].insert(0, '12')

        spin_D_8[i].delete(0, 'end')

        spin_D_8[i].insert(0, '12')

        phaseLabel_8[i].grid(column=0, row=8+row_adj, padx=15, pady=5)

        rad_A_8[i].grid(column=1, row=8+row_adj, pady=5)

        lbl_A_8[i].grid(column=2, row=8+row_adj, pady=5)

        spin_A_8[i].grid(column=3, row=8+row_adj, pady=5)

        label_h1_8[i].grid(column=4, row=8+row_adj, pady=5)

        spin_B_8[i].grid(column=5, row=8+row_adj, pady=5)

        lbl_B_8[i].grid(column=6, row=8+row_adj, pady=5)

        spin_C_8[i].grid(column=7, row=8+row_adj, pady=5)

        label_h2_8[i].grid(column=8, row=8+row_adj, pady=5)

        spin_D_8[i].grid(column=9, row=8+row_adj, pady=5)

        rad_B_8[i].grid(column=10, row=8+row_adj, padx=15, pady=5)

        rad_C_8[i].grid(column=11, row=8+row_adj, pady=5)

        # phase 9

        spin_A_9[i].delete(0, 'end')

        spin_A_9[i].insert(0, '07')

        spin_B_9[i].delete(0, 'end')

        spin_B_9[i].insert(0, '00')

        spin_C_9[i].delete(0, 'end')

        spin_C_9[i].insert(0, '12')

        spin_D_9[i].delete(0, 'end')

        spin_D_9[i].insert(0, '12')

        phaseLabel_9[i].grid(column=0, row=9+row_adj, padx=15, pady=5)

        rad_A_9[i].grid(column=1, row=9+row_adj, pady=5)

        lbl_A_9[i].grid(column=2, row=9+row_adj, pady=5)

        spin_A_9[i].grid(column=3, row=9+row_adj, pady=5)

        label_h1_9[i].grid(column=4, row=9+row_adj, pady=5)

        spin_B_9[i].grid(column=5, row=9+row_adj, pady=5)

        lbl_B_9[i].grid(column=6, row=9+row_adj, pady=5)

        spin_C_9[i].grid(column=7, row=9+row_adj, pady=5)

        label_h2_9[i].grid(column=8, row=9+row_adj, pady=5)

        spin_D_9[i].grid(column=9, row=9+row_adj, pady=5)

        rad_B_9[i].grid(column=10, row=9+row_adj, padx=15, pady=5)

        rad_C_9[i].grid(column=11, row=9+row_adj, pady=5)

        # phase 10

        spin_A_10[i].delete(0, 'end')

        spin_A_10[i].insert(0, '07')

        spin_B_10[i].delete(0, 'end')

        spin_B_10[i].insert(0, '00')

        spin_C_10[i].delete(0, 'end')

        spin_C_10[i].insert(0, '12')

        spin_D_10[i].delete(0, 'end')

        spin_D_10[i].insert(0, '12')

        phaseLabel_10[i].grid(column=0, row=10+row_adj, padx=15, pady=5)

        rad_A_10[i].grid(column=1, row=10+row_adj, pady=5)

        lbl_A_10[i].grid(column=2, row=10+row_adj, pady=5)

        spin_A_10[i].grid(column=3, row=10+row_adj, pady=5)

        label_h1_10[i].grid(column=4, row=10+row_adj, pady=5)

        spin_B_10[i].grid(column=5, row=10+row_adj, pady=5)

        lbl_B_10[i].grid(column=6, row=10+row_adj, pady=5)

        spin_C_10[i].grid(column=7, row=10+row_adj, pady=5)

        label_h2_10[i].grid(column=8, row=10+row_adj, pady=5)

        spin_D_10[i].grid(column=9, row=10+row_adj, pady=5)

        rad_B_10[i].grid(column=10, row=10+row_adj, padx=15, pady=5)

        rad_C_10[i].grid(column=11, row=10+row_adj, pady=5)
        # phase 11

        spin_A_11[i].delete(0, 'end')

        spin_A_11[i].insert(0, '07')

        spin_B_11[i].delete(0, 'end')

        spin_B_11[i].insert(0, '00')

        spin_C_11[i].delete(0, 'end')

        spin_C_11[i].insert(0, '12')

        spin_D_11[i].delete(0, 'end')

        spin_D_11[i].insert(0, '12')

        phaseLabel_11[i].grid(column=0, row=11+row_adj, padx=15, pady=5)

        rad_A_11[i].grid(column=1, row=11+row_adj, pady=5)

        lbl_A_11[i].grid(column=2, row=11+row_adj, pady=5)

        spin_A_11[i].grid(column=3, row=11+row_adj, pady=5)

        label_h1_11[i].grid(column=4, row=11+row_adj, pady=5)

        spin_B_11[i].grid(column=5, row=11+row_adj, pady=5)

        lbl_B_11[i].grid(column=6, row=11+row_adj, pady=5)

        spin_C_11[i].grid(column=7, row=11+row_adj, pady=5)

        label_h2_11[i].grid(column=8, row=11+row_adj, pady=5)

        spin_D_11[i].grid(column=9, row=11+row_adj, pady=5)

        rad_B_11[i].grid(column=10, row=11+row_adj, padx=15, pady=5)

        rad_C_11[i].grid(column=11, row=11+row_adj, pady=5)
        # phase 12

        spin_A_12[i].delete(0, 'end')

        spin_A_12[i].insert(0, '07')

        spin_B_12[i].delete(0, 'end')

        spin_B_12[i].insert(0, '00')

        spin_C_12[i].delete(0, 'end')

        spin_C_12[i].insert(0, '12')

        spin_D_12[i].delete(0, 'end')

        spin_D_12[i].insert(0, '12')

        phaseLabel_12[i].grid(column=0, row=12+row_adj, padx=15, pady=5)

        rad_A_12[i].grid(column=1, row=12+row_adj, pady=5)

        lbl_A_12[i].grid(column=2, row=12+row_adj, pady=5)

        spin_A_12[i].grid(column=3, row=12+row_adj, pady=5)

        label_h1_12[i].grid(column=4, row=12+row_adj, pady=5)

        spin_B_12[i].grid(column=5, row=12+row_adj, pady=5)

        lbl_B_12[i].grid(column=6, row=12+row_adj, pady=5)

        spin_C_12[i].grid(column=7, row=12+row_adj, pady=5)

        label_h2_12[i].grid(column=8, row=12+row_adj, pady=5)

        spin_D_12[i].grid(column=9, row=12+row_adj, pady=5)

        rad_B_12[i].grid(column=10, row=12+row_adj, padx=15, pady=5)

        rad_C_12[i].grid(column=11, row=12+row_adj, pady=5)

        # phase 13

        spin_A_13[i].delete(0, 'end')

        spin_A_13[i].insert(0, '07')

        spin_B_13[i].delete(0, 'end')

        spin_B_13[i].insert(0, '00')

        spin_C_13[i].delete(0, 'end')

        spin_C_13[i].insert(0, '12')

        spin_D_13[i].delete(0, 'end')

        spin_D_13[i].insert(0, '12')

        phaseLabel_13[i].grid(column=0, row=13+row_adj, padx=15, pady=5)

        rad_A_13[i].grid(column=1, row=13+row_adj, pady=5)

        lbl_A_13[i].grid(column=2, row=13+row_adj, pady=5)

        spin_A_13[i].grid(column=3, row=13+row_adj, pady=5)

        label_h1_13[i].grid(column=4, row=13+row_adj, pady=5)

        spin_B_13[i].grid(column=5, row=13+row_adj, pady=5)

        lbl_B_13[i].grid(column=6, row=13+row_adj, pady=5)

        spin_C_13[i].grid(column=7, row=13+row_adj, pady=5)

        label_h2_13[i].grid(column=8, row=13+row_adj, pady=5)

        spin_D_13[i].grid(column=9, row=13+row_adj, pady=5)

        rad_B_13[i].grid(column=10, row=13+row_adj, padx=15, pady=5)

        rad_C_13[i].grid(column=11, row=13+row_adj, pady=5)

        # phase 14

        spin_A_14[i].delete(0, 'end')

        spin_A_14[i].insert(0, '07')

        spin_B_14[i].delete(0, 'end')

        spin_B_14[i].insert(0, '00')

        spin_C_14[i].delete(0, 'end')

        spin_C_14[i].insert(0, '12')

        spin_D_14[i].delete(0, 'end')

        spin_D_14[i].insert(0, '12')

        phaseLabel_14[i].grid(column=0, row=14+row_adj, padx=15, pady=5)

        rad_A_14[i].grid(column=1, row=14+row_adj, pady=5)

        lbl_A_14[i].grid(column=2, row=14+row_adj, pady=5)

        spin_A_14[i].grid(column=3, row=14+row_adj, pady=5)

        label_h1_14[i].grid(column=4, row=14+row_adj, pady=5)

        spin_B_14[i].grid(column=5, row=14+row_adj, pady=5)

        lbl_B_14[i].grid(column=6, row=14+row_adj, pady=5)

        spin_C_14[i].grid(column=7, row=14+row_adj, pady=5)

        label_h2_14[i].grid(column=8, row=14+row_adj, pady=5)

        spin_D_14[i].grid(column=9, row=14+row_adj, pady=5)

        rad_B_14[i].grid(column=10, row=14+row_adj, padx=15, pady=5)

        rad_C_14[i].grid(column=11, row=14+row_adj, pady=5)
        # phase 15

        spin_A_15[i].delete(0, 'end')

        spin_A_15[i].insert(0, '07')

        spin_B_15[i].delete(0, 'end')

        spin_B_15[i].insert(0, '00')

        spin_C_15[i].delete(0, 'end')

        spin_C_15[i].insert(0, '12')

        spin_D_15[i].delete(0, 'end')

        spin_D_15[i].insert(0, '12')

        phaseLabel_15[i].grid(column=0, row=15+row_adj, padx=15, pady=5)

        rad_A_15[i].grid(column=1, row=15+row_adj, pady=5)

        lbl_A_15[i].grid(column=2, row=15+row_adj, pady=5)

        spin_A_15[i].grid(column=3, row=15+row_adj, pady=5)

        label_h1_15[i].grid(column=4, row=15+row_adj, pady=5)

        spin_B_15[i].grid(column=5, row=15+row_adj, pady=5)

        lbl_B_15[i].grid(column=6, row=15+row_adj, pady=5)

        spin_C_15[i].grid(column=7, row=15+row_adj, pady=5)

        label_h2_15[i].grid(column=8, row=15+row_adj, pady=5)

        spin_D_15[i].grid(column=9, row=15+row_adj, pady=5)

        rad_B_15[i].grid(column=10, row=15+row_adj, padx=15, pady=5)

        rad_C_15[i].grid(column=11, row=15+row_adj, pady=5)
        # phase 16

        spin_A_16[i].delete(0, 'end')

        spin_A_16[i].insert(0, '07')

        spin_B_16[i].delete(0, 'end')

        spin_B_16[i].insert(0, '00')

        spin_C_16[i].delete(0, 'end')

        spin_C_16[i].insert(0, '12')

        spin_D_16[i].delete(0, 'end')

        spin_D_16[i].insert(0, '12')

        phaseLabel_16[i].grid(column=0, row=16+row_adj, padx=15, pady=5)

        rad_A_16[i].grid(column=1, row=16+row_adj, pady=5)

        lbl_A_16[i].grid(column=2, row=16+row_adj, pady=5)

        spin_A_16[i].grid(column=3, row=16+row_adj, pady=5)

        label_h1_16[i].grid(column=4, row=16+row_adj, pady=5)

        spin_B_16[i].grid(column=5, row=16+row_adj, pady=5)

        lbl_B_16[i].grid(column=6, row=16+row_adj, pady=5)

        spin_C_16[i].grid(column=7, row=16+row_adj, pady=5)

        label_h2_16[i].grid(column=8, row=16+row_adj, pady=5)

        spin_D_16[i].grid(column=9, row=16+row_adj, pady=5)

        rad_B_16[i].grid(column=10, row=16+row_adj, padx=15, pady=5)

        rad_C_16[i].grid(column=11, row=16+row_adj, pady=5)
        # phase 17

        spin_A_17[i].delete(0, 'end')

        spin_A_17[i].insert(0, '07')

        spin_B_17[i].delete(0, 'end')

        spin_B_17[i].insert(0, '00')

        spin_C_17[i].delete(0, 'end')

        spin_C_17[i].insert(0, '12')

        spin_D_17[i].delete(0, 'end')

        spin_D_17[i].insert(0, '12')

        phaseLabel_17[i].grid(column=0, row=17+row_adj, padx=15, pady=5)

        rad_A_17[i].grid(column=1, row=17+row_adj, pady=5)

        lbl_A_17[i].grid(column=2, row=17+row_adj, pady=5)

        spin_A_17[i].grid(column=3, row=17+row_adj, pady=5)

        label_h1_17[i].grid(column=4, row=17+row_adj, pady=5)

        spin_B_17[i].grid(column=5, row=17+row_adj, pady=5)

        lbl_B_17[i].grid(column=6, row=17+row_adj, pady=5)

        spin_C_17[i].grid(column=7, row=17+row_adj, pady=5)

        label_h2_17[i].grid(column=8, row=17+row_adj, pady=5)

        spin_D_17[i].grid(column=9, row=17+row_adj, pady=5)

        rad_B_17[i].grid(column=10, row=17+row_adj, padx=15, pady=5)

        rad_C_17[i].grid(column=11, row=17+row_adj, pady=5)
        # phase 18

        spin_A_18[i].delete(0, 'end')

        spin_A_18[i].insert(0, '07')

        spin_B_18[i].delete(0, 'end')

        spin_B_18[i].insert(0, '00')

        spin_C_18[i].delete(0, 'end')

        spin_C_18[i].insert(0, '12')

        spin_D_18[i].delete(0, 'end')

        spin_D_18[i].insert(0, '12')

        phaseLabel_18[i].grid(column=0, row=18+row_adj, padx=15, pady=5)

        rad_A_18[i].grid(column=1, row=18+row_adj, pady=5)

        lbl_A_18[i].grid(column=2, row=18+row_adj, pady=5)

        spin_A_18[i].grid(column=3, row=18+row_adj, pady=5)

        label_h1_18[i].grid(column=4, row=18+row_adj, pady=5)

        spin_B_18[i].grid(column=5, row=18+row_adj, pady=5)

        lbl_B_18[i].grid(column=6, row=18+row_adj, pady=5)

        spin_C_18[i].grid(column=7, row=18+row_adj, pady=5)

        label_h2_18[i].grid(column=8, row=18+row_adj, pady=5)

        spin_D_18[i].grid(column=9, row=18+row_adj, pady=5)

        rad_B_18[i].grid(column=10, row=18+row_adj, padx=15, pady=5)

        rad_C_18[i].grid(column=11, row=18+row_adj, pady=5)
        # phase 19

        spin_A_19[i].delete(0, 'end')

        spin_A_19[i].insert(0, '07')

        spin_B_19[i].delete(0, 'end')

        spin_B_19[i].insert(0, '00')

        spin_C_19[i].delete(0, 'end')

        spin_C_19[i].insert(0, '12')

        spin_D_19[i].delete(0, 'end')

        spin_D_19[i].insert(0, '12')

        phaseLabel_19[i].grid(column=0, row=19+row_adj, padx=15, pady=5)

        rad_A_19[i].grid(column=1, row=19+row_adj, pady=5)

        lbl_A_19[i].grid(column=2, row=19+row_adj, pady=5)

        spin_A_19[i].grid(column=3, row=19+row_adj, pady=5)

        label_h1_19[i].grid(column=4, row=19+row_adj, pady=5)

        spin_B_19[i].grid(column=5, row=19+row_adj, pady=5)

        lbl_B_19[i].grid(column=6, row=19+row_adj, pady=5)

        spin_C_19[i].grid(column=7, row=19+row_adj, pady=5)

        label_h2_19[i].grid(column=8, row=19+row_adj, pady=5)

        spin_D_19[i].grid(column=9, row=19+row_adj, pady=5)

        rad_B_19[i].grid(column=10, row=19+row_adj, padx=15, pady=5)

        rad_C_19[i].grid(column=11, row=19+row_adj, pady=5)
        # phase 20

        spin_A_20[i].delete(0, 'end')

        spin_A_20[i].insert(0, '07')

        spin_B_20[i].delete(0, 'end')

        spin_B_20[i].insert(0, '00')

        spin_C_20[i].delete(0, 'end')

        spin_C_20[i].insert(0, '12')

        spin_D_20[i].delete(0, 'end')

        spin_D_20[i].insert(0, '12')

        phaseLabel_20[i].grid(column=0, row=20+row_adj, padx=15, pady=5)

        rad_A_20[i].grid(column=1, row=20+row_adj, pady=5)

        lbl_A_20[i].grid(column=2, row=20+row_adj, pady=5)

        spin_A_20[i].grid(column=3, row=20+row_adj, pady=5)

        label_h1_20[i].grid(column=4, row=20+row_adj, pady=5)

        spin_B_20[i].grid(column=5, row=20+row_adj, pady=5)

        lbl_B_20[i].grid(column=6, row=20+row_adj, pady=5)

        spin_C_20[i].grid(column=7, row=20+row_adj, pady=5)

        label_h2_20[i].grid(column=8, row=20+row_adj, pady=5)

        spin_D_20[i].grid(column=9, row=20+row_adj, pady=5)

        rad_B_20[i].grid(column=10, row=20+row_adj, padx=15, pady=5)

        rad_C_20[i].grid(column=11, row=20+row_adj, pady=5)

        # Other stuffs

        btnAll[i].grid(column=16, row=1+row_adj, pady=5,
                       columnspan='1', sticky='w')

        boxsched_stat[i].grid(column=3, row=4+row_adj,
                              columnspan='8', sticky='w')

        tab_title2[i].grid(column=12, row=row_adj+20,
                           columnspan='27', sticky='we')

        boxrec_text[i].set('Recording not started yet.')

        boxrec_stat[i].grid(column=12, row=row_adj+21,
                            columnspan='27', sticky='we')

        tab_control.pack(expand=1, fill='both')

        window.update_idletasks()

    # Main loop

    window.mainloop()
