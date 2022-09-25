import unittest
from typing import List


class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dp1, dp2 = [1] * len(nums), [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                dp1[i] = dp1[i - 1] + 1

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                dp2[i] = dp2[i + 1] + 1

        ans = []
        for i in range(k, n - k):
            if dp1[i - 1] >= k and dp2[i + 1] >= k:
                ans.append(i)
        return ans


class Test(unittest.TestCase):
    def test(self):
        cases = [
            [dict(nums=[2, 1, 1, 1, 3, 4, 1], k=2), [2, 3]],
            [dict(nums=[2, 1, 1, 2], k=2), []],
            [dict(nums=[440043, 276285, 336957], k=1), [1]],
            [dict(nums=[388589, 17165, 726687, 401298, 600033, 537254, 301052, 151069, 399955], k=4), []],
        ]
        for ci, co in cases:
            result = Solution().goodIndices(ci['nums'], ci['k'])
            assert result == co, (ci, co, result)


if __name__ == '__main__':
    unittest.main(exit=False)
