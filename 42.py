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

'''

'''
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


def tree_deserialize(string):
    """
    author: @StefanPochmann
    """
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


def tree_height(root):
    """
    author: @StefanPochmann
    """
    return 1 + max(tree_height(root.left), tree_height(root.right)) if root else -1


def tree_draw(root):
    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()
    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y - 20)
            t.write(node.val, align='center', font=('Arial', 12, 'normal'))
            draw(node.left, x - dx, y - 60, dx / 2)
            jumpto(x, y - 20)
            draw(node.right, x + dx, y - 60, dx / 2)
    import turtle
    t = turtle.Turtle()
    t.speed(0)
    turtle.delay(0)
    h = tree_height(root)
    jumpto(0, 30 * h)
    draw(root, 0, 30 * h, 40 * h)
    t.hideturtle()
    turtle.mainloop()


class Solution:
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        def conv_str(s):
            s = s.lower()
            r = re.match(r'^(\w+)@(\w+)\.(\w+)', s).groups()
            first = r[0]
            rst = first[0] + '*'*5 + first[-1]
            return ''.join([rst, '@', r[1], '.', r[2]])
        
        def conv_num(s):
            s = [i for i in s if i.isdigit()]
            extra_no = len(s) - 10
            extra = '' if extra_no == 0 else '+' + '*'*extra_no + '-'
            return extra + '***-***-' + ''.join(s[-4:])

        if S[-1].isalpha():
            return conv_str(S)
        else: return conv_num(S)


class Test(unittest.TestCase):

    def test(self):
        cases = [
            ["LeetCode@LeetCode.com", "l*****e@leetcode.com"],
            ["AB@qq.com", "a*****b@qq.com"],
            ["1(234)567-890", "***-***-7890"],
            ["86-(10)12345678", "+**-***-***-5678"],
            ["+5(4266)719-677-", '+*-***-***-9677']
        ]
        for ci, co in cases:
            print(Solution().maskPII(ci))
            assert Solution().maskPII(ci) == co
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

    def est_tree_draw(self):
        tree_draw(tree_deserialize('[1,2,3,4,5,6,7]'))

if __name__ == '__main__':
    unittest.main(exit=False)
