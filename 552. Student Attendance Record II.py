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
            nums.append((nums[i] + nums[i-1] + nums[i-2])% 1000000007)
            i += 1
        result = (nums[n] + nums[n-1] + nums[n-2]) % 1000000007
        for i in range(n):
            result += nums[i+1] * nums[n-i] % 1000000007
            result %= 1000000007
        return result

class Test(unittest.TestCase):

    def test(self):
        assert Solution().checkRecord(2) == 8

if __name__ == '__main__':
    unittest.main()
