import unittest

from pickler import ListPickler,ListUnpickler

class TestsForPickler(unittest.TestCase):
	"""docstring for TestsForPickler"""
	def setUp(self):
		self.sample_pickle = [1,2,3]

	def tearDown(self):
		self.sample_pickle = None

	def assign_list_to_variable_test(self):
		my_list = [1,2,3]
		another_list = self.sample_pickle
		self.assertEqual(my_list, another_list)
		

