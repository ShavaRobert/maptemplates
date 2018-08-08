# -*- coding: utf-8 -*-
"""
Note that this is experimental coding - reuse of variables, generic variable names and other bad practices
will be common - code should not be copied but rather recreated based on comprehension. 

"""




# import "requests" to allow us to send HTTP/1.1 requests
import requests as RQ

# import "json" to work with json files
import json

# importe pandas for general utility
import pandas as pd

# import xlsx writer to write to xlsx? untested
import xlsxwriter

# import pprint to... print? Code that reads json files uses it
from pprint import pprint

# write from json to xlsx:    https://stackoverflow.com/questions/35583963/writing-heirarchical-json-data-to-excel-xls-from-python



# send request and record response as 'response'
response = RQ.get("https://opendata.arcgis.com/datasets/ae90afc385c04d869bc8cf8890bd1bcd_1.geojson")

# print status code to determine whether the request was successful
print(response.status_code)

# if response.ok is true, print content then save a json file of the output
if response.ok == True:
    print(response.content)
    lad_geo = response.json()
    with open('lad_geo.json','w') as outfile:
        json.dump(lad_geo,outfile)


# reading json files
with open('lad_geo.json') as jsonfile:
        lad_data = json.load(jsonfile)