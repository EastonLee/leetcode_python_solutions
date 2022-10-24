import unittest
from typing import List

"""
You are given two 0-indexed arrays nums and cost consisting each of n positive integers.

You can do the following operation any number of times:

Increase or decrease any element of the array nums by 1.
The cost of doing one operation on the ith element is cost[i].

Return the minimum total cost such that all the elements of the array nums become equal.
"""


# find the min value of a function f(x) = sum(cost[i] * abs(nums[i] - x))
# we assume the function is convex, first monotonic decreasing and then monotonic increasing (I cannot prove it)
# we can find the min value by binary search
def minValueOfFunction(start: int, end: int, nums: List[int], cost: List[int]) -> int:
    if start == end:
        return sum([cost[i] * abs(nums[i] - start) for i in range(len(nums))])

    mid = (start + end) // 2
    if sum([cost[i] * abs(nums[i] - mid) for i in range(len(nums))]) < sum(
            [cost[i] * abs(nums[i] - (mid + 1)) for i in range(len(nums))]):
        return minValueOfFunction(start, mid, nums, cost)
    else:
        return minValueOfFunction(mid + 1, end, nums, cost)


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        Min = min(nums)
        Max = max(nums)
        return minValueOfFunction(Min, Max, nums, cost)


class Test(unittest.TestCase):
    def test(self):
        cases = [

            [[1, 3, 5, 2], [2, 3, 1, 14], 8],
            [[2, 2, 2, 2, 2], [4, 2, 8, 1, 3], 0],
            [[735103, 366367, 132236, 133334, 808160, 113001, 49051, 735598, 686615, 665317, 999793, 426087, 587000,
              649989, 509946, 743518],
             [
                 724182, 447415, 723725, 902336, 600863, 287644, 13836, 665183, 448859, 917248, 397790, 898215, 790754,
                 320604, 468575, 825614], 1907611126748]
        ]
        for ci0, ci1, co in cases:
            result = Solution().minCost(ci0, ci1)
            assert result == co, (ci0, ci1, co, result)


if __name__ == '__main__':
    unittest.main(exit=False)
