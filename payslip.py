#payslip example using if else
#payslip.py
"""da=20
ta=15
hra=15
ma=5
gpf=2
lic=2"""
"""da=30
ta=25
hra=20
ma=10
gpf=1
lic=1"""
eno = int(input("Enter Employee Number: "))
ename =(input("Enter Employee Name: "))
basicsal =float(input("Enter Basic Salary of Employee: "))
if (basicsal==0):
   print("Invalid Salary: ")
else:
    if (basicsal >=10000):
           da= basicsal*(20/100)
           ta=basicsal*(15/100)
           hra=basicsal*(15/100)
           ma=basicsal*(5/100)
           gpf=basicsal*(2/100)
           lic=basicsal*(2/100)
    else:
          da= basicsal*(30/100)
          ta=basicsal*(25/100)
          hra=basicsal*(20/100)  
          ma=basicsal*(10/100)
          gpf=basicsal*(1/100)
          lic=basicsal*(1/100)
    netsal=(basicsal+da+ta+hra+ma)-(gpf+lic)
    print("*"*50)
    print("Employee number:{}".format(eno))
    print("Employee name:{}".format(ename))
    print("Employee Basic Salary:{}".format(basicsal))
    print("Employee DA:{}".format(da))
    print("Employee TA:{}".format(ta))
    print("Employee HRA:{}".format(hra))
    print("Employee MA:{}".format(ma))
    print("Employee GPF:{}".format(gpf))
    print("Employee LIC:{}".format(lic))
    print("*"*50)
    print("Net Salary:{}".format(netsal))
    print("*"*50)