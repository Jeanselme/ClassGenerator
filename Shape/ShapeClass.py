"""
	Class Generator
	by Vincent Jeanselme
	vincent.jeanselme@gmail.com
"""

class ShapeClass():
	"""
		Represents a class
		All the class have to have points in [0;1]^2
		Abstract
	"""

	k = 0

	def __init__(self):
		"""
		Increments the number of class
		"""
		self.num = ShapeClass.k
		ShapeClass.k += 1

	def inClass(self, x, y):
		"""
		Returns a boolean if the point (x,y) is in the class
		x,y in [0,1]^2
		Abstract
		"""
		return False

	def getClass(self):
		"""
		Returns the number of the class
		"""
		return self.num
