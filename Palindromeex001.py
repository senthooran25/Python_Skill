"""Write a function that takes a string consisting
of alphabetic characters as input argument and returns True
if the string is a palindrome. A palindrome is a string
which is the same backward or forward. Note that capitalization
 does not matter here i.e. a lower case character can be considered
the same as an upper case character."""

def palindrome_name():
    word = input("Enter the word :")
    list_word = list(word)
    print(list_word)
    rword = ""
    list_word.reverse()
    print(list_word)
    rword = ''.join(list_word)

    if word == rword:
        print("The word is", word, "palindrome")
    else:
        print("The word is", word, "NOT palindrome")



palindrome_name()


