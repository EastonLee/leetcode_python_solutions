import unittest
from pprint import pprint
import re
import cProfile
from heapq import *
import collections


class Solution(object):

    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        rst = [1] + [0] * amount
        for i in coins:
            for j in range(i, amount + 1):
                rst[j] += rst[j - i]
        return rst[amount]


class Test(unittest.TestCase):

    def test(self):
        amount = 5
        coins = [5, 2, 1]
        assert Solution().change(amount, coins) == 4
        amount = 3
        coins = [2]
        assert Solution().change(amount, coins) == 0
        amount = 10
        coins = [10]
        assert Solution().change(amount, coins) == 1
        assert Solution().change(0, [1, 2]) == 1
        assert Solution().change(0, []) == 1
        assert Solution().change(500, [1, 2]) == 251
        assert Solution().change(500, [3, 5, 7, 8, 9, 10, 11]) == 35502874
        assert Solution().change(7, []) == 0

if __name__ == '__main__':
    unittest.main()
