import maya.cmds as cmds
import math

def makeFace():

	newFace = cmds.polyCreateFacet(p=[(-1,-1,0),(1,- 1,0),(1,1,0),(-1,1,0)])


makeFace()
