#!/usr/bin/python3

#Test case to add 2 numbers

import unittest
from Program1 import summation

class TestSum(unittest.TestCase):
	def test_list_int(self):
		data=[10,20]
		result=summation(data)
		self.assertEqual(result,30)

if __name__=='__main__':
	unittest.main()
		