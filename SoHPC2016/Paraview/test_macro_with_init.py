#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'NetCDF Reader'
ave20140926120000_notimenc = NetCDFReader(FileName=['/pico/scratch/userexternal/plazzari/xVISUALIZZAZIONE3d/ave.20140926-12:00:00_notime.nc'])
ave20140926120000_notimenc.Dimensions = '(depth, lat, lon)'

# Properties modified on ave20140926120000_notimenc
ave20140926120000_notimenc.VerticalScale = -100.0
ave20140926120000_notimenc.VerticalBias = 6000000.0

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [695, 601]

# show data in view
ave20140926120000_notimencDisplay = Show(ave20140926120000_notimenc, renderView1)
# trace defaults for the display properties.
ave20140926120000_notimencDisplay.Representation = 'Outline'
ave20140926120000_notimencDisplay.ColorArrayName = [None, '']
ave20140926120000_notimencDisplay.ScalarOpacityUnitDistance = 19864.29158272848

# reset view to fit data
renderView1.ResetCamera()

# create a new 'Clip'
clip1 = Clip(Input=ave20140926120000_notimenc)
clip1.ClipType = 'Plane'
clip1.Scalars = ['CELLS', 'N1p']
clip1.Value = 5.000000100204387e+19

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [4125921.189686847, 1136868.1970353876, 3530320.1977314623]

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=clip1)

# Properties modified on clip1
clip1.ClipType = 'Scalar'
clip1.Value = 1.0
clip1.InsideOut = 1

# show data in view
clip1Display = Show(clip1, renderView1)
# trace defaults for the display properties.
clip1Display.ColorArrayName = [None, '']
clip1Display.ScalarOpacityUnitDistance = 28120.580147046414

# set active source
SetActiveSource(ave20140926120000_notimenc)

# set active source
SetActiveSource(clip1)

# set scalar coloring
ColorBy(clip1Display, ('CELLS', 'N1p'))

# rescale color and/or opacity maps used to include current data range
clip1Display.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'N1p'
n1pLUT = GetColorTransferFunction('N1p')
n1pLUT.RGBPoints = [1.9657159100461286e-06, 0.231373, 0.298039, 0.752941, 0.49964418945432953, 0.865003, 0.865003, 0.865003, 0.999286413192749, 0.705882, 0.0156863, 0.14902]
n1pLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'N1p'
n1pPWF = GetOpacityTransferFunction('N1p')
n1pPWF.Points = [1.9657159100461286e-06, 0.0, 0.5, 0.0, 0.999286413192749, 1.0, 0.5, 0.0]
n1pPWF.ScalarRangeInitialized = 1

# create a new 'Clip'
clip2 = Clip(Input=clip1)
clip2.ClipType = 'Plane'
clip2.Scalars = ['CELLS', 'N1p']
clip2.Value = 0.49964418945432953

# init the 'Plane' selected for 'ClipType'
clip2.ClipType.Origin = [4416257.145620574, 1067446.0006137078, 3652749.4309997726]

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip2)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=clip2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip2)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=clip2)

# Properties modified on clip2
clip2.ClipType = 'Box'

# Properties modified on clip2.ClipType
clip2.ClipType.Bounds = [3860942.887098376, 4971571.404142772, -767845.1390752384, 2902737.140302654, 3002818.1443427694, 4302680.717656776]
clip2.ClipType.Position = [0.0, 196796.9029041141, 0.0]
clip2.ClipType.Scale = [1.0, 0.91717496890289, 1.0]

# show data in view
clip2Display = Show(clip2, renderView1)
# trace defaults for the display properties.
clip2Display.ColorArrayName = ['CELLS', 'N1p']
clip2Display.LookupTable = n1pLUT
clip2Display.ScalarOpacityUnitDistance = 85681.76185924826

# hide data in view
Hide(clip1, renderView1)

# show color bar/color legend
clip2Display.SetScalarBarVisibility(renderView1, True)

# Properties modified on clip2.ClipType
clip2.ClipType.Position = [0.0, 217811.61108359194, 0.0]
clip2.ClipType.Scale = [1.0, 0.9445433887964956, 1.0]

# Properties modified on clip2
clip2.InsideOut = 1

# hide data in view
Hide(ave20140926120000_notimenc, renderView1)

# hide color bar/color legend
clip2Display.SetScalarBarVisibility(renderView1, False)

# show color bar/color legend
clip2Display.SetScalarBarVisibility(renderView1, True)

# rescale color and/or opacity maps used to exactly fit the current data range
clip2Display.RescaleTransferFunctionToDataRange(False)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip2)

# Properties modified on n1pPWF
n1pPWF.Points = [1.9657159100461286e-06, 0.0, 0.5, 0.0, 0.1614808887243271, 0.261904776096344, 0.5, 0.0, 0.6212472915649414, 1.0, 0.5, 0.0]

# Properties modified on n1pPWF
n1pPWF.Points = [1.9657159100461286e-06, 0.0, 0.5, 0.0, 0.15699537098407745, 0.2777777910232544, 0.5, 0.0, 0.6212472915649414, 1.0, 0.5, 0.0]

# Properties modified on n1pPWF
n1pPWF.Points = [1.9657159100461286e-06, 0.0, 0.5, 0.0, 0.13008220493793488, 0.5158730745315552, 0.5, 0.0, 0.6212472915649414, 1.0, 0.5, 0.0]

# Properties modified on n1pPWF
n1pPWF.Points = [1.9657159100461286e-06, 0.0, 0.5, 0.0, 0.10765458643436432, 0.7619048357009888, 0.5, 0.0, 0.6212472915649414, 1.0, 0.5, 0.0]

# Properties modified on n1pPWF
n1pPWF.Points = [1.9657159100461286e-06, 0.0, 0.5, 0.0, 0.10765458643436432, 0.8174603581428528, 0.5, 0.0, 0.6212472915649414, 1.0, 0.5, 0.0]

# Properties modified on n1pPWF
n1pPWF.Points = [1.9657159100461286e-06, 0.0, 0.5, 0.0, 0.07177037745714188, 0.8571429252624512, 0.5, 0.0, 0.6212472915649414, 1.0, 0.5, 0.0]

# Properties modified on n1pPWF
n1pPWF.Points = [1.9657159100461286e-06, 0.0, 0.5, 0.0, 0.0762559026479721, 0.7777778506278992, 0.5, 0.0, 0.6212472915649414, 1.0, 0.5, 0.0]

# Properties modified on n1pPWF
n1pPWF.Points = [1.9657159100461286e-06, 0.0, 0.5, 0.0, 0.0762559026479721, 0.7777778506278992, 0.5, 0.0, 0.46649664640426636, 0.9206349849700928, 0.5, 0.0, 0.6212472915649414, 1.0, 0.5, 0.0]

# Properties modified on n1pPWF
n1pPWF.Points = [1.9657159100461286e-06, 0.0, 0.5, 0.0, 0.0762559026479721, 0.7777778506278992, 0.5, 0.0, 0.46425387263298035, 0.8968254327774048, 0.5, 0.0, 0.6212472915649414, 1.0, 0.5, 0.0]

# Properties modified on n1pPWF
n1pPWF.Points = [1.9657159100461286e-06, 0.0, 0.5, 0.0, 0.0762559026479721, 0.7777778506278992, 0.5, 0.0, 0.4171558618545532, 0.5634921193122864, 0.5, 0.0, 0.6212472915649414, 1.0, 0.5, 0.0]

# Properties modified on n1pPWF
n1pPWF.Points = [1.9657159100461286e-06, 0.0, 0.5, 0.0, 0.0762559026479721, 0.7777778506278992, 0.5, 0.0, 0.4171558618545532, 0.5793651342391968, 0.5, 0.0, 0.6212472915649414, 1.0, 0.5, 0.0]

# Properties modified on n1pPWF
n1pPWF.Points = [1.9657159100461286e-06, 0.0, 0.5, 0.0, 0.0762559026479721, 0.7777778506278992, 0.5, 0.0, 0.37902888655662537, 0.2460317611694336, 0.5, 0.0, 0.6212472915649414, 1.0, 0.5, 0.0]

# Properties modified on n1pPWF
n1pPWF.Points = [1.9657159100461286e-06, 0.0, 0.5, 0.0, 0.0762559026479721, 0.7777778506278992, 0.5, 0.0, 0.3364163935184479, 0.0476190522313118, 0.5, 0.0, 0.6212472915649414, 1.0, 0.5, 0.0]

# Properties modified on n1pPWF
n1pPWF.Points = [1.9657159100461286e-06, 0.0, 0.5, 0.0, 0.0762559026479721, 0.7777778506278992, 0.5, 0.0, 0.3274453282356262, 0.0634920671582222, 0.5, 0.0, 0.6212472915649414, 1.0, 0.5, 0.0]

# Properties modified on n1pPWF
n1pPWF.Points = [1.9657159100461286e-06, 0.0, 0.5, 0.0, 0.0762559026479721, 0.7777778506278992, 0.5, 0.0, 0.3139887750148773, 0.2063492238521576, 0.5, 0.0, 0.6212472915649414, 1.0, 0.5, 0.0]

# Properties modified on n1pPWF
n1pPWF.Points = [1.9657159100461286e-06, 0.0, 0.5, 0.0, 0.0762559026479721, 0.7777778506278992, 0.5, 0.0, 0.3095032274723053, 0.2301587462425232, 0.5, 0.0, 0.6212472915649414, 1.0, 0.5, 0.0]

# Properties modified on n1pPWF
n1pPWF.Points = [1.9657159100461286e-06, 0.0, 0.5, 0.0, 0.0762559026479721, 0.7777778506278992, 0.5, 0.0, 0.2242782562971115, 0.2301587462425232, 0.5, 0.0, 0.6212472915649414, 1.0, 0.5, 0.0]

# Properties modified on n1pPWF
n1pPWF.Points = [1.9657159100461286e-06, 0.0, 0.5, 0.0, 0.0762559026479721, 0.7777778506278992, 0.5, 0.0, 0.2220354825258255, 0.2301587462425232, 0.5, 0.0, 0.6212472915649414, 1.0, 0.5, 0.0]

# Properties modified on n1pPWF
n1pPWF.Points = [1.9657159100461286e-06, 0.0, 0.5, 0.0, 0.0762559026479721, 0.7777778506278992, 0.5, 0.0, 0.2220354825258255, 0.2142857313156128, 0.5, 0.0, 0.6212472915649414, 1.0, 0.5, 0.0]

# Properties modified on n1pLUT
n1pLUT.RGBPoints = [1.9657159100461286e-06, 0.231373, 0.298039, 0.752941, 0.29828941822052, 0.865003, 0.865003, 0.865003, 0.6212472915649414, 0.705882, 0.0156863, 0.14902]

# Properties modified on n1pLUT
n1pLUT.RGBPoints = [1.9657159100461286e-06, 0.231373, 0.298039, 0.752941, 0.25791969895362854, 0.865003, 0.865003, 0.865003, 0.6212472915649414, 0.705882, 0.0156863, 0.14902]

# Properties modified on n1pLUT
n1pLUT.RGBPoints = [1.9657159100461286e-06, 0.231373, 0.298039, 0.752941, 0.19960786402225494, 0.865003, 0.865003, 0.865003, 0.6212472915649414, 0.705882, 0.0156863, 0.14902]

# Properties modified on n1pLUT
n1pLUT.RGBPoints = [1.9657159100461286e-06, 0.231373, 0.298039, 0.752941, 0.18166576325893402, 0.865003, 0.865003, 0.865003, 0.6212472915649414, 0.705882, 0.0156863, 0.14902]

# Properties modified on n1pLUT
n1pLUT.RGBPoints = [1.9657159100461286e-06, 0.231373, 0.298039, 0.752941, 0.1771802306175232, 0.865003, 0.865003, 0.865003, 0.6212472915649414, 0.705882, 0.0156863, 0.14902]

# Properties modified on n1pLUT
n1pLUT.RGBPoints = [1.9657159100461286e-06, 0.231373, 0.298039, 0.752941, 0.16596642136573792, 0.865003, 0.865003, 0.865003, 0.6212472915649414, 0.705882, 0.0156863, 0.14902]

# Properties modified on n1pLUT
n1pLUT.RGBPoints = [1.9657159100461286e-06, 0.231373, 0.298039, 0.752941, 0.15699537098407745, 0.865003, 0.865003, 0.865003, 0.6212472915649414, 0.705882, 0.0156863, 0.14902]

# Properties modified on n1pLUT
n1pLUT.RGBPoints = [1.9657159100461286e-06, 0.231373, 0.298039, 0.752941, 0.18166576325893402, 0.865003, 0.865003, 0.865003, 0.6212472915649414, 0.705882, 0.0156863, 0.14902]

# Properties modified on n1pLUT
n1pLUT.RGBPoints = [1.9657159100461286e-06, 0.231373, 0.298039, 0.752941, 0.21530720591545105, 0.865003, 0.865003, 0.865003, 0.6212472915649414, 0.705882, 0.0156863, 0.14902]

# Properties modified on n1pLUT
n1pLUT.RGBPoints = [1.9657159100461286e-06, 0.231373, 0.298039, 0.752941, 0.2242782562971115, 0.865003, 0.865003, 0.865003, 0.6212472915649414, 0.705882, 0.0156863, 0.14902]

# Properties modified on n1pLUT
n1pLUT.RGBPoints = [1.9657159100461286e-06, 0.231373, 0.298039, 0.752941, 0.2377348244190216, 0.865003, 0.865003, 0.865003, 0.6212472915649414, 0.705882, 0.0156863, 0.14902]

# convert to log space
n1pLUT.MapControlPointsToLogSpace()

# Properties modified on n1pLUT
n1pLUT.UseLogScale = 1

# Properties modified on n1pLUT
n1pLUT.RGBPoints = [1.9657159100461294e-06, 0.231373, 0.298039, 0.752941, 0.0001901024952530861, 0.865003, 0.865003, 0.865003, 0.6212472915649417, 0.705882, 0.0156863, 0.14902]

# Properties modified on n1pLUT
n1pLUT.RGBPoints = [1.9657159100461294e-06, 0.231373, 0.298039, 0.752941, 7.618936069775373e-05, 0.865003, 0.865003, 0.865003, 0.6212472915649417, 0.705882, 0.0156863, 0.14902]

# Properties modified on n1pLUT
n1pLUT.RGBPoints = [1.9657159100461294e-06, 0.231373, 0.298039, 0.752941, 4.90471938974224e-06, 0.865003, 0.865003, 0.865003, 0.6212472915649417, 0.705882, 0.0156863, 0.14902]

# Properties modified on n1pLUT
n1pLUT.RGBPoints = [1.9657159100461294e-06, 0.231373, 0.298039, 0.752941, 3.3458789403084666e-05, 0.865003, 0.865003, 0.865003, 0.6212472915649417, 0.705882, 0.0156863, 0.14902]

# Properties modified on n1pLUT
n1pLUT.RGBPoints = [1.9657159100461294e-06, 0.231373, 0.298039, 0.752941, 0.00027404705178923905, 0.865003, 0.865003, 0.865003, 0.6212472915649417, 0.705882, 0.0156863, 0.14902]

# Properties modified on n1pLUT
n1pLUT.RGBPoints = [1.9657159100461294e-06, 0.231373, 0.298039, 0.752941, 0.0006240354268811643, 0.865003, 0.865003, 0.865003, 0.6212472915649417, 0.705882, 0.0156863, 0.14902]

# Properties modified on n1pLUT
n1pLUT.RGBPoints = [1.9657159100461294e-06, 0.231373, 0.298039, 0.752941, 0.002574564889073372, 0.865003, 0.865003, 0.865003, 0.6212472915649417, 0.705882, 0.0156863, 0.14902]

# Properties modified on n1pLUT
n1pLUT.RGBPoints = [1.9657159100461294e-06, 0.231373, 0.298039, 0.752941, 0.01062181405723095, 0.865003, 0.865003, 0.865003, 0.6212472915649417, 0.705882, 0.0156863, 0.14902]

# Properties modified on n1pLUT
n1pLUT.RGBPoints = [1.9657159100461294e-06, 0.231373, 0.298039, 0.752941, 0.029040325433015823, 0.865003, 0.865003, 0.865003, 0.6212472915649417, 0.705882, 0.0156863, 0.14902]

# Properties modified on n1pLUT
n1pLUT.RGBPoints = [1.9657159100461294e-06, 0.231373, 0.298039, 0.752941, 0.07245943695306778, 0.865003, 0.865003, 0.865003, 0.6212472915649417, 0.705882, 0.0156863, 0.14902]

# Properties modified on n1pLUT
n1pLUT.RGBPoints = [1.9657159100461294e-06, 0.231373, 0.298039, 0.752941, 0.07584892958402634, 0.865003, 0.865003, 0.865003, 0.6212472915649417, 0.705882, 0.0156863, 0.14902]

# Properties modified on n1pLUT
n1pLUT.RGBPoints = [1.9657159100461294e-06, 0.231373, 0.298039, 0.752941, 0.05507656931877136, 0.865003, 0.865003, 0.865003, 0.6212472915649417, 0.705882, 0.0156863, 0.14902]

# Properties modified on n1pLUT
n1pLUT.RGBPoints = [1.9657159100461294e-06, 0.231373, 0.298039, 0.752941, 0.052615340799093246, 0.865003, 0.865003, 0.865003, 0.6212472915649417, 0.705882, 0.0156863, 0.14902]

# Properties modified on n1pLUT
n1pLUT.RGBPoints = [1.9657159100461294e-06, 0.231373, 0.298039, 0.752941, 0.11445679515600204, 0.865003, 0.865003, 0.865003, 0.6212472915649417, 0.705882, 0.0156863, 0.14902]

# Properties modified on n1pLUT
n1pLUT.RGBPoints = [1.9657159100461294e-06, 0.231373, 0.298039, 0.752941, 0.013974194414913654, 0.865003, 0.865003, 0.865003, 0.6212472915649417, 0.705882, 0.0156863, 0.14902]

# Properties modified on n1pLUT
n1pLUT.RGBPoints = [1.9657159100461294e-06, 0.231373, 0.298039, 0.752941, 0.011638794094324112, 0.865003, 0.865003, 0.865003, 0.6212472915649417, 0.705882, 0.0156863, 0.14902]

# Properties modified on n1pLUT
n1pLUT.RGBPoints = [1.9657159100461294e-06, 0.231373, 0.298039, 0.752941, 0.009693697094917297, 0.865003, 0.865003, 0.865003, 0.6212472915649417, 0.705882, 0.0156863, 0.14902]

# Properties modified on n1pPWF
n1pPWF.Points = [1.9657159100461286e-06, 0.0, 0.5, 0.0, 0.0762559026479721, 0.7777778506278992, 0.5, 0.0, 0.2354920655488968, 0.30158731341362, 0.5, 0.0, 0.6212472915649414, 1.0, 0.5, 0.0]

# Properties modified on n1pPWF
n1pPWF.Points = [1.9657159100461286e-06, 0.0, 0.5, 0.0, 0.0762559026479721, 0.7777778506278992, 0.5, 0.0, 0.2668907344341278, 0.6428571939468384, 0.5, 0.0, 0.6212472915649414, 1.0, 0.5, 0.0]

# Properties modified on n1pPWF
n1pPWF.Points = [1.9657159100461286e-06, 0.0, 0.5, 0.0, 0.0762559026479721, 0.7777778506278992, 0.5, 0.0, 0.2691335082054138, 0.6587302088737488, 0.5, 0.0, 0.6212472915649414, 1.0, 0.5, 0.0]

# Properties modified on n1pPWF
n1pPWF.Points = [1.9657159100461286e-06, 0.0, 0.5, 0.0, 0.148024320602417, 0.5714285969734192, 0.5, 0.0, 0.2691335082054138, 0.6587302088737488, 0.5, 0.0, 0.6212472915649414, 1.0, 0.5, 0.0]

# Properties modified on n1pPWF
n1pPWF.Points = [1.9657159100461286e-06, 0.0, 0.5, 0.0, 0.13008220493793488, 0.3888889253139496, 0.5, 0.0, 0.148024320602417, 0.5714285969734192, 0.5, 0.0, 0.2691335082054138, 0.6587302088737488, 0.5, 0.0, 0.6212472915649414, 1.0, 0.5, 0.0]

# Properties modified on n1pLUT
n1pLUT.RGBPoints = [1.9657159100461294e-06, 0.231373, 0.298039, 0.752941, 0.004664603620767593, 0.865003, 0.865003, 0.865003, 0.6212472915649417, 0.705882, 0.0156863, 0.14902]

# Properties modified on n1pLUT
n1pLUT.RGBPoints = [1.9657159100461294e-06, 0.231373, 0.298039, 0.752941, 0.0003950593527406454, 0.865003, 0.865003, 0.865003, 0.6212472915649417, 0.705882, 0.0156863, 0.14902]

# Properties modified on n1pLUT
n1pLUT.ColorSpace = 'HSV'

# Properties modified on n1pLUT
n1pLUT.ColorSpace = 'RGB'

# Properties modified on n1pLUT
n1pLUT.ColorSpace = 'Lab'