def capitalize(to_capitalize):
    """

    >>> capitalize("boom")
    'Boom'

    >>> capitalize(5)
    Traceback (most recent call last):
        ...
    AttributeError: 'int' object has no attribute 'capitalize'
    """
    return to_capitalize.capitalize()
    
