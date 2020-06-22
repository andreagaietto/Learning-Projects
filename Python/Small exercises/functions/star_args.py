def sum_all_nums(*args):
    
    print(sum(args))

#returns a tuple

sum_all_nums(1, 2, 3, 4)

sum_all_nums(1, 2)

# can also do something like (num1, *args)
# also doesn't have to be named args, can be something else