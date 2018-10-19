import serial   # For Serial communication
import time     # Required for using delay functions
import datetime # For date-time setting and timedelta calculations
import sys
import platform
import glob
import tkinter as tk
from tkinter import * #import INIT set of tkinter library for GUI
from tkinter import ttk
from tkinter import messagebox
import json
try:
    from tkinter import filedialog
except ImportError:
    fileDialog = tk.filedialog
import threading #to run Arduino loop and tkinter loop alongside
import serial.tools.list_ports #for identifying Arduino port
import numpy as np

# Global variables
global hourOn1_1, minOn1_1, hourOff1_1, minOff1_1, hourOn2_1, minOn2_1, hourOff2_1, minOff2_1 
global hourOn3_1, minOn3_1, hourOff3_1, minOff3_1, hourOn4_1, minOn4_1, hourOff4_1, minOff4_1 
global hourOn5_1, minOn5_1, hourOff5_1, minOff5_1, hourOn6_1, minOn6_1,  hourOff6_1, minOff6_1  
global hourOn7_1, minOn7_1, hourOff7_1, minOff7_1, hourOn8_1, minOn8_1, hourOff8_1, minOff8_1 
global hourOn9_1, minOn9_1, hourOff9_1, minOff9_1, hourOn10_1, minOn10_1, hourOff10_1, minOff10_1
global dark1_1, light1_1, dark2_1, light2_1, dark3_1, light3_1, dark4_1, light4_1, dark5_1, light5_1  
global dark6_1, light6_1, dark7_1, light7_1, dark8_1, light8_1, dark9_1, light9_1, dark10_1, light10_1  
global hourOn3_2, minOn3_2, hourOff3_2, minOff3_2, hourOn1_2, minOn1_2, hourOff1_2, minOff1_2
global hourOn2_2, minOn2_2, hourOff2_2, minOff2_2, hourOn4_2, minOn4_2, hourOff4_2, minOff4_2 
global hourOn5_2, minOn5_2, hourOff5_2, minOff5_2, hourOn6_2, minOn6_2, hourOff6_2, minOff6_2 
global hourOn7_2, minOn7_2, hourOff7_2, minOff7_2, hourOn8_2, minOn8_2, hourOff8_2, minOff8_2 
global hourOn9_2, minOn9_2, hourOff9_2, minOff9_2, hourOn10_2, minOn10_2, hourOff10_2, minOff10_2  
global dark1_2, light1_2, dark2_2, light2_2, dark3_2, light3_2, dark4_2, light4_2, dark5_2, light5_2 
global dark6_2, light6_2, dark7_2, light7_2, dark8_2, light8_2, dark9_2, light9_2, dark10_2, light10_2 
global date1_2, month1_2, year1_2, date2_2, month2_2, year2_2, date3_2, month3_2, year3_2, date4_2, month4_2, year4_2 
global date5_2, month5_2, year5_2, date6_2, month6_2, year6_2, date7_2, month7_2, year7_2  
global date8_2, month8_2, year8_2, date9_2, month9_2, year9_2, date10_2, month10_2, year10_2 
global hourFrom1_2, minuteFrom1_2, hourFrom2_2, minuteFrom2_2, hourFrom3_2, minuteFrom3_2, hourFrom4_2, minuteFrom4_2
global hourFrom5_2, minuteFrom5_2, hourFrom6_2, minuteFrom6_2, hourFrom7_2, minuteFrom7_2, hourFrom8_2, minuteFrom8_2
global hourFrom9_2, minuteFrom9_2, hourFrom10_2, minuteFrom10_2
global hourOn1_3, minOn1_3, hourOff1_3, minOff1_3, hourOn2_3, minOn2_3, hourOff2_3, minOff2_3
global hourOn3_3, minOn3_3, hourOff3_3, minOff3_3, hourOn4_3, minOn4_3, hourOff4_3, minOff4_3 
global hourOn5_3, minOn5_3, hourOff5_3, minOff5_3, hourOn6_3, minOn6_3, hourOff6_3, minOff6_3  
global hourOn7_3, minOn7_3, hourOff7_3, minOff7_3, hourOn8_3, minOn8_3, hourOff8_3, minOff8_3 
global hourOn9_3, minOn9_3, hourOff9_3, minOff9_3, hourOn10_3, minOn10_3, hourOff10_3, minOff10_3
global dark1_3, light1_3, dark2_3, light2_3, dark3_3, light3_3, dark4_3, light4_3, dark5_3, light5_3
global dark6_3, light6_3, dark7_3, light7_3, dark8_3, light8_3, dark9_3, light9_3, dark10_3, light10_3 
global date1_3, month1_3, year1_3, date2_3, month2_3, year2_3, date3_3, month3_3, year3_3, date4_3, month4_3, year4_3 
global date5_3, month5_3, year5_3, date6_3, month6_3, year6_3, date7_3, month7_3, year7_3, date8_3, month8_3, year8_3 
global date9_3, month9_3, year9_3, date10_3, month10_3, year10_3 
global hourFrom1_3, minuteFrom1_3, hourFrom2_3, minuteFrom2_3, hourFrom3_3, minuteFrom3_3, hourFrom4_3, minuteFrom4_3 
global hourFrom5_3, minuteFrom5_3, hourFrom6_3, minuteFrom6_3, hourFrom7_3, minuteFrom7_3, hourFrom8_3, minuteFrom8_3 
global hourFrom9_3, minuteFrom9_3, hourFrom10_3, minuteFrom10_3 
global setBox1, setBox2, setBox3, setBox4, setBox5, setBox6, setBox7, setBox8, setBox9, setBox10

# Preset values
setBox1=0
setBox2=0
setBox3=0
setBox4=0
setBox5=0
setBox6=0
setBox7=0
setBox8=0
setBox9=0
setBox10=0

# Version information
def about():
    return messagebox.showinfo('About',
                                '10-Box Schedule Setter\n'+
                                'LocoBox.py\n\n'+
                                'Version 0.2.10\n'+
                                'Oct 15, 2018\n\n'+
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
window.title('LocoBox (10-box)')
if sys.platform.startswith('win'):
    window.geometry('730x420')
elif sys.platform.startswith('darwin'):
    window.geometry('1000x440')
elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
    window.geometry('730x420')
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
    box1rec_text.set('Preparing for recording.')
    box2rec_text.set('Preparing for recording.')
    box3rec_text.set('Preparing for recording.')
    box4rec_text.set('Preparing for recording.')
    box5rec_text.set('Preparing for recording.')
    box6rec_text.set('Preparing for recording.')
    box7rec_text.set('Preparing for recording.')
    box8rec_text.set('Preparing for recording.')
    box9rec_text.set('Preparing for recording.')
    box10rec_text.set('Preparing for recording.')
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
    try:
        while True:
            string2 = serial_obj.readline().decode('utf-8')
            if string2 != '':
                with open(filename,'a') as w:
                    w.write(string2)
                w.close()
            print(string2)
            if i==0:
                print('Synching time...')
                status.pack(side='bottom', fill='x')
                status.set('Synching time...')
                t= datetime.datetime.now()
                serial_obj.write(str.encode(t.strftime('%Y-%m-%d %H:%M:%S')))
            if i==1:
                serial_obj.write(str.encode(hourOn1_1+minOn1_1+hourOff1_1+minOff1_1+hourOn2_1+minOn2_1+hourOff2_1+minOff2_1+
                                            hourOn3_1+minOn3_1+hourOff3_1+minOff3_1+hourOn4_1+minOn4_1+hourOff4_1+minOff4_1+
                                            hourOn5_1+minOn5_1+hourOff5_1+minOff5_1))
            if i==2:    
                serial_obj.write(str.encode(hourOn6_1+minOn6_1+hourOff6_1+minOff6_1+hourOn7_1+minOn7_1+hourOff7_1+minOff7_1+
                                            hourOn8_1+minOn8_1+hourOff8_1+minOff8_1+hourOn9_1+minOn9_1+hourOff9_1+minOff9_1+
                                            hourOn10_1+minOn10_1+hourOff10_1+minOff10_1+
                                            dark1_1+light1_1+dark2_1+light2_1+dark3_1+light3_1+dark4_1+light4_1+
                                            dark5_1+light5_1+dark6_1+light6_1+dark7_1+light7_1+dark8_1+light8_1+
                                            dark9_1+light9_1+dark10_1+light10_1))
                status.pack(side='bottom', fill='x')
                status.set('Phase 1 schedules sent.')                              
            if i==3:
                serial_obj.write(str.encode(hourOn1_2+minOn1_2+hourOff1_2+minOff1_2+hourOn2_2+minOn2_2+hourOff2_2+minOff2_2+
                                            hourOn3_2+minOn3_2+hourOff3_2+minOff3_2+hourOn4_2+minOn4_2+hourOff4_2+minOff4_2+
                                            hourOn5_2+minOn5_2+hourOff5_2+minOff5_2))
            if i==4:
                serial_obj.write(str.encode(hourOn6_2+minOn6_2+hourOff6_2+minOff6_2+hourOn7_2+minOn7_2+hourOff7_2+minOff7_2+
                                            hourOn8_2+minOn8_2+hourOff8_2+minOff8_2+hourOn9_2+minOn9_2+hourOff9_2+minOff9_2+
                                            hourOn10_2+minOn10_2+hourOff10_2+minOff10_2+
                                            dark1_2+light1_2+dark2_2+light2_2+dark3_2+light3_2+dark4_2+light4_2+
                                            dark5_2+light5_2+dark6_2+light6_2+dark7_2+light7_2+dark8_2+light8_2+
                                            dark9_2+light9_2+dark10_2+light10_2))
            if i==5:
                serial_obj.write(str.encode(date1_2+month1_2+year1_2+date2_2+month2_2+year2_2+
                                            date3_2+month3_2+year3_2+date4_2+month4_2+year4_2+
                                            date5_2+month5_2+year5_2+hourFrom1_2+minuteFrom1_2+
                                            hourFrom2_2+minuteFrom2_2+hourFrom3_2+minuteFrom3_2+
                                            hourFrom4_2+minuteFrom4_2+hourFrom5_2+minuteFrom5_2))  
            if i==6:
                serial_obj.write(str.encode(date6_2+month6_2+year6_2+date7_2+month7_2+year7_2+
                                            date8_2+month8_2+year8_2+date9_2+month9_2+year9_2+
                                            date10_2+month10_2+year10_2+hourFrom6_2+minuteFrom6_2+
                                            hourFrom7_2+minuteFrom7_2+hourFrom8_2+minuteFrom8_2+
                                            hourFrom9_2+minuteFrom9_2+hourFrom10_2+minuteFrom10_2))
                status.pack(side='bottom', fill='x')
                status.set('Phase 2 schedules sent.')   
            if i==7:
                serial_obj.write(str.encode(hourOn1_3+minOn1_3+hourOff1_3+minOff1_3+hourOn2_3+minOn2_3+hourOff2_3+minOff2_3+
                                            hourOn3_3+minOn3_3+hourOff3_3+minOff3_3+hourOn4_3+minOn4_3+hourOff4_3+minOff4_3+
                                            hourOn5_3+minOn5_3+hourOff5_3+minOff5_3))
            if i==8:
                serial_obj.write(str.encode(hourOn6_3+minOn6_3+hourOff6_3+minOff6_3+hourOn7_3+minOn7_3+hourOff7_3+minOff7_3+
                                            hourOn8_3+minOn8_3+hourOff8_3+minOff8_3+hourOn9_3+minOn9_3+hourOff9_3+minOff9_3+
                                            hourOn10_3+minOn10_3+hourOff10_3+minOff10_3+
                                            dark1_3+light1_3+dark2_3+light2_3+dark3_3+light3_3+
                                            dark4_3+light4_3+dark5_3+light5_3+dark6_3+light6_3+
                                            dark7_3+light7_3+dark8_3+light8_3+dark9_3+light9_3+dark10_3+light10_3))
            if i==9:
                serial_obj.write(str.encode(date1_3+month1_3+year1_3+date2_3+month2_3+year2_3+
                                            date3_3+month3_3+year3_3+date4_3+month4_3+year4_3+
                                            date5_3+month5_3+year5_3+hourFrom1_3+minuteFrom1_3+
                                            hourFrom2_3+minuteFrom2_3+hourFrom3_3+minuteFrom3_3+
                                            hourFrom4_3+minuteFrom4_3+hourFrom5_3+minuteFrom5_3)) 
            if i==10:
                serial_obj.write(str.encode(date6_3+month6_3+year6_3+date7_3+month7_3+year7_3+
                                            date8_3+month8_3+year8_3+date9_3+month9_3+year9_3+
                                            date10_3+month10_3+year10_3+hourFrom6_3+minuteFrom6_3+
                                            hourFrom7_3+minuteFrom7_3+hourFrom8_3+minuteFrom8_3+
                                            hourFrom9_3+minuteFrom9_3+hourFrom10_3+minuteFrom10_3))
                status.pack(side='bottom', fill='x')
                status.set('All schedules transferred. Recording began.') 
                box1rec_text.set('Recording on-going.')
                box2rec_text.set('Recording on-going.')
                box3rec_text.set('Recording on-going.')
                box4rec_text.set('Recording on-going.')
                box5rec_text.set('Recording on-going.')
                box6rec_text.set('Recording on-going.')
                box7rec_text.set('Recording on-going.')
                box8rec_text.set('Recording on-going.')
                box9rec_text.set('Recording on-going.')
                box10rec_text.set('Recording on-going.')
                window.update_idletasks()
            i=i+1
            
            if len(string2)>=139:               
                box1rec_text.set('# '+str(counti)+'    Time: '+string2[0:8]+'    LED1: '+string2[20:25]+'    '+'PIR1: '+string2[26:31])
                box2rec_text.set('# '+str(counti)+'    Time: '+string2[0:8]+'    LED2: '+string2[32:37]+'    '+'PIR2: '+string2[38:43])
                box3rec_text.set('# '+str(counti)+'    Time: '+string2[0:8]+'    LED3: '+string2[44:49]+'    '+'PIR3: '+string2[50:55])
                box4rec_text.set('# '+str(counti)+'    Time: '+string2[0:8]+'    LED4: '+string2[56:61]+'    '+'PIR4: '+string2[62:67])
                box5rec_text.set('# '+str(counti)+'    Time: '+string2[0:8]+'    LED5: '+string2[68:73]+'    '+'PIR5: '+string2[74:79])
                box6rec_text.set('# '+str(counti)+'    Time: '+string2[0:8]+'    LED6: '+string2[80:85]+'    '+'PIR6: '+string2[86:91])
                box7rec_text.set('# '+str(counti)+'    Time: '+string2[0:8]+'    LED7: '+string2[92:97]+'    '+'PIR7: '+string2[98:103])
                box8rec_text.set('# '+str(counti)+'    Time: '+string2[0:8]+'    LED8: '+string2[104:109]+'    '+'PIR8: '+string2[110:115])
                box9rec_text.set('# '+str(counti)+'    Time: '+string2[0:8]+'    LED9: '+string2[116:121]+'    '+'PIR9: '+string2[122:127])
                box10rec_text.set('# '+str(counti)+'    Time: '+string2[0:8]+'    LED10: '+string2[128:133]+'    '+'PIR10: '+string2[134:139]) 
                counti = counti+1
    except:
        print('Stopped recording and disconnected from the boxes.')
        status.pack(side='bottom', fill='x')
        status.set('Stopped recording and disconnected from the boxes.') 
        box1rec_text.set('Recording stopped.')
        box2rec_text.set('Recording stopped.')
        box3rec_text.set('Recording stopped.')
        box4rec_text.set('Recording stopped.')
        box5rec_text.set('Recording stopped.')
        box6rec_text.set('Recording stopped.')
        box7rec_text.set('Recording stopped.')
        box8rec_text.set('Recording stopped.')
        box9rec_text.set('Recording stopped.')
        box10rec_text.set('Recording stopped.')
        window.update_idletasks()

def writeToJSONFile(filename, data):
    filePathNameWExt = filename
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

def save_conf(): # Save schedule configuration
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
    config['hourOn7_1'] = hourOn7_1
    config['minOn7_1'] = minOn7_1
    config['hourOff7_1'] = hourOff7_1
    config['minOff7_1'] = minOff7_1
    config['hourOn8_1'] = hourOn8_1
    config['minOn8_1'] = minOn8_1
    config['hourOff8_1'] = hourOff8_1
    config['minOff8_1'] = minOff8_1
    config['hourOn9_1'] = hourOn9_1
    config['minOn9_1'] = minOn9_1
    config['hourOff9_1'] = hourOff9_1
    config['minOff9_1'] = minOff9_1
    config['hourOn10_1'] = hourOn10_1
    config['minOn10_1'] = minOn10_1
    config['hourOff10_1'] = hourOff10_1
    config['minOff10_1'] = minOff10_1
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
    config['dark7_1'] = dark7_1
    config['light7_1'] = light7_1
    config['dark8_1'] = dark8_1
    config['light8_1'] = light8_1
    config['dark9_1'] = dark9_1
    config['light9_1'] = light9_1
    config['dark10_1'] = dark10_1
    config['light10_1'] = light10_1
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
    config['hourOn7_2'] = hourOn7_2
    config['minOn7_2'] = minOn7_2
    config['hourOff7_2'] = hourOff7_2
    config['minOff7_2'] = minOff7_2
    config['hourOn8_2'] = hourOn8_2
    config['minOn8_2'] = minOn8_2
    config['hourOff8_2'] = hourOff8_2
    config['minOff8_2'] = minOff8_2
    config['hourOn9_2'] = hourOn9_2
    config['minOn9_2'] = minOn9_2
    config['hourOff9_2'] = hourOff9_2
    config['minOff9_2'] = minOff9_2
    config['hourOn10_2'] = hourOn10_2
    config['minOn10_2'] = minOn10_2
    config['hourOff10_2'] = hourOff10_2
    config['minOff10_2'] = minOff10_2
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
    config['dark7_2'] = dark7_2
    config['light7_2'] = light7_2
    config['dark8_2'] = dark8_2
    config['light8_2'] = light8_2
    config['dark9_2'] = dark9_2
    config['light9_2'] = light9_2
    config['dark10_2'] = dark10_2
    config['light10_2'] = light10_2
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
    config['date6_2'] = date6_2
    config['month6_2'] = month6_2
    config['year6_2'] = year6_2
    config['date7_2'] = date7_2
    config['month7_2'] = month7_2
    config['year7_2'] = year7_2
    config['date8_2'] = date8_2
    config['month8_2'] = month8_2
    config['year8_2'] = year8_2
    config['date9_2'] = date9_2
    config['month9_2'] = month9_2
    config['year9_2'] = year9_2
    config['date10_2'] = date10_2
    config['month10_2'] = month10_2
    config['year10_2'] = year10_2
    config['hourFrom6_2'] = hourFrom6_2
    config['minuteFrom6_2'] = minuteFrom6_2
    config['hourFrom7_2'] = hourFrom7_2
    config['minuteFrom7_2'] = minuteFrom7_2
    config['hourFrom8_2'] = hourFrom8_2
    config['minuteFrom8_2'] = minuteFrom8_2
    config['hourFrom9_2'] = hourFrom9_2
    config['minuteFrom9_2'] = minuteFrom9_2
    config['hourFrom10_2'] = hourFrom10_2
    config['minuteFrom10_2'] = minuteFrom10_2
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
    config['hourOn7_3'] = hourOn7_3
    config['minOn7_3'] = minOn7_3
    config['hourOff7_3'] = hourOff7_3
    config['minOff7_3'] = minOff7_3
    config['hourOn8_3'] = hourOn8_3
    config['minOn8_3'] = minOn8_3
    config['hourOff8_3'] = hourOff8_3
    config['minOff8_3'] = minOff8_3
    config['hourOn9_3'] = hourOn9_3
    config['minOn9_3'] = minOn9_3
    config['hourOff9_3'] = hourOff9_3
    config['minOff9_3'] = minOff9_3
    config['hourOn10_3'] = hourOn10_3
    config['minOn10_3'] = minOn10_3
    config['hourOff10_3'] = hourOff10_3
    config['minOff10_3'] = minOff10_3
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
    config['dark7_3'] = dark7_3
    config['light7_3'] = light7_3
    config['dark8_3'] = dark8_3
    config['light8_3'] = light8_3
    config['dark9_3'] = dark9_3
    config['light9_3'] = light9_3
    config['dark10_3'] = dark10_3
    config['light10_3'] = light10_3
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
    config['date6_3'] = date6_3
    config['month6_3'] = month6_3
    config['year6_3'] = year6_3
    config['date7_3'] = date7_3
    config['month7_3'] = month7_3
    config['year7_3'] = year7_3
    config['date8_3'] = date8_3
    config['month8_3'] = month8_3
    config['year8_3'] = year8_3
    config['date9_3'] = date9_3
    config['month9_3'] = month9_3
    config['year9_3'] = year9_3
    config['date10_3'] = date10_3
    config['month10_3'] = month10_3
    config['year10_3'] = year10_3
    config['hourFrom6_3'] = hourFrom6_3
    config['minuteFrom6_3'] = minuteFrom6_3
    config['hourFrom7_3'] = hourFrom7_3
    config['minuteFrom7_3'] = minuteFrom7_3
    config['hourFrom8_3'] = hourFrom8_3
    config['minuteFrom8_3'] = minuteFrom8_3
    config['hourFrom9_3'] = hourFrom9_3
    config['minuteFrom9_3'] = minuteFrom9_3
    config['hourFrom10_3'] = hourFrom10_3
    config['minuteFrom10_3'] = minuteFrom10_3
    configfilename = configfilename_entry.get()
    writeToJSONFile(configfilename, config)
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
    global hourOn5_1, minOn5_1, hourOff5_1, minOff5_1, hourOn6_1, minOn6_1,  hourOff6_1, minOff6_1  
    global hourOn7_1, minOn7_1, hourOff7_1, minOff7_1, hourOn8_1, minOn8_1, hourOff8_1, minOff8_1 
    global hourOn9_1, minOn9_1, hourOff9_1, minOff9_1, hourOn10_1, minOn10_1, hourOff10_1, minOff10_1
    global dark1_1, light1_1, dark2_1, light2_1, dark3_1, light3_1, dark4_1, light4_1, dark5_1, light5_1  
    global dark6_1, light6_1, dark7_1, light7_1, dark8_1, light8_1, dark9_1, light9_1, dark10_1, light10_1  
    global hourOn3_2, minOn3_2, hourOff3_2, minOff3_2, hourOn1_2, minOn1_2, hourOff1_2, minOff1_2
    global hourOn2_2, minOn2_2, hourOff2_2, minOff2_2, hourOn4_2, minOn4_2, hourOff4_2, minOff4_2 
    global hourOn5_2, minOn5_2, hourOff5_2, minOff5_2, hourOn6_2, minOn6_2, hourOff6_2, minOff6_2 
    global hourOn7_2, minOn7_2, hourOff7_2, minOff7_2, hourOn8_2, minOn8_2, hourOff8_2, minOff8_2 
    global hourOn9_2, minOn9_2, hourOff9_2, minOff9_2, hourOn10_2, minOn10_2, hourOff10_2, minOff10_2  
    global dark1_2, light1_2, dark2_2, light2_2, dark3_2, light3_2, dark4_2, light4_2, dark5_2, light5_2 
    global dark6_2, light6_2, dark7_2, light7_2, dark8_2, light8_2, dark9_2, light9_2, dark10_2, light10_2 
    global date1_2, month1_2, year1_2, date2_2, month2_2, year2_2, date3_2, month3_2, year3_2, date4_2, month4_2, year4_2 
    global date5_2, month5_2, year5_2, date6_2, month6_2, year6_2, date7_2, month7_2, year7_2  
    global date8_2, month8_2, year8_2, date9_2, month9_2, year9_2, date10_2, month10_2, year10_2 
    global hourFrom1_2, minuteFrom1_2, hourFrom2_2, minuteFrom2_2, hourFrom3_2, minuteFrom3_2, hourFrom4_2, minuteFrom4_2
    global hourFrom5_2, minuteFrom5_2, hourFrom6_2, minuteFrom6_2, hourFrom7_2, minuteFrom7_2, hourFrom8_2, minuteFrom8_2
    global hourFrom9_2, minuteFrom9_2, hourFrom10_2, minuteFrom10_2
    global hourOn1_3, minOn1_3, hourOff1_3, minOff1_3, hourOn2_3, minOn2_3, hourOff2_3, minOff2_3
    global hourOn3_3, minOn3_3, hourOff3_3, minOff3_3, hourOn4_3, minOn4_3, hourOff4_3, minOff4_3 
    global hourOn5_3, minOn5_3, hourOff5_3, minOff5_3, hourOn6_3, minOn6_3, hourOff6_3, minOff6_3  
    global hourOn7_3, minOn7_3, hourOff7_3, minOff7_3, hourOn8_3, minOn8_3, hourOff8_3, minOff8_3 
    global hourOn9_3, minOn9_3, hourOff9_3, minOff9_3, hourOn10_3, minOn10_3, hourOff10_3, minOff10_3
    global dark1_3, light1_3, dark2_3, light2_3, dark3_3, light3_3, dark4_3, light4_3, dark5_3, light5_3
    global dark6_3, light6_3, dark7_3, light7_3, dark8_3, light8_3, dark9_3, light9_3, dark10_3, light10_3 
    global date1_3, month1_3, year1_3, date2_3, month2_3, year2_3, date3_3, month3_3, year3_3, date4_3, month4_3, year4_3 
    global date5_3, month5_3, year5_3, date6_3, month6_3, year6_3, date7_3, month7_3, year7_3, date8_3, month8_3, year8_3 
    global date9_3, month9_3, year9_3, date10_3, month10_3, year10_3 
    global hourFrom1_3, minuteFrom1_3, hourFrom2_3, minuteFrom2_3, hourFrom3_3, minuteFrom3_3, hourFrom4_3, minuteFrom4_3 
    global hourFrom5_3, minuteFrom5_3, hourFrom6_3, minuteFrom6_3, hourFrom7_3, minuteFrom7_3, hourFrom8_3, minuteFrom8_3 
    global hourFrom9_3, minuteFrom9_3, hourFrom10_3, minuteFrom10_3 

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
    hourOn7_1 = config['hourOn7_1'] 
    minOn7_1 = config['minOn7_1'] 
    hourOff7_1 = config['hourOff7_1'] 
    minOff7_1 = config['minOff7_1'] 
    hourOn8_1 = config['hourOn8_1'] 
    minOn8_1 = config['minOn8_1'] 
    hourOff8_1 = config['hourOff8_1'] 
    minOff8_1 = config['minOff8_1'] 
    hourOn9_1 =config['hourOn9_1'] 
    minOn9_1 = config['minOn9_1'] 
    hourOff9_1 = config['hourOff9_1'] 
    minOff9_1 = config['minOff9_1'] 
    hourOn10_1 =config['hourOn10_1'] 
    minOn10_1 = config['minOn10_1']   
    hourOff10_1 = config['hourOff10_1'] 
    minOff10_1 = config['minOff10_1'] 
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
    dark7_1 = config['dark7_1']
    light7_1 = config['light7_1'] 
    dark8_1 = config['dark8_1'] 
    light8_1 = config['light8_1'] 
    dark9_1 = config['dark9_1']
    light9_1 = config['light9_1'] 
    dark10_1 = config['dark10_1'] 
    light10_1 = config['light10_1'] 
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
    hourOn7_2 = config['hourOn7_2'] 
    minOn7_2 = config['minOn7_2'] 
    hourOff7_2 = config['hourOff7_2'] 
    minOff7_2 = config['minOff7_2'] 
    hourOn8_2 = config['hourOn8_2'] 
    minOn8_2 = config['minOn8_2'] 
    hourOff8_2 = config['hourOff8_2'] 
    minOff8_2 = config['minOff8_2']
    hourOn9_2 = config['hourOn9_2']
    minOn9_2 = config['minOn9_2'] 
    hourOff9_2 = config['hourOff9_2'] 
    minOff9_2 = config['minOff9_2'] 
    hourOn10_2 = config['hourOn10_2'] 
    minOn10_2 = config['minOn10_2'] 
    hourOff10_2 = config['hourOff10_2'] 
    minOff10_2 = config['minOff10_2'] 
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
    dark7_2 = config['dark7_2'] 
    light7_2 = config['light7_2'] 
    dark8_2 = config['dark8_2'] 
    light8_2 = config['light8_2'] 
    dark9_2 = config['dark9_2'] 
    light9_2 = config['light9_2'] 
    dark10_2 = config['dark10_2'] 
    light10_2 = config['light10_2'] 
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
    date6_2 = config['date6_2'] 
    month6_2 = config['month6_2'] 
    year6_2 = config['year6_2'] 
    date7_2 = config['date7_2'] 
    month7_2 = config['month7_2'] 
    year7_2 = config['year7_2'] 
    date8_2 = config['date8_2'] 
    month8_2 = config['month8_2'] 
    year8_2 = config['year8_2'] 
    date9_2 = config['date9_2'] 
    month9_2 = config['month9_2'] 
    year9_2 = config['year9_2'] 
    date10_2 = config['date10_2'] 
    month10_2 = config['month10_2'] 
    year10_2 = config['year10_2'] 
    hourFrom6_2 = config['hourFrom6_2'] 
    minuteFrom6_2 = config['minuteFrom6_2'] 
    hourFrom7_2 = config['hourFrom7_2'] 
    minuteFrom7_2 = config['minuteFrom7_2'] 
    hourFrom8_2 = config['hourFrom8_2'] 
    minuteFrom8_2 = config['minuteFrom8_2'] 
    hourFrom9_2 = config['hourFrom9_2'] 
    minuteFrom9_2 = config['minuteFrom9_2'] 
    hourFrom10_2 = config['hourFrom10_2'] 
    minuteFrom10_2 = config['minuteFrom10_2'] 
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
    hourOn7_3 = config['hourOn7_3'] 
    minOn7_3 = config['minOn7_3'] 
    hourOff7_3 = config['hourOff7_3'] 
    minOff7_3 = config['minOff7_3'] 
    hourOn8_3 = config['hourOn8_3'] 
    minOn8_3 = config['minOn8_3'] 
    hourOff8_3 = config['hourOff8_3'] 
    minOff8_3 = config['minOff8_3'] 
    hourOn9_3 = config['hourOn9_3'] 
    minOn9_3 = config['minOn9_3'] 
    hourOff9_3 = config['hourOff9_3'] 
    minOff9_3 = config['minOff9_3'] 
    hourOn10_3 = config['hourOn10_3'] 
    minOn10_3 = config['minOn10_3'] 
    hourOff10_3 = config['hourOff10_3'] 
    minOff10_3 = config['minOff10_3'] 
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
    dark7_3 = config['dark7_3'] 
    light7_3 = config['light7_3'] 
    dark8_3 = config['dark8_3'] 
    light8_3 = config['light8_3'] 
    dark9_3 = config['dark9_3'] 
    light9_3 = config['light9_3'] 
    dark10_3 = config['dark10_3'] 
    light10_3 = config['light10_3'] 
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
    date6_3 = config['date6_3'] 
    month6_3 = config['month6_3'] 
    year6_3 = config['year6_3'] 
    date7_3 = config['date7_3'] 
    month7_3 = config['month7_3'] 
    year7_3 = config['year7_3'] 
    date8_3 = config['date8_3'] 
    month8_3 = config['month8_3'] 
    year8_3 = config['year8_3'] 
    date9_3 = config['date9_3'] 
    month9_3 = config['month9_3'] 
    year9_3 = config['year9_3'] 
    date10_3 = config['date10_3'] 
    month10_3 = config['month10_3'] 
    year10_3 = config['year10_3'] 
    hourFrom6_3 = config['hourFrom6_3'] 
    minuteFrom6_3 = config['minuteFrom6_3'] 
    hourFrom7_3 = config['hourFrom7_3'] 
    minuteFrom7_3 = config['minuteFrom7_3'] 
    hourFrom8_3 = config['hourFrom8_3'] 
    minuteFrom8_3 = config['minuteFrom8_3'] 
    hourFrom9_3 = config['hourFrom9_3'] 
    minuteFrom9_3 = config['minuteFrom9_3'] 
    hourFrom10_3 = config['hourFrom10_3'] 
    minuteFrom10_3 = config['minuteFrom10_3'] 

    btnRun['state']='normal'
    show_conf()
    window.update_idletasks()

    status.pack(side='bottom', fill='x')
    status.set('The schedule configuration is loaded.')
    box1sched_text.set('Box1 schedule loaded.')
    box2sched_text.set('Box2 schedule loaded.')
    box3sched_text.set('Box3 schedule loaded.')
    box4sched_text.set('Box4 schedule loaded.')
    box5sched_text.set('Box5 schedule loaded.')
    box6sched_text.set('Box6 schedule loaded.')
    box7sched_text.set('Box7 schedule loaded.')
    box8sched_text.set('Box8 schedule loaded.')
    box9sched_text.set('Box9 schedule loaded.')
    box10sched_text.set('Box10 schedule loaded.')
    window.update_idletasks()

def show_conf(): # Show schedule configuration
    global hourOn1_1, minOn1_1, hourOff1_1, minOff1_1, hourOn2_1, minOn2_1, hourOff2_1, minOff2_1 
    global hourOn3_1, minOn3_1, hourOff3_1, minOff3_1, hourOn4_1, minOn4_1, hourOff4_1, minOff4_1 
    global hourOn5_1, minOn5_1, hourOff5_1, minOff5_1, hourOn6_1, minOn6_1,  hourOff6_1, minOff6_1  
    global hourOn7_1, minOn7_1, hourOff7_1, minOff7_1, hourOn8_1, minOn8_1, hourOff8_1, minOff8_1 
    global hourOn9_1, minOn9_1, hourOff9_1, minOff9_1, hourOn10_1, minOn10_1, hourOff10_1, minOff10_1
    global dark1_1, light1_1, dark2_1, light2_1, dark3_1, light3_1, dark4_1, light4_1, dark5_1, light5_1  
    global dark6_1, light6_1, dark7_1, light7_1, dark8_1, light8_1, dark9_1, light9_1, dark10_1, light10_1  
    global hourOn3_2, minOn3_2, hourOff3_2, minOff3_2, hourOn1_2, minOn1_2, hourOff1_2, minOff1_2
    global hourOn2_2, minOn2_2, hourOff2_2, minOff2_2, hourOn4_2, minOn4_2, hourOff4_2, minOff4_2 
    global hourOn5_2, minOn5_2, hourOff5_2, minOff5_2, hourOn6_2, minOn6_2, hourOff6_2, minOff6_2 
    global hourOn7_2, minOn7_2, hourOff7_2, minOff7_2, hourOn8_2, minOn8_2, hourOff8_2, minOff8_2 
    global hourOn9_2, minOn9_2, hourOff9_2, minOff9_2, hourOn10_2, minOn10_2, hourOff10_2, minOff10_2  
    global dark1_2, light1_2, dark2_2, light2_2, dark3_2, light3_2, dark4_2, light4_2, dark5_2, light5_2 
    global dark6_2, light6_2, dark7_2, light7_2, dark8_2, light8_2, dark9_2, light9_2, dark10_2, light10_2 
    global date1_2, month1_2, year1_2, date2_2, month2_2, year2_2, date3_2, month3_2, year3_2, date4_2, month4_2, year4_2 
    global date5_2, month5_2, year5_2, date6_2, month6_2, year6_2, date7_2, month7_2, year7_2  
    global date8_2, month8_2, year8_2, date9_2, month9_2, year9_2, date10_2, month10_2, year10_2 
    global hourFrom1_2, minuteFrom1_2, hourFrom2_2, minuteFrom2_2, hourFrom3_2, minuteFrom3_2, hourFrom4_2, minuteFrom4_2
    global hourFrom5_2, minuteFrom5_2, hourFrom6_2, minuteFrom6_2, hourFrom7_2, minuteFrom7_2, hourFrom8_2, minuteFrom8_2
    global hourFrom9_2, minuteFrom9_2, hourFrom10_2, minuteFrom10_2
    global hourOn1_3, minOn1_3, hourOff1_3, minOff1_3, hourOn2_3, minOn2_3, hourOff2_3, minOff2_3
    global hourOn3_3, minOn3_3, hourOff3_3, minOff3_3, hourOn4_3, minOn4_3, hourOff4_3, minOff4_3 
    global hourOn5_3, minOn5_3, hourOff5_3, minOff5_3, hourOn6_3, minOn6_3, hourOff6_3, minOff6_3  
    global hourOn7_3, minOn7_3, hourOff7_3, minOff7_3, hourOn8_3, minOn8_3, hourOff8_3, minOff8_3 
    global hourOn9_3, minOn9_3, hourOff9_3, minOff9_3, hourOn10_3, minOn10_3, hourOff10_3, minOff10_3
    global dark1_3, light1_3, dark2_3, light2_3, dark3_3, light3_3, dark4_3, light4_3, dark5_3, light5_3
    global dark6_3, light6_3, dark7_3, light7_3, dark8_3, light8_3, dark9_3, light9_3, dark10_3, light10_3 
    global date1_3, month1_3, year1_3, date2_3, month2_3, year2_3, date3_3, month3_3, year3_3, date4_3, month4_3, year4_3 
    global date5_3, month5_3, year5_3, date6_3, month6_3, year6_3, date7_3, month7_3, year7_3, date8_3, month8_3, year8_3 
    global date9_3, month9_3, year9_3, date10_3, month10_3, year10_3 
    global hourFrom1_3, minuteFrom1_3, hourFrom2_3, minuteFrom2_3, hourFrom3_3, minuteFrom3_3, hourFrom4_3, minuteFrom4_3 
    global hourFrom5_3, minuteFrom5_3, hourFrom6_3, minuteFrom6_3, hourFrom7_3, minuteFrom7_3, hourFrom8_3, minuteFrom8_3 
    global hourFrom9_3, minuteFrom9_3, hourFrom10_3, minuteFrom10_3 

    col11_1 = Label(tab11, text='Phase 1')
    col11_2 = Label(tab11, text='Phase 2')
    col11_3 = Label(tab11, text='Phase 3')

    row11_1 = Label(tab11, text='Box1')
    row11_2 = Label(tab11, text='Box2')
    row11_3 = Label(tab11, text='Box3')
    row11_4 = Label(tab11, text='Box4')
    row11_5 = Label(tab11, text='Box5')
    row11_6 = Label(tab11, text='Box6')
    row11_7 = Label(tab11, text='Box7')
    row11_8 = Label(tab11, text='Box8')
    row11_9 = Label(tab11, text='Box9')
    row11_10 = Label(tab11, text='Box10')

    col11_1.grid(column=2,row=0,padx=5)
    col11_2.grid(column=4,row=0,padx=5)
    col11_3.grid(column=6,row=0,padx=5)

    schedSep = ttk.Separator(tab11, orient=HORIZONTAL)
    schedSep.grid(column=0, row = 1, columnspan='8', sticky='we')
    schedSep2 = ttk.Separator(tab11, orient=VERTICAL)
    schedSep2.grid(column=1, row = 2, rowspan='10', sticky='ns')
    schedSep3 = ttk.Separator(tab11, orient=VERTICAL)
    schedSep3.grid(column=3, row = 2, rowspan='10', sticky='ns')
    schedSep4 = ttk.Separator(tab11, orient=VERTICAL)
    schedSep4.grid(column=5, row = 2, rowspan='10', sticky='ns')
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

    box1pha1text=StringVar()
    box1pha1text.set('                                ')
    box1pha1_LD=Label(tab11, textvariable=box1pha1text, width=32, anchor=W, justify=LEFT)
    box1pha1_LD.grid(column=2,row=2,padx=2,pady=0)
    box1pha2text=StringVar()
    box1pha2text.set('                                ')
    box1pha2_LD=Label(tab11, textvariable=box1pha2text, width=32, anchor=W, justify=LEFT)
    box1pha2_LD.grid(column=4,row=2,padx=2,pady=0)
    box1pha3text=StringVar()
    box1pha3text.set('                                ')
    box1pha3_LD=Label(tab11, textvariable=box1pha3text, width=32, anchor=W, justify=LEFT)
    box1pha3_LD.grid(column=6,row=2,padx=2,pady=0)
    window.update_idletasks()

    box2pha1text=StringVar()
    box2pha1text.set('                                ')
    box2pha1_LD=Label(tab11, textvariable=box2pha1text, width=32, anchor=W, justify=LEFT)
    box2pha1_LD.grid(column=2,row=3,padx=2,pady=0)
    box2pha2text=StringVar()
    box2pha2text.set('                                ')
    box2pha2_LD=Label(tab11, textvariable=box2pha2text, width=32, anchor=W, justify=LEFT)
    box2pha2_LD.grid(column=4,row=3,padx=2,pady=0)
    box2pha3text=StringVar()
    box2pha3text.set('                                ')
    box2pha3_LD=Label(tab11, textvariable=box2pha3text, width=32, anchor=W, justify=LEFT)
    box2pha3_LD.grid(column=6,row=3,padx=2,pady=0)
    window.update_idletasks()

    box3pha1text=StringVar()
    box3pha1text.set('                                ')
    box3pha1_LD=Label(tab11, textvariable=box3pha1text, width=32, anchor=W, justify=LEFT)
    box3pha1_LD.grid(column=2,row=4,padx=2,pady=0)
    box3pha2text=StringVar()
    box3pha2text.set('                                ')
    box3pha2_LD=Label(tab11, textvariable=box3pha2text, width=32, anchor=W, justify=LEFT)
    box3pha2_LD.grid(column=4,row=4,padx=2,pady=0)
    box3pha3text=StringVar()
    box3pha3text.set('                                ')
    box3pha3_LD=Label(tab11, textvariable=box3pha3text, width=32, anchor=W, justify=LEFT)
    box3pha3_LD.grid(column=6,row=4,padx=2,pady=0)
    window.update_idletasks()

    box4pha1text=StringVar()
    box4pha1text.set('                                ')
    box4pha1_LD=Label(tab11, textvariable=box4pha1text, width=32, anchor=W, justify=LEFT)
    box4pha1_LD.grid(column=2,row=5,padx=2,pady=0)
    box4pha2text=StringVar()
    box4pha2text.set('                                ')
    box4pha2_LD=Label(tab11, textvariable=box4pha2text, width=32, anchor=W, justify=LEFT)
    box4pha2_LD.grid(column=4,row=5,padx=2,pady=0)
    box4pha3text=StringVar()
    box4pha3text.set('                                ')
    box4pha3_LD=Label(tab11, textvariable=box4pha3text, width=32, anchor=W, justify=LEFT)
    box4pha3_LD.grid(column=6,row=5,padx=2,pady=0)
    window.update_idletasks()

    box5pha1text=StringVar()
    box5pha1text.set('                                ')
    box5pha1_LD=Label(tab11, textvariable=box5pha1text, width=32, anchor=W, justify=LEFT)
    box5pha1_LD.grid(column=2,row=6,padx=2,pady=0)
    box5pha2text=StringVar()
    box5pha2text.set('                                ')
    box5pha2_LD=Label(tab11, textvariable=box5pha2text, width=32, anchor=W, justify=LEFT)
    box5pha2_LD.grid(column=4,row=6,padx=2,pady=0)
    box5pha3text=StringVar()
    box5pha3text.set('                                ')
    box5pha3_LD=Label(tab11, textvariable=box5pha3text, width=32, anchor=W, justify=LEFT)
    box5pha3_LD.grid(column=6,row=6,padx=2,pady=0)
    window.update_idletasks()

    box6pha1text=StringVar()
    box6pha1text.set('                                ')
    box6pha1_LD=Label(tab11, textvariable=box6pha1text, width=32, anchor=W, justify=LEFT)
    box6pha1_LD.grid(column=2,row=7,padx=2,pady=0)
    box6pha2text=StringVar()
    box6pha2text.set('                                ')
    box6pha2_LD=Label(tab11, textvariable=box6pha2text, width=32, anchor=W, justify=LEFT)
    box6pha2_LD.grid(column=4,row=7,padx=2,pady=0)
    box6pha3text=StringVar()
    box6pha3text.set('                                ')
    box6pha3_LD=Label(tab11, textvariable=box6pha3text, width=32, anchor=W, justify=LEFT)
    box6pha3_LD.grid(column=6,row=7,padx=2,pady=0)
    window.update_idletasks()

    box7pha1text=StringVar()
    box7pha1text.set('                                ')
    box7pha1_LD=Label(tab11, textvariable=box7pha1text, width=32, anchor=W, justify=LEFT)
    box7pha1_LD.grid(column=2,row=8,padx=2,pady=0)
    box7pha2text=StringVar()
    box7pha2text.set('                                ')
    box7pha2_LD=Label(tab11, textvariable=box7pha2text, width=32, anchor=W, justify=LEFT)
    box7pha2_LD.grid(column=4,row=8,padx=2,pady=0)
    box7pha3text=StringVar()
    box7pha3text.set('                                ')
    box7pha3_LD=Label(tab11, textvariable=box7pha3text, width=32, anchor=W, justify=LEFT)
    box7pha3_LD.grid(column=6,row=8,padx=2,pady=0)
    window.update_idletasks()

    box8pha1text=StringVar()
    box8pha1text.set('                                ')
    box8pha1_LD=Label(tab11, textvariable=box8pha1text, width=32, anchor=W, justify=LEFT)
    box8pha1_LD.grid(column=2,row=9,padx=2,pady=0)
    box8pha2text=StringVar()
    box8pha2text.set('                                ')
    box8pha2_LD=Label(tab11, textvariable=box8pha2text, width=32, anchor=W, justify=LEFT)
    box8pha2_LD.grid(column=4,row=9,padx=2,pady=0)
    box8pha3text=StringVar()
    box8pha3text.set('                                ')
    box8pha3_LD=Label(tab11, textvariable=box8pha3text, width=32, anchor=W, justify=LEFT)
    box8pha3_LD.grid(column=6,row=9,padx=2,pady=0)
    window.update_idletasks()

    box9pha1text=StringVar()
    box9pha1text.set('                                ')
    box9pha1_LD=Label(tab11, textvariable=box9pha1text, width=32, anchor=W, justify=LEFT)
    box9pha1_LD.grid(column=2,row=10,padx=2,pady=0)
    box9pha2text=StringVar()
    box9pha2text.set('                                ')
    box9pha2_LD=Label(tab11, textvariable=box9pha2text, width=32, anchor=W, justify=LEFT)
    box9pha2_LD.grid(column=4,row=10,padx=2,pady=0)
    box9pha3text=StringVar()
    box9pha3text.set('                                ')
    box9pha3_LD=Label(tab11, textvariable=box9pha3text, width=32, anchor=W, justify=LEFT)
    box9pha3_LD.grid(column=6,row=10,padx=2,pady=0)
    window.update_idletasks()

    box10pha1text=StringVar()
    box10pha1text.set('                                ')
    box10pha1_LD=Label(tab11, textvariable=box10pha1text, width=32, anchor=W, justify=LEFT)
    box10pha1_LD.grid(column=2,row=11,padx=2,pady=0)
    box10pha2text=StringVar()
    box10pha2text.set('                                ')
    box10pha2_LD=Label(tab11, textvariable=box10pha2text, width=32, anchor=W, justify=LEFT)
    box10pha2_LD.grid(column=4,row=11,padx=2,pady=0)
    box10pha3text=StringVar()
    box10pha3text.set('                                ')
    box10pha3_LD=Label(tab11, textvariable=box10pha3text, width=32, anchor=W, justify=LEFT)
    box10pha3_LD.grid(column=6,row=11,padx=2,pady=0)
    window.update_idletasks()

    if light1_1=='0' and dark1_1=='0':
        box1pha1text.set('                                ')
        window.update_idletasks()
        box1pha1text.set('From record onset'+' | '+hourOn1_1+':'+minOn1_1+' on>'+hourOff1_1+':'+minOff1_1+' off')
        window.update_idletasks()
    if light1_2=='0' and dark1_2=='0':
        box1pha2text.set('                                ')
        window.update_idletasks()
        box1pha2text.set(year1_2+'/'+month1_2+'/'+date1_2+' '+hourFrom2_2+':'+minuteFrom1_2+' | '+hourOn1_2+':'+minOn1_2+' on>'+hourOff1_2+':'+minOff1_2+' off')
        window.update_idletasks()
    if light1_3=='0' and dark1_3=='0':
        box1pha3text.set('                                ')
        window.update_idletasks()
        box1pha3text.set(year1_3+'/'+month1_3+'/'+date1_3+' '+hourFrom2_3+':'+minuteFrom1_3+' | '+hourOn1_3+':'+minOn1_3+' on>'+hourOff1_3+':'+minOff1_3+' off')
        window.update_idletasks()
    if light1_1=='0' and dark1_1=='1':
        box1pha1text.set('                                ')
        window.update_idletasks()
        box1pha1text.set('From record onset'+' | '+'DD')
        window.update_idletasks()
    if light1_2=='0' and dark1_2=='1':
        box1pha2text.set('                                ')
        window.update_idletasks()
        box1pha2text.set(year1_2+'/'+month1_2+'/'+date1_2+' '+hourFrom2_2+':'+minuteFrom1_2+' | '+'DD')
        window.update_idletasks()
    if light1_3=='0' and dark1_3=='1':
        box1pha3text.set('                                ')
        window.update_idletasks()
        box1pha3text.set(year1_3+'/'+month1_3+'/'+date1_3+' '+hourFrom2_3+':'+minuteFrom1_3+' | '+'DD')
        window.update_idletasks()
    if light1_1=='1' and dark1_1=='0':
        box1pha1text.set('                                ')
        window.update_idletasks()
        box1pha1text.set('From record onset'+' | '+'LL')
        window.update_idletasks()
    if light1_2=='1' and dark1_2=='0':
        box1pha2text.set('                                ')
        window.update_idletasks()
        box1pha2text.set(year1_2+'/'+month1_2+'/'+date1_2+' '+hourFrom2_2+':'+minuteFrom1_2+' | '+'LL')
        window.update_idletasks()
    if light1_3=='1' and dark1_3=='0':
        box1pha3text.set('                                 ')
        window.update_idletasks()
        box1pha3text.set(year1_3+'/'+month1_3+'/'+date1_3+' '+hourFrom2_3+':'+minuteFrom1_3+' | '+'LL')
        window.update_idletasks()

    if light2_1=='0' and dark2_1=='0':
        box2pha1text.set('                                ')
        window.update_idletasks()
        box2pha1text.set('From record onset'+' | '+hourOn2_1+':'+minOn2_1+' on>'+hourOff2_1+':'+minOff2_1+' off')
        window.update_idletasks()
    if light2_2=='0' and dark2_2=='0':
        box2pha2text.set('                                ')
        window.update_idletasks()
        box2pha2text.set(year2_2+'/'+month2_2+'/'+date2_2+' '+hourFrom2_2+':'+minuteFrom2_2+' | '+hourOn2_2+':'+minOn2_2+' on>'+hourOff2_2+':'+minOff2_2+' off')
        window.update_idletasks()
    if light2_3=='0' and dark2_3=='0':
        box2pha3text.set('                                ')
        window.update_idletasks()
        box2pha3text.set(year2_3+'/'+month2_3+'/'+date2_3+' '+hourFrom2_3+':'+minuteFrom2_3+' | '+hourOn2_3+':'+minOn2_3+' on>'+hourOff2_3+':'+minOff2_3+' off')
        window.update_idletasks()
    if light2_1=='0' and dark2_1=='1':
        box2pha1text.set('                                ')
        window.update_idletasks()
        box2pha1text.set('From record onset'+' | '+'DD')
        window.update_idletasks()
    if light2_2=='0' and dark2_2=='1':
        box2pha2text.set('                                ')
        window.update_idletasks()
        box2pha2text.set(year2_2+'/'+month2_2+'/'+date2_2+' '+hourFrom2_2+':'+minuteFrom2_2+' | '+'DD')
        window.update_idletasks()
    if light2_3=='0' and dark2_3=='1':
        box2pha3text.set('                                ')
        window.update_idletasks()
        box2pha3text.set(year2_3+'/'+month2_3+'/'+date2_3+' '+hourFrom2_3+':'+minuteFrom2_3+' | '+'DD')
        window.update_idletasks()
    if light2_1=='1' and dark2_1=='0':
        box2pha1text.set('                                ')
        window.update_idletasks()
        box2pha1text.set('From record onset'+' | '+'LL')
        window.update_idletasks()
    if light2_2=='1' and dark2_2=='0':
        box2pha2text.set('                                ')
        window.update_idletasks()
        box2pha2text.set(year2_2+'/'+month2_2+'/'+date2_2+' '+hourFrom2_2+':'+minuteFrom2_2+' | '+'LL')
        window.update_idletasks()
    if light2_3=='1' and dark2_3=='0':
        box2pha3text.set('                                 ')
        window.update_idletasks()
        box2pha3text.set(year2_3+'/'+month2_3+'/'+date2_3+' '+hourFrom2_3+':'+minuteFrom2_3+' | '+'LL')
        window.update_idletasks()

    if light3_1=='0' and dark3_1=='0':
        box3pha1text.set('                                ')
        window.update_idletasks()
        box3pha1text.set('From record onset'+' | '+hourOn3_1+':'+minOn3_1+' on>'+hourOff3_1+':'+minOff3_1+' off')
        window.update_idletasks()
    if light3_2=='0' and dark3_2=='0':
        box3pha2text.set('                                ')
        window.update_idletasks()
        box3pha2text.set(year3_2+'/'+month3_2+'/'+date3_2+' '+hourFrom3_2+':'+minuteFrom3_2+' | '+hourOn3_2+':'+minOn3_2+' on>'+hourOff3_2+':'+minOff3_2+' off')
        window.update_idletasks()
    if light3_3=='0' and dark3_3=='0':
        box3pha3text.set('                                ')
        window.update_idletasks()
        box3pha3text.set(year3_3+'/'+month3_3+'/'+date3_3+' '+hourFrom3_3+':'+minuteFrom3_3+' | '+hourOn3_3+':'+minOn3_3+' on>'+hourOff3_3+':'+minOff3_3+' off')
        window.update_idletasks()
    if light3_1=='0' and dark3_1=='1':
        box3pha1text.set('                                ')
        window.update_idletasks()
        box3pha1text.set('From record onset'+' | '+'DD')
        window.update_idletasks()
    if light3_2=='0' and dark3_2=='1':
        box3pha2text.set('                                ')
        window.update_idletasks()
        box3pha2text.set(year3_2+'/'+month3_2+'/'+date3_2+' '+hourFrom3_2+':'+minuteFrom3_2+' | '+'DD')
        window.update_idletasks()
    if light3_3=='0' and dark3_3=='1':
        box3pha3text.set('                                ')
        window.update_idletasks()
        box3pha3text.set(year3_3+'/'+month3_3+'/'+date3_3+' '+hourFrom3_3+':'+minuteFrom3_3+' | '+'DD')
        window.update_idletasks()
    if light3_1=='1' and dark3_1=='0':
        box3pha1text.set('                                ')
        window.update_idletasks()
        box3pha1text.set('From record onset'+' | '+'LL')
        window.update_idletasks()
    if light3_2=='1' and dark3_2=='0':
        box3pha2text.set('                                ')
        window.update_idletasks()
        box3pha2text.set(year3_2+'/'+month3_2+'/'+date3_2+' '+hourFrom3_2+':'+minuteFrom3_2+' | '+'LL')
        window.update_idletasks()
    if light3_3=='1' and dark3_3=='0':
        box3pha3text.set('                                 ')
        window.update_idletasks()
        box3pha3text.set(year3_3+'/'+month3_3+'/'+date3_3+' '+hourFrom3_3+':'+minuteFrom3_3+' | '+'LL')
        window.update_idletasks()

    if light4_1=='0' and dark4_1=='0':
        box4pha1text.set('                                ')
        window.update_idletasks()
        box4pha1text.set('From record onset'+' | '+hourOn4_1+':'+minOn4_1+' on>'+hourOff4_1+':'+minOff4_1+' off')
        window.update_idletasks()
    if light4_2=='0' and dark4_2=='0':
        box4pha2text.set('                                ')
        window.update_idletasks()
        box4pha2text.set(year4_2+'/'+month4_2+'/'+date4_2+' '+hourFrom4_2+':'+minuteFrom4_2+' | '+hourOn4_2+':'+minOn4_2+' on>'+hourOff4_2+':'+minOff4_2+' off')
        window.update_idletasks()
    if light4_3=='0' and dark4_3=='0':
        box4pha3text.set('                                ')
        window.update_idletasks()
        box4pha3text.set(year4_3+'/'+month4_3+'/'+date4_3+' '+hourFrom4_3+':'+minuteFrom4_3+' | '+hourOn4_3+':'+minOn4_3+' on>'+hourOff4_3+':'+minOff4_3+' off')
        window.update_idletasks()
    if light4_1=='0' and dark4_1=='1':
        box4pha1text.set('                                ')
        window.update_idletasks()
        box4pha1text.set('From record onset'+' | '+'DD')
        window.update_idletasks()
    if light4_2=='0' and dark4_2=='1':
        box4pha2text.set('                                ')
        window.update_idletasks()
        box4pha2text.set(year4_2+'/'+month4_2+'/'+date4_2+' '+hourFrom4_2+':'+minuteFrom4_2+' | '+'DD')
        window.update_idletasks()
    if light4_3=='0' and dark4_3=='1':
        box4pha3text.set('                                ')
        window.update_idletasks()
        box4pha3text.set(year4_3+'/'+month4_3+'/'+date4_3+' '+hourFrom4_3+':'+minuteFrom4_3+' | '+'DD')
        window.update_idletasks()
    if light4_1=='1' and dark4_1=='0':
        box4pha1text.set('                                ')
        window.update_idletasks()
        box4pha1text.set('From record onset'+' | '+'LL')
        window.update_idletasks()
    if light4_2=='1' and dark4_2=='0':
        box4pha2text.set('                                ')
        window.update_idletasks()
        box4pha2text.set(year4_2+'/'+month4_2+'/'+date4_2+' '+hourFrom4_2+':'+minuteFrom4_2+' | '+'LL')
        window.update_idletasks()
    if light4_3=='1' and dark4_3=='0':
        box4pha3text.set('                                 ')
        window.update_idletasks()
        box4pha3text.set(year4_3+'/'+month4_3+'/'+date4_3+' '+hourFrom4_3+':'+minuteFrom4_3+' | '+'LL')
        window.update_idletasks()

    if light5_1=='0' and dark5_1=='0':
        box5pha1text.set('                                ')
        window.update_idletasks()
        box5pha1text.set('From record onset'+' | '+hourOn5_1+':'+minOn5_1+' on>'+hourOff5_1+':'+minOff5_1+' off')
        window.update_idletasks()
    if light5_2=='0' and dark5_2=='0':
        box5pha2text.set('                                ')
        window.update_idletasks()
        box5pha2text.set(year5_2+'/'+month5_2+'/'+date5_2+' '+hourFrom5_2+':'+minuteFrom5_2+' | '+hourOn5_2+':'+minOn5_2+' on>'+hourOff5_2+':'+minOff5_2+' off')
        window.update_idletasks()
    if light5_3=='0' and dark5_3=='0':
        box5pha3text.set('                                ')
        window.update_idletasks()
        box5pha3text.set(year5_3+'/'+month5_3+'/'+date5_3+' '+hourFrom5_3+':'+minuteFrom5_3+' | '+hourOn5_3+':'+minOn5_3+' on>'+hourOff5_3+':'+minOff5_3+' off')
        window.update_idletasks()
    if light5_1=='0' and dark5_1=='1':
        box5pha1text.set('                                ')
        window.update_idletasks()
        box5pha1text.set('From record onset'+' | '+'DD')
        window.update_idletasks()
    if light5_2=='0' and dark5_2=='1':
        box5pha2text.set('                                ')
        window.update_idletasks()
        box5pha2text.set(year5_2+'/'+month5_2+'/'+date5_2+' '+hourFrom5_2+':'+minuteFrom5_2+' | '+'DD')
        window.update_idletasks()
    if light5_3=='0' and dark5_3=='1':
        box5pha3text.set('                                ')
        window.update_idletasks()
        box5pha3text.set(year5_3+'/'+month5_3+'/'+date5_3+' '+hourFrom5_3+':'+minuteFrom5_3+' | '+'DD')
        window.update_idletasks()
    if light5_1=='1' and dark5_1=='0':
        box5pha1text.set('                                ')
        window.update_idletasks()
        box5pha1text.set('From record onset'+' | '+'LL')
        window.update_idletasks()
    if light5_2=='1' and dark5_2=='0':
        box5pha2text.set('                                ')
        window.update_idletasks()
        box5pha2text.set(year5_2+'/'+month5_2+'/'+date5_2+' '+hourFrom5_2+':'+minuteFrom5_2+' | '+'LL')
        window.update_idletasks()
    if light5_3=='1' and dark5_3=='0':
        box5pha3text.set('                                 ')
        window.update_idletasks()
        box5pha3text.set(year5_3+'/'+month5_3+'/'+date5_3+' '+hourFrom5_3+':'+minuteFrom5_3+' | '+'LL')
        window.update_idletasks()

    if light6_1=='0' and dark6_1=='0':
        box6pha1text.set('                                ')
        window.update_idletasks()
        box6pha1text.set('From record onset'+' | '+hourOn6_1+':'+minOn6_1+' on>'+hourOff6_1+':'+minOff6_1+' off')
        window.update_idletasks()
    if light6_2=='0' and dark6_2=='0':
        box6pha2text.set('                                ')
        window.update_idletasks()
        box6pha2text.set(year6_2+'/'+month6_2+'/'+date6_2+' '+hourFrom6_2+':'+minuteFrom6_2+' | '+hourOn6_2+':'+minOn6_2+' on>'+hourOff6_2+':'+minOff6_2+' off')
        window.update_idletasks()
    if light6_3=='0' and dark6_3=='0':
        box6pha3text.set('                                ')
        window.update_idletasks()
        box6pha3text.set(year6_3+'/'+month6_3+'/'+date6_3+' '+hourFrom6_3+':'+minuteFrom6_3+' | '+hourOn6_3+':'+minOn6_3+' on>'+hourOff6_3+':'+minOff6_3+' off')
        window.update_idletasks()
    if light6_1=='0' and dark6_1=='1':
        box6pha1text.set('                                ')
        window.update_idletasks()
        box6pha1text.set('From record onset'+' | '+'DD')
        window.update_idletasks()
    if light6_2=='0' and dark6_2=='1':
        box6pha2text.set('                                ')
        window.update_idletasks()
        box6pha2text.set(year6_2+'/'+month6_2+'/'+date6_2+' '+hourFrom6_2+':'+minuteFrom6_2+' | '+'DD')
        window.update_idletasks()
    if light6_3=='0' and dark6_3=='1':
        box6pha3text.set('                                ')
        window.update_idletasks()
        box6pha3text.set(year6_3+'/'+month6_3+'/'+date6_3+' '+hourFrom6_3+':'+minuteFrom6_3+' | '+'DD')
        window.update_idletasks()
    if light6_1=='1' and dark6_1=='0':
        box6pha1text.set('                                ')
        window.update_idletasks()
        box6pha1text.set('From record onset'+' | '+'LL')
        window.update_idletasks()
    if light6_2=='1' and dark6_2=='0':
        box6pha2text.set('                                ')
        window.update_idletasks()
        box6pha2text.set(year6_2+'/'+month6_2+'/'+date6_2+' '+hourFrom6_2+':'+minuteFrom6_2+' | '+'LL')
        window.update_idletasks()
    if light6_3=='1' and dark6_3=='0':
        box6pha3text.set('                                 ')
        window.update_idletasks()
        box6pha3text.set(year6_3+'/'+month6_3+'/'+date6_3+' '+hourFrom6_3+':'+minuteFrom6_3+' | '+'LL')
        window.update_idletasks()

    if light7_1=='0' and dark7_1=='0':
        box7pha1text.set('                                ')
        window.update_idletasks()
        box7pha1text.set('From record onset'+' | '+hourOn7_1+':'+minOn7_1+' on>'+hourOff7_1+':'+minOff7_1+' off')
        window.update_idletasks()
    if light7_2=='0' and dark7_2=='0':
        box7pha2text.set('                                ')
        window.update_idletasks()
        box7pha2text.set(year7_2+'/'+month7_2+'/'+date7_2+' '+hourFrom7_2+':'+minuteFrom7_2+' | '+hourOn7_2+':'+minOn7_2+' on>'+hourOff7_2+':'+minOff7_2+' off')
        window.update_idletasks()
    if light7_3=='0' and dark7_3=='0':
        box7pha3text.set('                                ')
        window.update_idletasks()
        box7pha3text.set(year7_3+'/'+month7_3+'/'+date7_3+' '+hourFrom7_3+':'+minuteFrom7_3+' | '+hourOn7_3+':'+minOn7_3+' on>'+hourOff7_3+':'+minOff7_3+' off')
        window.update_idletasks()
    if light7_1=='0' and dark7_1=='1':
        box7pha1text.set('                                ')
        window.update_idletasks()
        box7pha1text.set('From record onset'+' | '+'DD')
        window.update_idletasks()
    if light7_2=='0' and dark7_2=='1':
        box7pha2text.set('                                ')
        window.update_idletasks()
        box7pha2text.set(year7_2+'/'+month7_2+'/'+date7_2+' '+hourFrom7_2+':'+minuteFrom7_2+' | '+'DD')
        window.update_idletasks()
    if light7_3=='0' and dark7_3=='1':
        box7pha3text.set('                                ')
        window.update_idletasks()
        box7pha3text.set(year7_3+'/'+month7_3+'/'+date7_3+' '+hourFrom7_3+':'+minuteFrom7_3+' | '+'DD')
        window.update_idletasks()
    if light7_1=='1' and dark7_1=='0':
        box7pha1text.set('                                ')
        window.update_idletasks()
        box7pha1text.set('From record onset'+' | '+'LL')
        window.update_idletasks()
    if light7_2=='1' and dark7_2=='0':
        box7pha2text.set('                                ')
        window.update_idletasks()
        box7pha2text.set(year7_2+'/'+month7_2+'/'+date7_2+' '+hourFrom7_2+':'+minuteFrom7_2+' | '+'LL')
        window.update_idletasks()
    if light7_3=='1' and dark7_3=='0':
        box7pha3text.set('                                 ')
        window.update_idletasks()
        box7pha3text.set(year7_3+'/'+month7_3+'/'+date7_3+' '+hourFrom7_3+':'+minuteFrom7_3+' | '+'LL')
        window.update_idletasks()

    if light8_1=='0' and dark8_1=='0':
        box8pha1text.set('                                ')
        window.update_idletasks()
        box8pha1text.set('From record onset'+' | '+hourOn8_1+':'+minOn8_1+' on>'+hourOff8_1+':'+minOff8_1+' off')
        window.update_idletasks()
    if light8_2=='0' and dark8_2=='0':
        box8pha2text.set('                                ')
        window.update_idletasks()
        box8pha2text.set(year8_2+'/'+month8_2+'/'+date8_2+' '+hourFrom8_2+':'+minuteFrom8_2+' | '+hourOn8_2+':'+minOn8_2+' on>'+hourOff8_2+':'+minOff8_2+' off')
        window.update_idletasks()
    if light8_3=='0' and dark8_3=='0':
        box8pha3text.set('                                ')
        window.update_idletasks()
        box8pha3text.set(year8_3+'/'+month8_3+'/'+date8_3+' '+hourFrom8_3+':'+minuteFrom8_3+' | '+hourOn8_3+':'+minOn8_3+' on>'+hourOff8_3+':'+minOff8_3+' off')
        window.update_idletasks()
    if light8_1=='0' and dark8_1=='1':
        box8pha1text.set('                                ')
        window.update_idletasks()
        box8pha1text.set('From record onset'+' | '+'DD')
        window.update_idletasks()
    if light8_2=='0' and dark8_2=='1':
        box8pha2text.set('                                ')
        window.update_idletasks()
        box8pha2text.set(year8_2+'/'+month8_2+'/'+date8_2+' '+hourFrom8_2+':'+minuteFrom8_2+' | '+'DD')
        window.update_idletasks()
    if light8_3=='0' and dark8_3=='1':
        box8pha3text.set('                                ')
        window.update_idletasks()
        box8pha3text.set(year8_3+'/'+month8_3+'/'+date8_3+' '+hourFrom8_3+':'+minuteFrom8_3+' | '+'DD')
        window.update_idletasks()
    if light8_1=='1' and dark8_1=='0':
        box8pha1text.set('                                ')
        window.update_idletasks()
        box8pha1text.set('From record onset'+' | '+'LL')
        window.update_idletasks()
    if light8_2=='1' and dark8_2=='0':
        box8pha2text.set('                                ')
        window.update_idletasks()
        box8pha2text.set(year8_2+'/'+month8_2+'/'+date8_2+' '+hourFrom8_2+':'+minuteFrom8_2+' | '+'LL')
        window.update_idletasks()
    if light8_3=='1' and dark8_3=='0':
        box8pha3text.set('                                 ')
        window.update_idletasks()
        box8pha3text.set(year8_3+'/'+month8_3+'/'+date8_3+' '+hourFrom8_3+':'+minuteFrom8_3+' | '+'LL')
        window.update_idletasks()

    if light9_1=='0' and dark9_1=='0':
        box9pha1text.set('                                ')
        window.update_idletasks()
        box9pha1text.set('From record onset'+' | '+hourOn9_1+':'+minOn9_1+' on>'+hourOff9_1+':'+minOff9_1+' off')
        window.update_idletasks()
    if light9_2=='0' and dark9_2=='0':
        box9pha2text.set('                                ')
        window.update_idletasks()
        box9pha2text.set(year9_2+'/'+month9_2+'/'+date9_2+' '+hourFrom9_2+':'+minuteFrom9_2+' | '+hourOn9_2+':'+minOn9_2+' on>'+hourOff9_2+':'+minOff9_2+' off')
        window.update_idletasks()
    if light9_3=='0' and dark9_3=='0':
        box9pha3text.set('                                ')
        window.update_idletasks()
        box9pha3text.set(year9_3+'/'+month9_3+'/'+date9_3+' '+hourFrom9_3+':'+minuteFrom9_3+' | '+hourOn9_3+':'+minOn9_3+' on>'+hourOff9_3+':'+minOff9_3+' off')
        window.update_idletasks()
    if light9_1=='0' and dark9_1=='1':
        box9pha1text.set('                                ')
        window.update_idletasks()
        box9pha1text.set('From record onset'+' | '+'DD')
        window.update_idletasks()
    if light9_2=='0' and dark9_2=='1':
        box9pha2text.set('                                ')
        window.update_idletasks()
        box9pha2text.set(year9_2+'/'+month9_2+'/'+date9_2+' '+hourFrom9_2+':'+minuteFrom9_2+' | '+'DD')
        window.update_idletasks()
    if light9_3=='0' and dark9_3=='1':
        box9pha3text.set('                                ')
        window.update_idletasks()
        box9pha3text.set(year9_3+'/'+month9_3+'/'+date9_3+' '+hourFrom9_3+':'+minuteFrom9_3+' | '+'DD')
        window.update_idletasks()
    if light9_1=='1' and dark9_1=='0':
        box9pha1text.set('                                ')
        window.update_idletasks()
        box9pha1text.set('From record onset'+' | '+'LL')
        window.update_idletasks()
    if light9_2=='1' and dark9_2=='0':
        box9pha2text.set('                                ')
        window.update_idletasks()
        box9pha2text.set(year9_2+'/'+month9_2+'/'+date9_2+' '+hourFrom9_2+':'+minuteFrom9_2+' | '+'LL')
        window.update_idletasks()
    if light9_3=='1' and dark9_3=='0':
        box9pha3text.set('                                 ')
        window.update_idletasks()
        box9pha3text.set(year9_3+'/'+month9_3+'/'+date9_3+' '+hourFrom9_3+':'+minuteFrom9_3+' | '+'LL')
        window.update_idletasks()

    if light10_1=='0' and dark10_1=='0':
        box10pha1text.set('                                ')
        window.update_idletasks()
        box10pha1text.set('From record onset'+' | '+hourOn10_1+':'+minOn10_1+' on>'+hourOff10_1+':'+minOff10_1+' off')
        window.update_idletasks()
    if light10_2=='0' and dark10_2=='0':
        box10pha2text.set('                                ')
        window.update_idletasks()
        box10pha2text.set(year10_2+'/'+month10_2+'/'+date10_2+' '+hourFrom10_2+':'+minuteFrom10_2+' | '+hourOn10_2+':'+minOn10_2+' on>'+hourOff10_2+':'+minOff10_2+' off')
        window.update_idletasks()
    if light10_3=='0' and dark10_3=='0':
        box10pha3text.set('                                ')
        window.update_idletasks()
        box10pha3text.set(year10_3+'/'+month10_3+'/'+date10_3+' '+hourFrom10_3+':'+minuteFrom10_3+' | '+hourOn10_3+':'+minOn10_3+' on>'+hourOff10_3+':'+minOff10_3+' off')
        window.update_idletasks()
    if light10_1=='0' and dark10_1=='1':
        box10pha1text.set('                                ')
        window.update_idletasks()
        box10pha1text.set('From record onset'+' | '+'DD')
        window.update_idletasks()
    if light10_2=='0' and dark10_2=='1':
        box10pha2text.set('                                ')
        window.update_idletasks()
        box10pha2text.set(year10_2+'/'+month10_2+'/'+date10_2+' '+hourFrom10_2+':'+minuteFrom10_2+' | '+'DD')
        window.update_idletasks()
    if light10_3=='0' and dark10_3=='1':
        box10pha3text.set('                                ')
        window.update_idletasks()
        box10pha3text.set(year10_3+'/'+month10_3+'/'+date10_3+' '+hourFrom10_3+':'+minuteFrom10_3+' | '+'DD')
        window.update_idletasks()
    if light10_1=='1' and dark10_1=='0':
        box10pha1text.set('                                ')
        window.update_idletasks()
        box10pha1text.set('From record onset'+' | '+'LL')
        window.update_idletasks()
    if light10_2=='1' and dark10_2=='0':
        box10pha2text.set('                                ')
        window.update_idletasks()
        box10pha2text.set(year10_2+'/'+month10_2+'/'+date10_2+' '+hourFrom10_2+':'+minuteFrom10_2+' | '+'LL')
        window.update_idletasks()
    if light10_3=='1' and dark10_3=='0':
        box10pha3text.set('                                 ')
        window.update_idletasks()
        box10pha3text.set(year10_3+'/'+month10_3+'/'+date10_3+' '+hourFrom10_3+':'+minuteFrom10_3+' | '+'LL')
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
    box1rec_text.set('Recording stopped.')
    box2rec_text.set('Recording stopped.')
    box3rec_text.set('Recording stopped.')
    box4rec_text.set('Recording stopped.')
    box5rec_text.set('Recording stopped.')
    box6rec_text.set('Recording stopped.')
    box7rec_text.set('Recording stopped.')
    box8rec_text.set('Recording stopped.')
    box9rec_text.set('Recording stopped.')
    box10rec_text.set('Recording stopped.')
    window.update_idletasks()

def OnButtonClick(button_id):
    global setBox1, setBox2, setBox3, setBox4, setBox5, setBox6, setBox7, setBox8, setBox9, setBox10
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
        getBox6Schedule()
        setBox6=1
    elif button_id == 7:
        getBox7Schedule()
        setBox7=1
    elif button_id == 8:
        getBox8Schedule()
        setBox8=1
    elif button_id == 9:
        getBox9Schedule()
        setBox9=1
    elif button_id == 10:
        getBox10Schedule()
        setBox10=1
                
def getBox1Schedule(): 
    global setBox1
    setBox1=1
    global hourOn1_1, minOn1_1, hourOff1_1, minOff1_1, dark1_1, light1_1
    hourOn1_1=spin1_A_1.get()
    minOn1_1=spin1_B_1.get()
    hourOff1_1=spin1_C_1.get()
    minOff1_1=spin1_D_1.get()                            
    if var1_1.get()==1:
        dark1_1='0'
        light1_1='0'
    if var1_1.get()==2:
        dark1_1='1'
        light1_1='0'
    if var1_1.get()==3:
        dark1_1='0'
        light1_1='1'
    global date1_2, month1_2, year1_2, hourFrom1_2, minuteFrom1_2, hourOn1_2, minOn1_2, hourOff1_2, minOff1_2, dark1_2, light1_2
    date1_2 = date1_2_entry.get()
    month1_2 = month1_2_entry.get()
    year1_2 = year1_2_entry.get()
    hourFrom1_2= spin1_E_2.get()
    minuteFrom1_2= spin1_F_2.get()
    hourOn1_2=spin1_A_2.get()
    minOn1_2=spin1_B_2.get()
    hourOff1_2=spin1_C_2.get()
    minOff1_2=spin1_D_2.get()                            
    if var1_2.get()==1:
        dark1_2='0'
        light1_2='0'
    if var1_2.get()==2:
        dark1_2='1'
        light1_2='0'
    if var1_2.get()==3:
        dark1_2='0'
        light1_2='1'
    global date1_3, month1_3, year1_3, hourFrom1_3, minuteFrom1_3, hourOn1_3, minOn1_3, hourOff1_3, minOff1_3, dark1_3, light1_3
    date1_3 = date1_3_entry.get()
    month1_3 = month1_3_entry.get()
    year1_3 = year1_3_entry.get()
    hourFrom1_3= spin1_E_3.get()
    minuteFrom1_3= spin1_F_3.get()
    hourOn1_3=spin1_A_3.get()
    minOn1_3=spin1_B_3.get()
    hourOff1_3=spin1_C_3.get()
    minOff1_3=spin1_D_3.get()                            
    if var1_3.get()==1:
        dark1_3='0'
        light1_3='0'
    if var1_3.get()==2:
        dark1_3='1'
        light1_3='0'
    if var1_3.get()==3:
        dark1_3='0'
        light1_3='1'
    status.pack(side='bottom', fill='x')
    status.set('Box1 schedule is set.')
    box1sched_text.set('Box1 schedule set.')
    if setBox1+setBox2+setBox3+setBox4+setBox5+setBox6+setBox7+setBox8+setBox9+setBox10 == 10:
        btnSave['state']='normal'
        btnRun['state']='normal'
        show_conf()
    window.update_idletasks()

def getBox2Schedule(): 
    global setBox2
    setBox2=1
    global hourOn2_1, minOn2_1, hourOff2_1, minOff2_1, dark2_1, light2_1
    hourOn2_1=spin2_A_1.get()
    minOn2_1=spin2_B_1.get()
    hourOff2_1=spin2_C_1.get()
    minOff2_1=spin2_D_1.get()                            
    if var2_1.get()==1:
        dark2_1='0'
        light2_1='0'
    if var2_1.get()==2:
        dark2_1='1'
        light2_1='0'
    if var2_1.get()==3:
        dark2_1='0'
        light2_1='1'
    global date2_2, month2_2, year2_2, hourFrom2_2, minuteFrom2_2, hourOn2_2, minOn2_2, hourOff2_2, minOff2_2, dark2_2, light2_2
    date2_2 = date2_2_entry.get()
    month2_2 = month2_2_entry.get()
    year2_2 = year2_2_entry.get()
    hourFrom2_2= spin2_E_2.get()
    minuteFrom2_2= spin2_F_2.get()
    hourOn2_2=spin2_A_2.get()
    minOn2_2=spin2_B_2.get()
    hourOff2_2=spin2_C_2.get()
    minOff2_2=spin2_D_2.get()                            
    if var2_2.get()==1:
        dark2_2='0'
        light2_2='0'
    if var2_2.get()==2:
        dark2_2='1'
        light2_2='0'
    if var2_2.get()==3:
        dark2_2='0'
        light2_2='1'
    global date2_3, month2_3, year2_3, hourFrom2_3, minuteFrom2_3, hourOn2_3, minOn2_3, hourOff2_3, minOff2_3, dark2_3, light2_3
    date2_3 = date2_3_entry.get()
    month2_3 = month2_3_entry.get()
    year2_3 = year2_3_entry.get()
    hourFrom2_3= spin2_E_3.get()
    minuteFrom2_3= spin2_F_3.get()
    hourOn2_3=spin2_A_3.get()
    minOn2_3=spin2_B_3.get()
    hourOff2_3=spin2_C_3.get()
    minOff2_3=spin2_D_3.get()                            
    if var2_3.get()==1:
        dark2_3='0'
        light2_3='0'
    if var2_3.get()==2:
        dark2_3='1'
        light2_3='0'
    if var2_3.get()==3:
        dark2_3='0'
        light2_3='1'
    status.pack(side='bottom', fill='x')
    status.set('Box2 schedule is set.')
    box2sched_text.set('Box2 schedule set.')
    if setBox1+setBox2+setBox3+setBox4+setBox5+setBox6+setBox7+setBox8+setBox9+setBox10 == 10:
        btnSave['state']='normal'
        btnRun['state']='normal'
        show_conf()
    window.update_idletasks()

def getBox3Schedule(): 
    global setBox3
    setBox3=1
    global hourOn3_1, minOn3_1, hourOff3_1, minOff3_1, dark3_1, light3_1
    hourOn3_1=spin3_A_1.get()
    minOn3_1=spin3_B_1.get()
    hourOff3_1=spin3_C_1.get()
    minOff3_1=spin3_D_1.get()                            
    if var3_1.get()==1:
        dark3_1='0'
        light3_1='0'
    if var3_1.get()==2:
        dark3_1='1'
        light3_1='0'
    if var3_1.get()==3:
        dark3_1='0'
        light3_1='1'
    global date3_2, month3_2, year3_2, hourFrom3_2, minuteFrom3_2, hourOn3_2, minOn3_2, hourOff3_2, minOff3_2, dark3_2, light3_2
    date3_2 = date3_2_entry.get()
    month3_2 = month3_2_entry.get()
    year3_2 = year3_2_entry.get()
    hourFrom3_2= spin3_E_2.get()
    minuteFrom3_2= spin3_F_2.get()
    hourOn3_2=spin3_A_2.get()
    minOn3_2=spin3_B_2.get()
    hourOff3_2=spin3_C_2.get()
    minOff3_2=spin3_D_2.get()                            
    if var3_2.get()==1:
        dark3_2='0'
        light3_2='0'
    if var3_2.get()==2:
        dark3_2='1'
        light3_2='0'
    if var3_2.get()==3:
        dark3_2='0'
        light3_2='1'
    global date3_3, month3_3, year3_3, hourFrom3_3, minuteFrom3_3, hourOn3_3, minOn3_3, hourOff3_3, minOff3_3, dark3_3, light3_3
    date3_3 = date3_3_entry.get()
    month3_3 = month3_3_entry.get()
    year3_3 = year3_3_entry.get()
    hourFrom3_3= spin3_E_3.get()
    minuteFrom3_3= spin3_F_3.get()
    hourOn3_3=spin3_A_3.get()
    minOn3_3=spin3_B_3.get()
    hourOff3_3=spin3_C_3.get()
    minOff3_3=spin3_D_3.get()                            
    if var3_3.get()==1:
        dark3_3='0'
        light3_3='0'
    if var3_3.get()==2:
        dark3_3='1'
        light3_3='0'
    if var3_3.get()==3:
        dark3_3='0'
        light3_3='1'
    status.pack(side='bottom', fill='x')
    status.set('Box3 schedule is set.')
    box3sched_text.set('Box3 schedule set.')
    if setBox1+setBox2+setBox3+setBox4+setBox5+setBox6+setBox7+setBox8+setBox9+setBox10 == 10:
        btnSave['state']='normal'
        btnRun['state']='normal'
        show_conf()
    window.update_idletasks()

def getBox4Schedule(): 
    global setBox4
    setBox4=1
    global hourOn4_1, minOn4_1, hourOff4_1, minOff4_1, dark4_1, light4_1
    hourOn4_1=spin4_A_1.get()
    minOn4_1=spin4_B_1.get()
    hourOff4_1=spin4_C_1.get()
    minOff4_1=spin4_D_1.get()                            
    if var4_1.get()==1:
        dark4_1='0'
        light4_1='0'
    if var4_1.get()==2:
        dark4_1='1'
        light4_1='0'
    if var4_1.get()==3:
        dark4_1='0'
        light4_1='1'
    global date4_2, month4_2, year4_2, hourFrom4_2, minuteFrom4_2, hourOn4_2, minOn4_2, hourOff4_2, minOff4_2, dark4_2, light4_2
    date4_2 = date4_2_entry.get()
    month4_2 = month4_2_entry.get()
    year4_2 = year4_2_entry.get()
    hourFrom4_2= spin4_E_2.get()
    minuteFrom4_2= spin4_F_2.get()
    hourOn4_2=spin4_A_2.get()
    minOn4_2=spin4_B_2.get()
    hourOff4_2=spin4_C_2.get()
    minOff4_2=spin4_D_2.get()                            
    if var4_2.get()==1:
        dark4_2='0'
        light4_2='0'
    if var4_2.get()==2:
        dark4_2='1'
        light4_2='0'
    if var4_2.get()==3:
        dark4_2='0'
        light4_2='1'
    global date4_3, month4_3, year4_3, hourFrom4_3, minuteFrom4_3, hourOn4_3, minOn4_3, hourOff4_3, minOff4_3, dark4_3, light4_3
    date4_3 = date4_3_entry.get()
    month4_3 = month4_3_entry.get()
    year4_3 = year4_3_entry.get()
    hourFrom4_3= spin4_E_3.get()
    minuteFrom4_3= spin4_F_3.get()
    hourOn4_3=spin4_A_3.get()
    minOn4_3=spin4_B_3.get()
    hourOff4_3=spin4_C_3.get()
    minOff4_3=spin4_D_3.get()                            
    if var4_3.get()==1:
        dark4_3='0'
        light4_3='0'
    if var4_3.get()==2:
        dark4_3='1'
        light4_3='0'
    if var4_3.get()==3:
        dark4_3='0'
        light4_3='1'
    status.pack(side='bottom', fill='x')
    status.set('Box4 schedule is set.')
    box4sched_text.set('Box4 schedule set.')
    if setBox1+setBox2+setBox3+setBox4+setBox5+setBox6+setBox7+setBox8+setBox9+setBox10 == 10:
        btnSave['state']='normal'
        btnRun['state']='normal'
        show_conf()
    window.update_idletasks()

def getBox5Schedule(): 
    global setBox5
    setBox5=1
    global hourOn5_1, minOn5_1, hourOff5_1, minOff5_1, dark5_1, light5_1
    hourOn5_1=spin5_A_1.get()
    minOn5_1=spin5_B_1.get()
    hourOff5_1=spin5_C_1.get()
    minOff5_1=spin5_D_1.get()                            
    if var5_1.get()==1:
        dark5_1='0'
        light5_1='0'
    if var5_1.get()==2:
        dark5_1='1'
        light5_1='0'
    if var5_1.get()==3:
        dark5_1='0'
        light5_1='1'
    global date5_2, month5_2, year5_2, hourFrom5_2, minuteFrom5_2, hourOn5_2, minOn5_2, hourOff5_2, minOff5_2, dark5_2, light5_2
    date5_2 = date5_2_entry.get()
    month5_2 = month5_2_entry.get()
    year5_2 = year5_2_entry.get()
    hourFrom5_2= spin5_E_2.get()
    minuteFrom5_2= spin5_F_2.get()
    hourOn5_2=spin5_A_2.get()
    minOn5_2=spin5_B_2.get()
    hourOff5_2=spin5_C_2.get()
    minOff5_2=spin5_D_2.get()                            
    if var5_2.get()==1:
        dark5_2='0'
        light5_2='0'
    if var5_2.get()==2:
        dark5_2='1'
        light5_2='0'
    if var5_2.get()==3:
        dark5_2='0'
        light5_2='1'
    global date5_3, month5_3, year5_3, hourFrom5_3, minuteFrom5_3, hourOn5_3, minOn5_3, hourOff5_3, minOff5_3, dark5_3, light5_3
    date5_3 = date5_3_entry.get()
    month5_3 = month5_3_entry.get()
    year5_3 = year5_3_entry.get()
    hourFrom5_3= spin5_E_3.get()
    minuteFrom5_3= spin5_F_3.get()
    hourOn5_3=spin5_A_3.get()
    minOn5_3=spin5_B_3.get()
    hourOff5_3=spin5_C_3.get()
    minOff5_3=spin5_D_3.get()                            
    if var5_3.get()==1:
        dark5_3='0'
        light5_3='0'
    if var5_3.get()==2:
        dark5_3='1'
        light5_3='0'
    if var5_3.get()==3:
        dark5_3='0'
        light5_3='1'
    status.pack(side='bottom', fill='x')
    status.set('Box5 schedule is set.')
    box5sched_text.set('Box5 schedule set.')
    if setBox1+setBox2+setBox3+setBox4+setBox5+setBox6+setBox7+setBox8+setBox9+setBox10 == 10:
        btnSave['state']='normal'
        btnRun['state']='normal'
        show_conf()
    window.update_idletasks()

def getBox6Schedule(): 
    global setBox6
    setBox6=1
    global hourOn6_1, minOn6_1, hourOff6_1, minOff6_1, dark6_1, light6_1
    hourOn6_1=spin6_A_1.get()
    minOn6_1=spin6_B_1.get()
    hourOff6_1=spin6_C_1.get()
    minOff6_1=spin6_D_1.get()                            
    if var6_1.get()==1:
        dark6_1='0'
        light6_1='0'
    if var6_1.get()==2:
        dark6_1='1'
        light6_1='0'
    if var6_1.get()==3:
        dark6_1='0'
        light6_1='1'
    global date6_2, month6_2, year6_2, hourFrom6_2, minuteFrom6_2, hourOn6_2, minOn6_2, hourOff6_2, minOff6_2, dark6_2, light6_2
    date6_2 = date6_2_entry.get()
    month6_2 = month6_2_entry.get()
    year6_2 = year6_2_entry.get()
    hourFrom6_2= spin6_E_2.get()
    minuteFrom6_2= spin6_F_2.get()
    hourOn6_2=spin6_A_2.get()
    minOn6_2=spin6_B_2.get()
    hourOff6_2=spin6_C_2.get()
    minOff6_2=spin6_D_2.get()                            
    if var6_2.get()==1:
        dark6_2='0'
        light6_2='0'
    if var6_2.get()==2:
        dark6_2='1'
        light6_2='0'
    if var6_2.get()==3:
        dark6_2='0'
        light6_2='1'
    global date6_3, month6_3, year6_3, hourFrom6_3, minuteFrom6_3, hourOn6_3, minOn6_3, hourOff6_3, minOff6_3, dark6_3, light6_3
    date6_3 = date6_3_entry.get()
    month6_3 = month6_3_entry.get()
    year6_3 = year6_3_entry.get()
    hourFrom6_3= spin6_E_3.get()
    minuteFrom6_3= spin6_F_3.get()
    hourOn6_3=spin6_A_3.get()
    minOn6_3=spin6_B_3.get()
    hourOff6_3=spin6_C_3.get()
    minOff6_3=spin6_D_3.get()                            
    if var6_3.get()==1:
        dark6_3='0'
        light6_3='0'
    if var6_3.get()==2:
        dark6_3='1'
        light6_3='0'
    if var6_3.get()==3:
        dark6_3='0'
        light6_3='1'
    status.pack(side='bottom', fill='x')
    status.set('Box6 schedule is set.')
    box6sched_text.set('Box6 schedule set.')
    if setBox1+setBox2+setBox3+setBox4+setBox5+setBox6+setBox7+setBox8+setBox9+setBox10 == 10:
        btnSave['state']='normal'
        btnRun['state']='normal'
        show_conf()
    window.update_idletasks()

def getBox7Schedule(): 
    global setBox7
    setBox7=1
    global hourOn7_1, minOn7_1, hourOff7_1, minOff7_1, dark7_1, light7_1
    hourOn7_1=spin7_A_1.get()
    minOn7_1=spin7_B_1.get()
    hourOff7_1=spin7_C_1.get()
    minOff7_1=spin7_D_1.get()                            
    if var7_1.get()==1:
        dark7_1='0'
        light7_1='0'
    if var7_1.get()==2:
        dark7_1='1'
        light7_1='0'
    if var7_1.get()==3:
        dark7_1='0'
        light7_1='1'
    global date7_2, month7_2, year7_2, hourFrom7_2, minuteFrom7_2, hourOn7_2, minOn7_2, hourOff7_2, minOff7_2, dark7_2, light7_2
    date7_2 = date7_2_entry.get()
    month7_2 = month7_2_entry.get()
    year7_2 = year7_2_entry.get()
    hourFrom7_2= spin7_E_2.get()
    minuteFrom7_2= spin7_F_2.get()
    hourOn7_2=spin7_A_2.get()
    minOn7_2=spin7_B_2.get()
    hourOff7_2=spin7_C_2.get()
    minOff7_2=spin7_D_2.get()                            
    if var7_2.get()==1:
        dark7_2='0'
        light7_2='0'
    if var7_2.get()==2:
        dark7_2='1'
        light7_2='0'
    if var7_2.get()==3:
        dark7_2='0'
        light7_2='1'
    global date7_3, month7_3, year7_3, hourFrom7_3, minuteFrom7_3, hourOn7_3, minOn7_3, hourOff7_3, minOff7_3, dark7_3, light7_3
    date7_3 = date7_3_entry.get()
    month7_3 = month7_3_entry.get()
    year7_3 = year7_3_entry.get()
    hourFrom7_3= spin7_E_3.get()
    minuteFrom7_3= spin7_F_3.get()
    hourOn7_3=spin7_A_3.get()
    minOn7_3=spin7_B_3.get()
    hourOff7_3=spin7_C_3.get()
    minOff7_3=spin7_D_3.get()                            
    if var7_3.get()==1:
        dark7_3='0'
        light7_3='0'
    if var7_3.get()==2:
        dark7_3='1'
        light7_3='0'
    if var7_3.get()==3:
        dark7_3='0'
        light7_3='1'
    status.pack(side='bottom', fill='x')
    status.set('Box7 schedule is set.')
    box7sched_text.set('Box7 schedule set.')
    if setBox1+setBox2+setBox3+setBox4+setBox5+setBox6+setBox7+setBox8+setBox9+setBox10 == 10:
        btnSave['state']='normal'
        btnRun['state']='normal'
        show_conf()
    window.update_idletasks()

def getBox8Schedule(): 
    global setBox8
    setBox8=1
    global hourOn8_1, minOn8_1, hourOff8_1, minOff8_1, dark8_1, light8_1
    hourOn8_1=spin8_A_1.get()
    minOn8_1=spin8_B_1.get()
    hourOff8_1=spin8_C_1.get()
    minOff8_1=spin8_D_1.get()                            
    if var8_1.get()==1:
        dark8_1='0'
        light8_1='0'
    if var8_1.get()==2:
        dark8_1='1'
        light8_1='0'
    if var8_1.get()==3:
        dark8_1='0'
        light8_1='1'
    global date8_2, month8_2, year8_2, hourFrom8_2, minuteFrom8_2, hourOn8_2, minOn8_2, hourOff8_2, minOff8_2, dark8_2, light8_2
    date8_2 = date8_2_entry.get()
    month8_2 = month8_2_entry.get()
    year8_2 = year8_2_entry.get()
    hourFrom8_2= spin8_E_2.get()
    minuteFrom8_2= spin8_F_2.get()
    hourOn8_2=spin8_A_2.get()
    minOn8_2=spin8_B_2.get()
    hourOff8_2=spin8_C_2.get()
    minOff8_2=spin8_D_2.get()                            
    if var8_2.get()==1:
        dark8_2='0'
        light8_2='0'
    if var8_2.get()==2:
        dark8_2='1'
        light8_2='0'
    if var8_2.get()==3:
        dark8_2='0'
        light8_2='1'
    global date8_3, month8_3, year8_3, hourFrom8_3, minuteFrom8_3, hourOn8_3, minOn8_3, hourOff8_3, minOff8_3, dark8_3, light8_3
    date8_3 = date8_3_entry.get()
    month8_3 = month8_3_entry.get()
    year8_3 = year8_3_entry.get()
    hourFrom8_3= spin8_E_3.get()
    minuteFrom8_3= spin8_F_3.get()
    hourOn8_3=spin8_A_3.get()
    minOn8_3=spin8_B_3.get()
    hourOff8_3=spin8_C_3.get()
    minOff8_3=spin8_D_3.get()                            
    if var8_3.get()==1:
        dark8_3='0'
        light8_3='0'
    if var8_3.get()==2:
        dark8_3='1'
        light8_3='0'
    if var8_3.get()==3:
        dark8_3='0'
        light8_3='1'
    status.pack(side='bottom', fill='x')
    status.set('Box8 schedule is set.')
    box8sched_text.set('Box8 schedule set.')
    if setBox1+setBox2+setBox3+setBox4+setBox5+setBox6+setBox7+setBox8+setBox9+setBox10 == 10:
        btnSave['state']='normal'
        btnRun['state']='normal'
        show_conf()
    window.update_idletasks()

def getBox9Schedule(): 
    global setBox9
    setBox9=1
    global hourOn9_1, minOn9_1, hourOff9_1, minOff9_1, dark9_1, light9_1
    hourOn9_1=spin9_A_1.get()
    minOn9_1=spin9_B_1.get()
    hourOff9_1=spin9_C_1.get()
    minOff9_1=spin9_D_1.get()                            
    if var9_1.get()==1:
        dark9_1='0'
        light9_1='0'
    if var9_1.get()==2:
        dark9_1='1'
        light9_1='0'
    if var9_1.get()==3:
        dark9_1='0'
        light9_1='1'
    global date9_2, month9_2, year9_2, hourFrom9_2, minuteFrom9_2, hourOn9_2, minOn9_2, hourOff9_2, minOff9_2, dark9_2, light9_2
    date9_2 = date9_2_entry.get()
    month9_2 = month9_2_entry.get()
    year9_2 = year9_2_entry.get()
    hourFrom9_2= spin9_E_2.get()
    minuteFrom9_2= spin9_F_2.get()
    hourOn9_2=spin9_A_2.get()
    minOn9_2=spin9_B_2.get()
    hourOff9_2=spin9_C_2.get()
    minOff9_2=spin9_D_2.get()                            
    if var9_2.get()==1:
        dark9_2='0'
        light9_2='0'
    if var9_2.get()==2:
        dark9_2='1'
        light9_2='0'
    if var9_2.get()==3:
        dark9_2='0'
        light9_2='1'
    global date9_3, month9_3, year9_3, hourFrom9_3, minuteFrom9_3, hourOn9_3, minOn9_3, hourOff9_3, minOff9_3, dark9_3, light9_3
    date9_3 = date9_3_entry.get()
    month9_3 = month9_3_entry.get()
    year9_3 = year9_3_entry.get()
    hourFrom9_3= spin9_E_3.get()
    minuteFrom9_3= spin9_F_3.get()
    hourOn9_3=spin9_A_3.get()
    minOn9_3=spin9_B_3.get()
    hourOff9_3=spin9_C_3.get()
    minOff9_3=spin9_D_3.get()                            
    if var9_3.get()==1:
        dark9_3='0'
        light9_3='0'
    if var9_3.get()==2:
        dark9_3='1'
        light9_3='0'
    if var9_3.get()==3:
        dark9_3='0'
        light9_3='1'
    status.pack(side='bottom', fill='x')
    status.set('Box9 schedule is set.')
    box9sched_text.set('Box9 schedule set.')
    if setBox1+setBox2+setBox3+setBox4+setBox5+setBox6+setBox7+setBox8+setBox9+setBox10 == 10:
        btnSave['state']='normal'
        btnRun['state']='normal'
        show_conf()
    window.update_idletasks()

def getBox10Schedule(): 
    global setBox10, hourOn10_1, minOn10_1, hourOff10_1, minOff10_1, dark10_1, light10_1
    hourOn10_1=spin10_A_1.get()
    minOn10_1=spin10_B_1.get()
    hourOff10_1=spin10_C_1.get()
    minOff10_1=spin10_D_1.get()                            
    if var10_1.get()==1:
        dark10_1='0'
        light10_1='0'
    if var10_1.get()==2:
        dark10_1='1'
        light10_1='0'
    if var10_1.get()==3:
        dark10_1='0'
        light10_1='1'
    global date10_2, month10_2, year10_2, hourFrom10_2, minuteFrom10_2, hourOn10_2, minOn10_2, hourOff10_2, minOff10_2, dark10_2, light10_2
    date10_2 = date10_2_entry.get()
    month10_2 = month10_2_entry.get()
    year10_2 = year10_2_entry.get()
    hourFrom10_2= spin10_E_2.get()
    minuteFrom10_2= spin10_F_2.get()
    hourOn10_2=spin10_A_2.get()
    minOn10_2=spin10_B_2.get()
    hourOff10_2=spin10_C_2.get()
    minOff10_2=spin10_D_2.get()                            
    if var10_2.get()==1:
        dark10_2='0'
        light10_2='0'
    if var10_2.get()==2:
        dark10_2='1'
        light10_2='0'
    if var10_2.get()==3:
        dark10_2='0'
        light10_2='1'
    global date10_3, month10_3, year10_3, hourFrom10_3, minuteFrom10_3, hourOn10_3, minOn10_3, hourOff10_3, minOff10_3, dark10_3, light10_3
    date10_3 = date10_3_entry.get()
    month10_3 = month10_3_entry.get()
    year10_3 = year10_3_entry.get()
    hourFrom10_3= spin10_E_3.get()
    minuteFrom10_3= spin10_F_3.get()
    hourOn10_3=spin10_A_3.get()
    minOn10_3=spin10_B_3.get()
    hourOff10_3=spin10_C_3.get()
    minOff10_3=spin10_D_3.get()                            
    if var10_3.get()==1:
        dark10_3='0'
        light10_3='0'
    if var10_3.get()==2:
        dark10_3='1'
        light10_3='0'
    if var10_3.get()==3:
        dark10_3='0'
        light10_3='1'
    status.pack(side='bottom', fill='x') # Ackowledge in the Status Bar
    status.set('Box10 schedule is set.')
    box10sched_text.set('Box10 schedule set.')
    setBox10=1
    if setBox1+setBox2+setBox3+setBox4+setBox5+setBox6+setBox7+setBox8+setBox9+setBox10 == 10:
        btnSave['state']='normal'
        btnRun['state']='normal'
        show_conf()
    window.update_idletasks()

def getAllBoxSchedule(): 
    getBox1Schedule()
    getBox2Schedule()
    getBox3Schedule()
    getBox4Schedule()
    getBox5Schedule()
    getBox6Schedule()
    getBox7Schedule()
    getBox8Schedule()
    getBox9Schedule()
    getBox10Schedule()
    status.pack(side='bottom', fill='x')
    status.set('Schedules for all boxes are set.')
    show_conf()
    btnSave['state']='normal'
    btnRun['state']='normal'
    window.update_idletasks()

if __name__ == '__main__':
    #### All of the components and their positions in the GUI ####
    # You can change the design from here #       
    menu = Menu(window) #define menu

    # Define Var to keep track of the schedule
                                    #1 for LD
                                    #2 for DD
                                    #3 for LL           
    var1_1 = IntVar(value=1) 
    var1_2 = IntVar(value=1)
    var1_3 = IntVar(value=1)
    var2_1 = IntVar(value=1) 
    var2_2 = IntVar(value=1)
    var2_3 = IntVar(value=1)
    var3_1 = IntVar(value=1) 
    var3_2 = IntVar(value=1)
    var3_3 = IntVar(value=1)
    var4_1 = IntVar(value=1) 
    var4_2 = IntVar(value=1)
    var4_3 = IntVar(value=1)
    var5_1 = IntVar(value=1) 
    var5_2 = IntVar(value=1)
    var5_3 = IntVar(value=1)
    var6_1 = IntVar(value=1) 
    var6_2 = IntVar(value=1)
    var6_3 = IntVar(value=1)
    var7_1 = IntVar(value=1) 
    var7_2 = IntVar(value=1)
    var7_3 = IntVar(value=1)
    var8_1 = IntVar(value=1) 
    var8_2 = IntVar(value=1)
    var8_3 = IntVar(value=1)
    var9_1 = IntVar(value=1) 
    var9_2 = IntVar(value=1)
    var9_3 = IntVar(value=1)
    var10_1 = IntVar(value=1) 
    var10_2 = IntVar(value=1)
    var10_3 = IntVar(value=1)

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
    recordingmenu.add_command(label='Start revised', command=lambda:get_data(1))
    recordingmenu.add_separator()
    recordingmenu.add_command(label='Stop', command=disconnect)
    menu.add_cascade(label='Recording', menu=recordingmenu)
    #create About menu
    aboutmenu = Menu(menu)
    aboutmenu.add_command(label='About LocoBox', command=about)
    menu.add_cascade(label='Help', menu=aboutmenu)
    window.config(menu=menu)

    tab_control = ttk.Notebook(window)
    tab1 = ttk.Frame(tab_control)
    tab2 = ttk.Frame(tab_control)
    tab3 = ttk.Frame(tab_control)
    tab4 = ttk.Frame(tab_control)
    tab5 = ttk.Frame(tab_control)
    tab6 = ttk.Frame(tab_control)
    tab7 = ttk.Frame(tab_control)
    tab8 = ttk.Frame(tab_control)
    tab9 = ttk.Frame(tab_control)
    tab10 = ttk.Frame(tab_control)
    tab11 = ttk.Frame(tab_control)
    tab_control.add(tab1, text='Box1')
    tab_control.add(tab2, text='Box2')
    tab_control.add(tab3, text='Box3')
    tab_control.add(tab4, text='Box4')
    tab_control.add(tab5, text='Box5')
    tab_control.add(tab6, text='Box6')
    tab_control.add(tab7, text='Box7')
    tab_control.add(tab8, text='Box8')
    tab_control.add(tab9, text='Box9')
    tab_control.add(tab10, text='Box10')
    tab_control.add(tab11, text='Schedules')

    #Display all available serial ports
    #openPorts=serial_ports()
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        print(p)
    openPorts=p.device
    if len(np.shape(openPorts)) == 0:
        openPorts=[openPorts]
    status.pack(side='bottom', fill='x')
    status.set('Available ports: '+', '.join(map(str,openPorts)))

    #Entry for Port, Baud, timeout, filename to save
    port   = Label(text = 'Port').place(x = 40, y = 320)
    baud   = Label(text =  'Baud rate').place(x = 363, y = 320)
    timeout = Label(text = 'Time out').place(x= 565, y=320)
    filename = Label(text= 'File').place(x=40, y=360)
    configfilename = Label(text= 'Schedule').place(x=363, y=360)

    port_entry = Spinbox(values=openPorts, width=25)
    port_entry.delete(0,'end')
    port_entry.insert(0,openPorts[0]) #first port is the default 
    port_entry.place(x = 80, y = 320)
    baud_entry = Spinbox(values=(300, 600, 1200, 2400, 4800, 9600, 14400, 19200, 28800, 38400, 57600, 115200), width=7)
    baud_entry.delete(0,'end')
    baud_entry.insert(0,'9600')
    baud_entry.place(x = 440, y = 320)
    timeout_entry = Entry(width = 4)
    timeout_entry.place(x=635,y=320)
    timeout_entry.insert(0,'10')
    filename_entry = Entry(width = 25)
    filename_entry.place(x=80, y=360)
    date_string = time.strftime('%Y%m%d') # predefine a default filename with ISO date    
    filename_entry.insert(0,'BOX1-'+date_string+'.txt')
    configfilename_entry = Entry(width = 25)
    configfilename_entry.place(x=440, y=360)
    configfilename_entry.insert(0,'BOX1-sched-'+date_string+'.json')

    btnSave = Button(text=' Save ', command=save_conf, state='disabled')
    btnRun = Button(text= ' Recording Start ', command=connect, state='disabled')
  
    # if box settings of all 10 boxes are done, activate save and run buttons
    if setBox1+setBox2+setBox3+setBox4+setBox5+setBox6+setBox7+setBox8+setBox9+setBox10 == 10:
        btnSave['state']='normal'
        btnRun['state']='normal'
        show_conf()
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

    # Box1
    btn1 = Button(tab1, text='  Set  ', command=lambda: OnButtonClick(1))
    btnAll1 = Button(tab1, text='Set All', command=getAllBoxSchedule)
    tab1_title = Label(tab1, text= 'LED schedule', anchor='center')
    tab1_title.grid(column=0, row= -1+row_adj, columnspan='27', sticky='we')
    capSep1 = ttk.Separator(tab1, orient=HORIZONTAL)
    capSep1.grid(column=0, row = row_adj+5, columnspan='27', sticky='we')
    box1sched_text=StringVar()
    box1sched_text.set('Schedule not set.')
    box1sched_stat=Label(tab1, textvariable=box1sched_text, anchor=W, justify=LEFT)
        # phase 1
    phaseLabel1_1 = Label(tab1, text='Phase 1')
    dateLabel = time.strftime('%H:%M   %Y/%m/%d') # reads time for Phase 1 start-time
    fromLabel1_1 = Label(tab1, text='From:')
    date_label1 = Label(tab1, text=dateLabel+' (HH:MN YYYY/MO/DD)')
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
    date1_2_entry = Spinbox(tab1, from_=00, to=31, width=3, format='%02.0f')
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
    phaseLabel1_2.grid(column=0, row=2+row_adj, padx=15, pady=5)
    fromLabel1_2.grid(column=1,row=2+row_adj)
    spin1_E_2.grid(column=2,row=2+row_adj)
    label1_h0_2.grid(column=3,row=2+row_adj)
    spin1_F_2.grid(column=4,row=2+row_adj)
    label1_m0_2.grid(column=5,row=2+row_adj)
    space1_2.grid(column=6,row=2+row_adj)
    year1_2_entry.grid(column=7, row=2+row_adj)
    label1_m_2.grid(column=8,row=2+row_adj)
    month1_2_entry.grid(column=9, row=2+row_adj)
    label1_d_2.grid(column=10,row=2+row_adj)
    date1_2_entry.grid(column=11, row=2+row_adj) # ISO format
    space1_2_2.grid(column=12,row=2+row_adj,padx=5)
    rad1_A_2.grid(column=13, row=2+row_adj, pady=5)
    lbl1_A_2.grid(column=14, row=2+row_adj, pady=5)
    spin1_A_2.grid(column=15,row=2+row_adj, pady=5)
    label1_h1_2.grid(column=16,row=2+row_adj, pady=5)
    spin1_B_2.grid(column=17,row=2+row_adj, pady=5)
    label1_m1_2.grid(column=18,row=2+row_adj, pady=5)
    lbl1_B_2.grid(column=19, row=2+row_adj, pady=5)
    spin1_C_2.grid(column=20,row=2+row_adj, pady=5)
    label1_h2_2.grid(column=21,row=2+row_adj, pady=5)
    spin1_D_2.grid(column=22,row=2+row_adj, pady=5)
    label1_m2_2.grid(column=23,row=2+row_adj, pady=5)
    rad1_B_2.grid(column=24, row=2+row_adj, padx=15, pady=5)
    rad1_C_2.grid(column=25, row=2+row_adj, pady=5)
        # phase 3
    phaseLabel1_3 = Label(tab1, text='Phase 3')
    fromLabel1_3 = Label(tab1, text='From:')
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
    day_phase3 = day_phase2 + datetime.timedelta(days=21) # calculate dates for 21 days after recording initiation
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
    phaseLabel1_3.grid(column=0, row=3+row_adj, padx=15, pady=5)
    fromLabel1_3.grid(column=1,row=3+row_adj)
    spin1_E_3.grid(column=2,row=3+row_adj)
    label1_h0_3.grid(column=3,row=3+row_adj)
    spin1_F_3.grid(column=4,row=3+row_adj)
    label1_m0_3.grid(column=5,row=3+row_adj)
    space1_3.grid(column=6,row=3+row_adj)
    date1_3_entry.grid(column=11, row=3+row_adj)
    label1_d_3.grid(column=8,row=3+row_adj)
    month1_3_entry.grid(column=9, row=3+row_adj)
    label1_m_3.grid(column=10,row=3+row_adj)
    year1_3_entry.grid(column=7, row=3+row_adj) # ISO format
    space1_3_2.grid(column=12,row=3+row_adj,padx=5)
    rad1_A_3.grid(column=13, row=3+row_adj, pady=5)
    lbl1_A_3.grid(column=14, row=3+row_adj, pady=5)
    spin1_A_3.grid(column=15,row=3+row_adj, pady=5)
    label1_h1_3.grid(column=16,row=3+row_adj, pady=5)
    spin1_B_3.grid(column=17,row=3+row_adj, pady=5)
    label1_m1_3.grid(column=18,row=3+row_adj, pady=5)
    lbl1_B_3.grid(column=19, row=3+row_adj, pady=5)
    spin1_C_3.grid(column=20,row=3+row_adj, pady=5)
    label1_h2_3.grid(column=21,row=3+row_adj, pady=5)
    spin1_D_3.grid(column=22,row=3+row_adj, pady=5)
    label1_m2_3.grid(column=23,row=3+row_adj, pady=5)
    rad1_B_3.grid(column=24, row=3+row_adj, padx=15, pady=5)
    rad1_C_3.grid(column=25, row=3+row_adj, pady=5)
    btn1.grid(column=0, row=4+row_adj, padx=25, pady=5, columnspan='2', sticky='w')
    btnAll1.grid(column=1, row=4+row_adj, pady=5, columnspan='1', sticky='w')
    box1sched_stat.grid(column=3, row=4+row_adj, columnspan='8', sticky='w')
    window.update_idletasks()
    tab1_title2 = Label(tab1, text= 'Recording status', anchor='center')
    tab1_title2.grid(column=0, row= row_adj+6, columnspan='27', sticky='we')
    box1rec_text=StringVar()
    box1rec_text.set('Recording not started yet.')
    box1rec_stat=Label(tab1, textvariable=box1rec_text, anchor='center', justify=LEFT)
    box1rec_stat.grid(column=0, row= row_adj+7, columnspan='27', sticky='we')
    window.update_idletasks()

    # Box2
    btn2 = Button(tab2, text='  Set  ', command=lambda: OnButtonClick(2))
    btnAll2 = Button(tab2, text='Set All', command=getAllBoxSchedule)
    tab2_title = Label(tab2, text= 'LED schedule', anchor='center')
    tab2_title.grid(column=0, row= -1+row_adj, columnspan='27', sticky='we')
    capSep2 = ttk.Separator(tab2, orient=HORIZONTAL)
    capSep2.grid(column=0, row = row_adj+5, columnspan='27', sticky='we')
    box2sched_text=StringVar()
    box2sched_text.set('Schedule not set.')
    box2sched_stat=Label(tab2, textvariable=box2sched_text, anchor=W, justify=LEFT)
        # phase 1
    phaseLabel2_1 = Label(tab2, text='Phase 1')
    dateLabel = time.strftime('%H:%M   %Y/%m/%d') # reads time for Phase 1 start-time
    fromLabel2_1 = Label(tab2, text='From:')
    date_label2 = Label(tab2, text=dateLabel+' (HH:MN YYYY/MO/DD)')
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
    phaseLabel2_2.grid(column=0, row=2+row_adj, padx=15, pady=5)
    fromLabel2_2.grid(column=1,row=2+row_adj)
    spin2_E_2.grid(column=2,row=2+row_adj)
    label2_h0_2.grid(column=3,row=2+row_adj)
    spin2_F_2.grid(column=4,row=2+row_adj)
    label2_m0_2.grid(column=5,row=2+row_adj)
    space2_2.grid(column=6,row=2+row_adj)
    date2_2_entry.grid(column=11, row=2+row_adj)
    label2_d_2.grid(column=8,row=2+row_adj)
    month2_2_entry.grid(column=9, row=2+row_adj)
    label2_m_2.grid(column=10,row=2+row_adj)
    year2_2_entry.grid(column=7, row=2+row_adj) # ISO format
    space2_2_2.grid(column=12,row=2+row_adj,padx=5)
    rad2_A_2.grid(column=13, row=2+row_adj, pady=5)
    lbl2_A_2.grid(column=14, row=2+row_adj, pady=5)
    spin2_A_2.grid(column=15,row=2+row_adj, pady=5)
    label2_h1_2.grid(column=16,row=2+row_adj, pady=5)
    spin2_B_2.grid(column=17,row=2+row_adj, pady=5)
    label2_m1_2.grid(column=18,row=2+row_adj, pady=5)
    lbl2_B_2.grid(column=19, row=2+row_adj, pady=5)
    spin2_C_2.grid(column=20,row=2+row_adj, pady=5)
    label2_h2_2.grid(column=21,row=2+row_adj, pady=5)
    spin2_D_2.grid(column=22,row=2+row_adj, pady=5)
    label2_m2_2.grid(column=23,row=2+row_adj, pady=5)
    rad2_B_2.grid(column=24, row=2+row_adj, padx=15, pady=5)
    rad2_C_2.grid(column=25, row=2+row_adj, pady=5)
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
    day_phase3 = day_phase2 + datetime.timedelta(days=21) # calculate dates for 21 days after recording initiation
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
    phaseLabel2_3.grid(column=0, row=3+row_adj, padx=15, pady=5)
    fromLabel2_3.grid(column=1,row=3+row_adj)
    spin2_E_3.grid(column=2,row=3+row_adj)
    label2_h0_3.grid(column=3,row=3+row_adj)
    spin2_F_3.grid(column=4,row=3+row_adj)
    label2_m0_3.grid(column=5,row=3+row_adj)
    space2_3.grid(column=6,row=3+row_adj)
    date2_3_entry.grid(column=11, row=3+row_adj)
    label2_d_3.grid(column=8,row=3+row_adj)
    month2_3_entry.grid(column=9, row=3+row_adj)
    label2_m_3.grid(column=10,row=3+row_adj)
    year2_3_entry.grid(column=7, row=3+row_adj) # ISO format
    rad2_A_3.grid(column=13, row=3+row_adj, pady=5)
    lbl2_A_3.grid(column=14, row=3+row_adj, pady=5)
    spin2_A_3.grid(column=15,row=3+row_adj, pady=5)
    label2_h1_3.grid(column=16,row=3+row_adj, pady=5)
    spin2_B_3.grid(column=17,row=3+row_adj, pady=5)
    label2_m1_3.grid(column=18,row=3+row_adj, pady=5)
    lbl2_B_3.grid(column=19, row=3+row_adj, pady=5)
    spin2_C_3.grid(column=20,row=3+row_adj, pady=5)
    label2_h2_3.grid(column=21,row=3+row_adj, pady=5)
    spin2_D_3.grid(column=22,row=3+row_adj, pady=5)
    label2_m2_3.grid(column=23,row=3+row_adj, pady=5)
    rad2_B_3.grid(column=24, row=3+row_adj, padx=15, pady=5)
    rad2_C_3.grid(column=25, row=3+row_adj, pady=5)
    btn2.grid(column=0, row=4+row_adj, padx=25, pady=5, columnspan='2', sticky='w')
    btnAll2.grid(column=1, row=4+row_adj, pady=5, columnspan='1', sticky='w')
    box2sched_stat.grid(column=3, row=4+row_adj, columnspan='8', sticky='w')
    window.update_idletasks()
    tab2_title2 = Label(tab2, text= 'Recording status', anchor='center')
    tab2_title2.grid(column=0, row= row_adj+6, columnspan='27', sticky='we')
    box2rec_text=StringVar()
    box2rec_text.set('Recording not started yet.')
    box2rec_stat=Label(tab2, textvariable=box2rec_text, anchor='center', justify=LEFT)
    box2rec_stat.grid(column=0, row= row_adj+7, columnspan='27', sticky='we')
    window.update_idletasks()

    # Box3
    btn3 = Button(tab3, text='  Set  ', command=lambda: OnButtonClick(3))
    btnAll3 = Button(tab3, text='Set All', command=getAllBoxSchedule)
    tab3_title = Label(tab3, text= 'LED schedule', anchor='center')
    tab3_title.grid(column=0, row= -1+row_adj, columnspan='27', sticky='we')
    capSep3 = ttk.Separator(tab3, orient=HORIZONTAL)
    capSep3.grid(column=0, row = row_adj+5, columnspan='27', sticky='we')
    box3sched_text=StringVar()
    box3sched_text.set('Schedule not set.')
    box3sched_stat=Label(tab3, textvariable=box3sched_text, anchor=W, justify=LEFT)
        # phase 1
    phaseLabel3_1 = Label(tab3, text='Phase 1')
    dateLabel = time.strftime('%H:%M   %Y/%m/%d') # reads time for Phase 1 start-time
    fromLabel3_1 = Label(tab3, text='From:')
    date_label3 = Label(tab3, text=dateLabel+' (HH:MN YYYY/MO/DD)')
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
    phaseLabel3_2.grid(column=0, row=2+row_adj, padx=15, pady=5)
    fromLabel3_2.grid(column=1,row=2+row_adj)
    spin3_E_2.grid(column=2,row=2+row_adj)
    label3_h0_2.grid(column=3,row=2+row_adj)
    spin3_F_2.grid(column=4,row=2+row_adj)
    label3_m0_2.grid(column=5,row=2+row_adj)
    space3_2.grid(column=6,row=2+row_adj)
    date3_2_entry.grid(column=11, row=2+row_adj)
    label3_d_2.grid(column=8,row=2+row_adj)
    month3_2_entry.grid(column=9, row=2+row_adj)
    label3_m_2.grid(column=10,row=2+row_adj)
    year3_2_entry.grid(column=7, row=2+row_adj) # ISO format
    space3_2_2.grid(column=12,row=2+row_adj,padx=5)
    rad3_A_2.grid(column=13, row=2+row_adj, pady=5)
    lbl3_A_2.grid(column=14, row=2+row_adj, pady=5)
    spin3_A_2.grid(column=15,row=2+row_adj, pady=5)
    label3_h1_2.grid(column=16,row=2+row_adj, pady=5)
    spin3_B_2.grid(column=17,row=2+row_adj, pady=5)
    label3_m1_2.grid(column=18,row=2+row_adj, pady=5)
    lbl3_B_2.grid(column=19, row=2+row_adj, pady=5)
    spin3_C_2.grid(column=20,row=2+row_adj, pady=5)
    label3_h2_2.grid(column=21,row=2+row_adj, pady=5)
    spin3_D_2.grid(column=22,row=2+row_adj, pady=5)
    label3_m2_2.grid(column=23,row=2+row_adj, pady=5)
    rad3_B_2.grid(column=24, row=2+row_adj, padx=15, pady=5)
    rad3_C_2.grid(column=25, row=2+row_adj, pady=5)
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
    day_phase3 = day_phase2 + datetime.timedelta(days=21) # calculate dates for 21 days after recording initiation
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
    phaseLabel3_3.grid(column=0, row=3+row_adj, padx=15, pady=5)
    fromLabel3_3.grid(column=1,row=3+row_adj)
    spin3_E_3.grid(column=2,row=3+row_adj)
    label3_h0_3.grid(column=3,row=3+row_adj)
    spin3_F_3.grid(column=4,row=3+row_adj)
    label3_m0_3.grid(column=5,row=3+row_adj)
    space3_3.grid(column=6,row=3+row_adj)
    date3_3_entry.grid(column=11, row=3+row_adj)
    label3_d_3.grid(column=8,row=3+row_adj)
    month3_3_entry.grid(column=9, row=3+row_adj)
    label3_m_3.grid(column=10,row=3+row_adj)
    year3_3_entry.grid(column=7, row=3+row_adj) # ISO format
    rad3_A_3.grid(column=13, row=3+row_adj, pady=5)
    lbl3_A_3.grid(column=14, row=3+row_adj, pady=5)
    spin3_A_3.grid(column=15,row=3+row_adj, pady=5)
    label3_h1_3.grid(column=16,row=3+row_adj, pady=5)
    spin3_B_3.grid(column=17,row=3+row_adj, pady=5)
    label3_m1_3.grid(column=18,row=3+row_adj, pady=5)
    lbl3_B_3.grid(column=19, row=3+row_adj, pady=5)
    spin3_C_3.grid(column=20,row=3+row_adj, pady=5)
    label3_h2_3.grid(column=21,row=3+row_adj, pady=5)
    spin3_D_3.grid(column=22,row=3+row_adj, pady=5)
    label3_m2_3.grid(column=23,row=3+row_adj, pady=5)
    rad3_B_3.grid(column=24, row=3+row_adj, padx=15, pady=5)
    rad3_C_3.grid(column=25, row=3+row_adj, pady=5)
    btn3.grid(column=0, row=4+row_adj, padx=25, pady=5, columnspan='2', sticky='w')
    btnAll3.grid(column=1, row=4+row_adj, pady=5, columnspan='1', sticky='w')
    box3sched_stat.grid(column=3, row=4+row_adj, columnspan='8', sticky='w')
    window.update_idletasks()
    tab3_title2 = Label(tab3, text= 'Recording status', anchor='center')
    tab3_title2.grid(column=0, row= row_adj+6, columnspan='27', sticky='we')
    box3rec_text=StringVar()
    box3rec_text.set('Recording not started yet.')
    box3rec_stat=Label(tab3, textvariable=box3rec_text, anchor='center', justify=LEFT)
    box3rec_stat.grid(column=0, row= row_adj+7, columnspan='27', sticky='we')
    window.update_idletasks()
    
    # Box4
    btn4 = Button(tab4, text='  Set  ', command=lambda: OnButtonClick(4))
    btnAll4 = Button(tab4, text='Set All', command=getAllBoxSchedule)
    tab4_title = Label(tab4, text= 'LED schedule', anchor='center')
    tab4_title.grid(column=0, row= -1+row_adj, columnspan='27', sticky='we')
    capSep4 = ttk.Separator(tab4, orient=HORIZONTAL)
    capSep4.grid(column=0, row = row_adj+5, columnspan='27', sticky='we')
    box4sched_text=StringVar()
    box4sched_text.set('Schedule not set.')
    box4sched_stat=Label(tab4, textvariable=box4sched_text, anchor=W, justify=LEFT)
        # phase 1
    phaseLabel4_1 = Label(tab4, text='Phase 1')
    dateLabel = time.strftime('%H:%M   %Y/%m/%d') # reads time for Phase 1 start-time
    fromLabel4_1 = Label(tab4, text='From:')
    date_label4 = Label(tab4, text=dateLabel+' (HH:MN YYYY/MO/DD)')
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
    phaseLabel4_2.grid(column=0, row=2+row_adj, padx=15, pady=5)
    fromLabel4_2.grid(column=1,row=2+row_adj)
    spin4_E_2.grid(column=2,row=2+row_adj)
    label4_h0_2.grid(column=3,row=2+row_adj)
    spin4_F_2.grid(column=4,row=2+row_adj)
    label4_m0_2.grid(column=5,row=2+row_adj)
    space4_2.grid(column=6,row=2+row_adj)
    date4_2_entry.grid(column=11, row=2+row_adj)
    label4_d_2.grid(column=8,row=2+row_adj)
    month4_2_entry.grid(column=9, row=2+row_adj)
    label4_m_2.grid(column=10,row=2+row_adj)
    year4_2_entry.grid(column=7, row=2+row_adj) # ISO format
    space4_2_2.grid(column=12,row=2+row_adj,padx=5)
    rad4_A_2.grid(column=13, row=2+row_adj, pady=5)
    lbl4_A_2.grid(column=14, row=2+row_adj, pady=5)
    spin4_A_2.grid(column=15,row=2+row_adj, pady=5)
    label4_h1_2.grid(column=16,row=2+row_adj, pady=5)
    spin4_B_2.grid(column=17,row=2+row_adj, pady=5)
    label4_m1_2.grid(column=18,row=2+row_adj, pady=5)
    lbl4_B_2.grid(column=19, row=2+row_adj, pady=5)
    spin4_C_2.grid(column=20,row=2+row_adj, pady=5)
    label4_h2_2.grid(column=21,row=2+row_adj, pady=5)
    spin4_D_2.grid(column=22,row=2+row_adj, pady=5)
    label4_m2_2.grid(column=23,row=2+row_adj, pady=5)
    rad4_B_2.grid(column=24, row=2+row_adj, padx=15, pady=5)
    rad4_C_2.grid(column=25, row=2+row_adj, pady=5)
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
    day_phase3 = day_phase2 + datetime.timedelta(days=21) # calculate dates for 21 days after recording initiation
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
    phaseLabel4_3.grid(column=0, row=3+row_adj, padx=15, pady=5)
    fromLabel4_3.grid(column=1,row=3+row_adj)
    spin4_E_3.grid(column=2,row=3+row_adj)
    label4_h0_3.grid(column=3,row=3+row_adj)
    spin4_F_3.grid(column=4,row=3+row_adj)
    label4_m0_3.grid(column=5,row=3+row_adj)
    space4_3.grid(column=6,row=3+row_adj)
    date4_3_entry.grid(column=11, row=3+row_adj)
    label4_d_3.grid(column=8,row=3+row_adj)
    month4_3_entry.grid(column=9, row=3+row_adj)
    label4_m_3.grid(column=10,row=3+row_adj)
    year4_3_entry.grid(column=7, row=3+row_adj)
    rad4_A_3.grid(column=13, row=3+row_adj, pady=5)
    lbl4_A_3.grid(column=14, row=3+row_adj, pady=5)
    spin4_A_3.grid(column=15,row=3+row_adj, pady=5)
    label4_h1_3.grid(column=16,row=3+row_adj, pady=5)
    spin4_B_3.grid(column=17,row=3+row_adj, pady=5)
    label4_m1_3.grid(column=18,row=3+row_adj, pady=5)
    lbl4_B_3.grid(column=19, row=3+row_adj, pady=5)
    spin4_C_3.grid(column=20,row=3+row_adj, pady=5)
    label4_h2_3.grid(column=21,row=3+row_adj, pady=5)
    spin4_D_3.grid(column=22,row=3+row_adj, pady=5)
    label4_m2_3.grid(column=23,row=3+row_adj, pady=5)
    rad4_B_3.grid(column=24, row=3+row_adj, padx=15, pady=5)
    rad4_C_3.grid(column=25, row=3+row_adj, pady=5)
    btn4.grid(column=0, row=4+row_adj, padx=25, pady=5, columnspan='2', sticky='w')
    btnAll4.grid(column=1, row=4+row_adj, pady=5, columnspan='1', sticky='w')
    box4sched_stat.grid(column=3, row=4+row_adj, columnspan='8', sticky='w')
    window.update_idletasks()
    tab4_title2 = Label(tab4, text= 'Recording status', anchor='center')
    tab4_title2.grid(column=0, row= row_adj+6, columnspan='27', sticky='we')
    box4rec_text=StringVar()
    box4rec_text.set('Recording not started yet.')
    box4rec_stat=Label(tab4, textvariable=box4rec_text, anchor='center', justify=LEFT)
    box4rec_stat.grid(column=0, row= row_adj+7, columnspan='27', sticky='we')
    window.update_idletasks()

    # Box5
    btn5 = Button(tab5, text='  Set  ', command=lambda: OnButtonClick(5))
    btnAll5 = Button(tab5, text='Set All', command=getAllBoxSchedule)
    tab5_title = Label(tab5, text= 'LED schedule', anchor='center')
    tab5_title.grid(column=0, row= -1+row_adj, columnspan='27', sticky='we')
    capSep5 = ttk.Separator(tab5, orient=HORIZONTAL)
    capSep5.grid(column=0, row = row_adj+5, columnspan='27', sticky='we')
    box5sched_text=StringVar()
    box5sched_text.set('Schedule not set.')
    box5sched_stat=Label(tab5, textvariable=box5sched_text, anchor=W, justify=LEFT)
        # phase 1
    phaseLabel5_1 = Label(tab5, text='Phase 1')
    dateLabel = time.strftime('%H:%M   %Y/%m/%d') # reads time for Phase 1 start-time
    fromLabel5_1 = Label(tab5, text='From:')
    date_label5 = Label(tab5, text=dateLabel+' (HH:MN YYYY/MO/DD)')
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
    phaseLabel5_2.grid(column=0, row=2+row_adj, padx=15, pady=5)
    fromLabel5_2.grid(column=1,row=2+row_adj)
    spin5_E_2.grid(column=2,row=2+row_adj)
    label5_h0_2.grid(column=3,row=2+row_adj)
    spin5_F_2.grid(column=4,row=2+row_adj)
    label5_m0_2.grid(column=5,row=2+row_adj)
    space5_2.grid(column=6,row=2+row_adj)
    date5_2_entry.grid(column=11, row=2+row_adj)
    label5_d_2.grid(column=8,row=2+row_adj)
    month5_2_entry.grid(column=9, row=2+row_adj)
    label5_m_2.grid(column=10,row=2+row_adj)
    year5_2_entry.grid(column=7, row=2+row_adj) # ISO format
    space5_2_2.grid(column=12,row=2+row_adj,padx=5)
    rad5_A_2.grid(column=13, row=2+row_adj, pady=5)
    lbl5_A_2.grid(column=14, row=2+row_adj, pady=5)
    spin5_A_2.grid(column=15,row=2+row_adj, pady=5)
    label5_h1_2.grid(column=16,row=2+row_adj, pady=5)
    spin5_B_2.grid(column=17,row=2+row_adj, pady=5)
    label5_m1_2.grid(column=18,row=2+row_adj, pady=5)
    lbl5_B_2.grid(column=19, row=2+row_adj, pady=5)
    spin5_C_2.grid(column=20,row=2+row_adj, pady=5)
    label5_h2_2.grid(column=21,row=2+row_adj, pady=5)
    spin5_D_2.grid(column=22,row=2+row_adj, pady=5)
    label5_m2_2.grid(column=23,row=2+row_adj, pady=5)
    rad5_B_2.grid(column=24, row=2+row_adj, padx=15, pady=5)
    rad5_C_2.grid(column=25, row=2+row_adj, pady=5)
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
    day_phase3 = day_phase2 + datetime.timedelta(days=21) # calculate dates for 21 days after recording initiation
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
    phaseLabel5_3.grid(column=0, row=3+row_adj, padx=15, pady=5)
    fromLabel5_3.grid(column=1,row=3+row_adj)
    spin5_E_3.grid(column=2,row=3+row_adj)
    label5_h0_3.grid(column=3,row=3+row_adj)
    spin5_F_3.grid(column=4,row=3+row_adj)
    label5_m0_3.grid(column=5,row=3+row_adj)
    space5_3.grid(column=6,row=3+row_adj)
    date5_3_entry.grid(column=11, row=3+row_adj)
    label5_d_3.grid(column=8,row=3+row_adj)
    month5_3_entry.grid(column=9, row=3+row_adj)
    label5_m_3.grid(column=10,row=3+row_adj)
    year5_3_entry.grid(column=7, row=3+row_adj) # ISO format
    rad5_A_3.grid(column=13, row=3+row_adj, pady=5)
    lbl5_A_3.grid(column=14, row=3+row_adj, pady=5)
    spin5_A_3.grid(column=15,row=3+row_adj, pady=5)
    label5_h1_3.grid(column=16,row=3+row_adj, pady=5)
    spin5_B_3.grid(column=17,row=3+row_adj, pady=5)
    label5_m1_3.grid(column=18,row=3+row_adj, pady=5)
    lbl5_B_3.grid(column=19, row=3+row_adj, pady=5)
    spin5_C_3.grid(column=20,row=3+row_adj, pady=5)
    label5_h2_3.grid(column=21,row=3+row_adj, pady=5)
    spin5_D_3.grid(column=22,row=3+row_adj, pady=5)
    label5_m2_3.grid(column=23,row=3+row_adj, pady=5)
    rad5_B_3.grid(column=24, row=3+row_adj, padx=15, pady=5)
    rad5_C_3.grid(column=25, row=3+row_adj, pady=5)
    btn5.grid(column=0, row=4+row_adj, padx=25, pady=5, columnspan='2', sticky='w')
    btnAll5.grid(column=1, row=4+row_adj, pady=5, columnspan='1', sticky='w')
    box5sched_stat.grid(column=3, row=4+row_adj, columnspan='8', sticky='w')
    window.update_idletasks()
    tab5_title2 = Label(tab5, text= 'Recording status', anchor='center')
    tab5_title2.grid(column=0, row= row_adj+6, columnspan='27', sticky='we')
    box5rec_text=StringVar()
    box5rec_text.set('Recording not started yet.')
    box5rec_stat=Label(tab5, textvariable=box5rec_text, anchor='center', justify=LEFT)
    box5rec_stat.grid(column=0, row= row_adj+7, columnspan='27', sticky='we')
    window.update_idletasks()

    # Box6
    btn6 = Button(tab6, text='  Set  ', command=lambda: OnButtonClick(6))
    btnAll6 = Button(tab6, text='Set All', command=getAllBoxSchedule)
    tab6_title = Label(tab6, text= 'LED schedule', anchor='center')
    tab6_title.grid(column=0, row= -1+row_adj, columnspan='27', sticky='we')
    capSep6 = ttk.Separator(tab6, orient=HORIZONTAL)
    capSep6.grid(column=0, row = row_adj+5, columnspan='27', sticky='we')
    box6sched_text=StringVar()
    box6sched_text.set('Schedule not set.')
    box6sched_stat=Label(tab6, textvariable=box6sched_text, anchor=W, justify=LEFT)
        # phase 1
    phaseLabel6_1 = Label(tab6, text='Phase 1')
    dateLabel = time.strftime('%H:%M   %Y/%m/%d') # reads time for Phase 1 start-time
    fromLabel6_1 = Label(tab6, text='From:')
    date_label6 = Label(tab6, text=dateLabel+' (HH:MN YYYY/MO/DD)')
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
    phaseLabel6_2.grid(column=0, row=2+row_adj, padx=15, pady=5)
    fromLabel6_2.grid(column=1,row=2+row_adj)
    spin6_E_2.grid(column=2,row=2+row_adj)
    label6_h0_2.grid(column=3,row=2+row_adj)
    spin6_F_2.grid(column=4,row=2+row_adj)
    label6_m0_2.grid(column=5,row=2+row_adj)
    space6_2.grid(column=6,row=2+row_adj)
    date6_2_entry.grid(column=11, row=2+row_adj)
    label6_d_2.grid(column=8,row=2+row_adj)
    month6_2_entry.grid(column=9, row=2+row_adj)
    label6_m_2.grid(column=10,row=2+row_adj)
    year6_2_entry.grid(column=7, row=2+row_adj) # ISO format
    space6_2_2.grid(column=12,row=2+row_adj,padx=5)
    rad6_A_2.grid(column=13, row=2+row_adj, pady=5)
    lbl6_A_2.grid(column=14, row=2+row_adj, pady=5)
    spin6_A_2.grid(column=15,row=2+row_adj, pady=5)
    label6_h1_2.grid(column=16,row=2+row_adj, pady=5)
    spin6_B_2.grid(column=17,row=2+row_adj, pady=5)
    label6_m1_2.grid(column=18,row=2+row_adj, pady=5)
    lbl6_B_2.grid(column=19, row=2+row_adj, pady=5)
    spin6_C_2.grid(column=20,row=2+row_adj, pady=5)
    label6_h2_2.grid(column=21,row=2+row_adj, pady=5)
    spin6_D_2.grid(column=22,row=2+row_adj, pady=5)
    label6_m2_2.grid(column=23,row=2+row_adj, pady=5)
    rad6_B_2.grid(column=24, row=2+row_adj, padx=15, pady=5)
    rad6_C_2.grid(column=25, row=2+row_adj, pady=5)
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
    day_phase3 = day_phase2 + datetime.timedelta(days=21) # calculate dates for 21 days after recording initiation
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
    phaseLabel6_3.grid(column=0, row=3+row_adj, padx=15, pady=5)
    fromLabel6_3.grid(column=1,row=3+row_adj)
    spin6_E_3.grid(column=2,row=3+row_adj)
    label6_h0_3.grid(column=3,row=3+row_adj)
    spin6_F_3.grid(column=4,row=3+row_adj)
    label6_m0_3.grid(column=5,row=3+row_adj)
    space6_3.grid(column=6,row=3+row_adj)
    date6_3_entry.grid(column=11, row=3+row_adj)
    label6_d_3.grid(column=8,row=3+row_adj)
    month6_3_entry.grid(column=9, row=3+row_adj)
    label6_m_3.grid(column=10,row=3+row_adj)
    year6_3_entry.grid(column=7, row=3+row_adj) # ISO format
    rad6_A_3.grid(column=13, row=3+row_adj, pady=5)
    lbl6_A_3.grid(column=14, row=3+row_adj, pady=5)
    spin6_A_3.grid(column=15,row=3+row_adj, pady=5)
    label6_h1_3.grid(column=16,row=3+row_adj, pady=5)
    spin6_B_3.grid(column=17,row=3+row_adj, pady=5)
    label6_m1_3.grid(column=18,row=3+row_adj, pady=5)
    lbl6_B_3.grid(column=19, row=3+row_adj, pady=5)
    spin6_C_3.grid(column=20,row=3+row_adj, pady=5)
    label6_h2_3.grid(column=21,row=3+row_adj, pady=5)
    spin6_D_3.grid(column=22,row=3+row_adj, pady=5)
    label6_m2_3.grid(column=23,row=3+row_adj, pady=5)
    rad6_B_3.grid(column=24, row=3+row_adj, padx=15, pady=5)
    rad6_C_3.grid(column=25, row=3+row_adj, pady=5)
    btn6.grid(column=0, row=4+row_adj, padx=25, pady=5, columnspan='2', sticky='w')
    btnAll6.grid(column=1, row=4+row_adj, pady=5, columnspan='1', sticky='w')
    box6sched_stat.grid(column=3, row=4+row_adj, columnspan='8', sticky='w')
    window.update_idletasks()
    tab6_title2 = Label(tab6, text= 'Recording status', anchor='center')
    tab6_title2.grid(column=0, row= row_adj+6, columnspan='27', sticky='we')
    box6rec_text=StringVar()
    box6rec_text.set('Recording not started yet.')
    box6rec_stat=Label(tab6, textvariable=box6rec_text, anchor='center', justify=LEFT)
    box6rec_stat.grid(column=0, row= row_adj+7, columnspan='27', sticky='we')
    window.update_idletasks()

    # Box7
    btn7 = Button(tab7, text='  Set  ', command=lambda: OnButtonClick(7))
    btnAll7 = Button(tab7, text='Set All', command=getAllBoxSchedule)
    tab7_title = Label(tab7, text= 'LED schedule', anchor='center')
    tab7_title.grid(column=0, row= -1+row_adj, columnspan='27', sticky='we')
    capSep7 = ttk.Separator(tab7, orient=HORIZONTAL)
    capSep7.grid(column=0, row = row_adj+5, columnspan='27', sticky='we')
    box7sched_text=StringVar()
    box7sched_text.set('Schedule not set.')
    box7sched_stat=Label(tab7, textvariable=box7sched_text, anchor=W, justify=LEFT)
        # phase 1
    phaseLabel7_1 = Label(tab7, text='Phase 1')
    dateLabel = time.strftime('%H:%M   %Y/%m/%d') # reads time for Phase 1 start-time
    fromLabel7_1 = Label(tab7, text='From:')
    date_label7 = Label(tab7, text=dateLabel+' (HH:MN YYYY/MO/DD)')
    rad7_A_1 = Radiobutton(tab7, text='LD', variable=var7_1, value=1)
    lbl7_A_1 = Label(tab7, text= 'On:')
    spin7_A_1 = Spinbox(tab7, from_=00, to=24, width=3, format='%02.0f')
    spin7_B_1 = Spinbox(tab7, from_=00, to=59, width=3, format='%02.0f')
    spin7_A_1.delete(0,'end')
    spin7_A_1.insert(0,'07')
    spin7_B_1.delete(0,'end')
    spin7_B_1.insert(0,'00')
    label7_h1_1 = Label(tab7, text=':')
    label7_m1_1 = Label(tab7, text='')
    lbl7_B_1 = Label(tab7, text= 'Off:')
    spin7_C_1 = Spinbox(tab7, from_=00, to=24, width=3, format='%02.0f')
    spin7_D_1 = Spinbox(tab7, from_=00, to=59, width=3, format='%02.0f')
    spin7_C_1.delete(0,'end')
    spin7_C_1.insert(0,'19')
    spin7_D_1.delete(0,'end')
    spin7_D_1.insert(0,'00')
    label7_h2_1 = Label(tab7, text=':')
    label7_m2_1 = Label(tab7, text='')
    rad7_B_1 = Radiobutton(tab7, text='DD', variable=var7_1, value=2)
    rad7_C_1 = Radiobutton(tab7, text='LL', variable=var7_1, value=3)
    phaseLabel7_1.grid(column=0, row=1+row_adj, padx=15, pady=5)
    fromLabel7_1.grid(column=1,row=1+row_adj)
    date_label7.grid(column=2, row=1+row_adj, columnspan='10', sticky='w')
    rad7_A_1.grid(column=13, row=1+row_adj, pady=5)
    lbl7_A_1.grid(column=14, row=1+row_adj, pady=5)
    spin7_A_1.grid(column=15,row=1+row_adj, pady=5)
    label7_h1_1.grid(column=16,row=1+row_adj, pady=5, sticky='w')
    spin7_B_1.grid(column=17,row=1+row_adj, pady=5)
    label7_m1_1.grid(column=18,row=1+row_adj, pady=5, sticky='w')
    lbl7_B_1.grid(column=19, row=1+row_adj, pady=5)
    spin7_C_1.grid(column=20,row=1+row_adj, pady=5)
    label7_h2_1.grid(column=21,row=1+row_adj, pady=5, sticky='w')
    spin7_D_1.grid(column=22,row=1+row_adj, pady=5)
    label7_m2_1.grid(column=23,row=1+row_adj, pady=5, sticky='w')
    rad7_B_1.grid(column=24, row=1+row_adj, padx=15, pady=5)
    rad7_C_1.grid(column=25, row=1+row_adj, pady=5)
        # phase 2
    phaseLabel7_2 = Label(tab7, text='Phase 2')
    fromLabel7_2 = Label(tab7, text='From:')
    space7_2 = Label(tab7, text=' ')
    space7_2_2 = Label(tab7, text=' ')
    spin7_E_2 = Spinbox(tab7, from_=00, to=24, width=3, format='%02.0f')
    spin7_F_2 = Spinbox(tab7, from_=00, to=59, width=3, format='%02.0f')
    spin7_E_2.delete(0,'end')
    spin7_E_2.insert(0,'07')
    spin7_F_2.delete(0,'end')
    spin7_F_2.insert(0,'00')
    label7_h0_2 = Label(tab7, text=':')
    label7_m0_2 = Label(tab7, text='')
    date7_2_entry = Spinbox(tab7, from_=00, to=31, width=3, format='%02.0f')
    month7_2_entry = Spinbox(tab7, from_=00, to=12, width=3, format='%02.0f')
    year7_2_entry = Spinbox(tab7, from_=2018, to=2030, width=5)
    date7_2_entry.delete(0,'end')
    today=datetime.date.today() # today
    day_phase2 = today + datetime.timedelta(days=7) # calculate dates for 7 days after recording initiation
    date7_2_entry.insert(0,'{:02d}'.format(day_phase2.day))
    month7_2_entry.delete(0,'end')
    month7_2_entry.insert(0,'{:02d}'.format(day_phase2.month))
    year7_2_entry.delete(0,'end')
    year7_2_entry.insert(0,day_phase2.year) # ISO format is YYYY/MM/DD
    label7_d_2 = Label(tab7, text= '/')
    label7_m_2 = Label(tab7, text= '/')
    rad7_A_2 = Radiobutton(tab7, text='LD', variable=var7_2, value=1)
    lbl7_A_2 = Label(tab7, text= 'On:')
    spin7_A_2 = Spinbox(tab7, from_=00, to=24, width=3, format='%02.0f')
    spin7_B_2 = Spinbox(tab7, from_=00, to=59, width=3, format='%02.0f')
    spin7_A_2.delete(0,'end')
    spin7_A_2.insert(0,'07')
    spin7_B_2.delete(0,'end')
    spin7_B_2.insert(0,'00')
    label7_h1_2 = Label(tab7, text=':')
    label7_m1_2 = Label(tab7, text='')
    lbl7_B_2 = Label(tab7, text= 'Off:')
    spin7_C_2 = Spinbox(tab7, from_=00, to=24, width=3, format='%02.0f')
    spin7_D_2 = Spinbox(tab7, from_=00, to=59, width=3, format='%02.0f')
    spin7_C_2.delete(0,'end')
    spin7_C_2.insert(0,'19')
    spin7_D_2.delete(0,'end')
    spin7_D_2.insert(0,'00')
    label7_h2_2 = Label(tab7, text=':')
    label7_m2_2 = Label(tab7, text='')
    rad7_B_2 = Radiobutton(tab7, text='DD', variable=var7_2, value=2)
    rad7_C_2 = Radiobutton(tab7, text='LL', variable=var7_2, value=3)
    phaseLabel7_2.grid(column=0, row=2+row_adj, padx=15, pady=5)
    fromLabel7_2.grid(column=1,row=2+row_adj)
    spin7_E_2.grid(column=2,row=2+row_adj)
    label7_h0_2.grid(column=3,row=2+row_adj)
    spin7_F_2.grid(column=4,row=2+row_adj)
    label7_m0_2.grid(column=5,row=2+row_adj)
    space7_2.grid(column=6,row=2+row_adj)
    date7_2_entry.grid(column=11, row=2+row_adj)
    label7_d_2.grid(column=8,row=2+row_adj)
    month7_2_entry.grid(column=9, row=2+row_adj)
    label7_m_2.grid(column=10,row=2+row_adj)
    year7_2_entry.grid(column=7, row=2+row_adj) # ISO format
    space7_2_2.grid(column=12,row=2+row_adj,padx=5)
    rad7_A_2.grid(column=13, row=2+row_adj, pady=5)
    lbl7_A_2.grid(column=14, row=2+row_adj, pady=5)
    spin7_A_2.grid(column=15,row=2+row_adj, pady=5)
    label7_h1_2.grid(column=16,row=2+row_adj, pady=5)
    spin7_B_2.grid(column=17,row=2+row_adj, pady=5)
    label7_m1_2.grid(column=18,row=2+row_adj, pady=5)
    lbl7_B_2.grid(column=19, row=2+row_adj, pady=5)
    spin7_C_2.grid(column=20,row=2+row_adj, pady=5)
    label7_h2_2.grid(column=21,row=2+row_adj, pady=5)
    spin7_D_2.grid(column=22,row=2+row_adj, pady=5)
    label7_m2_2.grid(column=23,row=2+row_adj, pady=5)
    rad7_B_2.grid(column=24, row=2+row_adj, padx=15, pady=5)
    rad7_C_2.grid(column=25, row=2+row_adj, pady=5)
        # phase 3
    phaseLabel7_3 = Label(tab7, text='Phase 3')
    fromLabel7_3 = Label(tab7, text='From:')
    space7_3 = Label(tab7, text=' ')
    spin7_E_3 = Spinbox(tab7, from_=00, to=24, width=3, format='%02.0f')
    spin7_F_3 = Spinbox(tab7, from_=00, to=59, width=3, format='%02.0f')
    spin7_E_3.delete(0,'end')
    spin7_E_3.insert(0,'07')
    spin7_F_3.delete(0,'end')
    spin7_F_3.insert(0,'00')
    label7_h0_3 = Label(tab7, text=':')
    label7_m0_3 = Label(tab7, text='')
    date7_3_entry = Spinbox(tab7, from_=00, to=31, width=3, format='%02.0f')
    month7_3_entry = Spinbox(tab7, from_=00, to=12, width=3, format='%02.0f')
    year7_3_entry = Spinbox(tab7, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase3 = day_phase2 + datetime.timedelta(days=21) # calculate dates for 21 days after recording initiation
    date7_3_entry.delete(0,'end')
    date7_3_entry.insert(0,'{:02d}'.format(day_phase3.day))
    month7_3_entry.delete(0,'end')
    month7_3_entry.insert(0,'{:02d}'.format(day_phase3.month))
    year7_3_entry.delete(0,'end')
    year7_3_entry.insert(0,day_phase3.year)
    label7_d_3 = Label(tab7, text= '/')
    label7_m_3 = Label(tab7, text= '/')
    rad7_A_3 = Radiobutton(tab7, text='LD', variable=var7_3, value=1)
    lbl7_A_3 = Label(tab7, text= 'On:')
    spin7_A_3 = Spinbox(tab7, from_=00, to=24, width=3, format='%02.0f')
    spin7_B_3 = Spinbox(tab7, from_=00, to=59, width=3, format='%02.0f')
    spin7_A_3.delete(0,'end')
    spin7_A_3.insert(0,'07')
    spin7_B_3.delete(0,'end')
    spin7_B_3.insert(0,'00')
    label7_h1_3 = Label(tab7, text=':')
    label7_m1_3 = Label(tab7, text='')
    lbl7_B_3 = Label(tab7, text= 'Off:')
    spin7_C_3 = Spinbox(tab7, from_=00, to=24, width=3, format='%02.0f')
    spin7_D_3 = Spinbox(tab7, from_=00, to=59, width=3, format='%02.0f')
    spin7_C_3.delete(0,'end')
    spin7_C_3.insert(0,'19')
    spin7_D_3.delete(0,'end')
    spin7_D_3.insert(0,'00')
    label7_h2_3 = Label(tab7, text=':')
    label7_m2_3 = Label(tab7, text='')
    rad7_B_3 = Radiobutton(tab7, text='DD', variable=var7_3, value=2)
    rad7_C_3 = Radiobutton(tab7, text='LL', variable=var7_3, value=3)
    phaseLabel7_3.grid(column=0, row=3+row_adj, padx=15, pady=5)
    fromLabel7_3.grid(column=1,row=3+row_adj)
    spin7_E_3.grid(column=2,row=3+row_adj)
    label7_h0_3.grid(column=3,row=3+row_adj)
    spin7_F_3.grid(column=4,row=3+row_adj)
    label7_m0_3.grid(column=5,row=3+row_adj)
    space7_3.grid(column=6,row=3+row_adj)
    date7_3_entry.grid(column=11, row=3+row_adj)
    label7_d_3.grid(column=8,row=3+row_adj)
    month7_3_entry.grid(column=9, row=3+row_adj)
    label7_m_3.grid(column=10,row=3+row_adj)
    year7_3_entry.grid(column=7, row=3+row_adj) # ISO format
    rad7_A_3.grid(column=13, row=3+row_adj, pady=5)
    lbl7_A_3.grid(column=14, row=3+row_adj, pady=5)
    spin7_A_3.grid(column=15,row=3+row_adj, pady=5)
    label7_h1_3.grid(column=16,row=3+row_adj, pady=5)
    spin7_B_3.grid(column=17,row=3+row_adj, pady=5)
    label7_m1_3.grid(column=18,row=3+row_adj, pady=5)
    lbl7_B_3.grid(column=19, row=3+row_adj, pady=5)
    spin7_C_3.grid(column=20,row=3+row_adj, pady=5)
    label7_h2_3.grid(column=21,row=3+row_adj, pady=5)
    spin7_D_3.grid(column=22,row=3+row_adj, pady=5)
    label7_m2_3.grid(column=23,row=3+row_adj, pady=5)
    rad7_B_3.grid(column=24, row=3+row_adj, padx=15, pady=5)
    rad7_C_3.grid(column=25, row=3+row_adj, pady=5)
    btn7.grid(column=0, row=4+row_adj, padx=25, pady=5, columnspan='2', sticky='w')
    btnAll7.grid(column=1, row=4+row_adj, pady=5, columnspan='1', sticky='w')
    box7sched_stat.grid(column=3, row=4+row_adj, columnspan='8', sticky='w')
    window.update_idletasks()
    tab7_title2 = Label(tab7, text= 'Recording status', anchor='center')
    tab7_title2.grid(column=0, row= row_adj+6, columnspan='27', sticky='we')
    box7rec_text=StringVar()
    box7rec_text.set('Recording not started yet.')
    box7rec_stat=Label(tab7, textvariable=box7rec_text, anchor='center', justify=LEFT)
    box7rec_stat.grid(column=0, row= row_adj+7, columnspan='27', sticky='we')
    window.update_idletasks()

    # Box8
    btn8 = Button(tab8, text='  Set  ', command=lambda: OnButtonClick(8))
    btnAll8 = Button(tab8, text='Set All', command=getAllBoxSchedule)
    tab8_title = Label(tab8, text= 'LED schedule', anchor='center')
    tab8_title.grid(column=0, row= -1+row_adj, columnspan='27', sticky='we')
    capSep8 = ttk.Separator(tab8, orient=HORIZONTAL)
    capSep8.grid(column=0, row = row_adj+5, columnspan='27', sticky='we')
    box8sched_text=StringVar()
    box8sched_text.set('Schedule not set.')
    box8sched_stat=Label(tab8, textvariable=box8sched_text, anchor=W, justify=LEFT)
        # phase 1
    phaseLabel8_1 = Label(tab8, text='Phase 1')
    dateLabel = time.strftime('%H:%M   %Y/%m/%d') # reads time for Phase 1 start-time
    fromLabel8_1 = Label(tab8, text='From:')
    date_label8 = Label(tab8, text=dateLabel+' (HH:MN YYYY/MO/DD)')
    rad8_A_1 = Radiobutton(tab8, text='LD', variable=var8_1, value=1)
    lbl8_A_1 = Label(tab8, text= 'On:')
    spin8_A_1 = Spinbox(tab8, from_=00, to=24, width=3, format='%02.0f')
    spin8_B_1 = Spinbox(tab8, from_=00, to=59, width=3, format='%02.0f')
    spin8_A_1.delete(0,'end')
    spin8_A_1.insert(0,'07')
    spin8_B_1.delete(0,'end')
    spin8_B_1.insert(0,'00')
    label8_h1_1 = Label(tab8, text=':')
    label8_m1_1 = Label(tab8, text='')
    lbl8_B_1 = Label(tab8, text= 'Off:')
    spin8_C_1 = Spinbox(tab8, from_=00, to=24, width=3, format='%02.0f')
    spin8_D_1 = Spinbox(tab8, from_=00, to=59, width=3, format='%02.0f')
    spin8_C_1.delete(0,'end')
    spin8_C_1.insert(0,'19')
    spin8_D_1.delete(0,'end')
    spin8_D_1.insert(0,'00')
    label8_h2_1 = Label(tab8, text=':')
    label8_m2_1 = Label(tab8, text='')
    rad8_B_1 = Radiobutton(tab8, text='DD', variable=var8_1, value=2)
    rad8_C_1 = Radiobutton(tab8, text='LL', variable=var8_1, value=3)
    phaseLabel8_1.grid(column=0, row=1+row_adj, padx=15, pady=5)
    fromLabel8_1.grid(column=1,row=1+row_adj)
    date_label8.grid(column=2, row=1+row_adj, columnspan='10', sticky='w')
    rad8_A_1.grid(column=13, row=1+row_adj, pady=5)
    lbl8_A_1.grid(column=14, row=1+row_adj, pady=5)
    spin8_A_1.grid(column=15,row=1+row_adj, pady=5)
    label8_h1_1.grid(column=16,row=1+row_adj, pady=5, sticky='w')
    spin8_B_1.grid(column=17,row=1+row_adj, pady=5)
    label8_m1_1.grid(column=18,row=1+row_adj, pady=5, sticky='w')
    lbl8_B_1.grid(column=19, row=1+row_adj, pady=5)
    spin8_C_1.grid(column=20,row=1+row_adj, pady=5)
    label8_h2_1.grid(column=21,row=1+row_adj, pady=5, sticky='w')
    spin8_D_1.grid(column=22,row=1+row_adj, pady=5)
    label8_m2_1.grid(column=23,row=1+row_adj, pady=5, sticky='w')
    rad8_B_1.grid(column=24, row=1+row_adj, padx=15, pady=5)
    rad8_C_1.grid(column=25, row=1+row_adj, pady=5)
        # phase 2
    phaseLabel8_2 = Label(tab8, text='Phase 2')
    fromLabel8_2 = Label(tab8, text='From:')
    space8_2 = Label(tab8, text=' ')
    space8_2_2 = Label(tab8, text=' ')
    spin8_E_2 = Spinbox(tab8, from_=00, to=24, width=3, format='%02.0f')
    spin8_F_2 = Spinbox(tab8, from_=00, to=59, width=3, format='%02.0f')
    spin8_E_2.delete(0,'end')
    spin8_E_2.insert(0,'07')
    spin8_F_2.delete(0,'end')
    spin8_F_2.insert(0,'00')
    label8_h0_2 = Label(tab8, text=':')
    label8_m0_2 = Label(tab8, text='')
    date8_2_entry = Spinbox(tab8, from_=00, to=31, width=3, format='%02.0f')
    month8_2_entry = Spinbox(tab8, from_=00, to=12, width=3, format='%02.0f')
    year8_2_entry = Spinbox(tab8, from_=2018, to=2030, width=5)
    date8_2_entry.delete(0,'end')
    today=datetime.date.today() # today
    day_phase2 = today + datetime.timedelta(days=7) # calculate dates for 7 days after recording initiation
    date8_2_entry.insert(0,'{:02d}'.format(day_phase2.day))
    month8_2_entry.delete(0,'end')
    month8_2_entry.insert(0,'{:02d}'.format(day_phase2.month))
    year8_2_entry.delete(0,'end')
    year8_2_entry.insert(0,day_phase2.year) # ISO format is YYYY/MM/DD
    label8_d_2 = Label(tab8, text= '/')
    label8_m_2 = Label(tab8, text= '/')
    rad8_A_2 = Radiobutton(tab8, text='LD', variable=var8_2, value=1)
    lbl8_A_2 = Label(tab8, text= 'On:')
    spin8_A_2 = Spinbox(tab8, from_=00, to=24, width=3, format='%02.0f')
    spin8_B_2 = Spinbox(tab8, from_=00, to=59, width=3, format='%02.0f')
    spin8_A_2.delete(0,'end')
    spin8_A_2.insert(0,'07')
    spin8_B_2.delete(0,'end')
    spin8_B_2.insert(0,'00')
    label8_h1_2 = Label(tab8, text=':')
    label8_m1_2 = Label(tab8, text='')
    lbl8_B_2 = Label(tab8, text= 'Off:')
    spin8_C_2 = Spinbox(tab8, from_=00, to=24, width=3, format='%02.0f')
    spin8_D_2 = Spinbox(tab8, from_=00, to=59, width=3, format='%02.0f')
    spin8_C_2.delete(0,'end')
    spin8_C_2.insert(0,'19')
    spin8_D_2.delete(0,'end')
    spin8_D_2.insert(0,'00')
    label8_h2_2 = Label(tab8, text=':')
    label8_m2_2 = Label(tab8, text='')
    rad8_B_2 = Radiobutton(tab8, text='DD', variable=var8_2, value=2)
    rad8_C_2 = Radiobutton(tab8, text='LL', variable=var8_2, value=3)
    phaseLabel8_2.grid(column=0, row=2+row_adj, padx=15, pady=5)
    fromLabel8_2.grid(column=1,row=2+row_adj)
    spin8_E_2.grid(column=2,row=2+row_adj)
    label8_h0_2.grid(column=3,row=2+row_adj)
    spin8_F_2.grid(column=4,row=2+row_adj)
    label8_m0_2.grid(column=5,row=2+row_adj)
    space8_2.grid(column=6,row=2+row_adj)
    date8_2_entry.grid(column=11, row=2+row_adj)
    label8_d_2.grid(column=8,row=2+row_adj)
    month8_2_entry.grid(column=9, row=2+row_adj)
    label8_m_2.grid(column=10,row=2+row_adj)
    year8_2_entry.grid(column=7, row=2+row_adj) # ISO format
    space8_2_2.grid(column=12,row=2+row_adj,padx=5)
    rad8_A_2.grid(column=13, row=2+row_adj, pady=5)
    lbl8_A_2.grid(column=14, row=2+row_adj, pady=5)
    spin8_A_2.grid(column=15,row=2+row_adj, pady=5)
    label8_h1_2.grid(column=16,row=2+row_adj, pady=5)
    spin8_B_2.grid(column=17,row=2+row_adj, pady=5)
    label8_m1_2.grid(column=18,row=2+row_adj, pady=5)
    lbl8_B_2.grid(column=19, row=2+row_adj, pady=5)
    spin8_C_2.grid(column=20,row=2+row_adj, pady=5)
    label8_h2_2.grid(column=21,row=2+row_adj, pady=5)
    spin8_D_2.grid(column=22,row=2+row_adj, pady=5)
    label8_m2_2.grid(column=23,row=2+row_adj, pady=5)
    rad8_B_2.grid(column=24, row=2+row_adj, padx=15, pady=5)
    rad8_C_2.grid(column=25, row=2+row_adj, pady=5)
        # phase 3
    phaseLabel8_3 = Label(tab8, text='Phase 3')
    fromLabel8_3 = Label(tab8, text='From:')
    space8_3 = Label(tab8, text=' ')
    spin8_E_3 = Spinbox(tab8, from_=00, to=24, width=3, format='%02.0f')
    spin8_F_3 = Spinbox(tab8, from_=00, to=59, width=3, format='%02.0f')
    spin8_E_3.delete(0,'end')
    spin8_E_3.insert(0,'07')
    spin8_F_3.delete(0,'end')
    spin8_F_3.insert(0,'00')
    label8_h0_3 = Label(tab8, text=':')
    label8_m0_3 = Label(tab8, text='')
    date8_3_entry = Spinbox(tab8, from_=00, to=31, width=3, format='%02.0f')
    month8_3_entry = Spinbox(tab8, from_=00, to=12, width=3, format='%02.0f')
    year8_3_entry = Spinbox(tab8, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase3 = day_phase2 + datetime.timedelta(days=21) # calculate dates for 21 days after recording initiation
    date8_3_entry.delete(0,'end')
    date8_3_entry.insert(0,'{:02d}'.format(day_phase3.day))
    month8_3_entry.delete(0,'end')
    month8_3_entry.insert(0,'{:02d}'.format(day_phase3.month))
    year8_3_entry.delete(0,'end')
    year8_3_entry.insert(0,day_phase3.year)
    label8_d_3 = Label(tab8, text= '/')
    label8_m_3 = Label(tab8, text= '/')
    rad8_A_3 = Radiobutton(tab8, text='LD', variable=var8_3, value=1)
    lbl8_A_3 = Label(tab8, text= 'On:')
    spin8_A_3 = Spinbox(tab8, from_=00, to=24, width=3, format='%02.0f')
    spin8_B_3 = Spinbox(tab8, from_=00, to=59, width=3, format='%02.0f')
    spin8_A_3.delete(0,'end')
    spin8_A_3.insert(0,'07')
    spin8_B_3.delete(0,'end')
    spin8_B_3.insert(0,'00')
    label8_h1_3 = Label(tab8, text=':')
    label8_m1_3 = Label(tab8, text='')
    lbl8_B_3 = Label(tab8, text= 'Off:')
    spin8_C_3 = Spinbox(tab8, from_=00, to=24, width=3, format='%02.0f')
    spin8_D_3 = Spinbox(tab8, from_=00, to=59, width=3, format='%02.0f')
    spin8_C_3.delete(0,'end')
    spin8_C_3.insert(0,'19')
    spin8_D_3.delete(0,'end')
    spin8_D_3.insert(0,'00')
    label8_h2_3 = Label(tab8, text=':')
    label8_m2_3 = Label(tab8, text='')
    rad8_B_3 = Radiobutton(tab8, text='DD', variable=var8_3, value=2)
    rad8_C_3 = Radiobutton(tab8, text='LL', variable=var8_3, value=3)
    phaseLabel8_3.grid(column=0, row=3+row_adj, padx=15, pady=5)
    fromLabel8_3.grid(column=1,row=3+row_adj)
    spin8_E_3.grid(column=2,row=3+row_adj)
    label8_h0_3.grid(column=3,row=3+row_adj)
    spin8_F_3.grid(column=4,row=3+row_adj)
    label8_m0_3.grid(column=5,row=3+row_adj)
    space8_3.grid(column=6,row=3+row_adj)
    date8_3_entry.grid(column=11, row=3+row_adj)
    label8_d_3.grid(column=8,row=3+row_adj)
    month8_3_entry.grid(column=9, row=3+row_adj)
    label8_m_3.grid(column=10,row=3+row_adj)
    year8_3_entry.grid(column=7, row=3+row_adj) # ISO format
    rad8_A_3.grid(column=13, row=3+row_adj, pady=5)
    lbl8_A_3.grid(column=14, row=3+row_adj, pady=5)
    spin8_A_3.grid(column=15,row=3+row_adj, pady=5)
    label8_h1_3.grid(column=16,row=3+row_adj, pady=5)
    spin8_B_3.grid(column=17,row=3+row_adj, pady=5)
    label8_m1_3.grid(column=18,row=3+row_adj, pady=5)
    lbl8_B_3.grid(column=19, row=3+row_adj, pady=5)
    spin8_C_3.grid(column=20,row=3+row_adj, pady=5)
    label8_h2_3.grid(column=21,row=3+row_adj, pady=5)
    spin8_D_3.grid(column=22,row=3+row_adj, pady=5)
    label8_m2_3.grid(column=23,row=3+row_adj, pady=5)
    rad8_B_3.grid(column=24, row=3+row_adj, padx=15, pady=5)
    rad8_C_3.grid(column=25, row=3+row_adj, pady=5)
    btn8.grid(column=0, row=4+row_adj, padx=25, pady=5, columnspan='2', sticky='w')
    btnAll8.grid(column=1, row=4+row_adj, pady=5, columnspan='1', sticky='w')
    box8sched_stat.grid(column=3, row=4+row_adj, columnspan='8', sticky='w')
    window.update_idletasks()
    tab8_title2 = Label(tab8, text= 'Recording status', anchor='center')
    tab8_title2.grid(column=0, row= row_adj+6, columnspan='27', sticky='we')
    box8rec_text=StringVar()
    box8rec_text.set('Recording not started yet.')
    box8rec_stat=Label(tab8, textvariable=box8rec_text, anchor='center', justify=LEFT)
    box8rec_stat.grid(column=0, row= row_adj+7, columnspan='27', sticky='we')
    window.update_idletasks()

    # Box9
    btn9 = Button(tab9, text='  Set  ', command=lambda: OnButtonClick(9))
    btnAll9 = Button(tab9, text='Set All', command=getAllBoxSchedule)
    tab9_title = Label(tab9, text= 'LED schedule', anchor='center')
    tab9_title.grid(column=0, row= -1+row_adj, columnspan='27', sticky='we')
    capSep9 = ttk.Separator(tab9, orient=HORIZONTAL)
    capSep9.grid(column=0, row = row_adj+5, columnspan='27', sticky='we')
    box9sched_text=StringVar()
    box9sched_text.set('Schedule not set.')
    box9sched_stat=Label(tab9, textvariable=box9sched_text, anchor=W, justify=LEFT)
        # phase 1
    phaseLabel9_1 = Label(tab9, text='Phase 1')
    dateLabel = time.strftime('%H:%M   %Y/%m/%d') # reads time for Phase 1 start-time
    fromLabel9_1 = Label(tab9, text='From:')
    date_label9 = Label(tab9, text=dateLabel+' (HH:MN YYYY/MO/DD)')
    rad9_A_1 = Radiobutton(tab9, text='LD', variable=var9_1, value=1)
    lbl9_A_1 = Label(tab9, text= 'On:')
    spin9_A_1 = Spinbox(tab9, from_=00, to=24, width=3, format='%02.0f')
    spin9_B_1 = Spinbox(tab9, from_=00, to=59, width=3, format='%02.0f')
    spin9_A_1.delete(0,'end')
    spin9_A_1.insert(0,'07')
    spin9_B_1.delete(0,'end')
    spin9_B_1.insert(0,'00')
    label9_h1_1 = Label(tab9, text=':')
    label9_m1_1 = Label(tab9, text='')
    lbl9_B_1 = Label(tab9, text= 'Off:')
    spin9_C_1 = Spinbox(tab9, from_=00, to=24, width=3, format='%02.0f')
    spin9_D_1 = Spinbox(tab9, from_=00, to=59, width=3, format='%02.0f')
    spin9_C_1.delete(0,'end')
    spin9_C_1.insert(0,'19')
    spin9_D_1.delete(0,'end')
    spin9_D_1.insert(0,'00')
    label9_h2_1 = Label(tab9, text=':')
    label9_m2_1 = Label(tab9, text='')
    rad9_B_1 = Radiobutton(tab9, text='DD', variable=var9_1, value=2)
    rad9_C_1 = Radiobutton(tab9, text='LL', variable=var9_1, value=3)
    phaseLabel9_1.grid(column=0, row=1+row_adj, padx=15, pady=5)
    fromLabel9_1.grid(column=1,row=1+row_adj)
    date_label9.grid(column=2, row=1+row_adj, columnspan='10', sticky='w')
    rad9_A_1.grid(column=13, row=1+row_adj, pady=5)
    lbl9_A_1.grid(column=14, row=1+row_adj, pady=5)
    spin9_A_1.grid(column=15,row=1+row_adj, pady=5)
    label9_h1_1.grid(column=16,row=1+row_adj, pady=5, sticky='w')
    spin9_B_1.grid(column=17,row=1+row_adj, pady=5)
    label9_m1_1.grid(column=18,row=1+row_adj, pady=5, sticky='w')
    lbl9_B_1.grid(column=19, row=1+row_adj, pady=5)
    spin9_C_1.grid(column=20,row=1+row_adj, pady=5)
    label9_h2_1.grid(column=21,row=1+row_adj, pady=5, sticky='w')
    spin9_D_1.grid(column=22,row=1+row_adj, pady=5)
    label9_m2_1.grid(column=23,row=1+row_adj, pady=5, sticky='w')
    rad9_B_1.grid(column=24, row=1+row_adj, padx=15, pady=5)
    rad9_C_1.grid(column=25, row=1+row_adj, pady=5)
        # phase 2
    phaseLabel9_2 = Label(tab9, text='Phase 2')
    fromLabel9_2 = Label(tab9, text='From:')
    space9_2 = Label(tab9, text=' ')
    space9_2_2 = Label(tab9, text=' ')
    spin9_E_2 = Spinbox(tab9, from_=00, to=24, width=3, format='%02.0f')
    spin9_F_2 = Spinbox(tab9, from_=00, to=59, width=3, format='%02.0f')
    spin9_E_2.delete(0,'end')
    spin9_E_2.insert(0,'07')
    spin9_F_2.delete(0,'end')
    spin9_F_2.insert(0,'00')
    label9_h0_2 = Label(tab9, text=':')
    label9_m0_2 = Label(tab9, text='')
    date9_2_entry = Spinbox(tab9, from_=00, to=31, width=3, format='%02.0f')
    month9_2_entry = Spinbox(tab9, from_=00, to=12, width=3, format='%02.0f')
    year9_2_entry = Spinbox(tab9, from_=2018, to=2030, width=5)
    date9_2_entry.delete(0,'end')
    today=datetime.date.today() # today
    day_phase2 = today + datetime.timedelta(days=7) # calculate dates for 7 days after recording initiation
    date9_2_entry.insert(0,'{:02d}'.format(day_phase2.day))
    month9_2_entry.delete(0,'end')
    month9_2_entry.insert(0,'{:02d}'.format(day_phase2.month))
    year9_2_entry.delete(0,'end')
    year9_2_entry.insert(0,day_phase2.year) # ISO format is YYYY/MM/DD
    label9_d_2 = Label(tab9, text= '/')
    label9_m_2 = Label(tab9, text= '/')
    rad9_A_2 = Radiobutton(tab9, text='LD', variable=var9_2, value=1)
    lbl9_A_2 = Label(tab9, text= 'On:')
    spin9_A_2 = Spinbox(tab9, from_=00, to=24, width=3, format='%02.0f')
    spin9_B_2 = Spinbox(tab9, from_=00, to=59, width=3, format='%02.0f')
    spin9_A_2.delete(0,'end')
    spin9_A_2.insert(0,'07')
    spin9_B_2.delete(0,'end')
    spin9_B_2.insert(0,'00')
    label9_h1_2 = Label(tab9, text=':')
    label9_m1_2 = Label(tab9, text='')
    lbl9_B_2 = Label(tab9, text= 'Off:')
    spin9_C_2 = Spinbox(tab9, from_=00, to=24, width=3, format='%02.0f')
    spin9_D_2 = Spinbox(tab9, from_=00, to=59, width=3, format='%02.0f')
    spin9_C_2.delete(0,'end')
    spin9_C_2.insert(0,'19')
    spin9_D_2.delete(0,'end')
    spin9_D_2.insert(0,'00')
    label9_h2_2 = Label(tab9, text=':')
    label9_m2_2 = Label(tab9, text='')
    rad9_B_2 = Radiobutton(tab9, text='DD', variable=var9_2, value=2)
    rad9_C_2 = Radiobutton(tab9, text='LL', variable=var9_2, value=3)
    phaseLabel9_2.grid(column=0, row=2+row_adj, padx=15, pady=5)
    fromLabel9_2.grid(column=1,row=2+row_adj)
    spin9_E_2.grid(column=2,row=2+row_adj)
    label9_h0_2.grid(column=3,row=2+row_adj)
    spin9_F_2.grid(column=4,row=2+row_adj)
    label9_m0_2.grid(column=5,row=2+row_adj)
    space9_2.grid(column=6,row=2+row_adj)
    date9_2_entry.grid(column=11, row=2+row_adj)
    label9_d_2.grid(column=8,row=2+row_adj)
    month9_2_entry.grid(column=9, row=2+row_adj)
    label9_m_2.grid(column=10,row=2+row_adj)
    year9_2_entry.grid(column=7, row=2+row_adj) # ISO format
    space9_2_2.grid(column=12,row=2+row_adj,padx=5)
    rad9_A_2.grid(column=13, row=2+row_adj, pady=5)
    lbl9_A_2.grid(column=14, row=2+row_adj, pady=5)
    spin9_A_2.grid(column=15,row=2+row_adj, pady=5)
    label9_h1_2.grid(column=16,row=2+row_adj, pady=5)
    spin9_B_2.grid(column=17,row=2+row_adj, pady=5)
    label9_m1_2.grid(column=18,row=2+row_adj, pady=5)
    lbl9_B_2.grid(column=19, row=2+row_adj, pady=5)
    spin9_C_2.grid(column=20,row=2+row_adj, pady=5)
    label9_h2_2.grid(column=21,row=2+row_adj, pady=5)
    spin9_D_2.grid(column=22,row=2+row_adj, pady=5)
    label9_m2_2.grid(column=23,row=2+row_adj, pady=5)
    rad9_B_2.grid(column=24, row=2+row_adj, padx=15, pady=5)
    rad9_C_2.grid(column=25, row=2+row_adj, pady=5)
        # phase 3
    phaseLabel9_3 = Label(tab9, text='Phase 3')
    fromLabel9_3 = Label(tab9, text='From:')
    space9_3 = Label(tab9, text=' ')
    spin9_E_3 = Spinbox(tab9, from_=00, to=24, width=3, format='%02.0f')
    spin9_F_3 = Spinbox(tab9, from_=00, to=59, width=3, format='%02.0f')
    spin9_E_3.delete(0,'end')
    spin9_E_3.insert(0,'07')
    spin9_F_3.delete(0,'end')
    spin9_F_3.insert(0,'00')
    label9_h0_3 = Label(tab9, text=':')
    label9_m0_3 = Label(tab9, text='')
    date9_3_entry = Spinbox(tab9, from_=00, to=31, width=3, format='%02.0f')
    month9_3_entry = Spinbox(tab9, from_=00, to=12, width=3, format='%02.0f')
    year9_3_entry = Spinbox(tab9, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase3 = day_phase2 + datetime.timedelta(days=21) # calculate dates for 21 days after recording initiation
    date9_3_entry.delete(0,'end')
    date9_3_entry.insert(0,'{:02d}'.format(day_phase3.day))
    month9_3_entry.delete(0,'end')
    month9_3_entry.insert(0,'{:02d}'.format(day_phase3.month))
    year9_3_entry.delete(0,'end')
    year9_3_entry.insert(0,day_phase3.year)
    label9_d_3 = Label(tab9, text= '/')
    label9_m_3 = Label(tab9, text= '/')
    rad9_A_3 = Radiobutton(tab9, text='LD', variable=var9_3, value=1)
    lbl9_A_3 = Label(tab9, text= 'On:')
    spin9_A_3 = Spinbox(tab9, from_=00, to=24, width=3, format='%02.0f')
    spin9_B_3 = Spinbox(tab9, from_=00, to=59, width=3, format='%02.0f')
    spin9_A_3.delete(0,'end')
    spin9_A_3.insert(0,'07')
    spin9_B_3.delete(0,'end')
    spin9_B_3.insert(0,'00')
    label9_h1_3 = Label(tab9, text=':')
    label9_m1_3 = Label(tab9, text='')
    lbl9_B_3 = Label(tab9, text= 'Off:')
    spin9_C_3 = Spinbox(tab9, from_=00, to=24, width=3, format='%02.0f')
    spin9_D_3 = Spinbox(tab9, from_=00, to=59, width=3, format='%02.0f')
    spin9_C_3.delete(0,'end')
    spin9_C_3.insert(0,'19')
    spin9_D_3.delete(0,'end')
    spin9_D_3.insert(0,'00')
    label9_h2_3 = Label(tab9, text=':')
    label9_m2_3 = Label(tab9, text='')
    rad9_B_3 = Radiobutton(tab9, text='DD', variable=var9_3, value=2)
    rad9_C_3 = Radiobutton(tab9, text='LL', variable=var9_3, value=3)
    phaseLabel9_3.grid(column=0, row=3+row_adj, padx=15, pady=5)
    fromLabel9_3.grid(column=1,row=3+row_adj)
    spin9_E_3.grid(column=2,row=3+row_adj)
    label9_h0_3.grid(column=3,row=3+row_adj)
    spin9_F_3.grid(column=4,row=3+row_adj)
    label9_m0_3.grid(column=5,row=3+row_adj)
    space9_3.grid(column=6,row=3+row_adj)
    date9_3_entry.grid(column=11, row=3+row_adj)
    label9_d_3.grid(column=8,row=3+row_adj)
    month9_3_entry.grid(column=9, row=3+row_adj)
    label9_m_3.grid(column=10,row=3+row_adj)
    year9_3_entry.grid(column=7, row=3+row_adj) # ISO format
    rad9_A_3.grid(column=13, row=3+row_adj, pady=5)
    lbl9_A_3.grid(column=14, row=3+row_adj, pady=5)
    spin9_A_3.grid(column=15,row=3+row_adj, pady=5)
    label9_h1_3.grid(column=16,row=3+row_adj, pady=5)
    spin9_B_3.grid(column=17,row=3+row_adj, pady=5)
    label9_m1_3.grid(column=18,row=3+row_adj, pady=5)
    lbl9_B_3.grid(column=19, row=3+row_adj, pady=5)
    spin9_C_3.grid(column=20,row=3+row_adj, pady=5)
    label9_h2_3.grid(column=21,row=3+row_adj, pady=5)
    spin9_D_3.grid(column=22,row=3+row_adj, pady=5)
    label9_m2_3.grid(column=23,row=3+row_adj, pady=5)
    rad9_B_3.grid(column=24, row=3+row_adj, padx=15, pady=5)
    rad9_C_3.grid(column=25, row=3+row_adj, pady=5)
    btn9.grid(column=0, row=4+row_adj, padx=25, pady=5, columnspan='2', sticky='w')
    btnAll9.grid(column=1, row=4+row_adj, pady=5, columnspan='1', sticky='w')
    box9sched_stat.grid(column=3, row=4+row_adj, columnspan='8', sticky='w')
    window.update_idletasks()
    tab9_title2 = Label(tab9, text= 'Recording status', anchor='center')
    tab9_title2.grid(column=0, row= row_adj+6, columnspan='27', sticky='we')
    box9rec_text=StringVar()
    box9rec_text.set('Recording not started yet.')
    box9rec_stat=Label(tab9, textvariable=box9rec_text, anchor='center', justify=LEFT)
    box9rec_stat.grid(column=0, row= row_adj+7, columnspan='27', sticky='we')
    window.update_idletasks()

    # Box10
    btn10 = Button(tab10, text='  Set  ', command=lambda: OnButtonClick(10))
    btnAll10 = Button(tab10, text='Set All', command=getAllBoxSchedule)
    tab10_title = Label(tab10, text= 'LED schedule', anchor='center')
    tab10_title.grid(column=0, row= -1+row_adj, columnspan='27', sticky='we')
    capSep10 = ttk.Separator(tab10, orient=HORIZONTAL)
    capSep10.grid(column=0, row = row_adj+5, columnspan='27', sticky='we')
    box10sched_text=StringVar()
    box10sched_text.set('Schedule not set.')
    box10sched_stat=Label(tab10, textvariable=box10sched_text, anchor=W, justify=LEFT)
        # phase 1
    phaseLabel10_1 = Label(tab10, text='Phase 1')
    dateLabel = time.strftime('%H:%M   %Y/%m/%d') # reads time for Phase 1 start-time
    fromLabel10_1 = Label(tab10, text='From:')
    date_label10 = Label(tab10, text=dateLabel+' (HH:MN YYYY/MO/DD)')
    rad10_A_1 = Radiobutton(tab10, text='LD', variable=var10_1, value=1)
    lbl10_A_1 = Label(tab10, text= 'On:')
    spin10_A_1 = Spinbox(tab10, from_=00, to=24, width=3, format='%02.0f')
    spin10_B_1 = Spinbox(tab10, from_=00, to=59, width=3, format='%02.0f')
    spin10_A_1.delete(0,'end')
    spin10_A_1.insert(0,'07')
    spin10_B_1.delete(0,'end')
    spin10_B_1.insert(0,'00')
    label10_h1_1 = Label(tab10, text=':')
    label10_m1_1 = Label(tab10, text='')
    lbl10_B_1 = Label(tab10, text= 'Off:')
    spin10_C_1 = Spinbox(tab10, from_=00, to=24, width=3, format='%02.0f')
    spin10_D_1 = Spinbox(tab10, from_=00, to=59, width=3, format='%02.0f')
    spin10_C_1.delete(0,'end')
    spin10_C_1.insert(0,'19')
    spin10_D_1.delete(0,'end')
    spin10_D_1.insert(0,'00')
    label10_h2_1 = Label(tab10, text=':')
    label10_m2_1 = Label(tab10, text='')
    rad10_B_1 = Radiobutton(tab10, text='DD', variable=var10_1, value=2)
    rad10_C_1 = Radiobutton(tab10, text='LL', variable=var10_1, value=3)
    phaseLabel10_1.grid(column=0, row=1+row_adj, padx=15, pady=5)
    fromLabel10_1.grid(column=1,row=1+row_adj)
    date_label10.grid(column=2, row=1+row_adj, columnspan='10', sticky='w')
    rad10_A_1.grid(column=13, row=1+row_adj, pady=5)
    lbl10_A_1.grid(column=14, row=1+row_adj, pady=5)
    spin10_A_1.grid(column=15,row=1+row_adj, pady=5)
    label10_h1_1.grid(column=16,row=1+row_adj, pady=5, sticky='w')
    spin10_B_1.grid(column=17,row=1+row_adj, pady=5)
    label10_m1_1.grid(column=18,row=1+row_adj, pady=5, sticky='w')
    lbl10_B_1.grid(column=19, row=1+row_adj, pady=5)
    spin10_C_1.grid(column=20,row=1+row_adj, pady=5)
    label10_h2_1.grid(column=21,row=1+row_adj, pady=5, sticky='w')
    spin10_D_1.grid(column=22,row=1+row_adj, pady=5)
    label10_m2_1.grid(column=23,row=1+row_adj, pady=5, sticky='w')
    rad10_B_1.grid(column=24, row=1+row_adj, padx=15, pady=5)
    rad10_C_1.grid(column=25, row=1+row_adj, pady=5)
        # phase 2
    phaseLabel10_2 = Label(tab10, text='Phase 2')
    fromLabel10_2 = Label(tab10, text='From:')
    space10_2 = Label(tab10, text=' ')
    space10_2_2 = Label(tab10, text=' ')
    spin10_E_2 = Spinbox(tab10, from_=00, to=24, width=3, format='%02.0f')
    spin10_F_2 = Spinbox(tab10, from_=00, to=59, width=3, format='%02.0f')
    spin10_E_2.delete(0,'end')
    spin10_E_2.insert(0,'07')
    spin10_F_2.delete(0,'end')
    spin10_F_2.insert(0,'00')
    label10_h0_2 = Label(tab10, text=':')
    label10_m0_2 = Label(tab10, text='')
    date10_2_entry = Spinbox(tab10, from_=00, to=31, width=3, format='%02.0f')
    month10_2_entry = Spinbox(tab10, from_=00, to=12, width=3, format='%02.0f')
    year10_2_entry = Spinbox(tab10, from_=2018, to=2030, width=5)
    date10_2_entry.delete(0,'end')
    today=datetime.date.today() # today
    day_phase2 = today + datetime.timedelta(days=7) # calculate dates for 7 days after recording initiation
    date10_2_entry.insert(0,'{:02d}'.format(day_phase2.day))
    month10_2_entry.delete(0,'end')
    month10_2_entry.insert(0,'{:02d}'.format(day_phase2.month))
    year10_2_entry.delete(0,'end')
    year10_2_entry.insert(0,day_phase2.year) # ISO format is YYYY/MM/DD
    label10_d_2 = Label(tab10, text= '/')
    label10_m_2 = Label(tab10, text= '/')
    rad10_A_2 = Radiobutton(tab10, text='LD', variable=var10_2, value=1)
    lbl10_A_2 = Label(tab10, text= 'On:')
    spin10_A_2 = Spinbox(tab10, from_=00, to=24, width=3, format='%02.0f')
    spin10_B_2 = Spinbox(tab10, from_=00, to=59, width=3, format='%02.0f')
    spin10_A_2.delete(0,'end')
    spin10_A_2.insert(0,'07')
    spin10_B_2.delete(0,'end')
    spin10_B_2.insert(0,'00')
    label10_h1_2 = Label(tab10, text=':')
    label10_m1_2 = Label(tab10, text='')
    lbl10_B_2 = Label(tab10, text= 'Off:')
    spin10_C_2 = Spinbox(tab10, from_=00, to=24, width=3, format='%02.0f')
    spin10_D_2 = Spinbox(tab10, from_=00, to=59, width=3, format='%02.0f')
    spin10_C_2.delete(0,'end')
    spin10_C_2.insert(0,'19')
    spin10_D_2.delete(0,'end')
    spin10_D_2.insert(0,'00')
    label10_h2_2 = Label(tab10, text=':')
    label10_m2_2 = Label(tab10, text='')
    rad10_B_2 = Radiobutton(tab10, text='DD', variable=var10_2, value=2)
    rad10_C_2 = Radiobutton(tab10, text='LL', variable=var10_2, value=3)
    phaseLabel10_2.grid(column=0, row=2+row_adj, padx=15, pady=5)
    fromLabel10_2.grid(column=1,row=2+row_adj)
    spin10_E_2.grid(column=2,row=2+row_adj)
    label10_h0_2.grid(column=3,row=2+row_adj)
    spin10_F_2.grid(column=4,row=2+row_adj)
    label10_m0_2.grid(column=5,row=2+row_adj)
    space10_2.grid(column=6,row=2+row_adj)
    date10_2_entry.grid(column=11, row=2+row_adj)
    label10_d_2.grid(column=8,row=2+row_adj)
    month10_2_entry.grid(column=9, row=2+row_adj)
    label10_m_2.grid(column=10,row=2+row_adj)
    year10_2_entry.grid(column=7, row=2+row_adj) # ISO format
    space10_2_2.grid(column=12,row=2+row_adj,padx=5)
    rad10_A_2.grid(column=13, row=2+row_adj, pady=5)
    lbl10_A_2.grid(column=14, row=2+row_adj, pady=5)
    spin10_A_2.grid(column=15,row=2+row_adj, pady=5)
    label10_h1_2.grid(column=16,row=2+row_adj, pady=5)
    spin10_B_2.grid(column=17,row=2+row_adj, pady=5)
    label10_m1_2.grid(column=18,row=2+row_adj, pady=5)
    lbl10_B_2.grid(column=19, row=2+row_adj, pady=5)
    spin10_C_2.grid(column=20,row=2+row_adj, pady=5)
    label10_h2_2.grid(column=21,row=2+row_adj, pady=5)
    spin10_D_2.grid(column=22,row=2+row_adj, pady=5)
    label10_m2_2.grid(column=23,row=2+row_adj, pady=5)
    rad10_B_2.grid(column=24, row=2+row_adj, padx=15, pady=5)
    rad10_C_2.grid(column=25, row=2+row_adj, pady=5)
        # phase 3
    phaseLabel10_3 = Label(tab10, text='Phase 3')
    fromLabel10_3 = Label(tab10, text='From:')
    space10_3 = Label(tab10, text=' ')
    spin10_E_3 = Spinbox(tab10, from_=00, to=24, width=3, format='%02.0f')
    spin10_F_3 = Spinbox(tab10, from_=00, to=59, width=3, format='%02.0f')
    spin10_E_3.delete(0,'end')
    spin10_E_3.insert(0,'07')
    spin10_F_3.delete(0,'end')
    spin10_F_3.insert(0,'00')
    label10_h0_3 = Label(tab10, text=':')
    label10_m0_3 = Label(tab10, text='')
    date10_3_entry = Spinbox(tab10, from_=00, to=31, width=3, format='%02.0f')
    month10_3_entry = Spinbox(tab10, from_=00, to=12, width=3, format='%02.0f')
    year10_3_entry = Spinbox(tab10, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase3 = day_phase2 + datetime.timedelta(days=21) # calculate dates for 21 days after recording initiation
    date10_3_entry.delete(0,'end')
    date10_3_entry.insert(0,'{:02d}'.format(day_phase3.day))
    month10_3_entry.delete(0,'end')
    month10_3_entry.insert(0,'{:02d}'.format(day_phase3.month))
    year10_3_entry.delete(0,'end')
    year10_3_entry.insert(0,day_phase3.year)
    label10_d_3 = Label(tab10, text= '/')
    label10_m_3 = Label(tab10, text= '/')
    rad10_A_3 = Radiobutton(tab10, text='LD', variable=var10_3, value=1)
    lbl10_A_3 = Label(tab10, text= 'On:')
    spin10_A_3 = Spinbox(tab10, from_=00, to=24, width=3, format='%02.0f')
    spin10_B_3 = Spinbox(tab10, from_=00, to=59, width=3, format='%02.0f')
    spin10_A_3.delete(0,'end')
    spin10_A_3.insert(0,'07')
    spin10_B_3.delete(0,'end')
    spin10_B_3.insert(0,'00')
    label10_h1_3 = Label(tab10, text=':')
    label10_m1_3 = Label(tab10, text='')
    lbl10_B_3 = Label(tab10, text= 'Off:')
    spin10_C_3 = Spinbox(tab10, from_=00, to=24, width=3, format='%02.0f')
    spin10_D_3 = Spinbox(tab10, from_=00, to=59, width=3, format='%02.0f')
    spin10_C_3.delete(0,'end')
    spin10_C_3.insert(0,'19')
    spin10_D_3.delete(0,'end')
    spin10_D_3.insert(0,'00')
    label10_h2_3 = Label(tab10, text=':')
    label10_m2_3 = Label(tab10, text='')
    rad10_B_3 = Radiobutton(tab10, text='DD', variable=var10_3, value=2)
    rad10_C_3 = Radiobutton(tab10, text='LL', variable=var10_3, value=3)
    phaseLabel10_3.grid(column=0, row=3+row_adj, padx=15, pady=5)
    fromLabel10_3.grid(column=1,row=3+row_adj)
    spin10_E_3.grid(column=2,row=3+row_adj)
    label10_h0_3.grid(column=3,row=3+row_adj)
    spin10_F_3.grid(column=4,row=3+row_adj)
    label10_m0_3.grid(column=5,row=3+row_adj)
    space10_3.grid(column=6,row=3+row_adj)
    date10_3_entry.grid(column=11, row=3+row_adj)
    label10_d_3.grid(column=8,row=3+row_adj)
    month10_3_entry.grid(column=9, row=3+row_adj)
    label10_m_3.grid(column=10,row=3+row_adj)
    year10_3_entry.grid(column=7, row=3+row_adj) # ISO format
    rad10_A_3.grid(column=13, row=3+row_adj, pady=5)
    lbl10_A_3.grid(column=14, row=3+row_adj, pady=5)
    spin10_A_3.grid(column=15,row=3+row_adj, pady=5)
    label10_h1_3.grid(column=16,row=3+row_adj, pady=5)
    spin10_B_3.grid(column=17,row=3+row_adj, pady=5)
    label10_m1_3.grid(column=18,row=3+row_adj, pady=5)
    lbl10_B_3.grid(column=19, row=3+row_adj, pady=5)
    spin10_C_3.grid(column=20,row=3+row_adj, pady=5)
    label10_h2_3.grid(column=21,row=3+row_adj, pady=5)
    spin10_D_3.grid(column=22,row=3+row_adj, pady=5)
    label10_m2_3.grid(column=23,row=3+row_adj, pady=5)
    rad10_B_3.grid(column=24, row=3+row_adj, padx=15, pady=5)
    rad10_C_3.grid(column=25, row=3+row_adj, pady=5)
    btn10.grid(column=0, row=4+row_adj, padx=25, pady=5, columnspan='2', sticky='w')
    btnAll10.grid(column=1, row=4+row_adj, pady=5, columnspan='1', sticky='w')
    tab_control.pack(expand=1, fill='both')
    box10sched_stat.grid(column=3, row=4+row_adj, columnspan='8', sticky='w')
    window.update_idletasks()
    tab10_title2 = Label(tab10, text= 'Recording status', anchor='center')
    tab10_title2.grid(column=0, row= row_adj+6, columnspan='27', sticky='we')
    box10rec_text=StringVar()
    box10rec_text.set('Recording not started yet.')
    box10rec_stat=Label(tab10, textvariable=box10rec_text, anchor='center', justify=LEFT)
    box10rec_stat.grid(column=0, row= row_adj+7, columnspan='27', sticky='we')
    window.update_idletasks()

    ### Main loop
    window.mainloop()
