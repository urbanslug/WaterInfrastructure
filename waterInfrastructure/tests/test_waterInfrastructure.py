import pytest
import waterInfrastructure.waterInfrastructure as wi



class TestWaterInfrastructure ():
    dataSet = [ dict(communities_villages="VilA", water_functioning="yes")
              , dict(communities_villages="VilB", water_functioning="no")
              , dict(communities_villages="VilC", water_functioning="yes")
              , dict(communities_villages="VilA", water_functioning="yes")
              , dict(communities_villages="VilB", water_functioning="no")
              ]

    def test_generateDict(self):
        assert ((wi.generateDict(TestWaterInfrastructure.dataSet)
                        == dict( number_functional = 3
                              , number_water_points = dict(VilA=2, VilB=2, VilC=1)
                              , community_ranking   = dict(VilA=0, VilB=100, VilC=0))))


if __name__ == '__main__':
    pytest.main()
