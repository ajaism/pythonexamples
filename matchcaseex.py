#matchcaseex1.py
#it is used in python 3.10
wkno = int(input("Entr Week Number: "))
match wkno:
       case 1:
               print("Its Monday")
       case 2:
               print("Its Tuesday")
       case 3:
               print("Its Wednesday")
       case 4:
               print("Its Thursday")
       case 5:
               print("Its friday")
       case 6:
               print("Its Satureday")
       case 7:
               print("Its Sunday")
       case _:
             print("Its not a week number Learn--Weeks")
print("Program is over")