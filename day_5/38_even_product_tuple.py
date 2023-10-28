num_list = input('Enter number list: ').split()
num_list = [float(n) for n in num_list]
num_tuple = tuple(num_list)
even_nums = [n for n in num_tuple if n % 2 == 0]
new_list = []

for i in even_nums:
    for j in num_tuple:
        new_list.append((i, j))

print(tuple(new_list))
