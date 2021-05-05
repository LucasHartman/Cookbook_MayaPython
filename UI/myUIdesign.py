from pymel.core import *

"""
Source Learn:
https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=__PyMel_ui_html

Source Layout:
https://help.autodesk.com/cloudhelp/2017/ENU/Maya-Tech-Docs/PyMel/generated/functions/pymel.core.windows/pymel.core.windows.layout.html    

pymel recomandations:
	pymel.core.windows.dimWhen                create objects , select/deselect all, delete, all in one menu
	pymel.core.windows.defaultNavigation      create object, choose a Render note, like 2d/3d texture
	pymel.core.windows.headsUpMessage         create a message in the viewport
	pymel.core.windows.image                  show image
	pymel.core.windows.tabLayout              create tabs
	pymel.core.windows.toolBar                creaete custom toolbar    
"""

# delcare Method
def myWindow():
	# Instance Object: Window
	with window() as win:
		# Layer 1: top
		with columnLayout(adjustableColumn=True):
			with verticalLayout():
				text( label='Layer 01', align='left' )
				btn1 = button(label='print', command = lambda *args: buttonPressed('chad') )               # print
				btn2 = button(label='create cube', command = lambda *args: cmds.polyCube( n='plg' ) )      # create
				
		# Layer 2
		with columnLayout(adjustableColumn=True):
			with horizontalLayout():
				text( label='Layer 02', align='left' )
				button(label='sub2H1')
				button(label='sub2H2')
		# Layer 3: Bottum
		with columnLayout(adjustableColumn=True):
			with verticalLayout():
				text( label='Layer 03', align='left' )
				button(label='sub4H1')
				button(label='sub4H2')
		# Layer 4
		with columnLayout(adjustableColumn=True):
			with horizontalLayout():
				text( label='Layer 04', align='left' )
				nameField()
		# Layer 5
		with columnLayout(adjustableColumn=True):
			with horizontalLayout():
				text( label='Layer 05', align='left' )               
				intSlider( min=-100, max=100, value=0, step=1 )
		# Layer 6
		with columnLayout(adjustableColumn=True):
				text( label='Layer 06: get object attribute', align='left' )    
				object = sphere() # create object
				move(object[0], 1,5,9)
				attrFieldGrp( attribute='%s.translate' % object[0] )
		# Layer 7
		with columnLayout(adjustableColumn=True):
				text( label='Layer 07: set object attribute', align='left' )    
				object = sphere() # create object
				attrFieldSliderGrp( min=-10.0, max=10.0, at='%s.ty' % object[0] )
		# Layer 8
		with columnLayout(adjustableColumn=True):
				text( label='Layer 08: get Render Note', align='left' )    
				#newNode = shadingNode( 'blinn', asShader=True )
				#newNodeAttr = newNode + '.normalCamera'
				#pm.attrNavigationControlGrp( l='bump mapping', at=newNodeAttr )
		# Layer 9
		with columnLayout(adjustableColumn=True):
			with horizontalLayout():
				text( label='Layer 09', align='left' )    
				checkBox( label='One' )
				checkBox( label='Two' )
		# Layer 10
		with columnLayout(adjustableColumn=True):        
			text( label='Layer 10', align='left' )    
			clipSchedulerOutliner( 'myOutliner', clipScheduler='charScheduler1',height=60 )
		# Layer 11
		with columnLayout(adjustableColumn=True):        
			text( label='Layer 11: code editor', align='left' )
			cmdScrollFieldExecuter(width=100, height=60)
		# Layer 12
		with columnLayout(adjustableColumn=True):        
			text( label='Layer 12', align='left' )
			cmdScrollFieldReporter(width=100, height=60)
		# Layer 13
		with columnLayout(adjustableColumn=True):        
			text( label='Layer 13', align='left' )       
			colorIndexSliderGrp( label='Select Color', min=0, max=20, value=10 )
			colorSliderGrp( label='Blue', rgb=(0, 0, 1) )
		# Layer 14
		with columnLayout(adjustableColumn=True):        
			text( label='Layer 14: HUD message', align='left') 
			pm.headsUpMessage( 'Ouch!' )
			#pm.headsUpMessage( 'This is Circle 1', object='circle1' )
			#pm.headsUpMessage( 'These objects are selectedp', selection=True )
			#pm.headsUpMessage( 'Text appears for minimum of 5 seconds.', time=5.0 )
			#pm.headsUpMessage( 'Text appears 0 pixels above point.', verticalOffset=20 )
			#pm.headsUpMessage( 'Text appears 20 pixels to the left of the point.', horizontalOffset=-100 )
		# Layer 15
		with columnLayout(adjustableColumn=True):        
			text( label='Layer 15: scroll list', align='left') 
			iconTextScrollList(allowMultiSelection=True, append=('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen'), selectItem='six' )
		# Layer 16
		with columnLayout(adjustableColumn=True):        
			text( label='Layer 16: int int only', align='left')
			intField( minValue=-1000, maxValue=1000, step=10 )
		# Layer 17
		with columnLayout(adjustableColumn=True):        
			text( label='Layer 17', align='left')           
			radioButtonGrp( label='Three Buttons', labelArray3=['One', 'Two', 'Three'], numberOfRadioButtons=3 )
		# Layer 18
		with columnLayout(adjustableColumn=True):        
			text( label='Layer 18: seperators', align='left')
			separator()    
			separator( style='single' )  
			separator( height=10, style='double' )
		# Layer 19
		with columnLayout(adjustableColumn=True):        
			text( label='Layer 19: text,field,button', align='left')            
			textFieldButtonGrp( label='Label', text='Text', buttonLabel='Button' )

					   
myWindow()