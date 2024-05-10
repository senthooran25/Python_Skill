def dic_return():
    marks_file = open('testwrite.txt', 'r')
    marks_list = marks_file.readlines()
    smark_list =[]
    # print(marks_list)
    dic_out = {}
    for line in marks_list:
        sline = line.strip('\n')
        smark_list.append(sline)
        name ,m1 ,m2,m3,m4 = line.strip().split(',')
        dic_out[name] =[float(m1),float(m2), float(m3), float(m4)]
    # return dic_out
    print(dic_out)



dic_return()