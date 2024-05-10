
sample = {"rabbit" : [1, 2, 3],
          "kitten" : [2, 2, 6],
          "lioness": [6, 8, 9]}
itemsam = list (sample.items())
print(itemsam)
usernum = int(input("Enter a integer :"))
for i in itemsam:
    skeys = i[0]
    svales = i[1]
    # print(skeys)
    # print(svales)
    if usernum in svales:
        print(skeys)
