#listbasedex1.py
#example for finding sum and avg
# in this program from user you can tak input in the form of list and show sum and avg of that number this program tak input in the form of list
n = int(input("Enter How many number sum and avg you want to find: "))
if(n<=0):
   print("{} is invalid input:".format(n))
else:
     l=list()
     for i in range (1,n+1):
            val=float(input("Enter {} value :".format(i)))
            l.append(val)
     else:
           print("------------------------------------------")
           print("content of l ={}".format(l))
           print("------------------------------------------")
           s=0
           for val in l:
                    s=s+val
           else:
                 print("-------------------------------------")
                 print("sum={}".format(s))
                 print("avg={}".format(s/len(l)))
                 print("--------------------------------")