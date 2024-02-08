"""
  FUNCTIONS:
    getHighestRainfall(param: dict) => return: tuple
    getSmallestRainfall(param: dict) => return: tuple
    getMeanRainfall(param: dict) => return: float
    getCitiesGreaterMean(param: dict, float) => return: int
    main()
"""


def getHighestRainfall(collection):
    highestRainfall = 0
    highestRainfallLocation = None
    for city, rainfall_amt in collection.items():
        if rainfall_amt > highestRainfall:
            highestRainfall = rainfall_amt
            highestRainfallLocation = city
    return highestRainfallLocation, highestRainfall


def getLowestRainfall(collection):
    lowestRainfall = list(collection.values())[0]
    lowestLocationLocation = list(collection.keys())[0]
    for city, rainfall_amt in collection.items():
        if rainfall_amt < lowestRainfall:
            lowestRainfall = rainfall_amt
            lowestLocationLocation = city
    return lowestLocationLocation, lowestRainfall


def getMeanRainfall(collection):
    meanRainfall = 0
    LISTOFRAINFALLVALUES = list(collection.values())
    for rainfall_amt in LISTOFRAINFALLVALUES:
        meanRainfall += rainfall_amt
    meanRainfall = round(meanRainfall / len(LISTOFRAINFALLVALUES), 2)
    return meanRainfall


def getNumCitiesGreaterThanMean(collection, mean):
    numCities = 0
    LISTOFRAINFALLVALUES = list(collection.values())
    for rainfall_amt in LISTOFRAINFALLVALUES:
        if rainfall_amt > mean:
            numCities += 1
    return numCities


def main():
    fileContents = ""
    fileContents_in_cm = ""
    rainfall_collections = {}
    try:
        with open("./rainfall.txt", "r") as f:
            # store file contents in var fileContents
            fileContents = f.read()

            # use dict to correspond place with rainfall amount
            for line in fileContents.split("\n"):
                place_to_rainfall = line.split(" ")

                # convert rainfall from inches to cm
                RAINFALL_IN_CM = round(float(place_to_rainfall[1]) * 2.54, 2)
                # correspond key=place to value=rainfall_amt
                rainfall_collections[place_to_rainfall[0]] = RAINFALL_IN_CM
                # print to console new format
                fileContents_in_cm += f"{place_to_rainfall[0]} {rainfall_collections[place_to_rainfall[0]]}\n"
    except FileNotFoundError:
        print("File not found")

    print(fileContents_in_cm)
    print(f"Highest Rainfall: {getHighestRainfall(rainfall_collections)} (in cm)")
    print(f"Lowest Rainfall: {getLowestRainfall(rainfall_collections)} (in cm)")

    # store mean rainfall in variable for use
    MEANRAINFALL = getMeanRainfall(rainfall_collections)
    print(f"Mean Rainfall: {MEANRAINFALL} (in cm)")
    print(
        f"The total number of cities where rainfall is greater than the mean number of rainfall is: {getNumCitiesGreaterThanMean(rainfall_collections, MEANRAINFALL)} cities"
    )


main()
