simport maya.cmds as cmds

"""
Namespace Window:        Window > General Editors > Namespace 

1. Create namespace
2. set namespace
3. create items with namespace
4. set namespace back to the root
5. select and add selected to ls
6. deselect selected
7. remove Shape String
8. get from ls object name


"""

# Create  namespace
cmds.namespace( add='Lulu' )

#Set the current namespace to Lulu
cmds.namespace( set='Lulu' )

# Create objects
cmds.sphere( n='sphere1' )
cmds.sphere( n='sphere2' )

# set current namaespace back to the root
cmds.namespace( set=':' )

# select all with namespace
sel = cmds.select( 'Lulu:*' )
objects = cmds.ls(sl=True, g=True)

# Deselect all selected
cmds.select( clear=True )

# print values
print ('print all ls value: {}'.format(objects))
print ('print first ls value: {}'.format(objects[0].replace("Shape", "")))

# move object from ls
cmds.setAttr( '{}.translateX'.format(objects[0].replace("Shape", "")), 5 )

