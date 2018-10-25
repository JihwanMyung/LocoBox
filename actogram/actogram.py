#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import matplotlib
import matplotlib.animation as animation
from matplotlib import style
style.use('seaborn')

df = pd.read_table('test.txt', sep='\s+', skiprows=23, index_col=None)

df.index = pd.to_datetime(df['MO/DY/YEAR']+' ' + df['HH:MM:SS'],
                          format="%m/%d/%Y %H:%M:%S")

fig, axes = plt.subplots(nrows=5, ncols=1)
dategroup = df.groupby(pd.Grouper(freq='D'))
j = 0
for name, group in dategroup:
    group['PIR01'].plot.area(ax=axes[j])
    (group['LED01']*50).plot.area(linewidth=0,
                                  colormap="Pastel1", ax=axes[j])
    j = j+1

axes[0].set_title('BOX1')
plt.show()

# group = dategroup.groups
# value = group.values
# print(group)

# df['PIR01'].groupby(pd.Grouper(freq='D')).plot(
#     subplots=True, sharex=True, sharey=False)
# (df['LED01']*60).groupby(pd.Grouper(freq='D')).plot.area(
#     subplots=True, linewidth=0, colormap="Pastel1")


# match_datestamp = "10/12/2018"
# print(df.loc[(df.index.strftime("%m/%d/%Y") == match_datestamp)])

# for dates in df.index.date:
#     data_date = df

# print(df.index.date)
# df['PIR01'].plot(subplots=True, legend=None)
# plt.show()
