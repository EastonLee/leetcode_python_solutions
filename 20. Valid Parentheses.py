import unittest


class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        m = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        l = '([{'
        stack = []
        for c in s:
            if c in l:
                stack.append(c)
            if c in m:
                if not stack:
                    return False
                if stack[-1] != m[c]:
                    return False
                stack.pop()

        return not stack


class Test(unittest.TestCase):
    def test(self):
        cases = [
            ["()", True],
            ["()[]{}", True],
            ["(]", False],
        ]
        for ci, co in cases:
            result = Solution().isValid(ci)
            assert result == co, (ci, co, result)


if __name__ == '__main__':
    unittest.main(exit=False)
