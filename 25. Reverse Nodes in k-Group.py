from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        stack = []
        while head is not None:
            stack.append(head)
            head = head.next
            if len(stack) == k:
                break

        if len(stack) < k:
            return stack[0]

        for i in range(len(stack) - 1, 0, -1):
            stack[i].next = stack[i - 1]

        stack[0].next = self.reverseKGroup(head, k)
        return stack[-1]
