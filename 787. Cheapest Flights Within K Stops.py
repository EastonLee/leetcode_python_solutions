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

    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        flights = {(x[0], x[1]): x[2] for x in flights}
        if K == 0:
            return flights[(src, dst)] if (src, dst) in flights else -1
        dp = [[None] * n for i in range(K+1)] # a (K+1) * n matrix
        for i in range(n):
            if (i, dst) in flights:
                dp[0][i] = flights[(i, dst)]
        for i in range(1, K+1):
            for j in range(n): # this line
                viable_paths = []
                for k in range(n): # last line
                    if (j, k) in flights and dp[i-1][k]:
                        viable_paths.append(flights[(j,k)] + dp[i-1][k])
                if viable_paths:
                    dp[i][j] = min(viable_paths)
        res = min([i[src] or float('inf') for i in dp])
        return res if not res == float('inf') else -1


class Test(unittest.TestCase):

    def test(self):
        n = 3; edges = [[0,1,100],[1,2,100],[0,2,500]]
        src = 0; dst = 2; k = 1
        assert Solution().findCheapestPrice(n, edges, src, dst, k) == 200
        n = 3; edges = [[0,1,100],[1,2,100],[0,2,500]]
        src = 0; dst = 2; k = 0
        assert Solution().findCheapestPrice(n, edges, src, dst, k) == 500
        n = 5; edges = [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]]
        src = 2; dst = 1; k = 1
        assert Solution().findCheapestPrice(n, edges, src, dst, k) == -1
        n = 10; edges = [[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]]
        src = 6; dst = 0; k = 7
        assert Solution().findCheapestPrice(n, edges, src, dst, k) == 14
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

    def est_tree_draw(self):
        tree_draw(tree_deserialize('[1,2,3,4,5,6,7]'))

if __name__ == '__main__':
    unittest.main()
