""" when your function is called as:
n_letter_dictionary("The way you see people is the way you treat them and the Way you treat them is what they become")
Then, your function should return a dictionary such as
{2: ['is'], 3: ['and', 'see', 'the', 'way', 'you'], 4: ['them', 'they', 'what'], 5: ['treat'], 6: ['become', 'people']}"""

def n_letter_dictionary_final_sp(my_string):
    my_dict = {}
    my_list = my_string.strip().split()
    for word in my_list:
        length=len(word)
        lowered_word=word.lower()
        if my_dict.get(length):
            if lowered_word not in my_dict[length]:
                my_dict[length].append(lowered_word)
                my_dict[length].sort()
        else:
            my_dict[length]=[lowered_word]
    return my_dict

x = "see way you see"
y = n_letter_dictionary_final_sp(x)
print(y)