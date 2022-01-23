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
def factors(n):    
    s = set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    s.remove(n)
    return s

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        def is_prime(n):
          if n == 2 or n == 3: return True
          if n < 2 or n%2 == 0: return False
          if n < 9: return True
          if n%3 == 0: return False
          r = int(n**0.5)
          f = 5
          while f <= r:
            if n%f == 0: return False
            if n%(f+2) == 0: return False
            f +=6
          return True 
        from math import sqrt, floor
        import math
        if is_prime(num):return False
        if num<=0: return False
        divs = factors(num)
        return sum(divs) == num


class Test(unittest.TestCase):

    def test(self):
        print factors(28)
        case = 28
        assert Solution().checkPerfectNumber(case) == 1
        case = 27
        assert Solution().checkPerfectNumber(case) == 0
        case = 1
        assert Solution().checkPerfectNumber(case) == 0
        case = 13466917
        assert Solution().checkPerfectNumber(case) == 0
        case = 33550336
        assert Solution().checkPerfectNumber(case) == 1
        case = -6
        assert Solution().checkPerfectNumber(case) == 0



        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

if __name__ == '__main__':
    unittest.main()
