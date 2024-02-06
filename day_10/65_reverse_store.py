filename_read = input("Enter filename to read: ")
filename_write = input("Enter filename to write: ")
with open(filename_write, "w") as fw:
    with open(filename_read) as fr:
        for line in fr:
            fw.write(line.rstrip()[::-1])
            fw.write("\n")
