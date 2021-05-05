import maya.cmds as cmds
import math

def makeFace():

	newFace = cmds.polyCreateFacet(p=[(-1,-1,0),(1,- 1,0),(1,1,0),(-1,1,0)])

def makeFaceWithHole():

	points = []

	# create the inital square
	points.append((-5, -5, 0))
	points.append(( 5, -5, 0))
	points.append(( 5, 5, 0))
	points.append((-5, 5, 0))    

	# add empty point to start a hole
	points.append(())

	for i in range(32):
		theta = (math.pi * 2) / 32 * i
		x = math.cos(theta) * 2
		y = math.sin(theta) * 2
		points.append((x, y, 0))
		
	newFace = cmds.polyCreateFacet(p=points)

makeFace()
makeFaceWithHole()