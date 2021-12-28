#multiplicationtable.py
print("Enter list of values seprated by space: ")
lst=[int(val)for val in input().split()]
print("content of list".format(lst))
print("-"*50)
for n in lst:
      if(n<=0):
          print("{} is invalid input".format(n))
      else:
              print("multiplicatition Table for{}".format(n))
              print("-"*50)
              for i in range(1,11):
                 print("\t{}X{}={}".format(n,i,n*i))
                 print("-"*50)
