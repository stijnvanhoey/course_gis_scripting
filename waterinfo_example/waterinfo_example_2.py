#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 11:14:43 2017

@author: stijn_vanhoey
"""

import sys
import argparse
from datetime import datetime

import requests
import pandas as pd
import matplotlib.pyplot as plt


def request_waterinfo_timeseries(station_id, period="P3D"):
    """Request time series data from VMM Waterinfo

    Parameters
    ----------
    station_id : string
        ts_id as defined by Waterinfo/Kisters/dbase
    period : string
        define the timeframe to request data from. e.g. 1 day: P1D or 10 days: P10D,
        default to 3 days period

    Returns
    -------
    dict with the data and metadata fields from the request
    """
    returnfields = ["Timestamp", "Value", "Quality Code"]
    r = requests.get("http://download.waterinfo.be/tsmdownload/KiWIS/KiWIS", 
                    params={"datasource": 0, "type": "queryServices", 
                            "service": "kisters", 
                            "request": "getTimeseriesValues",
                            "ts_id": station_id, "format": "json", 
                            "period": period, "metadata": "true", 
                            "returnfields": ','.join(returnfields)})

    return r.json()[0]


def plot_waterheight_timeseries(jsondata, moving_windows=[3, 6, 12]):
    """Make a plot of waterheighst with moving window averages
    
    Parameters
    ----------
    jsondata : dict
        dict with data and metadata fields from the Waterinfo API
    moving_windows : list
        set of HOURLY moving windows that will be applied to the data
    
    Returns
    -------
    fig, ax : matplotlib figure and ax object
    """
    # Extract the waterheight information
    waterhoogte = pd.DataFrame(jsondata['data'], 
                            columns = jsondata["columns"].split(','))
    waterhoogte["Timestamp"] = pd.to_datetime(waterhoogte["Timestamp"])
    waterhoogte = waterhoogte.set_index("Timestamp")

    # Make a plot of the data (with rolling mean for 3, 6 and 12H windows)
    fig, ax = plt.subplots(figsize=(12, 6))
    waterhoogte["Value"].plot(ax=ax, label='observed')
    for freq in moving_windows:
        label = str(freq) + 'H rolling mean'
        waterhoogte["Value"].resample('H').mean().rolling(window=int(freq), 
                                                          center=True).mean().plot(ax=ax, 
                                                                                   label=label)
    ax.set_ylabel("Waterhoogte [m TAW]")
    ax.set_title("Waterpeil " + jsondata['station_name'])
    ax.set_xlabel("")
    #ax.set_ylim([0, waterhoogte["Value"].max()+  waterhoogte["Value"].max()*0.1])
    ax.legend()

    return fig, ax

def main(argv=None):
    """
    Request waterheight of timeseriesgroup_id of VMM Waterinfo API
    and plot the data together with provided moving window values
    """    
    parser = argparse.ArgumentParser(description="""Request time series 
        data from the VMM Waterinfo API and make a time series plot with 
        rolling average derivatives
        """)    
    
    parser.add_argument('station', type=str, default="023072043",
                        help='ts_id as defined by Waterinfo/Kisters/dbase')

    parser.add_argument('--period', type=str,
                        action='store', default="P3D", 
                        help='define the timeframe to request data from. e.g. 1 day: P1D or 10 days: P10D')

    parser.add_argument('--windows', type=str, nargs='+',
                        action='store', default=["3", "6", "12"], 
                        help="""set of HOURLY moving windows that will 
                            be applied to the data
                            """)
    parser.add_argument('--save', action='store_true',
                        default=False, help='Sace the outcome to file or just show the outcome.')     

    args = parser.parse_args()   

    print("Working on the API requests to waterinfo...")
    data = request_waterinfo_timeseries(args.station, 
                                       period=args.period)
    print(args.windows)
    fig, ax = plot_waterheight_timeseries(data, 
                                          moving_windows=args.windows)
    
    if args.save:
        filename = datetime.now().strftime("%Y-%m-%d") + "_waterheight_" + "_station"
        fig.savefig(filename + ".png")
        fig.savefig(filename + ".pdf")
        print("saving to file...done!")
    else:
        plt.show()

if __name__ == "__main__":
    sys.exit(main())
