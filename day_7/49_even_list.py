numbers = input("Enter numbers: ").split()
numbers = [int(n) for n in numbers]
is_even = lambda n: n % 2 == 0
even_list = []

for n in numbers:
    if is_even(n):
        even_list.append(n)

print("Even numbers:", even_list)
