import os
import re

here = os.path.dirname(os.path.abspath(__file__))  # this "__file__" will return the same directiory of the python file.
filepath = os.path.join(here, 'input.txt')
f = open(filepath, "r")
timeArr = f.readline().split(":")[1].strip()
timeArr = re.sub(r'\s+', ' ', timeArr).split(" ")
timeArr = [int(num) for num in timeArr]
distanceArr = f.readline().split(":")[1].strip()
distanceArr = re.sub(r'\s+', ' ', distanceArr).split(" ")
distanceArr = [int(num) for num in distanceArr]
print(timeArr)
print(distanceArr)

result = 1
for i in range(len(timeArr)):
    time = timeArr[i]
    distance = distanceArr[i]
    wins = 0
    for j in range(1, time+1):
        dis = j*(time-j)
        if (dis > distance):
            wins+=1
    print(wins)
    result*=wins
print(result)
