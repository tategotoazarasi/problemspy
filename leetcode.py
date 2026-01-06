from typing import List


class Solutions:
	def minOperations(self, nums: List[int], k: int) -> int:
		sum_ = 0
		for num in nums:
			sum_ += num
		return sum_ % k
