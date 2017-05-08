fig, ax = plt.subplots()
geo_df.to_crs(epsg="4326").plot(markersize=10, ax=ax) # on the fly conversion to WGS84
geo_df.buffer(500).to_crs(epsg="4326").plot(ax=ax) # on the fly conversion to WGS84
mplleaflet.display()