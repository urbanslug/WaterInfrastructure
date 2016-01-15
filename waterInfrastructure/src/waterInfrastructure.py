import computeWaterInfrastructure as ci
import fetchReduceJson


def calculate (url:str) -> dict:
    """
    The main function of this package. Glues everything together.
    """
    theJson = fetchReduceJson.fetchJSON(url)
    dataSet = fetchReduceJson.reduceJSON(theJson)
    return generateDict(dataSet)


def generateDict (dataSet: dict) -> dict:
    """
    For testing on a smaller dataset and increased modularity.
    Returns a data structure with the following format:
        {
          number_functional: …,
          number_water_points: {
            communityA: …,
          },
          community_ranking: …
        }
    """
    return dict( number_functional= ci.sumFunctionalWaterPoints(dataSet)
               , number_water_points = ci.sumWaterPointsPerCommunity(dataSet)
               , community_ranking = ci.rankCommunitiesByPercentBrokenWaterPoints(dataSet)
               )
