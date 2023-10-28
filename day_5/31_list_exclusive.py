list1 = input('Enter number list1: ').split()
list2 = input('Enter number list2: ').split()

new_list = [n for n in list2 if n not in list1]
print(new_list)
