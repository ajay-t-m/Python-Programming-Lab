x=str(input("Enter the string: "))
first=x[0]
x1=x.replace(first,"$")
x1=first+x1[1:]
print(x1)