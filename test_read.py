import unittest

import read


class TestIPL(unittest.TestCase):

    def test_get_total_run_by_team(self):
        result = read.get_total_runs_by_team()

        self.assertEqual(result['Royal Challengers Bangalore'], 23436)
        self.assertEqual(result['Chennai Super Kings'], 20899)

    def test_get_player_runs_by_team(self):
        result = read.get_player_runs_by_team('Chennai Super Kings')

        self.assertEqual(result['MS Dhoni'], 2986)
        self.assertEqual(result['SK Raina'], 3707)
        self.assertEqual(result['BB McCullum'], 841)


if __name__ == "__main__":

    unittest.main()
