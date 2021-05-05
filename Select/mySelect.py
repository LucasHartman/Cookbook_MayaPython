import maya.cmds as cmds

class mySelect():
    
    def SelectEdges(self):
        """ Select edges of a poly object """
        cmds.polyCube( n="pCube1", ch=False )
        cmds.polySelect( 'pCube1', edgeRing=1 )
        cmds.polySelect( 'pCube1', toggle=True, edgeRingPath=(0, 1) )

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


# initialize =============================================================        
call = mySelect()
call.SelectEdges()
call.SelectComp()