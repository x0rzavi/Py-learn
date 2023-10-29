numbers = input('Enter numbers: ').split()
numbers = [int(n) for n in numbers]
is_bigger = lambda x, y: x if x > y else y
max = numbers[0]
for n in numbers:
    max = is_bigger(n, max)

print('Maximum number:', max)
