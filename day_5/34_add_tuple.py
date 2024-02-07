num_list = input("Enter elements: ").split()
num_tuple = tuple(num_list)
sum = 0

for n in num_tuple:
    sum += float(n)

print("Addition:", sum)
