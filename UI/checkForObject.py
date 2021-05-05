import pymel.core as pm

class UI(object):
	uiName = 'myUi'

	def __init__(self, *args):
		self.WIN = self.__class__.uiName
		
		# Check if window exists
		if pm.window(self.WIN, exists=True):
			pm.deleteUI(self.WIN)
		
		# Initiate Methods
		#self.helloWorld()
		#self.existChecker()
		cmds.polyCube(n='companionCube') # create test cube
		var = self.getListExistingObjects('companionCube') # check existing items
		print(var)
		
		# Create Window
		self.WIN = pm.window(self.WIN, s=True, title='My UI')
		self.WIN.show()

# Define -------------------------------------------------------------

	def helloWorld(self, *args):
		print('hello world')
	
	def existChecker(self, *args):
		"""
		Check if an object already exists
		"""
		if cmds.objExists('companionCube'):
			print("already there")
		else:
			cmds.polyCube(n='companionCube')


	def getListExistingObjects(self, objectName, *args ):
		"""
		Return a list of objects already existing
		- create a list to append all existing items
		- loop through all existing name values
		- if item exsit append to list
		- else break loop off
		- output list of all existing items
		"""
		checklist = [] # create emty
		# Check first object 
		if cmds.objExists(objectName):
			  print('companionCube  {}'.format("already exists"))
			  checklist.append('companionCube')
		# Check object by name value
		i = 1
		while True:
		  check = '{}{}'.format(objectName,i)
		  # if objectt exists - append
		  if cmds.objExists(check):
			  print('{} {}'.format(check,"already exists"))
			  checklist.append(check)
		  # else, break of loop
		  else:
			  print('{} {}'.format(check,"does not exist"))
			  break
		  i += 1 # update index
		print(checklist)
		return checklist
		
# Initiate -----------------------------------------------------------

UI()