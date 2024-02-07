my_list = input("Enter elements: ").split()
my_tuple = tuple(my_list)
freq = {}

for i in range(len(my_tuple)):
    c = 0
    for j in range(len(my_tuple)):
        if my_tuple[i] == my_tuple[j]:
            c += 1
    freq[my_tuple[i]] = c

print(freq)
