# Module for fetching and parsing the JSON.

import requests
import json

# Handle the JSON fetching and parsing.


# Fetch JSON and handle exceptions.
# I don't know if attempting x3 is a good idea to begin with.

#returns parsed JSON so I don't need json.loads anywhere
def fetchJSON(url: str, attempts: int = 3) -> list:
    """Attempt to fetch the JSON file thrice. If all fails, return the exception."""
    while attempts:
        try:
            reply = requests.get(url)
            if reply.status_code == 200:
                return reply.json()
            else:
                return reply.status_code
        except(URLRequired):
            return "Use a valid url"
        except(ConnectionError, ConnectTimeout, ReadTimeout, Timeout, RequestException):
            attempts -= 1
            if not attempts:
                raise  #Reraise the exception if you're out of attempts 
        

# Reduce the list of dicts to: {communities_villages => <name>, water_functioning => <yes/no>}
# Is there need to catch a KeyError? 

"""
To test for this?
>>> import requests
>>> r = requests.get("https://raw.githubusercontent.com/onaio/ona-tech/master/data/water_points.json")
>>> len(r.json())
712"""
def reduceJSON(decodedJson: [dict]) -> [dict]:
    """"
    We reduce a list of big dictionaries into a list of smaller dicts which contain what we want:
      community_villages
      water_functioning

    We will check that the JSON follows this structure [dict] in the tests.
    Check that the JSON dicts have community_villages and water_functioning values.
    """
    return [dict (communities_villages = each_dict["communities_villages"],
                  water_functioning    = each_dict["water_functioning"])
              for each_dict in decodedJson]

