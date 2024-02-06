def copy_binary_data(src_file, dest_file, length=100):
    with open(src_file, "rb") as src, open(dest_file, "wb") as dest:
        dest.write(src.read(length))


copy_binary_data("src.bin", "dest.bin")
