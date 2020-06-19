def is_palindrome(word):
    reversed =  word[::-1]
    if word == reversed:
        return True
    else:
        return False
