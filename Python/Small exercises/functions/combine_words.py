def combine_words(word, **kwargs):
        for command, letters in kwargs.items():
            if command == "suffix":
                print(f"{word}{letters}")
            elif command == "prefix":
                print(f"{letters}{word}")
            else:
                print(f"{word}")
                

combine_words("child", prefix="man")

#def combine_words(word,**kwargs):
 #   if 'prefix' in kwargs:
  #      return kwargs['prefix'] + word
   # elif 'suffix' in kwargs:
    #    return word + kwargs['suffix']
    #return word

    #can also do above way