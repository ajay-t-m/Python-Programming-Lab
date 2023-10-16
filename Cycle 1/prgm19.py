list=[1,3,2,5,12,17,19,22,25]
print("List: ",list)
l=[]
for i in list:
    if i%2!=0:
        l.append(i)
print("New list is ",l)