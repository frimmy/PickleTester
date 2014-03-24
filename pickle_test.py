import unittest

from pickler import ListPickler, UnPickler

class TestsForPickler(unittest.TestCase):
	"""docstring for TestsForPickler"""
	def setUp(self):
		self.file = "sample_pickle.p"
		self.pickler = ListPickler()
		self.unpickler = UnPickler()
		# self.sample_pickle = [1,2,3]

	def tearDown(self):
		self.pickler = None
		self.unpickler = None
		self.file = None

	def assign_list_to_variable_test(self):
		my_list = [1,2,3]
		self.pickler.pickle_list(my_list, self.file)
		another_list = self.unpickler.unpickle_list(self.file)
		self.assertEqual(my_list, another_list)
		

