#sortnamescompare.py
print("Enter Number of names seprated by Space: ")
names = [val for val in input().split()]
print("-------------------------------------------")
print("Given names")
print("-------------------------------------------")
for name in names:
          print(name)
print("-------------------------------------------")
names.sort(reverse=True)
print("Sorted Names-- Ascending order:")
print("-------------------------------------------")
for name in names:
      print(name)
print("-------------------------------------------")