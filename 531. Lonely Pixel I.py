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
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        r_no = len(picture)
        c_no = len(picture[0])
        search_r = [[i, i.index('B')] for i in picture if i.count('B')==1]
        seen_c = set()
        count = 0
        for i in search_r:
            if i[1] in seen_c: continue
            conflict_r = filter(lambda x:x[i[1]]=='B', picture)
            conflict_r_no = len(conflict_r)
            seen_c.add(i[1])
            if conflict_r_no == 1:
                count += 1
        return count

        


class Test(unittest.TestCase):

    def test(self):
        case = \
[['W', 'W', 'B'],
 ['W', 'B', 'W'],
 ['B', 'W', 'W']]
        assert Solution().findLonelyPixel(case) == 3
        #cProfile.runctx('Solution().calculate(case)', globals(), locals())

if __name__ == '__main__':
    unittest.main()
