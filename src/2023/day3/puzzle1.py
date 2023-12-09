import os

here = os.path.dirname(os.path.abspath(__file__))  # this "__file__" will return the same directiory of the python file.
filepath = os.path.join(here, 'input.txt')
f = open(filepath, "r")

engine = f.read().split("\n")
number = ""
fullDot = True
sum = 0
height, width = len(engine), len(engine[0])
for i in range(0, height):
    for j in range(0, width):
        num = engine[i][j]
        if (num.isdigit()):
            number = number + num
            if (fullDot == False):
                continue
            if (j != 0 and engine[i][j-1].isdigit() == False): #left check
                fullDot = engine[i][j-1] == '.' and fullDot
            if (j != width-1 and engine[i][j+1].isdigit() == False):
                fullDot = engine[i][j+1] == '.' and fullDot
            if (i != 0): # upper line
                fullDot = engine[i-1][j] == '.' and fullDot
                if (j != 0): #upper left
                    fullDot = engine[i-1][j-1] == '.' and fullDot
                if (j != width-1): # upper right
                    fullDot = engine[i-1][j+1] == '.' and fullDot
            if (i != height-1):
                fullDot = engine[i+1][j] == '.' and fullDot
                if (j != 0): #upper left
                    fullDot = engine[i+1][j-1] == '.' and fullDot
                if (j != width-1): # upper right
                    fullDot = engine[i+1][j+1] == '.' and fullDot
        else:
            if (number != '' and fullDot == False):
                sum = sum + int(number)
            number = ''
            fullDot = True
    if (number != '' and fullDot == False):
        sum = sum + int(number)
    number = ''
    fullDot = True
print(sum)