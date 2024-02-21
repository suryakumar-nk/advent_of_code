import os

here = os.path.dirname(os.path.abspath(__file__))  # this "__file__" will return the same directiory of the python file.
filepath = os.path.join(here, 'input.txt')
f = open(filepath, "r")

seeds = f.readline().split(':')[1].strip().split(' ')
# print(seeds)
seedToSoilMap = []
soilToFertilizerMap = []
fertilizerToWaterMap = []
waterToLightMap = []
lightToTempratureMap = []
tempratureToHumidityMap = []
humidityToLocationMap = []
maps = {
    1 : seedToSoilMap,
    2 : soilToFertilizerMap,
    3 : fertilizerToWaterMap,
    4 : waterToLightMap,
    5 : lightToTempratureMap,
    6 : tempratureToHumidityMap,
    7 : humidityToLocationMap
}


k = 0
currentMap = []
for i in f.readlines():
    if(i != '\n'):
        if (i.count(':') == 1):
            continue
        designation = int(i.split(" ")[0])
        source = int(i.split(" ")[1])
        scale = int(i.split(' ')[2].strip('\n'))
        currentMap.append([source, designation, scale])
    else:
        k+=1
        currentMap = maps.get(k)

def getDesignation(maps, key):
    des = -1
    for arr in maps:
        if (key >= arr[0] and key < (arr[0]+arr[2])):
            des = arr[1] + key - arr[0]
            break
    if (des == -1):
        des = key
    return des

print(seeds)
result = -1
for seed in seeds:
    soil = getDesignation(seedToSoilMap, int(seed))
    fertilizer = getDesignation(soilToFertilizerMap, soil)
    water = getDesignation(fertilizerToWaterMap, fertilizer)
    light = getDesignation(waterToLightMap, water)
    temprature = getDesignation(lightToTempratureMap, light)
    humidity = getDesignation(tempratureToHumidityMap, temprature)
    location = getDesignation(humidityToLocationMap, humidity)
    if (result == -1):
        result = location
    elif (location < result):
        result = location
    print('seed', seed, ', soil', soil,', fertilizer', fertilizer,', water', water,', light', light,
          ', temprature', temprature, ', humidity', humidity, ', location', location)
print("Minimum location", result)