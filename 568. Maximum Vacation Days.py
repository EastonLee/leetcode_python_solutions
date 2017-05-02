import unittest
from pprint import pprint
import re
import cProfile
import heapq
import collections
import itertools
import numpy as np

class Solution(object):
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        no_of_citys,  no_of_weeks = len(days), len(days[0])
        for i in range(no_of_citys):
            flights[i][i] = 1
        dp = [[None] * no_of_citys for i in range(no_of_weeks + 1)]
        dp[0][0] = 0
        for i in range(1, no_of_weeks + 1):
            for j in range(no_of_citys):
                last_city = [True if lc2 is not None and flights[lc1][j] else False for lc1, lc2 in enumerate(dp[i-1])]
                dp[i][j] = days[j][i-1] + max([dp[i-1][lc1] for lc1, lc2 in enumerate(last_city) if lc2]) if any(last_city) else None
        return max(dp[-1])



class Test(unittest.TestCase):

    def test(self):
        flights = [[0,1,1],[1,0,1],[1,1,0]]; days = [[1,3,1],[6,0,3],[3,3,3]]
        assert Solution().maxVacationDays(flights, days) == 12
        flights = [[0,0,0],[0,0,0],[0,0,0]]; days = [[1,1,1],[7,7,7],[7,7,7]]
        assert Solution().maxVacationDays(flights, days) == 3
        flights = [[0,1,1],[1,0,1],[1,1,0]]; days = [[7,0,0],[0,7,0],[0,0,7]]
        assert Solution().maxVacationDays(flights, days) == 21
        flights = [[0,1,0],[0,0,0],[0,0,0]]; days = [[0,0,7],[2,0,0],[7,7,7]]
        assert Solution().maxVacationDays(flights, days) == 7
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

if __name__ == '__main__':
    unittest.main()
