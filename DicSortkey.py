""""Write a function that accepts a dictionary as input
which contains the names and grades of students
(The keys are student names and the values are lists of grades for 3 exams
(1 Dimensional list)) and returns the list of names for
those students whose grade on all three exams is greater than or equal to 78."""
def DisinctionStudent ():
    student_dict = {"kumar": [78, 89, 97], "Ravi": [69, 84, 75], "Raj": [78, 48, 95], "Sana": [49, 98, 94]}
    student_name = list(student_dict.keys())
    name = []
    print(student_name)
    for i in student_name:
        marks = student_dict[i]
        # print(marks)
        for m in marks:
            # print(m)
            if m < 77:
                continue
                name.append(i)
            # else:

    print("name :", name)

DisinctionStudent()

input_dic ={}
def sort_val_dictionary():
    val = input_dic.values()
    skeys = list(val)
    skeys.sort()
    print(skeys)