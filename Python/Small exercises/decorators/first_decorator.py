def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a nice day!")
    return wrapper

@be_polite
def greet():
    print("My name is Matt.")



#previously used these
#greet = be_polite(greet)
#print(greet())


#adding the @be_polite means we can just do this:
print(greet())