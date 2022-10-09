import unittest
from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = []
        for i, p in enumerate(pref):
            if i == 0:
                ans.append(p)
            else:
                ans.append(p ^ pref[i - 1])
        return ans


class Test(unittest.TestCase):
    def test(self):
        cases = [
            [[5, 2, 0, 3, 1], [5, 7, 2, 3, 2]]
        ]
        for ci, co in cases:
            result = Solution().findArray(ci)
            assert result == co, (ci, co, result)


if __name__ == '__main__':
    unittest.main(exit=False)
