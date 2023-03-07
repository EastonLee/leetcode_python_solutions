import unittest
from typing import List


class Solution:
    def trips_in_time(self, times: List[int], time: int):
        return sum([time // t for t in times])

    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        # binary search
        time.sort()
        maxt = totalTrips * time[-1]

        l, r = 1, maxt + 1
        while l < r:
            mid = (l + r) // 2
            trips = self.trips_in_time(time, mid)
            if trips >= totalTrips:
                r = mid
            else:
                l = mid + 1

        return l


class Test(unittest.TestCase):

    def test(self):
        cases = [
            [([1, 2, 3], 5), 3],
            [([2], 1), 2],
        ]
        for ci, co in cases:
            result = Solution().minimumTime(*ci)
            assert result == co, (ci, co, result)
        # cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')


if __name__ == '__main__':
    unittest.main(exit=False)
