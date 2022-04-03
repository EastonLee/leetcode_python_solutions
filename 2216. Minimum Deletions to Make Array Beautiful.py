import unittest
from typing import List


class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        count = 0
        for i, v in enumerate(nums):
            length = len(nums)
            if i % 2 == 1:
                continue
            if i == length - 1:
                nums.pop(i)
                count += 1
                break
            while len(nums) > i + 1 and v == nums[i + 1]:
                nums.pop(i)
                count += 1

        # if the last number is left, it must not be needed
        if len(nums) % 2 == 1:
            count += 1

        return count


# https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful/discuss/1887031/JavaC%2B%2BPython-O(1)-Greedy-Solution-with-Explanation
# by @lee215
class Solution2:
    def minDeletion(self, A):
        res = []
        for a in A:
            if len(res) % 2 == 0 or a != res[-1]:
                res.append(a)
        return len(A) - (len(res) - len(res) % 2)


class Test(unittest.TestCase):

    def test(self):
        cases = [
            [[1, 1, 2, 3, 5], 1],
            [[1, 1, 2, 2, 3, 3], 2],
            [[2, 6, 2, 5, 8, 9, 7, 2, 2, 5, 6, 2, 2, 0, 6, 8, 7, 3, 9, 2, 1, 1, 3, 2, 6, 2, 4, 6, 5, 8, 4, 8, 7, 0, 4,
              8, 7, 8, 4, 1, 1, 4, 0, 1, 5, 7, 7, 5, 9, 7, 5, 5, 8, 6, 4, 3, 6, 5, 1, 6, 7, 6, 9, 9, 6, 8, 6, 0, 9, 5,
              6, 7, 6, 9, 5, 5, 7, 3, 0, 0, 5, 5, 4, 8, 3, 9, 3, 4, 1, 7, 9, 3, 1, 8, 8, 9, 1, 6, 0, 0], 6],
        ]
        for ci, co in cases:
            assert Solution().minDeletion(ci) == co, (ci, co)


if __name__ == '__main__':
    unittest.main(exit=False)
