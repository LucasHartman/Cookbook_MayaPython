import maya.cmds as cmds

"""
list all object and their type
"""
#cmds.circle( n='circle1' )
cmds.sphere( n='sphere1' )


# list all objects
test = cmds.ls( type='geometryShape', showType=True )
print(test) # 

