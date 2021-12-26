#innerforwhileloopex1.py
for i in range(5,0,-1):
    print("---------------------------------------------")
    print("value of i-outer for loop={}".format(i))
    print("----------------------------------------------")
    j=14
    while(j>=10):
         print("\tVal of j-inner while loop={}".format(j))
         j=j-1
         print("\n Inner while loop ever")
         print("--------------------------------------------")
else:
      print("outer for loop over")