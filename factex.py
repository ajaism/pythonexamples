#programs on while loop
#factex.py
n = int(input("Enter a number: "))
if(n<0):
    print("{} is invalid input")
else:
    i=1
    r =1
    while(i<=n):
      r = r*i
      i= i+1
    else:
          print("Factorail of {} = {}".format(n,r))