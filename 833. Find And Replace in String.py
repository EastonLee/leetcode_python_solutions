#!/usr/bin/env python
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

    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        rst = []
        cover = []
        sliced = []
        for idx,(i,s,t) in enumerate(zip(indexes, sources, targets)):
            cover.append(list(range(i,i+len(s))))
            sub = S[i:i+len(s)]
            if sub == s:
                sliced.append(t)
            else:
                sliced.append(sub)
        heads = [i[0] for i in cover]
        for i in range(len(S)):
            if not any([i in j for j in cover]):
                rst.append(S[i])
            elif i in heads:
                idx = heads.index(i)
                rst.extend(sliced[idx])
        return ''.join(rst)

        

        


class Test(unittest.TestCase):

    def test(self):
        cases = [
            [["abcd",[0,2],["a","cd"],["eee","ffff"]], 'eeebffff'],
            [["abcd", [0,2], ["ab","ec"], ["eee","ffff"]], 'eeecd'],
            [["vmokgggqzp",[3,5,1],["kg","ggq","mo"],["s","so","bfr"]], "vbfrssozp"]
        ]
        for ci, co in cases:
            print(Solution().findReplaceString(*ci))
            assert Solution().findReplaceString(*ci) == co
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

    def est_tree_draw(self):
        tree_draw(tree_deserialize('[1,2,3,4,5,6,7]'))

if __name__ == '__main__':
    unittest.main(exit=False)
