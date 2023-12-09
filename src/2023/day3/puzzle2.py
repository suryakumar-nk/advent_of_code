import os

here = os.path.dirname(os.path.abspath(__file__))  # this "__file__" will return the same directiory of the python file.
filepath = os.path.join(here, 'input.txt')
f = open(filepath, "r")

engine = f.read().split("\n")
sum = 0
height, width = len(engine), len(engine[0])

def findLeftNumber(i:int, j:int):
    num = ''
    k = 1
    while(j-k > -1):
        if (engine[i][j-k].isdigit()):
            num = num + engine[i][j-k]
            k = k+1
        else:
            break
    return num[::-1]

def findRightNumber(i:int, j:int):
    num = ''
    k = 1
    while(j+k < width):
        if (engine[i][j+k].isdigit()):
            num = num + engine[i][j+k]
            k=k+1
        else:
            break
    return num

def findNumber(i:int, j:int):
    leftnum = findLeftNumber(i, j)
    rightnum = findRightNumber(i, j)
    if (engine[i][j].isdigit()):
        return [leftnum + engine[i][j] + rightnum]
    nums = []
    if (leftnum != ''):
        nums.append(leftnum)
    if (rightnum != ''):
        nums.append(rightnum)
    return nums

        
for i in range(0, height):
    for j in range(0, width):
        if (engine[i][j] == '*'):
            nums = []
            if (i!=0):
                list = findNumber(i-1, j)
                if (len(list) > 0):
                    nums = nums + list
            if (i!=(height-1)):
                list = findNumber(i+1, j)
                if (len(list) > 0):
                    nums = nums + list
            if (j!=0):
                num = findLeftNumber(i,j)
                if (num != ''):
                    nums.append(num)
            if (j!=(width-1)):
                num = findRightNumber(i,j)
                if (num != ''):
                    nums.append(num)
            if (len(nums) > 1):
                total = 1
                for num in nums:
                    total = total*int(num)
                sum = sum + total
print(sum)

