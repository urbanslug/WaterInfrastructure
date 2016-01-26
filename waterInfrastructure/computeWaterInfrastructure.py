# Run various computations on various datasets.

import collections


# number_functional
def sumFunctionalWaterPoints(dataSet: [dict]) -> int:
    """
    Given a dataset with structure: [{"community_villages" => <name>, "water_functioning" => <yes/no>},...]
    Compute the number of times that "yes" appears as a value of "water_functioning" in the list of dicts.
    """
    listOfYes = [ x for x in dataSet if x["water_functioning"] == "yes"]
    return len(listOfYes)

# number_water_points
def sumWaterPointsPerCommunity(dataSet: [dict]) -> dict:
    """
    Given a dataset with structure: [{"community_villages" => <name>, "water_functioning" => <yes/no>},...]
    Compute the number of times that each value is repeated for the "community_villages" key.
    """
    listOfCommunityVillages = [x["communities_villages"] for x in dataSet]
    return dict(collections.Counter(listOfCommunityVillages))

def sumBrokenWaterPointsPerCommunity(dataSet: [dict]) -> dict:
    """
    Given a dataset with structure: [{"community_villages" => <name>, "water_functioning" => <yes/no>},...]
    Compute the total number of BROKEN water points in each community.
    """
    setOfCommunityVillages = {x["communities_villages"] for x in dataSet}
    listOfCommunityVillagesWithBrokenWaterPoints = [x["communities_villages"] for x in dataSet
                                                   if x["water_functioning"] == "no"] # list
    setOfCommunityVillagesWithBrokenWaterPoints = set(listOfCommunityVillagesWithBrokenWaterPoints)
    setOfCommunityVillagesWithoutBrokenWaterPoints = setOfCommunityVillages - setOfCommunityVillagesWithBrokenWaterPoints
    dictOfBrokenWaterPointsEqZero = dict ([(str(x),0) for x in setOfCommunityVillagesWithoutBrokenWaterPoints])
    dictOfBrokenWaterPointsGtZero = dict(collections.Counter(listOfCommunityVillagesWithBrokenWaterPoints))
    dictOfBrokenWaterPoints = dictOfBrokenWaterPointsGtZero.copy()
    dictOfBrokenWaterPoints.update(dictOfBrokenWaterPointsEqZero)
    return dictOfBrokenWaterPoints
    

# community_ranking
def rankCommunitiesByPercentBrokenWaterPoints(dataSet: [dict]) -> dict:
    """
    Given a dataset with structure: [{"community_villages" => <name>, "water_functioning" => <yes/no>},...]
    Calculate a pertange of BROKEN water points per community.
    So build a dict with structure {<community_village_name> => <percentage>, ...}
    """
    dictOfBrokenWaterPoints = sumBrokenWaterPointsPerCommunity(dataSet)
    dictOfWaterPoints = sumWaterPointsPerCommunity(dataSet)

    # Can we make this part faster?
    listOfWaterPoints = dictOfBrokenWaterPoints.keys()
    return dict([(x,(dictOfBrokenWaterPoints[x]/dictOfWaterPoints[x]*100)) for x in listOfWaterPoints])
