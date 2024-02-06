filename = input("Enter filename: ")
with open(filename) as f:
    for line in f:
        print(line.rstrip()[::-1])
