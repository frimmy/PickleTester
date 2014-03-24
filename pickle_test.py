import unittest
from pickler import list_pickler

class TestsForPickler(unittest.TestCase):
	"""docstring for TestsForPickler"""
	def assign_list_to_variable_test(self, arg):
		super(TestsForPickler, self).__init__()
		self.arg = arg
