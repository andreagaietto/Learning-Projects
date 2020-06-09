def return_day(day_of_week):
    week_days = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday", 7: "Saturday" 
    }
    if day_of_week in week_days:
        return week_days[day_of_week]
    else:
        return None

print(return_day(10))