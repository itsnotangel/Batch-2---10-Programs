# Program: Quotient of Two Numbers Without The Decimal

n1 = float(input("Enter number 1: "))
n2 = float(input("Enter nummber 2: "))

if n2 == 0:
    print ("Indeterminate")
else:
    quotient = int(n1 // n2)
    print (quotient)