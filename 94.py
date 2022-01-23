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
    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        self.count = 0
        self.A, self.B = list(A), list(B)
        def remove_same():
            N = len(self.A)
            for i in range(N-1,-1,-1):
                if self.A[i] == self.B[i]:
                    self.A.pop(i)
                    self.B.pop(i)

        def remove_symetric():
            # same slots should've been removed
            pairs = list(zip(self.A, self.B))
            N = len(self.A)
            for i in range(N):
                if pairs[i] == [None, None]: continue
                if pairs[i][::-1] in pairs:
                    idx = pairs.index(pairs[i][::-1])
                    pairs[i] = pairs[idx] = [None, None]
                    self.count += 1
            pairs = list(zip(*pairs))
            self.A = list(filter(bool, pairs[0]))
            self.B = list(filter(bool, pairs[1]))

        def swap():
            first_a, first_b = self.A[0], self.B[0]
            idx_b = self.B.index(first_a)
            self.B[0] = self.B[idx_b]
            self.B[idx_b] = first_b
            self.count += 1

        while self.A:
            remove_same()
            if self.A:
                remove_symetric()
            if self.A:
                swap()

        return self.count

class Test(unittest.TestCase):

    def test(self):
        cases = [
            [['ab','ba'], 1],
            [['abc','bca'], 2],
            [['abac','baca'], 2],
            [['aabc','abca'], 2],
        ]
        for ci, co in cases:
            tmp = Solution().kSimilarity(*ci)
            print(tmp)
            assert tmp == co
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

    def est_tree_draw(self):
        tree_draw(tree_deserialize('[1,2,3,4,5,6,7]'))

if __name__ == '__main__':
    unittest.main(exit=False)
