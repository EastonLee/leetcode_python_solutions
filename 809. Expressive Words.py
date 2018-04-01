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

    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        def convert(s):
            res = []
            count = 1
            for i in range(1, len(s)):
                if s[i] == s[i-1]:
                    count += 1
                if s[i] != s[i-1]:
                    res.append([s[i-1], count])
                    count = 1
                if i == len(s) - 1:
                    res.append([s[i], count])
            return res

        def compare(s, d):
            if len(s) != len(d):
                return False
            for i in range(len(s)):
                if s[i][0] != d[i][0]:
                    return False
                if d[i][1] < 3 and s[i][1] != d[i][1]:
                    return False
                if d[i][1] >= 3 and s[i][1] > d[i][1]:
                    return False
            return True

        target = convert(S)
        res = 0
        for w in words:
            w = convert(w)
            if compare(w, target):
                res += 1
        
        return res   


class Test(unittest.TestCase):

    def test(self):
        cases = [
            [dict(S = "heeellooo", words = ["hello", "hi", "helo"]), 1]
        ]
        for ci, co in cases:
            assert Solution().expressiveWords(**ci) == co
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

    def est_tree_draw(self):
        tree_draw(tree_deserialize('[1,2,3,4,5,6,7]'))

if __name__ == '__main__':
    unittest.main(exit=False)

