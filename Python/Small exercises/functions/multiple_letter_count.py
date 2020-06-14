def multiple_letter_count(word):
    return {x: word.count(x) for x in word}
