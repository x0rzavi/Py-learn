# series: 1,1,2,3,4,9,8,27,16,81,32,243,64,729,128,2187...
def nth_term(n):
    if n % 2 == 0:
        return 3 ** ((n // 2) - 1)
    else:
        return 2 ** (n // 2)


n = int(input("Enter n: "))
print(nth_term(n))
