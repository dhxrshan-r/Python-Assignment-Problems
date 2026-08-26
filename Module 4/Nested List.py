cities = [ ["Pittsburgh", "Allegheny", 302407],
           ["Philadelphia", "Philadelphia", 1584981],
           ["Allentown", "Lehigh", 123838],
           ["Erie", "Erie", 97639],
           ["Scranton", "Lackawanna", 77182] ]

def getCounty(cities, cityName):
    for i in range(len(cities)):
        entry = cities[i]
        if entry[0] == cityName:
            return entry[1]

def getCounty(cities, cityName):
    for i in range(len(cities)):
        if cities[i][0] == cityName:
            return cities[i][1]
print(getCounty(cities, "Pittsburgh"))
