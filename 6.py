n1 = float(input("Enter number 1: "))

total = n1
for i in range(9):
    num = float(input("Enter number " + str(i+2) + ": "))
    total -= num
print (total)