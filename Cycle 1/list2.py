list1=[2,6,4,8,9]
list2=[10,15,12,16,4]
print("list1: ",list1)
print("list2: ",list2)
#a
print("Length of list1: ",len(list1))
print("Length of list2: ",len(list2))
if len(list1)==len(list2):
    print("Length of list is same")
else:
    print("Length of list is not same")
#b
print("Sum of list1 is",sum(list1))
print("Sum of list2 is",sum(list2))
if sum(list1)==sum(list2):
    print("Sum of list are same")
else:
    print("Sum of list are not same")
#c
check=any(i in list1 for i in list2)
print("Any common value is present in both list: ",check)