list1 = input("Enter list1: ").split()
list2 = input("Enter list2: ").split()

new_list = [n for n in list1] + [n for n in list2]
print("Concatenated list:", new_list)
