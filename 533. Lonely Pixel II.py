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
    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        r_no = len(picture)
        c_no = len(picture[0])
        search_r = [i for i in range(r_no) if picture[i].count('B')==N]
        search_c = [i for i in range(c_no) if [j[i] for j in picture].count('B')==N]
        count = 0
        for r in search_r:
            for c in search_c:
                if picture[r][c] == 'B':
                    cur_row = picture[r]
                    sibs = filter(lambda x:x[c]=='B', picture)
                    if all([s==cur_row for s in sibs]):
                        count += 1
        return count




class Test(unittest.TestCase):

    def test(self):
        case = \
    [['W', 'B', 'W', 'B', 'B', 'W'],    
     ['W', 'B', 'W', 'B', 'B', 'W'],    
     ['W', 'B', 'W', 'B', 'B', 'W'],    
     ['W', 'W', 'B', 'W', 'B', 'W']]  
        assert Solution().findBlackPixel(case, 3) == 6

        case = \
    [['W', 'B', 'W', 'B', 'B', 'W'],    
     ['W', 'B', 'W', 'B', 'B', 'W'],    
     ['W', 'B', 'W', 'B', 'B', 'W'],    
     ['B', 'W', 'B', 'W', 'B', 'W']]  
        assert Solution().findBlackPixel(case, 3) == 6
        #cProfile.runctx('Solution().calculate(case)', globals(), locals())

if __name__ == '__main__':
    unittest.main()
