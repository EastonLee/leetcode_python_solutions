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

    def movesToChessboard(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        N = len(board[0])
        col_density = sum(board[0])
        row_density = sum(board[i][0] for i in range(N))
        if not N/2 <= col_density <= (N+1)/2: return -1
        if not N/2 <= row_density <= (N+1)/2: return -1
        c1 = collections.Counter(tuple(i) for i in board)
        if not len(c1) == 2: return -1
        if any(c1.keys()[0][i] == c1.keys()[1][i] for i in range(N)): return -1
        c2 = collections.Counter(zip(*board))
        if not len(c2) == 2: return -1
        if any(c2.keys()[0][i] == c2.keys()[1][i] for i in range(N)): return -1
        
        col_match = sum(board[0][i] == i%2 for i in range(N))
        row_match = sum(board[i][0] == i%2 for i in range(N))
        if N % 2:
            if col_match % 2: col_match = N - col_match
            if row_match % 2: row_match = N - row_match
        else:
            col_match = min(col_match, N - col_match)
            row_match = min(row_match, N - row_match)
        return (col_match + row_match) / 2
            


class Test(unittest.TestCase):

    def test(self):
        #board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
        #assert Solution().movesToChessboard(board) == 2
        #board = [[0, 1], [1, 0]]
        #assert Solution().movesToChessboard(board) == 0
        #board = [[1, 1], [0, 0]]
        #assert Solution().movesToChessboard(board) == -1
        board = [[1,1,0],[0,0,1],[0,0,1]]
        assert Solution().movesToChessboard(board) == 2
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

    def est_tree_draw(self):
        tree_draw(tree_deserialize('[1,2,3,4,5,6,7]'))

if __name__ == '__main__':
    unittest.main(exit=False)
