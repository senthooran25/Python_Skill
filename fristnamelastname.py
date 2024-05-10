# def countmilk ():
#     datafile = open('testwrite.txt', 'r')
#     list1 = datafile.readlines()
#     out_dict = {}
#     milklist1 = []
#     breadlist1 = []
#     # print("List : ", list1)
#     for i in list1:
#         # print(i)
#         key1, r1, r2, r3 = i.strip('\n').split(' ')
#         # print("Key : ", key1)
#         if key1 == 'm':
#             milklist =[r1, r2, r3]
#             milklist1.append(milklist)
#         else:
#             breadlist =[r1, r2, r3]
#             breadlist1.append(breadlist)
#     out_dict['milk'] = milklist1
#     out_dict['bread'] = breadlist1
#     print(out_dict)# def countmilk ():
# #     datafile = open('testwrite.txt', 'r')
# #     list1 = datafile.readlines()
# #     out_dict = {}
# #     milklist1 = []
# #     breadlist1 = []
# #     # print("List : ", list1)
# #     for i in list1:
# #         # print(i)
# #         key1, r1, r2, r3 = i.strip('\n').split(' ')
# #         # print("Key : ", key1)
# #         if key1 == 'm':
# #             milklist =[r1, r2, r3]
# #             milklist1.append(milklist)
# #         else:
# #             breadlist =[r1, r2, r3]
# #             breadlist1.append(breadlist)
# #     out_dict['milk'] = milklist1
# #     out_dict['bread'] = breadlist1
# #     print(out_dict)

# # countmilk()


def family_mem():
    family_data = open('famaily_Mem.txt', 'r')
    family_list = family_data.readlines()
    out_dic = {}
    listmembers = []

    # print("family list : ",family_list[1])
    for i in range(len(family_list)):
        firstname, lastname, age = family_list[i].strip('\n').split(',')
        # print("Last name  :", lastname)
        # if lastname[i] == lastname[i+1]
        #     out_dic[lastname] = firstname ,age
        for j in range(1, len(family_list)):
            firstname2, lastname2, age2 = family_list[j].strip('\n').split(',')
            if lastname == lastname2:
                listmembers =[firstname2, age2]
                listmembers.append(listmembers)
    out_dic[lastname] = listmembers
            # print("Last name 2 :", lastname2)
    print(out_dic)

    # for person in family_list:
    #     print(person)

family_mem()
