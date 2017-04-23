import unittest
from pprint import pprint
import re
import cProfile
import heapq
import collections
import itertools

# https://discuss.leetcode.com/topic/86485/python-dp-with-explanation
# by @zym_ustc


class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 3
        if n == 0:
            return 0
        nums = [1, 1, 2]
        i = 2
        while i < n:
            nums.append((nums[i] + nums[i - 1] + nums[i - 2]) % 1000000007)
            i += 1
        result = (nums[n] + nums[n - 1] + nums[n - 2]) % 1000000007
        for i in range(n):
            result += nums[i + 1] * nums[n - i] % 1000000007
            result %= 1000000007
        return result

    # by easton
    def checkRecord2(self, n):
        if n == 0:return 0
        a = [1,2,4]
        for i in range(3,n+1):
            a.append((a[i-1] + a[i-2] + a[i-3])%1000000007)
        return (a[n] + sum([a[i]*a[n-1-i] for i in range(n)])) % 1000000007

# https://discuss.leetcode.com/topic/86526/improving-the-runtime-from-o-n-to-o-log-n/8
# by @lixx2100 and @StefanPochmann
# time complexity O(log(n))
import numpy as np

class Mint:
    def __init__(self, value):
        self.value = value % (10**9 + 7)
    def __add__(self, other):
        return Mint(self.value + other.value)
    def __mul__(self, other):
        return Mint(self.value * other.value)

class Solution(object):
    def checkRecord(self, n):
        O, I = Mint(0), Mint(1)
        A = np.matrix([[O, O, I, O, O, O],
                       [I, O, I, O, O, O],
                       [O, I, I, O, O, O],
                       [O, O, I, O, O, I],
                       [O, O, I, I, O, I],
                       [O, O, I, O, I, I]], dtype=object)
        return (A**(n+1))[5, 2].value        

class Test(unittest.TestCase):

    def test(self):
        assert Solution().checkRecord(2) == 8
        assert Solution().checkRecord(1000000) == 168078346


if __name__ == '__main__':
    unittest.main()
