import heapq
from collections import defaultdict
from dataclasses import dataclass, field
from typing import List


class Solutions:
	"""
	Collection of solutions for LeetCode problems.
	"""

	def minOperations(self, nums: List[int], k: int) -> int:
		"""
		Calculates the minimum operations required based on sum modulo k.

		(Note: Based on the provided code logic, this calculates sum(nums) % k.
		Update the docstring if the problem logic implies specific operations).

		Args:
			nums (List[int]): A list of integers.
			k (int): The divisor.

		Returns:
			int: The remainder of the sum of the array divided by k.

		Example:
			>>> sol = Solutions()
			>>> sol.minOperations([3, 9, 7], 5)
			4
		"""
		sum_ = 0
		for num in nums:
			sum_ += num
		return sum_ % k


class Solution3651:
	@dataclass(order=False)
	class Status:
		weight: int
		x: int = field(compare=False)  # name 不参与比较
		y: int = field(compare=False)
		k: int

		def __lt__(self, other):
			if self.weight != other.weight:
				return self.weight < other.weight
			return self.k > other.k

	def minCost(self, grid: List[List[int]], k: int) -> int:
		pq = []
		group = defaultdict(list)
		keys = set()
		vis = {}
		m = len(grid)
		n = len(grid[0])

		for i in range(m):
			for j in range(n):
				group[grid[i][j]].append((i, j))
				keys.add(grid[i][j])

		sorted_keys = sorted(keys)
		key_i = {key: i for i, key in enumerate(sorted_keys)}

		processed_idx = [-1] * k

		heapq.heappush(pq, self.Status(0, 0, 0, k))

		while pq:
			current = pq[0]
			heapq.heappop(pq)

			if (current.x, current.y) in vis and vis[(current.x, current.y)] >= current.k:
				continue
			vis[(current.x, current.y)] = current.k

			if current.x == m - 1 and current.y == n - 1:
				return current.weight

			if current.x < m - 1:
				weight_down = current.weight + grid[current.x + 1][current.y]
				if vis.get((current.x + 1, current.y), -1) < current.k:
					heapq.heappush(pq, self.Status(weight_down, current.x + 1, current.y, current.k))

			if current.y < n - 1:
				weight_right = current.weight + grid[current.x][current.y + 1]
				if vis.get((current.x, current.y + 1), -1) < current.k:
					heapq.heappush(pq, self.Status(weight_right, current.x, current.y + 1, current.k))

			if current.k > 0:
				current_key = grid[current.x][current.y]
				idx = key_i[current_key]
				target_k = current.k - 1

				if idx > processed_idx[target_k]:
					start_idx = processed_idx[target_k] + 1
					for i in range(start_idx, idx + 1):
						val = sorted_keys[i]
						for r, c in group[val]:
							if r == current.x and c == current.y:
								continue
							if vis.get((r, c), -1) < target_k:
								heapq.heappush(pq, self.Status(current.weight, r, c, target_k))

					processed_idx[target_k] = idx

		return 0
