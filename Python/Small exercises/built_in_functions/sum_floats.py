def sum_floats(*args):
    result = sum(list(filter(lambda x: isinstance(x, float), args)))
    return result


print(sum_floats(1, 2, 3, 4, 5))

#another way
#def sum_floats(*args):
    #return sum(arg for arg in args if type(arg) == float)