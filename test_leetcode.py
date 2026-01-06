import unittest

import leetcode


class Test3512(unittest.TestCase):
	solver = leetcode.Solutions()

	def test_case1(self):
		nums = [3, 9, 7]
		k = 5
		answer = 4

		result = self.solver.minOperations(nums, k)

		self.assertEqual(result, answer)
