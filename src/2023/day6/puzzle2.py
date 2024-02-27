import os
import re

here = os.path.dirname(os.path.abspath(__file__))  # this "__file__" will return the same directiory of the python file.
filepath = os.path.join(here, 'input.txt')
f = open(filepath, "r")
timeArr = f.readline().split(":")[1].strip()
timeArr = re.sub(r'\s+', ' ', timeArr).split(" ")
time = ''
for i in timeArr:
    time+=i
time = int(time)
distanceArr = f.readline().split(":")[1].strip()
distanceArr = re.sub(r'\s+', ' ', distanceArr).split(" ")
distance = ''
for i in distanceArr:
    distance+=i
distance = int(distance)
print(time)
print(distance)

wins = 0
for j in range(1, time+1):
    dis = j*(time-j)
    if (dis > distance):
        wins+=1
print(wins)