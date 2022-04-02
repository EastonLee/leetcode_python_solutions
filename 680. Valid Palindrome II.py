import unittest


class Solution:
    def validPalindrome(self, s: str) -> bool:
        length = len(s)
        for i, c in enumerate(s):
            if i == length // 2:
                return True
            if c == s[length - 1 - i]:
                continue
            optionA = s[i + 1:length - i]
            optionB = s[i:length - 1 - i]
            for option in [optionA, optionB]:
                if option == option[::-1]:
                    return True
            return False


class Test(unittest.TestCase):

    def test(self):
        assert Solution().validPalindrome("deeee")
        assert Solution().validPalindrome("abca")
        assert not Solution().validPalindrome("abc")
        assert not Solution().validPalindrome("abc")


if __name__ == '__main__':
    unittest.main(exit=False)
