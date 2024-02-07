# r = int(input("Enter no of rows: "))
# R = range(2 * (r) - 1, 0, -2)
# k = r
# for i in R:
#     print(" " * (r-k) + "*" * (i), end = " ")
#     k = k - 1
#     print()

n = int(input("Enter no of rows: "))
for i in range(n, 0, -1):
    for j in range(1, n - i + 1):
        print("  ", end="")
    for j in range(1, 2 * i):
        print("* ", end="")
    print()
