src_file = input("Enter file name to open: ")
dest_file = input("Enter file name to write: ")


def copy_python_script(src_file, dest_file):
    with open(src_file, "r") as src, open(dest_file, "w") as dest:
        for line in src:
            stripped_line = line.strip()
            if not stripped_line.startswith("#"):
                dest.write(line)


copy_python_script(src_file, dest_file)
