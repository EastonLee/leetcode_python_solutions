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

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def inorder(node):
            if node:
                for val in inorder(node.left):
                    yield val
                yield node.val
                for val in inorder(node.right):
                    yield val
        l = [-float('inf')] + [i for i in inorder(root)]
        return min(l[i] - l[i-1] for i in range(1, len(l)))


class Test(unittest.TestCase):

    def test(self):
        case = "[4,2,6,1,3,null,null]"
        assert Solution().minDiffInBST(tree_deserialize(case)) == 1
        case = "[4,2,6,1,3,null,null]"
        assert Solution().minDiffInBST(tree_deserialize(case)) == 1
        case = "[27,null,34,null,58,50,null,44,null,null,null]"
        assert Solution().minDiffInBST(tree_deserialize(case)) == 6
        case = "[90,69,null,49,89,null,52,null,null,null,null]"
        assert Solution().minDiffInBST(tree_deserialize(case)) == 1
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

    def est_tree_draw(self):
        tree_draw(tree_deserialize('[1,2,3,4,5,6,7]'))

if __name__ == '__main__':
    unittest.main(exit=False)
