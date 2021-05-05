import maya.cmds as cmds

# examine data for a currently-selected polygonal object
def getPolyData():
	# select object
	selectedObjects = cmds.ls(selection=True)    
	obj = selectedObjects[-1]    
	
	# get number of vertexes
	vertNum = cmds.polyEvaluate(obj, vertex=True)    
	print('Vertex Number: ',vertNum)    
	
	# get number of edges
	edgeNum = cmds.polyEvaluate(obj, edge=True)    
	print('Edge Number: ', edgeNum)    
	
	# get number of faces
	faceNum = cmds.polyEvaluate(obj, face=True)    
	print('Face Number: ',faceNum)

getPolyData()