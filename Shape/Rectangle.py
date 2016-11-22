"""
	Class Generator
	by Vincent Jeanselme
	vincent.jeanselme@gmail.com
"""

from Shape.ShapeClass import ShapeClass

class Rectangle(ShapeClass):
	"""
		Represents a rectangle
	"""

	def __init__(self, ulx, uly, width, height):
		"""
		Increments the number of class
		And init the circle attribute
		"""
		self.ulx = ulx
		self.uly = uly
		self.width = width
		self.height = height
		ShapeClass.__init__(self)

	def inClass(self, x, y):
		"""
		Returns a boolean if the point (x,y) is in the rectangle of dimension
		width * height with upper left angle ulx, uly
		x,y in [0,1]^2
		"""
		return x > self.ulx and x < self.ulx + self.width and y > self.uly and y < self.uly + self.height
