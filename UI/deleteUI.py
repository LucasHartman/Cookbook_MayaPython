import pymel.core as pm
class UI(object):
	uiName = 'myUi'

	def __init__(self, *args):
		self.WIN = self.__class__.uiName
		if pm.window(self.WIN, exists=True):
			pm.deleteUI(self.WIN)

		self.WIN = pm.window(self.WIN, s=True, title='My UI')
		self.WIN.show()

UI()