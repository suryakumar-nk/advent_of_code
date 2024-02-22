import os

here = os.path.dirname(os.path.abspath(__file__))  # this "__file__" will return the same directiory of the python file.
filepath = os.path.join(here, 'input.txt')
f = open(filepath, "r")

seeds = f.readline().split(':')[1].strip().split(' ')
seedToSoilMap = {}
soilToFertilizerMap = {}
fertilizerToWaterMap = {}
waterToLightMap = {}
lightToTempratureMap = {}
tempratureToHumidityMap = {}
humidityToLocationMap = {}
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
currentMap = {}
for i in f.readlines():
    if(i != '\n'):
        if (i.count(':') == 1):
            continue
        designation = int(i.split(" ")[0])
        source = int(i.split(" ")[1])
        scale = int(i.split(' ')[2].strip('\n'))
        currentMap[source] = designation
        currentMap[source+scale-1] = designation+scale-1
    else:
        if (k!=0):
            # currentMap = dict(sorted(currentMap.items()))
            start = list(dict(sorted(currentMap.items())).keys())[0]
            if (start != 0):
                currentMap[0] = 0
                if (start != 1):
                    currentMap[start-1] = start-1
            if ((len(currentMap)%2) != 0):
                end = list(dict(sorted(currentMap.items())).keys())[-1]
                currentMap[end+1] = end+1
        k+=1
        currentMap = maps.get(k)

start = list(dict(sorted(humidityToLocationMap.items())).keys())[0]
if (start != 0):
    humidityToLocationMap[0] = 0
    if (start != 1):
        humidityToLocationMap[start-1] = start-1

seedToSoilMap = dict(sorted(seedToSoilMap.items()))
soilToFertilizerMap = dict(sorted(soilToFertilizerMap.items()))
fertilizerToWaterMap = dict(sorted(fertilizerToWaterMap.items()))
waterToLightMap = dict(sorted(waterToLightMap.items()))
lightToTempratureMap = dict(sorted(lightToTempratureMap.items()))
tempratureToHumidityMap = dict(sorted(tempratureToHumidityMap.items()))
humidityToLocationMap = dict(sorted(humidityToLocationMap.items()))

def getDestination(maps, ranges):
    desRanges = []
    sources = list(maps.keys())
    for range in ranges:
        c = 0
        flag = 0
        while (c < len(sources)):
            a = -1
            b = -1
            if (sources[c] == range[0]):
                a = maps[sources[c]]
            if (range[0] < sources[c+1]):
                a = maps[sources[c]] + range[0] - sources[c]
            if (a == -1):
                c+=2
                continue
            if (range[1] < sources[c+1]):
                b = maps[sources[c+1]] - (sources[c+1] - range[1])
                desRanges.append((a,b))
                flag = 1
                break
            b = maps[sources[c+1]]
            desRanges.append((a,b))
            if (range[1] == sources[c+1]):
                flag = 1
                break
            range = (sources[c+1]+1, range[1])
            c+=2
        if (flag == 0):
            desRanges.append(range)
    return desRanges

k = 0
locations = []
while (k < len(seeds)):
    seedRange = [(int(seeds[k]), int(seeds[k+1])+int(seeds[k])-1)]
    # print('seedranges', seedRange)
    soilRanges = getDestination(seedToSoilMap, seedRange)
    # print('soilRanges', soilRanges)
    fertilizerRanges = getDestination(soilToFertilizerMap, soilRanges)
    # print('fertilizerRanges', fertilizerRanges)
    waterRanges = getDestination(fertilizerToWaterMap, fertilizerRanges)
    # print('waterRanges', waterRanges)
    lightRanges = getDestination(waterToLightMap, waterRanges)
    # print('lightRanges', lightRanges)
    tempratureRanges = getDestination(lightToTempratureMap, lightRanges)
    # print('tempratureRanges', tempratureRanges)
    humidityRanges = getDestination(tempratureToHumidityMap, tempratureRanges)
    # print('humidityRanges', humidityRanges)
    locationRanges = getDestination(humidityToLocationMap, humidityRanges)
    # print('locationRanges', locationRanges)
    k+=2
    for i in locationRanges:
        locations.append(i[0])
        locations.append(i[1])
print(locations)
print(min(locations))
