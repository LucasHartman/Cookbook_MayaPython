import maya.cmds as cmds

#mySphere = cmds.sphere(n='mySphere')

def createExpression(att, minVal, maxVal, speed):
	"""
	create a expresion for wave animation
	- animate objects attribute using a wave Function
	- create a custom speed atribute
	- Calculate values for the wave fuction:
		speed      = wave to strech or shrink alnog the horizantal
		multiplier = overal range (min/max, or top/down wave)
		offset     =  min/max values are where they should be.
		we move the 0 position of the wave to be
		midway between our minVal and maxVal
	- Create the expression
	- run script when item is seleced
	
	"""
	# get selected object
	objs = cmds.ls(selection=True)
	obj = objs[0]

	# create Attr: Speed
	cmds.addAttr(obj, longName="speed", shortName="speed", min=0, keyable=True)
	
	amplitude = (maxVal - minVal)/2.0 # multiplier
	offset = minVal + amplitude # offset
	
	# set expresion items
	baseString = "{0}.{1} = ".format(obj, att) # object.attribute as string
	sineClause = '(sin(time * '+ obj + '.speed)' # sin Function as a string
	valueClause = ' * ' + str(amplitude) + ' + ' + str(offset) + ')'
	# set expression
	expressionString = baseString + sineClause + valueClause
	cmds.expression(string=expressionString)

createExpression('translateY', 5, 10, 1)