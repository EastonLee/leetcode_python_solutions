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
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        root.level = 1
        s = collections.deque([root])
        ans = []
        tmp_sum = 0
        tmp_count = 0
        while s:
            cur = s.popleft()
            if cur.left:
                cur.left.level = cur.level + 1
                s.append(cur.left)
            if cur.right:
                cur.right.level = cur.level + 1
                s.append(cur.right)

            if len(s) == 0 or cur.level < s[0].level:
                ans.append((tmp_sum + cur.val)/float(tmp_count + 1))
                tmp_sum, tmp_count = 0, 0
            else:
                tmp_sum += cur.val
                tmp_count += 1
        return ans

class Test(unittest.TestCase):

    def test(self):
        case = tree_deserialize('[3,9,20,null,null,15,7]')
        assert Solution().averageOfLevels(case) == [3, 14.5, 11]
        case = tree_deserialize('[5,14,null,1]')
        assert Solution().averageOfLevels(case) == [5.00000,14.00000,1.00000]
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

if __name__ == '__main__':
    unittest.main()
