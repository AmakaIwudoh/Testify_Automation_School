# write a unit test to check the correctness of the function for tech_interview_challenge10

import tech_interview_challenge10
import unittest


class TechChallenge10(unittest.TestCase):
    def test_sentenceConversion(self):
        self.assertEqual(tech_interview_challenge10.sentenceConversion("amaka"), "Amaka")  # add assertion here


if __name__ == '__main__':
    unittest.main()
