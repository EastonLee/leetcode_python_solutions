'''
On a horizontal number line, we have gas stations at positions stations[0], stations[1], ..., stations[N-1], where N = stations.length.

Now, we add K more gas stations so that D, the maximum distance between adjacent gas stations, is minimized.

Return the smallest possible value of D.
'''
import unittest
from pprint import pprint
import re
import cProfile
import heapq
import bisect
import collections
import itertools
import numpy as np
import math

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

# I cant see this problem, it's only open to premium members
# http://bookshadow.com/weblog/2018/01/28/leetcode-minimize-max-distance-to-gas-station/
class Solution(object):

    def minmaxGasDist(self, stations, K):
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """
        stations.sort()
        step = 1e-9
        left, right = 0, 1e9
        while left <= right:
            mid = (left + right) / 2
            if self.isValid(mid, stations, K):
                right = mid - step
            else:
                left = mid + step
        return mid
    def isValid(self, gap, stations, K):
        for x in range(len(stations) - 1):
            dist = stations[x + 1] - stations[x]
            K -= int(math.ceil(dist / gap)) - 1
        return K >= 0



class Test(unittest.TestCase):

    def test(self):
        stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; K = 9
        print(Solution().minmaxGasDist(stations, K))
        assert abs(Solution().minmaxGasDist(stations, K) - 0.5) <= 1e-6
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

    def est_tree_draw(self):
        tree_draw(tree_deserialize('[1,2,3,4,5,6,7]'))

if __name__ == '__main__':
    unittest.main(exit=False)
