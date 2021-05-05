import os
import maya.cmds as cmds

def browseCustomData():
	projDir = cmds.internalVar(userWorkspaceDir=True)    # current project directory
	print('current directory: {}'.format(projDir))


	newDir = os.path.join(projDir, 'customData')  
	print('new directory:     {}'.format(newDir))  

    # create new directory
	if (not os.path.exists(newDir)):        
		os.makedirs(newDir)    
	
	# open directory window
	cmds.fileDialog2(startingDirectory=newDir)


browseCustomData()