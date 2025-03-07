EvenTotal = 0

for i in range(10):
    num = float(input("Enter number " + str(i+1) + ": "))
    if num % 2 == 0:
        EvenTotal += 1

print (EvenTotal)