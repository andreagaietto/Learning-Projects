def copy_and_reverse(file_name, reversed_file):
    with open(file_name, "r") as file:
        with open(reversed_file, "w") as new_file:
            data = file.read()[::-1]
            new_file.write(data)


copy_and_reverse("story.txt", "reversed.txt")