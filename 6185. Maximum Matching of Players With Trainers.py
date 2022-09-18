import unittest
from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        ans = 0
        player_index = 0
        for i in range(len(trainers)):
            if player_index < len(players) and players[player_index] <= trainers[i]:
                ans += 1
                player_index += 1

        return ans


class Test(unittest.TestCase):
    def test(self):
        cases = [
            [([4, 7, 9], [8, 2, 5, 8]), 2],
            [([1, 1, 1], [10]), 1],
            [([4, 2], [4, 4, 3]), 2]
        ]
        for ci, co in cases:
            result = Solution().calculate(ci)
            assert result == co, (ci, co, result)


if __name__ == '__main__':
    unittest.main(exit=False)
