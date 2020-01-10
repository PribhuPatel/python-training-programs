students = []
secondHighestMark = 0


def find_secondHIghestMarks(information):
    high = 0
    sec_high = 0
    high = information[0][1]
    sec_high = 0

    for i, j in information:
        if sec_high < j < high:
            sec_high = j
            # high = j
        elif high < j:
            high = j
    return sec_high


try:
    inp = int(input("Enter the number of students : "))
    # storing data of the student
    for i in range(inp):
        name = input("Enter name : ")
        marks = int(input("Enter marks : "))
        students.append([name, marks])
    secondHighestMark = find_secondHIghestMarks(students)

    # printing students who got second highest marks
    for i in students:
        if i[1] == secondHighestMark:
            print(i[0])

except ValueError:
    print("Enter valid information")
