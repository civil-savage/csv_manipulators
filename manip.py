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

    def write_combo(self, o, k, n):
        with open(n, "wb") as nf:
            csv_out = csv.writer(nf)
            f = 0 #first row flag 
            for orow in o.rows:
                for irow in self.rows:
                    if f == 0: #first row of all
                        f = 1 
                        for item in irow:
                            orow.append(item)
                    elif irow[k[0]] == orow[k[1]]: #matching item
                        for item in irow:
                            orow.append(item)
                csv_out.writerow(orow)

    def return_rows(self, o, k):
        like_rows = []
        for x in range(1,o.row_num):
            for y in range(1,self.row_num):
                if self.rows[y][k[0]] == o.rows[x][k[1]]: 
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

    def delete_rows(self, r, f):
        with open(f, "wb") as nf:
            row_num = 0
            csv_out = csv.writer(nf)
            for row in self.rows:
                if row_num not in r:
                    print row
                    csv_out.writerows(row)
                row_num += 1
            

    def delete_cols(self, c):
        pass
    
i = csv_manip("images_t.csv")
d = csv_manip("data_t.csv")

y = csv_manip("y.csv")
y.delete_rows([1,2,3] , "d.csv")

# i.csv2tsv("x.tsv")
# x = csv_manip("x.tsv")
# x.tsv2csv("y.csv")


i.find_keys(d)
i.write_combo(d,i.like_keys[0],"combo.csv")

