"""
line = str(input('Enter string: ')).lower()
line_len = len(line)
for i in range(int(line_len / 2)):
    if line[i] != line[line_len - i - 1]:
        print('Not palindrome')
        exit()
print('Palindrome')
"""

line = str(input('Enter string: ')).lower()
if line == line[::-1]:
    print('Palindrome')
else:
    print('Not Palindrome')
