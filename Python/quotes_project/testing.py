import datetime
try:
    day = 28
    month = 9
    year = 2020
    formatted = datetime.date(year, month, day)
    print(formatted)

except ValueError:
    print("wrong")