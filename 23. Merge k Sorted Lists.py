import heapq
from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    heap = None

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if self.heap is None:
            self.heap = [(l.val, i) for i, l in enumerate(lists) if l is not None]
            heapq.heapify(self.heap)

        if len(self.heap) == 0:
            return None
        minHeadIndex = heapq.heappop(self.heap)[1]
        head = lists[minHeadIndex]
        if head.next:
            heapq.heappush(self.heap, (head.next.val, minHeadIndex))

        lists[minHeadIndex] = head.next
        head.next = self.mergeKLists(lists)
        return head
