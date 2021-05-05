import maya.cmds as cmds

class myCreate():
    
    def createCube(self):
        """ create a polyCube"""
        myCube = cmds.polyCube( n="pCube1", ch=True )
        cmds.xform( myCube[0], r=True, t=(5,0,0), s=(10,10,10), ro=(30,30,30) )      # Transform cube

    def createInstance(self):
        myCube = cmds.polyCube( n="pCube1", ch=True )
        instCube = mc.instance( myCube[0] )                                        # Instance Box
        cmds.move( 0,0,-20, instCube[0] )                                            # move Instance

# initialize =============================================================        
call = myCreate()
call.createCube()
call.createInstance()