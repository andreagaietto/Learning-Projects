from csv import reader, writer
def update_users(old_first, old_last, new_first, new_last):
    change_count = 0
    with open("users.csv") as file:
        csv_reader = reader(file)
        data = list(csv_reader)
        for row in data:
            if row[0] == old_first and row[1] == old_last:
                row[0] = new_first
                row[1] = new_last
                change_count += 1
        with open("users.csv", "w", newline="") as file:
            csv_writer = writer(file)
            for row in data:
                csv_writer.writerow(row)
        return change_count


print(update_users("Grace", "Hopper", "Silly", "Face"))
