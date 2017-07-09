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
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        def tok(s):
            return [i for i in re.findall(r'[+-]?\d*x?', s) if i]
        def count_x(l):
            tmp = []
            for i in l:
                if i in ['x', '+x']:
                    tmp.append(1)
                elif i == '-x':
                    tmp.append(-1)
                else:
                    tmp.append(int(re.search(r'[+-]?\d+', i).group()))
            return sum(tmp)

        def exe_n(l):
            l = ''.join(l)
            if not l:
                return 0
            return eval(l)
                
        left, right = equation.split('=')
        left = tok(left)
        right = tok(right)
        l_x = [i for i in left if 'x' in i]
        l_n = [i for i in left if 'x' not in i]
        r_x = [i for i in right if 'x' in i]
        r_n = [i for i in right if 'x' not in i]
        l_x_c = count_x(l_x)
        l_n = exe_n(l_n)
        r_x_c = count_x(r_x)
        r_n = exe_n(r_n)
        left = l_x_c - r_x_c
        right = r_n - l_n
        if left ==0 and right == 0 :
            return "Infinite solutions"
        if left == 0 and right != 0:
            return "No solution"
        return 'x={}'.format(right/left)


class Test(unittest.TestCase):

    def test(self):
        case = "x+5-3+x=6+x-2"
        assert Solution().solveEquation(case) == "x=2"
        case = "x=x"
        assert Solution().solveEquation(case) == "Infinite solutions"
        case = "2x=x"
        assert Solution().solveEquation(case) == "x=0"
        case = "2x+3x-6x=x+2"
        assert Solution().solveEquation(case) == "x=-1"
        case = "x=x+2"
        assert Solution().solveEquation(case) == "No solution"
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')


if __name__ == '__main__':
    unittest.main()
