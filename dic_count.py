userStr = input("enter the string :")
done = {}
lone = []
for i in userStr:
    countkey = userStr.count(i)
    done[i] = countkey
    lone.append(i)
print(done)
print(lone)