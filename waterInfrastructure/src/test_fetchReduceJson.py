import unittest
import fetchReduceJson

jsonUrl = "https://raw.githubusercontent.com/onaio/ona-tech/master/data/water_points.json"

class TestFetchReduceJson (unittest.TestCase):
    theJSON = [ dict(communities_villages="VilA", water_functioning="yes", water_developer="com")
              , dict(communities_villages="VilB", water_functioning="no", water_developer="org")
              , dict(communities_villages="VilC", water_functioning="yes", water_developer="com")
              ]
    reduced = [ dict(communities_villages="VilA", water_functioning="yes")
              , dict(communities_villages="VilB", water_functioning="no")
              , dict(communities_villages="VilC", water_functioning="yes")
              ]
    def test_fetchJSON(self):
        """
        Test on the structure of the JSON. In this case test that it contains certain values.
        """
        self.assertEqual("water_point_geocode" in
                              (fetchReduceJson.fetchJSON(jsonUrl))[0], True)
        self.assertEqual( fetchReduceJson.reduceJSON(TestFetchReduceJson.theJSON)
                        , fetchReduceJson.reduceJSON(TestFetchReduceJson.reduced))


if __name__ == '__main__':
    unittest.main()
