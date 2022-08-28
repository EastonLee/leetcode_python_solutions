import unittest
from typing import List


class Solution:
    # copilot
    def subsets1(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for n in nums:
            ans += [i + [n] for i in ans]
        return ans

    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        sub = self.subsets(nums[:-1])
        return sub + [i + [nums[-1]] for i in sub]


class Test(unittest.TestCase):
    def test(self):
        cases = [
            [[1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]],
            [[0], [[], [0]]]
        ]
        for ci, co in cases:
            result = Solution().subsets(ci)
            assert result == co, (ci, co, result)


if __name__ == '__main__':
    unittest.main(exit=False)
