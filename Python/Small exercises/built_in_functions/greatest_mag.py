def max_magnitude(iterable):
    new_list = [abs(x) for x in iterable]
    max_mag = max(new_list)
    return max_mag



max_num = max_magnitude([300, 20, -900])
print(max_num)

# easier code for same item = def max_magnitude(nums):
    #return max(abs(num) for num in nums)