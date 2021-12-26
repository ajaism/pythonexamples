#studentmarksreport.py
#validation of student number
while(True):
   stno=int(input("Enter Student Number: "))
   if(stno>0)and(stno<=100):
        break
#Accept name
sname= input("Enter student name: ")
#Accept Mark and Validate
while(True):
       cm= int(input("Enter Marks in C: "))
       if(cm>=0) and (cm<=100):
          break
while(True):
       cppm= int(input("Enter Marks in CPP: "))
       if(cppm>=0) and (cppm<=100):
          break 
while(True):
       pytm= int(input("Enter Marks in Python: "))
       if(pytm>=0) and (pytm<=100):
          break
#Validation on marks
totmarks=cm+cppm+pytm
percentmarks=(totmarks/300)*100
# Decide grades
if(cm<40)or(cppm<40)or(pytm<40):
       grade= "Fails"
else:
         if((totmarks>=200) and (totmarks<=300)):
               grade="Passed in Distiction"
         elif((totmarks>=200) and (totmarks<=249)):
               grade ="Passed in First"
         elif((totmarks>=150) and (totmarks<=199)):
               grade ="Passed in Second"
         else:
                if ((totmarks>=120) and (totmarks<=149)):
                     grade ="Passed in Third"
# Display Marks Report
print("*"*50)
print("\t S T U D E N T M A R K S R E P O R T:")
print("*"*50)
print("\tStudent Number:{}".format(stno))
print("\tStudent Name:{}".format(sname))
print("\tStudent Marks in C:{}".format(cm))
print("\tStudent Marks in CPP:{}".format(cppm))
print("\tStudent Marks in Python:{}".format(pytm))
print("*"*50)
print("\tStudent total marks:{}".format(totmarks))
print("\tStudent Percentage of Marks:{}".format(percentmarks))
print("\tStudent Result:{}".format(grade))
print("*"*50)