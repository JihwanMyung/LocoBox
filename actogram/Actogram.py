#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pylab as plt

from matplotlib import style
from matplotlib.colors import ListedColormap
from matplotlib.pyplot import figure
from matplotlib.widgets import Slider

style.use('seaborn-colorblind')

pd.set_option("display.max_rows", None)



def plot_doubleplot(box, pir, led, filename):
    

    df = pd.read_table(filename, sep='\s+',
                    skiprows=23, index_col=None)
    df.index = pd.to_datetime(df['MO/DY/YEAR']+' ' + df['HH:MM:SS'],
                            format="%m/%d/%Y %H:%M:%S")
    df0 = pd.DataFrame(
        {'HH:MM:SS': ['00:00:00'],  'MO/DY/YEAR':  [df['MO/DY/YEAR'][0]],
        'LED01': [0], 'PIR01': [0], 'LED02': [0], 'PIR02': [0], 'LED03': [0], 'PIR03': [0], 'LED04': [0], 'PIR04': [0], 'LED05': [0], 'PIR05': [0], 'LED06': [0], 'PIR06': [0], 'LED07': [0], 'PIR07': [0], 'LED08': [0], 'PIR08': [0], 'LED09': [0], 'PIR09': [0], 'LED10': [0], 'PIR10': [0]
        })
    df0.index = pd.to_datetime(df0['MO/DY/YEAR']+' ' + df0['HH:MM:SS'],
                            format="%m/%d/%Y %H:%M:%S")

    #df0 = df0.groupby(np.arange(len(df0))//60).mean() 

    df1 = pd.DataFrame(
        {'HH:MM:SS': df['HH:MM:SS'][0],  'MO/DY/YEAR':  [df['MO/DY/YEAR'][0]],
        'LED01': [0], 'PIR01': [0], 'LED02': [0], 'PIR02': [0], 'LED03': [0], 'PIR03': [0], 'LED04': [0], 'PIR04': [0], 'LED05': [0], 'PIR05': [0], 'LED06': [0], 'PIR06': [0], 'LED07': [0], 'PIR07': [0], 'LED08': [0], 'PIR08': [0], 'LED09': [0], 'PIR09': [0], 'LED10': [0], 'PIR10': [0]
        })
    df1.index = pd.to_datetime(df1['MO/DY/YEAR']+' ' + df1['HH:MM:SS'],
                            format="%m/%d/%Y %H:%M:%S")
    # df1.index.set_value(df1.index, df1.index[0], pd.Timestamp(
    #     df1.index.date[0].year, df1.index.date[0].month, df1.index.date[0].day, df1.index.time[0].hour, df1.index.time[0].minute-1, df1.index.time[0].second))

    #df1 = df1.groupby(np.arange(len(df1))//60).mean() 

    df2 = pd.DataFrame(
        {'HH:MM:SS': ['00:00:00'],  'MO/DY/YEAR':  [df['MO/DY/YEAR'][-1]],
        'LED01': [0], 'PIR01': [0], 'LED02': [0], 'PIR02': [0], 'LED03': [0], 'PIR03': [0], 'LED04': [0], 'PIR04': [0], 'LED05': [0], 'PIR05': [0], 'LED06': [0], 'PIR06': [0], 'LED07': [0], 'PIR07': [0], 'LED08': [0], 'PIR08': [0], 'LED09': [0], 'PIR09': [0], 'LED10': [0], 'PIR10': [0]
        })
    df2.index = pd.to_datetime(df2['MO/DY/YEAR']+' ' + df2['HH:MM:SS'],
                            format="%m/%d/%Y %H:%M:%S")
    # df2.index.set_value(df2.index, df2.index[0], pd.Timestamp(
    #     df2.index.date[0].year, df2.index.date[0].month, df2.index.date[0].day, 23, 59, 0))

    #df2 = df2.groupby(np.arange(len(df2))//60).mean() 

    df3 = pd.DataFrame(
        {'HH:MM:SS': df['HH:MM:SS'][-1],  'MO/DY/YEAR':  [df['MO/DY/YEAR'][-1]],
        'LED01': [0], 'PIR01': [0], 'LED02': [0], 'PIR02': [0], 'LED03': [0], 'PIR03': [0], 'LED04': [0], 'PIR04': [0], 'LED05': [0], 'PIR05': [0], 'LED06': [0], 'PIR06': [0], 'LED07': [0], 'PIR07': [0], 'LED08': [0], 'PIR08': [0], 'LED09': [0], 'PIR09': [0], 'LED10': [0], 'PIR10': [0]
        })
    df3.index = pd.to_datetime(df3['MO/DY/YEAR']+' ' + df3['HH:MM:SS'],
                            format="%m/%d/%Y %H:%M:%S")
    # df3.index.set_value(df3.index, df3.index[0], pd.Timestamp(
    #     df3.index.date[0].year, df3.index.date[0].month, df3.index.date[0].day, df3.index.time[0].hour, df3.index.time[0].minute+1, df3.index.time[0].second))

    #df3 = df3.groupby(np.arange(len(df3))//60).mean() 


    df = pd.concat([df0, df1, df, df3, df2])
    #df = df.groupby(np.arange(len(df))//60).mean() 
    dategroup = df.groupby(pd.Grouper(freq='D'))
    

    k = 0
    df2 = pd.DataFrame()
    for name, group in dategroup:
        if k >= 1:
            a = group
            df2 = pd.concat([df2, a], axis=0)
        k = k+1

    # Remove the marginsclear
    dategroup2 = df2.groupby(pd.Grouper(freq='D'))
    plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
    plt.rcParams['axes.xmargin'] = 0.
    plt.rcParams['axes.ymargin'] = 0.1
    #plt.rcParams['xtick.direction'] = 'out'
    plt.rcParams['axes.linewidth'] = 0.5 # axis thickness
    plt.rcParams['font.family'] = ['sans serif']
    plt.rcParams['font.size'] = 10

    n_group = dategroup.ngroups

    fig, axes = plt.subplots(nrows=n_group, ncols=2)

    # Half-opaque grayscale colormap 
    # by Bart https://stackoverflow.com/questions/37327308/add-alpha-to-an-existing-matplotlib-colormap
    cmap = plt.cm.gray
    my_cmap = cmap(np.arange(cmap.N))
    my_cmap[:,-1] = np.linspace(0.2, 1, cmap.N)
    my_cmap = ListedColormap(my_cmap)

    # scale to 1000 if max PIR is 60
    scale = 1000/max(group[pir])

    # Double-plot actogram
    # Plot the 1st column
    j = 0
    for name, group in dategroup:
       
        labels = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]
        (group[pir]*scale).plot.area(ax=axes[j, 0], sharey=True, cmap='gray', figsize=(4.5, 0.2*n_group))
        ((1-group[led])*800).plot.area(linewidth=0, ax=axes[j, 0],
                                cmap=my_cmap, sharey=True)
        axes[j, 0].axes.set_yticklabels([])
        axes[j, 0].axes.set_yticks([])
        #axes[j, 0].axes.set_xticks(range(1,18))
        axes[j, 0].axes.set_xticklabels(labels, rotation=0, size=8.5)
        axes[j, 0].axes.set_ylim(1,800)
        axes[j, 0].axes.set_xlabel('Hour of day', rotation=0, size=8.5)
        axes[j, 0].axes.set_ylabel(
            str(group[pir].index.date[0].month) + '/' + str(group[pir].index.date[0].day) + ' ', rotation=0, size=9)
        axes[j, 0].yaxis.set_label_coords(-0.125,0.0)
        if j < n_group-1:
            x_axis = axes[j, 0].axes.get_xaxis()
            x_axis.set_visible(False)
        j = j+1
    # Plot the 2nd column
    i = 0
    for name, group in dategroup2:
        (group[pir]*scale).plot.area(ax=axes[i, 1], sharey=True, cmap='gray', figsize=(4.3, 0.2*n_group))
        ((1-group[led])*800).plot.area(linewidth=0,
                                cmap=my_cmap, ax=axes[i, 1], sharey=True)
        x_axis = axes[i, 1].axes.get_xaxis()
        x_axis.set_visible(False)
        axes[i, 1].axes.set_ylim(1,800)
        y_axis = axes[i, 1].axes.get_yaxis()
        y_axis.set_visible(False)
        i = i+1

    fig.subplots_adjust(left=0.12, right=0.9, bottom=0.3, wspace=0, hspace=0)
    plt.axis('off')
    plt.suptitle(box, size=9)
    #plt.savefig(box+'.png')
    #plt.show()
    return fig 




box = 'BOX2'
pir = 'PIR02'
led = 'LED02'

filename = '/home/zow/LocoBox/actogram/BOX1-3-20181018.txt'

#plot_doubleplot(box, pir, led, filename)