#pop take a single argument coresponding to a key and removed the key-value pair from the dictionary. Returns the value corresponding to the key that was removed
d = dict(a=1, b=2, c=3, d=4, e=5)
value = d.pop('a')
print(value)
print(d)

#popitem removes a random key from the dictionary
val = d.popitem()
print(val)
print(d)

#update updates keys and values in a dictionary with another set of key value pairs

first = dict(a=1, b=2, c=3, d=4, e=5)
second = {}

second.update(first)
print(second)

#can also overwrite an existing key
second['a'] = "AMAZING"
print(second)

second.update(first)
print(second)