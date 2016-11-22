"""
	Class Generator
	by Vincent Jeanselme
	vincent.jeanselme@gmail.com
"""

from Shape.ShapeClass import ShapeClass

class Circle(ShapeClass):
	"""
		Represents a circle
	"""

	def __init__(self, cx, cy, deltaR, r=0):
		"""
		Increments the number of class
		And init the circle attributes
		"""
		self.cx = cx
		self.cy = cy
		self.r = r
		self.deltaR = deltaR
		ShapeClass.__init__(self)

	def inClass(self, x, y):
		"""
		Returns a boolean if the point (x,y) is in the circle between r and deltaR + r
		x,y in [0,1]^2
		"""
		position = (x-self.cx)**2 + (y-self.cy)**2
		return (position > self.r**2) and (position < (self.r+self.deltaR)**2)
