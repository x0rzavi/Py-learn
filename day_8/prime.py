def prime(n):
    c = 0
    for i in range(2, n + 1):
        if n % i == 0:
            c += 1
            if c > 1:
                break

    if c == 1:
        return 1
    else:
        return 0
