
# coding: utf-8

import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import matplotlib
import matplotlib.animation as animation


plt.ion()
fig, ax = plt.subplots()
while True:
    df = pd.read_table('test1.txt', sep='\s+', skiprows=23, index_col=None)
    df.index = pd.to_datetime(df['MO/DY/YEAR']+' ' + df['HH:MM:SS'],
                              format="%m/%d/%Y %H:%M:%S")
    df.plot(subplots=True, legend=None, ax=ax)
    plt.draw()
    plt.pause(3)

plt.show()
