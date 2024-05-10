"""Write a function that accepts a dictionary as input and returns a sorted list of all the keys in the dictionary.
Code Editor1"""
def sort_dictionary():
    input_dic = {"zname1": "kumar", "sname2": "Ravi", "wname3": "Amir", "gname4": "Dinesh", "yname5": "Niru", "cname6": "Sentho"}
    keys = input_dic.keys()
    skeys = list(keys)
    skeys.sort()
    print("sorted keys :",skeys)

    values2 = input_dic.values()
    print("Values :", values2)

    items1 = input_dic.items()
    print("Items :", items1)


sort_dictionary()