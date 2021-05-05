import maya.cmds as cmds
import os

myFolder = "C:/Users/12213119/Documents/maya/2020/scripts/Lab/mesh/"
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