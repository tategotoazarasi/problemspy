import io
import unittest

import kattis


def run_io_test(solver_main, input_str):
	# Mock Standard Input
	mock_stdin = io.StringIO(input_str)
	# Mock Standard Output
	mock_stdout = io.StringIO()

	# Execute
	solver_main(mock_stdin, mock_stdout)

	# Get result
	return mock_stdout.getvalue()


class Test_addtwonumbers(unittest.TestCase):
	def test_case1(self):
		input_str = "3 4"
		expected = "7"
		result = run_io_test(kattis.addtwonumbers.main, input_str)
		self.assertEqual(result, expected)

	def test_case2(self):
		input_str = "987 23"
		expected = "1010"
		result = run_io_test(kattis.addtwonumbers.main, input_str)
		self.assertEqual(result, expected)
