import bisect
import collections
import cProfile
import heapq
import itertools
import math
import re
import unittest
from pprint import pprint

import numpy as np
from typing import List

'''

'''


# Definition for a binary tree node.

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        while pushed:
            stack.append(pushed.pop(0))
            while stack and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
        return not stack


class Test(unittest.TestCase):

    def test(self):
        cases = [
            [dict(pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1]), True],
            [dict(pushed=[1, 2, 3, 4, 5], popped=[4, 3, 5, 1, 2]), False],
        ]
        for ci, co in cases:
            result = Solution().validateStackSequences(ci['pushed'], ci['popped'])
            assert result == co, (ci, co, result)


if __name__ == '__main__':
    unittest.main(exit=False)
