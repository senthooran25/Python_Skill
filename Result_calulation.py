def my_final_grade_calculation(filename):
    std_file = open(filename, 'r')
    std_list = std_file.readlines()
    print(std_list)
    std_name = []
    std_quizs = []
    result_dic = {}

    for std_one in std_list:
        std_one_list = std_one.strip('').split(',')
        std_name = std_one_list[0]
        print(std_name)
        std_quizs = std_one_list[1:7]
        std_quizs_int = sorted(list(map(int, std_quizs)))
        print("Quizs Marks 6 :",std_quizs_int )

        std_assig = std_one_list[7:11]
        std_assig_int = sorted(list(map(int,std_assig)))
        print("Assigment marks :", std_assig_int)

        std_mid = int(std_one_list[11])
        print("Mid term Mark :",std_mid)

        std_fin = int(std_one_list[12])
        print("Final mark :", std_fin)

        tot_mark = ((sum(std_quizs_int[2:6])/4)*0.25) + ((sum(std_assig_int[1:4])/3)*0.25) + (std_mid * 0.25) + (std_fin * 0.25)
        print("Total :", tot_mark)

        if tot_mark > 60:
            res = "Pass"
        else:
            res = "Fail"
        result_dic[std_name] = res
    print("Result Dic :", result_dic)



 # std_file.close()

a = "stdentmarks.txt"
my_final_grade_calculation(a)
