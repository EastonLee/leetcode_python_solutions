import unittest


# https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1729/11-line-simple-Java-solution-O(n)-with-explanation
# this solution uses looking backward longest window
# anther method is looking forward longest window, but it's more complicated
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right_index_map = {}
        slow_head = fast_tail = rst = 0
        for fast_tail, tail in enumerate(s):
            if tail in right_index_map:
                slow_head = max(right_index_map[tail] + 1, slow_head)
            right_index_map[tail] = fast_tail
            rst = max(rst, fast_tail - slow_head + 1)
        return rst


class Test(unittest.TestCase):
    def test(self):
        cases = [
            ["abcabcbb", 3],
            ["bbbb", 1],
            ["pwwkew", 3]
        ]
        for ci, co in cases:
            result = Solution().lengthOfLongestSubstring(ci)
            assert result == co, (ci, co, result)


if __name__ == '__main__':
    unittest.main(exit=False)
