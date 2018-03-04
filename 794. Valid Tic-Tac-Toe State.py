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
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        board = ''.join(board)
        if not (board.count('X') - board.count('O')) in [0, 1]: return False
        def win(w, b):
            if any([all(map(lambda x:x==w, board[0:3])),
                all(map(lambda x:x==w, board[3:6])),
                all(map(lambda x:x==w, board[6:9])),
                all(map(lambda x:x==w, board[0:9:3])),
                all(map(lambda x:x==w, board[1:9:3])),
                all(map(lambda x:x==w, board[2:9:3])),
                all(map(lambda x:x==w, board[0:9:4])),
                all(map(lambda x:x==w, board[2:9:2])),
                ]): return True
            return False
        if win('X', board) and win('O', board): return False
        if win('X', board) and board.count('X') == board.count('O'): return False
        if win('O', board) and board.count('X') == board.count('O') + 1: return False
        
        return True


class Test(unittest.TestCase):

    def test(self):
        board = ["O  ", "   ", "   "]
        assert Solution().validTicTacToe(board) == False
        board = ["XOX", " X ", "   "]
        assert Solution().validTicTacToe(board) == False
        board = ["XXX", "   ", "OOO"]
        assert Solution().validTicTacToe(board) == False
        board = ["XOX", "O O", "XOX"]
        assert Solution().validTicTacToe(board) == True
        board = ["XXX","XOO","OO "]
        assert Solution().validTicTacToe(board) == False
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

    def est_tree_draw(self):
        tree_draw(tree_deserialize('[1,2,3,4,5,6,7]'))

if __name__ == '__main__':
    unittest.main()
