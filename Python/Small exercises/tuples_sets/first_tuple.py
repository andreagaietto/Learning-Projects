first_tuple = (1, 2, 3, 3, 3)
print(first_tuple[1])

locations = {
    (35.6895, 39.6917): "Tokyo Office",
    (40.7128, 74.0060): "New York Office"
}
print(locations)

print(locations[(40.7128, 74.0060)])

cat = {
    "name": "biscuit", "age": 0.5, "favorite toy": "catnip"
    }
print(cat.items())