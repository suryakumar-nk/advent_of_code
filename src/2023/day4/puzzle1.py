import os

here = os.path.dirname(os.path.abspath(__file__))  # this "__file__" will return the same directiory of the python file.
filepath = os.path.join(here, 'input.txt')
f = open(filepath, "r")

sum = 0
for line in f:
    line = line.split(":")[1].strip()
    card = list(map(int, line.split("|")[0].strip().split()))
    cards = list(map(int, line.split("|")[1].strip().split()))
    total = 0
    soo = 0
    for i in card:
        if (cards.count(i) > 0):
            soo = soo+1
            if (total == 0): total = 1
            else: total = total*2
    sum = sum + total
    print(soo)
print(sum)