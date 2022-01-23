import unittest
from pprint import pprint
import re
import cProfile
import heapq
import collections
import itertools

'''

'''
# Definition for a binary tree node.


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return 'value: {}'.format(self.val)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None: return []
        left = []
        right = []
        leaves = []
        def left_most(r):
            if r is None or r.left is None and r.right is None:
                return
            if not r.left and r.right:
                left.append(r.val)
                left_most(r.right)
            if r.left:
                left.append(r.val)
                left_most(r.left)        
        def right_most(r):
            if r is None or r.left is None and r.right is None:
                return
            if not r.right and r.left:
                right.append(r.val)
                right_most(r.left)
            if r.right:
                right.append(r.val)
                right_most(r.right)
        def find_leavse(r):
            if r is None:
                return
            if r.left is None and r.right is None:
                leaves.append(r.val)
            if r.left:
                find_leavse(r.left)
            if r.right:
                find_leavse(r.right)
        left_most(root)
        right_most(root)
        find_leavse(root)
        if len(left)>1:
            left = left[1:]
        if len(right)>1:
            right = right[1:]
        return [root.val] + (left if root.left else []) + leaves + (right[::-1] if root.right else [])
        





class Test(unittest.TestCase):

    def test(self):
        case = '[1,null,2,3,4]'
        assert Solution().calculate(case) == -1
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

if __name__ == '__main__':
    unittest.main()
