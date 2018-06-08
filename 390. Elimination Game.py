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
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        right = 1
        l = list(range(1,n+1))
        while len(l) > 1:
            for i in l[::2*right]:
                l.remove(i)
            right *= -1
        return l[0]
        
    def lastRemaining(self, n):
        def chain(l):
            if not l:
                return lambda x:x
            rst = l[-1]
            if len(l) > 1:
                for i in l[-2::-1]:
                    rst = lambda x,i=i,rst=rst: i(rst(x))
            return rst
        
        l = []
        right = 1
        while n>1:
            if n%2 == 0:
                if right == 1:
                    l.append(lambda x:2*x)
                else:
                    l.append(lambda x: 2*x - 1)
            else:
                l.append(lambda x:2*x)
            n = n // 2
            right *= -1
        
        chainup = chain(l)
        return chainup(1)

    # https://leetcode.com/problems/elimination-game/discuss/122415/5-lines-simple-iteration-solution
    # by @linfongi
    def lastRemaining(self, n):
        first, step = 1, 1
        while n > 1:
            if step % 2 or n % 2:
                first += 2**(step-1)
            step += 1
            n //= 2
        return first

class Test(unittest.TestCase):

    def test(self):
        cases = [
            [9, 6],
            [1,1],
            [2,2],
            [3,2]
        ]
        for ci, co in cases:
            tmp = Solution().lastRemaining(ci)
            print(tmp)
            assert tmp == co
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

    def est_tree_draw(self):
        tree_draw(tree_deserialize('[1,2,3,4,5,6,7]'))

if __name__ == '__main__':
    unittest.main(exit=False)
