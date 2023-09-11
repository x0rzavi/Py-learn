line = str(input('Enter string: ')).lower()
length = len(line)
for i in range(0, int(length / 2)):
    if line[i] != line[length - i - 1]:
        print('Not palindrome')
        exit()
print('Palindrome')
