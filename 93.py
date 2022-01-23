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


class ExamRoom:

    def __init__(self, N):
        """
        :type N: int
        """
        self.num = N
        self.s = []

    def seat(self):
        """
        :rtype: int
        """
        def intervals():
            res = []
            for i in range(len(self.s)):
                if i == 0:
                    if self.s[i] != 0:
                        res.append([0, self.s[i]])
                if i == len(self.s) - 1:
                    if self.s[i] != self.num-1:
                        res.append([self.s[i]+1, self.num-self.s[i]-1])
                if i != 0:
                    length = self.s[i] - self.s[i-1] - 1
                    if length > 0:
                        res.append([self.s[i-1]+1, length])
            return res
        
        def longest_dist(l):
            res = [-1,-1]
            for s, length in l:
                if s == 0:
                    res = [s, length]
                if s + length == self.num:
                    if length > res[1]:
                        res = [self.num-1, length]
                tmp = (length+1)//2
                if tmp > res[1]:
                    res = [s+(tmp-1), tmp]
            return res
                


        if not self.s:
            self.s.append(0)
            return 0

        ints = intervals()
        res = longest_dist(ints)
        bisect.insort(self.s, res[0])
        return res[0] 

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        self.s.remove(p)
        


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)




class Test(unittest.TestCase):

    def test(self):
        obj = ExamRoom(10)
        print(obj.seat())
        print(obj.seat())
        print(obj.seat())
        print(obj.seat())
        obj.leave(4)
        print(obj.seat())
        # cases = [
        #     [, ]
        # ]
        # for ci, co in cases:
        #     tmp = Solution().(**ci)
        #     print(tmp)
        #     assert tmp == co
        # #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

    def est_tree_draw(self):
        tree_draw(tree_deserialize('[1,2,3,4,5,6,7]'))

if __name__ == '__main__':
    unittest.main(exit=False)
