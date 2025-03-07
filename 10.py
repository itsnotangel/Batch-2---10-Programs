# Program 10: Numbers Between 2 Numbers
n1 = int(input("Enter number 1: "))
n2 = int(input("enter number 2: "))

if n1 == n2:
    print ("Equal numbers.")
elif n1 + 1 == n2 or n2 + 1 == n1:
    print ("Consecutive numbers.")
else:
    start = min (n1, n2)
    end = max (n1, n2)

    for i in range(start + 1, end):
        print (i)