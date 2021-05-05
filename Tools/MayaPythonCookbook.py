import sys
import maya.cmds as cmds
"""
------------------------------------------------------------------------
Maya script editor: load external file

#apply root to maya import list
sys.path.append('c:/Users/12213119/Documents/maya/2020/scripts/Lab/')

# print list of system directories
from pprint import pprint
sys.path
pprint(sys.path)


# import file to script editor
import File
reload(File)
File.class()
"""

def showUI():  
	myWin = cmds.window(title="Simple Window", widthHeight=(300, 200))
	cmds.columnLayout()    
	cmds.text(label="Hello, Maya!")
	cmds.showWindow(myWin)

showUI()