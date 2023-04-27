def is_palindrome(word):
    if word == word[::-1]:
        print("It is a palindrome",word[::-1])
    else:
        print("It is not a palindrome", word[::-1])
is_palindrome("oyo")