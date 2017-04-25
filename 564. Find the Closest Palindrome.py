import unittest
from pprint import pprint
import re
import cProfile
import heapq
import collections
import itertools
import numpy as np
import sys


class Solution(object):
    def nearestPalindromic(self, n):
        n_int, length = int(n), len(n)
        tmp = map(str, map(lambda x: x + int(n[:(length + 1) / 2]), (-1, 0, 1)))
        candidates = ['9' * (length - 1) or sys.maxint,'1' + '0' * (length - 1) + '1']
        candidates += [i for i in [i + (i[-2::-1] if length % 2 else i[::-1]) for i in tmp] if i != n]
        return candidates[min([(abs(int(v) - n_int), i) for i, v in enumerate(candidates)])[1]]


class Test(unittest.TestCase):

    def test(self):
        assert Solution().nearestPalindromic("1") == "0"
        assert Solution().nearestPalindromic("11") == "9"
        assert Solution().nearestPalindromic("123") == "121"
        assert Solution().nearestPalindromic("100") == "99"
        assert Solution().nearestPalindromic("1095500901") == "1095445901"


if __name__ == '__main__':
    unittest.main()
