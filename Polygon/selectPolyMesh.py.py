import maya.cmds as cmds

def currentSelectionPolygonal(obj):

	shapeNode = cmds.listRelatives(obj, shapes=True)
	nodeType = cmds.nodeType(shapeNode)

	if nodeType == "mesh":
		return True

	return False


def checkSelection():

	selectedObjs = cmds.ls(selection=True)    

	if (len(selectedObjs) < 1):        
		cmds.error('Please select an object')
		
	lastSelected = selectedObjs[-1]

	isPolygon = currentSelectionPolygonal(lastSelected)

	if (isPolygon):
		print('FOUND POLYGON')
	else:
		cmds.error('Please select a polygonal object')

checkSelection()