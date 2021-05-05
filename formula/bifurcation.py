import maya.cmds as cmds

'''
graph 

horizanal:  r
            r - start value : 0.0
            r -       CHOAS : 3.567
            r - end value   : -

verticle:  x

'''
r = 2.6 # growth rate
x = 0.4 # initial population

for i in range(60):
    x = r*x*(1-x)
    print(x)
