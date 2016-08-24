import argparse
import csv


parser = argparse.ArgumentParser("Checks a lsit of csv files for duplicates.")

parser.add_argument('field', nargs=1, type=str,
                    help="A field to check for duplicates.")
parser.add_argument('csv_files', nargs='*',
                    help="A list of csv files to check.")


args = parser.parse_args()
ITEMS = dict()
FIELD = args.field.pop()

for csv_file in args.csv_files:
        with open(csv_file, 'rb') as csvfile:
                csv_dict = csv.DictReader(csvfile)
                for row in csv_dict:
                        if row[FIELD] not in ITEMS.keys():
                                ITEMS[row[FIELD]] = [csv_file]
                        else:
                                ITEMS[row[FIELD]].append(csv_file)

out_str = """
For the field '{}' there were duplicates in the following:
""".format(FIELD)

for item in ITEMS.keys():
        if len(ITEMS[item]) > 1:
                out_str += """
                For item '{}', check in the files '{}'
                """.format(item, ITEMS[item])

print out_str
