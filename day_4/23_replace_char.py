line = str(input("Enter string: "))
last_char = line[-1]
new_str = line[:-1].replace(last_char, "*") + last_char
print("New string:", new_str)
