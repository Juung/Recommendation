import numpy as np

class BatchGenerator:

	def __init__(self, X, Y, batch_size):
		if self.is_sparse(X):
			if X.shape[0] != Y.shape[0]:
				raise ValueError('Size of X and Y is not same')
			self.X = X
			self.Y = Y
			self.data_size = X.shape[0]
			self.batch_size = batch_size
			self.iter = self.make_random_iter()

		else:
			if len(X) != len(Y):
				raise ValueError('Size of X and Y is not same')
			self.X = np.array(X)
			self.Y = np.array(Y)
			self.data_size = len(self.X)
			self.batch_size = batch_size
			self.iter = self.make_random_iter()

	def make_random_iter(self):
		splits = np.arange(self.batch_size, self.data_size, self.batch_size)
		it = np.split(np.random.permutation(range(self.data_size)), splits)[:-1]
		return iter(it)

	def next_batch(self):
		try:
			idxs = next(self.iter)
		except StopIteration:
			self.iter = self.make_random_iter()
			idxs = next(self.iter)
		
		inputs = self.X[idxs]
		targets = self.Y[idxs]
		if self.is_sparse(self.X):
			inputs = inputs.todense()
			targets = targets.todense()

		return inputs, targets

	def is_sparse(self, X):
			if str(type(X)).startswith("<class 'scipy.sparse"):
				return True
			else:
				return False