from typing import List


class Solution:
	def runningSum(self, nums: List[int]) -> List[int]:
		rst = []
		for i in nums:
			rst.append(i + (rst[-1] if rst else 0))
		return rst
