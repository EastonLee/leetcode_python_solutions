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
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        theory_length = 0
        first = A[0]
        while first <= A[-1]:
            first  = first * 2 +1
            theory_length += 1
        theory_length = 2 * theory_length -1

        idx = bisect.bisect(A, A[-1]/2)
        firsts = A[:idx]
        rst = []
        for f in firsts:
            length = 2
            for s in A[bisect.bisect(A,f):]:
                n1 = s
                n2 = f + s
                while n2 in A:
                    length += 1
                    if length == theory_length:
                        return length
                    n1, n2 = n2, n2 + n1
                if length >= 3:
                    rst.append(length)
        print(rst)
        return max(rst) if rst else 0



class Test(unittest.TestCase):

    def test(self):
        cases = [
            [[1,2,3,4,5,6,7,8], 5],
            [[1,3,7,11,12,14,18], 3],
            [[1,3,5], 0],
            [[2,4,7,8,9,10,14,15,18,23,32,50], 5]
        ]
        for ci, co in cases:
            tmp = Solution().lenLongestFibSubseq(ci)
            print(tmp)
            assert tmp == co
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

    def est_tree_draw(self):
        tree_draw(tree_deserialize('[1,2,3,4,5,6,7]'))

if __name__ == '__main__':
    unittest.main(exit=False)
