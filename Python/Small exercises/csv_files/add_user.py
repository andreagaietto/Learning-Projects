from csv import writer

def add_user(first_name, last_name):
    with open("users.csv", "a", newline="") as file:
        csv_writer = writer(file)
        csv_writer.writerow([first_name, last_name])
