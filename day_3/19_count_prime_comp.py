prime_sum = 0
comp_sum = 0
while (True):
    n = int(input("Enter number (-1 to exit): "))
    if (n == -1):
        break
    else:
        c = 0
        for i in range(1, n + 1):
            if (n % i == 0):
                c += 1
                if (c > 2):
                    comp_sum += 1
                    break
        if (c == 2):
            prime_sum += 1
print('No of prime:', prime_sum)
print('No of composite:', comp_sum)
