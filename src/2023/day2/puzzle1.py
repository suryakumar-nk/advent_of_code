import os

here = os.path.dirname(os.path.abspath(__file__))  # this "__file__" will return the same directiory of the python file.
filepath = os.path.join(here, 'input.txt')
f = open(filepath, "r")

sum_of_ids = 0
for line in f:
    game = line.split(":")[0]
    gameId = game.split(" ")[1]
    flag = False
    for cubes in line.split(":")[1].split(";"):
        for cube in cubes.split(","):
            num = int(cube.split(" ")[1])
            if (cube.endswith("green") or cube.endswith("green\n")):
                if (num > 13): flag = True
            if (cube.endswith("red") or cube.endswith("red\n")):
                if (num > 12): flag = True
            if (cube.endswith("blue") or cube.endswith("blue\n")):
                if (num > 14): flag = True
            if (flag == True): break
        if (flag == True): break
    if (flag == False): sum_of_ids = sum_of_ids + int(gameId)
print("        ")
print("total = ", sum_of_ids)