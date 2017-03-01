import unittest
from pprint import pprint
import re
import cProfile
from heapq import *
import collections

'''

'''
# Definition for a binary tree node.


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return 'value: {}'.format(self.val)


class Solution(object):

    def calculate(self, s):
        tokens = re.findall('\d+|\S', s)
        total = 0
        signs = [1]
        sign = 1
        i = 0
        while i < len(tokens):
            if tokens[i] == '(':
                signs.append(signs[-1] * sign)
                sign = 1
            if tokens[i] == ')':
                signs.pop()
            if tokens[i] == '+':
                sign = 1
            if tokens[i] == '-':
                sign = -1
            if tokens[i].isdigit():
                total += int(tokens[i]) * sign * signs[-1]
            i += 1
        return total


class Test(unittest.TestCase):

    def test(self):
        #assert Solution().calculate(" 0 - 0 ") == 0
        #assert Solution().calculate("1 + 1") == 2
        #assert Solution().calculate(" 2-1 + 2 ") == 3
        #assert Solution().calculate("(1+(4+5+2)-3)+(6+8)") == 23
        #assert Solution().calculate("1-(5)") == -4
        case = "1+7-(7+3+3)+6-3+1"
        print(case + '=' + str(Solution().calculate(case)))
        #cProfile.runctx('Solution().calculate(case)', globals(), locals())

if __name__ == '__main__':
    unittest.main()
