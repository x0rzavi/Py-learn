a = int(input("Enter a: "))
b = int(input("Enter b: "))
for i in range(1, a + 1 if a < b else b + 1):
    if (a % i == 0 and b % i == 0):
        gcd = i
print(gcd)
