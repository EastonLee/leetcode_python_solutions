import unittest
from pprint import pprint
import re
import cProfile
import heapq
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

    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        def all_subs_no(n):
            return n*(n+1)/2
        def proc_sec(l):
            res = 0
            n = len(l)
            sep = [i for i,j in enumerate(l) if j >=L and j<=R]
            if not sep: return 0
            for i,s in enumerate(sep):
                if i == 0:
                    res += all_subs_no(s)
                else:
                    res += all_subs_no(s-sep[i-1]-1)
                if i == len(sep)-1:
                    res += all_subs_no(n-s-1)
            return all_subs_no(n) - res

        sep = [i for i,j in enumerate(A) if j > R]
        res = 0
        for i,s in enumerate(sep):
            if i == 0:
                res += proc_sec(A[:s])
            else:
                res += proc_sec(A[sep[i-1]+1:s])
            if i == len(sep)-1:
                res += proc_sec(A[s+1:])
            
        return res

class Test(unittest.TestCase):

    def test(self):
        A = [2, 1, 4, 3]
        L = 2
        R = 3
        #assert Solution().numSubarrayBoundedMax(A,L,R) == 3
        A=[2,9,2,5,6]
        L=2
        R=8
        assert Solution().numSubarrayBoundedMax(A,L,R) == 7
        A=[16,69,88,85,79,87,37,33,39,34]
        L=55
        R=57
        assert Solution().numSubarrayBoundedMax(A,L,R) == 0
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

    def est_tree_draw(self):
        tree_draw(tree_deserialize('[1,2,3,4,5,6,7]'))

if __name__ == '__main__':
    unittest.main()
