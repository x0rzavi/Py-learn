line = str(input("Enter string: "))
line_len = len(line)
# for j in range(1, line_len + 1): # no of chars taken at time
#     for i in range(line_len): # iterating through chars
#         sub_str = line[i : i + j] # print + j chars at a time
#         if len(sub_str) != j: # only print if j chars are present at once
#             break
#         else:
#             print(sub_str)
for i in range(1, line_len + 1):
    for j in range(0, line_len):
        sub_str = line[j : j + i]
        if len(sub_str) == i:
            print(line[j : j + i])
