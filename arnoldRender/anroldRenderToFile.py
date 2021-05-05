from mtoa.cmds.arnoldRender import arnoldRender
import maya.cmds as cmds
import mtoa.aovs as aovs
import pymel.core as pm

#declare target render dir
render_dir= r'C:\Users\12213119\Documents\temp'

#define workspace file rule for images
pm.workspace(fileRule=['images',render_dir])



# ---------------------------------------------------------
# Render Image
# ---------------------------------------------------------

# Set AOVs
aovs.AOVInterface().addAOV('beauty' )
aovs.AOVInterface().addAOV('specular' )
aovs.AOVInterface().addAOV('N' )

# Set Sampeling
cmds.setAttr("defaultArnoldRenderOptions.AASamples", 1)              # set Camera Sample
cmds.setAttr("defaultArnoldRenderOptions.GIDiffuseSamples", 1)       # set Diffuse Sample
cmds.setAttr("defaultArnoldRenderOptions.GISpecularSamples", 1)      # set Specular Sample
cmds.setAttr("defaultArnoldRenderOptions.GITransmissionSamples", 1)  # set Trasmission
cmds.setAttr("defaultArnoldRenderOptions.GISssSamples", 1)           # set SSS
cmds.setAttr("defaultArnoldRenderOptions.GIVolumeSamples", 1)        # set Volume Indirect

# Set File
cmds.setAttr("defaultArnoldDriver.ai_translator", "png", type="string")    # set file type
cmds.setAttr("defaultArnoldDriver.pre", "cam1_rnd1", type="string")        # set file name

# Set Render
arnoldRender(1920, 1080, True, True,'camera1', ' -layer defaultRenderLayer')
#arnoldRender(width, height, doShadows, doGlowPass, camera, options)
