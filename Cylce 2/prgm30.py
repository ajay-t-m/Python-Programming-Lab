print("Rectangle:")
l=int(input("Enter the length:"))
b=int(input("Enter the breadth:"))
r=lambda x,y:x*y
print("Area of rectangle is ",str(r(l,b)))
print("Sqaure:")
s=int(input("Enter the side:"))
a=lambda x:x*x
print("Area of sqaure is ",str(a(s)))
print("Triangle:")
b=int(input("Enter the base:"))
h=int(input("Enter the height:"))
t=lambda x,y:.5*x*y
print("Area of triangle is",str(t(b,h)))