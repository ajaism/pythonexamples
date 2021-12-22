#multableex1.py
#USING for multiplication table
n = int(input("Enter a number : "))
if(n<=0):
     print("{} is invalid input".format(n))
else:
     print("*"*40)
     print("Mul table for :{}".format(n))
     print("*"*40)
     for i in range(1,11):
            print("{}X{}={}".format(n,i,n*i))
     else:
            print("*"*40)