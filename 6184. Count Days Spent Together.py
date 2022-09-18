import unittest

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def month_and_day(day):
    month, day = day.split('-')
    return int(month), int(day)


def nth_day(date):
    return sum(days[:date[0] - 1]) + date[1]


class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        arriveAlice, leaveAlice, arriveBob, leaveBob = map(nth_day, map(month_and_day,
                                                                        [arriveAlice, leaveAlice, arriveBob, leaveBob]))
        return max(0, min(leaveAlice, leaveBob) - max(arriveAlice, arriveBob) + 1)


class Test(unittest.TestCase):
    def test(self):
        cases = [
            [dict(arriveAlice="08-15", leaveAlice="08-18", arriveBob="08-16", leaveBob="08-19"), 3]
        ]
        for ci, co in cases:
            result = Solution().countDaysTogether(ci['arriveAlice'], ci['leaveAlice'], ci['arriveBob'], ci['leaveBob'])
            assert result == co, (ci, co, result)


if __name__ == '__main__':
    unittest.main(exit=False)
