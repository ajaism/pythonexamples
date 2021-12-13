# using if statement finding big number
#bigex1.py
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
#logic for deciding big number
if(a>b)and (a>c):
     print("big({},{},{})={}".format(a,b,c,a))
if(b>a)and (b>c):
     print("big({},{},{})={}".format(a,b,c,b))
if(c>a)and (c>b):
     print("big({},{},{})={}".format(a,b,c,c))
if(a==b)and (b==c):
     print("ALL VALUES ARE EQUAL")
	
   