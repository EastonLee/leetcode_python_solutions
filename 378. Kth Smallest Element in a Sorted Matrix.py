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

    # https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85170/on-from-paper-yes-orows
    # this method is too tricky to be general
    # but has O(n) time and space complexity
    # not really worth remembering (I cant remember it for long)
    def kthSmallest1(self, matrix, k):
        # The median-of-medians selection function.
        def pick(a, k):
            if k == 1:
                return min(a)
            groups = (a[i:i+5] for i in range(0, len(a), 5))
            medians = [sorted(group)[len(group) / 2] for group in groups]
            pivot = pick(medians, len(medians) / 2 + 1)
            smaller = [x for x in a if x < pivot]
            if k <= len(smaller):
                return pick(smaller, k)
            k -= len(smaller) + a.count(pivot)
            return pivot if k < 1 else pick([x for x in a if x > pivot], k)

        # Find the k1-th and k2th smallest entries in the submatrix.
        def biselect(index, k1, k2):

            # Provide the submatrix.
            n = len(index)
            def A(i, j):
                return matrix[index[i]][index[j]]
            
            # Base case.
            if n <= 2:
                nums = sorted(A(i, j) for i in range(n) for j in range(n))
                return nums[k1-1], nums[k2-1]

            # Solve the subproblem.
            index_ = index[::2] + index[n-1+n%2:] # easton: select the intersection each other rows and columns
            # easton: I still don't fully understand
            k1_ = (k1 + 2*n) / 4 + 1 if n % 2 else n + 1 + (k1 + 3) / 4 # this smallest index that is bigger than k1
            k2_ = (k2 + 3) / 4 # the biggest index that is smaller than k2
            a, b = biselect(index_, k1_, k2_) # the corresponding value of k1_th and k2_th smallest in submatrix

            # Prepare ra_less, rb_more and L with saddleback search variants.
            ra_less = rb_more = 0 # numbers of those less than a and greater than b
            L = []
            jb = n   # jb is the first where A(i, jb) is larger than b.
            ja = n   # ja is the first where A(i, ja) is larger than or equal to a.
            for i in range(n):
                while jb and A(i, jb - 1) > b:
                    jb -= 1
                while ja and A(i, ja - 1) >= a:
                    ja -= 1
                ra_less += ja
                rb_more += n - jb
                L.extend(A(i, j) for j in range(jb, ja))
                
            # Compute and return x and y.
            x = a if ra_less <= k1 - 1 else \
                b if k1 + rb_more - n*n <= 0 else \
                pick(L, k1 + rb_more - n*n)
            y = a if ra_less <= k2 - 1 else \
                b if k2 + rb_more - n*n <= 0 else \
                pick(L, k2 + rb_more - n*n)
            return x, y

        # Set up and run the search.
        n = len(matrix)
        start = max(k - n*n + n-1, 0) # easton: shrink the possible start range
        k -= n*n - (n - start)**2
        return biselect(range(start, min(n, start+k)), k, k)[0]

    # https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85193/Binary-Search-Heap-and-Sorting-comparison-with-concise-code-and-1-liners-Python-72-ms
    # these methods are easier to understand and remember
    # binary search
    def kthSmallest(self, matrix, k):
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo<hi:
            mid = (lo+hi)//2
            if sum(bisect.bisect_right(row, mid) for row in matrix) < k:
                lo = mid+1
            else:
                hi = mid
        return lo

class Test(unittest.TestCase):

    def test(self):
        matrix = [
   [ 1,  5,  9, 10],
   [10, 11, 13, 13],
   [12, 13, 15, 15],
   [12, 13, 15, 15]
]
        k = 8   
        assert Solution().kthSmallest(matrix,k) 
        matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
        k = 8   
        assert Solution().kthSmallest(matrix,k) == 13
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

    def est_tree_draw(self):
        tree_draw(tree_deserialize('[1,2,3,4,5,6,7]'))

if __name__ == '__main__':
    unittest.main(exit=False)
