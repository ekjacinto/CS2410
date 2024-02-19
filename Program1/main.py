"""
    FUNCTIONS:
        getHighestRainfall(@param: dict) => @return: tuple
        getSmallestRainfall(@param: dict) => @return: tuple
        getMeanRainfall(@param: dict) => @return: float
        getCitiesGreaterMean(@param: dict, float) => @return: int
        main()
"""

""" getHighestRainfall(collection)
    Get the highest rainfall amount from rainfall.txt

    Keyword arguments:
    collection -- dictionary of cities to rainfall amount values

    Returns value:
    highestRainfallLocation, highestRainfall -- tuple of the city and highest rainfall amount
"""


def getHighestRainfall(collection):
    highestRainfall = 0
    highestRainfallLocation = None
    for city, rainfall_amt in collection.items():
        if rainfall_amt > highestRainfall:
            highestRainfall = rainfall_amt
            highestRainfallLocation = city
    return highestRainfallLocation, highestRainfall


""" getLowestRainfall(collection)
    Get the lowest rainfall amount from rainfall.txt

    Keyword arguments:
    collection -- dictionary of cities to rainfall amount values

    Return value:
    lowestRainfallLocation, lowestRainfall -- tuple of the city and lowest rainfall amount
"""


def getLowestRainfall(collection):
    lowestRainfall = list(collection.values())[0]
    lowestLocationLocation = list(collection.keys())[0]
    for city, rainfall_amt in collection.items():
        if rainfall_amt < lowestRainfall:
            lowestRainfall = rainfall_amt
            lowestLocationLocation = city
    return lowestLocationLocation, lowestRainfall


""" getMeanRainfall(collection)
    Get the mean rainfall amount from rainfall.txt

    Keyword arguments:
    collection -- dictionary of cities to rainfall amount values

    Return value:
    meanRainfall -- floating point value of the sum of rainfall values with the total number of cities
"""


def getMeanRainfall(collection):
    meanRainfall = 0
    LISTOFRAINFALLVALUES = list(collection.values())
    for rainfall_amt in LISTOFRAINFALLVALUES:
        meanRainfall += rainfall_amt
    meanRainfall = round(meanRainfall / len(LISTOFRAINFALLVALUES), 2)
    return meanRainfall


""" getNumCitiesGreaterThanMean(collection, mean)
    Get the number of cities greater than the mean rainfall amount from rainfall.txt

    Keyword arguments:
    collection -- dictionary of cities to rainfall amount values
    mean -- the mean rainfall amount value

    Return value:
    numCities -- the number of cities greater than the mean rainfall amount
"""


def getNumCitiesGreaterThanMean(collection, mean):
    numCities = 0
    LISTOFRAINFALLVALUES = list(collection.values())
    for rainfall_amt in LISTOFRAINFALLVALUES:
        if rainfall_amt > mean:
            numCities += 1
    return numCities


""" main()
    Reads rainfall.txt, prints multi-line string of cities with converted cm rainfall values, stores 
    city and corresponding rainfall value in a dictionary, calls defined functions for console output
"""


def main():
    fileContents = ""
    fileContents_in_cm = ""
    rainfall_collections = {}
    try:
        file = open("./rainfall.txt", "r")
        # store file contents in var fileContents
        fileContents = file.read()

        # use dict to correspond place with rainfall amount
        for line in fileContents.split("\n"):
            place_to_rainfall = line.split(" ")

            # convert rainfall from inches to cm
            RAINFALL_IN_CM = round(float(place_to_rainfall[1]) * 2.54, 2)
            # correspond key=place to value=rainfall_amt
            rainfall_collections[place_to_rainfall[0]] = RAINFALL_IN_CM
            # print to console new format
            fileContents_in_cm += (
                f"{place_to_rainfall[0]} {rainfall_collections[place_to_rainfall[0]]}\n"
            )
        file.close()
    except FileNotFoundError:
        print("File not found")

    print(fileContents_in_cm)
    print(
        f"Highest Rainfall: {getHighestRainfall(rainfall_collections)[1]} cm in {getHighestRainfall(rainfall_collections)[0]}"
    )
    print(
        f"Lowest Rainfall: {getLowestRainfall(rainfall_collections)[1]} cm in {getLowestRainfall(rainfall_collections)[0]}"
    )

    # store mean rainfall in variable for use
    MEANRAINFALL = getMeanRainfall(rainfall_collections)
    print(f"Mean Rainfall: {MEANRAINFALL} cm")
    print(
        f"The total number of cities where rainfall is greater than the mean number of rainfall is: {getNumCitiesGreaterThanMean(rainfall_collections, MEANRAINFALL)} cities"
    )


main()
