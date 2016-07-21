#!usr/local/bin/python

import csv

with open('x.tsv','rb') as tsvin, open('x1.csv', 'wb') as csvout:
    tsvin = csv.reader(tsvin, delimiter='\t')
    csvf = csv.writer(csvout, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    csvf.writerows(tsvin)
## encodong issues, 
