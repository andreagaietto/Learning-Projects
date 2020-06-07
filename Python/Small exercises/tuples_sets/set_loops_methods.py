months = ("January", "Febuary", "March", "April")
for month in months:
    print(month)

i = len(months) - 1
while i >= 0:
    print(months[i])
    i -= 1

print(months.count("April"))

nums = (1, 2, 3, (4,5), 6, 7)
print(nums[3])
print(nums[3][1])