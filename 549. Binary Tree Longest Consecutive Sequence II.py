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
        return 'value: {}'.format(self.val)


# https://discuss.leetcode.com/topic/85778/dfs-c-python-solutions
# by @zqfan
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, parent):
            if not node:
                return 0, 0
            li, ld = dfs(node.left, node)
            ri, rd = dfs(node.right, node)
            l[0] = max(l[0], li + rd + 1, ld + ri + 1)
            if node.val == parent.val + 1:
                return max(li, ri) + 1, 0
            if node.val == parent.val - 1:
                return 0, max(ld, rd) + 1
            return 0, 0
        l = [0]
        dfs(root, root)
        return l[0]


class Test(unittest.TestCase):

    def test(self):
        case = [1, 2, 3]
        node1, node2, node3 = map(TreeNode, case)
        node1.left = node2
        node1.right = node3
        assert Solution().longestConsecutive(node1) == 2
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

if __name__ == '__main__':
    unittest.main()
