x=int(input("Enter the current year: "))
y=int(input("Enter the last year: "))
print("Leap years are: ")
for i in range(x,y):
    if (i%4==0) and (i%100!=0) or (i%400==0):
        print(i)