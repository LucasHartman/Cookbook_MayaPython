import maya.cmds as cmds

def listString():

    list = [ 'a', 'b', 'c' ]
    
    listSize = len(list)
    print(listSize)
    
    # list to String
    strList = str(list).replace('[', '').replace(']', '').replace(',', '').replace('\'', '')
    
    item = strList.split()
    print(item[1])



makeFace()
