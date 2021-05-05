import maya.cmds as cmds

class Main(object):
	def __init__(self):
		
		cmds.window()
		cmds.columnLayout()

		# input int
		self.num = cmds.intField(changeCommand = 'callback()') 		
		# input text
		self.txt = cmds.textField (tx= "Replace me", editable= True )
		# input checkbox
		self.checker = cmds.checkBox( label='One', editable= True )
		
		cmds.button( label='Button 1', command= self.myFunction )
		cmds.showWindow()

	# retrieve intField data		
	def callback_int(self):
		number = cmds.intField(self.num, q=1, v=1)
		return number
		
    # retrieve textField data	
	def callback_text(self):
		txt = cmds.textField(self.txt,  q=True,text=True)
		return txt

    # retrieve checkField data	
	def callback_check(self):
		check = cmds.checkBox(self.checker,  q=True, v=1)
		return check
		
			
	# use field data in a function
	def myFunction(self, args):
		getInt = self.callback_int()
		gettext = self.callback_text()
		getCheck = self.callback_check()
		print(getInt)
		print(gettext)
		print(getCheck)

Main()