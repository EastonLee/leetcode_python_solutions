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

    # by @lee215
    # https://leetcode.com/problems/longest-mountain-in-array/discuss/135593/C++JavaPython-1-pass-and-O(1)-space
    def longestMountain(self, A):
        res = up = down = 0
        for i in range(1, len(A)):
            if down and A[i - 1] < A[i] or A[i - 1] == A[i]: up = down = 0
            up += A[i - 1] < A[i]
            down += A[i - 1] > A[i]
            if up and down: res = max(res, up + down + 1)
        return res

    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        s = 0
        pre_trend, trend = 0, 0
        rst = []
        for i, v in enumerate(A):
            if i == 0: continue
            if A[i] > A[i-1]:
                if pre_trend == 1 and trend == -1:
                    rst.append(i-s)
                    s = i - 1
                if trend != 1:
                    pre_trend = trend
                trend = 1
            elif A[i] == A[i-1]:
                if pre_trend == 1 and trend == -1:
                    rst.append(i-s)
                if trend != 0:
                    pre_trend = trend
                trend = 0
                s = i
            else:
                if trend != -1:
                    pre_trend = trend
                trend = -1
                if pre_trend != 1:
                    s = i
                if i == len(A) - 1 and pre_trend == 1 and trend == -1:
                    rst.append(i-s+1)
        return len(rst) and max(rst)

class Test(unittest.TestCase):

    def test(self):
        cases = [
            [[2,1,4,7,3,2,5], 5],
            [[2,2,2], 0],
            [[0,1,2,3,4,5,4,3,2,1,0], 11],
            [[1,2,0,2,0,2], 3],
            [[875,884,239,731,723,685], 4]
        ]
        for ci, co in cases:
            tmp = Solution().longestMountain(ci)
            print(tmp)
            assert tmp == co
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

    def est_tree_draw(self):
        tree_draw(tree_deserialize('[1,2,3,4,5,6,7]'))

if __name__ == '__main__':
    unittest.main(exit=False)
