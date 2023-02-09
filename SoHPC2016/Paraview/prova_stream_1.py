#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'NetCDF Reader'
uVW20140926120000nc = NetCDFReader(FileName=['/pico/scratch/userexternal/plazzari/xVISUALIZZAZIONE3d/UVW.20140926-12:00:00.nc'])
uVW20140926120000nc.Dimensions = '(depth, lat, lon)'

# Properties modified on uVW20140926120000nc
uVW20140926120000nc.VerticalScale = -100.0
uVW20140926120000nc.VerticalBias = 6371000.0

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [740, 601]

# show data in view
uVW20140926120000ncDisplay = Show(uVW20140926120000nc, renderView1)
# trace defaults for the display properties.
uVW20140926120000ncDisplay.Representation = 'Outline'
uVW20140926120000ncDisplay.ColorArrayName = [None, '']
uVW20140926120000ncDisplay.ScalarOpacityUnitDistance = 21032.123379620578

# reset view to fit data
renderView1.ResetCamera()

# create a new 'Calculator'
calculator1 = Calculator(Input=uVW20140926120000nc)
calculator1.Function = ''

# Properties modified on calculator1
calculator1.ResultArrayName = 'v-vector'
calculator1.Function = 'u*iHat+v*jHat+w*kHat'

# show data in view
calculator1Display = Show(calculator1, renderView1)
# trace defaults for the display properties.
calculator1Display.Representation = 'Outline'
calculator1Display.ColorArrayName = [None, '']
calculator1Display.ScalarOpacityUnitDistance = 21032.123379620578

# hide data in view
Hide(uVW20140926120000nc, renderView1)

# Properties modified on calculator1
calculator1.CoordinateResults = 1

# Properties modified on calculator1
calculator1.AttributeMode = 'Cell Data'

# set active source
SetActiveSource(uVW20140926120000nc)

# show data in view
uVW20140926120000ncDisplay = Show(uVW20140926120000nc, renderView1)

# set active source
SetActiveSource(calculator1)

# Properties modified on calculator1
calculator1.CoordinateResults = 0
calculator1.ResultTCoords = 1

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(Input=calculator1,
    SeedType='Point Source')
streamTracer1.Vectors = ['CELLS', 'v-vector']
streamTracer1.MaximumStreamlineLength = 4109035.6644937517

# init the 'Point Source' selected for 'SeedType'
streamTracer1.SeedType.Center = [4390250.17252651, 1207122.294677829, 3756875.1823421046]
streamTracer1.SeedType.Radius = 410903.5664493752

# show data in view
streamTracer1Display = Show(streamTracer1, renderView1)
# trace defaults for the display properties.
streamTracer1Display.ColorArrayName = [None, '']

# set active source
SetActiveSource(calculator1)

# set active source
SetActiveSource(uVW20140926120000nc)

# set scalar coloring
ColorBy(uVW20140926120000ncDisplay, ('CELLS', 'v'))

# rescale color and/or opacity maps used to include current data range
uVW20140926120000ncDisplay.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
uVW20140926120000ncDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'v'
vLUT = GetColorTransferFunction('v')
vLUT.RGBPoints = [1.965715910046129e-06, 0.231373, 0.298039, 0.752941, 0.1233539208769798, 0.865003, 0.865003, 0.865003, 0.6212472915649417, 0.705882, 0.0156863, 0.14902]
vLUT.ColorSpace = 'RGB'

# get opacity transfer function/opacity map for 'v'
vPWF = GetOpacityTransferFunction('v')
vPWF.Points = [1.965715910046129e-06, 0.0, 0.5, 0.0, 0.09195524454116821, 0.5079365372657776, 0.5, 0.0, 0.2018506228923798, 0.7222222685813904, 0.5, 0.0, 0.2938039004802704, 0.40476194024086, 0.5, 0.0, 0.6212472915649414, 1.0, 0.5, 0.0]

# hide data in view
Hide(streamTracer1, renderView1)

# hide data in view
Hide(calculator1, renderView1)

# Properties modified on uVW20140926120000nc
uVW20140926120000nc.ReplaceFillValueWithNan = 1

# change representation type
uVW20140926120000ncDisplay.SetRepresentationType('Points')