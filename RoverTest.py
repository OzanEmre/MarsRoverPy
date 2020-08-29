import unittest
from RoverBusiness import RoverBusiness
import json

class RoverTest(unittest.TestCase):

    def test_first(self):
        RoverBusiness("5 5", "1 2 N", "LMLMLMLMM")
        result = json.loads(RoverBusiness.navigate())
        self.assertEqual("{} {} {}".format(result["result"][0], result["result"][1], result["result"][2]), "1 3 N")

    def test_second(self):
        RoverBusiness("5 5", "3 3 E", "MMRMMRMRRM")
        #RoverBusiness("5 5", "3 3 W", "MMMMMM")
        result = json.loads(RoverBusiness.navigate())
        self.assertEqual("{} {} {}".format(result["result"][0], result["result"][1], result["result"][2]), "5 1 E")

if __name__ == '__main__':
    unittest.main()