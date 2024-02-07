lb = int(input("Enter lower limit: "))
ub = int(input("Enter upper limit: "))
s = 0
for i in range(lb, ub + 1):
    c = 0
    for j in range(1, i + 1):
        if i % j == 0:
            c += 1
            if c > 2:
                break
    if c == 2:
        s += i
print("Sum is:", s)
