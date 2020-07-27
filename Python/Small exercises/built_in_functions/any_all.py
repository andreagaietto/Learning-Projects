# all returns True if all elements of an interable are truthy, or if the iterable is empty

all([char for char in 'eio' if char in 'aeiou'])

# any returns True if any iterable of the element is truthy. If element is empty, returns False

def is_all_strings(lst):
    return all([type(l) == str for l in lst])