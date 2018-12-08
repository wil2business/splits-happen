import unittest
from score_calculator import *

class TestScoreCalculator(unittest.TestCase):
	def test_computer_score(self):
		self.assertEqual(computer_score('XXXXXXXXXXXX'), 300)
		self.assertEqual(computer_score('9-9-9-9-9-9-9-9-9-9-'), 90)
		self.assertEqual(computer_score('5/5/5/5/5/5/5/5/5/5/5'), 150)
		self.assertEqual(computer_score('X7/9-X-88/-6XXX81'), 167)

if __name__ == '__main__':
    unittest.main()