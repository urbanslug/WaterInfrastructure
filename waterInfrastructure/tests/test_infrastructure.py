import pytest
import waterInfrastructure.infrastructure as infrastructure

url = "https://raw.githubusercontent.com/onaio/ona-tech/master/data/water_points.json"

class TestInfrastructure ():
    dataSet = [ dict(communities_villages="VilA", water_functioning="yes")
              , dict(communities_villages="VilB", water_functioning="no")
              , dict(communities_villages="VilC", water_functioning="yes")
              , dict(communities_villages="VilA", water_functioning="yes")
              , dict(communities_villages="VilB", water_functioning="no")
              ]
    def test_calculate(self):
        """
        Check that the resulting dict contains the following keys only:
        `number_functional`, `number_water_points`, `community_ranking`
        """
        d = infrastructure.calculate(url)
        requiredSet = set(["number_functional", "number_water_points", "community_ranking"])
        assert requiredSet - set(d.keys()) == set()

    def test_generateDict(self):
        assert ((infrastructure.generateDict(TestInfrastructure.dataSet)
                        == dict( number_functional = 3
                              , number_water_points = dict(VilA=2, VilB=2, VilC=1)
                              , community_ranking   = dict(VilA=0, VilB=100, VilC=0))))

    # The other two functions check each other:
    #  - percent_water_functioning_by
    #  - percent_boolean_key_by
    def test_percent_water_functioning_by_and_percent_boolean_key_by(self):
        assert infrastructure.percent_water_functioning_by("road_available") == infrastructure.percent_boolean_key_by("water_functioning", "road_available")

if __name__ == '__main__':
    pytest.main()
