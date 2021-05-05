import maya.OpenMaya as om
import maya.cmds as mc
  
def snapToClosest():
  selObj = om.MSelectionList()
  # Store active selection
  om.MGlobal.getActiveSelectionList(selObj)
  if selObj.length() < 2:
	  mc.warning("Select geo and then locator")
	  return
  locDag = om.MDagPath()
  meshDag = om.MDagPath()
  # extract dag paths, assuming the first selected is the mesh
  # and the second is the locator
  selObj.getDagPath(0, meshDag)
  selObj.getDagPath(1, locDag)
  locName = locDag.fullPathName()
  # get the locator position
  locT = om.MFnTransform( locDag.transform() )
  locPt = om.MPoint( locT.getTranslation(om.MSpace.kPostTransform) )
  
  # find the closest vertex
  vtxIt = om.MItMeshVertex(meshDag)
  mindist = 10000
  closestPt = om.MPoint()
  vtxId = -1
  while not vtxIt.isDone():
	  vtxPt = vtxIt.position( om.MSpace.kWorld)
	  dist = vtxPt.distanceTo(locPt)
	  if dist < mindist:
		  mindist = dist
		  closestPt = vtxPt
		  vtxId = vtxIt.index()
	  vtxIt.next()
  print "Closest vtx: %d at %f" % (vtxId, mindist)
  mc.xform(locName, t=[closestPt.x, closestPt.y, closestPt.z], ws=1, a=1)

snapToClosest()