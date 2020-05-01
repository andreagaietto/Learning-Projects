sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
word = ""   
for x in sounds:
    word += x

print(word.upper())

sounds.append("even")

sounds.extend(["though", "the", "sound", "of"])

print(sounds)

sounds.insert(-1, "nope")

print(sounds)

sounds.pop()

print(sounds)

sounds.pop(-1)
print(sounds)

sounds.remove("ali")

print(sounds)

print(sounds.index("even"))
