num_list = input('Enter number list: ').split()
num_list = [int(n) for n in num_list] # convert elements to int for proper comparison

min_num = num_list[0]
max_num = num_list[0]
for num in num_list:
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num

print('Minimum number is:', min_num)
print('Maximum number is:', max_num)
