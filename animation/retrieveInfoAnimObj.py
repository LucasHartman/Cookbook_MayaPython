import maya.cmds as cmds

def getAnimationData():
    objs = cmds.ls(selection=True)
    obj = objs[0]
    
    animAttributes = cmds.listAnimatable(obj);

    for attribute in animAttributes:
        
        numKeyframes = cmds.keyframe(attribute, query=True, keyframeCount=True)

        if (numKeyframes > 0):
            print("---------------------------")
            print("Found ", numKeyframes, " keyframes on ", attribute)
            
            times = cmds.keyframe(attribute, query=True, index=(0,numKeyframes),timeChange=True)
            values = cmds.keyframe(attribute, query=True, index=(0,numKeyframes), valueChange=True)
            
            print('frame#, time, value')
            for i in range(0, numKeyframes):
                print(i, times[i], values[i])
            
            print("---------------------------")

getAnimationData()