import unittest
from typing import *


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        if event1[0] == event2[0]:
            return True
        if event1[0] <= event2[0]:
            if event1[1] >= event2[0]:
                return True
        else:
            if event2[1] >= event1[0]:
                return True
        return False


class Test(unittest.TestCase):
    def test(self):
        cases = [
            [["01:15", "02:00"],
             ["02:00", "03:00"], True]
        ]
        for ci0, ci1, co in cases:
            result = Solution().haveConflict(ci0, ci1)
            assert result == co, (ci0, ci1, co, result)


if __name__ == '__main__':
    unittest.main(exit=False)
