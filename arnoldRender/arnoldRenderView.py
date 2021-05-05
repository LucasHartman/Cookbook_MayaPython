# import libraries (Maya Commands Library and mtoa Core Library)
import maya.cmds as cmds
import mtoa.core as core

# open arnoldRender View
def arnoldOpenMtoARenderView():
    core.createOptions()
    cmds.arnoldRenderView(mode ="open")

# open arnoldRender view and render 
def arnoldMtoARenderView():
    core.createOptions()
    cmds.arnoldRenderView(cam='cameraShape1')

#execute both functions
arnoldOpenMtoARenderView()
arnoldMtoARenderView()