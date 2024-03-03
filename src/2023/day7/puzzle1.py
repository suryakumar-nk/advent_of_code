import os

here = os.path.dirname(os.path.abspath(__file__))  # this "__file__" will return the same directiory of the python file.
filepath = os.path.join(here, 'input.txt')
f = open(filepath, "r")

handsScoreMap = {}
for i in f.readlines():
    handsScoreMap[i.split(" ")[0]] = i.split(" ")[1].strip()

def getCharMap(hand):
    charMap = {}
    for i in hand:
        if i in charMap:
            charMap[i] += 1
        else:
            charMap[i] = 1
    return charMap

def fiveOfKindCheck(val):
    if (val == [5]):
        return True
    return False

def fourOfKindCheck(val):
    if ((val == [1,4]) or (val == [4,1])):
        return True
    return False

def fullHouseCheck(val):
    if ((val == [2,3]) or (val == [3,2])):
        return True
    return False

def threeOfKindCheck(val):
    if ((val == [1,1,3]) or (val == [1,3,1]) or (val == [3,1,1])):
        return True
    return False

def twoPairCheck(val):
    if ((val == [1,2,2]) or (val == [2,2,1]) or (val == [2,1,2])):
        return True
    return False

def onePairCheck(val):
    if ((val == [2,1,1,1]) or (val == [1,2,1,1]) or (val == [1,1,2,1]) or (val == [1,1,1,2])):
        return True
    return False

letters = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']

handsMap = {
    'Five of a kind': {},
    'Four of a kind': {},
    'Full house': {},
    'Three of a kind': {},
    'Two pair': {},
    'One pair': {},
    'High card': {}
}

def addInDic(values, key):
    score = 0
    for i in key:
        score = (score*100)+(letters.index(i)+1)
    if score in values:
        values[score].append(key)
    else:
        values[score] = [key]
    return values

hands = list(handsScoreMap.keys())
for hand in hands:
    charMap = getCharMap(hand=hand)
    val = list(charMap.values())
    if (fiveOfKindCheck(val=val)):
        values = handsMap['Five of a kind']
        handsMap['Five of a kind'] = addInDic(values=values, key=hand)
        continue
    if (fourOfKindCheck(val=val)):
        values = handsMap['Four of a kind']
        handsMap['Four of a kind'] = addInDic(values=values, key=hand)
        continue
    if (fullHouseCheck(val=val)):
        values = handsMap['Full house']
        handsMap['Full house'] = addInDic(values=values, key=hand)
        continue
    if (threeOfKindCheck(val=val)):
        values = handsMap['Three of a kind']
        handsMap['Three of a kind'] = addInDic(values=values, key=hand)
        continue
    if (twoPairCheck(val=val)):
        values = handsMap['Two pair']
        handsMap['Two pair'] = addInDic(values=values, key=hand)
        continue
    if (onePairCheck(val=val)):
        values = handsMap['One pair']
        handsMap['One pair'] = addInDic(values=values, key=hand)
        continue
    values = handsMap['High card']
    handsMap['High card'] = addInDic(values=values, key=hand)

result = 0
rank = 1
keys = list(handsMap.keys())
keys.reverse()
i=0
for key in keys:
    values = handsMap[key]
    weights = list(values.keys())
    weights.sort()
    for weight in weights:
        print(i)
        i+=1
        hands = values[weight]
        if (len(hands) > 1):
            print("duplicate score", hands)
        for hand in hands:
            score = handsScoreMap[hand]
            result+=(int(score)*rank)
            rank+=1
    handsMap[key] = result
    result = 0
print(handsMap)
print(handsMap.values())
print(sum(handsMap.values()))