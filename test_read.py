import unittest
from unittest import result

import read

class TestIPL(unittest.TestCase):

    def test_get_total_run_by_team(self):
        result = read.get_total_runs_by_team()

        self.assertEqual(result['Royal Challengers Bangalore'], 23436)
        self.assertEqual(result['Chennai Super Kings'], 20899)

if __name__ == "__main__":

    unittest.main()