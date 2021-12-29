#menudriven.py
# this program is for area of rect,circle,triangle,square
import sys,math
while(True):
      print("-"*50)
      print("\tArea of Different figures")
      print("-"*50)
      print("\t1.Rectangle")
      print("\t2.Square")
      print("\t3.Circle")
      print("\t4.Triangle")
      print("\t5.Exit")
      print("-"*50)
      ch=int(input("Enter Your Choice:"))
      match ch:
             case 1:
                     l=float(input("Enter Length:"))
                     b=float(input("Enter Breadth:"))
                     ra=l*b
                     print("Area of Rectangle={}".format(ra))
             case 2:
                     s=float(input("Enter Side:"))
                     sa=s**2
                     print("Area of Square={}".format(sa))
             case 3:
                     r=float(input("Enter Radius:"))
                     ca=math.pi*r**2
                     print("Area of Circle={}".format(ca))
             case 4:
                     a=float(input("Enter Value of a: "))
                     b=float(input("Enter Value of b: "))
                     c=float(input("Enter value of c: "))
                     sa =(a+b+c)/2
                     at=(s*(s-a)*(s-b)*(s-c))**0.5
                     print("Area of Triangle={}".format(at))
             case 5: 
                     print("Thsnx for using this Program!!")
                     sys.exit()
             case _:
                     print("your choice is Inalid --Try Again!1")