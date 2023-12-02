import os

here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, 'input.txt')
f = open(filepath, "r")

totalSum = 0
nums = []
for line in f:
    lastnum = None
    firstnum = None
    for i in range(0, len(line)):
        if (line[i].isdigit()):
            if (firstnum == None):
                firstnum = int(line[i])
            lastnum = int(line[i])
            continue
        if (line[i] == 'o'):
            index = line.find("one", i, i+3)
            if (index != -1):
                if (firstnum == None):
                    firstnum = 1
                lastnum = 1
            continue
        if (line[i] == 't'):
            index = line.find("two", i, i+3)
            if (index != -1):
                if (firstnum == None):
                    firstnum = 2
                lastnum = 2
                continue
            index = line.find("three", i, i+5)
            if (index != -1):
                if (firstnum == None):
                    firstnum = 3
                lastnum = 3
                continue
        if (line[i] == 'f'):
            index = line.find("four", i, i+4)
            if (index != -1):
                if (firstnum == None):
                    firstnum = 4
                lastnum = 4
                continue
            index = line.find("five", i, i+4)
            if (index != -1):
                if (firstnum == None):
                    firstnum = 5
                lastnum = 5
                continue
        if (line[i] == 's'):
            index = line.find("six", i, i+3)
            if (index != -1):
                if (firstnum == None):
                    firstnum = 6
                lastnum = 6
                continue
            index = line.find("seven", i, i+5)
            if (index != -1):
                if (firstnum == None):
                    firstnum = 7
                lastnum = 7
                continue
        if (line[i] == 'e'):
            index = line.find("eight", i, i+5)
            if (index != -1):
                if (firstnum == None):
                    firstnum = 8
                lastnum = 8
                continue
        if (line[i] == 'n'):
            index = line.find("nine", i, i+4)
            if (index != -1):
                if (firstnum == None):
                    firstnum = 9
                lastnum = 9
                continue
    totalSum = totalSum + (firstnum*10 + lastnum)
    nums.append(firstnum*10 + lastnum)
# print(totalSum)
# totalSum = 0
# for i in nums:
#     totalSum = totalSum+i

print(totalSum)
print(nums)


# line = "btbcs2rsrcrshzp8six89"
# lastnum = None
# firstnum = None
# # ottffssen
# for i in range(0, len(line)):
#     if (line[i].isdigit()):
#         if (firstnum == None):
#             firstnum = int(line[i])
#         lastnum = int(line[i])
#         continue
#     if (line[i] == 'o'):
#         index = line.find("one", i, i+3)
#         if (index != -1):
#             if (firstnum == None):
#                 firstnum = 1
#             lastnum = 1
#         continue
#     if (line[i] == 't'):
#         index = line.find("two", i, i+3)
#         if (index != -1):
#             if (firstnum == None):
#                 firstnum = 2
#             lastnum = 2
#             continue
#         index = line.find("three", i, i+5)
#         if (index != -1):
#             if (firstnum == None):
#                 firstnum = 3
#             lastnum = 3
#             continue
#     if (line[i] == 'f'):
#         index = line.find("four", i, i+4)
#         if (index != -1):
#             if (firstnum == None):
#                 firstnum = 4
#             lastnum = 4
#             continue
#         index = line.find("five", i, i+4)
#         if (index != -1):
#             if (firstnum == None):
#                 firstnum = 5
#             lastnum = 5
#             continue
#     if (line[i] == 's'):
#         index = line.find("six", i, i+3)
#         if (index != -1):
#             if (firstnum == None):
#                 firstnum = 6
#             lastnum = 6
#             continue
#         index = line.find("seven", i, i+5)
#         if (index != -1):
#             if (firstnum == None):
#                 firstnum = 7
#             lastnum = 7
#             continue
#     if (line[i] == 'e'):
#         index = line.find("eight", i, i+5)
#         if (index != -1):
#             if (firstnum == None):
#                 firstnum = 8
#             lastnum = 8
#             continue
#     if (line[i] == 'n'):
#         index = line.find("nine", i, i+4)
#         if (index != -1):
#             if (firstnum == None):
#                 firstnum = 9
#             lastnum = 9
#             continue
# print(firstnum*10 + lastnum)
