from faulthandler import disable
import serial   # For Serial communication
import time     # Required for using delay functions
import datetime  # For date-time setting and timedelta calculations

import tkinter as tk
from tkinter import DISABLED, Tk, Frame, Canvas, Scrollbar, sys, Label, SUNKEN, BOTH, W, X, Y, Menu, IntVar, VERTICAL, HORIZONTAL, BOTTOM, Spinbox, Entry, ttk, messagebox, Button, StringVar, LEFT, RIGHT, Radiobutton
# from tkinter import * #import INIT set of tkinter library for GUI

from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo

try:
    from tkinter import filedialog
except ImportError:
    fileDialog = tk.filedialog
import threading  # To run Arduino loop and tkinter loop alongside
import serial.tools.list_ports  # For identifying Arduino port
from BoxSchedule import BoxSchedule, PhaseSchedule, getDarkLightValue, inverseDarkLightValue, StatusBar
import numpy as np
import traceback



# sudo chmod 666 /dev/ttyACM0


# Global variables 1_1 = Box_Phases
global hourOn1_1, minOn1_1, hourOff1_1, minOff1_1, dark1_1, light1_1
global hourOn2_1, minOn2_1, hourOff2_1, minOff2_1, dark2_1, light2_1
global hourOn3_1, minOn3_1, hourOff3_1, minOff3_1, dark3_1, light3_1
global hourOn4_1, minOn4_1, hourOff4_1, minOff4_1, dark4_1, light4_1
global hourOn5_1, minOn5_1, hourOff5_1, minOff5_1, dark5_1, light5_1

global hourOn1_2, minOn1_2, hourOff1_2, minOff1_2, date1_2, month1_2, year1_2, dark1_2, light1_2, hourFrom1_2, minuteFrom1_2
global hourOn2_2, minOn2_2, hourOff2_2, minOff2_2, date2_2, month2_2, year2_2, dark2_2, light2_2, hourFrom2_2, minuteFrom2_2
global hourOn3_2, minOn3_2, hourOff3_2, minOff3_2, date3_2, month3_2, year3_2, dark3_2, light3_2, hourFrom3_2, minuteFrom3_2
global hourOn4_2, minOn4_2, hourOff4_2, minOff4_2, date4_2, month4_2, year4_2, dark4_2, light4_2, hourFrom4_2, minuteFrom4_2
global hourOn5_2, minOn5_2, hourOff5_2, minOff5_2, date5_2, month5_2, year5_2, dark5_2, light5_2, hourFrom5_2, minuteFrom5_2

global hourOn1_3, minOn1_3, hourOff1_3, minOff1_3, dark1_3, light1_3, date1_3, month1_3, year1_3, hourFrom1_3, minuteFrom1_3
global hourOn2_3, minOn2_3, hourOff2_3, minOff2_3, dark2_3, light2_3, date2_3, month2_3, year2_3, hourFrom2_3, minuteFrom2_3
global hourOn3_3, minOn3_3, hourOff3_3, minOff3_3, dark3_3, light3_3, date3_3, month3_3, year3_3, hourFrom3_3, minuteFrom3_3
global hourOn4_3, minOn4_3, hourOff4_3, minOff4_3, dark4_3, light4_3, date4_3, month4_3, year4_3, hourFrom4_3, minuteFrom4_3
global hourOn5_3, minOn5_3, hourOff5_3, minOff5_3, dark5_3, light5_3, date5_3, month5_3, year5_3, hourFrom5_3, minuteFrom5_3

global hourOn1_4, minOn1_4, hourOff1_4, minOff1_4, dark1_4, light1_4, date1_4, month1_4, year1_4, hourFrom1_4, minuteFrom1_4
global hourOn2_4, minOn2_4, hourOff2_4, minOff2_4, dark2_4, light2_4, date2_4, month2_4, year2_4, hourFrom2_4, minuteFrom2_4
global hourOn3_4, minOn3_4, hourOff3_4, minOff3_4, dark3_4, light3_4, date3_4, month3_4, year3_4, hourFrom3_4, minuteFrom3_4
global hourOn4_4, minOn4_4, hourOff4_4, minOff4_4, dark4_4, light4_4, date4_4, month4_4, year4_4, hourFrom4_4, minuteFrom4_4
global hourOn5_4, minOn5_4, hourOff5_4, minOff5_4, dark5_4, light5_4, date5_4, month5_4, year5_4, hourFrom5_4, minuteFrom5_4

global hourOn1_5, minOn1_5, hourOff1_5, minOff1_5, dark1_5, light1_5, date1_5, month1_5, year1_5, hourFrom1_5, minuteFrom1_5
global hourOn2_5, minOn2_5, hourOff2_5, minOff2_5, dark2_5, light2_5, date2_5, month2_5, year2_5, hourFrom2_5, minuteFrom2_5
global hourOn3_5, minOn3_5, hourOff3_5, minOff3_5, dark3_5, light3_5, date3_5, month3_5, year3_5, hourFrom3_5, minuteFrom3_5
global hourOn4_5, minOn4_5, hourOff4_5, minOff4_5, dark4_5, light4_5, date4_5, month4_5, year4_5, hourFrom4_5, minuteFrom4_5
global hourOn5_5, minOn5_5, hourOff5_5, minOff5_5, dark5_5, light5_5, date5_5, month5_5, year5_5, hourFrom5_5, minuteFrom5_5

global hourOn1_6, minOn1_6, hourOff1_6, minOff1_6, dark1_6, light1_6, date1_6, month1_6, year1_6, hourFrom1_6, minuteFrom1_6
global hourOn2_6, minOn2_6, hourOff2_6, minOff2_6, dark2_6, light2_6, date2_6, month2_6, year2_6, hourFrom2_6, minuteFrom2_6
global hourOn3_6, minOn3_6, hourOff3_6, minOff3_6, dark3_6, light3_6, date3_6, month3_6, year3_6, hourFrom3_6, minuteFrom3_6
global hourOn4_6, minOn4_6, hourOff4_6, minOff4_6, dark4_6, light4_6, date4_6, month4_6, year4_6, hourFrom4_6, minuteFrom4_6
global hourOn5_6, minOn5_6, hourOff5_6, minOff5_6, dark5_6, light5_6, date5_6, month5_6, year5_6, hourFrom5_6, minuteFrom5_6

global hourOn1_7, minOn1_7, hourOff1_7, minOff1_7, dark1_7, light1_7, date1_7, month1_7, year1_7, hourFrom1_7, minuteFrom1_7
global hourOn2_7, minOn2_7, hourOff2_7, minOff2_7, dark2_7, light2_7, date2_7, month2_7, year2_7, hourFrom2_7, minuteFrom2_7
global hourOn3_7, minOn3_7, hourOff3_7, minOff3_7, dark3_7, light3_7, date3_7, month3_7, year3_7, hourFrom3_7, minuteFrom3_7
global hourOn4_7, minOn4_7, hourOff4_7, minOff4_7, dark4_7, light4_7, date4_7, month4_7, year4_7, hourFrom4_7, minuteFrom4_7
global hourOn5_7, minOn5_7, hourOff5_7, minOff5_7, dark5_7, light5_7, date5_7, month5_7, year5_7, hourFrom5_7, minuteFrom5_7

global hourOn1_8, minOn1_8, hourOff1_8, minOff1_8, dark1_8, light1_8, date1_8, month1_8, year1_8, hourFrom1_8, minuteFrom1_8
global hourOn2_8, minOn2_8, hourOff2_8, minOff2_8, dark2_8, light2_8, date2_8, month2_8, year2_8, hourFrom2_8, minuteFrom2_8
global hourOn3_8, minOn3_8, hourOff3_8, minOff3_8, dark3_8, light3_8, date3_8, month3_8, year3_8, hourFrom3_8, minuteFrom3_8
global hourOn4_8, minOn4_8, hourOff4_8, minOff4_8, dark4_8, light4_8, date4_8, month4_8, year4_8, hourFrom4_8, minuteFrom4_8
global hourOn5_8, minOn5_8, hourOff5_8, minOff5_8, dark5_8, light5_8, date5_8, month5_8, year5_8, hourFrom5_8, minuteFrom5_8

global hourOn1_9, minOn1_9, hourOff1_9, minOff1_9, dark1_9, light1_9, date1_9, month1_9, year1_9, hourFrom1_9, minuteFrom1_9
global hourOn2_9, minOn2_9, hourOff2_9, minOff2_9, dark2_9, light2_9, date2_9, month2_9, year2_9, hourFrom2_9, minuteFrom2_9
global hourOn3_9, minOn3_9, hourOff3_9, minOff3_9, dark3_9, light3_9, date3_9, month3_9, year3_9, hourFrom3_9, minuteFrom3_9
global hourOn4_9, minOn4_9, hourOff4_9, minOff4_9, dark4_9, light4_9, date4_9, month4_9, year4_9, hourFrom4_9, minuteFrom4_9
global hourOn5_9, minOn5_9, hourOff5_9, minOff5_9, dark5_9, light5_9, date5_9, month5_9, year5_9, hourFrom5_9, minuteFrom5_9

global hourOn1_10, minOn1_10, hourOff1_10, minOff1_10, dark1_10, light1_10, date1_10, month1_10, year1_10, hourFrom1_10, minuteFrom1_10
global hourOn2_10, minOn2_10, hourOff2_10, minOff2_10, dark2_10, light2_10, date2_10, month2_10, year2_10, hourFrom2_10, minuteFrom2_10
global hourOn3_10, minOn3_10, hourOff3_10, minOff3_10, dark3_10, light3_10, date3_10, month3_10, year3_10, hourFrom3_10, minuteFrom3_10
global hourOn4_10, minOn4_10, hourOff4_10, minOff4_10, dark4_10, light4_10, date4_10, month4_10, year4_10, hourFrom4_10, minuteFrom4_10
global hourOn5_10, minOn5_10, hourOff5_10, minOff5_10, dark5_10, light5_10, date5_10, month5_10, year5_10, hourFrom5_10, minuteFrom5_10

global hourOn1_11, minOn1_11, hourOff1_11, minOff1_11, dark1_11, light1_11, date1_11, month1_11, year1_11, hourFrom1_11, minuteFrom1_11
global hourOn2_11, minOn2_11, hourOff2_11, minOff2_11, dark2_11, light2_11, date2_11, month2_11, year2_11, hourFrom2_11, minuteFrom2_11
global hourOn3_11, minOn3_11, hourOff3_11, minOff3_11, dark3_11, light3_11, date3_11, month3_11, year3_11, hourFrom3_11, minuteFrom3_11
global hourOn4_11, minOn4_11, hourOff4_11, minOff4_11, dark4_11, light4_11, date4_11, month4_11, year4_11, hourFrom4_11, minuteFrom4_11
global hourOn5_11, minOn5_11, hourOff5_11, minOff5_11, dark5_11, light5_11, date5_11, month5_11, year5_11, hourFrom5_11, minuteFrom5_11

global hourOn1_12, minOn1_12, hourOff1_12, minOff1_12, dark1_12, light1_12, date1_12, month1_12, year1_12, hourFrom1_12, minuteFrom1_12
global hourOn2_12, minOn2_12, hourOff2_12, minOff2_12, dark2_12, light2_12, date2_12, month2_12, year2_12, hourFrom2_12, minuteFrom2_12
global hourOn3_12, minOn3_12, hourOff3_12, minOff3_12, dark3_12, light3_12, date3_12, month3_12, year3_12, hourFrom3_12, minuteFrom3_12
global hourOn4_12, minOn4_12, hourOff4_12, minOff4_12, dark4_12, light4_12, date4_12, month4_12, year4_12, hourFrom4_12, minuteFrom4_12
global hourOn5_12, minOn5_12, hourOff5_12, minOff5_12, dark5_12, light5_12, date5_12, month5_12, year5_12, hourFrom5_12, minuteFrom5_12

global value_mat, input_mat

# global setBox1, setBox2, setBox3, setBox4, setBox5, setBox6, setBox7, setBox8, setBox9, setBox10
global setBox_arr

global savedBoxSchedule, BoxSchedule1, BoxSchedule2, BoxSchedule3, BoxSchedule4, BoxSchedule5, BoxSchedule6, BoxSchedule7, BoxSchedule8, BoxSchedule9, BoxSchedule10

global BOX_N, PHASE_N

global display_string, display_counter

savedBoxSchedule = BoxSchedule()




display_string = ''
display_counter = 0




# Version information



def about():
    return messagebox.showinfo('About',
                               '5-Box Schedule Setter\n' +
                               'LocoBox.py\n\n' +
                               'Version 0.2.10\n' +
                               'Oct 15, 2018\n\n' +
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


def create_tab(parentframe):
        canvas = Canvas(parentframe, width=850, height=200)
        scroll = Scrollbar(parentframe, orient=VERTICAL, command=canvas.yview)
        canvas.grid(row=0, column=0)
        scroll.grid(row=0, column=1, sticky='ns')
        canvas.config(yscrollcommand=scroll.set)
        tab = Frame(canvas, width=200, height=300)
        tab.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
            )
        )
        canvas.create_window(400, 175, window=tab)
        return tab, canvas



# Initialize the windows size and name
window = Tk()
window.title('LocoBox (1-10_box)')
if sys.platform.startswith('win'):
    window.geometry('870x620')
elif sys.platform.startswith('darwin'):
    window.geometry('1200x640')
elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
    window.geometry('900x520')
else:
    window.geometry('1000x440')
status = StatusBar(window)


def change_box_phase_text(value_mat, box_id, phase_id, box_text):
    dark = value_mat[box_id, phase_id, 4]
    light = value_mat[box_id, phase_id, 5]

    if light == '0' and dark == '0':
        box_text.set('                                ')

        box_text.set('From record onset'+' | '+value_mat[box_id, phase_id, 0]+':'+value_mat[box_id,
                     phase_id, 1]+' on>'+value_mat[box_id, phase_id, 2]+':'+value_mat[box_id, phase_id, 3]+' off')
        window.update_idletasks()
    if light == '0' and dark == '1':
        box_text.set('                                ')

        box_text.set('From record onset'+' | '+'DD')
        window.update_idletasks()
    if light == '1' and dark == '0':
        box_text.set('                                ')

        box_text.set('From record onset'+' | '+'LL')
        window.update_idletasks()

# Define functions


def destruct():  # Quit the program
    print('LocoBox ended.')
    window.quit()


def get_data(istate=0):  # Start recording
    status.pack(side='bottom', fill='x')
    status.set('Starting the recording...')
    boxrec_text.set('Preparing for recording.')
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
    global value_mat
    global display_string, display_counter
    try:
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
                t = t + datetime.timedelta(minutes=1)
                serial_obj.write(str.encode(t.strftime('%Y-%m-%d %H:%M:%S')))
            if i == 1:
                phase_id = i-1
                all_boxes_line = ""
                for box_id in range(0, 10):
                    box_line = value_mat[box_id, phase_id, 0] + value_mat[box_id, phase_id,
                                                                          1] + value_mat[box_id, phase_id, 2] + value_mat[box_id, phase_id, 3]
                    all_boxes_line = all_boxes_line + box_line

                serial_obj.write(str.encode(all_boxes_line))

            if i == 2:
                phase_id = 0
                all_boxes_line = ""
                for box_id in range(0, 10):
                    box_line = value_mat[box_id, phase_id, 4] + value_mat[box_id, phase_id,5] 
                    all_boxes_line = all_boxes_line + box_line

                serial_obj.write(str.encode(all_boxes_line))
                

                status.pack(side='bottom', fill='x')
                status.set('Phase 1 schedules sent.')
            if i == 3:
                phase_id = 1
                all_boxes_line = ""
                for box_id in range(0, 10):
                    box_line = value_mat[box_id, phase_id, 0] + value_mat[box_id, phase_id,
                                                                          1] + value_mat[box_id, phase_id, 2] + value_mat[box_id, phase_id, 3]
                    all_boxes_line = all_boxes_line + box_line

                serial_obj.write(str.encode(all_boxes_line))
                

            if i == 4:
                phase_id = 1
                all_boxes_line = ""
                for box_id in range(0, 10):
                    box_line = value_mat[box_id, phase_id, 4] + value_mat[box_id, phase_id,5] 
                    all_boxes_line = all_boxes_line + box_line

                serial_obj.write(str.encode(all_boxes_line))

            if i == 5:
                phase_id = 2
                all_boxes_line = ""
                for box_id in range(0, 10):
                    box_line = value_mat[box_id, phase_id, 5] + value_mat[box_id, phase_id,
                                                                          6] + value_mat[box_id, phase_id, 7] + value_mat[box_id, phase_id, 8]  + value_mat[box_id, phase_id, 9]
                    all_boxes_line = all_boxes_line + box_line
                serial_obj.write(str.encode(all_boxes_line))
                
                status.pack(side='bottom', fill='x')
                status.set('Phase 2 schedules sent.')
            if i == 6:
                phase_id = 2
                all_boxes_line = ""
                for box_id in range(0, 10):
                    box_line = value_mat[box_id, phase_id, 0] + value_mat[box_id, phase_id,
                                                                          1] + value_mat[box_id, phase_id, 2] + value_mat[box_id, phase_id, 3]
                    all_boxes_line = all_boxes_line + box_line

                serial_obj.write(str.encode(all_boxes_line))

            if i == 7:
                phase_id = 2
                all_boxes_line = ""
                for box_id in range(0, 10):
                    box_line = value_mat[box_id, phase_id, 4] + value_mat[box_id, phase_id,5] 
                    all_boxes_line = all_boxes_line + box_line

                serial_obj.write(str.encode(all_boxes_line))


            if i == 8:
                phase_id = 2
                all_boxes_line = ""
                for box_id in range(0, 10):
                    box_line = value_mat[box_id, phase_id, 5] + value_mat[box_id, phase_id,
                                                                          6] + value_mat[box_id, phase_id, 7] + value_mat[box_id, phase_id, 8]  + value_mat[box_id, phase_id, 9]
                    all_boxes_line = all_boxes_line + box_line
                serial_obj.write(str.encode(all_boxes_line))

                status.pack(side='bottom', fill='x')
                status.set('Phase 3 schedules sent.')
            if i == 9:
                phase_id = 3
                all_boxes_line = ""
                for box_id in range(0, 10):
                    box_line = value_mat[box_id, phase_id, 0] + value_mat[box_id, phase_id,
                                                                          1] + value_mat[box_id, phase_id, 2] + value_mat[box_id, phase_id, 3]
                    all_boxes_line = all_boxes_line + box_line

                serial_obj.write(str.encode(all_boxes_line))

            if i == 10:
                phase_id = 3
                all_boxes_line = ""
                for box_id in range(0, 10):
                    box_line = value_mat[box_id, phase_id, 4] + value_mat[box_id, phase_id,5] 
                    all_boxes_line = all_boxes_line + box_line

                serial_obj.write(str.encode(all_boxes_line))


            if i == 11:
                phase_id = 3
                all_boxes_line = ""
                for box_id in range(0, 10):
                    box_line = value_mat[box_id, phase_id, 5] + value_mat[box_id, phase_id,
                                                                          6] + value_mat[box_id, phase_id, 7] + value_mat[box_id, phase_id, 8]  + value_mat[box_id, phase_id, 9]
                    all_boxes_line = all_boxes_line + box_line
                serial_obj.write(str.encode(all_boxes_line))

                status.pack(side='bottom', fill='x')
                status.set('Phase 4 schedules sent.')
            if i == 12:
                phase_id = 4
                all_boxes_line = ""
                for box_id in range(0, 10):
                    box_line = value_mat[box_id, phase_id, 0] + value_mat[box_id, phase_id,
                                                                          1] + value_mat[box_id, phase_id, 2] + value_mat[box_id, phase_id, 3]
                    all_boxes_line = all_boxes_line + box_line

                serial_obj.write(str.encode(all_boxes_line))

            if i == 13:
                phase_id = 4
                all_boxes_line = ""
                for box_id in range(0, 10):
                    box_line = value_mat[box_id, phase_id, 4] + value_mat[box_id, phase_id,5] 
                    all_boxes_line = all_boxes_line + box_line

                serial_obj.write(str.encode(all_boxes_line))
            if i == 14:
                phase_id = 4
                all_boxes_line = ""
                for box_id in range(0, 10):
                    box_line = value_mat[box_id, phase_id, 5] + value_mat[box_id, phase_id,
                                                                          6] + value_mat[box_id, phase_id, 7] + value_mat[box_id, phase_id, 8]  + value_mat[box_id, phase_id, 9]
                    all_boxes_line = all_boxes_line + box_line
                serial_obj.write(str.encode(all_boxes_line))
                status.pack(side='bottom', fill='x')
                status.set('Phase 5 schedules sent.')
            # Phase 6
            if i == 15:
                phase_id = 5
                all_boxes_line = ""
                for box_id in range(0, 10):
                    box_line = value_mat[box_id, phase_id, 0] + value_mat[box_id, phase_id,
                                                                          1] + value_mat[box_id, phase_id, 2] + value_mat[box_id, phase_id, 3]
                    all_boxes_line = all_boxes_line + box_line

            if i == 16:
                phase_id = 5
                all_boxes_line = ""
                for box_id in range(0, 10):
                    box_line = value_mat[box_id, phase_id, 4] + value_mat[box_id, phase_id,5] 
                    all_boxes_line = all_boxes_line + box_line

                serial_obj.write(str.encode(all_boxes_line))

            if i == 17:
                phase_id = 5
                all_boxes_line = ""
                for box_id in range(0, 10):
                    box_line = value_mat[box_id, phase_id, 5] + value_mat[box_id, phase_id,
                                                                          6] + value_mat[box_id, phase_id, 7] + value_mat[box_id, phase_id, 8]  + value_mat[box_id, phase_id, 9]
                    all_boxes_line = all_boxes_line + box_line
                serial_obj.write(str.encode(all_boxes_line))
                status.pack(side='bottom', fill='x')
                status.set('Phase 6 schedules sent.')
            # Phase 7
            if i == 18:
                phase_id = 6
                all_boxes_line = ""
                for box_id in range(0, 10):
                    box_line = value_mat[box_id, phase_id, 0] + value_mat[box_id, phase_id,
                                                                          1] + value_mat[box_id, phase_id, 2] + value_mat[box_id, phase_id, 3]
                    all_boxes_line = all_boxes_line + box_line
            if i == 19:
                phase_id = 6
                all_boxes_line = ""
                for box_id in range(0, 10):
                    box_line = value_mat[box_id, phase_id, 4] + value_mat[box_id, phase_id,5] 
                    all_boxes_line = all_boxes_line + box_line

                serial_obj.write(str.encode(all_boxes_line))
            if i == 20:
                phase_id = 6
                all_boxes_line = ""
                for box_id in range(0, 10):
                    box_line = value_mat[box_id, phase_id, 5] + value_mat[box_id, phase_id,
                                                                          6] + value_mat[box_id, phase_id, 7] + value_mat[box_id, phase_id, 8]  + value_mat[box_id, phase_id, 9]
                    all_boxes_line = all_boxes_line + box_line
                serial_obj.write(str.encode(all_boxes_line))
                status.pack(side='bottom', fill='x')
                status.set('Phase 7 schedules sent.')
            # Phase 8
            if i == 21:
                phase_id = 7
                all_boxes_line = ""
                for box_id in range(0, 10):
                    box_line = value_mat[box_id, phase_id, 0] + value_mat[box_id, phase_id,
                                                                          1] + value_mat[box_id, phase_id, 2] + value_mat[box_id, phase_id, 3]
                    all_boxes_line = all_boxes_line + box_line
            if i == 22:
                phase_id = 7
                all_boxes_line = ""
                for box_id in range(0, 10):
                    box_line = value_mat[box_id, phase_id, 4] + value_mat[box_id, phase_id,5] 
                    all_boxes_line = all_boxes_line + box_line

                serial_obj.write(str.encode(all_boxes_line))

            if i == 23:
                phase_id = 7
                all_boxes_line = ""
                for box_id in range(0, 10):
                    box_line = value_mat[box_id, phase_id, 5] + value_mat[box_id, phase_id,
                                                                          6] + value_mat[box_id, phase_id, 7] + value_mat[box_id, phase_id, 8]  + value_mat[box_id, phase_id, 9]
                    all_boxes_line = all_boxes_line + box_line
                serial_obj.write(str.encode(all_boxes_line))
                status.pack(side='bottom', fill='x')
                status.set('Phase 8 schedules sent.')
            # Phase 9
            if i == 24:
                phase_id = 8
                all_boxes_line = ""
                for box_id in range(0, 10):
                    box_line = value_mat[box_id, phase_id, 0] + value_mat[box_id, phase_id,
                                                                          1] + value_mat[box_id, phase_id, 2] + value_mat[box_id, phase_id, 3]
                    all_boxes_line = all_boxes_line + box_line

            if i == 25:
                phase_id = 8
                all_boxes_line = ""
                for box_id in range(0, 10):
                    box_line = value_mat[box_id, phase_id, 4] + value_mat[box_id, phase_id,5] 
                    all_boxes_line = all_boxes_line + box_line

                serial_obj.write(str.encode(all_boxes_line))

            if i == 26:
                phase_id = 8
                all_boxes_line = ""
                for box_id in range(0, 10):
                    box_line = value_mat[box_id, phase_id, 5] + value_mat[box_id, phase_id,
                                                                          6] + value_mat[box_id, phase_id, 7] + value_mat[box_id, phase_id, 8]  + value_mat[box_id, phase_id, 9]
                    all_boxes_line = all_boxes_line + box_line
                serial_obj.write(str.encode(all_boxes_line))

                status.pack(side='bottom', fill='x')
                status.set('Phase 9 schedules sent.')
            # Phase 10
            if i == 27:
                phase_id = 9
                all_boxes_line = ""
                for box_id in range(0, 10):
                    box_line = value_mat[box_id, phase_id, 0] + value_mat[box_id, phase_id,
                                                                          1] + value_mat[box_id, phase_id, 2] + value_mat[box_id, phase_id, 3]
                    all_boxes_line = all_boxes_line + box_line

            if i == 28:
                phase_id = 9
                all_boxes_line = ""
                for box_id in range(0, 10):
                    box_line = value_mat[box_id, phase_id, 4] + value_mat[box_id, phase_id,5] 
                    all_boxes_line = all_boxes_line + box_line

                serial_obj.write(str.encode(all_boxes_line))

            if i == 29:
                phase_id = 9
                all_boxes_line = ""
                for box_id in range(0, 10):
                    box_line = value_mat[box_id, phase_id, 5] + value_mat[box_id, phase_id,
                                                                          6] + value_mat[box_id, phase_id, 7] + value_mat[box_id, phase_id, 8]  + value_mat[box_id, phase_id, 9]
                    all_boxes_line = all_boxes_line + box_line
                serial_obj.write(str.encode(all_boxes_line))

                status.pack(side='bottom', fill='x')
                status.set('Phase 10 schedules sent.')
            # Phase 11
            if i == 30:
                phase_id = 10
                all_boxes_line = ""
                for box_id in range(0, 10):
                    box_line = value_mat[box_id, phase_id, 0] + value_mat[box_id, phase_id,
                                                                          1] + value_mat[box_id, phase_id, 2] + value_mat[box_id, phase_id, 3]
                    all_boxes_line = all_boxes_line + box_line

            if i == 31:
                phase_id = 10
                all_boxes_line = ""
                for box_id in range(0, 10):
                    box_line = value_mat[box_id, phase_id, 4] + value_mat[box_id, phase_id,5] 
                    all_boxes_line = all_boxes_line + box_line

                serial_obj.write(str.encode(all_boxes_line))

            if i == 32:
                phase_id = 10
                all_boxes_line = ""
                for box_id in range(0, 10):
                    box_line = value_mat[box_id, phase_id, 5] + value_mat[box_id, phase_id,
                                                                          6] + value_mat[box_id, phase_id, 7] + value_mat[box_id, phase_id, 8]  + value_mat[box_id, phase_id, 9]
                    all_boxes_line = all_boxes_line + box_line
                serial_obj.write(str.encode(all_boxes_line))

                status.pack(side='bottom', fill='x')
                status.set('Phase 11 schedules sent.')

            # Phase 12
            if i == 33:
                phase_id = 11
                all_boxes_line = ""
                for box_id in range(0, 10):
                    box_line = value_mat[box_id, phase_id, 0] + value_mat[box_id, phase_id,
                                                                          1] + value_mat[box_id, phase_id, 2] + value_mat[box_id, phase_id, 3]
                    all_boxes_line = all_boxes_line + box_line

            if i == 34:
                phase_id = 11
                all_boxes_line = ""
                for box_id in range(0, 10):
                    box_line = value_mat[box_id, phase_id, 4] + value_mat[box_id, phase_id,5] 
                    all_boxes_line = all_boxes_line + box_line

                serial_obj.write(str.encode(all_boxes_line))

            if i == 35:
                phase_id = 11
                all_boxes_line = ""
                for box_id in range(0, 10):
                    box_line = value_mat[box_id, phase_id, 5] + value_mat[box_id, phase_id,
                                                                          6] + value_mat[box_id, phase_id, 7] + value_mat[box_id, phase_id, 8]  + value_mat[box_id, phase_id, 9]
                    all_boxes_line = all_boxes_line + box_line
                serial_obj.write(str.encode(all_boxes_line))

                status.pack(side='bottom', fill='x')
                status.set('Phase 11 schedules sent.')
                status.set('All schedules transferred. Recording began.')

                for i in range(10):

                    boxrec_text[i].set('Recording on-going.')
                window.update_idletasks()
            i = i+1

            if len(string2) >= 79:
                display_string = string2
                display_counter = counti

                on_tab_change(counti, string2)
                

                window.update_idletasks()
             
                counti = counti+1

                
            
    except Exception:
        traceback.print_exc()
        print('Stopped recording and disconnected from the boxes.')
        status.pack(side='bottom', fill='x')
        status.set('Stopped recording and disconnected from the boxes.')
        boxrec_text.set('Recording stopped.')
        
        window.update_idletasks()

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

def on_tab_change( counti, string2):
    tab = int(tab_control.index('current'))+1
    #tab = event.widget.tab('current')['text']
    if tab == 1:
        boxrec_text.set('# '+str(counti)+'    Time: '+string2[0:8]+'    LED1: '+string2[20:25]+'    '+'PIR1: '+string2[26:31])
    elif tab == 2: 
        boxrec_text.set('# '+str(counti)+'    Time: '+string2[0:8]+'    LED2: '+string2[32:37]+'    '+'PIR2: '+string2[38:43])

    elif tab == 3:
        boxrec_text.set('# '+str(counti)+'    Time: '+string2[0:8]+'    LED3: '+string2[44:49]+'    '+'PIR3: '+string2[50:55])
               
    elif tab == 4:
        boxrec_text.set('# '+str(counti)+'    Time: '+string2[0:8]+'    LED4: '+string2[56:61]+'    '+'PIR4: '+string2[62:67])
    elif tab == 5:
        boxrec_text.set('# '+str(counti)+'    Time: '+string2[0:8]+'    LED5: '+string2[68:73]+'    '+'PIR5: '+string2[74:79])


def on_tab_change_trigger( event):
    global display_counter, display_string
    #tab = int(tab_control.index('current'))+1
    counti = display_counter
    string2 = display_string
    
    tab = event.widget.tab('current')['text']
    
    if tab == 'Box1':
        boxrec_text.set('# '+str(counti)+'    Time: '+string2[0:8]+'    LED1: '+string2[20:25]+'    '+'PIR1: '+string2[26:31])
    elif tab == 'Box2':
        boxrec_text.set('# '+str(counti)+'    Time: '+string2[0:8]+'    LED2: '+string2[32:37]+'    '+'PIR2: '+string2[38:43])
        

    elif tab == 'Box3':
        boxrec_text.set('# '+str(counti)+'    Time: '+string2[0:8]+'    LED3: '+string2[44:49]+'    '+'PIR3: '+string2[50:55])
               
    elif tab == 'Box4':
        boxrec_text.set('# '+str(counti)+'    Time: '+string2[0:8]+'    LED4: '+string2[56:61]+'    '+'PIR4: '+string2[62:67])
    elif tab == 'Box5':
        boxrec_text.set('# '+str(counti)+'    Time: '+string2[0:8]+'    LED5: '+string2[68:73]+'    '+'PIR5: '+string2[74:79])






def save_conf():  # Save schedule configuration
    global value_mat
    status.pack(side='bottom', fill='x')
    status.set('Saving the schedule configuration...')
    config = value_mat.reshape(value_mat.shape[0], -1)
    print(config)

    configfilename = configfilename_entry.get()
    np.savetxt(configfilename, config, fmt='%s') #save as txt    
    status.pack(side='bottom', fill='x')
    status.set('Schedule configuration saved.')






def read_data():  # Read data from file for plotting
    global file_plot
    status.pack(side='bottom', fill='x')
    status.set('Reading the data...')
    file_plot = askopenfilename(filetypes=(("Text files", "*.txt"),
                                           ("All files", "*.*")))
    status.pack(side='bottom', fill='x')
    status.set('Schedule configuration saved.')


def read_conf():  # Read schedule configuration
    global value_mat, input_mat
    status.pack(side='bottom', fill='x')
    status.set('Reading the schedule configuration...')
    configfilename = filedialog.askopenfilename()
    loaded_arr = np.loadtxt(configfilename)
    load_original_arr = loaded_arr.reshape(loaded_arr.shape[0], loaded_arr.shape[1] // 11, 11)
    print("shape of load_original_arr: ", load_original_arr.shape) 
    value_mat = load_original_arr
    print(value_mat)




   
    

    

    

    btnRun['state'] = 'normal'
    recordingmenu.entryconfig('Start new', state='normal')
    show_conf()
    window.update_idletasks()

    status.pack(side='bottom', fill='x')
    status.set('The schedule configuration is loaded.')
    boxsched_text.set('Box schedule loaded.')
    

    window.update_idletasks()


def show_conf():  # Show schedule configuration
    

    #print("hourOn1_1" + str(hourOn1_1))

    col11_1 = Label(tab11, text='Phase 1')
    col11_2 = Label(tab11, text='Phase 2')
    col11_3 = Label(tab11, text='Phase 3')
    col11_4 = Label(tab11, text='Phase 4')
    col11_5 = Label(tab11, text='Phase 5')
    col11_6 = Label(tab11, text='Phase 6')
    col11_7 = Label(tab11, text='Phase 7')
    col11_8 = Label(tab11, text='Phase 8')
    col11_9 = Label(tab11, text='Phase 9')
    col11_10 = Label(tab11, text='Phase 10')
    col11_11 = Label(tab11, text='Phase 11')
    col11_12 = Label(tab11, text='Phase 12')

    row11_1 = Label(tab11, text='Box1')
    row11_2 = Label(tab11, text='Box2')
    row11_3 = Label(tab11, text='Box3')
    row11_4 = Label(tab11, text='Box4')
    row11_5 = Label(tab11, text='Box5')
    row11_1 = Label(tab11, text='Box6')
    row11_2 = Label(tab11, text='Box7')
    row11_3 = Label(tab11, text='Box8')
    row11_4 = Label(tab11, text='Box9')
    row11_5 = Label(tab11, text='Box10')

    col11_1.grid(column=2, row=0, padx=5)
    col11_2.grid(column=4, row=0, padx=5)
    col11_3.grid(column=6, row=0, padx=5)
    col11_4.grid(column=8, row=0, padx=5)
    col11_5.grid(column=10, row=0, padx=5)
    col11_6.grid(column=12, row=0, padx=5)
    col11_7.grid(column=14, row=0, padx=5)
    col11_8.grid(column=16, row=0, padx=5)
    col11_9.grid(column=18, row=0, padx=5)
    col11_10.grid(column=20, row=0, padx=5)
    col11_11.grid(column=22, row=0, padx=5)
    col11_12.grid(column=24, row=0, padx=5)

    schedSep = ttk.Separator(tab11, orient=HORIZONTAL)
    schedSep.grid(column=0, row=1, columnspan='25', sticky='we')
    schedSep2 = ttk.Separator(tab11, orient=VERTICAL)
    schedSep2.grid(column=1, row=2, rowspan='10', sticky='ns')
    schedSep3 = ttk.Separator(tab11, orient=VERTICAL)
    schedSep3.grid(column=3, row=2, rowspan='10', sticky='ns')
    schedSep4 = ttk.Separator(tab11, orient=VERTICAL)
    schedSep4.grid(column=5, row=2, rowspan='10', sticky='ns')
    schedSep5 = ttk.Separator(tab11, orient=VERTICAL)
    schedSep5.grid(column=7, row=2, rowspan='10', sticky='ns')
    schedSep6 = ttk.Separator(tab11, orient=VERTICAL)
    schedSep6.grid(column=9, row=2, rowspan='10', sticky='ns')
    schedSep7 = ttk.Separator(tab11, orient=VERTICAL)
    schedSep7.grid(column=11, row=2, rowspan='10', sticky='ns')
    schedSep8 = ttk.Separator(tab11, orient=VERTICAL)
    schedSep8.grid(column=13, row=2, rowspan='10', sticky='ns')
    schedSep9 = ttk.Separator(tab11, orient=VERTICAL)
    schedSep9.grid(column=15, row=2, rowspan='10', sticky='ns')
    schedSep10 = ttk.Separator(tab11, orient=VERTICAL)
    schedSep10.grid(column=17, row=2, rowspan='10', sticky='ns')
    schedSep11 = ttk.Separator(tab11, orient=VERTICAL)
    schedSep11.grid(column=19, row=2, rowspan='10', sticky='ns')
    schedSep12 = ttk.Separator(tab11, orient=VERTICAL)
    schedSep12.grid(column=21, row=2, rowspan='10', sticky='ns')
    schedSep13 = ttk.Separator(tab11, orient=VERTICAL)
    schedSep13.grid(column=23, row=2, rowspan='10', sticky='ns')
    schedSep14 = ttk.Separator(tab11, orient=VERTICAL)
    schedSep14.grid(column=25, row=2, rowspan='10', sticky='ns')

    row11_1.grid(column=0, row=2, padx=2, pady=0)
    row11_2.grid(column=0, row=3, padx=2, pady=0)
    row11_3.grid(column=0, row=4, padx=2, pady=0)
    row11_4.grid(column=0, row=5, padx=2, pady=0)
    row11_5.grid(column=0, row=6, padx=2, pady=0)

    # array that contains all the stringvars)
    box_pha_text_arr = []
    
    for box_id in range(0, BOX_N):
        phase_var_arr = []
        box_pha_LD_arr = []
        for phase_id in range(0, PHASE_N):
            str_var = StringVar()
            phase_var_arr.append(str_var)
            box_pha_LD = Label(tab11, textvariable=str_var,
                        width=40, anchor=W, justify=LEFT)
            box_pha_LD.grid(column=2*(phase_id+1), row=2, padx=2, pady=0)
        
        phase_var_arr = np.asarray(phase_var_arr)
        box_pha_text_arr.append(phase_var_arr)

    box_pha_text_arr = np.asarray( box_pha_text_arr)



    box1pha1text = StringVar()
    box1pha1text.set('                                ')
    box1pha1_LD = Label(tab11, textvariable=box1pha1text,
                        width=40, anchor=W, justify=LEFT)
    box1pha1_LD.grid(column=2, row=2, padx=2, pady=0)
    box1pha2text = StringVar()
    box1pha2text.set('                                ')
    box1pha2_LD = Label(tab11, textvariable=box1pha2text,
                        width=40, anchor=W, justify=LEFT)
    box1pha2_LD.grid(column=4, row=2, padx=2, pady=0)
    box1pha3text = StringVar()
    box1pha3text.set('                                ')
    box1pha3_LD = Label(tab11, textvariable=box1pha3text,
                        width=40, anchor=W, justify=LEFT)
    box1pha3_LD.grid(column=6, row=2, padx=2, pady=0)
    box1pha4text = StringVar()
    box1pha4text.set('                                ')
    box1pha4_LD = Label(tab11, textvariable=box1pha4text,
                        width=40, anchor=W, justify=LEFT)
    box1pha4_LD.grid(column=8, row=2, padx=2, pady=0)
    box1pha5text = StringVar()
    box1pha5text.set('                                ')
    box1pha5_LD = Label(tab11, textvariable=box1pha5text,
                        width=40, anchor=W, justify=LEFT)
    box1pha5_LD.grid(column=10, row=2, padx=2, pady=0)
    box1pha6text = StringVar()
    box1pha6text.set('                                ')
    box1pha6_LD = Label(tab11, textvariable=box1pha6text,
                        width=40, anchor=W, justify=LEFT)
    box1pha6_LD.grid(column=12, row=2, padx=2, pady=0)
    box1pha7text = StringVar()
    box1pha7text.set('                                ')
    box1pha7_LD = Label(tab11, textvariable=box1pha7text,
                        width=40, anchor=W, justify=LEFT)
    box1pha7_LD.grid(column=14, row=2, padx=2, pady=0)
    box1pha8text = StringVar()
    box1pha8text.set('                                ')
    box1pha8_LD = Label(tab11, textvariable=box1pha8text,
                        width=40, anchor=W, justify=LEFT)
    box1pha8_LD.grid(column=16, row=2, padx=2, pady=0)
    box1pha9text = StringVar()
    box1pha9text.set('                                ')
    box1pha9_LD = Label(tab11, textvariable=box1pha9text,
                        width=40, anchor=W, justify=LEFT)
    box1pha9_LD.grid(column=18, row=2, padx=2, pady=0)
    box1pha10text = StringVar()
    box1pha10text.set('                                ')
    box1pha10_LD = Label(tab11, textvariable=box1pha10text,
                         width=40, anchor=W, justify=LEFT)
    box1pha10_LD.grid(column=20, row=2, padx=2, pady=0)
    box1pha11text = StringVar()
    box1pha11text.set('                                ')
    box1pha11_LD = Label(tab11, textvariable=box1pha11text,
                         width=40, anchor=W, justify=LEFT)
    box1pha11_LD.grid(column=22, row=2, padx=2, pady=0)
    box1pha12text = StringVar()
    box1pha12text.set('                                ')
    box1pha12_LD = Label(tab11, textvariable=box1pha12text,
                         width=40, anchor=W, justify=LEFT)
    box1pha12_LD.grid(column=24, row=2, padx=2, pady=0)

    window.update_idletasks()


    #BOX2

    box2pha1text = StringVar()
    box2pha1text.set('                                ')
    box2pha1_LD = Label(tab11, textvariable=box2pha1text,
                        width=40, anchor=W, justify=LEFT)
    box2pha1_LD.grid(column=2, row=3, padx=2, pady=0)
    box2pha2text = StringVar()
    box2pha2text.set('                                ')
    box2pha2_LD = Label(tab11, textvariable=box2pha2text,
                        width=40, anchor=W, justify=LEFT)
    box2pha2_LD.grid(column=4, row=3, padx=2, pady=0)
    box2pha3text = StringVar()
    box2pha3text.set('                                ')
    box2pha3_LD = Label(tab11, textvariable=box2pha3text,
                        width=40, anchor=W, justify=LEFT)
    box2pha3_LD.grid(column=6, row=3, padx=2, pady=0)
    box2pha4text = StringVar()
    box2pha4text.set('                                ')
    box2pha4_LD = Label(tab11, textvariable=box2pha4text,
                        width=40, anchor=W, justify=LEFT)
    box2pha4_LD.grid(column=8, row=3, padx=2, pady=0)
    box2pha5text = StringVar()
    box2pha5text.set('                                ')
    box2pha5_LD = Label(tab11, textvariable=box2pha5text,
                        width=40, anchor=W, justify=LEFT)
    box2pha5_LD.grid(column=10, row=3, padx=2, pady=0)
    box2pha6text = StringVar()
    box2pha6text.set('                                ')
    box2pha6_LD = Label(tab11, textvariable=box2pha6text,
                        width=40, anchor=W, justify=LEFT)
    box2pha6_LD.grid(column=12, row=3, padx=2, pady=0)
    box2pha7text = StringVar()
    box2pha7text.set('                                ')
    box2pha7_LD = Label(tab11, textvariable=box2pha7text,
                        width=40, anchor=W, justify=LEFT)
    box2pha7_LD.grid(column=14, row=3, padx=2, pady=0)
    box2pha8text = StringVar()
    box2pha8text.set('                                ')
    box2pha8_LD = Label(tab11, textvariable=box2pha8text,
                        width=40, anchor=W, justify=LEFT)
    box2pha8_LD.grid(column=16, row=3, padx=2, pady=0)
    box2pha9text = StringVar()
    box2pha9text.set('                                ')
    box2pha9_LD = Label(tab11, textvariable=box2pha9text,
                        width=40, anchor=W, justify=LEFT)
    box2pha9_LD.grid(column=18, row=3, padx=2, pady=0)
    box2pha10text = StringVar()
    box2pha10text.set('                                ')
    box2pha10_LD = Label(tab11, textvariable=box2pha10text,
                         width=40, anchor=W, justify=LEFT)
    box2pha10_LD.grid(column=20, row=3, padx=2, pady=0)
    box2pha11text = StringVar()
    box2pha11text.set('                                ')
    box2pha11_LD = Label(tab11, textvariable=box2pha11text,
                         width=40, anchor=W, justify=LEFT)
    box2pha11_LD.grid(column=22, row=3, padx=2, pady=0)
    box2pha12text = StringVar()
    box2pha12text.set('                                ')
    box2pha12_LD = Label(tab11, textvariable=box2pha12text,
                         width=40, anchor=W, justify=LEFT)
    box2pha12_LD.grid(column=24, row=3, padx=2, pady=0)

    window.update_idletasks()

    box3pha1text = StringVar()
    box3pha1text.set('                                ')
    box3pha1_LD = Label(tab11, textvariable=box3pha1text,
                        width=40, anchor=W, justify=LEFT)
    box3pha1_LD.grid(column=2, row=4, padx=2, pady=0)
    box3pha2text = StringVar()
    box3pha2text.set('                                ')
    box3pha2_LD = Label(tab11, textvariable=box3pha2text,
                        width=40, anchor=W, justify=LEFT)
    box3pha2_LD.grid(column=4, row=4, padx=2, pady=0)
    box3pha3text = StringVar()
    box3pha3text.set('                                ')
    box3pha3_LD = Label(tab11, textvariable=box3pha3text,
                        width=40, anchor=W, justify=LEFT)
    box3pha3_LD.grid(column=6, row=4, padx=2, pady=0)
    box3pha4text = StringVar()
    box3pha4text.set('                                ')
    box3pha4_LD = Label(tab11, textvariable=box3pha4text,
                        width=40, anchor=W, justify=LEFT)
    box3pha4_LD.grid(column=8, row=4, padx=2, pady=0)
    box3pha5text = StringVar()
    box3pha5text.set('                                ')
    box3pha5_LD = Label(tab11, textvariable=box3pha5text,
                        width=40, anchor=W, justify=LEFT)
    box3pha5_LD.grid(column=10, row=4, padx=2, pady=0)
    box3pha6text = StringVar()
    box3pha6text.set('                                ')
    box3pha6_LD = Label(tab11, textvariable=box3pha6text,
                        width=40, anchor=W, justify=LEFT)
    box3pha6_LD.grid(column=12, row=4, padx=2, pady=0)
    box3pha7text = StringVar()
    box3pha7text.set('                                ')
    box3pha7_LD = Label(tab11, textvariable=box3pha7text,
                        width=40, anchor=W, justify=LEFT)
    box3pha7_LD.grid(column=14, row=4, padx=2, pady=0)
    box3pha8text = StringVar()
    box3pha8text.set('                                ')
    box3pha8_LD = Label(tab11, textvariable=box3pha8text,
                        width=40, anchor=W, justify=LEFT)
    box3pha8_LD.grid(column=16, row=4, padx=2, pady=0)
    box3pha9text = StringVar()
    box3pha9text.set('                                ')
    box3pha9_LD = Label(tab11, textvariable=box3pha9text,
                        width=40, anchor=W, justify=LEFT)
    box3pha9_LD.grid(column=18, row=4, padx=2, pady=0)
    box3pha10text = StringVar()
    box3pha10text.set('                                ')
    box3pha10_LD = Label(tab11, textvariable=box3pha10text,
                         width=40, anchor=W, justify=LEFT)
    box3pha10_LD.grid(column=20, row=4, padx=2, pady=0)
    box3pha11text = StringVar()
    box3pha11text.set('                                ')
    box3pha11_LD = Label(tab11, textvariable=box3pha11text,
                         width=40, anchor=W, justify=LEFT)
    box3pha11_LD.grid(column=22, row=4, padx=2, pady=0)
    box3pha12text = StringVar()
    box3pha12text.set('                                ')
    box3pha12_LD = Label(tab11, textvariable=box3pha12text,
                         width=40, anchor=W, justify=LEFT)
    box3pha12_LD.grid(column=24, row=4, padx=2, pady=0)

    

    box4pha1text = StringVar()
    box4pha1text.set('                                ')
    box4pha1_LD = Label(tab11, textvariable=box4pha1text,
                        width=40, anchor=W, justify=LEFT)
    box4pha1_LD.grid(column=2, row=5, padx=2, pady=0)
    box4pha2text = StringVar()
    box4pha2text.set('                                ')
    box4pha2_LD = Label(tab11, textvariable=box4pha2text,
                        width=40, anchor=W, justify=LEFT)
    box4pha2_LD.grid(column=4, row=5, padx=2, pady=0)
    box4pha3text = StringVar()
    box4pha3text.set('                                ')
    box4pha3_LD = Label(tab11, textvariable=box4pha3text,
                        width=40, anchor=W, justify=LEFT)
    box4pha3_LD.grid(column=6, row=5, padx=2, pady=0)
    box4pha4text = StringVar()
    box4pha4text.set('                                ')
    box4pha4_LD = Label(tab11, textvariable=box4pha4text,
                        width=40, anchor=W, justify=LEFT)
    box4pha4_LD.grid(column=8, row=5, padx=2, pady=0)
    box4pha5text = StringVar()
    box4pha5text.set('                                ')
    box4pha5_LD = Label(tab11, textvariable=box4pha5text,
                        width=40, anchor=W, justify=LEFT)
    box4pha5_LD.grid(column=10, row=5, padx=2, pady=0)
    box4pha6text = StringVar()
    box4pha6text.set('                                ')
    box4pha6_LD = Label(tab11, textvariable=box4pha6text,
                        width=40, anchor=W, justify=LEFT)
    box4pha6_LD.grid(column=12, row=5, padx=2, pady=0)
    box4pha7text = StringVar()
    box4pha7text.set('                                ')
    box4pha7_LD = Label(tab11, textvariable=box4pha7text,
                        width=40, anchor=W, justify=LEFT)
    box4pha7_LD.grid(column=14, row=5, padx=2, pady=0)
    box4pha8text = StringVar()
    box4pha8text.set('                                ')
    box4pha8_LD = Label(tab11, textvariable=box4pha8text,
                        width=40, anchor=W, justify=LEFT)
    box4pha8_LD.grid(column=16, row=5, padx=2, pady=0)
    box4pha9text = StringVar()
    box4pha9text.set('                                ')
    box4pha9_LD = Label(tab11, textvariable=box4pha9text,
                        width=40, anchor=W, justify=LEFT)
    box4pha9_LD.grid(column=18, row=5, padx=2, pady=0)
    box4pha10text = StringVar()
    box4pha10text.set('                                ')
    box4pha10_LD = Label(tab11, textvariable=box4pha10text,
                         width=40, anchor=W, justify=LEFT)
    box4pha10_LD.grid(column=20, row=5, padx=2, pady=0)
    box4pha11text = StringVar()
    box4pha11text.set('                                ')
    box4pha11_LD = Label(tab11, textvariable=box4pha11text,
                         width=40, anchor=W, justify=LEFT)
    box4pha11_LD.grid(column=22, row=5, padx=2, pady=0)
    box4pha12text = StringVar()
    box4pha12text.set('                                ')
    box4pha12_LD = Label(tab11, textvariable=box4pha12text,
                         width=40, anchor=W, justify=LEFT)
    box4pha12_LD.grid(column=24, row=5, padx=2, pady=0)

    

    box5pha1text = StringVar()
    box5pha1text.set('                                ')
    box5pha1_LD = Label(tab11, textvariable=box5pha1text,
                        width=40, anchor=W, justify=LEFT)
    box5pha1_LD.grid(column=2, row=6, padx=2, pady=0)
    box5pha2text = StringVar()
    box5pha2text.set('                                ')
    box5pha2_LD = Label(tab11, textvariable=box5pha2text,
                        width=40, anchor=W, justify=LEFT)
    box5pha2_LD.grid(column=4, row=6, padx=2, pady=0)
    box5pha3text = StringVar()
    box5pha3text.set('                                ')
    box5pha3_LD = Label(tab11, textvariable=box5pha3text,
                        width=40, anchor=W, justify=LEFT)
    box5pha3_LD.grid(column=6, row=6, padx=2, pady=0)
    box5pha4text = StringVar()
    box5pha4text.set('                                ')
    box5pha4_LD = Label(tab11, textvariable=box5pha4text,
                        width=40, anchor=W, justify=LEFT)
    box5pha4_LD.grid(column=8, row=6, padx=2, pady=0)
    box5pha5text = StringVar()
    box5pha5text.set('                                ')
    box5pha5_LD = Label(tab11, textvariable=box5pha5text,
                        width=40, anchor=W, justify=LEFT)
    box5pha5_LD.grid(column=10, row=6, padx=2, pady=0)
    box5pha6text = StringVar()
    box5pha6text.set('                                ')
    box5pha6_LD = Label(tab11, textvariable=box5pha6text,
                        width=40, anchor=W, justify=LEFT)
    box5pha6_LD.grid(column=12, row=6, padx=2, pady=0)
    box5pha7text = StringVar()
    box5pha7text.set('                                ')
    box5pha7_LD = Label(tab11, textvariable=box5pha7text,
                        width=40, anchor=W, justify=LEFT)
    box5pha7_LD.grid(column=14, row=6, padx=2, pady=0)
    box5pha8text = StringVar()
    box5pha8text.set('                                ')
    box5pha8_LD = Label(tab11, textvariable=box5pha8text,
                        width=40, anchor=W, justify=LEFT)
    box5pha8_LD.grid(column=16, row=6, padx=2, pady=0)
    box5pha9text = StringVar()
    box5pha9text.set('                                ')
    box5pha9_LD = Label(tab11, textvariable=box5pha9text,
                        width=40, anchor=W, justify=LEFT)
    box5pha9_LD.grid(column=18, row=6, padx=2, pady=0)
    box5pha10text = StringVar()
    box5pha10text.set('                                ')
    box5pha10_LD = Label(tab11, textvariable=box5pha10text,
                         width=40, anchor=W, justify=LEFT)
    box5pha10_LD.grid(column=20, row=6, padx=2, pady=0)
    box5pha11text = StringVar()
    box5pha11text.set('                                ')
    box5pha11_LD = Label(tab11, textvariable=box5pha11text,
                         width=40, anchor=W, justify=LEFT)
    box5pha11_LD.grid(column=22, row=6, padx=2, pady=0)
    box5pha12text = StringVar()
    box5pha12text.set('                                ')
    box5pha12_LD = Label(tab11, textvariable=box5pha12text,
                         width=40, anchor=W, justify=LEFT)
    box5pha12_LD.grid(column=24, row=6, padx=2, pady=0)

    window.update_idletasks()

    # 1 Phase
    box_id = 0
    # for box_id in range(0,5):
    for phase_id in range(0, 12):
        # box, phase, box1pha1text
        change_box_phase_text(value_mat, box_id, phase_id,
                              box_pha_text_arr[box_id, phase_id])

   
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
    t1 = threading.Thread(target=lambda: get_data(0))
    t1.daemon = True
    # inactivate Recording Start button
    btnRun['state'] = 'disabled'
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
    #print(threading.active_count())
    #print(threading.enumerate())
    status.pack(side='bottom', fill='x')
    status.set('Stopped recording and disconnected from the boxes.')

    for i in range(10):

        boxrec_text[i].set('Recording stopped.')

    window.update_idletasks()


def OnButtonClick(button_id):
    global setBox_arr

   
    button_id = button_id - 1
    getBoxSchedule(button_id)
    setBox_arr[button_id] = 1

 


def getBoxSchedule(box_id):
    
    global  input_mat, value_mat

    
    # maybe I will have to change it for accounting for the 1st line
    #set all value_mat values acording to the input displayed
    for phase_ind in range(0, 12):
        value_mat[box_id, phase_ind, 0] = input_mat[box_id,
                                                    phase_ind, 0].get()  # box, phase, variable
        value_mat[box_id, phase_ind, 1] = input_mat[box_id, phase_ind, 1].get()
        value_mat[box_id, phase_ind, 2] = input_mat[box_id, phase_ind, 2].get()
        value_mat[box_id, phase_ind, 3] = input_mat[box_id, phase_ind, 3].get()
        
        value_mat[box_id, phase_ind, 4] = getDarkLightValue(
            input_mat[box_id, phase_ind, 4])[0]  # var dark, light
        value_mat[box_id, phase_ind, 5] = getDarkLightValue(
            input_mat[box_id, phase_ind, 4])[1]  # light
        if phase_ind == 0:
            value_mat[box_id, phase_ind, 6] = 0
            value_mat[box_id, phase_ind, 7] = 0
            value_mat[box_id, phase_ind, 8] = 0
            value_mat[box_id, phase_ind, 9] = 0
            value_mat[box_id, phase_ind, 10] = 0

        else:
            value_mat[box_id, phase_ind,
                      6] = input_mat[box_id, phase_ind, 5].get()
            value_mat[box_id, phase_ind,
                      7] = input_mat[box_id, phase_ind, 6].get()
            value_mat[box_id, phase_ind,
                      8] = input_mat[box_id, phase_ind, 7].get()
            value_mat[box_id, phase_ind,
                      9] = input_mat[box_id, phase_ind, 8].get()
            value_mat[box_id, phase_ind,
                      10] = input_mat[box_id, phase_ind, 9].get()

    status.pack(side='bottom', fill='x')
    status.set('Box '+str(box_id+1)+' schedule is set.')
    boxsched_text.set('Box '+str(box_id +1)+' schedule set.')
    if np.sum(setBox_arr)  == 10:
        btnSave['state'] = 'normal'
        btnRun['state'] = 'normal'
        recordingmenu.entryconfig('Start new', state='normal')
        show_conf()
    window.update_idletasks()


def getAllBoxSchedule():
    for box_id in range(0,11):
        getBoxSchedule(box_id)    

    boxsched_text.set('All schedules set.')

    #assign display values to value_mat

    status.pack(side='bottom', fill='x')
    status.set('Schedules for all boxes are set.')
    show_conf()
    btnSave['state'] = 'normal'
    btnRun['state'] = 'normal'
    recordingmenu.entryconfig('Start new', state='normal')
    window.update_idletasks()


def copyScheduletoAll(tab_index):
    global value_mat, input_mat

    #value_mat = np.zeros((5, 12, 11),dtype = object)
    #input_mat = np.zeros((5, 12, 10),dtype = object)
    #print("current frame " +str(tab_index))

    current_frame = tab_index # -1

    
    temp_savedBoxSchedule = copyBoxN(current_frame, input_mat)
    

    for ind in range(1, 12):
        # box_index_to be pasted, global_mat
        temp_savedBoxSchedule.pasteSchedule(ind, input_mat)





def copyBoxN(n, input_mat): #N is the box's ID
    #print("copy box n "+ str(n))
    temp_savedBoxSchedule = BoxSchedule()

    temp_savedBoxSchedule.addPhase1(
        input_mat[n, 0, 0].get(), input_mat[n, 0, 1].get(), input_mat[n, 0, 2].get(), input_mat[n, 0, 3].get(), input_mat[n, 0, 4])
    for phase_ind in range(1, 12):
        
        temp_savedBoxSchedule.addPhase(hourOn=input_mat[n, phase_ind, 0].get(), minOn=input_mat[n, phase_ind, 1].get(), hourOff=input_mat[n, phase_ind, 2].get(), minOff=input_mat[n,phase_ind, 3].get(),
         var=input_mat[n, phase_ind, 4], date=input_mat[n, phase_ind, 5].get(), month=input_mat[n, phase_ind, 6].get(), year=input_mat[n, phase_ind, 7].get(), hourFrom=input_mat[n,phase_ind, 8].get(),  minuteFrom=input_mat[n, phase_ind, 9].get())



# def assignPhasefromtxt(n, loaded_mat):
#     temp_savedBoxSchedule = BoxSchedule()
#     temp_savedBoxSchedule.addPhase1(loaded_mat[n, 0, 0].get(), input_mat[n, 0, 1].get(), input_mat[n, 0, 2].get(), input_mat[n, 0, 3].get(), input_mat[n, 0, 4])
    
#     for phase_ind in range(1, 12):
        
#         temp_savedBoxSchedule.addPhase(hourOn=input_mat[n, phase_ind, 0].get(), minOn=input_mat[n, phase_ind, 1].get(), hourOff=input_mat[n, phase_ind, 2].get(), minOff=input_mat[n,phase_ind, 3].get(),
#          var=input_mat[n, phase_ind, 4], date=input_mat[n, phase_ind, 5].get(), month=input_mat[n, phase_ind, 6].get(), year=input_mat[n, phase_ind, 7].get(), hourFrom=input_mat[n,phase_ind, 8].get(),  minuteFrom=input_mat[n, phase_ind, 9].get())

#     temp_savedBoxSchedule.pasteSchedule(ind, input_mat)

if __name__ == '__main__':
    #### All of the components and their positions in the GUI ####
    # You can change the design from here #
    #
    global value_mat, input_mat
    global BOX_N, PHASE_N
    global setBox_arr

    setBox_arr = np.zeros(10, dtype = int )

    BOX_N = 11
    PHASE_N = 12

    value_mat = np.empty((BOX_N, PHASE_N, 11),dtype=object)
    input_mat = np.empty((BOX_N, PHASE_N, 10),dtype=object) #maybe include the radio buttons
    menu = Menu(window)  # define menu

    # Define Var to keep track of the schedule
    # 1 for LD
    # 2 for DD
    # 3 for LL
    # 1_1 = Box_Phases

 


    log_mat =np.empty((120,12), dtype="<U10")

    # Create file menu
    filemenu = Menu(menu)
    filemenu.add_command(label='Load schedules', command=read_conf)
    filemenu.add_command(label='Save schedules', command=save_conf)
    filemenu.add_separator()
    filemenu.add_command(label='Quit', command=destruct)
    menu.add_cascade(label='File', menu=filemenu)
    # create setting menu
    settingmenu = Menu(menu)
    settingmenu.add_command(label='Set all boxes', command=getAllBoxSchedule)
    settingmenu.add_command(label='Show schedule', command=show_conf)
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


     #Window 900x550
    f1 = tk.Frame(window,  width=900,height=270)
    f2 = tk.Frame(window,  width=900, height=250)
    f3 = tk.Frame(window, width=900, height=70)

    def do_layout():
        f1.pack(side="top", fill="both", expand=True)
        f2.pack(side="top", fill="both", expand=True)
        f3.pack(side="top", fill="both", expand=True)


    do_layout()

    f2scrollbar=Scrollbar(f2,orient="vertical")
    f2scrollbar.pack(side="right",fill="y")
    #f2.config(yscrollcommand=f2scrollbar.set)


    



    tab_control = ttk.Notebook(f1)
    tab_control.bind('<<NotebookTabChanged>>', on_tab_change_trigger)

    ParentFrame1 = ttk.Frame(tab_control)
    ParentFrame2 = ttk.Frame(tab_control)
    ParentFrame3 = ttk.Frame(tab_control)
    ParentFrame4 = ttk.Frame(tab_control)
    ParentFrame5 = ttk.Frame(tab_control)
    ParentFrame6 = ttk.Frame(tab_control)
    ParentFrame7 = ttk.Frame(tab_control)
    ParentFrame8 = ttk.Frame(tab_control)
    ParentFrame9 = ttk.Frame(tab_control)
    ParentFrame10 = ttk.Frame(tab_control)
    ParentFrame11 = ttk.Frame(tab_control)
    tab_control.add(ParentFrame1, text='Box1')
    tab_control.add(ParentFrame2, text='Box2')
    tab_control.add(ParentFrame3, text='Box3')
    tab_control.add(ParentFrame4, text='Box4')
    tab_control.add(ParentFrame5, text='Box5')
    tab_control.add(ParentFrame6, text='Box6')
    tab_control.add(ParentFrame7, text='Box7')
    tab_control.add(ParentFrame8, text='Box8')
    tab_control.add(ParentFrame9, text='Box9')
    tab_control.add(ParentFrame10, text='Box10')
    tab_control.add(ParentFrame11, text='Schedules')

    tab1, canvas1 = create_tab(ParentFrame1)
    tab2, canvas2 = create_tab(ParentFrame2)
    tab3, canvas3 = create_tab(ParentFrame3)
    tab4, canvas4 = create_tab(ParentFrame4)
    tab5, canvas5 = create_tab(ParentFrame5)
    tab6, canvas6 = create_tab(ParentFrame6)
    tab7, canvas7 = create_tab(ParentFrame7)
    tab8, canvas8 = create_tab(ParentFrame8)
    tab9, canvas9 = create_tab(ParentFrame9)
    tab10, canvas10 = create_tab(ParentFrame10)
    tab11, canvas11 = create_tab(ParentFrame10)

    tab_arr = [tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11]
   

    

    # Display all available serial ports
    ports = list(serial.tools.list_ports.comports())
    openPorts = []
    for p in ports:
        #print(p)
        openPorts.append(p.device)
    if len(openPorts) == 0:
        openPorts = [openPorts]
    status.pack(side='bottom', fill='x')
    status.set('Available ports: '+', '.join(map(str, openPorts)))

    yupperbtns = 2
    ymidbtns = 30
    ylowerbtns = 60
    #Entry for Port, Baud, timeout, filename to save
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
    filename_entry.insert(0,'BOX1-5-'+date_string+'.txt')
    configfilename_entry = Entry(f3,width = 30)
    configfilename_entry.place(x=470, y=ymidbtns)
    configfilename_entry.insert(0,'BOX1-5-sched-'+date_string+'.txt')




#SHOW STATUS
    tab1_title2 = Label(f2, text= 'Recording status', anchor='center')    
    boxsched_text=StringVar()
    boxsched_text.set('Schedule not set.')
    boxsched_stat=Label(f2, textvariable=boxsched_text, anchor=W, justify=LEFT)    
    
    boxrec_text=StringVar()
    boxrec_text.set('Recording not started yet.')

    log_text = StringVar()
    log_text.set('# '+str(log_mat[0,0])+'    Time: '+str(log_mat[0,1])+'    LED: '+str(log_mat[0,2])+'    '+'PIR: '+str(log_mat[0,3]))
    #print(log_mat[0,:])
    log_display=Label(f2, textvariable=log_text, anchor='center', justify=LEFT)

    boxrec_stat=Label(f2, textvariable=boxrec_text, anchor='center', justify=LEFT)
    
    tab1_title2.pack()#place(x=40, y=yupperbtns )
    boxsched_stat.pack()#.place(x=40, y=yupperbtns+20)        
    log_display.pack()
    boxrec_stat.pack()#.place(x=40, y=yupperbtns+40)
    #log_stream.getvalue()

    window.update_idletasks() 
    btnSave = Button(f3, text=' Save ', command=save_conf, state='disabled')
    btnRun = Button(f3, text= ' Recording Start ', command=connect, state='disabled')
    btnSetCurrent = Button(f3,text=' Set current box ', command=lambda: OnButtonClick(int(tab_control.index('current'))+1))
    btnSetAll = Button(f3, text='Set All', command=getAllBoxSchedule)
    
    btnReplicateToAll = Button(f3, text=' Replicate to All ', command= lambda: copyScheduletoAll(int(tab_control.index('current'))+1))
   

    # if box settings of all 5 boxes are done, activate save and run buttons
    if np.sum(setBox_arr) == 10:
        btnSave['state'] = 'normal'
        btnRun['state'] = 'normal'

        recordingmenu.entryconfig('Start new', state='normal')
        show_conf()
        window.update_idletasks()

    if "Schedules" in tab_control.select():
        btnSetCurrent['state'] = 'disabled'
        window.update_idletasks()
    else:
        btnSetCurrent['state'] = 'normal'
        window.update_idletasks()

    # button positions change depending on OS

    #yupperbtns = 370
    #ylowerbtns = 410

    if sys.platform.startswith('win'):
        btnSave.place(x=570, y=450)
        btnRun.place(x=610, y=450)
        btnSetAll.place(x=570, y=480)
        btnSetCurrent.place(x=610, y=480)
        btnReplicateToAll.place(x=577, y=340)
    elif sys.platform.startswith('darwin'):
        btnSave.place(x=685, y=450)
        btnRun.place(x=745, y=450)
        btnSetAll.place(x=685, y=480)
        btnSetCurrent.place(x=745, y=480)
        btnReplicateToAll.place(x=577, y=340)
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        btnSave.place(x=730, y= ylowerbtns)
        btnRun.place(x=730, y=ymidbtns)
        btnSetCurrent.place(x=430, y=yupperbtns)       
        btnSetAll.place(x=730, y=yupperbtns)
        btnReplicateToAll.place(x=577, y=yupperbtns)
        
    else:
        btnSave.place(x=635, y=450)
        btnRun.place(x=695, y=450)
        btnSetAll.place(x=635, y=480)
        btnSetCurrent.place(x=695, y=480)
        btnReplicateToAll.place(x=542, y=300)   

    row_adj = 3  # useful when a new row is added above

    boxstatusSeparator = ttk.Separator(f2, orient='horizontal').place(x=0, y=0, relwidth=1)
    runSeparator = ttk.Separator(f3, orient='horizontal').place(x=0, y=0, relwidth=1)#ttk.Separator(window, orient='horizontal') #.place(x = 363, y = ylowerbtns + 30)
    
    # Box1

    radiobuttons = np.zeros((BOX_N, PHASE_N, 3),dtype= object)

 


#populate the input mat with spinboxes and radio buttons
    for box_id in range(0,11):
        tab_title = Label(tab_arr[box_id], text='LED schedule', anchor='center')
        tab_title.grid(column=0, row=-1+row_adj, columnspan='27', sticky='we')
        for phase_id in range(0,12):

            lbl_A_1 = Label(tab_arr[box_id], text='On:')
            label_h1_1 = Label(tab_arr[box_id], text=':')
            label_m1_1 = Label(tab_arr[box_id], text='')
            lbl_B_1 = Label(tab_arr[box_id], text='Off:')
            label_h2_1 = Label(tab_arr[box_id], text=':')
            label_m2_1 = Label(tab_arr[box_id], text='')

            input_mat[box_id, phase_id, 0] = Spinbox(tab_arr[box_id], from_=00, to=24, width=3, format='%02.0f') #change for the parent tab
            input_mat[box_id, phase_id, 1] = Spinbox(tab_arr[box_id], from_=00, to=59, width=3, format='%02.0f')
            input_mat[box_id, phase_id, 2] =  Spinbox(tab_arr[box_id], from_=00, to=24, width=3, format='%02.0f')
            input_mat[box_id, phase_id, 3] = Spinbox(tab_arr[box_id], from_=00, to=59, width=3, format='%02.0f')
            input_mat[box_id, phase_id, 0].delete(0, 'end')
            input_mat[box_id, phase_id, 0].insert(0, '07')
            input_mat[box_id, phase_id, 1].delete(0, 'end')
            input_mat[box_id, phase_id, 1].insert(0, '00')       
            input_mat[box_id, phase_id, 2].delete(0, 'end')
            input_mat[box_id, phase_id, 2].insert(0, '19')
            input_mat[box_id, phase_id, 3].delete(0, 'end')
            input_mat[box_id, phase_id, 3].insert(0, '00')
            input_mat[box_id, phase_id, 4] = IntVar(value=1)

           
            radiobuttons[box_id, phase_id, 0] = Radiobutton(tab_arr[box_id], text='LD', variable=input_mat[box_id, phase_id, 4], value=1)
            radiobuttons[box_id, phase_id, 1] = Radiobutton(tab_arr[box_id], text='DD', variable=input_mat[box_id, phase_id, 4], value=2)
            radiobuttons[box_id, phase_id, 2] = Radiobutton(tab_arr[box_id], text='LL', variable=input_mat[box_id, phase_id, 4], value=3)


            radiobuttons[box_id, phase_id, 0].grid(column=13, row=phase_id+1+row_adj, pady=5)
            lbl_A_1.grid(column=14, row=phase_id+1 +row_adj, pady=5)
            input_mat[box_id, phase_id, 0].grid(column=15, row=phase_id+1+row_adj, pady=5)
            label_h1_1.grid(column=16, row=phase_id+1+row_adj, pady=5, sticky='w')
            input_mat[box_id, phase_id, 1].grid(column=17, row=phase_id+1+row_adj, pady=5)
            label_m1_1.grid(column=18, row=phase_id+1+row_adj, pady=5, sticky='w')
            lbl_B_1.grid(column=19, row=phase_id+1+row_adj, pady=5)
            input_mat[box_id, phase_id, 2].grid(column=20, row=phase_id+1+row_adj, pady=5)
            label_h2_1.grid(column=21, row=phase_id+1+row_adj, pady=5, sticky='w')
            input_mat[box_id, phase_id, 3].grid(column=22, row=phase_id+1+row_adj, pady=5)
            label_m2_1.grid(column=23, row=phase_id+1+row_adj, pady=5, sticky='w')
            radiobuttons[box_id, phase_id, 1].grid(column=24, row=phase_id+1+row_adj, padx=15, pady=5)
            radiobuttons[box_id, phase_id, 2].grid(column=25, row=phase_id+1+row_adj, pady=5)

            phaseLabel = Label(tab_arr[box_id], text='Phase '+str(phase_id +1))
            fromLabel = Label(tab_arr[box_id], text='From:')
            phaseLabel.grid(column=0, row=phase_id+1+row_adj, padx=15, pady=5)
            fromLabel.grid(column=1, row=phase_id+1+row_adj)
            dateLabel = time.strftime('%H:%M   %Y/%m/%d')
           
            date_label1 = Label(tab_arr[box_id], text=dateLabel+' (HH:MN YYYY/MO/DD)')
            date_label1.grid(column=2, row=phase_id+1+row_adj, columnspan='10', sticky='w')
            
            

            if phase_id>0:
                input_mat[box_id, phase_id, 8] = Spinbox(tab_arr[box_id], from_=00, to=24, width=3, format='%02.0f')
                input_mat[box_id, phase_id, 9] = Spinbox(tab_arr[box_id], from_=00, to=59, width=3, format='%02.0f')  
    
                input_mat[box_id, phase_id, 8].delete(0, 'end')
                input_mat[box_id, phase_id, 8].insert(0, '07')
                input_mat[box_id, phase_id, 9].delete(0, 'end')
                input_mat[box_id, phase_id, 9].insert(0, '00')

                input_mat[box_id, phase_id, 5] = Spinbox(tab_arr[box_id], from_=00, to=31, width=3, format='%02.0f')
                input_mat[box_id, phase_id, 6] = Spinbox(tab_arr[box_id], from_=00, to=12, width=3, format='%02.0f')
                input_mat[box_id, phase_id, 7] = Spinbox(tab_arr[box_id], from_=2018, to=2030, width=5)
                input_mat[box_id, phase_id, 5].delete(0, 'end')
                today = datetime.date.today()  # today# calculate dates for 7 days after recording initiation
                day_phase2 = today + datetime.timedelta(days=7)
                input_mat[box_id, phase_id, 5].insert(0, '{:02d}'.format(day_phase2.day))
                input_mat[box_id, phase_id, 6].delete(0, 'end')
                input_mat[box_id, phase_id, 6].insert(0, '{:02d}'.format(day_phase2.month))
                input_mat[box_id, phase_id, 7].delete(0, 'end')
                input_mat[box_id, phase_id, 7].insert(0, day_phase2.year)  # ISO format is YYYY/MM/DD

                

                label_h0_2 = Label(tab_arr[box_id], text=':')
                label_m0_2 = Label(tab_arr[box_id], text='')
                space = Label(tab_arr[box_id], text=' ')
                space_2 = Label(tab_arr[box_id], text=' ')
                label1_d = Label(tab_arr[box_id], text='/')
                label1_m = Label(tab_arr[box_id], text='/')

                

                input_mat[box_id, phase_id, 8].grid(column=2, row=phase_id+1+row_adj)
                label_h0_2.grid(column=3, row=phase_id+1+row_adj)
                input_mat[box_id, phase_id, 9].grid(column=4, row=phase_id+1+row_adj)
                label_m0_2.grid(column=5, row=phase_id+1+row_adj)
                space.grid(column=6, row=2+row_adj)
                input_mat[box_id, phase_id, 7].grid(column=7, row=phase_id+1+row_adj)
                label1_m.grid(column=8, row=phase_id+1+row_adj)
                input_mat[box_id, phase_id, 6].grid(column=9, row=phase_id+1+row_adj)
                label1_d.grid(column=10, row=phase_id+1+row_adj)
                input_mat[box_id, phase_id, 5].grid(column=11, row=phase_id+1+row_adj)  # ISO format
                space_2.grid(column=12, row=phase_id+1+row_adj, padx=5)



    #value_mat = np.zeros((, 12, 11),)

    
    window.update_idletasks()
    

    tab_control.pack(expand=1, fill='both')

    

   

    # Main loop
    window.mainloop()
