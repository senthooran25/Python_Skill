"""Reversed and Case Swapped
 input_string = "Hello Python World"
 out put ="DLROw NOHTYp OLLEh"""
def reverse_sentence():
    sentence = input("Enter the sentence : ")
    words = sentence.split()
    rwords = ""
    print("words  :", words)
    for i in words:
        i = i[::-1]
        rwords = i+" "+rwords
    print(rwords.swapcase(), " ")


reverse_sentence()