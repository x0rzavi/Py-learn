from palindrome import palindrome

line = input('Enter string: ').lower()
if palindrome(line):
    print('Palindrome')
else:
    print('Not Palindrome')

