cat = {
    "name": "blue", "age": 3.5, "isCute": True
}
print(cat)

for value in cat.values():
    print(value)

for v in cat.keys():
    print(v)

for val in cat.items():
    print(val)

for key, valu in cat.items():
    print(key, valu)



cat2 = dict(name="kitty")
print(cat2)

print(cat["name"])