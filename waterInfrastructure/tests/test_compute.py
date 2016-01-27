import pytest
import waterInfrastructure.compute as compute



class TestCompute ():
    data = [ dict(communities_villages="VilA", water_functioning="yes", water_pay="yes")
           , dict(communities_villages="VilB", water_functioning="no",  water_pay="no")
           , dict(communities_villages="VilC", water_functioning="yes", water_pay="yes")
           , dict(communities_villages="VilA", water_functioning="yes", water_pay="no")
           , dict(communities_villages="VilB", water_functioning="no", water_pay="yes")
           ]

    def test_sumFunctionalWaterPoints(self):
        assert compute.sumFunctionalWaterPoints(TestCompute.data) == 3

    def test_sumWaterPointsPerCommunity(self):
        assert compute.sumWaterPointsPerSplitKey("communities_villages", TestCompute.data) == dict(VilA=2, VilB=2, VilC=1)

    def test_sumBrokenWaterPointsPerCommunity(self):
        assert compute.sumBrokenWaterPointsPerSplitKey("water_pay", "water_functioning", TestCompute.data) == {"yes":1, "no":1}

    def test_rankCommunitiesByPercentBrokenWaterPoints(self):
        assert compute.rank("water_pay", "water_functioning",TestCompute.data) == {"yes":(1/3*100), "no":50}


if __name__ == '__main__':
    pytest.main()
