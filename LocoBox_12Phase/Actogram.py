#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from matplotlib import style
from matplotlib.colors import ListedColormap
from matplotlib.pyplot import figure
import matplotlib.dates as mdates

style.use('seaborn-colorblind')
pd.set_option("display.max_rows", None)


"""
This will plot a initial plot when the software just starts
"""
def init_plot():
    fig = plt.figure(figsize=(2, 2))  
    fig.suptitle("No data")
    plt.savefig('./init.png')

"""
This will make a new image of the defined BOX data whenever the user click refresh plot from the python GUI
"""
def plot_doubleplot(box, pir, led, filename):

    number_of_skipped_lines = 0

    try:
        fo = open(filename, "r")

    except:
        raise Exception("Cannot open " + filename)

    for line in fo:
        
        if "HH:MM:SS" in line:
            break

        else:
            number_of_skipped_lines += 1 
    fo.close()

#determine number of rows to skip 
    try:
        df = pd.read_table(filename, sep='\s+', skip_blank_lines=True,
                     skiprows=number_of_skipped_lines, index_col=None)

    except Exception as e:
        print(e)
        fig = plt.figure(figsize=(2, 2))  
        fig.suptitle("No data")
        plt.savefig('./' + box + '.png')
        print("finished plotting " + box)

    if df.empty:
        print("empty table")
        fig = plt.figure(figsize=(2, 2))  
        fig.suptitle("No data")
        plt.savefig('./' + box + '.png')
        print("finished plotting " + box)
        
    else: 

        df = df.iloc[-10080:]

        df.index = pd.to_datetime(df['MO/DY/YEAR']+' ' + df['HH:MM:SS'],
                                format="%m/%d/%Y %H:%M:%S")

        dategroup = df.groupby(pd.Grouper(freq='D'))
        
        k = 0
        df2 = pd.DataFrame()
        for name, group in dategroup:
            if k >= 1:
                a = group
                df2 = pd.concat([df2, a], axis=0)
            k = k+1

        # Remove the marginsclear
        try:
            dategroup2 = df2.groupby(pd.Grouper(freq='D'))

        except:
            print("Only data for day 1")

        plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
        plt.rcParams['axes.xmargin'] = 0.
        plt.rcParams['axes.ymargin'] = 0.1
        plt.rcParams['axes.linewidth'] = 0.5 # axis thickness
        plt.rcParams['font.family'] = ['sans serif']
        plt.rcParams['font.size'] = 10

        n_group = dategroup.ngroups
        ### Double-plot actogram
        fig = plt.figure()
        
        # if there is only data from day 1, plot only one column
        if n_group == 1:
            axes = fig.subplots(nrows=n_group, ncols=1)

            # Half-opaque grayscale colormap 
            # by Bart https://stackoverflow.com/questions/37327308/add-alpha-to-an-existing-matplotlib-colormap
            cmap = plt.cm.gray
            my_cmap = cmap(np.arange(cmap.N))
            my_cmap[:,-1] = np.linspace(0.2, 1, cmap.N)
            my_cmap = ListedColormap(my_cmap)

            # scale to 1000 if max PIR is 60
            max_val=np.clip(max(group[pir]), a_min=1, a_max=max(group[pir]))
            scale = 1000/max_val

            # Plot the 1st column
            j = 0
            for name, group in dategroup:
            
                (group[pir]*scale).plot.area(ax=axes, sharey=True, sharex=True, cmap='gray', figsize=(3, 0.2*n_group))
                ((1-group[led])*1000).plot.area(linewidth=0, ax=axes,
                                        cmap=my_cmap, sharey=True, sharex=True)
                axes.axes.set_yticklabels([])
                axes.axes.set_yticks([])
                loc = mdates.HourLocator(interval=12)
                axes.xaxis.set_major_locator(loc)
                fmt = mdates.DateFormatter("%H")
                axes.xaxis.set_major_formatter(fmt)
                axes.axes.set_ylim(1,1000)
                axes.axes.set_ylabel(
                    str(group[pir].index.date[0].month) + '/' + str(group[pir].index.date[0].day) + ' ', rotation=0, size=9)
                
                axes.axes.set_xlim([pd.to_datetime(group['MO/DY/YEAR'][0]+' ' + '00:00:00',
                                    format="%m/%d/%Y %H:%M:%S"), pd.to_datetime(group['MO/DY/YEAR'][0]+' ' + '23:59:00',
                                    format="%m/%d/%Y %H:%M:%S")])
                axes.yaxis.set_label_coords(-0.125,0.0)
                j = j+1

            fig.subplots_adjust(left=0.12, right=0.9,  bottom=0.2, wspace=0, hspace=0)
            plt.axis('off')
            plt.suptitle(box, size=8)
            plt.savefig('./' + box + '.png')
            print("finished plotting x" + box)

        # plot two columns when there are enough data
        elif n_group>1: 
            axes = fig.subplots(nrows=n_group, ncols=2)

            # Half-opaque grayscale colormap 
            # by Bart https://stackoverflow.com/questions/37327308/add-alpha-to-an-existing-matplotlib-colormap
            cmap = plt.cm.gray
            my_cmap = cmap(np.arange(cmap.N))
            my_cmap[:,-1] = np.linspace(0.2, 1, cmap.N)
            my_cmap = ListedColormap(my_cmap)

            # scale to 1000 if max PIR is 60
            max_val=np.clip(max(group[pir]), a_min=1, a_max=max(group[pir]))
            scale = 1000/max_val

            # Plot the 1st column    
            j = 0
            for name, group in dategroup:
                (group[pir]*scale).plot.area(ax=axes[j, 0], sharey=True, sharex=True, cmap='gray', figsize=(3, 0.2*n_group))
                ((1-group[led])*800).plot.area(linewidth=0, ax=axes[j, 0],
                                        cmap=my_cmap, sharey=True, sharex=True)
                axes[j, 0].axes.set_yticklabels([])
                axes[j, 0].axes.set_yticks([])
                loc = mdates.HourLocator(interval=12)
                axes[j, 0].xaxis.set_major_locator(loc)
                fmt = mdates.DateFormatter("%H")
                axes[j, 0].xaxis.set_major_formatter(fmt)
                axes[j, 0].axes.set_ylim(1,800)
                axes[j, 0].axes.set_ylabel(
                    str(group[pir].index.date[0].month) + '/' + str(group[pir].index.date[0].day) + ' ', rotation=0, size=9)
                
                axes[j, 0].axes.set_xlim([pd.to_datetime(group['MO/DY/YEAR'][0]+' ' + '00:00:00',
                                    format="%m/%d/%Y %H:%M:%S"), pd.to_datetime(group['MO/DY/YEAR'][0]+' ' + '23:59:00',
                                    format="%m/%d/%Y %H:%M:%S")])
                axes[j, 0].yaxis.set_label_coords(-0.125,0.0)
                if j < n_group-1:
                    x_axis = axes[j, 0].axes.get_xaxis()
                    x_axis.set_visible(False)
                j = j+1

            # Plot the 2nd column
            i = 0
            for name, group in dategroup2:
                (group[pir]*scale).plot.area(ax=axes[i, 1], sharey=True, cmap='gray', figsize=(3, 0.2*n_group))
                ((1-group[led])*800).plot.area(linewidth=0,
                                        cmap=my_cmap, ax=axes[i, 1], sharey=True)
                x_axis = axes[i, 1].axes.get_xaxis()
                x_axis.set_visible(False)
                axes[i, 1].axes.set_ylim(1,800)
                y_axis = axes[i, 1].axes.get_yaxis()
                y_axis.set_visible(False)
                i = i+1

            fig.subplots_adjust(left=0.12, right=0.9,  bottom=0.2, wspace=0, hspace=0)
            plt.axis('off')
            plt.suptitle(box, size=8)
            plt.savefig('./' + box + '.png')
            print("finished plotting " + box)
        
        # This is just for sanity check (when number of groups == 0)
        else: 
            fig = plt.figure(figsize=(2, 2))  
            fig.suptitle("No data")
            plt.savefig('./' + box + '.png')
            print("finished plotting " + box)