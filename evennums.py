#even numbr using while loop
#evennums.py
n =int(input("Enter a number: "))
if(n<=0):
     print("{} is invalid".format(n))
else:
    print("*"*40)
    print("Even number within {}".format(n))
    print("*"*40)
    i =2
    while(i<=n):
       print("val of i = {}".format(i))
       print("*"*40)
       i = i+2
    else:
       print("*"*40)