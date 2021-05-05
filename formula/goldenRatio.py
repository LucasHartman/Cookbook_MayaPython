import maya.cmds as cmds


x = 1
y = 1
z = 0
for i in range(100):
    z = y
    y = x + y
    x = z
    print(y)