#program for swappning any value with multiline assignment
#swap.py
a = input("Enter value of a : ")
b = input("Enter value of b : ")
print("="*40)
print("Original value of a = {}".format(a))
print("Original value of a = {}".format(b))
print("="*40)
#swappnig Logic
a,b=b,a
print("swapped value of a = {}".format(a))
print("swapped value of b = {}".format(b))
print("="*40)