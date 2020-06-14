def single_letter_count(word, letter):
    letter_count = word.lower().count(letter.lower())
    if letter_count == 0:
        return 0
    else:
        return letter_count