n=int(input("Enter the numbers of elements: "))
list=[]
for i in range(0,n):
    x=int(input("Enter the elements: "))
    if x>100:
        list.append('over')
    else:
        list.append(x)
print(list)