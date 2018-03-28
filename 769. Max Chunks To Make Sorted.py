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

    def maxChunksToSorted1(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        N = len(arr)
        intervals = {i:(i,i) for i in range(N)}
        def union(a, b):
            return (min(a[0], b[0]), max(a[1], b[1]))

        for i in range(N):
            intervals[i] = tuple(sorted([i, arr[i]]))
        c, pre_c = 0, -1
        while pre_c != c:
            pre_c = c
            for i in range(N):
                b, e = intervals[i]
                for j in range(b, e+1):
                    if (b, e) != intervals[j]:
                        intervals[j] = union([b ,e], intervals[j])
                        c += 1
        return len(set(intervals.values()))

    # better solution
    # https://leetcode.com/articles/max-chunks-to-make-sorted-i/
    def maxChunksToSorted(self, arr):
        ans = ma = 0
        for i, x in enumerate(arr):
            ma = max(ma, x)
            if ma == i: ans += 1
        return ans


class Test(unittest.TestCase):

    def test(self):
        cases = [
            [dict(arr = [4,3,2,1,0]), 1],
            [dict(arr = [1,0,2,3,4]), 4]
        ]
        for ci, co in cases:
            assert Solution().maxChunksToSorted(**ci) == co
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

    def est_tree_draw(self):
        tree_draw(tree_deserialize('[1,2,3,4,5,6,7]'))

if __name__ == '__main__':
    unittest.main(exit=False)

