a = int(input("Enter a: "))
b = int(input("Enter b: "))
temp = b
b = a
a = temp
print("a is:", a)
print("b is:", b)

print("\n")

a = int(input("Enter a: "))
b = int(input("Enter b: "))
a, b = b, a
print("a is:", a)
print("b is:", b)
