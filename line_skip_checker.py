import nltk
from datetime import datetime
import pandas as pd
import os



#nltk.download('punkt')
#datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
directory = 'Prev_locobox_data'

for filename in os.listdir(directory):
    times = []
    passed = False

    fullpath = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(fullpath):

        with open(fullpath) as f:
            # for _ in range(51):
            #     next(f)

            
            for line in f:

                token_line = nltk.word_tokenize(line)
                
                if token_line == []:
                    next(f)

                elif passed:
                    times.append(datetime.strptime(token_line[0], '%H:%M:%S'))
                    #print(token_line[0])

                elif 'HH:MM:SS' in line:
                    passed = True
                    for _ in range(2):
                        next(f)

                elif 'HH:MM:SS' not in token_line:
                    #print(token_line[0])
                    for _ in range(2):
                        next(f)
                


                
                

        times1 = times[1:]
        times2 = times[:-1]

        intervals = []

        for a,b in zip(times1, times2):
            interv = a-b
            intervals.append(pd.Timedelta(interv).total_seconds())



        irregular_intervals = []
        for i, interval in enumerate(intervals):
            if interval > 60:
                irregular_intervals.append((i,interval)) #tuple of the index in the original, interval was 120 for all irregulars



        irr_interval_diffs = []
        for i in range(len(irregular_intervals)-1):
            diff =  irregular_intervals[i+1][0] - irregular_intervals[i][0]
            
            irr_interval_diffs.append(diff)

        rawinterval = {'indx_diffe_between_skips': irr_interval_diffs}
        intdf = pd.DataFrame(rawinterval)
        filename = filename[:-4]
        intdf.to_csv('Interval_comparisons/'+filename +'.csv', index=False)

