import maya.cmds as cmds
import operator

def objsDistance(object):
    """
    input an object and compare distance between all object in the scene
    output the name of the closed object
    """
  p1 = cmds.objectCenter(object, gl=True) # get position
  allObj = cmds.ls(type='surfaceShape') # get all scene objects
  disList = []
  disDict = {}
  for obj in allObj:
	  p2 = cmds.objectCenter( obj.replace('Shape','') ,gl=True) # get position
	  d = float("{:.2f}".format(math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2+(p2[2]-p1[2])**2)))
	  print('distance {} to {}: {}'.format(object, obj, d))
	  disList.append(d) # add to list
	  disDict['{}'.format(obj.replace('Shape',''))] = d # add to dictionary
  disList.sort() # sort list
  disList.pop(0) # remove first item from list
  print( 'distance Dictionary: {}'.format( sorted(disDict.items(), key=operator.itemgetter(1)) )) # sort dictionary
  print( 'distance List:       {}'.format(disList))
  
  key_list = list(disDict.keys())
  val_list = list(disDict.values())
  position = val_list.index(disList[0]) # get index from value
  print('{} is closed object to {}'.format(key_list[position], object))
  
  return key_list[position]


getnearest = objsDistance('pTorus1')
