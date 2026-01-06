import unittest

import test_kattis
import test_leetcode

if __name__ == '__main__':
	loader = unittest.TestLoader()
	suite = unittest.TestSuite()
	suite.addTests(loader.loadTestsFromModule(test_kattis))
	suite.addTests(loader.loadTestsFromModule(test_leetcode))
	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(suite)
