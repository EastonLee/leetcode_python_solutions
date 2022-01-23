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
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        self.x, self.y, self.d = 0, 0, 0
        def step(c):
            if c in [-2, -1]:
                self.d += [-1,1][c == -1]
                self.d %= 4
            else:
                for i in range(c):
                    tx, ty = self.x, self.y
                    if self.d == 0:
                        ty += 1
                    if self.d == 1:
                        tx += 1
                    if self.d == 2:
                        ty -= 1
                    if self.d == 3:
                        tx -= 1
                    if [tx,ty] in obstacles:
                        break
                    else:
                        self.x, self.y = tx, ty
                    print(self.x, self.y)

        for c in commands:
            step(c)
        # print(self.x, self.y, self.d)
        return self.x ** 2 + self.y ** 2


class Test(unittest.TestCase):

    def test(self):
        cases = [
            [dict(commands = [4,-1,3], obstacles = []), 25],
            [dict(commands = [4,-1,4,-2,4], obstacles = [[2,4]]), 65],
            [dict(commands = [2,5,2,5,-1,3,4,2,4,-2,5,8,-1,-2,-2,-1,8,-1,-2,-2,-1,-1,5,-1,-1,1,5,9,1,-1,-2,-1,-2,3,7,2,3,5,9,-2,5,2,1,4,6,5,9,1,9,6,3,-1,-1,9,9,-1,1,6,3,-2,2,2,5,-1,-1,-2,9,6,5,5,9,2,5,-2,-2,5,7,-1,-2,-1,2,-1,1,-1,-1,2,8,-1,8,3,-2,3,-1,-2,4,7,3,8,-1,2], obstacles = [[-5,-77],[35,40],[58,-30],[31,-96],[40,14],[-25,50],[37,-38],[-54,-31],[64,-41],[72,53],[83,-95],[-31,-61],[68,32],[-56,16],[88,-81],[-48,-31],[56,-57],[-74,24],[-42,-59],[72,-86],[40,34],[-85,-45],[22,-35],[-95,56],[-66,42],[-67,94],[46,10],[35,27],[-9,-6],[-84,-97],[38,-22],[3,-39],[71,-97],[-40,-86],[-45,56],[-91,59],[24,-11],[91,100],[-68,43],[34,27],[-60,32],[-20,34],[-34,34],[-31,-53],[52,-98],[-70,-15],[73,-41],[-94,95],[-78,-42],[-7,-11],[-37,-94],[26,-74],[-53,68],[72,2],[-80,-58],[-94,48],[-80,-57],[-35,69],[17,-45],[-72,-76],[21,99],[-25,-19],[-48,86],[86,-47],[59,-66],[-38,-16],[47,-44],[28,96],[92,-64],[-62,-35],[-63,-87],[-83,95],[25,-89],[30,-40],[-75,93],[47,-21],[12,-93],[70,-22],[-64,-43],[-17,-86],[-33,93],[-74,-7],[-78,5],[-37,-11],[-84,-29],[-29,-11],[17,9],[-64,10],[25,29],[14,25],[19,42],[71,52],[30,-76],[19,66],[40,99],[-61,-95],[-17,40],[6,-21],[7,28],[-4,85],[71,99],[50,99],[-53,-95],[-8,8],[63,-79],[88,-35],[50,-38],[-60,-31],[-2,-8],[-8,91],[-14,50],[-25,-26],[1,71],[-91,-64],[-40,46],[30,-97],[9,-55],[-36,-75],[71,99],[90,-53],[-68,-20],[-73,89],[-14,74],[-8,72],[82,48],[45,2],[-42,12],[77,22],[87,56],[73,-21],[78,15],[-6,-75],[24,46],[-11,-70],[-90,-77],[57,43],[-66,10],[-30,-47],[91,-37],[-4,-67],[-88,19],[66,29],[86,97],[-4,67],[54,-92],[-54,71],[-42,-17],[57,-91],[-9,-15],[-26,56],[-57,-58],[-72,91],[-55,35],[-20,29],[51,70],[-61,88],[-62,99],[52,17],[-75,-32],[91,-22],[54,33],[-45,-59],[47,-48],[53,-98],[-91,83],[81,12],[-34,-90],[-79,-82],[-15,-86],[-24,66],[-35,35],[3,31],[87,93],[2,-19],[87,-93],[24,-10],[84,-53],[86,87],[-88,-18],[-51,89],[96,66],[-77,-94],[-39,-1],[89,51],[-23,-72],[27,24],[53,-80],[52,-33],[32,4],[78,-55],[-25,18],[-23,47],[79,-5],[-23,-22],[14,-25],[-11,69],[63,36],[35,-99],[-24,82],[-29,-98]]), 0]
        ]
        for ci, co in cases:
            tmp = Solution().robotSim(**ci)
            print(tmp)
            assert tmp == co
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

    def est_tree_draw(self):
        tree_draw(tree_deserialize('[1,2,3,4,5,6,7]'))

if __name__ == '__main__':
    unittest.main(exit=False)
