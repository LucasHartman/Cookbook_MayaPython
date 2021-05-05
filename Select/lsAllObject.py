import maya.cmds as cmds

def findAll():
  allObjects = cmds.ls(type='surfaceShape')
  for obj in allObjects:
      print obj.replace('Shape','')
      
       
findAll()