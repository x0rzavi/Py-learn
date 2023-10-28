num_list = input('Enter number list: ').split()
num_list = [int(n) for n in num_list]
odd_nums = [n for n in num_list if n % 2 != 0]
new_list = []

for i in odd_nums:
    for j in odd_nums:
        new_list.append([i, j])

print(new_list)
