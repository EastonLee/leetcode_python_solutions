import unittest
from pprint import pprint
import re
import cProfile
import heapq
import collections
import itertools
import numpy as np


class Solution(object):
    # @easton042, TLE
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def valid_triangle(sides):
            sides.sort()
            return sides[0] + sides[1] > sides[2]
        ps = itertools.combinations(nums, 3)
        return sum([valid_triangle(list(p)) for p in ps])

    # @fallcreek, https://discuss.leetcode.com/topic/92173/python-o-n-2
    def triangleNumber(self, nums):
        nums.sort()
        nums = nums[::-1]
        
        sol = 0
        
        for i in range(len(nums) - 2):
            k = len(nums) - 1
            for j in range(i + 1, k):
                if j >= k:
                    break
                diff = nums[i] - nums[j]
                while nums[k] <= diff and k > j:
                    k -= 1
                sol += (k - j)
        return sol

class Test(unittest.TestCase):

    def test(self):
        case = [2,2,3,4]
        assert Solution().triangleNumber(case) == 3
        case = [74,7,30,63,7,77,89,93,62,21,67,71,17,98,18,71,80,32,99,31,74,60,35,38,34,1,62,95,38,20,75,99,57,26,39,37,31,18,3,54,27,66,57,5,23,34,29,85,97,29,8,13,8,99,68,76,26,54,1,59,28,88,84,91,99,0,29,2,41,63,19,2,63,52,40,10,79,24,98,11,50,99,42,80,23,21,39,27,93,13,12,33,40,22,74,87,93,2,22,88]
        print Solution().triangleNumber(case) 
        assert Solution().triangleNumber(case) == 3

if __name__ == '__main__':
    unittest.main()
