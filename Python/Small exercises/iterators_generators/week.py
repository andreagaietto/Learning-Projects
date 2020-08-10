def week():
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    count = 0
    while count <= 6:
        yield week[count]
        count += 1

days = week()
print(next(days))
print(next(days))
print(next(days))


#can also do for day in week: yield day