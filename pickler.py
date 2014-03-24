import cPickle as pickle
import os

class ListPickler(object):
	"""ListPickler that converts lists into pickled objects"""
	def pickle_list(self, list_to_pickle, filename):
		output = open(filename, "wb")
		pickle.dump(list_to_pickle, output)
		output.close()

class UnPickler(object):
	"""ListPickler that converts lists into pickled objects"""
	def unpickle_list(self, filename):
		output = open(filename, "rb")
		new_list = pickle.load(output)
		output.close()
		os.remove(filename)
		return new_list

