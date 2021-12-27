#innerwhileforloopex1.py
i = 1
while(i<=4):
print("-------------------------------------------")
print("Val of i-outer while loop={}".format(i))
print("---------------------------------------------")
for j in range(12,9,-1):
    print("\tVal of J-inner for loop={}".format(j))
print("\n inner for loop over")
print("---------------------------------------------")
i=i+1
else:
        print("outer while loop over")