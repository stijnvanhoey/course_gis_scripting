with fiona.open('../data/EUgrid10.geojson') as eugrid:
    feature = next(iter(eugrid)) # Just one checking the first
    print("cellcode: ", feature['properties']['CellCode'])
    print("Vectortype: ", feature['geometry']['type'])