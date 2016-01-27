import pytest
import waterInfrastructure.data as data

jsonUrl = "https://raw.githubusercontent.com/onaio/ona-tech/master/data/water_points.json"

class TestData ():
    theJSON = [ dict(communities_villages="VilA", water_functioning="yes", water_developer="com")
              , dict(communities_villages="VilB", water_functioning="no",  water_developer="org")
              , dict(communities_villages="VilC", water_functioning="yes", water_developer="com")
              ]
    reduced = [ dict(communities_villages="VilA", water_functioning="yes")
              , dict(communities_villages="VilB", water_functioning="no")
              , dict(communities_villages="VilC", water_functioning="yes")
              ]

    def test_fetchJSON(self):
        """
        Test the structure of the JSON. In this case test that it contains "water_point_geocode" as a key.
        """
        assert ("water_point_geocode" in
                              (data.fetchJSON(jsonUrl))[0]) == True

    def test_reduce(self):
        """
        Ensure that the reduceJSON filters out the unnecessary fields from the JSON.
        """
        assert data.reduce("water_functioning", "communities_villages", TestData.theJSON) == TestData.reduced

    def test_get_data(self):
        """
        The dict contains the keys `communities_villages` and `water_functioning` and no others.
        """
        reducedDict = data.get_data("water_functioning", "communities_villages", jsonUrl).pop()
        requiredSet = set(["communities_villages", "water_functioning"])
        # Assert that the resulting set is empty. If it is not empty there were other values in the dict.
        assert requiredSet - set(reducedDict.keys()) == set()


if __name__ == '__main__':
    pytest.main()
