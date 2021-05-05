'''
Create a list of instance classes
'''

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age


result = []
for x in range(3):
    nameList = ['lulu', 'jim', 'sel', 'jojo']
    ageList = [3,55, 777, 665]
    
    
    temp = Person( nameList[x], ageList[x] )
    result.append(temp)
    
    
print( result[2].name )