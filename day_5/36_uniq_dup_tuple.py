my_list = input("Enter elements: ").split()
my_tuple = tuple(my_list)
dupl = []
uniq = []

for element in my_tuple:
    if element in uniq:
        dupl.append(element)
    else:
        uniq.append(element)

uniq = [x for x in uniq if x not in dupl]

print("Duplicate elements:", tuple(dupl))
print("Unique elements:", tuple(uniq))
