import unittest
from pprint import pprint
import re
import cProfile
import heapq
import collections
import itertools
import numpy as np
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        ALL = []
        for i in nums:
            ALL += i
        length = len(ALL)
        if r * c != length: return nums
        res = []
        for i in range(0, r*c, c):
            res.append(ALL[i:i+c])
        return res
        
class Test(unittest.TestCase):

    def test(self):
        nums = \
[[1,2],
 [3,4]]
        assert Solution().matrixReshape(nums,1,4) == [[1,2,3,4]]
        nums = \
[[1,2],
 [3,4]]
        assert Solution().matrixReshape(nums,2,4) == [[1,2],[3,4]]
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

if __name__ == '__main__':
    unittest.main()
