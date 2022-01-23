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

    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        def helper(a, b):
            if b <= 0.5 * a + 7 or \
                b > a or \
                (a > 100 and b < 100):
                return False
            return True
        c = collections.Counter(ages).values()
        c = list(filter(lambda x:x>1, c))
        c = list(map(lambda x:x*(x-1)/2, c))
        rst = sum(c)
        aux = []
        ages = list(sorted(ages, reverse=True))
        N = len(ages)
        for i in range(N):
            for j in range(i+1, N):
                if helper(ages[i], ages[j]):
                    rst += 1
                    aux.append((ages[i], ages[j]))
        print(aux)    
        print(len(aux))
        return rst


class Test(unittest.TestCase):

    def test(self):
        cases = [
            [[16,16], 2],
            [[16,17,18], 2],
            [[20,30,100,110,120], 3],
            [[112, 110, 106, 100, 73, 71, 60, 46, 39, 35, 30, 26, 15, 6, 6], 29]
        ]
        for ci, co in cases:
            print(Solution().numFriendRequests(ci))
            assert Solution().numFriendRequests(ci) == co
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

    def est_tree_draw(self):
        tree_draw(tree_deserialize('[1,2,3,4,5,6,7]'))

if __name__ == '__main__':
    unittest.main(exit=False)
