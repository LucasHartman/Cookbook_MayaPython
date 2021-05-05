import maya.cmds as cmds

# create object
mySphere = cmds.sphere( name='myObject' )

# add Attribute: name & type
cmds.addAttr(mySphere[0], ln="basename", dataType="string")

# set value
cmds.setAttr('myObject.basename',"ImValue",type="string")

# get value
call = cmds.getAttr('myObject.basename')
print(call)

