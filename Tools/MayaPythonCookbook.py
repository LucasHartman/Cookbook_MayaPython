import sys
import maya.cmds as cmds
import math
import random
#import os from PIL 
#import Image
import struct
from functools import partial
import os
import operator

"""
------------------------------------------------------------------------
Load external Python-file
------------------------------------------------------------------------

	#add folder to PythonPath
	sys.path.append('c:/Users/12213119/Documents/maya/2020/scripts/Lab/')

	# print PythonPaths
	from pprint import pprint
	sys.path
	pprint(sys.path)

	# import file
	import ModuleName
	
	# refresh file
	reload(ModuleName)
	
	# call script
	ModuleName.Function()

------------------------------------------------------------------------
							Table Contents	
------------------------------------------------------------------------

	My Functions

		def sortDictionary(dictonary)	sort a dictionary
		def importObj(myFolder)			import a external obj file from root import
		def listAllObjs()				list all in the scene objectst
		def listSelected()				list al selected objects
	
	Python UI

		def showUI()					simple UI window
		def inputUI()					input value, and generate array of spheres
		def nestedLayout()				UI elemets places next to each other
		def tabUI()						simple UI window with Tabs
		def BarMenuUI()					simple UI window with top menu bar
		def addNoise(float)				add Noise to selected poly object

	Working with Geometry

		def checkSelection()			Notify use if a poly object is selected or not
		def getPolyData()				Examine data for a currently-selected polygonal object
		def getNURBSInfo()				Examine data for a currently-selected NURBS object
		def makeCurve()					Create Curve Square
		def complexCurve()				Create Curve with math module
		def makeFace()					Make a poly Face
		def makeFaceWithHole()			Create a poly Face, with a bit hole inside

	UVs and Materials

		def uvInfo()					selected object, UV info: number of UVs, position first UV, if first Edge is border
		def layoutUVs()					select object & create UVs (Windows/Modeling Editor/UV Editor)
		def createNodes()				create a new shader (Windows/Rendering Editors/Hypershade)
		def findUnattachedObjects()		select object - create shader & add to selected object (ERROR for now)
		def objectsFromShader()			input 'shaderName', get list of objects using this shader'''
		def keepCentered():				select 3 object. second object positon will be average of the other 2

	Rigging

		def createSimpleSkeleton(int)	creates a simple skeleton as a single chain of bones
		def createHand(int, int)		create hand joints arg: num of finger and joints
		def setDrivenKeys()				select joint and runscript, all bones downstream rotate when rotate Z
		def addCustomAttributes()	  	add cutum attrbiute
		def lockAndHide(obj, att)		remove selected attribute. argruemtns: 'objectName', 'attributeName'''   (ERROR for now)
		def rigUI(): 					setup IK Leg

	Animation

		def getAnimationData()			select Object, runscirpt, check animation info (Windows/Animation Editors/Graph Editor)
		def makeAnimLayer('Name')		make animation layer (ChannelBox/Anim)
		def copyKeyframes()				Select the animated object, shift-select at least one other object, and run the script
		def setKeyframes()				Run the preceding script with an object selected and trigger playback. You should see the objectmove up and down
		def createExpression()			add speed attribute to selected object and tie the attribute to a sine wave based on the current time'''  

	Rendering

		def createLightRig()		three lights created-two spotlight and one directionla light
		def ThreeLightUI()			new window with a control for each light in the scene (ERROR)
		def makeCameraRig()			Run the script, and you should have four isometric cameras, all looking at the origin
		def renderSpriteSheet()		render out multiple views. NOTE: PIL installed on your system 

	File Input/Output

		def browseCustomData()			browse the files in a customData folder if folder not exist, script makes one
		def listScripts()				get list of all of the script currently in the uses script directory
		def processFooLine				read example file Foo.txt as action to run scirpt	
		def readFooFile()				read text file (exmaple foo.txt needed)
		def writeFOO()					write text file
		def markAsPickup(obj, attr)		add the attribute and set its value
		def listPickups()  				???
		def saveFOBFile()				writing out a binary file
		def readFOBFile()				read binary file
		def readMultipleTypes()			script that is capable of reading in multiple file types 
		def goldenRatio(w=100)			generate a sequance golden ratio numbers
"""

'''------------------------------------------------------------------------
							My Functions
------------------------------------------------------------------------'''

def sortDictionary(d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}):
	''' sort a dictionary'''
	print('Original dictionary : ',d)
	sorted_d = sorted(d.items(), key=operator.itemgetter(1))
	print('Dictionary in ascending order by value : ',sorted_d)
	return sorted_d


def importObj(myFolder = "C:/Users/User/Documents/maya/2020/scripts/myFolder/"):
	''' impoirt a external obj file from root import'''
	fileType = 'OBJ'

	objFiles = cmds.getFileList(folder = myFolder, filespec = '*.%s' % fileType)

	for item in objFiles:
		fname = os.path.join(myFolder, item)
		objName, ext = os.path.splitext(os.path.basename(fname))
		# import each file
		imported_objects = cmds.file(fname, i=True, rnn=True) 
		transforms = cmds.ls(imported_objects, type='transform')
		
		for i, object in enumerate(transforms):
			# rename it
			goodName = '%s_%s' % (objName, str(i+1).zfill(3))
			cmds.rename(object, goodName)


def goldenRatio(w=100):
	'''generate a sequance golden ratio numbers'''
	x = 1
	y = 0
	z = 0
	for i in range(w):
		z = y
		y = x + y
		x = z
		print(y)


def listAllObjs():
	'''list all in the scene objectst'''
	objsList = []
	allObjects = cmds.ls(type='surfaceShape')
	for obj in allObjects:
		objsList.append(obj)
		print obj.replace('Shape','')
	return objsList


def listSelected():
	''' list al selected objects'''
	selList = []
	selectedObjs = cmds.ls( selection=True )
	selList.append(selectedObjs)
	print(selectedObjs)
	return selList

'''------------------------------------------------------------------------
								Python UI
------------------------------------------------------------------------'''

def showUI():  
	'''simple UI window'''
	myWin = cmds.window(title="Simple Window", widthHeight=(300, 200))
	cmds.columnLayout()    
	cmds.text(label="Hello, Maya!")
	cmds.button(label="Make Cube", command=buttonFunction)
	cmds.showWindow(myWin)

def buttonFunction(args):
	''' showUI button function, create a poly cube'''
	cmds.polyCube()


global sphereCountField
global sphereRadiusField

def inputUI():
	''' 
	Create a window
	- input a value
	- generate a array of speres, based on the input value
	'''
	global sphereCountField    
	global sphereRadiusField    

	myWin = cmds.window(title="Make Spheres", widthHeight=(300, 200))    
	cmds.columnLayout()    
	sphereCountField = cmds.intField(minValue=1)    
	sphereRadiusField = cmds.floatField(minValue=0.5)    
	cmds.button(label="Make Spheres", command=makeSpheres)    
	cmds.showWindow(myWin)

def makeSpheres(*args):
	'''
	For the UIobjAray method: make spheres
	''' 
	global sphereCountField    
	global sphereRadiusField    

	numSpheres = cmds.intField(sphereCountField, query=True, value=True)
	myRadius = cmds.floatField(sphereRadiusField, query=True, value=True)    

	for i in range(numSpheres):        
		cmds.polySphere(radius=myRadius)        
		cmds.move((i * myRadius * 2.2), 0, 0)


def nestedLayout():
	'''
	each row has 2 controls: label and text field
	'''
	win = cmds.window(title="Nested Layouts", widthHeight=(300,200))        
	
	cmds.columnLayout()
	cmds.rowLayout(numberOfColumns=2)   
	cmds.text(label="Input One:")  
	inputOne = cmds.intField() 
	cmds.setParent("..")
	
	cmds.rowLayout(numberOfColumns=2)
	cmds.text(label="Input Two:")
	inputTwo = cmds.intField()
	cmds.setParent("..")

	cmds.showWindow(win)


def tabUI():
	''' simple UI window with Tabs'''
	win = cmds.window(title="Tabbed Layout", widthHeight=(300, 300))
	tabs = cmds.tabLayout()        

	# add first tab
	firstTab = cmds.columnLayout()
	cmds.tabLayout(tabs, edit=True, tabLabel=[firstTab, 'Simple Tab'])
	cmds.button(label="Button")
	cmds.setParent("..")

	# add second tab, and setup scrolling
	newLayout = cmds.scrollLayout()
	cmds.tabLayout(tabs, edit=True, tabLabel=[newLayout, 'ScrollingTab'])
	cmds.columnLayout()

	for i in range(20):
		cmds.button(label="Button " + str(i+1))
	cmds.setParent("..")
	cmds.setParent("..")
	
	cmds.showWindow(win)


def BarMenuUI():
	'''simple UI window with top menu bar'''
	win = cmds.window(title="Menu Example", menuBar=True, widthHeight=(300,200))
	fileMenu = cmds.menu(label="File")
	loadOption = cmds.menuItem(label="Load")
	saveOption = cmds.menuItem(label="Save")
	cmds.setParent("..")

	objectsMenu = cmds.menu(label="Objects")
	sphereOption = cmds.menuItem(label="Make Sphere")
	cubeOption = cmds.menuItem(label="Make Cube")
	cmds.setParent("..")

	cmds.columnLayout()
	cmds.text(label="Put the rest of your interface here")

	cmds.showWindow(win)




'''------------------------------------------------------------------------
							Working with Geometry
------------------------------------------------------------------------'''

def checkSelection():
	'''Notify use if a poly object is selected or not'''

	selectedObjs = cmds.ls(selection=True)    

	if (len(selectedObjs) < 1):        
		cmds.error('Please select an object')
		
	lastSelected = selectedObjs[-1]

	isPolygon = currentSelectionPolygonal(lastSelected)

	if (isPolygon):
		print('FOUND POLYGON')
	else:
		cmds.error('Please select a polygonal object')

def currentSelectionPolygonal(obj):
	'''CheckSelection extention'''
	shapeNode = cmds.listRelatives(obj, shapes=True)
	nodeType = cmds.nodeType(shapeNode)

	if nodeType == "mesh":
		return True

	return False



def getPolyData():
	'''Examine data for a currently-selected polygonal object'''

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


def getNURBSInfo():
	'''Examine data for a currently-selected NURBS object'''
	selectedObjects = cmds.ls(selection=True)
	obj = selectedObjects[-1]
	degU = cmds.getAttr(obj + '.degreeU')
	spansU = cmds.getAttr(obj + '.spansU')
	cvsU = degU + spansU
	print('CVs (U): ', cvsU)
	
	degV = cmds.getAttr(obj + '.degreeV')
	spansV = cmds.getAttr(obj + '.spansV')
	cvsV = degV + spansV
	print('CVs (V): ', cvsV)


def makeCurve():
	'''Create Curve Square'''
	theCurve = cmds.curve(degree=1, p=[(-0.5,-0.5,0),(0.5,- 0.5,0),(0.5,0.5,0),(-0.5,0.5,0), (-0.5, -0.5, 0)])

def curveFunction(i):
	x = math.sin(i)
	y = math.cos(i)
	x = math.pow(x, 3)
	y = math.pow(y, 3)    
	return (x,y)

def complexCurve():
	'''Create Curve with math module'''
	theCurve = cmds.curve(degree=3, p=[(0,0,0)])
	for i in range(0, 32):
		val = (math.pi * 2)/32 * i
		newPoint = curveFunction(val)
		cmds.curve(theCurve, append=True, p=[(newPoint[0], newPoint[1], 0)])



def makeFace():
	'''Make a poly Face'''
	newFace = cmds.polyCreateFacet(p=[(-1,-1,0),(1,- 1,0),(1,1,0),(-1,1,0)])

def makeFaceWithHole():
	''' Create a poly Face, with a bit hole inside'''
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

def addNoise(amt=0.2):
	'''add Noise to selected poly object'''
	selectedObjs = cmds.ls(selection=True)
	obj = selectedObjs[-1]
	
	shapeNode = cmds.listRelatives(obj, shapes=True)

	if (cmds.nodeType(shapeNode) != 'mesh'):
		cmds.error('Select a mesh')        
		return    

	numVerts = cmds.polyEvaluate(obj, vertex=True)
	
	randAmt = [0, 0, 0]    
	for i in range(0, numVerts):
		
		for j in range(0, 3):
			randAmt[j] = random.random() * (amt*2) - amt
			
		vertexStr = "{0}.vtx[{1}]".format(obj, i)
		cmds.select(vertexStr, replace=True)
		cmds.move(randAmt[0], randAmt[1], randAmt[2], relative=True)
	
	cmds.select(obj, replace=True)



'''------------------------------------------------------------------------
								UVs and Materials
------------------------------------------------------------------------'''

def uvInfo():
	'''Selected object, UV info: number of UVs, position first UV, if first Edge is border'''
	sel = cmds.ls(selection=True)
	obj = sel[0]
	
	uvs = cmds.polyEvaluate(obj, uvComponent=True)
	uvPos = cmds.polyEditUV(obj + '.map[0]', query=True)
	isFirstEdgeSplit = isSplitEdge(obj, 0)
	
	print('Num UVs: ' + str(uvs))
	print("Position of first UV: ", uvPos)
	print("First edge is split: ", isFirstEdgeSplit)
	
	cmds.select(obj, replace=True)

def isSplitEdge(obj, index):
	'''Extension of uvInfo'''
	result = cmds.polyListComponentConversion(obj + '.e[' + str(index) + ']',fromEdge=True, toUV=True)
	cmds.select(result, replace=True)
	vertNum = cmds.polyEvaluate(vertexComponent=True)
	
	result = cmds.polyListComponentConversion(obj + '.e[' + str(index) + ']',fromEdge=True, toVertex=True)
	cmds.select(result, replace=True)
	uvNum = cmds.polyEvaluate(uvComponent=True)

	if (uvNum == vertNum):        
		return False    

	return True


def layoutUVs():
	'''Select object-create UVs (Windows/Modeling Editor/UV Editor)'''
	selected = cmds.ls(selection=True)
	obj = selected[0]
	
	totalFaces = cmds.polyEvaluate(obj, face=True)
	
	oneThird = totalFaces/3
	
	startFace = 0
	endFace = oneThird - 1
	cmds.polyProjection(obj + '.f[' + str(startFace) + ':' + str(endFace) + ']',type="planar")
	
	startFace = oneThird
	endFace = (oneThird * 2) - 1
	cmds.polyProjection(obj + '.f[' + str(startFace) + ':' + str(endFace) + ']',type="cylindrical")
	
	startFace = (oneThird * 2)
	endFace = totalFaces - 1
	cmds.polyProjection(obj + '.f[' + str(startFace) + ':' + str(endFace) + ']',type="spherical")


def createNodes():
	'''create a new shader (Windows/Rendering Editors/Hypershade)'''
	shaderNode = cmds.shadingNode('blinn', asShader=True)
	rampTexture = cmds.shadingNode('ramp', asTexture=True)
	samplerNode = cmds.shadingNode('samplerInfo', asUtility=True)

	cmds.setAttr(rampTexture + '.interpolation', 0)
	cmds.setAttr(rampTexture + '.colorEntryList[0].position', 0)
	cmds.setAttr(rampTexture + '.colorEntryList[1].position', 0.45)
	cmds.setAttr(rampTexture + '.colorEntryList[0].color', 0, 0, 0, type="float3")
	cmds.setAttr(rampTexture + '.colorEntryList[1].color', 1, 0, 0,type="float3")
	
	cmds.connectAttr(samplerNode + '.facingRatio', rampTexture + '.vCoord')
	cmds.connectAttr(rampTexture + '.outColor', shaderNode + '.color')



def shadersFromObject(obj):    
	cmds.select(obj, replace=True)    
	cmds.hyperShade(obj, shaderNetworksSelectMaterialNodes=True)    
	shaders = cmds.ls(selection=True)    
	return shaders

def isGeometry(obj):    
	shapes = cmds.listRelatives(obj, shapes=True)    
	
	shapeType = cmds.nodeType(shapes[0])    
	geometryTypes = ['mesh', 'nurbsSurface', 'subdiv']    
	
	if shapeType in geometryTypes:        
		return True    

	return False

def findUnattachedObjects():
	'''Select object - create shader & add to selected object (ERROR for now) ''' 
	objects = cmds.ls(type="transform")    
	
	unShaded = []    
	
	for i in range(0, len(objects)):        
		if (isGeometry(objects[i])):            
			shaders = shadersFromObject(objects[i])            
			if (len(shaders) < 1):                
				unShaded.append(objects[i])    
				
	newShader = cmds.shadingNode('blinn', asShader=True)
	cmds.setAttr(newShader + '.color', 0, 1, 1, type="double3")    
	
	cmds.select(unShaded, replace=True)
	cmds.hyperShade(assign=newShader)


def objectsFromShader(shader='lamber1'):
	'''input 'shaderName', get list of objects using this shader'''
	cmds.hyperShade(objects=shader)
	objects = cmds.ls(selection=True)   
	return objects

def keepCentered():
	'''select 3 object. second object positon will be average of the other 2'''
	objects = cmds.ls(selection=True)    

	if (len(objects) < 3):        
		cmds.error('Please select at least three objects')    

	avgNode = cmds.shadingNode('plusMinusAverage', asUtility=True)    
	cmds.setAttr(avgNode + '.operation', 3)    

	for i in range(0, len(objects) - 1):        
		cmds.connectAttr(objects[i] + '.translateX', avgNode +'.input3D[{0}].input3Dx'.format(i))        
		cmds.connectAttr(objects[i] + '.translateZ', avgNode +'.input3D[{0}].input3Dz'.format(i))    

		controlledObjIndex = len(objects) - 1    

		cmds.connectAttr(avgNode + '.output3D.output3Dx',objects[controlledObjIndex] + '.translateX')
		cmds.connectAttr(avgNode + '.output3D.output3Dz',objects[controlledObjIndex] + '.translateZ')


'''------------------------------------------------------------------------
								Rigging
------------------------------------------------------------------------'''

def createSimpleSkeleton(joints=5):    
	'''Creates a simple skeleton as a single chain of bones    ARGS:        
	joints- the number of bones to create    '''    

	cmds.select(clear=True)    

	bones = []    
	pos = [0, 0, 0]    

	for i in range(0, joints):        
		pos[1] = i * 5        
		bones.append(cmds.joint(p=pos))    

	cmds.select(bones[0], replace=True)


def createHand(fingers=5, joints=3):    
	'''Creates a set of 'fingers', each with a set number of joints    ARGS:        
	fingers- the number of joint chains to create        
	joints- the number of bones per finger    '''    
	cmds.select(clear=True)    

	baseJoint = cmds.joint(name='wrist', p=(0,0,0))    
	
	fingerSpacing = 2    
	palmLen = 4    
	jointLen = 2    

	for i in range(0, fingers):        
		cmds.select(baseJoint, replace=True)        
		pos = [0, palmLen, 0]        

		pos[0] = (i * fingerSpacing) - ((fingers-1) * fingerSpacing)/2        

		cmds.joint(name='finger{0}base'.format(i+1), p=pos)        

		for j in range(0, joints):            
			cmds.joint(name='finger{0}joint{1}'.format((i+1),(j+1)),relative=True, p=(0,jointLen, 0))
	
	cmds.select(baseJoint, replace=True)


def setDrivenKeys(): 
	'''select joint and runscript, all bones downstream rotate wehn rotate Z'''   
	objs = cmds.ls(selection=True)    
	baseJoint = objs[0]    
	
	driver = baseJoint + ".rotateZ"    
	
	children = cmds. listRelatives(children=True, allDescendents=True)    

	for bone in children:        
		driven = bone + ".rotateZ"        
		
		cmds.setAttr(driver, 0)        
		cmds.setDrivenKeyframe(driven, cd=driver, value=0, driverValue=0)        
		
		cmds.setAttr(driver, 30)        
		cmds.setDrivenKeyframe(driven, cd=driver, value=30, driverValue=30)    

		cmds.setAttr(driver, 0)


def addCustomAttributes():  
	'''add cutum attrbiute''' 
	objs = cmds.ls(selection=True)    
	cmds.addAttr(objs[0], shortName="blink", longName="blink", defaultValue=0,minValue=-1, maxValue=1, keyable=True)    
	cmds.addAttr(objs[0], shortName="ikfkR", longName="ikfkRight",attributeType="bool", keyable=True)    

	cmds.addAttr(objs[0], shortName="ikfkL", longName="ikfkLeft",attributeType="enum", enumName="IK:FK", keyable=True)    
	cmds.setAttr(objs[0]+".rotateX", edit=True, lock=True, keyable=False,channelBox=False)   

	for att in ['rotateY','rotateZ','scaleX','scaleY','scaleZ']:        
		lockAndHide(objs[0], att)

def lockAndHide(obj, att):
	''' remove selected attribute. argruemtns: 'objectName', 'attributeName'''    
	fullAttributeName = obj + '.' + att    
	cmds.setAttr(fullAttributeName, edit=True, lock=True, keyable=False,channelBox=False)

	setup()
	addCustomAttributes()


def rigUI(): 
	'''setup IK Leg'''   
	myWin = cmds.window(title="IK Rig", widthHeight=(200, 200))    
	cmds.columnLayout()    
	cmds.button(label="Make Locators", command=makeLocators, width=200)    
	cmds.button(label="Setup IK", command=setupIK, width=200)    
	cmds.showWindow(myWin)

def makeLocators(args):    
	global hipLoc    
	global kneeLoc    
	global ankleLoc    
	global footLoc    

	hipLoc = cmds.spaceLocator(name="HipLoc")    
	kneeLoc = cmds.spaceLocator(name="KneeLoc")    
	ankleLoc = cmds.spaceLocator(name="AnkleLoc")    
	footLoc = cmds.spaceLocator(name="FootLoc")    

	cmds.xform(kneeLoc, absolute=True, translation=(0, 5, 0))    
	cmds.xform(hipLoc, absolute=True, translation=(0, 10, 0))    
	cmds.xform(footLoc, absolute=True, translation=(2, 0, 0))

def setupIK(args):    
	global hipLoc    
	global kneeLoc    
	global ankleLoc    
	global footLoc    

	cmds.select(clear=True)    

	pos = cmds.xform(hipLoc, query=True, translation=True, worldSpace=True)    
	hipJoint = cmds.joint(position=pos)    

	pos = cmds.xform(kneeLoc, query=True, translation=True, worldSpace=True)    
	kneeJoint = cmds.joint(position=pos)    
	
	pos = cmds.xform(ankleLoc, query=True, translation=True, worldSpace=True)    
	ankleJoint = cmds.joint(position=pos)    

	pos = cmds.xform(footLoc, query=True, translation=True, worldSpace=True)    
	footJoint = cmds.joint(position=pos)    

	cmds.ikHandle(startJoint=hipJoint, endEffector=ankleJoint)



'''------------------------------------------------------------------------
								Animation
------------------------------------------------------------------------'''

def getAnimationData():
	'''Select Object, runscirpt, check animation info (Windows/Animation Editors/Graph Editor)'''
	objs = cmds.ls(selection=True)
	obj = objs[0]
	
	animAttributes = cmds.listAnimatable(obj);

	for attribute in animAttributes:
		
		numKeyframes = cmds.keyframe(attribute, query=True, keyframeCount=True)

		if (numKeyframes > 0):
			print("---------------------------")
			print("Found ", numKeyframes, " keyframes on ", attribute)
			
			times = cmds.keyframe(attribute, query=True, index=(0,numKeyframes),timeChange=True)
			values = cmds.keyframe(attribute, query=True, index=(0,numKeyframes), valueChange=True)
			
			print('frame#, time, value')
			for i in range(0, numKeyframes):
				print(i, times[i], values[i])
			
			print("---------------------------")



def makeAnimLayer(layerName='newLayer'):
	'''make animation layer (ChannelBox/Anim)'''
	baseAnimationLayer = cmds.animLayer(query=True, root=True)    
	
	foundLayer = False    

	if (baseAnimationLayer != None):        
		childLayers = cmds.animLayer(baseAnimationLayer, query=True,children=True)        

		if (childLayers != None) and (len(childLayers) > 0):            
			if layerName in childLayers:                
				foundLayer = True    

		if not foundLayer:        
			cmds.animLayer(layerName)    
		else:        
			print('Layer ' + layerName + ' already exists')



def getAttName(fullname):    
	parts = fullname.split('.')    
	return parts[-1]



def copyKeyframes():
	'''Select the animated object, shift-select at least one other object, and run the script'''
	objs = cmds.ls(selection=True)    

	if (len(objs) < 2):        
		cmds.error("Please select at least two objects")    

	sourceObj = objs[0]    

	animAttributes = cmds.listAnimatable(sourceObj);    

	for attribute in animAttributes:        

		numKeyframes = cmds.keyframe(attribute, query=True, keyframeCount=True)        

		if (numKeyframes > 0):            
			cmds.copyKey(attribute)            

			for obj in objs[1:]:                
				cmds.pasteKey(obj, attribute=getAttName(attribute),option="replace")


def setKeyframes():
	'''Run the preceding script with an object selected and trigger playback. You should see the objectmove up and down'''  
	objs = cmds.ls(selection=True)    
	obj = objs[0]    

	yVal = 0    
	xVal = 0    
	frame = 0    

	maxVal = 10    

	for i in range(0, 20):        
		frame = i * 10        
		xVal = i * 2        

		if i % 2 == 1:            
			yVal = 0        
		else:            
			yVal = maxVal            
			maxVal *= 0.8        

		cmds.setKeyframe(obj + '.translateY', value=yVal, time=frame)        
		cmds.setKeyframe(obj + '.translateX', value=xVal, time=frame)


def createExpression(att='translateY', minVal=5, maxVal=10, speed=1):
	'''add speed attribute to selected object and tie the attribute to a sine wave based on the current time'''  
	objs = cmds.ls(selection=True)    
	obj = objs[0]    

	cmds.addAttr(obj, longName="speed", shortName="speed", min=0, keyable=True)    
   
	amplitude = (maxVal - minVal)/2.0
	offset = minVal + amplitude    

	baseString =  "{0}.{1} = ".format(obj, att)    
	sineClause = '(sin(time * ' + obj + '.speed)'    
	valueClause = ' * ' + str(amplitude) + ' + ' + str(offset) + ')'    

	expressionString = baseString + sineClause + valueClause    

	cmds.expression(string=expressionString)


'''------------------------------------------------------------------------
								Rendering
------------------------------------------------------------------------'''


def createLightRig():
	'''three lights created-two spotlight and one directionla light'''
	offsetAmount = 10    
	lightRotation = 30    

	newLight = cmds.spotLight(rgb=(1, 1, 1), name="KeyLight")    
	lightTransform = cmds.listRelatives(newLight, parent=True)    
	keyLight = lightTransform[0]    

	newLight = cmds.spotLight(rgb=(0.8, 0.8, 0.8), name="FillLight")    
	lightTransform = cmds.listRelatives(newLight, parent=True)    
	fillLight = lightTransform[0]    

	newLight = cmds.directionalLight(rgb=(0.2, 0.2, 0.2), name="BackLight")    
	lightTransform = cmds.listRelatives(newLight, parent=True)    
	backLight = lightTransform[0]    

	cmds.move(0, 0, offsetAmount, keyLight)    
	cmds.move(0, 0, 0, keyLight + ".rotatePivot")    
	cmds.rotate(-lightRotation, lightRotation, 0, keyLight)    

	cmds.move(0, 0, offsetAmount, fillLight)    
	cmds.move(0, 0, 0, fillLight + ".rotatePivot")    
	cmds.rotate(-lightRotation, -lightRotation, 0, fillLight)    

	cmds.move(0, 0, offsetAmount, backLight)    
	cmds.move(0, 0, 0, backLight + ".rotatePivot")    
	cmds.rotate(180 + lightRotation, 0, 0, backLight)    

	rigNode = cmds.group(empty=True, name="LightRig")    

	cmds.parent(keyLight, rigNode)    
	cmds.parent(fillLight, rigNode)    
	cmds.parent(backLight, rigNode)    

	cmds.select(rigNode, replace=True)

'''
def ThreeLightUI():
	#new window with a control for each light in the scene
	global lights
	global lightControls
	global lightNum
	
	lights = []
	lightControls = []
	lightNum = 0

	if (cmds.window("ahLightRig", exists=True)):            
		cmds.deleteUI("ahLightRig")        

	win = cmds.window("ahLightRig", title="Light Board")        
	cmds.columnLayout()        

	lights = cmds.ls(lights=True)        

	for light in lights:
		createLightControl(light)

	cmds.showWindow(win)


def updateColor(lightID):
	newColor = cmds.colorSliderGrp(lightControls[lightID], query=True,rgb=True)        
	cmds.setAttr(lights[lightID]+ '.color', newColor[0], newColor[1],newColor[2], type="double3")    


def createLightControl(lightShape):
	global lights
	global lightControls
	global lightNum        
	
	parents = cmds.listRelatives(lightShape, parent=True)        
	lightName = parents[0]        
	
	color = cmds.getAttr(lightShape + '.color')        
	changeCommandFunc = partial(updateColor, lightNum)        

	newSlider = cmds.colorSliderGrp(label=lightName, rgb=color[0],changeCommand=changeCommandFunc)

	lights.append(lightShape)
	lightControls.append(newSlider)

	lightNum += 1

'''

def makeCameraRig():
	'''Run the script, and you should have four isometric cameras, all looking at the origin'''  
	aimLoc = cmds.spaceLocator()    
	
	offset = 10    

	for i in range(0, 4):        
		newCam = cmds.camera(orthographic=True)        
		cmds.aimConstraint(aimLoc[0], newCam[0], aimVector=(0,0,- 1))        

		xpos = 0        
		ypos = 6        
		zpos = 0        

		if (i % 2 == 0):            
			xpos = -offset        
		else:            
			xpos = offset        

		if (i >= 2):            
			zpos = -offset        
		else:            
			zpos = offset        

		cmds.move(xpos, ypos, zpos, newCam[0])


FRAME_WIDTH = 400
FRAME_HEIGHT = 300

def renderSpriteSheet():
	'''render out multiple views. NOTE: PIL installed on your system. ''' 
	allCams = cmds.listCameras()    

	customCams = []    

	for cam in allCams:        
		if (cam not in ["front", "persp", "side", "top"]):            
			customCams.append(cam)    

	# make sure we're rendering TGAs    
	cmds.setAttr("defaultRenderGlobals.imageFormat", 19)    

	# create a new image    
	fullImage = Image.new("RGBA", (FRAME_WIDTH*len(customCams), FRAME_HEIGHT),"black")    

	# run through each camera, rendering the view and adding it to the mage        
	for i in range(0, len(customCams)):        
		result = cmds.render(customCams[i], x=FRAME_WIDTH, y=FRAME_HEIGHT)        
		tempImage = Image.open(result)        
		fullImage.paste(tempImage, (i*FRAME_WIDTH,0))    

	basePath = cmds.workspace(query=True, rootDirectory=True)    
	fullPath = os.path.join(basePath, "images", "frames.tga")    
	fullImage.save(fullPath)


'''------------------------------------------------------------------------
							File Input/Output
------------------------------------------------------------------------'''

def browseCustomData():
	'''browse the files in a customData folder if folder not exist, script makes one'''
	projDir = cmds.internalVar(userWorkspaceDir=True)    # current project directory
	print('current directory: {}'.format(projDir))

	newDir = os.path.join(projDir, 'customData')  
	print('new directory:     {}'.format(newDir))  

	# create new directory
	if (not os.path.exists(newDir)):        
		os.makedirs(newDir)    
	
	# open directory window
	cmds.fileDialog2(startingDirectory=newDir)

def listScripts():
	''' get list of all of the script currently in the uses script directory'''
	scriptDir = cmds.internalVar(userScriptDir=True)    
	print(os.listdir(scriptDir))


def processFooLine(line):
	'''read example file Foo.txt as action to run scirpt'''  
	parts = line.split()    

	if (len(parts) < 4):        
		cmds.error("BAD DATA " + line)    

		x = float(parts[1])    
		y = float(parts[2])    
		z = float(parts[3])    

		if (parts[0] == "spr"):        
			cmds.sphere()    
		elif (parts[0] == "cub"):        
			cmds.polyCube()    

		cmds.move(x, y, z)

def readFooFile():
	'''read text file (exmaple foo.txt needed)'''
	filePath = cmds.fileDialog2(fileMode=1, fileFilter="*.foo")    
	fileRef = open(filePath[0], "r")    

	line = fileRef.readline()   
	while (line):        
		processFooLine(line)        
		line = fileRef.readline()    

	fileRef.close()


def checkHistory(obj):    
	history = cmds.listHistory(obj)    

	geoType = ""    

	for h in history:        

		if (h.startswith("makeNurbSphere")):            
			geoType = "spr"        

		if (h.startswith("polyCube")):            
			geoType = "cub"    

	return geoType


def writeFOO():
	''' write text file'''
	filePath = cmds.fileDialog2(fileMode=0, fileFilter="FOO files (*.foo)")    

	if (filePath == None):        
		return    

	fileRef = open(filePath[0], "w")    

	objects = cmds.ls(type="transform")    

	for obj in objects:        
		geoType = checkHistory(obj)        

		if (geoType != ""):            

			position = cmds.xform(obj, query=True, translation=True,worldSpace=True)            
			positionString = " ".join(format(x, ".3f") for x in position)            

			newLine = geoType + " " + positionString + "\n"            
			fileRef.write(newLine)    

	fileRef.close()


def markAsPickup(obj, pickupType):
	'''add the attribute and set its value''' 
	customAtts = cmds.listAttr(obj, userDefined=True)    

	if ("pickupType" not in customAtts):        
		cmds.addAttr(obj, longName="pickupType", keyable=True)    

	cmds.setAttr(obj + ".pickupType", pickupType)


def listPickups():    
	'''???'''
	pickups = []    
	objects = cmds.ls(type="transform")    

	for obj in objects:        
		customAtts = cmds.listAttr(obj, userDefined=True)        
		if (customAtts != None):            
			if ("pickupType" in customAtts):                
				print(obj)                
				pickups.append(obj)
	return pickups


def checkHistory(obj):    
	history = cmds.listHistory(obj)    

	geoType = ""    

	for h in history:        

		if (h.startswith("makeNurbSphere")):            
			geoType = "spr"        

		if (h.startswith("polyCube")):            
			geoType = "cub"    

	return geoType


def writeFOBHeader(f):    
	headerStr = 'iii'    
	f.write(struct.pack(headerStr, 3, 3, 4))


def writeObjData(obj, geoType, f):    
	position = cmds.xform(obj, query=True, translation=True, worldSpace=True)    

	f.write(geoType)    

	f.write(struct.pack('fff', position[0], position[1], position[2]))


def saveFOBFile():
	''' writing out a binary file'''    
	filePath = cmds.fileDialog2(fileMode=0, fileFilter="FOO Binary files(*.fob)")    

	if (filePath == None):        
		return    

	fileRef = open(filePath[0], "wb")    

	writeFOBHeader(fileRef)    
	objects = cmds.ls(type="transform")    

	for obj in objects:        
		geoType = checkHistory(obj)        

		if (geoType != ""):
			writeObjData(obj, geoType, fileRef)            
			# positionString = " ".join(format(x, ".3f") for x in position)    

	fileRef.close()


def makeObject(objType, pos):    
	newObj = None    

	if (objType == "spr"):        
		newObj = cmds.sphere()    
	elif (objType == "cub"):        
		newObj = cmds.polyCube()    

	if (newObj != None):        
		cmds.move(pos[0], pos[1], pos[2])


def readFOBFile():
	'''read binary file'''
	filePath = cmds.fileDialog2(fileMode=1, fileFilter="FOO binary files(*.fob)")    

	if (filePath == None):        
		return    

	f = open(filePath[0], "rb")    

	data = f.read()    

	headerLen = 12    

	res = struct.unpack('iii', data[0:headerLen])    

	geoTypeLen = res[0]    
	numData = res[1]    
	bytesPerData = res[2]    

	objectLen = geoTypeLen + (numData * bytesPerData)    

	numEntries = (len(data) - headerLen) / objectLen    

	dataStr = 'f'*numData    

	for i in range(0,numEntries):        
		start = (i * objectLen) + headerLen         
		end = start + geoTypeLen        

		geoType = data[start:end]        

		start = end
		end = start + (numData * bytesPerData)        

		pos = struct.unpack(dataStr, data[start:end])        
		makeObject(geoType, pos)    

	f.close()


def readMultipleTypes():
	''' script that is capable of reading in multiple file types'''  
	fileRes = cmds.fileDialog2(fileMode=1, fileFilter="FOO files(*.foo);;FOObinary files (*.fob)")    

	if (fileRes == None):        
		return    

	filePath = fileRes[0]    

	pathParts = os.path.splitext(filePath)    
	extension = pathParts[1]    

	if (extension == ".foo"):        
		readFOOFile(filePath)    
	elif (extension == ".fob"):        
		readFOBFile(filePath)    
	else:        
		cmds.error("unrecognized file type")
