fruits = {'Apple': 3, 'Banana': 5, 'Orange': 15, 'Grapes': 11, 'Watermelon': 22}
print("Fruits: ",fruits)
l1=list(fruits.items())
l1.sort()
print('Ascending order is : ',l1)
l2=list(fruits.items())
l2.sort(reverse=True)
print('Descending order is : ',l2)