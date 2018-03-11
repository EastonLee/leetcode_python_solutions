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

    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        m = [[0] * (i+1) for i in range(101)]
        m[0][0] = float(poured)
        for i in range(100):
            for j in range(i+1):
                v = m[i][j]
                if v > 1:
                    m[i+1][j] += (v-1)/2
                    m[i+1][j+1] += (v-1)/2
                    m[i][j] = 1
        return m[query_row][query_glass]

class Test(unittest.TestCase):

    def test(self):
        poured = 1; query_glass = 1; query_row = 1
        assert Solution().champagneTower(poured, query_row, query_glass) == 0
        poured = 2; query_glass = 1; query_row = 1
        assert Solution().champagneTower(poured, query_row, query_glass) == 0.5
        poured = 0; query_glass = 0; query_row = 0
        assert Solution().champagneTower(poured, query_row, query_glass) == 0
        poured = 4; query_glass = 0; query_row = 2
        assert Solution().champagneTower(poured, query_row, query_glass) == 0.25
        poured = 4; query_glass = 2; query_row = 2
        assert Solution().champagneTower(poured, query_row, query_glass) == 0.25
        poured = 6; query_glass = 0; query_row = 2
        assert Solution().champagneTower(poured, query_row, query_glass) == 0.75
        poured = 1000000000; query_glass = 99; query_row = 99
        assert Solution().champagneTower(poured, query_row, query_glass) == 0
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

    def est_tree_draw(self):
        tree_draw(tree_deserialize('[1,2,3,4,5,6,7]'))

if __name__ == '__main__':
    unittest.main(exit=False)
