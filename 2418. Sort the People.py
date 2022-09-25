import unittest
from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        z = sorted(zip(names, heights), key=lambda x: (-x[1], x[0]))
        return [x[0] for x in z]


class Test(unittest.TestCase):
    def test(self):
        cases = [
            ["1+7-(7+3+3)+6-3+1", -1]
        ]
        for ci, co in cases:
            result = Solution().sortPeople(ci)
            assert result == co, (ci, co, result)


if __name__ == '__main__':
    unittest.main(exit=False)
