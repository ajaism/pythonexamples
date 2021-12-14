#matchcaseex2.py
wkno = input("Enter week Name: ")
match wkno[0:3].lower():
       case "mon"|"tue"|"wed"|"thr"|"fri":
                    print("its working".format(wkno))
       case "sun":
                    print(" its a Holiday".format(wkno))
       case "sat":
                    print("its a week end".format(wkno))
       case _:
                    print("its not a week number ----learn weeks")
print("Program is over")