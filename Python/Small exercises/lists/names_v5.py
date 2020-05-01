import collections
letters = []
with open('names.txt', 'r') as f:
    myNames = [line.strip() for line in f]
    for name in myNames:
        letters.append(name[0])
    print(letters)
    print(f"Here is the most common first letter and it's count: {collections.Counter(letters).most_common()[0]}")
    print(f"Here is the least common first letter and it's count: {collections.Counter(letters).most_common()[-1]}") 