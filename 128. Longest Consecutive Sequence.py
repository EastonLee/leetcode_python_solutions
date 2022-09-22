from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = list(set(nums))
        nums.sort()
        longest = 1
        current_len = 0
        last = -10 ** 9 - 2
        for i in nums:
            if i == last + 1:
                current_len += 1
                longest = max(current_len, longest)
            else:
                current_len = 1
            last = i
        return longest
