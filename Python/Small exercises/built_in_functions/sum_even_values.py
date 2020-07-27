def sum_even_values(*args):
    evens_list = [x for x in args if x%2 == 0]
    if len(evens_list) != 0:
        return sum(evens_list)
    else:
        return 0


answer = sum_even_values(1)
print(answer)

#can be done in one line!
#def sum_even_values(*args):
    #return sum(arg for arg in args if arg % 2 == 0)