import unittest
from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        old_head = head
        tails = [None] * (n + 1)
        while head:
            tails = tails[1:] + [head]
            head = head.next
        print(tails)
        if tails[0] is None:
            if n == 1:
                return None
            return tails[2]
        tails[0].next = tails[1].next
        return old_head


class Test(unittest.TestCase):
    def test(self):
        cases = [
            ["1+7-(7+3+3)+6-3+1", -1]
        ]
        for ci, co in cases:
            result = Solution().calculate(ci)
            assert result == co, (ci, co, result)


if __name__ == '__main__':
    unittest.main(exit=False)
