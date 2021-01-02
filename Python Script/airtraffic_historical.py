#!/usr/bin/env python
# coding: utf-8

from traffic.data import opensky
#pooling air traffic data 
opensky.history("2020-01-01", "2020-05-31",
    airport="LOWS",bounds = (12.2,47.3,13.7,48.2)).to_csv(r'C:\Users\Dell\Documents\opensky\airtraff_jan_may2020.csv')
#pooling flights info
opensky.flightlist("2020-01-01", "2020-05-31", 
                   airport = 'LOWS').to_csv(r'C:\Users\Dell\Documents\opensky\flightlist_jan_may2020.csv')




