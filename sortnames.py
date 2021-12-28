#sortnames.py
n =int(input("Enter how many names you have: "))
if(n<=0):
   print("{} invalid input".fornmat(n))
else:
      l = list()
      print("------------------------------------------------")
      print("Enter names {}".format(n))
      print("------------------------------------------------")
      for i in range(1,n+1):
           name=input()
           l.append(name)
      else:
            print("------------------------------------------------")
            print("Given Names: ".format(n))
            print("------------------------------------------------")
            for name in l:
                print("name")
            print("------------------------------------------------")
            l.sort()
            print("Sorted Names in Ascending Order: ")
            print("------------------------------------------------")
            for name in l:
                print(name)
            print("------------------------------------------------")
            l = l[::-1]
            print("Sorted names in descending order: ")
            print("------------------------------------------------")
            for name in l:
               print(name)
            print("------------------------------------------------")