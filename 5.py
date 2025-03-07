# Program 5: Remainder of Two Numbers

n1 = float(input("Enter number 1: "))
n2 = float(input("Enter number 2: "))

if n2 == 0:
    print ("Cannot divide by zero.")
else:
    remainder = n1 % n2
    print (remainder)