import random as r
a="abcdefghigjlmnopqrstuvwxyz"
b="1234567890"
c=a+b
d=16
user=int(input("Enter number of gmail :-- "))
for i in range (user):
	e="".join(r.sample(c,d))
	print(e+"@gmail.com")
