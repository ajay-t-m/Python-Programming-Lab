a=int(input("Enter the lower limit: "))
b=int(input("Enter the upper limit: "))
list=[i for i in range(a,b+1) if all(int(digit) % 2 == 0 for digit in str(i)) and int(i**0.5)**2 == i]
print(list)
