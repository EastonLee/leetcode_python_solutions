import unittest
from pprint import pprint
import re
import cProfile
import heapq
import collections
import itertools
import numpy as np

'''

'''

# by @totolipton, https://discuss.leetcode.com/topic/95412/python-dfs-with-memorization
class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        d = {}
        def dfs(cur):
            val = sum(cur[i]*price[i] for i in range(len(needs))) #cost without special
            for spec in special:
                tmp = [cur[j] - spec[j] for j in range(len(needs))]
                if min(tmp) >= 0: # skip deals that exceed needs
                    val = min(val, d.get(tuple(tmp), dfs(tmp)) + spec[-1]) # .get check the dictionary first for result, otherwise perform dfs.
            d[tuple(cur)] = val
            return val
        return dfs(needs)

        

class Test(unittest.TestCase):

    def test(self):
        price, special, needs = [2,5], [[3,0,5],[1,2,10]], [3,2]
        assert Solution().shoppingOffers(price, special, needs) == 14
        price, special, needs = [2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]
        assert Solution().shoppingOffers(price, special, needs) == 11
        #cProfile.runctx('Solution().shoppingOffers(case)', globals(), locals(), sort='cumtime')


if __name__ == '__main__':
    unittest.main()
