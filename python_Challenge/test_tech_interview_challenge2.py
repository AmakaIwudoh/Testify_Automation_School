# write a unit test to check the correctness of the function for tech_interview_challenge2

import tech_interview_challenge2
import unittest


class TechChallenge2(unittest.TestCase):
    def test_exponent(self):
        self.assertEqual(tech_interview_challenge2.exponent(2, 3), 8)  # add assertion here


if __name__ == '__main__':
    unittest.main()