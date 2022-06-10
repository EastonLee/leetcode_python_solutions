# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rst, tmp = [], 0
        i, j = l1, l2
        while i or j:
            s = (i and i.val or 0) + (j and j.val or 0) + tmp
            rst.append(s % 10)
            tmp = s // 10
            if i: i = i.next
            if j: j = j.next
        if tmp:
            rst.append(tmp)
        return make_link(rst)


def make_link(l: List[int]):
    link, last = None, None
    for i in l:
        new = ListNode(i, None)
        if last:
            last.next = new
            last = new
        else:
            link = last = new
    return link


def print_link(l: Optional[ListNode]):
    while l:
        print(l.val)
        l = l.next


# class Test(unittest.TestCase):
#     def test(self):
#         cases = [
#             [dict(l1=[2, 4, 3], l2=[5, 6, 4]), [7, 0, 8]],
#             [dict(l1=[0], l2=[0]), [0]],
#             [dict(l1=[9, 9, 9, 9, 9, 9, 9], l2=[9, 9, 9, 9]), [8, 9, 9, 9, 0, 0, 0, 1]]
#         ]
#         for ci, co in cases:
#             result = Solution().addTwoNumbers(ci["l1"], ci["l2"])
#             assert result == co, (ci, co, result)


if __name__ == '__main__':
    # unittest.main(exit=False)
    print_link(make_link([7, 0, 8]))
