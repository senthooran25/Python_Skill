def over70():
    stdfile = open('stdentmarks.txt', 'r+')
    marklist = stdfile.readlines()
    print(marklist)
    out_dic = {}
    for i in marklist:
        name, math, physics, chemistry, biology = i.strip('\n').split(',')
        if int(math) > 70 and int(chemistry) > 70:
            out_dic[name] = math, physics, chemistry, biology
    print("result :", out_dic)



over70()