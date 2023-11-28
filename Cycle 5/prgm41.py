import csv
c=open('csv3.csv',newline='')
d=csv.DictReader(c)
print("Rollno  StudentName")
for i in d:
    print(i['ROLL NO'],'    ',i['STUDENT NAME'])