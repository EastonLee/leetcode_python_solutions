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
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        self.fives, self.tens = 0, 0
        def can_change(i):
            if i == 0: return True
            if i == 5:
                if bool(self.fives):
                    self.fives -= 1
                    return True
                return False
            if i == 10:
                if self.tens:
                    self.tens -= 1
                    return True
                if self.fives >= 2:
                    self.fives -= 2
                    return True
                return False
            if i == 15:
                if (bool(self.tens) and bool(self.fives)):
                    self.tens -= 1
                    self.fives -= 1
                    return True
                if self.fives >= 3:
                    self.fives -= 3
                    return True
                return False
        
        for b in bills:
            if not can_change(b - 5):
                return False
            if b ==  5:
                self.fives += 1
            if b == 10:
                self.tens += 1
            
        return True




class Test(unittest.TestCase):

    def test(self):
        cases = [
            [[5,5,5,10,20], True],
            [[5,5,10], True],
            [[10, 10], False],
            [[5,5,10,10,20], False]
        ]
        for ci, co in cases:
            tmp = Solution().lemonadeChange(ci)
            print(tmp)
            assert tmp == co
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

    def est_tree_draw(self):
        tree_draw(tree_deserialize('[1,2,3,4,5,6,7]'))

if __name__ == '__main__':
    unittest.main(exit=False)
