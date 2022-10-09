import unittest
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            area = (r - l) * min(height[l], height[r])
            max_area = max(max_area, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area


class Test(unittest.TestCase):
    def test(self):
        cases = [
            [[1, 8, 6, 2, 5, 4, 8, 3, 7], 49],
            [[1, 1], 1],
        ]
        for ci, co in cases:
            result = Solution().maxArea(ci)
            assert result == co, (ci, co, result)


if __name__ == '__main__':
    unittest.main(exit=False)
