# Program: Printing The Smaller Number

n1 = float(input("Enter number 1: "))
n2 = float(input("Enter number 2: "))

if n1 > n2:
    print (n2, "is the smaller number")
elif n1 < n2:
    print (n1, "is the smaller number.")
else:
    print ("Equal numbers")