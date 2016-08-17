#!usr/local/bin/python

import argparse
import csv
import sys

parser = argparse.ArgumentParser("Converts a tsv file to a csv file.")

parser.add_argument('tsv', nargs='?', type=argparse.FileType('rb'),
                    default=sys.stdin, help="A tsv file to convert.")
parser.add_argument('csv', nargs='?', type=argparse.FileType('wb'),
                    default=sys.stdout, help="A csv file to output.")
args = parser.parse_args()
tsvin = csv.reader(args.tsv, delimiter='\t')
csv_out = csv.writer(args.csv, delimiter=',', quoting=csv.QUOTE_MINIMAL)
csv_out.writerows(tsvin)
