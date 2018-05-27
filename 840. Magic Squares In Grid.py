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
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def is_magic(grid):
            if any(map(lambda x:x<1 or x>9, [item for sublist in grid for item in sublist])):
                return False
            if grid[1][1] != 5:
                return False
            if not sum(grid[0]) == sum(grid[0]) == sum(grid[0]) == 15:
                return False
            trans = list(zip(*grid))
            if not sum(trans[0]) == sum(trans[0]) == sum(trans[0]) == 15:
                return False
            if not (sum((grid[0][0], grid[1][1], grid[2][2])) == sum((grid[0][2], grid[1][1], grid[2][0])) == 15):
                return False
            return True
        
        N = len(grid)
        rst = 0
        for i in range(2, N):
            for j in range(2, len(grid[0])):
                if is_magic([[grid[k][j-2],grid[k][j-1],grid[k][j]] for k in (i-2,i-1,i)]):
                    rst += 1
        return rst
            



class Test(unittest.TestCase):

    def test(self):
        cases = [
            [[[4,3,8,4],[9,5,1,9],[2,7,6,2]], 1],
            [[[1,8,6],[10,5,0],[4,2,9]], 0]
        ]
        for ci, co in cases:
            tmp = Solution().numMagicSquaresInside(ci)
            print(tmp)
            assert tmp == co
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

    def est_tree_draw(self):
        tree_draw(tree_deserialize('[1,2,3,4,5,6,7]'))

if __name__ == '__main__':
    unittest.main(exit=False)
