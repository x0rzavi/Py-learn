list1 = input('Enter list1: ').split()
list2 = input('Enter list2: ').split()

for n in list2:
    if n not in list1:
        list1.append(n)

print('List union:', list1)
