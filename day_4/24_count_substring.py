line = str(input("Enter string: "))
sub_str = str(input("Enter substring: "))
line_len = len(line)
sub_str_len = len(sub_str)

count = 0
# for i in range(0, line_len, sub_str_len): # non overlapping
for i in range(line_len):  # overlapping
    if line[i : i + sub_str_len] == sub_str:
        count += 1
print(f"No of occurrences: {count}")
