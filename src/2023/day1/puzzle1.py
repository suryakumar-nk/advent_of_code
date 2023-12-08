import os

here = os.path.dirname(os.path.abspath(__file__))  # this "__file__" will return the same directiory of the python file.
filepath = os.path.join(here, 'input.txt')
f = open(filepath, "r")

totalSum = 0
for line in f:
    firstnum = 0
    lastnum = 0
    for c in line:
        if (c.isdigit()):
            if (firstnum == 0 and lastnum == 0):
                firstnum = lastnum = int(c)
            else:
                lastnum = int(c)
    totalSum = totalSum + (firstnum*10 + lastnum)
print(totalSum)
