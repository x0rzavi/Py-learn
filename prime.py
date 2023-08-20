n = int(input("Enter number: "))
c = 0
for i in range(2, n + 1):
    if (n % i == 0):
        c += 1
        if (c > 1):
            print("Number is not Prime")
            exit()
if (c == 1):
    print("Number is Prime")
