import unittest

from typing import List


# proved in mind
class Solution:
	def twoSum(self, numbers: List[int], target: int) -> List[int]:
		s, e = 0, len(numbers) - 1
		while s != e:
			if numbers[s] + numbers[e] == target:
				return [s + 1, e + 1]
			if numbers[s] + numbers[e] < target:
				s += 1
			if numbers[s] + numbers[e] > target:
				e -= 1


class Test(unittest.TestCase):
	def test(self):
		cases = [
			[dict(numbers=[2, 7, 11, 15], target=9), [1, 2]],
			[dict(numbers=[2, 3, 4], target=6), [1, 3]],
			[dict(numbers=[-1, 0], target=-1), [1, 2]]
		]
		for ci, co in cases:
			result = Solution().twoSum(ci["numbers"], ci["target"])
			assert result == co, (ci, co, result)


if __name__ == '__main__':
	unittest.main(exit=False)
