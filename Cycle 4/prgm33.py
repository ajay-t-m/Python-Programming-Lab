class rectangle:
    def __init__(self, l, b):
        self.a1=l
        self.a2=b

    def area(self):
        self.a=self.a1*self.a2

    def peri(self):
        self.p=2*(self.a1+self.a2)

    def display(self):
        print("Area of rectangle is ",self.a)
        print("Perimeter of rectangle is",self.p)

    def compare(self, obj2):
        if self.a==obj2.a:
            print("Area of rectangle is equal ")
        elif self.a>obj2.a:
            print("Area1 is greater than Area2")
        else:
            print("Area2 is greater than Area1")

l1=int(input("Enter the length of rectangle1:"))
b1=int(input("Enter the breadth of rectangle1:"))
l2=int(input("Enter the length of rectangle2:"))
b2=int(input("Enter the breadth of rectangle2:"))
obj1=rectangle(l1, b1)
obj2=rectangle(l2, b2)

obj1.area()
obj2.area()
obj1.peri()
obj2.peri()
obj1.display()
obj2.display()
obj1.compare(obj2)