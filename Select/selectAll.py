import maya.cmds as cmds

"""
list all selected objects
"""
#cmds.circle( n='circle1' )
#cmds.sphere( n='sphere1' )


# list all objects
test = cmds.ls( selection=True )
print(test) # [u'time1', u'sequenceManager1', u'hardwareRenderingGlobals', u'renderPartition', 

