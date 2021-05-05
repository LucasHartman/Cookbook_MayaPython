import math
print(4**2)

# p1 pos
x1 = 1
y1 = 2
z1 = -5
p1 = (x1,y1,z1)

# p2 pos
x2 = 4
y2 = 6
z2 = 7
p2 = (x2,y2,z2)

#exponent
x = (x2-x1)**2
y = (y2-y1)**2
z = (z2-z1)**2
print(x)
print(y)
print(z)

# distance
d = math.sqrt(x + y + z)
print (d)

#-------------------------------

def pointsDistance(x1, y1, z1, x2, y2, z2):
    d = math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
    print('distance between point a and b = {}'.format(d))
    return d
    
result = pointsDistance(1, 2, -5, 4, 6, 7)