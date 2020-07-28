def extract_full_name(names):
    return list(map(lambda x: x['first'] + " " + x['last'], names))




names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]

print(extract_full_name(names))