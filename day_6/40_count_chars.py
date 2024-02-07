line = input("Enter string: ")
count = {char: 0 for char in line if char.isalpha()}

for char in line:
    if char.isalpha():
        count[char] += 1

print(count)
