import unittest
from whiteboard import solution

class TestWhiteboard(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])

    def test_2(self):
        self.assertEqual(solution([0, 0, 1, 1, 2, 3, 4]), [1, 1, 2, 3, 4, 0, 0])

    def test_3(self):
        self.assertEqual(solution([1, 1, 1, 1, 1]), [1, 1, 1, 1, 1])

    def test_4(self):
        self.assertEqual(solution([-1, 0, 0, 0, 0, 2]), [-1, 2, 0, 0, 0, 0])

    def test_5(self):
        self.assertEqual(solution([0, 0, 0, 0, 0]), [0, 0, 0, 0, 0])

if __name__ == "__main__":
    unittest.main()