# import csv
# with open('csv3.csv',newline='') as csvfile:
#     d=csv.reader(csvfile,delimiter=' ',quotechar='|')
#     for i in d:
#         print(','.join(i))

import csv
c=open('csv3.csv',newline='')
d=csv.reader(c)
for i in d:
    print(','.join(i))