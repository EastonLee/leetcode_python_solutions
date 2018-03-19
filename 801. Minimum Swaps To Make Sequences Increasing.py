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

    # same as codility Cobaltum 2018
    def solution(self, A, B):
        N = len(A)
        def is_inc(l):
            n = len(l)
            return all(l[i] > l[i-1] for i in range(1,n))
        if is_inc(A) and is_inc(B): return 0
        links = [[A[i],B[i]] for i in range(N)]
        def link_cand(p1,p2):
            s = sum(i1<i2 for i1 in p1 for i2 in p2)
            if 2 <= s <= 3: return 1
            if s == 4: return 2
            return 0
        def link_cands(p1, p2):
            comps = [[i1,i2] for i1 in p1 for i2 in p2]
            s = sum(i1<i2 for i1,i2 in comps)
            if s == 4: return [[p1,p2], [p1, p2[::-1]]]
            if s == 3:
                not_inc = list(filter(lambda x:x[0]>=x[1], comps))[0]
                n1, n2 = p1.index(not_inc[0]), p2.index(not_inc[1])
                return [[[p1[n1], p1[~n1]], [p2[~n2], p2[n2]]]]
            return []

        links_cands = [link_cands(links[i], links[i+1]) for i in range(0, N-1)]
        links_cands_len = [len(i) for i in links_cands]
        if any(i==0 for i in links_cands_len): return -1
        one_cand_links = []
        for i, c in enumerate(links_cands):
            if len(c) == 1:
                if i == 0 or len(links_cands[i-1]) == 2:
                    one_cand_links.append([[c[0],i]])
                elif len(links_cands[i-1]) == 1:
                    one_cand_links[-1].append([c[0],i])
        def min_swap(l):
            def diffs(a,b):
                N = len(a)
                return sum(a[i] != b[i] for i in range(N))
            for i,[j,k] in enumerate(l[1:]):
                if j[0] != l[i][0][1]:
                    j[0] = j[0][::-1]
                    j[1] = j[1][::-1]
            link = [i[0][0] for i in l] + [l[-1][0][1]]
            z = list(zip(*link))
            a, b = z[0], z[1]
            linki = [i[1] for i in l] + [l[-1][1]+1]
            ao = [A[i] for i in linki]
            bo = [B[i] for i in linki]
            return min(diffs(a, ao), diffs(a, bo), diffs(b, ao), diffs(b, bo))
        return sum(min_swap(i) for i in one_cand_links)

    # https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/discuss/119830/Python-O(1)-space-O(n)-time-DP-solution
    def solution(self, A, B):
        import sys
        n = len(A)
        pre = [0, 1]
        for i in range(1, n):
            cur = [sys.maxsize, sys.maxsize]
            if A[i]>A[i-1] and B[i]>B[i-1]:
                cur[0] = min(cur[0], pre[0])
                cur[1] = min(cur[1], pre[1]+1)
            if A[i]>B[i-1] and B[i]>A[i-1]:
                cur[0] = min(cur[0], pre[1])
                cur[1] = min(cur[1], pre[0]+1)
            pre = cur
        return min(pre) if min(pre) != sys.maxsize else -1


class Test(unittest.TestCase):

    def test(self):
        A = [5,3,7,7,10]; B = [1,6,6,9,9]
        assert Solution().solution(A,B) == 2
        A = [5,-3,6,4,8]; B = [2,6,-5,1,0]
        print (Solution().solution(A,B))
        assert Solution().solution(A,B) == -1
        A = [1,5,6]; B = [-2,0,2]
        assert Solution().solution(A,B) == 0
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

    def est_tree_draw(self):
        tree_draw(tree_deserialize('[1,2,3,4,5,6,7]'))

if __name__ == '__main__':
    unittest.main(exit=False)

