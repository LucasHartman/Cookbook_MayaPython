import maya.cmds as cmds

class myVertex():

    def MoveVertex(self):
        """ move vertex position of a object """
        cmds.polyCube( n="pCube1", ch=True )
        cmds.setAttr('pCube1.pnts[3].pntx', 5.0)        
    
    def SelectComp(self):
        """ select vertex, edges, or faces"""
        #cmds.polyCube( n="pCube1", ch=True )
        #cmds.select('pCube1.vtx[2]')                    # selected vertices 
        #cmds.select('pCube1.f[2]')                      # select faces
        #cmds.select('pCube1.e[2]')                      # select edges
        #cmds.select('pCube1.vtx[0:2]')                  # vertex select inbetween
        #cmds.select(clear=True)                         # deselect
        my_faces = ['pCube1.vtx[1]', 'pCube1.vtx[2]']    # selection to list
        cmds.select(my_faces)

    def NumberOfVertex(self):
        """Get the number of vertecies of an object"""
        cmds.polyPlane( n='plg', sx=4, sy=4, w=5, h=5 )
        nof = cmds.polyEvaluate( v=True ) # query the number of vertecis
        print(nof)
        
        
# initialize =============================================================        
call = myVertex()
call.MoveVertex()
call.SelectComp()
call.NumberOfVertex()