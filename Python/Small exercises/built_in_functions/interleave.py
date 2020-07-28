def interleave(string1, string2):
    zipped_strings = list(zip(string1, string2))
    joined_strings = [''.join(x) for x in zipped_strings]
    final = ''.join(joined_strings)
    return(final)



interleave('hi', 'ha')

#better solution, one line
#def interleave(str1,str2):
    #return ''.join(''.join(x) for x in (zip(str1,str2)))