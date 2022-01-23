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

    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        rst = []
        S = S[1:-1]
        length = len(S)
        part = [[S[:i], S[i:]] for i in range(1, length)]
        def str2ans(s):
            if s == '0':
                return ['0']
            if s.startswith('0') and s.endswith('0'):
                return []
            if s.startswith('0'):
                return ['0.' + s[1:]]
            if s.endswith('0'):
                return [s]
            rst = [s]
            rst += [s[:i] + '.' + s[i:] for i in range(1, len(s))]
            return rst
        for i,j in part:
            left = str2ans(i)
            right = str2ans(j)
            if not (left and right): continue
            rst += [f'({m}, {n})' for m in left for n in right]
        return rst
                


class Test(unittest.TestCase):

    def test(self):
        cases = [
            ["(123)", set(["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"])],
            ["(00011)", set(["(0.001, 1)", "(0, 0.011)"])],
            ["(0123)", set(["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"])],
            ["(100)", set(["(10, 0)"])]
        ]
        for ci, co in cases:
            print(ci)
            print(Solution().ambiguousCoordinates(ci))
            assert set(Solution().ambiguousCoordinates(ci)) == co
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

    def est_tree_draw(self):
        tree_draw(tree_deserialize('[1,2,3,4,5,6,7]'))

if __name__ == '__main__':
    unittest.main(exit=False)
