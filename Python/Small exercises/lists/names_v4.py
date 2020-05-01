import collections
with open('names.txt', 'r') as f:
    myNames = [line.strip() for line in f]
    lst = [x.upper() for x in myNames]
    for name in lst:
        print(f"{name} = {collections.Counter(name).most_common(1)[0]}")
        