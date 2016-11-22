"""
	Class Generator
	by Vincent Jeanselme
	vincent.jeanselme@gmail.com
"""

import random, scipy.misc, json
import numpy as np
from Shape.ShapeClass import ShapeClass

def generatePoint():
	"""
		Generates a point
	"""
	return random.random(), random.random()

def generateClass(classesList, n):
	"""
		For a list of classes generates a list of n random points
		-1 if there is no corresponding class
	"""
	data = []
	for i in range(n):
		x, y = generatePoint()
		added = False
		for shape in classesList:
			if (shape.inClass(x,y)) :
				data.append([shape.getClass(), x, y])
				added = True
		if not(added):
			data.append([-1, x, y])
	return data

def color(k, kmax):
	"""
		Return a color for a given class
	"""
	c = (k+1) * 255/(min(int((kmax+1)/3),1))
	res = [0,0,0]
	res[k%3] = c
	return res

def draw(height, width, pointsList, output=""):
	"""
		Draws the different point on the map with a color for each class
		PointsList = [[k,x,y]*]
	"""
	kmax = len(set([p[0] for p in pointsList]))
	res = np.zeros((height, width, 3))

	for point in pointsList:
		k, x, y = point
		x = int(x*width)
		y = min(height-1, int(y*height))
		if (k != -1):
			# MultiClass case
			if np.count_nonzero(res[y][x]) == 0:
				res[y][x] = color(k, kmax)
			else:
				res[y][x] = [(color(k, kmax)[i] + res[y][x][i])/2 for i in range(3)]
		else:
			res[y][x] = [125,125,125]

	scipy.misc.imshow(res)
	if output != "":
		scipy.misc.imsave(output, res)
