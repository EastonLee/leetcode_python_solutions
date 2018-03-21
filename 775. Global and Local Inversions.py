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

    # https://leetcode.com/problems/global-and-local-inversions/discuss/113644/Easy-and-Concise-Solution-C++JavaPython
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        cmax = 0
        N = len(A)
        for i in range(N-2):
            cmax = max(cmax, A[i])
            if cmax > A[i+2]:
                return False
        return True

class Test(unittest.TestCase):

    def test(self):
        case = [1,0,2]
        assert Solution().isIdealPermutation(case) == True
        case = [1,2,0]
        assert Solution().isIdealPermutation(case) == False
        case = [0]
        assert Solution().isIdealPermutation(case) == True
        case = [0,1]
        assert Solution().isIdealPermutation(case) == True
        case = [1,0]
        assert Solution().isIdealPermutation(case) == True
        case = [2,0,3,1]
        assert Solution().isIdealPermutation(case) == False
        case = [0,3,2,1]
        assert Solution().isIdealPermutation(case) == False
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

    def est_tree_draw(self):
        tree_draw(tree_deserialize('[1,2,3,4,5,6,7]'))

if __name__ == '__main__':
    unittest.main(exit=False)

