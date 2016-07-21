#!/usr/local/bin/python3


import csv
import sys


data_zips = dict()
bad_zips = dict()
with open('diff.csv','r') as csvin:
    with open('a','r') as csvin2:
            diff_zips = csv.reader(csvin)
            raw_data_zips = csv.reader(csvin2)
            for row in raw_data_zips:
                data_zips[row[1]]=row[0]
            for zips in diff_zips:
                if str(zips[0]) in data_zips.keys():
                    print(data_zips[str(zips[0])])
              
            

   
