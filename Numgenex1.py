#Numgenex1.py
# this program genrates 1 to n  where n is positive
n = int(input("enter a number: "))
if (n<=0):
  print("{} is invalid".format(n))
else:
 i =1  #initilization part
 while(i<=n): #conditional part
     print("val of i ={}".format(i))
     i=i+1  # updation part
 else:
     print("\n I am from else----while---val of i =",i)
     print("\n program exucuted over while... else")
print("Program exec over ---if --else")