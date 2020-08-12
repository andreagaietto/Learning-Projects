def speak(animal = "dog"):
    """

    >>> speak("dog")
    'woof'
    >>> speak("pig")
    'oink'
    """


    if animal == "pig":
        return "oink"
    elif animal == "duck" :
        return "quack"
    elif animal == "cat":
        return "meow"
    elif animal == "dog":
        return "woof"
    else:
        return "?"

print(speak())
print(speak("cat"))