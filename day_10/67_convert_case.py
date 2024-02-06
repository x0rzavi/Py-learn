src_file = input("Enter file name to open: ")
dest_file = input("Enter file name to write: ")


def copy_text_data(src_file, dest_file):
    with open(src_file, "r") as src, open(dest_file, "w") as dest:
        for line in src:
            dest.write(line.upper())


copy_text_data(src_file, dest_file)
