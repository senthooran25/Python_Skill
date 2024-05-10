def mean_median(mytup):
    mylist = list(mytup)
    mylist.sort()
    # print(mylist)
    mean = sum(mylist)/len(mylist)
    # print(mean)
    if len(mylist) % 2 == 0:
        i = int(len(mylist)/2)
        median = (mylist[i-1] + mylist[i])/2
        # print("meadian ", median)
    else :
        j = len(mylist)//2
        median =(mylist[j+1])/2
        # print(median)
    return mean, median

x = (3, 3, 0, 1, 12, 13, 15, 16)

a,b = mean_median(x)
print(a, b)

