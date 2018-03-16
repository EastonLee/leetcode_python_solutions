import unittest
from pprint import pprint
import re
import cProfile
import heapq
import bisect
import collections
import itertools
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

    def calculate(self, A):
        N = len(A)
        d = collections.defaultdict(list)
        accum_sum = 0
        res = 0
        for i, v in enumerate(A):
            accum_sum += v
            d[accum_sum].append(i)
        for s, i_s in d.items():
            l = min(i_s)
            r = max(i_s)
            if s >= 0:
                l = -1
            if s <= accum_sum:
                r = N-1
            res = max(res, r - l)
        return res

class Test(unittest.TestCase):

    def test(self):
        case = [-1, -1, 1, -1, 1, 0, 1, -1, -1]
        assert Solution().calculate(case) == 7
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

    def est_tree_draw(self):
        tree_draw(tree_deserialize('[1,2,3,4,5,6,7]'))

if __name__ == '__main__':
    unittest.main(exit=False)
