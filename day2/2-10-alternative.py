# import json
import time

"""There are 3 methods compared. Bubble Sort is slow for this type of task.
    Better to use sorted() to sort list.
"""


students = []
secondHighestMark = 0


def bubble_sort(arr):
    len_arr = len(arr)
    start = 0
    end = 0
    mark = 0
    check = 2
    j = 0
    s = 0
    tem = True
    while True:
        # tem = True
        # if s == 0:
        #     # print("1")
        #     for i in range(0, len(arr) - j - 1):
        #         if arr[i][1] > arr[i + 1][1]:
        #             tem = False
        #             arr[i], arr[i + 1] = arr[i + 1], arr[i]
        #     if tem == True and s == 0:
        #         s = 1
        if j == 0:
            mark = arr[len(arr) - 1][1]

        if mark != arr[len_arr - j - 1][1]:
            mark = arr[len_arr - j - 1][1]
            check -= 1
            if start == 0 and check == 1:
                start = len_arr - j - 1
            elif end == 0 and check == 0:
                end = len_arr - j - 1
                break
        j += 1
    return arr[end + 1:start + 1]


def find_secondHIghestMarks(information):
    high = information[0][1]
    sec_high = 0
    k = 0
    for i, j in information:
        if j > high:
            if k != 0:
                sec_high = high
            else:
                k += 1
            high = j
        elif sec_high < j < high:
            k += 1
            sec_high = j
    return sec_high


def find_secondHIghestMarks2(information):
    arr = []
    number = 2
    for i, j in information:
        if j not in arr:
            arr.append(j)
    arr.sort()
    return arr[len(arr) - number]


try:
    inp = int(input("Enter the number of students : "))
    # storing data of the student
    for i in range(inp):
        name = input("Enter name : ")
        marks = int(input("Enter marks : "))
        students.append([name, marks])

    # Fetch data from json files
    # with open("temp-test-2-10.json", "r") as f:
    # students = json.load(f)

    # Use Bubble Sort by passing list without sort or pass a sorted list and remove sorting algorithm.
    t1 = time.time()
    studen = sorted(students, key=lambda k: k[1])
    students2 = bubble_sort(studen)
    # students2 = bubble_sort(students)
    t2 = time.time()
    print(t2 - t1)
    print("bubble=", students2)

    # Get Second Highest Marks with track of 2 variables. Cannot usable for 3rd,4th Highest marks
    ad = []
    t1 = time.time()
    secondHighestMark = find_secondHIghestMarks(students)
    # printing students who got second highest marks
    for i in students:
        if i[1] == secondHighestMark:
            ad.append(i)
    t2 = time.time()
    print(t2 - t1)
    print(ad)

    # Dynamic Highest mark chain with track of a list
    ad2 = []
    t1 = time.time()
    secondHighestMark2 = find_secondHIghestMarks2(students)
    # printing students who got second highest marks
    for i in students:
        if i[1] == secondHighestMark2:
            ad2.append(i)
    t2 = time.time()
    print(t2 - t1)
    print(ad2)
    print(len(students))


except ValueError:
    print("Enter valid information")
