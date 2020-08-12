#can write tests for functions inside of the docstring
#lets you supply the test and expect result from running that test
#will return None if test passes as expected
#can run via command line, for example:
# python -m doctest -v doctests(or file name).py
#very picky, expects all strings to have single quotes, everything must be exact, also be careful of trailing whitespace, order of keys in dict matters
def add(x, y):
    """add together x and y

    >>> add(1, 2)
    3

    >>> add(8, "hi")
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """

print(add(1, 2))
print(add(8, "hi"))