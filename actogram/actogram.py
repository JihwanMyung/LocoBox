#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import matplotlib

df = pd.read_table('test.txt', sep='\s+', skiprows=23, index_col=None)

df.index = pd.to_datetime(df['MO/DY/YEAR']+' ' + df['HH:MM:SS'],
                          format="%m/%d/%Y %H:%M:%S")
df.plot(subplots=True, legend=None)

plt.gcf().axes[0].legend(['LED1'])
plt.gcf().axes[1].legend(['PIR1'])
plt.show()
