import waterInfrastructure.data as data
import waterInfrastructure.compute as compute

url = "https://raw.githubusercontent.com/onaio/ona-tech/master/data/water_points.json"

# -------------------------------------
#       First challenge:
# --------------------------------------


def calculate (url):
    dataSet = data.get_data("water_functioning", "communities_villages", url)
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
    return dict( number_functional= compute.sumFunctionalWaterPoints(dataSet)
               , number_water_points = compute.sumWaterPointsPerSplitKey("communities_villages", dataSet)
               , community_ranking = compute.rank("water_functioning", "communities_villages", dataSet)
               )


# -------------------------------------
#       Second challenge:
# --------------------------------------


# Question 1
def percent_water_functioning_by(split_key: str) -> dict:
    dataSet = data.get_data("water_functioning", split_key, url)
    return compute.rank("water_functioning", split_key, dataSet)

# Question 2
def percent_boolean_key_by(boolean_key, split_key):
    dataSet = data.get_data(boolean_key, split_key, url)
    return compute.rank(boolean_key, split_key, dataSet)



if __name__ == "__main__" :
    print ("The main module of this package. It glues everything together.")
