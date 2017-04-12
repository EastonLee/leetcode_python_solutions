import unittest
from pprint import pprint
import re
import cProfile
import heapq
import collections
import itertools


class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        d = collections.defaultdict(list)
        seen = set()
        num = len(M)
        for i in range(num):
            seen.add(i)
            for j in range(i, num):
                if not M[i][j]:
                    continue
                seen.add(j)
                pre = [m for m,n in d.items() if i in n]
                pre = pre and pre[0] or i
                d[pre].append(j)
        print d
        return len(d)



class Test(unittest.TestCase):

    def test(self):
        case = [[1,1,0],
 [1,1,0],
 [0,0,1]]
        print Solution().findCircleNum(case)
        assert Solution().findCircleNum(case) == 2
        case = [[1,1,0],
 [1,1,1],
 [0,1,1]]
        assert Solution().findCircleNum(case) == 1
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

if __name__ == '__main__':
    unittest.main()
