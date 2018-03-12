import csv

class csv_manip:

    def __init__(self, csvfile):
        self.rows      = []
        self.names     = []
        self.col_num   = 0
        self.row_num   = 0
        self.name      = csvfile
        with open(csvfile) as datacsv:
            f = csv.reader(datacsv)
            first = f.next()
            self.rows.append(first)
            self.col_num = len(first)
            self.names = first 
            for row in f:
                self.rows.append(row)
            self.row_num = len(self.rows)
            
    def find_keys(self, o):
        self.like_keys = []
        self.key_names = []
        if self.col_num > o.col_num:
            longer   = self.col_num
            shorter  = o.col_num
        else:
            longer   = o.col_num
            shorter  = self.col_num
        for j in range(0,shorter):
            for x in range(0,longer):
                if o.rows[1][x] == self.rows[1][j]: #longest/shortest thrown out
                    self.like_keys.append([j,x])
                    self.key_names.append([self.rows[0][j],o.rows[0][x]])

    def write_csv(self, o, k):
        with open('combo.csv', "wb") as combo:
            combo_writer = csv.writer(combo)
            f = 0 #first row flag 
            for orow in o.rows:
                for irow in self.rows:
                    if f == 0: #first row of all
                        f = 1 
                        for item in irow:
                            orow.append(item)
                    elif orow[k[1]] == irow[k[0]]: #first item the same 
                        for item in irow:
                            orow.append(item)
                combo_writer.writerow(orow)

        
    def return_rows(self, o, keys):
        like_rows = []
        for x in range(1,o.row_num):
            for y in range(1,self.row_num):
                if o.rows[x][keys[1]] == self.rows[y][keys[0]]:
                    like_rows.append([x,y])
        return like_rows

    def tsv2csv(self, c):
        with open(self.name, "rb") as tf:
            tsvin = csv.reader(tf, delimiter='\t')
            with open(c, "wb") as cf:
                csv_out = csv.writer(cf,
                                     delimiter=',',
                                     quoting=csv.QUOTE_MINIMAL)
                csv_out.writerows(tsvin)

    def csv2tsv(self, t):
        with open(self.name, "rb") as cf:
            csvin = csv.reader(cf, delimiter=',')
            with open(t, "wb") as tf:
                tsv_out = csv.writer(tf,
                                     delimiter='\t',
                                     quoting=csv.QUOTE_MINIMAL)
                tsv_out.writerows(csvin)
                
    def dups(self, f, c):  #sort out dups
        items = dict()
        out = []
        for csv_file in c:
            with open(csv_file, 'rb') as csvfile:
                csv_dict = csv.DictReader(csvfile)
                for row in csv_dict:
                    if row[f] not in items.keys():
                        items[row[f]] = [csv_file]
                    else:
                        items[row[f]].append(csv_file)


        for item in items.keys():
            if len(items[item]) is not None:
                out_str.append(item, items[item])

        return  out_str
                
i = csv_manip("images_t.csv")
d = csv_manip("data_t.csv")

dups = i.dups("SKU", [d])
print dups

# i.csv2tsv("x.tsv")
# x = csv_manip("x.tsv")
# x.tsv2csv("y.csv")


# i.find_keys(d)
# i.write_csv(d,i.like_keys[0])

