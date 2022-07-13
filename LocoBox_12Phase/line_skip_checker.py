import nltk
from datetime import datetime
import pandas as pd

import time     # Required for using delay functions

#nltk.download('punkt')
#datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
times = []

with open('LocoBox_12Phase/BOXL1-L5-20210502.txt') as f:
    for _ in range(51):
        next(f)
    for line in f:
        token_line = nltk.word_tokenize(line)
        if token_line == []:
            next(f)
        else:
            times.append(datetime.strptime(token_line[0], '%H:%M:%S'))
            #print(token_line[0])

times1 = times[1:]
times2 = times[:-1]

intervals = []

for a,b in zip(times1, times2):
    interv = a-b
    intervals.append(pd.Timedelta(interv).total_seconds())



irregular_intervals = []
for i, interval in enumerate(intervals):
    if interval > 60:
        irregular_intervals.append((i,interval)) #tuple of the index in the original



irr_interval_diffs = []
for i in range(len(irregular_intervals)-1):
    diff =  irregular_intervals[i+1][0] - irregular_intervals[i][0]
    
    irr_interval_diffs.append(diff)

print(irr_interval_diffs)


