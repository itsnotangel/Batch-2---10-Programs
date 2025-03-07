# --------------------------- BATCH 1 ---------------------------

# Program 1: Bigger Number Between Two Numbers
n1 = float(input("Enter number 1: "))
n2 = float(input("Enter number 2: "))

if n1 > n2:
    print (n1 , "is the bigger number")
elif n1 < n2:
    print (n2 , "is the bigger number.")
else:
    print ("Equal")

# Program 2: Equal or Not Equal

n1 = float(input("Enter number 1: "))
n2 = float(input("Enter number 2: "))

if n1 == n2:
    print ("Equal numbers")
else:
    print ("Not equal")

# Program 3: Sum of Two Numbers

n1 = float(input("Enter number 1: "))
n2 = float(input("Enter number 2: "))

sum = n1 + n2
print (sum)

# Program 4: Product of Two Numbers
n1 = float(input("Enter number 1: "))
n2 = float(input("Enter number 2: "))
product = n1 * n2
print (product)

# Program 5: Division Without Decimal
n1 = float(input("Enter number 1: "))
n2 = float(input("Enter number 2: "))

if n2 == 0:
    print ("Cannot divide by zero.")
else:
    quotient =  int (n1 / n2)
    print (quotient)

# Program 6: Raising First Number To The Second Number
n1 = float(input("Enter number 1: "))
n2 = float(input("Enter number 2: "))
raise = n1 ** n2
print (raise)

# Program 7: Sum of 10 Numbers

AllNumSum = 0

for i in range(10):
    num = float(input("Enter number " + str(i+1) + ": "))
    AllNumSum += num
    
print (AllNumSum)

# Program 8: 0-100 Even Numbers
for even in range(0, 101, 2):
    print (even)

# Program 10: All Numbers from 0-100 Except Ending in 0 
for i in range(100):
    if i % 10 !=0:
        print (i)

# --------------------------- BATCH 2 ---------------------------

# Program 1: Smaller Number Between Two Numbers
n1 = float(input("Enter number 1: "))
n2 = float(input("Enter number 2: "))

if n1 > n2:
    print (n2 , "is the smaller number.")
elif n1 < n2:
    print (n1 , "is the smaller number.")
else:
    print ("Equal")

# Program 2: Equal or not Equal
n1 = float(input("Enter number 1: "))
n2 = float(input("Enter number 2: "))

if n1 == n2:
    print ("Equal numbers")
else:
    print ("Not euqal numbers")

# Program 3: Difference of Two Numbers
n1 = float(input("Enter number 1: "))
n2 = float(input("Enter number 2: "))
difference = n1-n2
print (difference)

# Program 4: Quotient of Two Numbers Without the Decimal Point
n1 = float(input("Enter number 1: "))
n2 = float(input("Enter number 2: "))

if n2 == 0:
    print ("Indeterminate")
else:
    quotient = int(n1 // n2)
    print (quotient)

# Program 5: Remainder of Two Numbers
n1 = float(input("Enter number 1: "))
n2 = float(input("Enter number 2: "))

if n2 == 0:
    print ("Division by zero is not allowed.")
else:
    remainder = n1 % n2
    print (remainder)

# Program 6: First Number Minus The Remaining
n1 = float(input("Enter number 1: "))
minuend = n1

for i in range(9):
    num = float(input("Enter number " + str(i + 1) + ": "))
    minuend -= num

print (minuend)

# Program 7: Even From 10 Numbers
even = 0

for i in range(10):
    num = int(input("Enter number " + str(i+1) + ": "))
    if num % 2 == 0:
        even += 1
    
print (even)

# Program 8: [While Loop] odd numbers from 1-100
odd = 1

while odd < 100:
    print (odd)
    odd += 2

# Program 9: Number from 1-100 Except Ending in [0, 5]
for i in range(100):
    if i % 10 !=0 and i % 10 !=5:
        print (i)

# Program 10: Numbers Between 2 Numbers
n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))

if n1 == n2:
    print ("Equal")
elif n1 + 1 == n2 or n2 + 1 == n1:
    print ("Consecutive")
else:
    start = min (n1, n2)
    end = max (n1, n2)

    for i in range (start +1, end):
        print (i)
