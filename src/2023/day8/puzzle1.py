import os

here = os.path.dirname(os.path.abspath(__file__))  # this "__file__" will return the same directiory of the python file.
filepath = os.path.join(here, 'input.txt')
f = open(filepath, "r")

ways = {}
directions = (f.readline()+f.readline()).strip()

for line in f.readlines():
    path = line.strip().split("=")
    key = path[0].strip()
    value = path[1].strip()
    ways[key] = (value[1:4], value[6:9])

steps = 0
start = 'AAA'
flag = 0

while(flag == 0):
    for i in directions:
        start = ways[start][0] if (i == 'L') else ways[start][1]
        steps+=1
        if (start == 'ZZZ'):
            flag = 1
            break
    print(start)
        
print(steps)
