my_list = input('Enter elements: ').split()
my_tuple = tuple(my_list)
dupl = []
uniq = []

for i in range(len(my_tuple)):
    for j in range(i + 1, len(my_tuple)):
        if my_tuple[i] in dupl:
            break
        if my_tuple[i] == my_tuple[j]:
            dupl.append(my_tuple[i])
            break

for i in my_list:
    if i not in dupl:
        uniq.append(i)

print('Duplicate elements:', tuple(dupl))
print('Unique elements:', tuple(uniq))

