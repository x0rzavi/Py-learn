line = str(input('Enter string: '))
sub_str = str(input('Enter substring: '))
line_len = len(line)
sub_str_len = len(sub_str)

i = c = 0
while i < line_len:
    i = line.find(sub_str, i) # start finding from position & save position
    if i == -1:
        break
    else:
        c += 1
        # i += sub_str_len # Non-overlapping
        i += 1 # Overlapping
print('No of occurences:', c)
