import MASH.api as mapi		# helper scripts to manipulation of MASH networks
import maya.cmds as cmds

import unittest #  unittest comes with Python. Unit testing makes your code future proof
reload(mapi) # reload(moduleName)
import maya.mel as mel # import mel to python
import time # provides various time-related functions: datetime, calendar, etc
#import MASH.dynamicsUtils as dynamics # ???


'''
Source:
https://help.autodesk.com/cloudhelp/2018/ENU/Maya-Tech-Docs/MASH/examples.html



import sys

#add folder to PythonPath
sys.path.append('c:/Users/12213119/Documents/maya/2020/scripts/Lab/')

# print PythonPaths
from pprint import pprint
sys.path
pprint(sys.path)

# import file
import mahsCookbook

# refresh file
#reload(mahsCookbook)

# call script
mahsCookbook.Function()

'''
def test():
	print('sub')


def mashSignal():
	'''
	Create a sphere filled with cubes 
	and when the a signal passes throught,
	the cube on te surface grow

	1. create ofbjects and a Mash network
	2. add a signal node: Adds either 4D Noise or Trigonometric animation to the network. 
	3. add falloff the the signal node
	4. distribute node comes with the Mash network, in this case we distribute the cubes on the surface
	'''

	# create Objects
	sphereToDistributeOn = cmds.polySphere(r=12)
	cmds.polyCube()

	# create a new MASH network
	mashNetwork = mapi.Network()
	mashNetwork.createNetwork(name="HelloWorld")
	
	# print out the default node names
	print mashNetwork.waiter
	print mashNetwork.distribute
	print mashNetwork.instancer

	# add Node: Signal
	node = mashNetwork.addNode("MASH_Signal")
	# set Attribute: Signal/Scale/ScaleX
	cmds.setAttr(node.name+".scaleX", 10)
	# print: name of the signal node
	print node.name

	# add Attribute: Signal/Falloff Object/ create:FallOff
	falloff = node.addFalloff()
	 # list command list of DAG object, p= Returns the parent of this dag node 
	falloffParent = cmds.listRelatives(falloff, p=True)[0]
	# set Attribute: Falloff Object/translateX
	cmds.setAttr(falloffParent+".translateX", 8)

	# distributs the cubes on the sphere surface
	mashNetwork.meshDistribute(sphereToDistributeOn[0])
	# set Attribute: Distribute/Number of Points
	mashNetwork.setPointCount(1000)

	# print all nodes in the network
	nodes = mashNetwork.getAllNodesInNetwork()
	print "All nodes in network: []".format(nodes) # set([u'Falloff_HelloWorld_SignalShape', u'HelloWorld_Signal', u'HelloWorld_ReproMesh', u'HelloWorld_Distribute', u'HelloWorld_Repro', u'HelloWorld', u'Falloff_HelloWorld_Signal'])

	# find all the falloffs in the network
	for node in nodes:
		mashNode = mapi.Node(node)
		falloffs = mashNode.getFalloffs()
		
		# found falloff
		if falloffs:
			print node+" has the following falloffs: " + str(falloffs) # [u'Falloff_HelloWorld_SignalShape']



def dynamicConstraints():
	'''
	create an array of plane, and position them in a circle.
	Duplicate them next to each other, and give them some Dynamics constraines

	1. create file
	2. set perspective view
	3. create object
	4. create Mash network
	5. create replicator:  duplicate network and position in positionZ
	6. create dynamics: add Maya Bullut to Mash Network
	7. create constain: enable 'Breakable', and set 'constainer Distance'
	8. create channelRandom
	9. create falloff: Area where contrain breaksoff
	10. show constainers
	11. playbast simulation
	'''

	# force a new file on default location
	cmds.file(force=True, new=True)

	# set Attributes: perspective view
	cmds.setAttr('persp.translateX', 35)
	cmds.setAttr('persp.translateY', 20)
	cmds.setAttr('persp.translateZ', 35)
	cmds.setAttr('persp.rotateX', -30)
	cmds.setAttr('persp.rotateY', 45)

	# create Object: Plane
	cmds.polyPlane()

	# create MASH network
	mashNetwork = mapi.Network()
	mashNetwork.createNetwork("DymamicsNetwork")
	# set Attributes: distribute
	cmds.setAttr( mashNetwork.distribute+".arrangement", 2) # Type: Radial
	cmds.setAttr( mashNetwork.distribute+".pointCount", 30) # number of points

	# create Node: Replictor
	replicantsNode = mashNetwork.addNode("MASH_Replicator")
	# set Attributes: Replictor
	cmds.setAttr( replicantsNode.name+".replicants", 4) # duplicate number of times
	cmds.setAttr( replicantsNode.name+".offsetPositionZ", -1.5) # offsett duplicates in posiztion Z

	# create Node: Dynamics
	dynamicsNode = mashNetwork.addNode("MASH_Dynamics")

	# create Node: Dynamics/Constains
	constraintNode = mashNetwork.addConstraint(dynamicsNode)
	# set Attributes: Constrain
	cmds.setAttr( constraintNode.name+".constraintBreakable", 1)
	cmds.setAttr( constraintNode.name+".constraintDistance", 2.5)

	#create Node: Dynamics/Constains/ChannelRandom
	channelRandom = mashNetwork.addChannelRandom(constraintNode)
	# set Attributes: ChannelRandom
	cmds.setAttr( channelRandom.name+".dynamicsChannelName", 0)
	cmds.setAttr( channelRandom.name+".constraintChannelName", 3)
	cmds.setAttr( channelRandom.name+".startValue", 30)

	# create Node:Dynamics/Constains/ChannelRandom/Falloff
	falloff = channelRandom.addFalloff()
	# set Attributes: Falloff
	cmds.setAttr( falloff+".falloffShape", 2)
	cmds.setAttr( falloff+".innerRadius", 1)
	cmds.setAttr( falloff+".falloffRamp[0].falloffRamp_FloatValue", 0.9)

	# select Node: falloff
	falloffParent = cmds.listRelatives(falloff, parent=True)[0]
	# set Attributes: Falloff
	cmds.setAttr( falloffParent+".invertFalloff", 1)
	cmds.setAttr( falloffParent+".translateY", -10)
	cmds.setAttr( falloffParent+".translateZ", -3)

	# list: ButtelSolver
	solver = cmds.ls(type="MASH_BulletSolver")[0] # select object type
	# set Attributes: BulletSolver
	cmds.setAttr( solver+".displayConstraints", 1) # display container of all selected

	# playblast
	cmds.playbackOptions( maxTime='10sec')
	cmds.playblast(format="qt", viewer=True, p=100 )



def colourOffsetMesh():
	'''
	Inhabit on object surface with a instance of cubes and make them transfom bases on the surface color
	The surface color is a animated noise texture

	1. create file: force a new file on default location
	2. set perspective view
	3. create object
	4. create Mash network/Repro:  Repro node is used to control various aspects of the meshes created when Geometry Type is set to Mesh during a MASH network's creation. 
	5. Disturube Instances on Surface
	6. offset position, scale, transformation space
	7. add noise shader & animate noise
	8. create color node
	9. create falloff for the color node
	'''

	# 1. new file
	cmds.file(force=True, new=True)

	# 2. move the camera
	cmds.setAttr('persp.translateX', 50)
	cmds.setAttr('persp.translateY', 35)
	cmds.setAttr('persp.translateZ', 50)

	# 3. create a poly cube
	ptorus = cmds.polyTorus(r=20, sr=2, sh=60, sx=400)
	pcube = cmds.polyCube(w=0.4, h=1.0, d=0.4)

	# 4. create a new MASH network
	mashNetwork = mapi.Network()
	mashNetwork.createNetwork(name="OffsetMapNetwork", geometry="Repro") # use Mash Repro node
	
	# 5. Disturube Instances on Surface
	shape = cmds.listRelatives(ptorus[0], s=True)[0] # select Torus object
	mashNetwork.meshDistribute(shape, 4) # Sets the MASH Network distribution method to mesh based. 4 = Face
	cmds.setAttr(mashNetwork.distribute + '.floodMesh', 1) # Flood Mesh Automatically fills the mesh with instances of the object, overriding the Number of Points. 

	# 6. add a World node
	offsetNode = mashNetwork.addNode("MASH_Offset")
	cmds.setAttr(offsetNode.name + '.positionOffsetY', 5)
	cmds.setAttr(offsetNode.name + '.scaleOffset1', 5)
	cmds.setAttr(offsetNode.name + '.transformationSpace', 2)

	# 7. add noise shader & animate noise
	noiseShader = cmds.shadingNode('noise', asTexture=True)
	place2dTexture = cmds.shadingNode('place2dTexture', asUtility=True)
	cmds.connectAttr(place2dTexture+'.outUV', noiseShader+'.uv')
	cmds.connectAttr(noiseShader+'.outColor', offsetNode.name+'.mColour')
	cmds.setAttr(noiseShader + '.noiseType', 2)
	cmds.setKeyframe( noiseShader, attribute='time', t=['0sec'], v=0.0 )
	cmds.setKeyframe( noiseShader, attribute='time', t=['5sec'], v=1.0 )

	# 8. create color node
	colorNode = mashNetwork.addNode("MASH_Color")
	# set Attribute: color, add background/ background color
	cmds.setAttr(colorNode.name + '.color', 0.859,0.31,0.251 , type='double3')
	cmds.setAttr(colorNode.name + '.enableBackgroundColor', 1)
	cmds.setAttr(colorNode.name + '.backgroundColor', 0.239,0.663,0.576 , type='double3')

	# 9. create color/falloff node
	colourFalloff = colorNode.addFalloff()
	cmds.connectAttr(shape+'.worldMesh[0]', colourFalloff+'.shapeIn')
	cmds.setAttr(colourFalloff + '.falloffShape', 6)
	cmds.setAttr(colourFalloff + '.searchRadius', 4)
	cmds.setAttr(colourFalloff + '.innerRadius', 0)

	#tell Maya to finish what it's doing before we continue
	cmds.flushIdleQueue()

	#playblast
	cmds.playbackOptions( animationEndTime='5sec')
	cmds.playblast(format="qt", viewer=True )



def continuousConstrains():
	'''
	Create an instances of cubes, = equal to current tine (basicly emitting cubes)
	When cube are created constrain them to local cubes

	1. create file: force a new file on default location
	2. set perspective view
	3. create object
	4. create Mash network/Instancer:
	5. set number of points equals current time
	6. create Note: dynamics
	7. create node: constain
	'''

	# 1. create
	cmds.file(force=True, new=True)

	# 2. set perspective view
	cmds.setAttr('persp.translateX', 40)
	cmds.setAttr('persp.translateY', 25)
	cmds.setAttr('persp.translateZ', 40)
	cmds.setAttr('persp.rotateX', -30)
	cmds.setAttr('persp.rotateY', 45)

	# 3. create object
	cmds.polyCube()

	# 4. create a new MASH network
	mashNetwork = mapi.Network()
	mashNetwork.createNetwork(name="DymamicsNetwork", geometry="Instancer")

	# set Attribute: arrangement
	cmds.setAttr( mashNetwork.distribute+".arrangement", 9) # 9 = volume
	
	# 5. number of points equals time
	cmds.setKeyframe( mashNetwork.distribute, attribute='pointCount', t=['0sec'], v=0.0 ) 
	cmds.setKeyframe( mashNetwork.distribute, attribute='pointCount', t=['20sec'], v=200.0 )

	# 6. create Note: dynamics
	dynamicsNode = mashNetwork.addNode("MASH_Dynamics")

	# 7. create node: constain
	constraintNode = mashNetwork.addConstraint(dynamicsNode)

	#tell Maya to finish what it's doing before we continue
	cmds.flushIdleQueue()

	#playblast
	cmds.playbackOptions( maxTime='20sec')
	cmds.playblast(format="qt", viewer=True, p=100 )



def curlNoise():
	'''
	create a swarm of cube with a tail behind

	1. create file: force a new file on default location
	2. set perspective view
	3. create object
	4. create Mash network: fills inside with instances
	5. playblast
	6. Signal: animate points with Noise
	7. Trail: moving instances get a trail behind them

	'''

	# 1. new file
	cmds.file(force=True, new=True)

	# 2. move the camera
	cmds.setAttr('persp.translateX', 50)
	cmds.setAttr('persp.translateY', 35)
	cmds.setAttr('persp.translateZ', 50)

	# 3. create a poly cube
	ptorus = cmds.polyTorus(r=20, sr=2, sh=15, sx=100)
	pcube = cmds.polyCube(w=0.1, h=0.1, d=0.1)

	# 4. create a new MASH network
	mashNetwork = mapi.Network()
	mashNetwork.createNetwork("CurlNoiseNetwork")
	shape = cmds.listRelatives(ptorus[0], s=True)[0] # select torus object
	mashNetwork.meshDistribute(shape, 4) # 4=Mesh
	cmds.setAttr(mashNetwork.distribute + '.floodMesh', 1) #  Flood Mesh Automatically fills the mesh with instances of the object, overriding the Number of Points. 

	# 5. playblast
	cmds.playbackOptions( animationEndTime='5sec')

	# 6. create node: Signal
	signalNode = mashNetwork.addNode("MASH_Signal")
	# set attributes
	cmds.setAttr(signalNode.name + '.signalType', 5)
	cmds.setAttr(signalNode.name + '.transformationSpace', 2)
	cmds.setAttr(signalNode.name + '.positionX', 5)
	cmds.setAttr(signalNode.name + '.positionZ', 5)
	cmds.setAttr(signalNode.name + '.timeScale', 3)

	# 7. create node: Trail
	trailsNode = mashNetwork.addNode("MASH_Trails")
	# set Atrribute: trail length
	cmds.setAttr(trailsNode.name + '.maxTrails', 1500)

	# hide object
	cmds.hide(ptorus)
	cmds.setAttr('lambert1.incandescence', 1, 1, 1, type='double3')

	#tell Maya to finish what it's doing before we continue
	cmds.flushIdleQueue()

	#playblast
	cmds.playbackOptions( animationEndTime='5sec')
	cmds.playblast(format="qt", viewer=True, p=100 )



def dynamicChain():
	'''
	create a dynamic chain object

	1. create file: force a new file on default location
	2. set perspective view
	3. create object
	4. create Mash network: fills inside with instances
	5. create node: Dynamics
	6. create node: dynamics/channelRandom
	7. setup a falloff area, where dynamics are active
	'''
	
	# 1. create file
	cmds.file(force=True, new=True)

	# 2. set perspective view
	cmds.setAttr('persp.translateX', 53)
	cmds.setAttr('persp.translateY', 26)
	cmds.setAttr('persp.translateZ', 36)
	cmds.setAttr('persp.rotateX', -30)
	cmds.setAttr('persp.rotateY', 45)

	# 3. create object
	cmds.polyTorus(r=2.5)

	# 4. create a new MASH network
	mashNetwork = mapi.Network()
	mashNetwork.createNetwork(name="DymamicsNetwork", geometry="Instancer")
	# set Attriubtes
	cmds.setAttr( mashNetwork.distribute+".pointCount", 10)
	cmds.setAttr( mashNetwork.distribute+".rotateX", 800)
	cmds.setAttr( mashNetwork.distribute+".amplitudeX", 32)

	# 5. create node: Dynamics
	dynamicsNode = mashNetwork.addNode("MASH_Dynamics")

	# 6. create node: dynamics/channelRandom
	channelRandom = mashNetwork.addChannelRandom(dynamicsNode)
	cmds.setAttr( channelRandom.name+".dynamicsChannelName", 11) # Channel Name: 9=Mass

	# 7 creaete node: dynamics/channelRandom/falloff
	falloff = channelRandom.addFalloff()
	cmds.setAttr( falloff+".falloffShape", 2) # 2=Cube
	cmds.setAttr( falloff+".innerRadius", 1) # inner radius =1
	# set falloff cube area
	falloffParent = cmds.listRelatives(falloff, parent=True)[0]
	cmds.setAttr( falloffParent+".translateX",15.8)
	cmds.setAttr( falloffParent+".scaleX", 15)
	cmds.setAttr( falloffParent+".scaleY", 15)
	cmds.setAttr( falloffParent+".scaleZ", 15)

	# select all bullet type objects
	solver = cmds.ls(type="MASH_BulletSolver")[0]

	#tell Maya to finish what it's doing before we continue
	cmds.flushIdleQueue()

	#playblast
	cmds.playbackOptions( animationEndTime='5sec')
	cmds.playblast(format="qt", viewer=True, p=100 )


def signalColour():
	'''
	create a matrix of cubes, effected by a signal, rotate, scale and color

	1. create file: force a new file on default location
	2. set perspective view
	3. create object
	4. create Mash network: fills inside with instances
	5. create node: signal
	6. create node: Signal/Falloff
	7. create node: colorNode
	'''

	# 1. new file
	cmds.file(force=True, new=True)

	# 2. move the camera
	cmds.setAttr('persp.translateX', 50)
	cmds.setAttr('persp.translateY', 48)
	cmds.setAttr('persp.translateZ', 50)

	# 3. create a poly cube
	pcube = cmds.polyCube(w=1.0, h=1.0, d=1.0)

	# 4. create a new MASH network
	mashNetwork = mapi.Network()
	mashNetwork.createNetwork(name="OffsetMapNetwork", geometry="Repro") # Repro node is used to control various aspects of the meshes created when Geometry Type is set to Mesh during a MASH network's creation. 
	cmds.setAttr(mashNetwork.distribute + '.arrangement', 6) # 6=grid
	cmds.setAttr(mashNetwork.distribute + '.gridAmplitudeX', 30) # set grid size
	cmds.setAttr(mashNetwork.distribute + '.gridAmplitudeY', 30)
	cmds.setAttr(mashNetwork.distribute + '.gridAmplitudeZ', 30)
	cmds.setAttr(mashNetwork.distribute + '.gridx', 30)
	cmds.setAttr(mashNetwork.distribute + '.gridy', 30)
	cmds.setAttr(mashNetwork.distribute + '.gridz', 30)

	# 5. create node: signal
	signalNode = mashNetwork.addNode("MASH_Signal")
	# set attributes
	cmds.setAttr(signalNode.name + '.positionX', 0) # signal transform
	cmds.setAttr(signalNode.name + '.positionY', 0)
	cmds.setAttr(signalNode.name + '.positionZ', 0)
	cmds.setAttr(signalNode.name + '.rotationX', 360)
	cmds.setAttr(signalNode.name + '.rotationY', 360)
	cmds.setAttr(signalNode.name + '.rotationZ', 360)
	cmds.setAttr(signalNode.name + '.scaleX', 5)
	cmds.setAttr(signalNode.name + '.timeScale', 0.2)

	# 6. create node: Signal/Falloff
	signalFalloff = signalNode.addFalloff()
	falloffTransform = cmds.listRelatives( signalFalloff, allParents=True )[0]
	cmds.setAttr(falloffTransform + '.translateX', 15.7)
	cmds.setAttr(falloffTransform + '.translateY', 14)
	cmds.setAttr(falloffTransform + '.scaleX', 25)
	cmds.setAttr(falloffTransform + '.scaleY', 25)
	cmds.setAttr(falloffTransform + '.scaleZ', 25)

	# 7. create node: colorNode
	colorNode = mashNetwork.addNode("MASH_Color")
	cmds.setAttr(colorNode.name + '.color', 1.0,0.188,0.192 , type='double3')
	cmds.setAttr(colorNode.name + '.enableBackgroundColor', 1)
	cmds.setAttr(colorNode.name + '.backgroundColor', 0.086,0.247,0.282 , type='double3')
	cmds.connectAttr(signalFalloff+'.falloffOut', colorNode.name+'.strengthPP[0]')

	colorNodeHotSpot = mashNetwork.addNode("MASH_Color")
	cmds.setAttr(colorNodeHotSpot.name + '.blendMode', 2)
	cmds.setAttr(colorNodeHotSpot.name + '.color', 0.626,0.626,0.238 , type='double3')
	
	# create node: falloff
	hotspotFalloff = colorNodeHotSpot.addFalloff()
	cmds.setAttr(hotspotFalloff + '.innerRadius', 0)
	falloffTransform = cmds.listRelatives( hotspotFalloff, allParents=True )[0]
	cmds.setAttr(falloffTransform + '.translateX', 15.7)
	cmds.setAttr(falloffTransform + '.translateY', 14)
	cmds.setAttr(falloffTransform + '.scaleX', 15)
	cmds.setAttr(falloffTransform + '.scaleY', 15)
	cmds.setAttr(falloffTransform + '.scaleZ', 15)

	#tell Maya to finish what it's doing before we continue
	cmds.flushIdleQueue()

	#playblast
	cmds.playbackOptions( animationEndTime='3sec')
	cmds.playblast(format="qt", viewer=True, p=100 )


def staggerTime():
	'''
	Animate a serie of planes and animed them 

	1. create file: force a new file on default location
	2. set perspective view
	3. create object
	4. create Mash network: fills inside with instances
	5. animation offset components
	'''

	# 1. new file
	cmds.file(force=True, new=True)

	# 2. move the camera
	cmds.setAttr('persp.translateX', 25)
	cmds.setAttr('persp.translateY', 20)
	cmds.setAttr('persp.translateZ', 20)

	# 3. create a poly cube
	pcube = cmds.polyPlane(sx=1, sy=1)
	cmds.setKeyframe( pcube[0], attribute='rotateX', t=['0sec'], v=-180.0 )
	cmds.setKeyframe( pcube[0], attribute='rotateX', t=['0.5sec'], v=0.0 )

	# 4. create a new MASH network
	mashNetwork = mapi.Network()
	mashNetwork.createNetwork(name="TimeNetwork", geometry="Repro")
	cmds.setAttr(mashNetwork.distribute + '.arrangement', 6) # 6=Grid
	cmds.setAttr(mashNetwork.distribute + '.gridAmplitudeX', 30)
	cmds.setAttr(mashNetwork.distribute + '.gridx', 30)
	cmds.setAttr(mashNetwork.distribute + '.gridz', 6)

	# 5. create node: timeNode
	timeNode = mashNetwork.addNode("MASH_Time")
	cmds.setAttr(timeNode.name + '.animationEnd', 1000) #one attribute way to turn off looping
	cmds.setAttr(timeNode.name + '.staggerFrames', 120)
	cmds.setAttr(timeNode.name + '.timeOffset', -120)

	reproMesh = cmds.listConnections(mashNetwork.instancer+'.outMesh', d=True, s=False )[0]

	cmds.flushIdleQueue()

	cmds.select(clear=True)
	cmds.select(reproMesh)
	bendDeformer = cmds.nonLinear( type='bend', curvature=179.5 )[1] #handle
	cmds.setAttr(bendDeformer + '.rotateX', 90)
	cmds.setAttr(bendDeformer + '.rotateY', 90)

	cmds.playbackOptions( animationEndTime='6sec')
	cmds.playblast(format="qt", viewer=True, p=100 )



def worldIgnoreSlope():
	#new file
	cmds.file(force=True, new=True)

	#move the camera
	cmds.setAttr('persp.translateX', 133.600)
	cmds.setAttr('persp.translateY', 97.700)
	cmds.setAttr('persp.translateZ', 133.600)

	#create a poly cube
	ptorus = cmds.polyTorus(r=80, sr=6, sh=15, sx=100)
	pcube = cmds.polyCube(w=0.1, h=2, d=0.1)

	#create a new MASH network
	mashNetwork = mapi.Network()
	mashNetwork.createNetwork("CurlNoiseNetwork")
	shape = cmds.listRelatives(ptorus[0], s=True)[0]
	mashNetwork.meshDistribute(shape, 1)
	cmds.setAttr(mashNetwork.distribute + '.floodMesh', 1)
	cmds.setAttr(mashNetwork.distribute + '.pointCount', 20)

	#add a World node
	node = mashNetwork.addNode("MASH_World")
	#set some attributes on the world node using the .name of the node instance
	cmds.setAttr( node.name+".clusterMode", 7)
	cmds.setAttr( node.name+".sparsity", 0.5)
	cmds.setKeyframe( node.name, attribute='ecosystemAge', t=['0sec'], v=0.0 )
	cmds.setKeyframe( node.name, attribute='ecosystemAge', t=['5sec'], v=120.0 )
	cmds.setAttr( node.name+".ignoreSlope", 1)

	node.addGroundPlane(ptorus[0])

	jsonString = '[{"Slope": 0.6, "colorBar": [255, 255, 255], "Id Min": 0, "Name": "Default Genotype", "Seed Count": 4, "Resiliance": 0.2, "Age": 100, "Soil Quality": 0.5, "Id": 0, "Temperature": 0.5, "Rate": 0.12, "Id Max": 0, "Id Color": [0.0, 0.0, 0.0], "Moisture": 0.5, "Variance": 0.2, "Seed Age": 10, "Size": 1.0}]' #
	cmds.setAttr(node.name + '.genotypeJSON', jsonString, type='string')

	cmds.hide(ptorus[0])
	cmds.flushIdleQueue()

	#playblast
	cmds.playbackOptions( animationEndTime='5sec')
	cmds.playblast(format="qt", viewer=True, p=100 )
