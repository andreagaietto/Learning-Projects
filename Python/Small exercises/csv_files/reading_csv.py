#can be read like any other text file, however, there are python modules dedicated to this that are better options


#reader- lets you iterate over rows of the csv as lists
#DictReader-let's you iterate over rows of the CSV as OrderedDicts
"""from csv import reader
with open("fighters.csv") as file:
    csv_reader = reader(file)
    next(csv_reader) #skips one row and eliminates the header
    for fighter in csv_reader:
        print(f"{fighter[0]} is from {fighter[1]}") #this is an iterator, if you try and call it again you will only get one copy
        #each row is a list!
        #print(row)"""


"""#to get a list
from csv import reader
with open("fighters.csv") as file:
    csv_reader = reader(file)
    data = list(csv_reader)
    print(data)"""

#using DictReader
from csv import DictReader
with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        #each row is an OrderedDict!
        print(row)


#can accept a delimiter kwarg in case your data isn't separated by commas
#csv_reader = reader(file, delimiter="|")