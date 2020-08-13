def copy(file_name, new_file_name):
    with open(file_name, "r") as read_file:
        with open(new_file_name, "a") as write_file:
            new_line = read_file.read()
            write_file.write(new_line)



copy("story.txt", "copy.txt")
