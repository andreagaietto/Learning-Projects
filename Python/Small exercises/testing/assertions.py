#assert accepts an expression
#returns None if expression is truthy
#returns AssertionError if the expression is falsy
#accepts optional error message as a second argument
#better options now available
#not a function, is a statement (no parens)
# if run with the -O (letter O) flag, assertions will not be evaluated

#def add_positive_numbers(x,y):
    #assert x > 0 and y > 0, "Both numbers must be positive!"
    #return x + y


def eat_junk(food):
    assert food in ["pizza", "ice cream", "candy"], "Food must be a junk food"
    return f"I am eating {food}"

#print(add_positive_numbers(1, 1))
#print(add_positive_numbers(1, -1))
print(eat_junk("pizza"))
print(eat_junk("cake"))


