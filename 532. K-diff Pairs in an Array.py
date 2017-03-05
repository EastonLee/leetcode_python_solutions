import unittest
from pprint import pprint
import re
import cProfile
from heapq import *
import collections

'''

'''
# Definition for a binary tree node.


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return 'value: {}'.format(self.val)


class Solution(object):

    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import Counter
        if k == 0:
            c = Counter(nums)
            return len(filter(lambda x:x[1]>1, c.items()))
        nums = list(set(nums))
        nums.sort()
        seen = set(nums[:1])
        c = 0
        for i in nums[1:]:
            if i-k in seen:
                c += 1
            seen.add(i)
        return c




class Test(unittest.TestCase):

    def test(self):
        case = [3, 1, 4, 1, 5]; k = 2
        #assert Solution().findPairs(case, k) == 2
        case = [1, 2, 3, 4, 5]; k = 1
        assert Solution().findPairs(case, k) == 4
        case = [1, 3, 1, 5, 4]; k = 0
        assert Solution().findPairs(case, k) == 1
        #cProfile.runctx('Solution().calculate(case)', globals(), locals())

if __name__ == '__main__':
    unittest.main()
