#def my_for(iterable):
    #iterator = iter(iterable)
    #while True:
        #try:
            #print(next(iterator))
        #except StopIteration:
            #break

#for example func could be print or any other thing like squaring etc
def my_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            thing = next(iterator)
        except StopIteration:
            break
        else:
            func(thing)