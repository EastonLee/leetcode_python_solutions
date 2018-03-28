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


class Poly(collections.Counter):
    def __add__(self, other):
        self.update(other)
        return self

    def __sub__(self, other):
        self.update({k: -v for k, v in other.items()})
        return self

    def __mul__(self, other):
        ans = Poly()
        for k1, v1 in self.items():
            for k2, v2 in other.items():
                ans.update({tuple(sorted(k1 + k2)): v1 * v2})
        return ans

    def evaluate(self, evalmap):
        ans = Poly()
        for k, c in self.items():
            free = []
            for token in k:
                if token in evalmap:
                    c *= evalmap[token]
                else:
                    free.append(token)
            ans[tuple(free)] += c
        return ans

    def to_list(self):
        return ["*".join((str(v),) + k)
                for k, v in sorted(self.items(),
                    key = lambda x: (-len(x[0]), x[0], x[1]))
                if v]

# https://leetcode.com/problems/basic-calculator-iv/solution/
class Solution(object):
    def basicCalculatorIV(self, expression, evalvars, evalints):
        evalmap = dict(zip(evalvars, evalints))

        def combine(left, right, symbol):
            if symbol == '+': return left + right
            if symbol == '-': return left - right
            if symbol == '*': return left * right
            raise

        def make(expr):
            ans = Poly()
            if expr.isdigit():
                ans.update({(): int(expr)})
            else:
                ans[(expr,)] += 1
            return ans

        def parse(expr):
            bucket = []
            symbols = []
            i = 0
            while i < len(expr):
                if expr[i] == '(':
                    bal = 0
                    for j in range(i, len(expr)):
                        if expr[j] == '(': bal += 1
                        if expr[j] == ')': bal -= 1
                        if bal == 0: break
                    bucket.append(parse(expr[i+1:j]))
                    i = j
                elif expr[i].isalnum():
                    for j in range(i, len(expr)):
                        if expr[j] == ' ':
                            bucket.append(make(expr[i:j]))
                            break
                    else:
                        bucket.append(make(expr[i:]))
                    i = j
                elif expr[i] in '+-*':
                    symbols.append(expr[i])
                i += 1

            for i in range(len(symbols) - 1, -1, -1):
                if symbols[i] == '*':
                    bucket[i] = combine(bucket[i], bucket.pop(i+1),
                                        symbols.pop(i))

            if not bucket: return Poly()
            ans = bucket[0]
            for i, symbol in enumerate(symbols, 1):
                ans = combine(ans, bucket[i], symbol)

            return ans

        P = parse(expression).evaluate(evalmap)
        return P.to_list()


class Test(unittest.TestCase):

    def test(self):
        cases = [
            #[dict(expression = "e + 8 - a + 5", evalvars = ["e"], evalints = [1]), ["-1*a","14"]],
            #[dict(expression = "e - 8 + temperature - pressure",
            #    evalvars = ["e", "temperature"], evalints = [1, 12]), ["-1*pressure","5"]],
            [dict(expression = "(e + 8) * (e - 8)", evalvars = [], evalints = []), ["1*e*e","-64"]],
            #[dict(expression = "7 - 7", evalvars = [], evalints = []), []],
            #[dict(expression = "a * b * c + b * a * c * 4", evalvars = [], evalints = []), ["5*a*b*c"]],
            #[dict(expression = "((a - b) * (b - c) + (c - a)) * ((a - b) + (b - c) * (c - a))",
            #    evalvars = [], evalints = []), ["-1*a*a*b*b","2*a*a*b*c","-1*a*a*c*c","1*a*b*b*b","-1*a*b*b*c","-1*a*b*c*c","1*a*c*c*c","-1*b*b*b*c","2*b*b*c*c","-1*b*c*c*c","2*a*a*b","-2*a*a*c","-2*a*b*b","2*a*c*c","1*b*b*b","-1*b*b*c","1*b*c*c","-1*c*c*c","-1*a*a","1*a*b","1*a*c","-1*b*c"]]
        ]
        for ci, co in cases:
            assert Solution().basicCalculatorIV(**ci) == co
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

    def est_tree_draw(self):
        tree_draw(tree_deserialize('[1,2,3,4,5,6,7]'))

if __name__ == '__main__':
    unittest.main(exit=False)
