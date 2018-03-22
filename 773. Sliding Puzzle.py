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

    # https://leetcode.com/problems/sliding-puzzle/discuss/113614/Simple-Python-solution-using-A*-search
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        self.scores = [0] * 6
        goal_pos = {1:(0, 0), 2:(0, 1), 3: (0, 2), 4: (1,0), 5:(1,1), 0:(1, 2)}

        for num in range(6): # Pre calculate manhattan distances
            self.scores[num] = [[abs(goal_pos[num][0] - i) + abs(goal_pos[num][1] - j) for j in range(3)] for i in range(2)]
        from collections import namedtuple
        Node = namedtuple('Node', ['heuristic_score', 'distance', 'board'])
        heap = [Node(0, 0, board)]
        closed = []

        while len(heap) > 0:
            node = heapq.heappop(heap)
            if self.get_score(node.board) == 0:
                return node.distance
            elif node.board in closed:
                continue
            else:
                for neighbor in self.get_neighbors(node.board):
                    if neighbor in closed: continue
                    heapq.heappush(heap, Node(node.distance + 1 + self.get_score(neighbor), node.distance + 1, neighbor))
            closed.append(node.board)
        return -1

    def get_neighbors(self, board):
        import copy
        r, c = (0, board[0].index(0)) if 0 in board[0] else (1, board[1].index(0))
        res = []

        for offr, offc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            if 0 <= r + offr < 2 and 0 <= c + offc < 3:
                board1 = copy.deepcopy(board)
                board1[r][c], board1[r+offr][c+offc] = board1[r+offr][c+offc], board1[r][c]
                res.append(board1)
        return res

    def get_score(self, board):
        return sum([self.scores[board[i][j]][i][j] for i in range(2) for j in range(3)])


class Test(unittest.TestCase):

    def test(self):
        board = [[1,2,3],[4,0,5]]
        assert Solution().slidingPuzzle(board) == 1
        board = [[1,2,3],[5,4,0]]
        assert Solution().slidingPuzzle(board) == -1
        board = [[4,1,2],[5,0,3]]
        assert Solution().slidingPuzzle(board) == 5
        board = [[3,2,4],[1,5,0]]
        assert Solution().slidingPuzzle(board) == 14
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

    def est_tree_draw(self):
        tree_draw(tree_deserialize('[1,2,3,4,5,6,7]'))

if __name__ == '__main__':
    unittest.main(exit=False)

