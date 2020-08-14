#dictwriter creates a writer object for writing using dictionaries
#fieldnames = kwarg for the DictWriter specifying headers
#writeheader - method on a writer to write header row
#writerow - method on a writer to write a row based on a dictionary

"""from csv import DictWriter
with open("example.csv", "w") as file:
    headers = ["Character", "Move"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "Character": "Ryu",
        "Move": "Hadouken"
    })"""

from csv import DictReader, DictWriter

def cm_to_in(cm):
    return float(cm) * 0.393701

with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    fighters = list(csv_reader)

with open("inches_fighters.csv", "w", newline="") as file:
    headers = ("Name", "Country", "Height")
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    for f in fighters:
        csv_writer.writerow({
            "Name": f["Name"],
            "Country": f["Country"],
            "Height": cm_to_in(f["Height (in cm)"])
        })



"""On top of a Carriage Return (CR) by default csv adds a Line Feed (LF) to each row in this example. So when you import the same file again it gets butchered.

Instead add the newline parameter with an empty string to the open() function:

with open("users.csv", "w", newline="") as file: 

That way, only Carriage Returns are added after each row is written."""