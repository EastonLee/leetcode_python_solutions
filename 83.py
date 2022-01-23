import bisect
import collections
import copy
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
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        # if quiet == [3,2,5,4,6,1,7,0]:
            # return [5,5,2,5,4,5,6,7]
        d = collections.defaultdict(set)
        for i,j in richer:
            d[j].add(i)
        N = len(quiet)
        def dricher(n):
            seen = set([n])
            l = [n]
            while l:
                tmp = l.pop()
                tmp = d[tmp]
                tmp = [i for i in tmp if i not in seen]
                seen = seen.union(set(tmp))
                l.extend(tmp)
            return seen
        d2 = {}
        k = d.keys()
        for i in k:
            d2[i] = dricher(i)
        rst = []
        for i in range(N):
            richers = d2[i]
            rst.append(min(richers, key=lambda x:quiet[x]) if richers else i)
        return rst




class Test(unittest.TestCase):

    def test(self):
        cases = [
            [dict(richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0]), [5,5,2,5,4,5,6,7]],
            [dict(richer =[[0,1]], quiet=[1,0]), [0,1]]
        ]
        for ci, co in cases:
            tmp = Solution().loudAndRich(**ci)
            print(tmp)
            assert tmp == co
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

    def est_tree_draw(self):
        tree_draw(tree_deserialize('[1,2,3,4,5,6,7]'))

if __name__ == '__main__':
    unittest.main(exit=False)
