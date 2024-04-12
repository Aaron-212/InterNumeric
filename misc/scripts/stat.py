from fontTools.designspaceLib import DesignSpaceDocument, LocationLabelDescriptor, AxisLabelDescriptor

path = "fonts-temp/master-ufo/InterNumeric.designspace"
dsfile = DesignSpaceDocument.fromfile(path)

wghtAxisLabels = [
    AxisLabelDescriptor(name="Thin", userValue=100),
    AxisLabelDescriptor(name="ExtraLight", userValue=200),
    AxisLabelDescriptor(name="Light", userValue=300),
    AxisLabelDescriptor(name="Regular", userValue=400, elidable=True, linkedUserValue=700),
    AxisLabelDescriptor(name="Medium", userValue=500),
    AxisLabelDescriptor(name="SemiBold", userValue=600),
    AxisLabelDescriptor(name="Bold", userValue=700),
    AxisLabelDescriptor(name="ExtraBold", userValue=800),
    AxisLabelDescriptor(name="Black", userValue=900),
]
dsfile.getAxisByTag("wght").axisLabels = wghtAxisLabels

RDNSAxisLabels = [
    AxisLabelDescriptor(name="Regular", userValue=-1, elidable=True),
    AxisLabelDescriptor(name="Softened", userValue=0),
    AxisLabelDescriptor(name="Rounded", userValue=1),
]

dsfile.getAxisByTag("RDNS").axisLabels = RDNSAxisLabels

locationLabels = [
    LocationLabelDescriptor(name="Thin", userLocation=dict(Roundness=-1, Weight=100)),
    LocationLabelDescriptor(name="ExtraLight", userLocation=dict(Roundness=-1, Weight=200)),
    LocationLabelDescriptor(name="Light", userLocation=dict(Roundness=-1, Weight=300)),
    LocationLabelDescriptor(name="Regular", userLocation=dict(Roundness=-1, Weight=400)),
    LocationLabelDescriptor(name="Medium", userLocation=dict(Roundness=-1, Weight=500)),
    LocationLabelDescriptor(name="SemiBold", userLocation=dict(Roundness=-1, Weight=600)),
    LocationLabelDescriptor(name="Bold", userLocation=dict(Roundness=-1, Weight=700)),
    LocationLabelDescriptor(name="ExtraBold", userLocation=dict(Roundness=-1, Weight=800)),
    LocationLabelDescriptor(name="Black", userLocation=dict(Roundness=-1, Weight=900)),
    
    LocationLabelDescriptor(name="Thin Softened", userLocation=dict(Roundness=0, Weight=100)),
    LocationLabelDescriptor(name="ExtraLight Softened", userLocation=dict(Roundness=0, Weight=200)),
    LocationLabelDescriptor(name="Light Softened", userLocation=dict(Roundness=0, Weight=300)),
    LocationLabelDescriptor(name="Softened", userLocation=dict(Roundness=0, Weight=400)),
    LocationLabelDescriptor(name="Medium Softened", userLocation=dict(Roundness=0, Weight=500)),
    LocationLabelDescriptor(name="SemiBold Softened", userLocation=dict(Roundness=0, Weight=600)),
    LocationLabelDescriptor(name="Bold Softened", userLocation=dict(Roundness=0, Weight=700)),
    LocationLabelDescriptor(name="ExtraBold Softened", userLocation=dict(Roundness=0, Weight=800)),
    LocationLabelDescriptor(name="Black Softened", userLocation=dict(Roundness=0, Weight=900)),
    
    LocationLabelDescriptor(name="Thin Rounded", userLocation=dict(Roundness=1, Weight=100)),
    LocationLabelDescriptor(name="ExtraLight Rounded", userLocation=dict(Roundness=1, Weight=200)),
    LocationLabelDescriptor(name="Light Rounded", userLocation=dict(Roundness=1, Weight=300)),
    LocationLabelDescriptor(name="Rounded", userLocation=dict(Roundness=1, Weight=400)),
    LocationLabelDescriptor(name="Medium Rounded", userLocation=dict(Roundness=1, Weight=500)),
    LocationLabelDescriptor(name="SemiBold Rounded", userLocation=dict(Roundness=1, Weight=600)),
    LocationLabelDescriptor(name="Bold Rounded", userLocation=dict(Roundness=1, Weight=700)),
    LocationLabelDescriptor(name="ExtraBold Rounded", userLocation=dict(Roundness=1, Weight=800)),
    LocationLabelDescriptor(name="Black Rounded", userLocation=dict(Roundness=1, Weight=900)),
]
for label in locationLabels:
    dsfile.addLocationLabel(label)

dsfile.write(path)