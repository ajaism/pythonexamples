#listprimes.py
print("Enter list of values seprated by spaces: ")
lst=[int(val) for val in input().split()]
print("content of list={}".format(lst))
print("--------------------------------------------")
for n in lst:
    if(n<=1):
         print("{} is invalid input:".format(n))
    else:
           result=True
           for i in range(2,n):
                  if (n%i==0):
                     result=False
                     break
           if(result):
                   print("{} is prime".format(n))
           else:
                    print("{} is not prime".format(n))