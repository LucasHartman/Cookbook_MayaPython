import maya.cmds as cmds

# set: Render Settings/Common/FrameAnimation ext: name#.ext


camera_list = {'cameraShape1':[1,2], 'cameraShape2':[3,4], 'cameraShape3':[5,6]}

for cam, frames in camera_list.items():
    print cam, "{}..{}".format(*frames)
    
    #cmds.arnoldRender(b=True, cam=cam, seq="{}..{}".format(*frames))
    cmds.arnoldRender(b=True, cam=cam, seq="{}..{}".format(*frames))