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

    # TLE
    def splitArraySameAverage2(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        N = len(A)
        average = sum(A) / N
        A.sort()
        if any(i==average for i in A): return True
        for i in range(2, N//2+1):
            if any(sum(j) == i*average for j in itertools.combinations(A, i)):
                return True
        return False

    # https://leetcode.com/problems/split-array-with-same-average/discuss/120654/Simple-python-with-explanation
    def splitArraySameAverage(self, A):
        if len(A)==1: return False
        global_avg = sum(A)/float(len(A))
        for lenB in range(1, len(A)//2+1):
            if int(lenB*global_avg) == lenB*global_avg:
                if self.exist(lenB*global_avg, lenB, A):
                    return True
        return False
            
    def exist(self, tosum, item_count, arr):
        if item_count==0:
            return False if tosum else True
        if item_count > len(arr) or not arr: 
            return False
        if any([self.exist(tosum-arr[0], item_count-1, arr[1:]),
               self.exist(tosum, item_count, arr[1:])]):
            return True
        return False

class Test(unittest.TestCase):

    def test(self):
        case = [5,3,11,19,2]
        case = [33,86,88,78,21,76,19,20,88,76,10,25,37,97,58,89,65,59,98,57,50,30,58,5,61,72,23,6]
        assert Solution().splitArraySameAverage(case) == False
        case = [1,2,3,4,5,6,7,8]
        assert Solution().splitArraySameAverage(case) == True
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

    def est_tree_draw(self):
        tree_draw(tree_deserialize('[1,2,3,4,5,6,7]'))

if __name__ == '__main__':
    unittest.main(exit=False)

