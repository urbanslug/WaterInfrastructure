# Run various computations on various datasets.
import collections

# number_functional
def sumFunctionalWaterPoints(dataSet: [dict]) -> int:
    """
    Given a dataset with structure: [{"community_villages" => <name>, "water_functioning" => <yes/no>},...]
    Compute the number of times that "yes" appears as a value of "water_functioning" in the list of dicts.
    """
    listOfYes = [x for x in dataSet if x["water_functioning"] == "yes"]
    return len(listOfYes)



# number_water_points
def sumWaterPointsPerSplitKey(split_key, dataSet: [dict]) -> dict:
    """
    Given a dataset with structure: [{"community_villages" => <name>, "water_functioning" => <yes/no>},...]
    Compute the number of times that each value is repeated for the "community_villages" key.
    """
    listOfCommunityVillages = [x[split_key] for x in dataSet]
    return dict(collections.Counter(listOfCommunityVillages))

def sumBrokenWaterPointsPerSplitKey(boolean_key, split_key, dataSet: [dict]) -> dict:
    """
    Given a dataset with structure: [{"community_villages" => <name>, "water_functioning" => <yes/no>},...]
    Compute the total number of BROKEN water points in each community.
    """
    setOfSplitKeys = {x[split_key] for x in dataSet}
    listOfSplitKeysWithBrokenWaterPoints = [x[split_key] for x in dataSet
                                                   if x[boolean_key] == "no"] # list
    setOfSplitKeysWithBrokenWaterPoints = set(listOfSplitKeysWithBrokenWaterPoints)
    setOfSplitKeysWithoutBrokenWaterPoints = setOfSplitKeys - setOfSplitKeysWithBrokenWaterPoints
    dictOfBrokenWaterPointsEqZero = dict ([(str(x),0) for x in setOfSplitKeysWithoutBrokenWaterPoints])
    dictOfBrokenWaterPointsGtZero = dict(collections.Counter(listOfSplitKeysWithBrokenWaterPoints))
    dictOfBrokenWaterPoints = dictOfBrokenWaterPointsGtZero.copy()
    dictOfBrokenWaterPoints.update(dictOfBrokenWaterPointsEqZero)
    return dictOfBrokenWaterPoints
    

# community_ranking
def rank(boolean_key, split_key, data: [dict]) -> dict:
    """
    Given a dataset with structure: [{"community_villages" => <name>, "water_functioning" => <yes/no>},...]
    Calculate a pertange of BROKEN water points per community.
    So build a dict with structure {<community_village_name> => <percentage>, ...}
    """
    dictOfBrokenSplitKeys = sumBrokenWaterPointsPerSplitKey(boolean_key, split_key, data)
    dictOfSplitKeys = sumWaterPointsPerSplitKey(split_key, data)

    # Can we make this part faster?
    listOfSplitKeys = dictOfBrokenSplitKeys.keys()
    return dict([(x,(dictOfBrokenSplitKeys[x]/dictOfSplitKeys[x]*100)) for x in listOfSplitKeys])

