import os

here = os.path.dirname(os.path.abspath(__file__))  # this "__file__" will return the same directiory of the python file.
filepath = os.path.join(here, 'input.txt')
f = open(filepath, "r")

puzzle_input = f.readlines()
count = 0
cardMultiply = [1 for _ in puzzle_input]

for line in puzzle_input:
    line1 = line.split(':')[0].strip().split(" ")
    card_no = int(line1[len(line1)-1])
    line = line.split(":")[1].strip()
    card = list(map(int, line.split("|")[0].strip().split()))
    cards = list(map(int, line.split("|")[1].strip().split()))
    
    win_count = 0
    for i in card:
        if (cards.count(i) > 0):
            win_count += 1
    
    for i in range(card_no, card_no+win_count):
        cardMultiply[i] += cardMultiply[card_no-1]
    count += cardMultiply[card_no-1]

print(sum(cardMultiply))
print(count)