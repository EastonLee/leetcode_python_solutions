import unittest
from pprint import pprint
import re
import cProfile
import heapq
import collections
import itertools
import numpy as np

class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        import numpy as np
        res = []
        def longest_ones(a):
            l = a.tolist()
            s = ''.join(map(str, l))
            ones = re.findall('1+', s)
            return max(map(len, ones)) if ones else 0
        a = np.array(M)
        shape = a.shape
        res.extend([a[i,:] for i in range(shape[0])])
        if len(shape) == 2:
            res.extend([a[:,i] for i in range(shape[1])])
            res.extend([a.diagonal(i) for i in range(-shape[0]+1, shape[1])])
            res.extend([np.fliplr(a).diagonal(i) for i in range(-shape[0]+1, shape[1])])
        ones = map(longest_ones, res)
        return max(ones) if ones else 0



class Test(unittest.TestCase):

    def test(self):
        case = [[0,1,1,0],
 [0,1,1,0],
 [0,0,0,1]]
        assert Solution().longestLine(case) == 3
        assert Solution().longestLine([]) == 0
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')


if __name__ == '__main__':
    unittest.main()
