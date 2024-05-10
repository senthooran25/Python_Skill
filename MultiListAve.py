# tudent_marks =[["kumar","65.78,88"],["ravi,55,75,56"],["Raj",45,65,44]]

def sum_2D_list(list1):
    # total = 0
    # num = 0
    ev1 = 0
    ev2 = 0
    for i in range(0, len(list1)):
        for j in range(0, len(list1[i])):
            if j % 2 == 0:
                ev1 = list1[i][j]
                print(ev1)
                if ev1 < ev2:
                    ev1 = ev2
    print(ev2)


a = [[77, 87, 55, 34], [56, 90, 89, 90], [45, 78, 65, 48], [65, 95, 25, 75], [45, 65, 74, 52]]
sum_2D_list(a)
