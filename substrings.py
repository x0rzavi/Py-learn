line = str(input('Enter string: '))
line_len = len(line)
for i in range(line_len):
    for j in range(1, line_len + 1):
        sub_str = line[i : i + j]
        if len(sub_str) != j:
            break
        else:
            print(sub_str)

