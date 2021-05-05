import maya.cmds as cmds

def selectVertex():
	# select object
	selectedObjects = cmds.ls(selection=True)    
	obj = selectedObjects[-1]  

	# select vertex
	#cmds.select(obj+'.vtx[0]', replace=True)

	# select edge
	#cmds.select(obj+'.e[0]', replace=True)

	# select face
	#cmds.select(obj+'.f[0]', replace=True)

	# select number of vertex's
	#cmds.select(obj+'.vtx[5:12]', replace=True)

	# select number of vertex's - clean setup
	objectName = "myObject"
	startIndex = 5
	endIndex = 12
	cmds.select("{0}.vtx[{1}:{2}]".format(objectName, startIndex, endIndex),replace=True)

selectVertex()