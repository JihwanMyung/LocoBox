
# coding: utf-8

import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import matplotlib
import matplotlib.animation as animation
import datetime as dt
import matplotlib.dates as md
from numpy import arange


y_stepsize = 10

plt.ion()
fig, ax = plt.subplots()
ax.set_yticks(np.arange(1.0, 50.0, y_stepsize))
ax.xaxis.set_major_locator(md.DayLocator())
ax.xaxis.set_minor_locator(md.HourLocator(arange(0, 25, 1)))
ax.xaxis.set_minor_formatter(md.DateFormatter('%H:%M:%S'))
ax.xaxis.set_major_formatter(md.DateFormatter('%m/%d/%Y'))

i = 1
while True:
    df = pd.read_table('test3.txt', sep='\s+', skiprows=12, index_col=None)
    # print(df)
    df.index = pd.to_datetime(df['MO/DY/YEAR']+' ' + df['HH:MM:SS'],
                              format="%m/%d/%Y %H:%M:%S")
    # df['PIR01'][:i].plot(ax = ax)
    x = df.index[:i]
    y = df['PIR01'][:i]
    ax.plot(x, y)
    plt.draw()
    plt.savefig('gif/books_read'+str(i)+'.png')
    plt.pause(0.2)
    i += 1


plt.show()
