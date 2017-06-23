import unittest
from pprint import pprint
import re
import cProfile
import heapq
import collections
import itertools
import numpy as np


class Solution(object):
    # @awice https://discuss.leetcode.com/topic/92952/python-straightforward-with-explanation
    def leastInterval(self, tasks, N):
        task_counts = collections.Counter(tasks).values()
        M = max(task_counts)
        Mct = task_counts.count(M)
        return max(len(tasks), (M - 1) * (N + 1) + Mct)

class Test(unittest.TestCase):

    def test(self):
        tasks = ['A','A','A','B','B','B']; n = 2
        assert Solution().leastInterval(tasks, n) == 8

if __name__ == '__main__':
    unittest.main()
