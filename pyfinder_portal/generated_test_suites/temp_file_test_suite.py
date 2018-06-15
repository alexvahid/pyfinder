import unittest
import sys
sys.path.append("/Users/alex/Drive/230/pyfinder")
sys.path.append("/Users/alex/Drive/230/pyfinder/pyfinder_portal")
from temp_file import elseif

class Test_temp_file(unittest.TestCase):

	def test0(self):
		self.assertEqual(elseif(0), 0)

	def test1(self):
		self.assertEqual(elseif(-1), 9)

	def test2(self):
		self.assertEqual(elseif(1), 1)

	def test3(self):
		self.assertEqual(elseif(2), 2)

	def test4(self):
		self.assertEqual(elseif(3), 3)

	def test5(self):
		self.assertEqual(elseif(4), 4)

	def test6(self):
		self.assertEqual(elseif(5), 5)

	def test7(self):
		self.assertEqual(elseif(6), 6)

	def test8(self):
		self.assertEqual(elseif(7), 7)

	def test9(self):
		self.assertEqual(elseif(8), 8)

if __name__ == '__main__':
	unittest.main()
