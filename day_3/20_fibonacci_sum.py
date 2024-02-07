def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


s = 0
for i in range(15):
    if fib(i) > 100:
        break
    else:
        if fib(i) % 2 == 0:
            s += fib(i)

print("Sum of even terms is:", s)
