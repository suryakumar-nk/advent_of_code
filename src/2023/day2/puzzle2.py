import os

here = os.path.dirname(os.path.abspath(__file__))  # this "__file__" will return the same directiory of the python file.
filepath = os.path.join(here, 'input.txt')
f = open(filepath, "r")

total = 0
for line in f:
    red, green, blue = 0, 0, 0
    for cubes in line.split(":")[1].split(";"):
        for cube in cubes.split(","):
            num = int(cube.split(" ")[1])
            if (cube.endswith("green") or cube.endswith("green\n")):
                if (num > green): green = num
            if (cube.endswith("red") or cube.endswith("red\n")):
                if (num > red): red = num
            if (cube.endswith("blue") or cube.endswith("blue\n")):
                if (num > blue): blue = num
    total = total + (green * blue * red)
print(total)