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


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dis(a,b):
            l1, l2 = len(a), len(b)
            count = 0
            for i in range(min(l1, l2)):
                if a[i]!=b[i]:
                    count = i
                    break
            count = count or min(l1, l2)
            # print 'a,b,dis,count', a,b,l1-count + l2 - count, count
            return l1-count + l2 - count
        if not root:
            return 0
        paths = []
        st = collections.deque([[root, []]])
        while st:
            # print st[0]
            cur, p = st.popleft()
            # left, right = cur.left, cur.right
            # for i in [left, right]:
            #     if i: 
            #         st.append([i, p + [cur.val]])
            if cur.left:
                st.append([cur.left, p+[cur.val]])
            if cur.right:
                st.append([cur.right, p+[cur.val]])
            paths.append(p+[cur.val])
        # print 'paths', paths
        max_dis = 0
        for idx, p in enumerate(paths):
            for p2 in paths[idx+1:]:
                max_dis = max(dis(p, p2), max_dis)
        return max_dis





class Test(unittest.TestCase):

    def test(self):
        Node1 = TreeNode(1)
        Node2 = TreeNode(2)
        Node3 = TreeNode(3)
        Node4 = TreeNode(4)
        Node5 = TreeNode(5)
        Node1.left = Node2
        Node1.right = Node3
        Node2.left = Node4
        Node2.right = Node5

        # print Solution().diameterOfBinaryTree(Node1)
        # assert Solution().diameterOfBinaryTree(Node1) == 3
        assert Solution().diameterOfBinaryTree(None) == 0

        # [2,1,4,3,null,5]
        Node1 = TreeNode(1)
        Node2 = TreeNode(2)
        Node3 = TreeNode(3)
        Node4 = TreeNode(4)
        Node5 = TreeNode(5)
        Node1.left = Node2
        Node1.right = Node3
        Node2.left = Node4
        Node3.right = Node5
        assert Solution().diameterOfBinaryTree(Node1) == 4

        Node1 = TreeNode(1)
        Node2 = TreeNode(2)
        Node3 = TreeNode(3)
        Node4 = TreeNode(4)
        Node5 = TreeNode(5)
        Node6 = TreeNode(6)
        Node1.left = Node2
        Node1.right = Node3
        Node2.left = Node4
        Node4.right = Node5
        Node3.left = Node6
        assert Solution().diameterOfBinaryTree(Node1) == 5

        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

if __name__ == '__main__':
    unittest.main()
