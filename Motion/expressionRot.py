import maya.cmds as cmds

#mySphere = cmds.sphere(n='mySphere')

def createExpression(att, speed):
	"""
	create a expresion: obj.attr(time * obj.speed)
	- create a custom speed atribute
	- Create the expression
	- run script when item is seleced
	"""

	# get selected object
	objs = cmds.ls(selection=True)
	obj = objs[0]

	# create Attr: Speed
	cmds.addAttr(obj, longName="speed", shortName="speed", min=0, keyable=True)

	# set expresion items
	baseString = "{0}.{1} = ".format(obj, att) # object.attribute as string
	valueClause = '(time * '+ obj + '.speed)'
	
	# set expression
	expressionString = baseString + valueClause
	cmds.expression(string=expressionString)

createExpression('rotateY', 10)