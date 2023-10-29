def count(line):
    lower = 0
    upper = 0
    for char in line:
        if char.isalpha():
            if char.islower():
                lower += 1
            if char.isupper():
                upper += 1
    return lower, upper

line = input('Enter string: ')
print('Lowercase character count:', count(line)[0])
print('Uppercase character count:', count(line)[1])
