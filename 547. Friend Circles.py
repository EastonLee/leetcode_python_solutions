import unittest
import cProfile
import collections


# by easton
# union method
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        d = collections.defaultdict(set)
        num = len(M)
        def get_circle(i):
            circle = [m for m,n in d.items() if i in n]
            if circle:
                return circle[0]
            return None
        for i in range(num):
            for j in range(i, num):
                if not M[i][j]:
                    continue
                ic, jc = map(get_circle, [i, j])
                if not ((ic is not None) or (jc is not None)):
                    d[i].add(j)
                if not (ic is not None) and (jc is not None):
                    d[jc].add(i)
                if (ic is not None) and not (jc is not None):
                    d[ic].add(j)
                if (ic is not None) and (jc is not None) and ic != jc:
                    d[ic] |= d[jc]
                    del d[jc]
        return len(d)

# https://discuss.leetcode.com/topic/85047/python-simple-explanation
# by @awice 
# dfs method
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        seen = set()
        count = 0
        def dfs(n):
            # print 'dfs', n
            f = [seen.add(i) or i for i,j in enumerate(M[n]) if j and i not in seen]
            # print 'f', f
            map(dfs, f)
        for i in range(len(M)):
            if i not in seen:
                dfs(i)
                count += 1
        return count

# https://discuss.leetcode.com/topic/85108/oneliners-p
# by @StefanPochmann
import scipy.sparse
class Solution(object):
    def findCircleNum(self, M):
        return scipy.sparse.csgraph.connected_components(M)[0]
import numpy as np
class Solution(object):
    def findCircleNum(self, M):
        return len(set(map(tuple, (np.matrix(M, dtype='bool')**len(M)).A)))

class Test(unittest.TestCase):

    def test(self):
        case = [[1,1,0],
 [1,1,0],
 [0,0,1]]
        assert Solution().findCircleNum(case) == 2
        case = [[1,1,0],
 [1,1,1],
 [0,1,1]]
        assert Solution().findCircleNum(case) == 1
        case = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
        assert Solution().findCircleNum(case) == 1

        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

if __name__ == '__main__':
    unittest.main()
