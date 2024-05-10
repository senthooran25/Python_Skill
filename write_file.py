def dic_return():
    marks_file = open('testwrite.txt', 'r')
    marks_list = marks_file.readlines()
    smark_list =[]
    # print(marks_list)
    dic_out = {}
    for line in marks_list:
        sline = line.strip('\n')
        smark_list.append(sline)
    # print(smark_list)
    for std_info in smark_list:
        # print(std_info)
        std_name = std_info.split(',')
        marks =[]
        for i in range(1, len(std_name)):
            key = std_name[0]
            m1 = std_name[i]
            marks.append(m1)
        dic_out[key] = marks
    print(dic_out)
        # print("name is :", key)
        # print("marks is :", marks)
dic_return()