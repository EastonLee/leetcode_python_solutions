import unittest
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        m = max(nums)
        l = map(lambda x: 1 if x & m == m else 0, nums)
        return max(map(len, ''.join(map(str, l)).split('0')))


class Test(unittest.TestCase):
    def test(self):
        cases = [
            [[10, 2, 2, 2, 3, 3, 5, 5], 1],
            [[311155, 311155, 311155, 311155, 311155, 311155, 311155, 311155, 201191, 311155], 8]
        ]
        for ci, co in cases:
            result = Solution().longestSubarray(ci)
            assert result == co, (ci, co, result)


if __name__ == '__main__':
    unittest.main(exit=False)
