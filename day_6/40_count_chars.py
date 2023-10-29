line = input('Enter string: ')
count = {}

for i in range(len(line)):
    c = 0
    if line[i].isalpha():
        for j in range(len(line)):
            if line[i] == line[j]:
                c += 1
        count[line[i]] = c

print(count)
