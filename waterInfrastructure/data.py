# Give us the data we require throughout the package through get_data.
import requests
import json

# Function for fetching and parsing the JSON.
## # returns parsed JSON so I don't need json.loads anywhere
def fetchJSON(url: str, attempts: int = 3) -> list:
    """Attempt to fetch the JSON file x3. If all fails, return the exception."""
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
# Reduce a [dict] extracted from the JSON to have less values but the list will remain to be of the same size.
def reduce(decodedJson: [dict], boolean_key: str, split_key: str) -> [dict]:
    """"
    Reduce a list of big dicts to a list of smaller dicts with `boolean_key` and `split_key` as the keys.
    reduce([{k:v, k1:v1...}, {..., k5:v5, k6:v6...}]) => [{split_key: <value>, boolean_key: <value>}]
    """
    return [{ split_key   : each_dict[split_key]
            , boolean_key : each_dict[boolean_key]
            } for each_dict in decodedJson]


def get_data(boolean_key, split_key: str, url) -> [dict]:
    """ 
    Takes the split_key and returns a [dict] that is the required dataset
    The dict will have the structure
    get_required_data (<split_key>) => [{split_key: <value>, water_functioning: <value>}, ...]
    """
    theJson = fetchJSON(url)
    return reduce(theJson, boolean_key, split_key)
