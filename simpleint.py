#program for simple intrest and total amount to pay
# simple intrest
#simple intrest(p*q*r)/100
#totalamt=p+si
p = float(input("Enter Prncipal amount: "))
t=float(input("Enter time: "))
r=float (input("Enter rate of intrest: "))
#calculate si
si = (p*t*r)/100
#calculate total amoount to pay
totalamt = p+si
print("---------------------------------------------")
print("\t Simple intrest result")
print("-----------------------------------------------")
print("\t principal amount {}".format(p))
print("\t time {}".format(t))
print("\t rate of intrest {}".format(r))
print("\t simple intrest is {}".format(si))
print("\t total amount to pay {}".format(totalamt))
print("-------------------------------------------------------")