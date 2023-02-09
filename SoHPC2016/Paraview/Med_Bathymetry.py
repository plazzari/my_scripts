#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'NetCDF Reader'
ave20140926120000_notimenc = NetCDFReader(FileName=['/pico/scratch/userexternal/plazzari/xVISUALIZZAZIONE3d/ave.20140926-12:00:00_notime.nc'])
ave20140926120000_notimenc.Dimensions = '(depth, lat, lon)'

# Properties modified on ave20140926120000_notimenc
ave20140926120000_notimenc.VerticalScale = -100.0
ave20140926120000_notimenc.VerticalBias = 6370000.0

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [807, 601]

# show data in view
ave20140926120000_notimencDisplay = Show(ave20140926120000_notimenc, renderView1)
# trace defaults for the display properties.
ave20140926120000_notimencDisplay.Representation = 'Outline'
ave20140926120000_notimencDisplay.ColorArrayName = [None, '']
ave20140926120000_notimencDisplay.ScalarOpacityUnitDistance = 21028.97511622662

# reset view to fit data
renderView1.ResetCamera()

# create a new 'Cell Data to Point Data'
cellDatatoPointData1 = CellDatatoPointData(Input=ave20140926120000_notimenc)

# show data in view
cellDatatoPointData1Display = Show(cellDatatoPointData1, renderView1)
# trace defaults for the display properties.
cellDatatoPointData1Display.Representation = 'Outline'
cellDatatoPointData1Display.ColorArrayName = [None, '']
cellDatatoPointData1Display.ScalarOpacityUnitDistance = 21028.97511622662

# hide data in view
Hide(ave20140926120000_notimenc, renderView1)

# create a new 'Contour'
contour1 = Contour(Input=cellDatatoPointData1)
contour1.ContourBy = ['POINTS', 'N1p']
contour1.Isosurfaces = [5.000000100204387e+19]
contour1.PointMergeMethod = 'Uniform Binning'

# Properties modified on contour1
contour1.Isosurfaces = [1000.0]

# show data in view
contour1Display = Show(contour1, renderView1)
# trace defaults for the display properties.
contour1Display.ColorArrayName = [None, '']

# set active source
SetActiveSource(contour1)

# create a new 'Smooth'
smooth1 = Smooth(Input=contour1)

# hide data in view
Hide(contour1, renderView1)

# show data in view
smooth1Display = Show(smooth1, renderView1)
# trace defaults for the display properties.
smooth1Display.ColorArrayName = [None, '']

# hide data in view
Hide(contour1, renderView1)

# set active source
SetActiveSource(contour1)

# hide data in view
Hide(smooth1, renderView1)

# show data in view
contour1Display = Show(contour1, renderView1)

# destroy smooth1
Delete(smooth1)
del smooth1

# create a new 'Clean'
clean1 = Clean(Input=contour1)

# set active source
SetActiveSource(contour1)

# destroy clean1
Delete(clean1)
del clean1

# set active source
SetActiveSource(cellDatatoPointData1)

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=cellDatatoPointData1)

# set active source
SetActiveSource(contour1)

# set active source
SetActiveSource(ave20140926120000_notimenc)

# create a new 'Clip'
clip1 = Clip(Input=ave20140926120000_notimenc)
clip1.ClipType = 'Plane'
clip1.Scalars = ['CELLS', 'N1p']
clip1.Value = 5.000000100204387e+19

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [4389537.695483816, 1206932.93053324, 3756264.522006227]

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=clip1)

# Properties modified on clip1
clip1.ClipType = 'Scalar'
clip1.InsideOut = 1

# show data in view
clip1Display = Show(clip1, renderView1)
# trace defaults for the display properties.
clip1Display.ColorArrayName = [None, '']
clip1Display.ScalarOpacityUnitDistance = 29818.66327359549

# show data in view
extractSurface1Display = Show(extractSurface1, renderView1)
# trace defaults for the display properties.
extractSurface1Display.ColorArrayName = [None, '']

# hide data in view
Hide(cellDatatoPointData1, renderView1)

# Properties modified on clip1
clip1.InsideOut = 0

# Properties modified on clip1
clip1.Value = 1000.0
clip1.InsideOut = 1

# Properties modified on clip1
clip1.InsideOut = 0

# set scalar coloring
ColorBy(clip1Display, ('CELLS', 'N1p'))

# rescale color and/or opacity maps used to include current data range
clip1Display.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'N1p'
n1pLUT = GetColorTransferFunction('N1p')
n1pLUT.RGBPoints = [1.0000000200408773e+20, 0.231373, 0.298039, 0.752941, 1.0000000200408773e+20, 0.865003, 0.865003, 0.865003, 1.0000000200408773e+20, 0.705882, 0.0156863, 0.14902]
n1pLUT.ColorSpace = 'RGB'
n1pLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'N1p'
n1pPWF = GetOpacityTransferFunction('N1p')
n1pPWF.Points = [1.0000000200408773e+20, 0.0, 0.5, 0.0, 1.0000000200408773e+20, 0.5079365372657776, 0.5, 0.0, 1.0000000200408773e+20, 0.7222222685813904, 0.5, 0.0, 1.0000000200408773e+20, 0.40476194024086, 0.5, 0.0, 1.0000000200408773e+20, 1.0, 0.5, 0.0]
n1pPWF.ScalarRangeInitialized = 1

# hide data in view
Hide(extractSurface1, renderView1)

# set active source
SetActiveSource(extractSurface1)

# set active source
SetActiveSource(extractSurface1)

# show data in view
extractSurface1Display = Show(extractSurface1, renderView1)

# hide data in view
Hide(extractSurface1, renderView1)

# set active source
SetActiveSource(clip1)

# turn off scalar coloring
ColorBy(clip1Display, None)