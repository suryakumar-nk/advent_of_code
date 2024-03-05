import os

here = os.path.dirname(os.path.abspath(__file__))  # this "__file__" will return the same directiory of the python file.
filepath = os.path.join(here, 'input.txt')
f = open(filepath, "r")

ways = {}
directions = (f.readline()+f.readline()).strip()
starts = {}

for line in f.readlines():
    path = line.strip().split("=")
    key = path[0].strip()
    value = path[1].strip()
    ways[key] = (value[1:4], value[6:9])
    if (key[2] == 'A'):
        starts[key] = 0
    
for key in list(starts.keys()):
    steps = 0
    flag = 0
    start = key
    while(flag == 0):
        for i in directions:
            start = ways[start][0] if (i == 'L') else ways[start][1]
            steps+=1
            if (start[2] == 'Z'):
                flag = 1
                break
        print(start)
    starts[key] = steps

print(starts)

from functools import reduce

def test(nums):
    return reduce(lambda x, y: lcm(x, y), nums)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print(test(starts.values()))