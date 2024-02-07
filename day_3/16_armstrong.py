n = int(input("Enter number: "))
nc = n
s = 0
len = len(str(n))
while n != 0:
    d = n % 10
    s += d**len
    n //= 10
if s == nc:
    print("Armstrong number")
else:
    print("Not Armstrong number")
