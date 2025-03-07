num1, num2 = sorted(map(float, input("Enter two numbers: ").split()))
print(*[i for i in range(int(num1) + 1, int(num2))])
