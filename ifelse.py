#if else example
#ifelse.py
a = int(input("Enter value of A: "))
b = int(input("Enter value of B: "))
if(a==b):
   print("Both values are equal")
else:
    if(a>b):
         print("big({},{}={})".format(a,b,a))
    else:
         print("big({},{}={})".format(a,b,b))