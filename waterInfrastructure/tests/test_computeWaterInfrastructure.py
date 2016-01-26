import pytest
import waterInfrastructure.computeWaterInfrastructure as ci



class TestComputeWaterInfrastructure ():
    dataSet = [ dict(communities_villages="VilA", water_functioning="yes")
              , dict(communities_villages="VilB", water_functioning="no")
              , dict(communities_villages="VilC", water_functioning="yes")
              , dict(communities_villages="VilA", water_functioning="yes")
              , dict(communities_villages="VilB", water_functioning="no")
              ]

    def test_sumFunctionalWaterPoints(self):
        assert ci.sumFunctionalWaterPoints(TestComputeWaterInfrastructure.dataSet) == 3
    def test_sumWaterPointsPerCommunity(self):
        assert ci.sumWaterPointsPerCommunity(TestComputeWaterInfrastructure.dataSet) == dict(VilA=2, VilB=2, VilC=1)
    def test_sumBrokenWaterPointsPerCommunity(self):
        assert ci.sumBrokenWaterPointsPerCommunity(TestComputeWaterInfrastructure.dataSet) == dict(VilA=0, VilB=2, VilC=0)
    def test_rankCommunitiesByPercentBrokenWaterPoints(self):
        assert ci.rankCommunitiesByPercentBrokenWaterPoints(TestComputeWaterInfrastructure.dataSet) == dict(VilA=0, VilB=100, VilC=0)


if __name__ == '__main__':
    pytest.main()
