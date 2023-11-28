class bank:
    def __init__(self,a,n,t,b):
        self.ac=a
        self.name=n
        self.type=t
        self.balance=b

    def dep(self,a1):
        self.balance+=a1
        print("Balance is ",self.balance)

    def withdrw(self,a2):
        if self.balance<a2:
            print("Balance insufficient")
        else:
            self.balance-=a2
            print("Balance is ",self.balance)

    def display(self):
        print("Account no:",self.ac)
        print("Name:",self.name)
        print("Type:",self.type)
        print("Balance:",self.balance)

a=int(input("Enter the account no:"))
n=input("Enter the name:")
t=input("Enter the type:")
b=int(input("Enter the balance:"))
obj=bank(a,n,t,b)
obj.display()
a1=int(input("Enter the amount to deposit:"))
obj.dep(a1)
a2=int(input("Enter the amount to withdraw:"))
obj.withdrw(a2)