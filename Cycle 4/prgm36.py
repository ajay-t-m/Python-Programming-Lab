class time:
    def __init__(self,h,m,s):
        self.hr=h
        self.mi=m
        self.se=s

    def __add__(self, x):
        hrs=self.hr+x.hr
        min=self.mi+x.mi
        sec=self.se+x.se
        if sec>=60:
            sec=sec-60
            min=min+1
        if min>=60:
            min=min-60
            hrs=hrs+1
        print(hrs,'hr:',min,'min:',sec,'sec')

print("Time1:")
h1=int(input("Enter the hour:"))
m1=int(input("Enter the minute:"))
s1=int(input("Enter the second:"))
t1=time(h1,m1,s1)
print("Time2:")
h2=int(input("Enter the hour:"))
m2=int(input("Enter the minute:"))
s2=int(input("Enter the second:"))
t2=time(h2,m2,s2)
print("Time is")
t1+t2
