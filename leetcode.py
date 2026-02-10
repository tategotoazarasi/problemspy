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


class Solution3640:
	def maxSumTrionic(self, nums: List[int]) -> int:
		down = {}
		up = {}
		isup = False
		isdown = False
		start = 0
		for i in range(len(nums) - 1):
			if nums[i + 1] > nums[i]:
				if isdown:
					down[start] = i
					start = i
				isdown = False
				isup = True
			if nums[i + 1] < nums[i]:
				if isup:
					up[start] = i
					start = i
				isup = False
				isdown = True
			if nums[i + 1] == nums[i]:
				if isup:
					up[start] = i
				if isdown:
					down[start] = i
				isup = False
				isdown = False
				start = i + 1
		if isup:
			up[start] = len(nums) - 1
		if isdown:
			down[start] = len(nums) - 1

		updown = {}
		for k, v in up.items():
			if v in down.keys():
				updown[k] = (v, down[v])
		updownup = {}
		for k, v in updown.items():
			if v[1] in up.keys():
				updownup[k] = (k, v[0], v[1], up[v[1]])
		ans = -10 ** 1000
		for k, v in updownup.items():
			s = 0
			for i in range(v[1], v[2] + 1):
				s += nums[i]
			sleft = 0
			smax = -10 ** 1000
			for i in range(v[1] - 1, v[0] - 1, -1):
				sleft += nums[i]
				smax = max(smax, sleft)
			s += smax
			sright = 0
			smax = -10 ** 1000
			for i in range(v[2] + 1, v[3] + 1):
				sright += nums[i]
				smax = max(smax, sright)
			s += smax
			ans = max(ans, s)

		return ans


class Solution1935:
	def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
		broken_set = set(brokenLetters)
		words = text.split(' ')
		count = 0
		for word in words:
			if all(letter not in broken_set for letter in word):
				count += 1
		return count
