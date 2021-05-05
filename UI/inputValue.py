import maya.cmds as cmds


# 2. gettting input from field correctly
def callback():
    number = cmds.intField(num, q=1, v=1)
    #print(number)
    return number


# 0. setup window
cmds.window()
cmds.columnLayout()
# 1./3. input Field, seen in the window, getting the value from callback function
num = cmds.intField(changeCommand = 'callback()') 
cmds.button( label='Button 1', command=myFunction )
cmds.showWindow()


# 4. function getting the input field data
def myFunction(args):
    getInt = callback()
    print(getInt)