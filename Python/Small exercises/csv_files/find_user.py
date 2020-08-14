from csv import reader
def find_user(first_name, last_name):
    with open("users.csv") as file:
        csv_reader = reader(file)
        data = list(csv_reader)
        print(data)
        for row in data:
            if row[0] == first_name and row[1] == last_name:
                return data.index(row)
        else:
            return "Not Here not found."


find_user("Oliver", "Gaietto")