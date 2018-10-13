import json

with open('BOX1-sched-20181013.json') as data_file:
    data = json.load(data_file)

print(data['hourOn1_1'])
