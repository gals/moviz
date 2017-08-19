"""
"""

class Operator(object):
	"""
	"""

	def __init__(self, name):
		"""
		"""
		self.name = name

	def __repr__(self):
		return "<%s(%s)>" % (self.__class__.__name__, self.name)

	def theaters(self):
		"""
		"""
		raise NotImplementedError()

class Theater(object):
	"""
	"""

	def __init__(self, name):
		"""
		"""
		self.name = name

	def __repr__(self):
		return "<%s(%s)>" % (self.__class__.__name__, self.name)

	def showtimes(self, date=None):
		"""
		"""
		raise NotImplementedError()