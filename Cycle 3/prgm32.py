from packages.circle import *
r=int(input("Enter the radius:"))
carea(r)
cperi(r)

from packages.rectangle import *
l=int(input("Enter the length of rectangle:"))
b=int(input("Enter the breadth of rectangle:"))
rarea(l,b)
rperi(l,b)

from packages.Dpack.sphere import *
r1=int(input("Enter the radius of sphere :"))
sarea(r1)
speri(r1)

from packages.Dpack.cuboid import *
l1=int(input("Enter the length of cuboid:"))
b1=int(input("Enter the breadth of cuboid:"))
h1=int(input("Enter the height of cuboid:"))
cuarea(l1,b1,h1)
cuperi(l1,b1,h1)