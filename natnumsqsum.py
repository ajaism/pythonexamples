#natnumsqsum.py
# it shows n no 1to n number square and shows sum of all values
n = int(input("Enter How Many Numbers: "))
if(n<=0):
    print("{} in invalid input: ")
else:
     i = 1
     s= 0
     while(i<=n):
         s = s+i**2
         print("\t {}".format(i**2))
         i = i+1
     else: 
         print("square sum ={}".format(s))