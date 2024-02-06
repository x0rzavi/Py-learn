filename = input("Enter filename: ")
with open(filename) as f:
    count = 0
    for line in f:
        words_line = line.rstrip().split()
        count += len(words_line)
print(f"Word Count: {count}")
