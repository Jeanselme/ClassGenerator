"""
	Class Generator
	by Vincent Jeanselme
	vincent.jeanselme@gmail.com
"""

from Shape.Circle import Circle
from Shape.Rectangle import Rectangle
from Generator import *

import json

if __name__ == '__main__':
	c1 = Circle(0.25,0.25,0.125,0.125)
	c2 = Circle(0.75,0.75,0.125,0.125)
	c3 = Circle(0.75,0.75,0.125)

	r1 = Rectangle(0.5,0.5,0.5,0.25)
	r2 = Rectangle(0,0,0.25,0.5)

	data = generateClass([c1,c2,c3], 10000)
	draw(200, 200, data, "Images/circles.jpg")

	data = generateClass([r1,r2], 10000)
	draw(200, 200, data, "Images/rectangles.jpg")

	data = generateClass([r1,r2,c1,c2,c3], 10000)
	draw(200, 200, data, "Images/both.jpg")

	with open("res.data", 'w') as outPut:
		json.dump(data, outPut)
