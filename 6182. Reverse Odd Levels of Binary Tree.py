import unittest
from typing import Optional


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


# tree by level
def tree_serialize(root):
    ans = []
    level = [root]
    while any(level):
        ans.extend(node.val if node else None for node in level)
        level = [kid for node in level for kid in (node.left, node.right) if node]
    return ans


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


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        s = tree_serialize(root)
        length = len(s)
        height = tree_height(root)
        for i in range(1, height + 1, 2):
            start = 2 ** i - 1
            end = 2 ** (i + 1) - 2
            if end >= length:
                end = length - 1
            s[start:end + 1] = s[start:end + 1][::-1]

        return tree_deserialize(str(s))


class Test(unittest.TestCase):
    def test(self):
        cases = [
            [[2, 3, 5, 8, 13, 21, 34], [2, 5, 3, 8, 13, 21, 34]],
            [[7, 13, 11], [7, 11, 13]],
            [[0, 1, 2, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2], [0, 2, 1, 0, 0, 0, 0, 2, 2, 2, 2, 1, 1, 1, 1]],
        ]
        for ci, co in cases:
            result = Solution().reverseOddLevels(tree_deserialize(str(ci)))
            result = tree_serialize(result)
            assert result == co, (ci, co, result)
        # cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

    def test_tree_draw(self):
        tree = tree_deserialize('[1,2,3,4,5,6,7]')
        tree_draw(tree)
        print(tree_serialize(tree))


if __name__ == '__main__':
    unittest.main(exit=False)
