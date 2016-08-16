import csv


CSV_FILES = ["test.csv","test_2.csv","test_3.csv"]
TEST_FIELD = "field_1"
ITEMS = dict()


for csv_file in CSV_FILES:
        with open(csv_file, 'rb') as csvfile:
                csv_dict = csv.DictReader(csvfile)
                for row in csv_dict:
                        if row[TEST_FIELD] not in ITEMS.keys() :
                                ITEMS[row[TEST_FIELD]] = [csv_file]
                        else:
                                ITEMS[row[TEST_FIELD]].append(csv_file)
                                
                                
out_str = "For the field '{}' there were duplicates in the following:".format(TEST_FIELD)
for item in ITEMS.keys():
        if len(ITEMS[item]) > 1:
                out_str += "For item '{}', check in the files '{}' ".format(item, ITEMS[item])

print out_str



