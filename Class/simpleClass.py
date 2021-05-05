import maya.cmds as cmds

class Box():
    
    def __init__(self, name, tx,ty,tz,rx,ry,rz,sx,sy,sz):
           """ instantiates a box object."""
           self.name = name
           self.tx = tx
           self.ty = ty
           self.tz = tz
           self.rx = rx
           self.rx = ry
           self.rx = rz
           self.sx = sx
           self.sy = sy
           self.sz = sz
           
    def createBox(self):
        cmds.polyCube( n=self.name, ch=True )
        cmds.xform( self.name, t=(self.tx,self.ty,self.tz), s=(self.sx, self.sy, self.sz) )


    
class ChildBox(Box):
     # def __init__(self, firstname, lastname): # Override parant init
    pass


# initialize =============================================================

    
# initialize Parent Class                
aBox = Box('lucas', 1,2,3,1,2,3,10,20,30) # class Instance
aBox.createBox() # initialize class.method
del aBox #delete instance

# initialize Child Class
bBox = ChildBox('Isabel', 10,2,3,1,2,3,10,30,10) # class Instance
bBox.createBox() # initialize class.method
del bBox #delete instance