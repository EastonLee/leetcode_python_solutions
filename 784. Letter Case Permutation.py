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

    # by @lee215
    def letterCasePermutation1(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        def letterCasePermutation(self, S):
            L = [[i.lower(), i.upper()] if i.isalpha() else i for i in S]
        return [''.join(i) for i in itertools.product(*L)]

    # https://leetcode.com/problems/letter-case-permutation/discuss/115508/Java-solution-using-recursion
    def letterCasePermutation(self, S):
        idx = [i if j.isalpha() else None for i,j in enumerate(S)]
        idx = filter(lambda x:x is not None, idx)
        res = []

        def helper(s, i, length):
            if i == length:
                res.append(s)
                return
            helper(s[:idx[i]] + s[idx[i]].lower() + s[idx[i]+1:], i+1, length)
            helper(s[:idx[i]] + s[idx[i]].upper() + s[idx[i]+1:], i+1, length)
        
        helper(S, 0, len(idx))
        return res


class Test(unittest.TestCase):

    def test(self):
        case = "a1b2"
        assert Solution().letterCasePermutation(case) == ["a1b2", "a1B2", "A1b2", "A1B2"]
        case = "3z4"
        assert Solution().letterCasePermutation(case) == ["3z4", "3Z4"]
        case = "12345"
        assert Solution().letterCasePermutation(case) == ["12345"]
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

if __name__ == '__main__':
    unittest.main()
