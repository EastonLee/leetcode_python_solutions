import unittest
'''

'''
# Definition for a binary tree node.


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return 'node value: {}'.format(self.val)


class Solution(object):

    # by Easton
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        l = [root]
        count = 0
        while l:
            c = l.pop()
            if isinstance(c, int):
                count += 1
                if count == k:
                    return c
                continue
            if c.right:
                l.append(c.right)
            l.append(c.val)
            if c.left:
                l.append(c.left)

    # https://discuss.leetcode.com/topic/18279/pythonic-approach-with-generator/2
    # by StefanPochmann
    def kthSmallest(self, root, k):
        import itertools

        def inorder(node):
            if node:
                for val in inorder(node.left):
                    yield val
                yield node.val
                for val in inorder(node.right):
                    yield val
        return next(itertools.islice(inorder(root), k - 1, k))


class Test(unittest.TestCase):

    def test(self):
        root = TreeNode(5)
        node1 = TreeNode(3)
        node2 = TreeNode(7)
        root.left = node1
        root.right = node2
        assert Solution().kthSmallest(root, 1) == 3
        assert Solution().kthSmallest(root, 2) == 5
        assert Solution().kthSmallest(root, 3) == 7


if __name__ == '__main__':
    unittest.main()
