#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 11:14:43 2017

@author: stijn_vanhoey
"""

from datetime import datetime

import requests
import pandas as pd
import matplotlib.pyplot as plt

station = "023072043" # != timeseriesgroup_id
period = "P3D"
returnfields = ["Timestamp", "Value", "Quality Code"]

print("Request the data from VMM Waterinfo...")
r = requests.get("http://download.waterinfo.be/tsmdownload/KiWIS/KiWIS", 
                 params={"datasource": 0, "type": "queryServices", 
                         "service": "kisters", 
                         "request": "getTimeseriesValues",
                         "ts_id": station, "format": "json", 
                         "period": period, "metadata": "true", 
                         "returnfields": ','.join(returnfields)})

print("Extract the waterheight information from the request...")
data = r.json()[0]
waterhoogte = pd.DataFrame(data['data'], 
                           columns = data["columns"].split(','))
waterhoogte["Timestamp"] = pd.to_datetime(waterhoogte["Timestamp"])
waterhoogte = waterhoogte.set_index("Timestamp")

print("Make a plot of the data (with rolling mean for 3, 6 and 12H windows...")
fig, ax = plt.subplots(figsize=(12, 6))
waterhoogte["Value"].plot(ax=ax, label='observed')
waterhoogte["Value"].resample('H').mean().rolling(window=3, center=True).mean().plot(ax=ax, label='3H rolling mean')
waterhoogte["Value"].resample('H').mean().rolling(window=6, center=True).mean().plot(ax=ax, label='6H rolling mean')
waterhoogte["Value"].resample('H').mean().rolling(window=12, center=True).mean().plot(ax=ax, label='12H rolling mean')
ax.set_ylabel("Waterhoogte [m TAW]")
ax.set_title("Waterpeil " + data['station_name'])
ax.set_xlabel("")
ax.legend()

print("Save the figure as png and pdf...")
filename = datetime.now().strftime("%Y-%m-%d") + "_waterheight_" + "_station"
fig.savefig(filename + ".png")
fig.savefig(filename + ".pdf")
print("...DONE!")