#program for calculating area and perimeter of rectangle 
#area fo rect length * breadth
#perimeter =2(length+breadth)
#react.py
l= float(input("Enter Length:"))
b = float(input("Enter Breadth"))
# calculatinr area and perimeter
area= l*b
pr=2*(l+b)
#dispaly the result
print("-"*40)
print("length is {}".format(l))
print("breadth is {}".format(b))
print("Area of rect {}".format(area))
print("peri of rect {}".format(pr))
print("-"*40)