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

    # slow
    def preimageSizeFZF2(self, K):
        """
        :type K: int
        :rtype: int
        """
        def no_factor5(n):
            c = 0
            while n % 5 == 0 and n:
                n = n / 5
                c += 1
            return c
        i, c = 0, 0
        while c < K:
            i += 1
            c += no_factor5(i) + 1
        return 0 if c > K else 5

    # fast, binary search
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        def no_of0(n): # count how many zeros in this factorial
            bits_based_on_5 = [] # number system based 5
            n = n / 5 * 5
            while n:
                bits_based_on_5.append(n%5)
                n = n / 5
            res = [j*(5**i-1)/4 for i,j in enumerate(bits_based_on_5)]
            return sum(res)

        l, r, m = 0, K*5, K*5/2 # binary search
        while m < r:
            mv = no_of0(m)
            if mv < K:
                l = m + 1
            elif mv > K:
                r = m - 1
            else:
                return 5
            m = (l + r) / 2
        return 5 if no_of0(m) == K else 0

    # this is a better solution
    # https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/discuss/117632/binary-search-python-code-40ms
    def preimageSizeFZF2(self, K):
        # return the no of tailing 0s ( = 5s as factor ) in factorial(n)
        def nzero(n):
            f = 5
            cnt = 0
            while f <= n:
                cnt += n // f
                f *= 5
            return cnt

        if K == 0:
            return 5

        min = 1
        max = K * 5
        while min < max:
            mid = (min + max) // 2
            if nzero(mid) < K:
                min = mid + 1
            else:
                max = mid

        if nzero(min) != K:
            return 0
        else:
            # next = (min // 5 + 1) * 5
            # return next - min
            return 5

class Test(unittest.TestCase):

    def test(self):
        print Solution().preimageSizeFZF(80502705)
        assert Solution().preimageSizeFZF(0) == 5
        assert Solution().preimageSizeFZF(5) == 0
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

    def est_tree_draw(self):
        tree_draw(tree_deserialize('[1,2,3,4,5,6,7]'))

if __name__ == '__main__':
    unittest.main(exit=False)
