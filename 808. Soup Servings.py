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


class Solution(object):

    # https://leetcode.com/contest/weekly-contest-78/ranking/
    # @TheStrayCat
    def soupServings(self, N):
        """
        :type N: int
        :rtype: float
        """
        from functools import wraps

        def memo(f):
            cache = {}
            @wraps(f)
            def wrap(*args):
                if args not in cache:
                    cache[args]=f(*args)
                return cache[args]
            return wrap
        if N>=5000:
            return 1
        @memo
        def helper(k,l):
            if k<=0 and l<=0: return 0.5
            if k<=0: return 1
            if l<=0: return 0
            return 0.25*(helper(k-4,l)+helper(k-3,l-1)+helper(k-2,l-2)+helper(k-1,l-3))
        
        if N%25!=0:
            k=N//25+1
        else:
            k=N//25
        return helper(k,k)

class Test(unittest.TestCase):

    def test(self):
        cases = [
            [50, 0.625]
        ]
        for ci, co in cases:
            print(Solution().soupServings(ci))
            assert Solution().soupServings(ci) == co
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

    def est_tree_draw(self):
        tree_draw(tree_deserialize('[1,2,3,4,5,6,7]'))

if __name__ == '__main__':
    unittest.main(exit=False)

