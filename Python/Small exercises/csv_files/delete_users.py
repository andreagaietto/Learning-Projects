from csv import reader, writer
def delete_users(first, last):
    change_count = 0
    with open("users.csv") as file:
        csv_reader = reader(file)
        data = list(csv_reader)
        for row in data:
            if row[0] == first and row[1] == last:
                data.remove(row)
                change_count += 1
        with open("users.csv", "w", newline="") as file:
            csv_writer = writer(file)
            for row in data:
                csv_writer.writerow(row)
        return change_count

print(delete_users("Grace", "Hopper"))
