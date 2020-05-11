cat = {
    "name": "blue", "age": 3.5, "isCute": True
}
# tests for the presence of a key only
if "name" in cat:
    print(cat["name"])
else:
    print("No name here")

if 3.5 in cat.values():
    print("yes")
else:
    print("no")