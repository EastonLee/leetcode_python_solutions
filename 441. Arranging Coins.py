import unittest
from pprint import pprint
import re
import cProfile
import heapq
import collections
import itertools

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
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        from math import sqrt, floor
        return int(floor(sqrt(2*n + 1/4.) - 1/2.))


class Test(unittest.TestCase):

    def test(self):
        case = "1+7-(7+3+3)+6-3+1"
        assert Solution().arrangeCoins(5) == 2
        assert Solution().arrangeCoins(8) == 3
        #cProfile.runctx('Solution().calculate(case)', globals(), locals())

if __name__ == '__main__':
    unittest.main()
