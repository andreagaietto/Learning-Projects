d = dict(a=1, b=2, c=3)
c = d.copy()
print(d)
d.clear()
print(d)
print(c)


#fromkeys can be useful for setting a bunch of keys to the same value
new_user = {}.fromkeys(["name", "score", "email"], "unknown")
print(new_user)

e = dict(a=1, b=2, c=3)
e.get("a") #will return 1
e.get("something") #will return none instead of an error (for example if you store the result of this in a variable and check if result is none, it will be true)

